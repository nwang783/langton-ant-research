from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'SUCCESSIVE_RECORD_DEFECT_SPLIT_MANIFEST.json';m=json.loads(mf.read_text())
for f,h in m.items():assert sha(P/f)==h
ref=json.loads((P/'SUCCESSIVE_RECORD_DEFECT_SPLIT_CHECKED.json').read_text());cat=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())['normal_catalog'];phase45=next(z for tab in cat for z in tab['records']if tab['outward_normal']==[1,-1]and z['phase']==45)
x={'__file__':str(S.parent/'check_eleven_cell_terminal_trap_independent.py')};src=(S.parent/'check_eleven_cell_terminal_trap_independent.py').read_text();exec(src[:src.index('B,p,h,reads,dead=replay(I,0j,2,C)')],x);replay=x['replay'];tail=x['tail'];xy=x['xy'];V=x['V'];W=phase45['cycle_word'];x['H']=W
J={complex(*q)for q in phase45['required_black']};seed=J-{-3-2j};assert len(seed)==14 and seed=={complex(*q)for q in ref['initial_seed']}
prep=(seed-{-1+1j})|{-1};b,p,h,_,_=replay(prep,-1+1j,1,'RL');assert(b,p,h)==(seed,0j,1)and len(prep)==14 and max(q.real-q.imag for q in prep)==-1
board=set(seed);p=0j;h=1;born={q:['initial',list(xy(q))]for q in seed};events=[];states={};records=[];maxlevel=max(q.real-q.imag for q in seed)
for time in range(309):
 states[time]=(set(board),p,h,{q:v[:]for q,v in born.items()})
 n=p.real-p.imag
 if n>maxlevel:
  maxlevel=n;matches=[]
  for tab in cat:
   normal=complex(*tab['outward_normal'])
   for guard in tab['records']:
    for rot in range(4):
     z=(-1j)**rot;nn=normal*z
     if(guard['normalized_heading']+rot)%4!=h:continue
     dot=lambda q:nn.real*q.real+nn.imag*q.imag
     if any(dot(q-p)>=0 for q in board):continue
     G={p+complex(*q)*z for q in guard['old_guard']};A={p+complex(*q)*z for q in guard['required_black']}
     if board&G==A:matches.append([tab['outward_normal'],guard['phase'],rot])
  old=next(a for a in ref['record_cuts']if a['time']==time);assert old['all_32_rotated_catalog_matches']==matches and old['full_black']==sorted(map(list,map(xy,board)))and old['pose']==[list(xy(p)),h]
  assert bool(matches)==(time==308)
  records.append({'time':time,'head':xy(p),'heading':h,'level':int(n),'all32_rotated_matches':matches,'remaining_initial_lifetimes':sum(v[0]=='initial'for v in born.values())})
 if time==308:break
 c='L'if p in board else'R';consumed=born.get(p);rec={'time':time,'cell':list(xy(p)),'incoming':h,'turn':c,'consumed':consumed};assert rec==ref['events'][time];events.append(rec)
 if c=='L':board.remove(p);del born[p]
 else:board.add(p);born[p]=['R',time]
 h=(h+(1 if c=='R'else-1))%4;p+=V[h]
word=''.join(z['turn']for z in events);assert word==ref['word_to_capture']and next(i for i,c in enumerate(word[:104])if c!=W[i])==71
assert [r['time']for r in records]==[0,1,10,11,104,105,114,115,308]and[ r['level']for r in records]==list(range(9))
for time,old in ref['selected_full_states'].items():
 B,p,h,life=states[int(time)];assert sorted(map(list,map(xy,B)))==old['black']and[list(xy(p)),h]==old['pose']and[[list(xy(q)),life[q]]for q in sorted(B,key=xy)]==old['lifetimes']
olddeaths=[e['time']for e in events if e['consumed']and e['consumed'][0]=='initial'];assert len(olddeaths)==14 and max(olddeaths)==70
base,bp,bh,base_reads,_=replay(J,0j,1,W);actual,p104,h104,_=states[104];assert(bp,bh)==(p104,h104)==(2-2j,1)and(len(actual),len(base))==(26,27)
assert actual-base=={-4-2j,-4-1j}and base-actual=={-3,-2-1j,-2}
G={complex(*q)for q in phase45['old_guard']};missing=J-{q-p104 for q in actual if q-p104 in G};extra={q-p104 for q in actual if q-p104 in G}-J
assert missing=={-4+1j,-4+2j}and not extra
assert events[61]['cell']==[-2,-1]and events[61]['consumed']==['initial',[-2,-1]]
assert events[69]['cell']==[-2,-1]and events[69]['turn']=='R'and events[81]['consumed']==['R',69]
assert events[60]['cell']==[-2,0]and events[60]['turn']=='R'and events[68]['consumed']==['R',60]and base_reads[80]==-2 and W[80]=='R'and events[80]['cell']!=[-2,0]
B308,p308,h308,_=states[308];assert(len(B308),p308,h308)==(54,4-4j,1)and all(q.real-q.imag<8 for q in B308)
Q,d,proof308=tail(B308,p308,h308);assert d==2-2j
# Do not confuse the convenient guard entry308 with the earliest aligned periodic word.
bad=[i for i,c in enumerate(word)if c!=W[(i-308)%104]];assert bad[-1]==261;entry=262;offset=(entry-308)%104;rotated=W[offset:]+W[:offset];x['H']=rotated
B262,p262,h262,_=states[262];Q2,d2,proof262=tail(B262,p262,h262);assert d2==2-2j;x['H']=W
out={'status':'PASS actual finite one-defect-to-two-defect production and all-future capture; guard entry308 is NOT earliest standard word onset','bindings':m,'complete_seed':sorted(map(xy,seed)),'all14_old_lifetimes_consumed_by':70,'first_deviation':71,'actual104_mass':26,'baseline104_mass':27,'complete104_extra_actual':sorted(map(xy,actual-base)),'complete104_missing_actual':sorted(map(xy,base-actual)),'actual104_guard_holes':sorted(map(xy,missing)),'fresh_defect_mechanisms':{'first':{'original_death':61,'new_birth':69,'new_death':81},'second':{'actual_birth':60,'actual_death':68,'skipped_baseline_birth':80}},'all_full_record_checks':records,'certified_phase45_guard_entry':308,'certified_complete_board_mass308':54,'all_infinite_ray_tests308':sum(len(z['all_change_point_tests'])for z in proof308),'additional_direct_periodic_word_start262':{'last_disagreeing_backward_aligned_turn':261,'head':xy(p262),'heading':h262,'full_mass':len(B262),'all_infinite_ray_tests':sum(len(z['all_change_point_tests'])for z in proof262)},'analytic_review':[
'The14-cell seed and explicit14-cell RL preparation were replayed from complete fields. Every one of308 actual reads, incoming headings, current lifetime births/deaths, selected full board and all9 record cuts agrees with the frozen certificate. There is no added later guide or discarded exterior archive.',
'One missing phase45 guard bit becomes exactly two missing black guard bits at the next same-pose strict record104. The COMPLETE discrepancy is five cells, including three exterior differences. Thus this is a finite defect production map, not a closed19-bit recurrence. All14 initial black lifetimes died by70; divergence begins71. The two new guard holes come from erasing a genuineR69 lifetime at81 and skipping the baselineR80 birth, not contemporary old-cohort retirements.',
'All32 proper rotations of eight catalog guards were tested with actual heading, whole-field pristine half-plane and all guard bits at each selected record. None holds at the first8 cuts. The full54-cell board at308 satisfies phase45 and exact infinite phase/ray parity. Other non-record cuts are not excluded as guard opportunities.',
'Precision qualification:308 is the convenient certified phase45 record-guard entry, not an earliest capture time. The actual word already agrees with the same backward-aligned H tail from262, last mismatch261. Direct infinite-tail verification on the complete actual262 board also passes. Including RL preparation these certified times shift by2. This strengthens no global conclusion; original literal fields remain unchanged.',
'The control refutes raw defect-count monotonicity and simultaneous distinct-old-token charging at defect production, not amortized earlier-input credits, a different cohort, a richer potential, or eventual standard capture. It actually captures. No repeatable noncapture or unrestricted regeneration invariant is asserted.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
