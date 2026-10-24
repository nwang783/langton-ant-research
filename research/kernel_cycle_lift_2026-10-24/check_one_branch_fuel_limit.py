"""One pre-funded old branch, not a cap8 kernel search.
An actual RL prefix creates the incoming hook; then one literal T block.
"""
from pathlib import Path
import sys,json
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import rot,cursor,ends,comp,step
T='RRRRLLLLRLRL';entry={(-1,-1),(-1,0),(0,-2),(2,1)};a=(-1,-1)
seed=(entry-{a})|{(0,-1)};B=set(seed);p=a;h=0;birth={q:None for q in B};trace=[];mx=0

def components(B,k):
 seen=set();C=[]
 for q in sorted(B):
  if q not in seen:
   D=comp(B,k,ends(q,k)[0]);seen|=D;C.append(sorted(D))
 return C

def fuel(B):return sum(len(C)in(1,2)for C in components(B,1))

for t in range(2+len(T)+1):
 C=comp(B,1,cursor(p,h));mx=max(mx,len(C));zz=rot((-1,-1),h);z=(2*p[0]+zz[0],2*p[1]+zz[1])
 trace.append(dict(cut=t,pose=[p,h],w_cursor=cursor(p,h),z_cursor=z,full_black=sorted(B),w_components=components(B,1),active_w=sorted(C),active_z=sorted(comp(B,0,z)),small_component_fuel=fuel(B),lifetimes=[dict(cell=q,birth=birth[q])for q in sorted(B)]))
 if t==2:assert B==entry and not C and birth[a]==0;before=fuel(B)
 if t==2+len(T):break
 c=('RL'+T)[t];assert c==('L'if p in B else'R')
 if c=='R':birth[p]=t
 else:birth.pop(p)
 p,h=step(B,p,h)
assert mx==8 and(p,h)==((2,2),0)and not comp(B,1,cursor(p,h))
assert before==1 and fuel(B)==3
assert components(B,1)==[[(0,-2)],[(0,0),(1,-1)],[(1,1)]]
out=dict(status='AUTHOR exact one-extra-old-branch countercontrol to cap7 small-component fuel',complete_initial_seed=sorted(seed),initial_pose=[a,0],initial_mass=len(seed),literal_word='RL'+T,current_T_start_cut=2,current_T_entry_field=sorted(entry),extra_old_branch=(0,-2),incoming_hook_birth=0,peak_active_w=mx,fuel_at_T_entry=before,fuel_at_T_exit=fuel(B),final_pose=[p,h],final_full_field=sorted(B),trace=trace,scope='A single finite complete board with no mid-run supply executes RL then T. One additional old branch allows active8 and changes complete singleton-or-dimer count1->3. This refutes extending that specific cap7 potential unchanged; no cap8 nonexit, recurrence, general nonexistence of a different potential, or capture claim.')
(OUT/'one_branch_fuel_limit_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='trace'},indent=2))
