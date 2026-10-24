"""Full outgoing-front guard test at the black-compatible single-turn poses.
The current head need not reach these poses. A matching interface would only
supply a one-shot launch, not a renewal or a physical connector.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
sys.path.insert(0,str(P.parents[1]/'computability'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot,xor
from probe_perpendicular_highway_wake import H,step
from periodic_tail_checker import State,first_mismatch
ctx=Context(max_operations=200000000)
def S(c):return ctx.set('[r,a,b]->{[x,y]:'+c+'}')
old=ctx.set(json.loads((P/'four_corner_loop_certificate.json').read_text())['output_relation'].replace('[r]','[r,a,b]',1))
cases=json.loads((P/'four_corner_all_phases_black.json').read_text())['black_stencil_matches'];out=[]
for c in cases:
 ctx.reset_operations();st=time.monotonic();d=c['phase_data'];k=c['rotation_ccw'];ha=d['input_head'];turn=d['cap'];b=d['out_phase'];w=H[b:]+H[:b]
 rr,_,_=trace(turn+w*12,(0,0),ha);first={}
 for q,h,t in rr:first.setdefault(q,t)
 B={q for q,t in first.items()if t=='L'};bb=set(B);p,h,t=step(bb,(0,0),ha);assert t==turn
 assert first_mismatch(State(frozenset(bb),p,h),w) is None
 rows,ep,eh=trace(w,p,h);dv=rot((ep[0]-p[0],ep[1]-p[1]),k)
 read=S('x=a and y=b')
 for q,hh,tt in rows:
  q=rot(q,k);read=read.union(S(f'exists(i:i>=0 and x=a+{q[0]}+{dv[0]}*i and y=b+{q[1]}+{dv[1]}*i)'))
 BK=[rot(q,k)for q in B];required=S(' or '.join(f'(x=a+{x} and y=b+{y})'for x,y in BK))
 corr=xor(required,old.intersect(read));placements=ctx.set(c['translations']).intersect(ctx.set(f'[r,a,b]->{{:(a+b+{ha-k}) mod 2=0}}'))
 good=placements.subtract(corr.params()).coalesce()
 out.append(dict(case=c['case'],rotation_ccw=k,input_heading=(ha-k)%4,source_black_placements=c['translations'],same_sector_placements=str(placements),exact_outgoing_front_placements=str(good),empty=good.is_empty(),required_black_relative=BK,correction_relation=str(corr),seconds=time.monotonic()-st))
 print(c['case'],k,'sector empty',placements.is_empty(),'full empty',good.is_empty(),flush=True)
 (P/'four_corner_phase_front_guards.partial.json').write_text(json.dumps(dict(scope=__doc__,cases=out),indent=2)+'\n')
(P/'four_corner_phase_front_guards.json').write_text(json.dumps(dict(scope=__doc__,cases=out),indent=2)+'\n')
