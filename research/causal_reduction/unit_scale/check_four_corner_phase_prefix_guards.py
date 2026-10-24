"""Exact parametric finite conflict partition at all known black-compatible caps.
Use the COMPLETE post-loop field, all r>=3 and every translated retained stencil.
A cap plus proposed104 tail is checked literally until its parameter set empties.
This does not classify arbitrary connectors or the other possible head poses.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=200000000)
old=ctx.set(json.loads((P/'four_corner_loop_certificate.json').read_text())['output_relation'].replace('[r]','[r,a,b]',1))
cases=json.loads((P/'four_corner_all_phases_black.json').read_text())['black_stencil_matches'];out=[]
for c in cases:
 ctx.reset_operations();st=time.monotonic();d=c['phase_data'];k=c['rotation_ccw'];ha=(d['input_head']-k)%4;turn=d['cap'];b=d['out_phase'];w=turn+(H[b:]+H[:b])*20
 active=ctx.set(c['translations']).intersect(ctx.set(f'[r,a,b]->{{:(a+b+{ha}) mod 2=0}}'))
 original=str(active);rows,_,_=trace(w,(0,0),ha);odd=set();records=[]
 for j,(q,h,ch)in enumerate(rows):
  if active.is_empty():break
  ctx.reset_operations()
  point=ctx.set(f'[r,a,b]->{{[x,y]:x=a+{q[0]} and y=b+{q[1]}}}').intersect_params(active)
  black=old.intersect(point).params()
  need=(ch=='L')^(q in odd)
  bad=active.subtract(black)if need else active.intersect(black)
  if not bad.is_empty():records.append(dict(first_conflict=j,point_relative=q,required_initial_black=need,parameters=str(bad.coalesce())))
  active=active.subtract(bad).coalesce();odd.symmetric_difference_update({q})
 row=dict(case=c['case'],rotation_ccw=k,initial_heading=ha,same_sector_placements=original,survivors=str(active),empty=active.is_empty(),conflicts=records,seconds=time.monotonic()-st)
 out.append(row);print(c['case'],k,'empty',row['empty'],'last',max((x['first_conflict']for x in records),default=-1),flush=True)
 (P/'four_corner_phase_prefix_guards.partial.json').write_text(json.dumps(dict(scope=__doc__,cases=out),indent=2)+'\n')
(P/'four_corner_phase_prefix_guards.json').write_text(json.dumps(dict(scope=__doc__,cases=out),indent=2)+'\n')
assert all(q['empty']for q in out)
