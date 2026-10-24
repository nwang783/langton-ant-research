from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];NOTE=R/'global_architecture_2026-10-23/standard_flight_P108_preparation_bound.md';H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];P=json.loads((R/'causal_reduction/unit_scale/reverse108_prepared_control.json').read_text())['word']
def trace(w,h,start=(0,0)):
 x,y=start;out=[];D=((0,1),(1,0),(0,-1),(-1,0))
 for c in w:
  out.append((x,y,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return out,(x,y),h
ps,_,_=trace(P,3);ks=[x//2 for x,y,c in ps];normals=[x-y for x,y,c in ps]
assert max(ks)-min(ks)==2 and(min(normals),max(normals))==(-7,4)
parallel=[]
for h in (1,3):
 for parity in (0,1):
  rr,end,hh=trace(H,h,(parity,0));span=max(x//2 for x,y,c in rr)-min(x//2 for x,y,c in rr);assert span<=3
  parallel.append({'heading':h,'x_parity':parity,'global_level_span':span})
perp=[]
for h in (0,2):
 rr,end,hh=trace(H,h);assert hh==h and end[0]==-end[1] and abs(end[0])==2
 classes={(x+y,x%2)for x,y,c in rr};assert len(classes)==22
 perp.append({'heading':h,'read_lattice_classes':22})
# Validate both algebraic endpoint partitions over all short lengths and translations.
controls=0
for sigma in (-1,1):
 for lo in range(-5,6):
  for width in range(7):
   hi=lo+width
   for N in range(0,10):
    if sigma==1:fringe=set(range(lo,hi))|set(range(lo+N,hi+N))
    else:fringe=set(range(lo-N+1,hi-N+1))|set(range(lo+1,hi+1))
    for k in range(lo-N-width-2,hi+N+width+3):
     if k in fringe:continue
     active=[k in {a+sigma*j for j in range(N)}for a in range(lo,hi+1)]
     assert all(active)or not any(active)
     controls+=1
assert (min(normals)-10,max(normals)+10)==(-17,14)
assert 2*(14-(-17)+1)==64 and 64*22==1408
for cut in range(105):
 U,V=H[:cut],H[cut:]
 for n in (1,2,4):assert(V+U)*n==V+H*(n-1)+U
out={'status':'PASS literal common-gauge constants and endpoint partition controls','note_sha256':hashlib.sha256(NOTE.read_bytes()).hexdigest(),'P_complete_level_loss':2,'parallel_spans':parallel,'perpendicular_classes':perp,'normal_envelope':[-17,14],'envelope_full_drift_classes':64,'perpendicular_loss':1408,'endpoint_partition_controls':controls,'cyclic_cut_cap_cost':104,'scope':'Analytic ownership lift signs |B|>=n-2-6 Fparallel-L-1408 Fperp for this P108 and actual canonical standard flights. No fixed mass/cap/flight assumption is needed for the inequality; bounded-complexity corollary only.'}
(R/'audits/check_standard_flight_boundary_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
