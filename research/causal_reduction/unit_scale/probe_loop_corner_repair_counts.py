"""Finite whole-field discovery counts, not an all-r repair theorem."""
from pathlib import Path
import json,time
from probe_perpendicular_highway_wake import H,step
from certify_highway_wake_reflector import trace,rot
P=Path(__file__).resolve().parent
seed=json.loads((P/'four_corner_loop_certificate.json').read_text())['seed_families_ax_bx_ay_by']
C=json.loads((P/'single_turn_corner_selected.json').read_text())['cases']
M=json.loads((P/'four_corner_all_phases_black.json').read_text())['black_stencil_matches']
def firster(case,k):
 ha=(case['input_head']-k)%4;a=case['in_phase'];b=case['out_phase'];cap=case['cap']
 ir,di,_=trace(H[a:]+H[:a],(0,0),ha);_,p,h=trace(cap,(0,0),ha);orr,e,_=trace(H[b:]+H[:b],p,h);do=(e[0]-p[0],e[1]-p[1]);tables=[]
 for rows,d,inc,sh in((ir,di,True,0),(orr,do,False,1)):
  table={}
  for j,(q,h,t)in enumerate(rows):table.setdefault((d[0]*q[1]-d[1]*q[0],q[0]%2),[]).append((j,q,t))
  tables.append((d,inc,sh,table))
 def first(q):
  events=[(0,cap)]if q==(0,0)else[]
  for d,inc,sh,table in tables:
   for j,a,t in table.get((d[0]*q[1]-d[1]*q[0],q[0]%2),[]):
    assert (q[0]-a[0])%d[0]==0;n=(q[0]-a[0])//d[0]
    if (n<0)if inc else(n>=0):events.append((104*n+j+sh,t))
  return min(events)[1]if events else None
 return first
out=[]
for r in(3,10,30,50):
 B={(a*r+b,c*r+d)for a,b,c,d in seed};p=(0,0);h=0
 for c in ('R'+H*r+H[:68])*3+'R'+H*r+H[:60]:p,h,t=step(B,p,h);assert t==c
 rr=[]
 for m in M:
  case=C[m['case']];k=m['rotation_ccw'];K={rot(q,k)for q in case['extra_relative_cap']};anchor=next(iter(K));first=firster(case,k);ha=(case['input_head']-k)%4;vals=[]
  for b in B:
   a=(b[0]-anchor[0],b[1]-anchor[1])
   if(sum(a)+ha)%2:continue
   if not all((a[0]+q[0],a[1]+q[1])in B for q in K):continue
   bad=[q for q in B if first((q[0]-a[0],q[1]-a[1]))=='R']
   vals.append((len(bad),a))
  rr.append(dict(case=m['case'],rotation_ccw=k,placements=len(vals),minimum=min(vals)if vals else None,maximum=max(vals)if vals else None))
 out.append(dict(r=r,cases=rr));print(r,[(v['case'],v['rotation_ccw'],v['placements'],v['minimum'][0]if v['minimum']else None)for v in rr],flush=True)
(P/'loop_corner_repair_counts.json').write_text(json.dumps(dict(scope=__doc__,rows=out),indent=2)+'\n')
