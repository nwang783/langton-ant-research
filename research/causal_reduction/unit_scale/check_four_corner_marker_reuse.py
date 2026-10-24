"""Exact all-r black-stencil reuse test on the full finite closed-loop output.
Black-subset matches alone do not supply white guards or a physical next pose.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import rot
ctx=Context(max_operations=200000000)
J=json.loads((P/'four_corner_loop_certificate.json').read_text());old=ctx.set(J['output_relation'].replace('[r]', '[r,a,b]',1));K=json.loads((P/'single_turn_highway_corner_certificate.json').read_text())['corner_relative_black'];out=[]
for k in range(4):
 st=time.monotonic();ctx.reset_operations();pts=[rot(q,k)for q in K]
 target=ctx.set('[r,a,b]->{[x,y]:r>=3 and ('+' or '.join(f'(x=a+{x} and y=b+{y})'for x,y in pts)+')}')
 good=ctx.set('[r,a,b]->{:r>=3}').subtract(target.subtract(old).params()).coalesce()
 out.append(dict(rotation_ccw=k,black_compatible_placements=str(good),empty=good.is_empty(),seconds=time.monotonic()-st));print(out[-1],flush=True)
(P/'four_corner_marker_reuse.json').write_text(json.dumps(dict(scope=__doc__,cases=out),indent=2)+'\n')
