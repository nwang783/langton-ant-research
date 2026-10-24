"""One real missing guard bit branches into two at a later strict record; full archive retained."""
import json
from pathlib import Path
from check_fresh_record_trap_bridge import geometry,verify_tail,replay,D
P=Path(__file__).parent
all_catalog=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())['normal_catalog'];catalog=all_catalog[2]['records'];r0=catalog[0];J=set(map(tuple,r0['required_black']));W=r0['cycle_word'];hole=(-3,-2);seed=J-{hole}
pre_seed=(seed-{(-1,1)})|{(-1,0)};pre_B,pre_p,pre_h,pre_events=replay(pre_seed,(-1,1),1,'RL');assert(pre_B,pre_p,pre_h)==(seed,(0,0),1)
B=set(seed);p=(0,0);h=1;birth={x:['initial',x]for x in B};events=[];record_cuts=[];states={};maxlevel=-1
for t in range(309):
 if t in(0,70,71,104,308):states[t]=dict(time=t,black=sorted(B),pose=[p,h],lifetimes=[[x,birth[x]]for x in sorted(B)])
 lev=p[0]-p[1]
 if lev>maxlevel:
  maxlevel=lev;guards=[]
  for a in catalog:
   if a['normalized_heading']!=h:continue
   G=set(map(tuple,a['old_guard']));A=set(map(tuple,a['required_black']));cur={q for q in G if(p[0]+q[0],p[1]+q[1])in B}
   guards.append(dict(phase=a['phase'],required_black_missing=sorted(A-cur),required_white_black=sorted(cur-A)))
  record_cuts.append(dict(time=t,pose=[p,h],level=lev,guards=guards,remaining_initial_lifetimes=sum(v[0]=='initial'for v in birth.values()),full_black=sorted(B)))
 if t==308:break
 a='L'if p in B else'R';events.append(dict(time=t,cell=p,incoming=h,turn=a,consumed=birth.get(p)))
 if a=='L':B.remove(p);birth.pop(p);h=(h-1)%4
 else:B.add(p);birth[p]=['R',t];h=(h+1)%4
 p=(p[0]+D[h][0],p[1]+D[h][1])
word=''.join(x['turn']for x in events);assert next(i for i,(a,b)in enumerate(zip(word,W))if a!=b)==71
assert len(seed)==14 and states[104]['pose']==[(2,-2),1] and states[308]['pose']==[(4,-4),1]
assert not any(x['consumed']and x['consumed'][0]=='initial'for x in events[71:])
assert sum(e['consumed']is not None and e['consumed'][0]=='initial'for e in events[:71])==14
r104=next(x for x in record_cuts if x['time']==104);g104=next(x for x in r104['guards']if x['phase']==45)
assert g104['required_black_missing']==[(-4,1),(-4,2)] and not g104['required_white_black']
assert [x['time']for x in record_cuts]==[0,1,10,11,104,105,114,115,308]
assert all(a['required_black_missing']or a['required_white_black']for r in record_cuts[:-1]for a in r['guards'])
assert not any(next(x for x in record_cuts[-1]['guards']if x['phase']==45)[k]for k in('required_black_missing','required_white_black'))
# At these actual cuts no other properly rotated catalog guard quietly captures earlier.
def rotate(v,r):
 x,y=v
 for _ in range(r):x,y=y,-x
 return(x,y)
for cut in record_cuts:
 head,hh=cut['pose'];current=set(map(tuple,cut['full_black']));matches=[]
 for block in all_catalog:
  for rec in block['records']:
   for rot in range(4):
    if(rec['normalized_heading']+rot)%4!=hh:continue
    n=rotate(block['outward_normal'],rot)
    if any(sum(n[j]*(x[j]-head[j])for j in range(2))>=0 for x in current):continue
    G={tuple(rotate(x,rot)[j]+head[j]for j in range(2))for x in rec['old_guard']}
    A={tuple(rotate(x,rot)[j]+head[j]for j in range(2))for x in rec['required_black']}
    if current&G==A:matches.append([block['outward_normal'],rec['phase'],rot])
 cut['all_32_rotated_catalog_matches']=matches
 assert bool(matches)==(cut['time']==308)
# Full compared boards, no removal of side output.
base=set(J);bp=(0,0);bh=1;base_events=[]
for t,a in enumerate(W):
 assert(bp in base)==(a=='L');base_events.append([t,bp,a]);base^={bp};bh=(bh+(1 if a=='R'else-1))%4;bp=(bp[0]+D[bh][0],bp[1]+D[bh][1])
actual104=set(map(tuple,states[104]['black']));assert actual104-base=={(-4,-2),(-4,-1)} and base-actual104=={(-3,0),(-2,-1),(-2,0)}
# The fresh R lifetime at the first new hole was born69, erased81; the other lacks the baseline birth80.
assert events[69]['cell']==(-2,-1)and events[69]['turn']=='R'
assert events[81]['cell']==(-2,-1)and events[81]['consumed']==['R',69]
assert base_events[80]==[80,(-2,0),'R'] and events[80]['cell']!=(-2,0)
assert [e['time']for e in events[:104]if e['cell']==(-2,0)]==[60,68]
# Complete actual tail, not only local guard matches.
assert all(x-y<8 for x,y in B);Q,d,tests=verify_tail(B,p,h,W);assert d==(2,-2)
result=dict(status='AUTHOR exact finite successive-record regeneration control and all-future capture, independent audit pending',initial_seed=sorted(seed),initial_pose=[(0,0),1],genuine_record_preparation=dict(initial_seed=sorted(pre_seed),initial_pose=[(-1,1),1],word='RL',events=pre_events,time_convention='All subsequent times measured from the new record cut after these2moves'),word_to_capture=word,capture_time=308,capture_pose=[p,h],period=W,drift=d,infinite_tail_tests=tests,events=events,record_cuts=record_cuts,selected_full_states=states,full_baseline_state104=sorted(base),complete_discrepancy104=dict(extra_actual_black=sorted(actual104-base),missing_actual_black=sorted(base-actual104)),first_deviation=71,last_initial_lifetime_retirement=70,new_guard_defects=dict(erased_fresh_lifetime=dict(cell=(-2,-1),birth=69,death=81),skipped_fresh_birth=dict(cell=(-2,0),baseline_birth=80,actual_previous_birth=60,actual_previous_death=68)))
(P/'SUCCESSIVE_RECORD_DEFECT_SPLIT_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n')
print(dict(initial_mass=14,first_deviation=71,old_cohort_exhausted=70,record_cuts=[r['time']for r in record_cuts],full_mass104=len(actual104),full_mass308=len(B),capture=308))
