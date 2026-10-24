"""The exact six-transition nonempty cap7 cycle, not the full cap7 kernel.
One loop is physical; two prescribed full-component loops are not. Literal
turn-word double repetition is deliberately retained as an adversarial control.
"""
from pathlib import Path
import json,hashlib
from finite_general_component_profile_lift import lift,transform
from active_flight import rot,cursor,ends,sector,vertices,comp,step
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
SRC=ROOT/'reframe_finite_seed_2026-10-24/cap7_structure_probe.json'
J=json.loads(SRC.read_text())['cycle_witness'];W=J['word'];assert W=='RRLLLL'
J={**J,'index':'cap7_nonempty_six_cycle'}
one=lift([J],True);two=lift([J,J],True)
seed={(-1,-1),(-1,0),(1,-1),(2,-1),(2,0)}
assert one['status']=='ACTUAL_FINITE_BOARD_LIFT'and set(one['initial_black'])==seed
assert one['maximum_complete_active_mass']==7 and one['final_pose']==[(1,-1),2]
assert set(one['final_black'])=={(-1,-1),(-1,0),(0,0)}
assert two['status']=='NO_COMPLETE_BOARD_LIFT'
# Record the exact consumed imported cells required by the next copy.
nextD=transform(J['transitions'][0]['imported_component'],(1,-1),2)
assert nextD=={(2,-1),(2,0)}
B=set(seed);p=(0,0);h=0;deletions={};word='';trace=[]
for t in range(13):
 C=comp(B,1,cursor(p,h));zz=rot((-1,-1),h);z=(2*p[0]+zz[0],2*p[1]+zz[1]);trace.append(dict(cut=t,pose=[p,h],w_cursor=cursor(p,h),z_cursor=z,full_black=sorted(B),active_w=sorted(C),active_z=sorted(comp(B,0,z))))
 if t==6:assert nextD.isdisjoint(B)
 if t==12:break
 c='L'if p in B else'R';word+=c
 if c=='L':deletions[p]=t
 p,h=step(B,p,h)
assert word==W*2 and deletions[(2,-1)]==3 and deletions[(2,0)]==4
assert set(trace[-1]['full_black'])=={(1,-1)}
expected_second=transform(J['transitions'][0]['output_active'],(1,-1),2)
assert len(trace[7]['active_w'])==4 and len(expected_second)==6 and set(trace[7]['active_w'])!=expected_second
out=dict(status='PASS exact cap7 nonempty core one-loop lift and double-loop obstruction',source_sha256={str(SRC.relative_to(ROOT)):hashlib.sha256(SRC.read_bytes()).hexdigest()},single_loop=one,double_loop_full_profile_conflict=two,next_required_imported_component=sorted(nextD),expected_second_after_first_R=sorted(expected_second),first_loop_deletions=[dict(cell=q,update=deletions[q])for q in sorted(nextD)],literal_double_word_control=dict(word=word,initial_black=sorted(seed),final_black=trace[-1]['full_black'],trace=trace),scope='Only the supplied six-transition nonempty core is tested; structural uniqueness of its cap7 SCC is a separate dependency. The literal word RRLLLL twice DOES execute from the5-cell seed, but with no second imported dimer and a different complete active path. No cap7 exit or capture theorem follows here.')
(OUT/'cap7_nonempty_cycle_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'single_seed':one['initial_black'],'single_exit':one['final_pose'],'single_output':one['final_black'],'double_conflict':two,'literal_double_word':word,'literal_double_final':trace[-1]['full_black']},indent=2))
