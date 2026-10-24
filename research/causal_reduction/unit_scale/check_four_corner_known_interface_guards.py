"""Exact complete-input white-guard conflicts for retained orthogonal104 corners.
The source is the complete43-cell loop output. Each target is the original
mature incoming half-ray, its literal single turn, and its outgoing half-ray.
Required initial color is computed from the EARLIEST actual read at a witness,
not the color at the cap after an omitted incoming pass. No renewal follows.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=200000000)
old=ctx.set(json.loads((P/'four_corner_loop_certificate.json').read_text())['output_relation'].replace('[r]','[r,a,b]',1))
cases=json.loads((P/'four_corner_all_phases_black.json').read_text())['black_stencil_matches'];out=[]
def mult(diff,d):
 z=next(i for i,a in enumerate(d)if a)
 if diff[z]%d[z]:return None
 n=diff[z]//d[z]
 return n if all(diff[i]==n*d[i]for i in range(2))else None
for c in cases:
 ctx.reset_operations();st=time.monotonic();d=c['phase_data'];k=c['rotation_ccw'];ha=(d['input_head']-k)%4;cap=d['cap'];ia=d['in_phase'];ob=d['out_phase']
 ir,di,_=trace(H[ia:]+H[:ia],(0,0),ha)
 cr,p,h=trace(cap,(0,0),ha);orr,e,_=trace(H[ob:]+H[:ob],p,h);do=(e[0]-p[0],e[1]-p[1])
 active=ctx.set(c['translations']).intersect(ctx.set(f'[r,a,b]->{{:(a+b+{ha}) mod 2=0}}'));original=str(active)
 K={rot(q,k)for q in d['extra_relative_cap']}
 def first(q):
  events=[(0,cap,'cap',0,0)]if q==(0,0)else[]
  for typ,rows,v,positive,shift in(('incoming',ir,di,False,0),('outgoing',orr,do,True,1)):
   for j,(a,hh,t)in enumerate(rows):
    n=mult((q[0]-a[0],q[1]-a[1]),v)
    if n is not None and((n>=0)if positive else(n<0)):events.append((104*n+j+shift,t,typ,n,j))
  return min(events)if events else None
 candidates={(0,0)}
 for rows,v,ns in((ir,di,range(-3,0)),(orr,do,range(3))):
  for q,hh,ch in rows:
   for n in ns:candidates.add((q[0]+n*v[0],q[1]+n*v[1]))
 witnesses=[]
 for q in sorted(candidates,key=lambda q:(abs(q[0])+abs(q[1]),q)):
  if active.is_empty():break
  event=first(q)
  if event is None or event[1]!='R':continue
  assert q not in K
  ctx.reset_operations();point=ctx.set(f'[r,a,b]->{{[x,y]:x=a+{q[0]} and y=b+{q[1]}}}').intersect_params(active)
  bad=old.intersect(point).params()
  if not bad.is_empty():
   witnesses.append(dict(point_relative=q,first_read=event,parameters=str(bad.coalesce())))
   active=active.subtract(bad).coalesce()
 row=dict(case=c['case'],rotation_ccw=k,initial_heading=ha,same_sector_placements=original,survivors=str(active),empty=active.is_empty(),white_witnesses=witnesses,seconds=time.monotonic()-st)
 out.append(row);print(c['case'],k,'empty',row['empty'],'witnesses',len(witnesses),flush=True)
 (P/'four_corner_known_interface_guards.partial.json').write_text(json.dumps(dict(scope=__doc__,cases=out),indent=2)+'\n')
(P/'four_corner_known_interface_guards.json').write_text(json.dumps(dict(scope=__doc__,cases=out),indent=2)+'\n')
assert all(q['empty']for q in out)
