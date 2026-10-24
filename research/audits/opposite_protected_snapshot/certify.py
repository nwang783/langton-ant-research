"""Complete two-variable finite-kernel proof for the protected three-marker cycles."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'));from bivariate import A,infinite_tail
from ant_exact import W,P,D,plan,canonical_source,certify_period
N=(1,0,100);M=(0,1,100);C=lambda v:(0,0,v)
def linear(a,b,c):return A.add(A.add(A.scale(N,a),A.scale(M,b)),C(c))
def main(r):
 assert r in [38,55,62]
 manifest=SRC/'manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='2cd64e957de70ed25e5ab7bb58ac87ce36765cfc6a1c234c05d65441aa8550a1'
 cp=SRC/f'certificate_r{r}.json';assert hashlib.sha256(cp.read_bytes()).hexdigest()==json.loads(manifest.read_text())['files'][cp.name];old=json.loads(cp.read_text())
 q1=plan(W,(0,0),2)[0][r];q2=tuple(linear(a,0,b) for a,b in old['second_marker_affine']);cp0,ch=old['capture_pose'];assert ch==1 and old['tail_phase']==0 and [v[0] for v in cp0]==[-2,-2]
 q30=plan(W[:72],tuple(v[1] for v in cp0),1)[2];q3=(linear(0,2,q30[0]),linear(0,2,q30[1]));inputs={'q2':q2,'q3':q3}
 B,p,h=canonical_source(42,0);assert len(B)==517 and p==(0,0) and h==2 and certify_period(B,p,h,W) and q1 not in B
 assert max(x-y for x,y in D)-4*43 < -160
 assert A.negative(A.sub(A.add(q2[0],q2[1]),C(min(x+y for x,y in B))))
 assert A.nonneg(A.sub(A.add(q3[0],q3[1]),C(1+max(x+y for x,y in B))))
 assert A.no_point_collision(q2,q3) and A.no_point_collision(A.point(*q1),q2) and A.no_point_collision(A.point(*q1),q3)
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();field=A.Field([A.point(*q) for q in P]+[A.point(*q1),q2,q3]);field.add_rays([A.point(x-2,y+2) for x,y in D],(-2,2),C(42),'complete42deposits')
 base=A.point(0,0);h=2;elapsed=C(0);records=[];contacts={};path=HERE/f'template_r{r}.json';T=json.loads(path.read_text());assert T['phase']==r;std={W[j:]+W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ['finite','periods'];data=A.word_data(word,h);reads=plan(word,(0,0),h)[0];count=None if s['type']=='finite' else linear(*s['count_np']);hits={}
  for j,b in enumerate(reads):
   actual=A.translate_local(b,base,0)
   for label,target in inputs.items():
    if label in contacts:continue
    if count is None:
     if actual==target:
      if label not in hits:hits[label]=A.add(elapsed,C(j))
     else:assert A.no_point_collision(actual,target)
    else:
     k=A.line_coordinate(A.psub(target,actual),data[2])
     if k is not None and A.in_range(k,count):
      t=A.add(A.add(elapsed,A.scale(k,104)),C(j));hits[label]=A.minimum(hits[label],t) if label in hits else t
  contacts.update(hits)
  if count is None:base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   assert len(word)==104 and word in std and data[3]==h and A.nonneg(A.sub(count,A.ONE));base=A.apply_periods(field,data,base,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h],contacts=hits));print(json.dumps(records[-1]),flush=True)
 assert contacts['q2']==linear(old['second_first_hit'][0],0,old['second_first_hit'][1])
 assert contacts['q3']==linear(old['capture_time'][0]+104,104,old['capture_time'][1]+72)
 tw=T['infinite_tail_word'];assert tw in std;data=A.word_data(tw,h);assert data[3]==h;tail=infinite_tail(field,data,base)
 # Complete all-parameter finite-prefix u strip, and protection of every
 # omitted older canonical deposit and arbitrary old history belowu=-160.
 us=[]
 for p in A.READ_POINTS:
  v=A.sub(p[0],p[1]);assert v[:2]==(0,0);us.append(v[2])
 for b,d,count in A.READ_RAYS:
  v=A.sub(b[0],b[1]);w=A.add(v,A.scale(A.sub(count,A.ONE),d[0]-d[1]));assert v[:2]==w[:2]==(0,0);us.extend([v[2],w[2]])
 prefix=[min(us),max(us)];tu=[];tz=[]
 for b in data[0]:
  p=A.translate_local(b,base,0);u=A.sub(p[0],p[1]);assert u[:2]==(0,0);tu.append(u[2]);tz.append(A.add(p[0],p[1]))
 assert data[2][0]-data[2][1]>=0 and min(prefix[0],min(tu))>=-160
 corners={'NW':(q2[0],q3[1]),'SE':(q3[0],q2[1])}
 assert A.negative(A.sub(A.sub(corners['NW'][0],corners['NW'][1]),C(min(prefix[0],min(tu)))))
 assert A.nonneg(A.sub(A.sub(corners['SE'][0],corners['SE'][1]),C(prefix[1]+1)))
 if data[2]==(-2,-2):assert A.nonneg(A.sub(A.sub(corners['SE'][0],corners['SE'][1]),C(max(tu)+1)))
 else:
  assert data[2]==(2,-2);cz=A.add(corners['SE'][0],corners['SE'][1]);assert all(A.nonneg(A.sub(cz,A.add(z,C(1)))) for z in tz)
 out=dict(status='exact complete finite-kernel three-marker cycle for all independent n,p>=100',phase=r,domain='n=U+100,p=V+100; U,V independent nonnegative integers',initial=[A.point(*q1),q2,q3],first_contacts=contacts,capture_time=elapsed,capture_pose=[base,h],tail=tail,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),prefix_u_bounds=prefix,whole_future_u_lower=min(prefix[0],min(tu)),unused_opposite_corners=corners,unused_corners_never_read=True,records=records,statistics=A.STATS.copy(),template_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),source_certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),scope='Arbitrary finite history belowu=-160 is protected, including the blank old history at fixed m>=100. Recurrence coupling is separately justified.')
 (HERE/f'certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
