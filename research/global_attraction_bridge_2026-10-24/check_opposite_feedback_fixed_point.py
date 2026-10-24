"""One exact actual self-written feedback loop: whole-state recurrence constraints and finite obstruction."""
from pathlib import Path
import json,hashlib,collections
from check_return_permanent_output_debt import DXY,future
from record_event_projection import trace
P=Path(__file__).parent;source=json.load(open(P/'OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json'));c=source['controls'][2]
assert c['residue']==[3,3]
s=49729;t=55541;period=t-s;W=c['actual_transient'][:period];origin=(112,105);dest=(44,177);h0=0
Q,d,eh=trace(W,(0,0),h0);assert period==5812 and d==(-68,72)and eh==h0
# Fresh literal full-board replay, preserving every BLACK identity and all subsequent fates.
seed=set(map(tuple,c['initial_black']));B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;death={};born={};snap={};word=[];selected={(43,178),(43,173),origin,dest};visits={q:[]for q in selected}
for n in range(c['physical_updates']):
 if n in(s,t,c['actual_exact_onset']):snap[n]=(dict(B),p,h)
 old=B.pop(p,None);ch='R'if old is None else'L';word.append(ch)
 if p in visits:visits[p].append([n,ch,old])
 if old is None:B[p]=n;born[n]=p
 else:death[old]=n
 h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
snap[c['physical_updates']]=(dict(B),p,h)
tail,dr,ft,tests=future(B,p,h);assert tail==c['actual_word'];death.update({i:c['physical_updates']+u for i,u in ft.items()})
assert ''.join(word[s:c['actual_exact_onset']])==c['actual_transient']
assert (snap[s][1],snap[s][2])==(origin,0)and(snap[t][1],snap[t][2])==(dest,0)
for tm,key,relkey in [(s,'first_contact_full','first_contact_relevant'),(t,'discrepancy_full','discrepancy_relevant')]:
 bb,pp,hh=snap[tm];assert{tuple(z['cell']):z['lifetime']for z in c[key]}==bb
 for z in c[key]:assert death.get(z['lifetime'])==z['death']
 rel={q for q,i in bb.items()if i in death};assert rel==set(map(tuple,c[relkey]))
assert B=={tuple(z['cell']):z['lifetime']for z in c['full_terminal_black']}
C0=set(map(tuple,c['first_contact_relevant']));C1=set(map(tuple,c['discrepancy_relevant']));translated={(x+d[0],y+d[1])for x,y in C0}
assert len(C0)==234 and len(C1)==144 and len(translated-C1)==170 and len(C1-translated)==80
oldsurviving={q for q in C1 if snap[t][0][q]<s};newrelevant=C1-oldsurviving
assert len(oldsurviving)==90 and len(newrelevant)==54
first={};T=set();orbits=collections.defaultdict(list)
for i,q in enumerate(Q):
 first.setdefault(q,[i,W[i]]);T.symmetric_difference_update({q})
 x,y=q;r=x%68;a=(x-r)//(-68);rep=(r,y-a*72);orbits[rep].append((a,i,W[i]))
assert len(first)==1210 and sum(v[1]=='L'for v in first.values())==144
# Full-field first-read requirements for the desired next W, not the actual-C* crop.
port_bad=[]
for q,(i,ch)in sorted(first.items(),key=lambda z:z[1][0]):
 absq=(dest[0]+q[0],dest[1]+q[1]);actual='L'if absq in snap[t][0]else'R'
 if actual!=ch:port_bad.append(dict(offset=i,cell=absq,required=ch,current=actual,current_lifetime=snap[t][0].get(absq)))
assert len(port_bad)==127 and sum(z['required']=='L'for z in port_bad)==61 and sum(z['required']=='R'for z in port_bad)==66
assert port_bad[0]['offset']==2 and port_bad[0]['cell']==(43,178)and port_bad[0]['required']=='L'
assert visits[(43,178)][:6]==[[18835,'R',None],[18843,'L',18835],[18847,'R',None],[18955,'L',18847],[18963,'R',None],[18971,'L',18963]]
first_actual_mismatch=next(i for i in range(min(period,len(word)-t))if W[i]!=word[t+i]);assert first_actual_mismatch==2
# The exact putative recurring-pruning equations on the WHOLE prescribed future footprint.
# E_r={r+k*d:k>=min a_i}. Finite support forces s(k)=XOR_{j>k}t(j).
S=set();Emin={};equations=[];leading_L=[];intrinsic=[]
for r,rows in sorted(orbits.items()):
 parity=collections.Counter(a for a,i,ch in rows);lo=min(parity);hi=max(parity);Emin[r]=lo;bit=0
 for k in range(hi,lo-1,-1):
  if bit:S.add((r[0]+k*d[0],r[1]+k*d[1]))
  eq=bool(parity[k]%2);equations.append(dict(rep=r,index=k,visit_parity=int(eq),entry_bit=int(bit)));bit^=eq
 ordered=sorted(rows,key=lambda z:z[1]-period*z[0])
 if ordered[0][2]=='L':leading_L.append(dict(rep=r,phase=ordered[0][1],index=ordered[0][0]))
 for a,b in zip(ordered,ordered[1:]):
  if a[2]==b[2]:intrinsic.append(dict(rep=r,earlier=a,later=b))
def in_future(q,shift=0):
 x,y=q;r0=x%68;a=(x-r0)//(-68);rep=(r0,y-a*72)
 return rep in Emin and a>=Emin[rep]+shift
assert all(in_future(q)for q in S)
SS={(x+d[0],y+d[1])for x,y in S};after=S^T
assert{q for q in after if in_future(q,1)}==SS
permanent_candidate=after-SS;assert all(not in_future(q,1)for q in permanent_candidate)
assert len(orbits)==1160 and len(S)==35 and len(T)==654 and len(permanent_candidate)==620 and len(leading_L)==115 and len(intrinsic)==30
assert (0,0)not in S and W[0]=='L'
assert orbits[(0,0)]==[(0,0,'L')]
assert snap[s][0][origin]==5605 and snap[s][0][dest]==18845 and snap[t][0][dest]==18845
assert (origin[0]+2*d[0],origin[1]+2*d[1])not in snap[s][0] and (origin[0]+2*d[0],origin[1]+2*d[1])not in snap[t][0]
# Find the earliest impossible consecutive-read obligation in the desired TWO-copy word.
last={};counter_positions,dd,hh=trace(W*2,(0,0),0);conflict=None
for i,q in enumerate(counter_positions):
 ch=(W*2)[i]
 if q in last and last[q][1]==ch:conflict=dict(cell=q,earlier_tick=last[q][0],later_tick=i,earlier_turn=ch,later_turn=ch);break
 last[q]=(i,ch)
assert conflict==dict(cell=(-69,68),earlier_tick=5733,later_tick=6745,earlier_turn='R',later_turn='R')
assert[(i,W[i])for i,q in enumerate(Q)if q==(-69,68)]==[(5733,'R')]
assert[(i,W[i])for i,q in enumerate(Q)if q==(-1,-4)]==[(933,'R'),(945,'L'),(961,'R'),(965,'L'),(997,'R')]
# Every cell's desired consecutive reads alternate strictly before the certified first conflict.
assert all(counter_positions[i]!=(-69,68)for i in range(5734,6745))
assert visits[(43,173)][0]==[55462,'R',None]
# Retain complete boards and all lifetime fates at each meaningful actual cut.
boards=[]
for tm,(bb,pp,hh)in sorted(snap.items()):boards.append(dict(cut=tm,pose=[pp,hh],full_black=[dict(cell=q,lifetime=i,death=death.get(i))for q,i in sorted(bb.items())],whole_actual_relevant=sorted(q for q,i in bb.items()if i in death)))
files=['OPPOSITE_TRANSVERSE_FEEDBACK_MANIFEST.json','OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json','../audits/check_opposite_transverse_feedback_independent.json','OPPOSITE_PREHISTORY_OBSTRUCTION_MANIFEST.json','../audits/check_opposite_prehistory_independent.json','record_event_projection.py','check_return_permanent_output_debt.py']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR exact one-feedback-loop obstruction; independent audit pending',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},
 initial_black=sorted(seed),actual_physical_reads=len(word),actual_full_word=''.join(word),contact_start=s,contact_end=t,period=period,loop_word=W,drift=d,heading=0,
 actual_full_snapshots=boards,actual_infinite_tail_word=tail,actual_tail_drift=dr,tail_parity_tests=tests,
 actual_relevant_comparison=dict(entry=234,exit=144,old_survivors=sorted(oldsurviving),new_relevant=sorted(newrelevant),missing_translated_entry=sorted(translated-C1),extra_current_relevant=sorted(C1-translated)),
 actual_fixed_preparation_port=dict(cell=[43,178],last_preparation_read=18971,last_turn='L',desired_next_offset=2,visits=visits[(43,178)]),
 desired_next_full_field_port_disagreements=port_bad,first_actual_repetition_mismatch=first_actual_mismatch,
 prescribed_loop_footprint=dict(read_cells=1210,first_black_inputs=144,drift_orbits=1160,odd_toggled_cells=654),
 finite_renewal_equations=equations,unique_candidate_relevant=sorted(S),candidate_permanent_output=sorted(permanent_candidate),candidate_first_mismatch=dict(tick=0,cell=[0,0],required='L',forced='R'),
 stable_first_L_orbits=leading_L,bulk_alternation_conflicts=intrinsic,earliest_two_copy_conflict=conflict,
 actual_marker_lifetime=dict(cell=[44,177],birth=18845,death=55541),marker_orbit=dict(single_one_cycle_visit=[0,0,'L'],first_marker=[112,105],old_second_marker=[44,177],missing_third_marker=[-24,249],marker_regeneration=False),
 scope='Only the exact5812 actual contact-to-contact word and its translation recurrence. W^2 is impossible on ANY board by an intrinsic consecutive-R contradiction. Actual future pruning and counterfactual periodic-footprint pruning are kept separate. Different loop words, altered preparations, intervening routing and global attraction remain open.')
(P/'OPPOSITE_FEEDBACK_FIXED_POINT_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS author: full actual57885; exact5812-loop two-copy contradiction6745; finite pruned candidate35 rejects first L',flush=True)
