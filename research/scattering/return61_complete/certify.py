"""Complete all-n color proof for the phase61 three-marker return."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A,infinite_tail
from ant_exact import W,P,D,plan,canonical_source,certify_period
N=(1,0,100);C=lambda v:(0,0,v)
def linear(a,b):return A.add(A.scale(N,a),C(b))
def main():
 mp=SRC/'manifest.json';assert hashlib.sha256(mp.read_bytes()).hexdigest()=='2cd64e957de70ed25e5ab7bb58ac87ce36765cfc6a1c234c05d65441aa8550a1'
 cp=SRC/'certificate_r61.json';assert hashlib.sha256(cp.read_bytes()).hexdigest()==json.loads(mp.read_text())['files'][cp.name];old=json.loads(cp.read_text());q1=plan(W,(0,0),2)[0][61];assert q1==(7,-2)
 q2=tuple(linear(a,b) for a,b in old['second_marker_affine']);assert q2==(linear(2,-5),linear(-2,-41))
 op,oh=old['capture_pose'];assert op==[[0,-36],[0,-19]] and oh==3 and old['tail_phase']==100
 p0,h0=plan((W[100:]+W[:100])[:4],(-36,-19),3)[2:];b72=plan(W[:72],p0,h0)[2];q3=tuple(A.add(C(v),A.scale(linear(1,7),-2)) for v in b72);assert q3==(linear(-2,-54),linear(-2,-41))
 B,p,h=canonical_source(42,0);assert len(B)==517 and p==(0,0) and h==2 and certify_period(B,p,h,W);assert q1 not in B
 assert max(x-y for x,y in D)-4*43 < -160
 assert A.no_point_collision(q2,q3) and all(A.no_point_collision(A.point(*v),q) for v in B|{q1} for q in [q2,q3])
 for k in A.STATS:A.STATS[k]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();field=A.Field([A.point(*q) for q in P]+[A.point(*q1),q2,q3]);field.add_rays([A.point(x-2,y+2) for x,y in D],(-2,2),C(42),'complete42deposits')
 base=A.point(0,0);h=2;elapsed=C(0);records=[];contacts={};path=HERE/'template.json';T=json.loads(path.read_text());std={W[j:]+W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ['finite','periods'];data=A.word_data(word,h);reads=plan(word,(0,0),h)[0];count=None if s['type']=='finite' else linear(*s['count_n']);hits={}
  for j,b in enumerate(reads):
   actual=A.translate_local(b,base,0)
   for label,target in [('q2',q2),('q3',q3)]:
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
 assert contacts=={'q2':linear(104,32634),'q3':linear(312,117727)}
 tw=T['infinite_tail_word'];assert tw in std;data=A.word_data(tw,h);assert data[3]==h and data[2]==(2,-2);tail=infinite_tail(field,data,base)
 def guard(p):
  u=A.sub(p[0],p[1]);z=A.add(p[0],p[1]);assert A.nonneg(A.add(u,C(108))) and A.nonneg(A.sub(C(65),z))
 for p in A.READ_POINTS:guard(p)
 for b,d,count in A.READ_RAYS:guard(b);guard(A.padd(b,tuple(A.scale(A.sub(count,A.ONE),v) for v in d)))
 for b in data[0]:guard(A.translate_local(b,base,0))
 assert elapsed==linear(520,263262) and base==(linear(-2,-17),linear(-2,-73)) and h==2 and tw==W
 out=dict(status='exact complete n>=100 three-marker theorem',domain='n=U+100, U>=0',initial=[A.point(*q1),q2,q3],first_contacts=contacts,capture_time=elapsed,capture_pose=[base,h],tail=tail,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),whole_future_bounds={'u_lower':-108,'z_upper':65},records=records,statistics=A.STATS.copy(),template_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),source_certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),scope='Complete42 canonical past; all older deposits and arbitrary extra history below u=-160 are protected. Remaining remote corners are treated by a fixed-m recurrence coupling.')
 (HERE/'certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
