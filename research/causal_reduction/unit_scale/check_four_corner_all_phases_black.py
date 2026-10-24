"""First exact no-new-fuel test for known positive single-turn corner phases.
Only required black stencils are checked first; a pass is not full legality.
The source is the complete finite four-corner loop output, for every r>=3.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import rot
st=time.monotonic();ctx=Context(max_operations=200000000)
old=ctx.set(json.loads((P/'four_corner_loop_certificate.json').read_text())['output_relation'].replace('[r]', '[r,a,b]',1))
C=json.loads((P/'single_turn_corner_selected.json').read_text())['cases'];matches=[]
for i,c in enumerate(C):
 for k in range(4):
  ctx.reset_operations();K=[rot(q,k)for q in c['extra_relative_cap']]
  target=ctx.set('[r,a,b]->{[x,y]:r>=3 and ('+' or '.join(f'(x=a+{x} and y=b+{y})'for x,y in K)+')}' )
  good=ctx.set('[r,a,b]->{:r>=3}').subtract(target.subtract(old).params()).coalesce()
  if not good.is_empty():matches.append(dict(case=i,rotation_ccw=k,translations=str(good),phase_data=c))
 if i%20==0:print('checked',i,'matches',len(matches),flush=True)
out=dict(scope=__doc__,source='full four-corner finite output, r>=3',target_cases=len(C),rotations=4,black_stencil_matches=matches,seconds=time.monotonic()-st)
(P/'four_corner_all_phases_black.json').write_text(json.dumps(out,indent=2)+'\n');print('FINISHED',len(matches),out['seconds'])
