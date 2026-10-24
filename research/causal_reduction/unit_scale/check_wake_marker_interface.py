"""Exact one geometrically specified spectator-marker control, not a search.
All m>=30; inherits the independently signed fixed-scatterer trajectory.
"""
from pathlib import Path
import sys,json,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,xor
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=100000000)
J=json.loads((P/'highway_wake_mirror_minimal.json').read_text())
D=json.loads((P/'wake_single_marker_control.json').read_text())
C=json.loads((P/'highway_wake_reflector_collision.json').read_text())['collision_word']
def S(c):return ctx.set('[n,m]->{[x,y]:n>=30 and m>=30 and ('+c+')}')
def pts(ps):return S(' or '.join(f'(x={x} and y={y})'for x,y in ps)or'false')
marker=(-32,-8);M=pts([marker]);initial=ctx.set(J['initial_relation']);entry=ctx.set(J['postcollision_relation'])
assert M.intersect(initial).is_empty()
rr,_,_=trace(C,(-19,20),2);assert marker not in {q for q,h,c in rr}
rr,_,_=trace(H,(0,0),2)
pres=S('false')
for q,h,c in rr:pres=pres.union(S(f'exists(i:0<=i<m-10 and x=-2*m+1+{q[0]}+2*i and y=2*m+{q[1]}-2*i)'))
assert pres.intersect(M).is_empty()
# The uniquely earliest fresh white tail read, after discarding full past reads.
tail,_,_=trace(H,(-31,-10),0)
Creads=pts({q for q,h,c in trace(C,(-19,20),2)[0]})
for t,(q,h,c)in enumerate(tail[:14]):
 if t==13:assert q==marker and c=='R'
 else:assert pts([q]).subtract(Creads.union(pres)).is_empty()
# Fixed changed124-turn block, first-color guard against the full parametric board.
w=D['tail_word'][:124];rr,p,h=trace(w,(-31,-10),0);assert(p,h)==((-33,-8),0)
B=xor(entry,M);odd=set();last={};first={}
for q,hh,c in rr:
 if q in last:assert last[q]!=c
 else:first[q]=c
 last[q]=c;odd.symmetric_difference_update({q})
needB=pts(q for q,c in first.items()if c=='L');needW=pts(q for q,c in first.items()if c=='R')
assert needB.subtract(B).is_empty();assert needW.intersect(B).is_empty()
changed=xor(B,pts(odd))
baseodd=set()
for q,hh,c in tail:baseodd.symmetric_difference_update({q})
baseline=xor(entry,pts(baseodd));delta=xor(changed,baseline)
expected=[(-32,-8),(-32,-6),(-32,-5),(-31,-7),(-31,-5),(-30,-8),(-30,-6),(-29,-8),(-29,-7)]
assert delta.is_equal(pts(expected))
# Every discrepancy is permanently behind the next canonical104 read support.
future=S('false')
for q,hh,c in trace(H,p,h)[0]:future=future.union(S(f'exists(i:i>=0 and x={q[0]}-2*i and y={q[1]}+2*i)'))
assert future.intersect(delta).is_empty()
out=dict(status='EXACT_ALL_M_SINGLE_MARKER_CAPTURE',domain='m>=30',marker=marker,marker_first_read_after_collision=13,changed_word=w,changed_length=len(w),endpoint=[p,h],ordinary_word_length=104,delay=20,complete_difference_vs_ordinary_next_phase=expected,difference_never_read_again=True,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'wake_marker_interface_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
