"""Exact finite repair for the nearest black-compatible alternate corner phase.
This identifies colors only, not a physical eraser or reachable next pose.
"""
from pathlib import Path
import sys,json
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=200000000)
def S(c):return ctx.set('[a,b]->{[x,y]:'+c+'}')
old=ctx.set(json.loads((P/'highway_corner_reuse_profile.json').read_text())['old_stable_black_relation'])
c=json.loads((P/'corner_phase_alternation_black.json').read_text())['black_stencil_matches'][1];assert(c['case'],c['rotation_ccw'])==(16,1)
d=c['phase_data'];k=1;ha=d['input_head'];a=d['in_phase'];b=d['out_phase'];turn=d['cap']
inrows,di,hi=trace(H[a:]+H[:a],(0,0),ha)
_,p,h=trace(turn,(0,0),ha);outrows,pe,he=trace(H[b:]+H[:b],p,h);do=(pe[0]-p[0],pe[1]-p[1])
reads=S('x=a and y=b');inread=S('false');outread=S('false')
for z,(rows,v,cond)in enumerate(((inrows,di,'i<0'),(outrows,do,'i>=0'))):
 v=rot(v,k);arm=S('false')
 for q,hh,tt in rows:
  q=rot(q,k);arm=arm.union(S(f'exists(i:{cond} and x=a+{q[0]}+{v[0]}*i and y=b+{q[1]}+{v[1]}*i)'))
 reads=reads.union(arm)
 if z==0:inread=arm
 else:outread=arm
K=[rot(q,k)for q in d['extra_relative_cap']];target=S(' or '.join(f'(x=a+{x} and y=b+{y})'for x,y in K));place=ctx.set('[a,b]->{:a=2 and b=7}')
extra=old.intersect(reads).subtract(target).intersect_params(place).coalesce()
assert extra.subtract(S('-30<=x<=30 and -30<=y<=30')).is_empty()
ps=[]
for x in range(-30,31):
 for y in range(-30,31):
  if not extra.intersect(S(f'x={x} and y={y}')).is_empty():ps.append((x,y))
outonly=extra.subtract(inread);inonly=extra.subtract(outread)
result=dict(scope=__doc__,case=16,target_incoming_phase=a,target_outgoing_phase=b,target_cap=turn,rotation_ccw=1,translation=[2,7],target_incoming_head=(ha-1)%4,required_erased_cells=ps,required_erased_count=len(ps),any_added_black_required=False,correction_relation=str(extra),incoming_only_correction=str(inonly),outgoing_only_correction=str(outonly))
(P/'corner_alternate_repair.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
