"""Two exact C4 marker-owned hook-retirement gates are impossible.
Actual ordinary C age, no foreign reset, U ancestry or simplicity premise.
"""
from pathlib import Path
import importlib.util,json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
o=load('owner',ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return (*q,h)
def S_counts(dx,dy):
 if dx<0 or dy<0:return[]
 out=[]
 for d in range(dx+1):
  v=dx-d;r=dy-d-3*v
  if r>=0 and r%4==0:out.append((d,v,r//4))
 return out

def guard(tag,target):
 rows=[]
 for a in'DVU':
  tr=l.trace(W[a]+l.M)
  for slot in map(tuple,l.literal_geometry(W[a])['inputs']):
   p=(*sub(tag,l.rot(slot,2)),2);ep=after(W[a],p)
   dx,dy=ep[0]-target[0],ep[1]-target[1]
   counts=S_counts(dx,dy);assert not counts
   rows.append(dict(guard_original=tag,consumer=a,true_input=slot,consumer_ENTRY=p,actual_RAW_EXIT=ep,actual_physical_L=o.describe(a,tr['first'][slot][1]),remaining_S_weights=(dx,dy),all_nonnegative_remaining_D_V_U_counts=counts))
 assert len(rows)==8
 return rows
cases=[]
for source in'FQB':
 trace=l.trace(W[source])
 source_cases=[dict(marker_tag=(-2,-1),source_guard=(-1,-1),target=(-3,-1,2),route='guard_BLACK_at_shared_FOREIGN_first_R44')]
 if source in'QB':source_cases.append(dict(marker_tag=(-3,-2),source_guard=(-3,-1),target=(-4,-2,2),route='guard_CURRENT_in_FOREIGN_ENTRY_CORE'))
 for base in source_cases:
  tag=base['marker_tag'];g=base['source_guard'];p=base['target']
  assert trace['last'][tag][0]==trace['last'][g][0]=='R'
  rows=guard(g,p)
  readers=[]
  for actor in'FQB':
   tr=l.trace(W[actor]+l.M);q=l.rot(sub(tag,p[:2]),2);assert q==(-1,0)and tr['first'][q]==('L',1)
   qg=l.rot(sub(g,p[:2]),2)
   if base['route'].startswith('guard_BLACK'):
    assert qg==(-2,0)and tr['first'][qg]==('R',44)
   else:assert qg==(-1,-1)and qg in l.K
   readers.append(dict(actor=actor,FOREIGN_ENTRY=p,original_marker_tag=tag,marker_tag_local=q,actual_FOREIGN_old_tag_L=o.describe(actor,1),protected_guard_original=g,guard_local=qg,guard_failure=base['route'],guard_first_actual_read=o.describe(actor,tr['first'][qg][1])))
  prev=[]
  # The marker-owned ordinary upper-input roles really exist; no selected
  # own-L input is confused with the next foreign's physical L1/read2.
  for a in'DVU':
   ep=after(W[a]);entry=(*sub(p[:2],l.rot(ep[:2],2)),2)
   slot=l.rot(sub(tag,entry[:2]),2);raw=l.trace(W[a]);ct=l.trace(W[a]+l.M)
   if slot in ct['first']and ct['first'][slot]==('L',len(W[a])+1):
    assert slot not in raw['last']
    prev.append(dict(previous_atom=a,actual_ENTRY=entry,actual_RAW_EXIT=p,marker_only_original_tag_slot=slot,physical_L=o.describe(a,len(W[a])+1),original_tag_physically_unread_by_previous_RAW=True))
  assert {x['previous_atom']for x in prev}=={'D','V','U'}
  cases.append(dict(source_foreign=source,source_ENTRY=(0,0,0),old_marker_tag=tag,source_tag_R_tick0=trace['last'][tag][1],guard_original=g,source_guard_R_tick0=trace['last'][g][1],candidate_FOREIGN_ENTRY=p,all8_first_S4_guard_loss_exits=rows,all3_NEXT_FOREIGN_reader_conflicts=readers,all3_genuine_marker_owned_predecessor_roles=prev))
assert len(cases)==5
assert sum(len(x['all3_NEXT_FOREIGN_reader_conflicts'])for x in cases)==15
D=['foreign_three_C_NE_reserve_2026-10-24/manifest.json','audits/check_foreign_three_C_NE_reserve_independent.json','foreign_hook_four_C_maturity_2026-10-24/manifest.json','audits/check_hook_four_C_maturity_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
result=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual source F/Q/B ENTRY0N, only ordinary RAWs containing exactly4 actual Cs, then next complete F/Q/B RAW+actualM. SourceF/Q/B cannot complete the next foreign at recipient ENTRY(-3,-1,S); sourceQ/B also cannot complete it at recipient ENTRY(-4,-2,S). These are two selected original-hook marker-loss gates, not all C4 gates. No U-entry, global-first-contact, simplicity, epoch-length or earlier-history premise.',
 all5_source_gate_cases=cases,
 common_all_length_argument='Signedf24 keeps sourceR46(-1,-1) CURRENT through ordinaryC3 for any sourceF/Q/B; signed528 keeps sourceQ/B hookR50(-3,-1) CURRENT throughC3. C4 hasI0 and cannot consume or silently capture a CURRENT external original. Any subsequent first loss before the selected recipient must therefore be a genuine D/V/U true input in the final S4 epoch. All8 actual RAW exits and every nonnegative following S D/V/U count are checked. None reaches the recipient pose. Hence the specified guard original is stillCURRENT there. This includes marker-owned CORE capture before its later physical L.',
 marker_ownership='In both selected gates the intended odd hook original is local(-1,0) of the recipientFOREIGN and is physically read L at that FOREIGN own tick1/read2. It can have entered the previous ordinary RAW exitCORE through its marker-only upper slot. The reader table retains these genuine D/V/U marker-only roles; D is separately impossible beforeFOREIGN in complete histories but is not silently omitted from this guard.',
 failure_distinction='At recipient(-3,-1,S), sourceR46 is local(-2,0); every nextFOREIGN first requests it WHITE at ownR44. The intended oldR47 may already have died at recipientL1 in a partial attempted word, but the fullFOREIGN cannot complete. At recipient(-4,-2,S), sourceR50 is local(-1,-1) ENTRY_CORE, incompatible with its provenCURRENT state. No assertion of physical permanence beyond the failure is made.',
 not_claimed=['No all-C4 or C4-plus hook/star-loss exclusion.','No arbitrary longer-cycle or all-length source-F pair seal.','No interpretation of a partial attempted FOREIGN as a completed word.','No geometric first-contact assumption or conclusion; actual marker ownership is independent.','No identity preservation through a further foreign, language coverage or capture.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'C4_marker_gate.json').write_text(json.dumps(result,indent=2)+'\n')
print('Two selected C4 marker-hook gates:5 source cases,15 nextFOREIGN readers; each guard8 S4 loss exits has empty suffix semigroup. Marker L is actualFOREIGN tick1/read2; no allC4 claim.')
