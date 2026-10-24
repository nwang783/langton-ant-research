"""Exact local necessary-guard obstruction for the phase-forced C/T/C attempt.
No missing approach or complete ring composition is assumed to execute.
"""
from pathlib import Path
import json,hashlib
from certify_highway_wake_reflector import trace
from probe_perpendicular_highway_wake import H,shifted_seed,step
P=Path(__file__).resolve().parent
C=json.loads((P/'opposite_wake_quarter_turn_word.json').read_text());T=json.loads((P/'opposite_wake_through_phase21_word.json').read_text())
B=shifted_seed(2,(-160,-160));p=(-160,-160);h=1
for c in H*160:p,h,a=step(B,p,h);assert a==c
X=set(map(tuple,C['complete_xor']));post=B^X
rr,_,_=trace(C['word'],(27,-16),0) # original cut+(4,4)
seen=set();fail=[]
for t,(q,hh,c)in enumerate(rr):
 if q in seen:continue
 seen.add(q)
 if -7<=q[0]-q[1]<=3:
  actual='L'if q in post else'R'
  if actual!=c:fail.append(dict(t=t,q=q,required=c,after_first_C=actual,was_old_black=q in B,flipped_by_C=q in X))
assert fail
rt,_,_=trace(T['word'],(77+22,-77-19),0)
Tmin=min(q[0]-q[1]for q,hh,c in rt);Tmax=max(q[0]-q[1]for q,hh,c in rt)
assert Tmin>3
rh,dh,hh=trace(H,(0,0),0);incoming_before_cut_min=43+4+min(q[0]-q[1]for q,h,c in rh)
assert incoming_before_cut_min>3
ro,do,ho=trace(H,(91,-63),1);outgoing_norms=[min(q[0]-q[1]for q,h,c in ro),max(q[0]-q[1]for q,h,c in ro)]
assert outgoing_norms[0]>3
# Fixed phase quotient L=< (2,2),(-2,2) > has invariants x mod2,sum mod4.
def cl(q):return(q[0]%2,sum(q)%4)
a=(3,0);b=(91,-63);bt=(-18,29);ot=(77,-77);aftert=(ot[0]+bt[0],ot[1]+bt[1])
assert cl((a[0]-b[0],a[1]-b[1]))==cl((2,1))
assert sum(aftert)==11 and cl((aftert[0]-4,aftert[1]-4))==cl(a)
out=dict(status='EXACT_PHASE_AND_UNTOUCHED_STRIP_GUARD',scope=__doc__,C_output_origin=b,required_turn_phase=a,next_new_rail_phase=cl((a[0]-b[0],a[1]-b[1])),T_old_origin=ot,T_output_origin=aftert,next_original_C_translation=[4,4],old_strip=[-7,3],T_read_normal_range=[Tmin,Tmax],incoming_before_next_C_min_normal=incoming_before_cut_min,outgoing_C_tail_normal_range=outgoing_norms,guard_failures=fail,first_guard_failure=fail[0],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'quarter_turn_two_phase_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items()if k!='guard_failures'});print('mismatch_count',len(fail))
