"""Exact new FRONT guard, not a supplied incoming ray, at the alternate corner.
The resulting finite field correction is an interface obligation, not a path.
"""
from pathlib import Path
import sys,json
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
sys.path.insert(0,str(P.parents[1]/'computability'))
from presburger_read_set_solver import Context
from periodic_tail_checker import State,first_mismatch
from certify_highway_wake_reflector import trace,xor
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=200000000)
def S(c):return ctx.set('[a,b]->{[x,y]:'+c+'}')
def pts(ps):return S(' or '.join(f'(x={x} and y={y})'for x,y in ps)or'false')
old=ctx.set(json.loads((P/'highway_corner_reuse_profile.json').read_text())['old_stable_black_relation'])
w=H[102:]+H[:102];rr,_,_=trace(w*20,(2,6),2);first={}
for q,h,c in rr:first.setdefault(q,c)
black={q for q,c in first.items()if c=='L'};assert first_mismatch(State(frozenset(black),(2,6),2),w)is None
rows,ep,eh=trace(w,(2,6),2);assert(ep,eh)==((4,4),2)
reads=S('false')
for q,h,c in rows:reads=reads.union(S(f'exists(i:i>=0 and x={q[0]}+2*i and y={q[1]}-2*i)'))
add=pts(black).subtract(old);erase=old.intersect(reads).subtract(pts(black));correction=add.union(erase)
assert correction.subtract(S('-30<=x<=30 and -30<=y<=30')).is_empty()
def enum(z):return[(x,y)for x in range(-30,31)for y in range(-30,31)if not z.intersect(pts([(x,y)])).is_empty()]
A=enum(add);E=enum(erase)
out=dict(scope=__doc__,target_pose=[2,6,'S'],target_period_phase=102,target_drift=[2,-2],required_minimal_black=sorted(black),add=A,erase=E,add_count=len(A),erase_count=len(E),correction_relation=str(correction))
(P/'direct_alternate_front_repair.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
