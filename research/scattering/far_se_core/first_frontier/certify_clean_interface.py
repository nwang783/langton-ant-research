"""Complete q+a history versus a clean SE front, on an entire forward half-plane."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,plan,step,multiple
M=(1,0,100);N=(1,1,200);C=lambda v:(0,0,v)
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
def n(a,b):return A.add(A.scale(N,a),C(b))
def value(p,name):return A.sub(p[0],p[1]) if name=='u' else A.add(p[0],p[1])
def main():
 T=json.loads(TFILE.read_text());field=A.Field([(n(-2,-33),n(-2,-14)),(n(-2,-33),n(2,41))]);p=A.point(0,0);h=0;elapsed=C(0);bounds={'u':-10**9,'z':-10**9}
 def record(q,drift=(0,0),count=None):
  for name in bounds:
   v=value(q,name);speed=drift[0]-drift[1] if name=='u' else sum(drift)
   if count is not None and speed>0:v=A.add(v,A.scale(A.sub(count,A.ONE),speed))
   assert v[0]<=0 and v[1]<=0;bounds[name]=max(bounds[name],v[2])
 for i,s in enumerate(T['segments'][:9]):
  word=s['word'];assert word and set(word)<={'R','L'};qs,_,end,eh=plan(word,(0,0),h);_,odd,_,_=A.word_data(word,h)
  count=None if s['type']=='finite' else n(*s['count'])
  if count is not None:assert len(word)==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
  for q in qs:record(A.translate_local(q,p,0),end,count)
  if count is None:field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0);elapsed=A.add(elapsed,C(len(word)))
  else:field.add_rays([A.translate_local(q,p,0) for q in odd],end,count,'old'+str(i));p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 assert p==A.point(40,-50) and h==2 and elapsed==n(416,146040)
 assert T['segments'][9]['word']==W[100:]+W[:100] and T['segments'][9]['count']==[1,-20]
 partial=W[100:];assert len(partial)==4
 qs,_,end,eh=plan(partial,(0,0),h);_,odd,_,_=A.word_data(partial,h)
 for q in qs:record(A.translate_local(q,p,0))
 field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0);elapsed=A.add(elapsed,C(4));h=eh
 assert p==A.point(40,-52) and h==2 and elapsed==n(416,146044) and bounds=={'u':98,'z':71},(p,h,elapsed,bounds)
 # At this fixed origin the exact field is canonical P plus the entire old
 # stationary archive E_n. Bound every term without deleting or clipping it.
 field.add_points(A.translate_local(q,p,0) for q in P)
 archive={'u':-10**9,'z':-10**9};saved=bounds;bounds=archive
 for q in field.points:record(q)
 for b,d,count,label in field.rays:record(b,d,count)
 bounds=saved;assert archive=={'u':97,'z':71},archive
 B=set(P);pp=(0,0);hh=2
 for ch in W:pp,hh,actual=step(B,pp,hh);assert actual==ch
 assert pp==(2,-2) and hh==2 and B=={(x+2,y-2) for x,y in P}^set(D)
 O=(A.add(A.scale(M,2),C(40)),A.add(A.scale(M,-2),C(-52)))
 source_time=A.add(elapsed,A.scale(M,104))
 assert A.nonneg(A.sub(A.scale(n(1,-20),104),A.add(A.scale(M,104),C(4))))
 # After m periods, the actual field equals mature canonical C_infinity at O
 # XOR the stationary E_n and the canonical deposits older than age m.
 older_global_u=max(x-y for x,y in D)+92-4;assert older_global_u==97
 assert A.negative(A.sub(C(102),A.sub(value(O,'u'),C(200))))
 reads,_,_,_=plan(W,(0,0),2);front=[]
 for i,q in enumerate(reads):
  if any((k:=multiple((p[0]-q[0],p[1]-q[1]),(2,-2))) is not None and (k>0 or k==0 and j<i) for j,p in enumerate(reads)):continue
  front.append(i)
 assert front==[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
 assert (min(x-y for x,y in reads),max(x-y for x,y in reads))==(0,10)
 assert A.negative(A.sub(A.add(A.scale(M,4),C(98)),n(4,22)))
 assert A.negative(A.sub(C(71),n(4,49)))
 bases=[(40+reads[r][0],-52+reads[r][1]) for r in front]
 assert {(x+y,x%2) for x,y in bases}=={(z,p) for z in range(-15,-4) for p in (0,1)}
 assert min(x-y for x,y in bases)==95 and max(x-y for x,y in bases)==102
 assert min(x-y for x,y in bases)+4*100>102
 out=dict(status='complete old history agrees with clean mature SE core throughout source u>=-200',domain='m>=100,n-m>=100',source_origin=O,source_time=source_time,stationary_archive_upper=archive,base_prefix_read_upper=bounds,checkpoint_prefix_u_upper_m=[4,98],checkpoint_prefix_z_upper=71,complete_model_discrepancy_global_u_upper=97,source_halfplane_u_lower=-200,fresh_phases=front,core_ray_bases=bases,sufficient_global_u_lower=502,source_template_sha256=hashlib.sha256(TFILE.read_bytes()).hexdigest(),scope='Any perturbed future staying in source u>=-200 transfers from the canonical infinite-past model. No claim for phase72 return or later remote corner encounters.')
 (HERE/'clean_interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
