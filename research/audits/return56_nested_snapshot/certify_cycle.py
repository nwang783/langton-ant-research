"""Full retained-field phase56 cycle after the forced relation p=n+38."""
import sys,json,hashlib
from pathlib import Path
from certify_strip_model import HERE,ROOT,SRC,geometry
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A,infinite_tail
from ant_exact import W,P,D,plan
C=lambda v:(0,0,v);N=(1,0,100);lin=lambda a,b:A.add(A.scale(N,a),C(b));sub=lambda v:(v[0]+v[1],0,v[2]+38*v[1]);psub=lambda q:tuple(sub(v) for v in q)
def main():
 old,points,rays=geometry();q4=(lin(2,98),lin(-2,-30));q5=(lin(-2,-19),lin(2,25));entry=(-70,130);p0=(2,24)
 for k in A.STATS:A.STATS[k]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear()
 points=[psub(q) for q in points]+[A.point(*q) for q in P]+[A.point(p0[0]-x,p0[1]-y) for x,y in P]+[A.point(entry[0]+x,entry[1]+y) for x,y in P]+[q4]
 F=A.Field(points)
 for i,(q,d,count) in enumerate(rays):F.add_rays([psub(q)],d,sub(count),'inherited_packet'+str(i))
 bases=[[(x-2,y+2) for x,y in D],[(p0[0]-x,p0[1]-y) for x,y in D],[(entry[0]+x-2,entry[1]+y+2) for x,y in D]]
 for i,bs in enumerate(bases):
  assert max(x-y for x,y in bs)-400<-250;F.add_rays([A.point(*q) for q in bs],(-2,2),C(100),'complete_rail'+str(i))
 Tpath=HERE/'template_cycle.json';T=json.loads(Tpath.read_text());base=A.point(*entry);h=2;elapsed=C(0);contact=None;records=[];std={W[j:]+W[:j] for j in range(104)}
 for i,seg in enumerate(T['segments']):
  assert seg['type'] in ['finite','periods'];w=seg['word'];assert w and set(w)<={'R','L'};data=A.word_data(w,h);count=None if seg['type']=='finite' else lin(*seg['count_n']);reads=plan(w,(0,0),h)[0]
  if contact is None:
   hits=[]
   for j,q in enumerate(reads):
    here=A.translate_local(q,base,0)
    if count is None:
     if here==q4:hits.append(A.add(elapsed,C(j)))
     else:assert A.no_point_collision(here,q4)
    else:
     k=A.line_coordinate(A.psub(q4,here),data[2])
     if k is not None and A.in_range(k,count):hits.append(A.add(A.add(elapsed,A.scale(k,104)),C(j)))
   if hits:
    contact=hits[0]
    for v in hits[1:]:contact=A.minimum(contact,v)
  if count is None:base=A.apply_finite(F,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(w)))
  else:
   assert len(w)==104 and w in std and data[3]==h and A.nonneg(A.sub(count,A.ONE));base=A.apply_periods(F,data,base,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h]));print(json.dumps(records[-1]),flush=True)
 assert contact==lin(104,18472)
 tw=T['infinite_tail_word'];assert tw in std;data=A.word_data(tw,h);assert data[3]==h and data[2]==(2,2);tail=infinite_tail(F,data,base)
 lower=[]
 for q in A.READ_POINTS:
  u=A.sub(q[0],q[1]);assert A.nonneg(A.sub(u,C(-200)));lower.append(u)
 for q,d,count in A.READ_RAYS:
  u=A.sub(q[0],q[1]);end=A.add(u,A.scale(A.sub(count,A.ONE),d[0]-d[1]));assert A.nonneg(A.sub(u,C(-200))) and A.nonneg(A.sub(end,C(-200)))
 for q in data[0]:
  u=A.sub(*A.translate_local(q,base,0));assert A.nonneg(A.sub(u,C(-200)))
 assert A.negative(A.sub(A.sub(q5[0],q5[1]),C(-200)))
 phase=next(i for i in range(104) if tw==W[i:]+W[:i]);out=dict(status='complete all-n retained-field cycle and infinite tail',domain='n>=100, p=n+38',capture_time=elapsed,capture_pose=[base,h],tail_phase=phase,tail=tail,first_fourth_corner=contact,unused_NW_corner=q5,unused_corner_never_read=True,whole_future_u_lower=-200,statistics=A.STATS.copy(),records=records,template_sha256=hashlib.sha256(Tpath.read_bytes()).hexdigest(),source_cycle_sha256=hashlib.sha256((SRC/'backward_certificate_r56.json').read_bytes()).hexdigest(),scope='The whole actual-history half-plane interface supplies the original blank state. The far NW fifth corner is protected independently by u.')
 (HERE/'cycle_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
