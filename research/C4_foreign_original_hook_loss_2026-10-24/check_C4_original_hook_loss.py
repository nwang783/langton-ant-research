"""Upper-cohort three-C reserve and C4 next-FOREIGN original-hook loss.
No search depth, global simplicity, U ancestry, or unchanged full-field claim.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
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
def local(q,p):return l.rot(sub(q,p[:2]),(-p[2])%4)
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)}
UPPER={(-4,1),(-4,2),(-3,2),(-2,1)}
F15=NE|UPPER|{(-2,-1)};HOOK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)}
assert len(F15)==15
sources=[]
for a in'FQB':
 tr=l.trace(W[a]);O=set(map(tuple,l.literal_geometry(W[a])['outputs']));assert F15<=O
 assert tr['last'][(-4,3)]==('L',35)
 protected={(-1,-1),(-2,-1)} if a=='F' else HOOK
 assert protected<=O and all(tr['last'][q][0]=='R'for q in protected)
 sources.append(dict(source=a,ENTRY=(0,0,0),EXIT=after(W[a]),all_protected_hook_R_births=[dict(cell=q,own_tick0=tr['last'][q][1])for q in sorted(protected)],all15_actual_source_R_births=[dict(cell=q,own_tick0=tr['last'][q][1])for q in sorted(F15)],left_hole=(-4,3),left_hole_last_L_own_tick0=35))
# First loss of ANY of the fifteen originals through ordinary C3.
first=[]
for heading in(0,3):
 for g in sorted(F15):
  for atom in'DVU':
   tr=l.trace(W[atom]+l.M)
   for slot in map(tuple,l.literal_geometry(W[atom])['inputs']):
    p=(*sub(g,l.rot(slot,heading)),heading);row=dict(heading=heading,original=g,consumer=atom,true_input=slot,ENTRY=p,actual_L=o.describe(atom,tr['first'][slot][1]))
    if(sum(p[:2])+heading)%2:route='sector'
    else:
     bad=[]
     for held in sorted(F15):
      q=local(held,p);f=tr['first'].get(q)
      if q in l.K or f and f[0]=='R':bad.append(dict(original=held,local=q,first=f,reason='ENTRY_CORE'if q in l.K else'first_WHITE'))
     row['conflicts']=bad;route='held_field'if bad else'first_loss_gate'
    row['route']=route;first.append(row)
assert len(first)==240
assert Counter(r['route']for r in first if r['heading']==0)=={'sector':54,'held_field':64,'first_loss_gate':2}
assert Counter(r['route']for r in first if r['heading']==3)=={'sector':66,'held_field':51,'first_loss_gate':3}
kept={(r['consumer'],r['ENTRY'],r['original'])for r in first if r['route']=='first_loss_gate'}
assert kept=={('U',(3,-1,0),(2,0)),('U',(3,-1,0),(2,1)),('U',(2,3,3),(1,2)),('U',(-2,3,3),(-4,2)),('U',(-2,3,3),(-3,2))}
left_hole=(-4,3);left_gate=(-2,3,3);lg_slot=local(left_hole,left_gate)
assert lg_slot==(0,2)and l.trace(W['U']+l.M)['first'][lg_slot]==('L',12)
R_bounds=[]
for a in'DCVU':
 p=(0,0,0);ep=after(W[a]);rs=[]
 for t,c in enumerate(W[a]):
  if c=='R':
   q=p[:2];assert q[1]>=0 and q[0]>=-1
   if a=='C':assert q[0]>=0
   else:assert q[1]<=ep[1]
   rs.append(dict(own_tick0=t,physical_local_cell=q))
  p=after(c,p)
 R_bounds.append(dict(atom=a,actual_RAW_EXIT=ep,all_physical_R_supports=rs))
new9={add((3,-1),tuple(q))for q in l.literal_geometry(W['U'])['outputs']}
old13=F15-{(2,0),(2,1)}
assert len(old13)==13 and len(new9)==9 and not old13&new9 and max(q[1]for q in old13|new9)==2
for q in old13:assert local(q,(3,-1,0))not in l.trace(W['U']+l.M)['first']
assert l.literal_geometry(W['C'])['inputs']==[]
# Individual CURRENT fact at an S4 cut, from CURRENT at S4 start.
# All8 genuine first-loss exits and every nonnegative remaining S count.
def S_counts(dx,dy):
 if dx<0 or dy<0:return[]
 out=[]
 for d in range(dx+1):
  v=dx-d;r=dy-d-3*v
  if r>=0 and r%4==0:out.append((d,v,r//4))
 return out
proofs={}
@lru_cache(None)
def current_proof(g,p):
 rows=[];possible=False
 for a in'DVU':
  ct=l.trace(W[a]+l.M)
  for slot in map(tuple,l.literal_geometry(W[a])['inputs']):
   entry=(*sub(g,l.rot(slot,2)),2);ep=after(W[a],entry);sector=(sum(entry[:2])+2)%2==0
   counts=S_counts(ep[0]-p[0],ep[1]-p[1])if sector else[]
   possible|=bool(counts)
   rows.append(dict(consumer=a,input=slot,ENTRY=entry,RAW_EXIT=ep,active_sector=sector,actual_L=o.describe(a,ct['first'][slot][1]),remaining_S_count_tuples=counts))
 key=str((g,p));proofs[key]=dict(tag=g,S4_cut=p,guaranteed_CURRENT=not possible,all8_first_loss_exit_rows=rows)
 return None if possible else key

def field_conflicts(atom,p,field):
 ct=l.trace(W[atom]+l.M);out=[]
 for g in sorted(field):
  proof=current_proof(g,p)
  if proof is None:continue
  q=local(g,p);f=ct['first'].get(q)
  if q in l.K or f and f[0]=='R':out.append(dict(guaranteed_CURRENT_original=g,current_endpoint_proof=proof,local=q,reason='ENTRY_CORE'if q in l.K else'first_WHITE',actual_first=f))
 return out

branches={'unspent':F15,'N2_paired':old13|new9};source_records=[]
for source in'FQB':
 hook={(-1,-1),(-2,-1)}if source=='F'else HOOK
 goals={}
 for actor in'FQB':
  tr=l.trace(W[actor]+l.M)
  for g in sorted(hook):
   # A SAME physically BLACK original must first be read L. Entry CORE
   # and marker-only physical reads are INCLUDED, not discarded.
   for slot,(turn,t)in tr['first'].items():
    if turn!='L':continue
    p=(g[0]+slot[0],g[1]+slot[1],2)
    if(sum(p[:2])+2)%2:continue
    goals.setdefault((actor,p),[]).append(dict(original_hook_cell=g,first_L_slot=slot,actual_L=o.describe(actor,t)))
 assert len(goals)==(49 if source=='F'else 68)
 for branch,basefield in branches.items():
  field=basefield|hook;rows=[];counts=Counter()
  for(actor,p),witness in sorted(goals.items()):
   row=dict(source=source,C3_state_branch=branch,actor=actor,FOREIGN_ENTRY=p,possible_same_original_first_L=witness)
   conflicts=field_conflicts(actor,p,field)
   if conflicts:
    row.update(route='FOREIGN_current_field',conflicts=conflicts);counts['FOREIGN_current_field']+=1
   else:
    types=[]
    for previous in'VU':
     pair=l.trace(W[previous]+W[actor]+l.M)
     if not pair['feasible']:
      types.append(dict(previous=previous,route='previous_FOREIGN_literal_conflict',conflict=pair));counts['previous_FOREIGN_literal_conflict']+=1;continue
     delta=l.rot(after(W[previous])[:2],2);pre=(*sub(p[:2],delta),2)
     pr=l.trace(W[previous]);alive=[w for w in witness if local(w['original_hook_cell'],pre)not in pr['last']]
     if not alive:
      types.append(dict(previous=previous,previous_ENTRY=pre,route='previous_RAW_already_touched_every_original_candidate'));counts['previous_RAW_already_touched']+=1;continue
     bad=field_conflicts(previous,pre,field)
     if bad:
      types.append(dict(previous=previous,previous_ENTRY=pre,route='previous_current_field',conflicts=bad));counts['previous_current_field']+=1;continue
     carry=[];act=l.trace(W[actor]+l.M)
     for g in sorted(field):
      proof=current_proof(g,pre)
      if proof is None:continue
      prevlocal=local(g,pre);targetlocal=local(g,p);f=act['first'].get(targetlocal)
      if prevlocal not in pr['last']and f and f[0]=='R':
       carry.append(dict(original=g,CURRENT_at_previous_ENTRY_proof=proof,previous_local_cell=prevlocal,physically_UNREAD_by_previous_RAW=True,FOREIGN_local_cell=targetlocal,actual_first_WHITE=o.describe(actor,f[1])))
     assert carry,(source,branch,actor,p,previous,pre,alive)
     types.append(dict(previous=previous,previous_ENTRY=pre,route='carried_SAME_BLACK_through_previous_RAW',surviving_original_candidates=alive,conflicts=carry));counts['carried_SAME_BLACK']+=1
    row.update(route='last_actual_base_split',previous_types=types)
   rows.append(row)
  if source=='F':assert counts=={'FOREIGN_current_field':48,'previous_FOREIGN_literal_conflict':1,'carried_SAME_BLACK':1}
  else:assert counts=={'FOREIGN_current_field':66,'previous_FOREIGN_literal_conflict':2,'previous_current_field':1,'carried_SAME_BLACK':1}
  source_records.append(dict(source=source,C3_state_branch=branch,all_current_at_S4_start=sorted(field),unique_recipient_pose_count=len(goals),disjoint_cut_counts=dict(counts),all_recipient_pose_rows=rows))
assert len(source_records)==6
# Only endpoint proofs actually cited by a contradiction are retained as
# the guaranteed-CURRENT interface; unused possible-loss ports are not
# erased from the physical state or called dead.
captures=[]
for a in'FQB':
 ep=after(W[a]);rt=l.trace(W[a]);ct=l.trace(W[a]+l.M)
 for q in sorted({add(ep[:2],l.rot(v,ep[2]))for v in l.K}):
  if q not in l.K and q not in rt['last']:
   assert ct['first'][q][0]=='L'and list(q)in l.literal_geometry(W[a])['inputs']
  captures.append(dict(actor=a,RAW_EXIT_CORE_cell=q,in_ENTRY_CORE=q in l.K,RAW_last_read=rt['last'].get(q),complete_first_read=ct['first'].get(q)))
assert len(captures)==15
D=['foreign_Q_B_hook_contact_reserve_2026-10-24/manifest.json','audits/check_foreign_hook_reserve_independent.json','foreign_three_C_NE_reserve_2026-10-24/manifest.json','audits/check_foreign_three_C_NE_reserve_independent.json','foreign_hook_four_C_maturity_2026-10-24/manifest.json','audits/check_hook_four_C_maturity_independent.json','foreign_interval_packet_grammar_2026-10-24/manifest.json','audits/check_foreign_interval_grammar_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual source F/Q/B ENTRY0N, ordinary RAW section with exactly4 actual Cs, then next complete F/Q/B RAW+its real M11. SourceF originalR46/R47, and sourceQ/B all4 original hook identities, cannot have their physical first deletion during that next FOREIGN RAW or its supplied M. Originals may have died earlier in the ordinary S4 section; this is NOT unconditional CURRENT preservation through C4. No U/history/global-first/simplicity or rail-length premise.',
 theorem_A_15_output_reserve_through_C3=dict(all3_source_births=sources,all240_joint_first_CURRENT_loss_rows=first,all_ordinary_physical_R_supports=R_bounds,left_W_gate=dict(ENTRY=left_gate,requires_source_L35_hole=left_hole,own_first_L=o.describe('U',12)),unspent_current_originals=sorted(F15),paired_retained13=sorted(old13),paired_new9=sorted(new9),proof='S0/E1 inputs miss every original by height. N2 first15loss table leaves only actual U3,-1 paired loss, which leaves13old+9new all y<=2, below every remaining N/C/W input throughC3. W3 table otherwise leaves rightU2,3 (already excluded by signedf24 L28-hole proof) or leftU-2,3. Source L35 hole r(-4,3) is WHITE: S/E R supports miss it; any completed N R writer exits at y>=3 so C3 makes laterW y>=4>gate3; C3 R writers exit x<=r_x=-4, and completed W R writers also exitx<=-4. W cannot return rightward to gatex-2. Thus leftU ownL12 fails before the apparent paired loss. Physical CORE writes are all included. C hasI0. No higherC/FOREIGN claim follows.'),
 theorem_B_all_C4_original_hook_loss=dict(source_branch_cases=source_records,all_S4_tag_endpoint_proofs=proofs,last_base_grammar='Signed0edd forces the last ordinary RAW before this nextFOREIGN to be plainV/U. All5 feasible pair types and V-to-B failure are checked literally. Every physical firstL on a SAME original must be included in the goal set. If the immediately preceding RAW touched that cell, the old identity cannot still survive, so any later BLACK there is another identity. Otherwise all known CURRENT facts at the previous ENTRY and recipient ENTRY use exact8 S-loss exit equations. A source tag missed physically by the previous RAW stays SAME BLACK, even if no CURRENT-at-recipient claim is available; a firstR in FOREIGN RAW+M is then impossible.',residue_explanation='Only a B marker-only geometry survives the immediate CURRENT masks in each branch. For sourceF it is B(-4,-6,S), lastU(-4,-2,S); sourceR46 is stillCURRENT at lastU entry and is physically missed by thatU, but B ownR70 demandsWHITE. For sourceQ/B it is B(-5,-7,S), lastU(-5,-3,S); the same sourceR46 is retained and missed, but B contextR80 demandsWHITE at next actual word tick6/read7. Its earlier markerL1 may partially delete another oldhook, but then full suppliedM fails. No whole-word completion is asserted for that partial attempt.'),
 conditional_C4_CURRENT_corollary='For sourceQ/B, if the four originals are CURRENT at recipientENTRY (in particular if the preceding ordinary prefix has no nonadjacent contact with the source proxy, by signed715), they remainCURRENT at recipient RAW EXIT and physicallySAME BLACK through its actual M. No deletion plus complete exitCORE capture coverage excludes silent absorption. This does not prove the ordinary prefix contact-free, and cannot be iterated through another foreign.',all15_FOREIGN_exitCORE_capture_checks=captures,
 limits=['No no-loss theorem for ordinary S4 itself; hooks can retire there before the nextFOREIGN.','No extension to C5 or any furtherFOREIGN by resetting the source state.','No SOURCE initial-U-star conclusion.','No geometric first-contact assumption or exclusion; actual identity and completion ownership are separate.','Not a finite whole-field quotient or decreasing resource; every unresolved tag/repair remains open.','No ant-language coverage or capture.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'C4_original_hook_loss.json').write_text(json.dumps(out,indent=2)+'\n')
print('15-output C3 reserve:240 roles, two WHITE-hole W guards. C4 original-hook nextFOREIGN loss:370 source/branch recipient poses all cut; final B marker cases carriedBLACK. No ordinaryC4 permanence or C5 claim.')
