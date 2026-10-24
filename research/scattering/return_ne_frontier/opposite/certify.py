"""Finite cap-kernel plus a remote opposite corner, all k>=100."""
import json,sys,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(HERE.parent));from discover_caps import initial
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'));from bivariate import A,infinite_tail
from ant_exact import W,plan
K=(1,0,100);C=lambda v:(0,0,v);lin=lambda a,b:A.add(A.scale(K,a),C(b))
def main(r):
 cap=next(x for x in json.loads((HERE.parent/'fixed_caps.json').read_text())['rows'] if x['phase']==r);assert cap['tail_phase']==0 and cap['drift']==[2,2];finite,p,h=initial(r);assert [list(p),h]==cap['start'];cp,ch=cap['pose'];d0=plan(W[:72],tuple(cp),ch)[2];marker=(lin(2,d0[0]),lin(2,d0[1]));field=A.Field([A.point(*q) for q in finite.changes]+[marker]);assert all(A.no_point_collision(A.point(*q),marker) for q in finite.changes)
 for b,d,lo,hi in finite.rays:
  assert lo==0 and hi is None and d==(-2,-2);field.add_rays([A.point(*b)],d,C(100),'finite_kernel');assert sum(b)-400<-250;assert not A.ray_membership(marker,A.point(*b),d,C(100))
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();base=A.point(*p);elapsed=C(0);tp=HERE/f'template_r{r}.json';T=json.loads(tp.read_text());first=None;records=[]
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ['finite','periods'];data=A.word_data(word,h);count=None if s['type']=='finite' else lin(*s['count_k_constant']);hits=[]
  if first is None:
   for j,q in enumerate(plan(word,(0,0),h)[0]):
    q=A.translate_local(q,base,0)
    if count is None:
     if q==marker:hits.append(A.add(elapsed,C(j)))
     else:assert A.no_point_collision(q,marker)
    else:
     k=A.line_coordinate(A.psub(marker,q),data[2])
     if k is not None and A.in_range(k,count):hits.append(A.add(A.add(elapsed,A.scale(k,104)),C(j)))
   if hits:first=hits[0]
   for t in hits[1:]:first=A.minimum(first,t)
  if count is None:base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   assert len(word)==104 and word in {W[j:]+W[:j] for j in range(104)} and data[3]==h and A.nonneg(A.sub(count,C(1)));base=A.apply_periods(field,data,base,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h]));print(json.dumps(records[-1]),flush=True)
 assert first==lin(104,cap['capture']+72)
 tw=T['infinite_tail_word'];assert tw in {W[j:]+W[:j] for j in range(104)};data=A.word_data(tw,h);assert data[2]==(-2,2) and data[3]==h;proof=infinite_tail(field,data,base)
 umin=10**9;umax=-10**9;zmin=10**9
 def collect(q):
  nonlocal umin,umax,zmin
  u=A.sub(*q);z=A.add(*q);assert u[:2]==(0,0) and A.nonneg(A.add(z,C(125)));umin=min(umin,u[2]);umax=max(umax,u[2]);assert z[0]>=0 and z[1]>=0;zmin=min(zmin,z[2])
 for q in A.READ_POINTS:collect(q)
 for b,d,count in A.READ_RAYS:collect(b);collect(tuple(A.add(v,A.scale(A.sub(count,C(1)),di)) for v,di in zip(b,d)))
 tail_u=[];tail_z=[]
 for q in data[0]:
  q=A.translate_local(q,base,0);collect(q);tail_u.append(A.sub(*q));tail_z.append(A.add(*q))
 assert all(z[:2]==tail_z[0][:2] for z in tail_z)
 expected={70:(lin(208,60008),((C(-14),C(29)),3),103,[-54,122],[[0,0,9],[0,0,19]]),75:(lin(312,156571),((lin(2,11),lin(2,41)),0),0,[-50,142],[[4,0,445],[4,0,455]])}[r]
 assert elapsed==expected[0] and (base,h)==expected[1] and tw==W[expected[2]:]+W[:expected[2]] and [umin,umax]==expected[3] and [list(min(tail_z)),list(max(tail_z))]==expected[4] and zmin==-105
 out=dict(status='exact all-k finite cap-kernel capture; every infinite future read remains in z>=-125',phase=r,domain='k=U+100,U>=0',initial_marker=marker,first_contact=first,capture_time=elapsed,capture_pose=[base,h],tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),tail=proof,finite_prefix_u_bounds=[umin,umax],whole_future_u_upper=umax,whole_future_z_lower=zmin,tail_z_bounds=[min(tail_z),max(tail_z)],records=records,statistics=A.STATS.copy(),template_sha256=hashlib.sha256(tp.read_bytes()).hexdigest(),cap_certificate_sha256=hashlib.sha256((HERE.parent/'fixed_caps.json').read_bytes()).hexdigest())
 (HERE/f'certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
