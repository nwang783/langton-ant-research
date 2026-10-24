"""Separate causal repair of exactly firstC→N4 U(-1,-1).
Does not validate original143d universal F-pair/current claim.
"""
from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('l',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def rel(q,p):return l.rot(sub(q,p[:2]),-p[2])
g=(-1,2);target=(-1,-1,0);loc=rel(g,target);assert loc==(0,3)and loc not in l.K
f=l.trace(W['U']+l.M)['first'][loc];assert f==('L',23)
JO=dict((tuple(x[:3]),x[3])for x in json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text()));assert JO[7,0,3]>=4
# Whole actual prefix, no hypothetical third-C marker ownership.
t=l.trace(W['F']+3*W['C']+l.M);assert not t['feasible']and t['previous_read']==47 and t['conflict_read']==99 and t['turn']=='R'
assert t['cell']==[-2,-1]and t['conflict_read']==len(W['F'])+2*len(W['C'])+13
assert l.trace(W['F']+2*W['C']+l.M)['feasible']
limit=dict(word='FCCC',actual_conflict=t,original_F_R47_still_unread_until_third_C=True,third_C_own_RAW_tick0=13,third_C_own_RAW_read1=14,third_C_RAW_not_complete=True,not_a_terminal_C_or_DCC_grammar_claim=True)
for m in(1,2):
 raw=W['F']+m*W['C'];last=l.trace(raw)['last'][(-2,-1)];assert last==('R',47)
branches=[]
for m in(1,2):
 p=after(m*W['C']);assert p==((0,1,3)if m==1 else(-1,1,2))
 for a in'DVU':
  tr=l.trace(W[a]+l.M);q=rel(g,p);ff=tr['first'][q]
  if m==1:
   assert q==(1,1)and q not in l.K and ff==('R',6);route='physical_WHITE_at_first_BASE_ENTRY_by_own_first_R6'
  else:
   assert q==(0,-1)and q in l.K and ff==('L',3);route='real_CORE_g_physically_deleted_by_first_BASE_own_L3'
  branches.append(dict(initial_leading_C_count=m,first_actual_BASE=a,first_BASE_pose=p,actual_first_BASE_ENTRY_C_clock=m,physical_guard_g=g,local=q,actual_first=ff,actual_owner=o.describe(a,ff[1]),route=route,g_cannot_be_an_external_entry_residual_of_selected_BASE_factor=True,target_U_ENTRY_clock=4,maximum_possible_produced_age=4-m,produced_input_minimum=JO[7,0,3],strict_age_contradiction=4-m<JO[7,0,3],actual_prior_RAW_to_first_BASE='C',selected_BASE_to_actual_target_U_is_actual_G8_by_signed_BASE_cut_bridge=True,no_FOREIGN_inside_selected_factor=True))
assert len(branches)==6
# Bind exact unresolved label from the rejected broader certificate.
old=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification.json').read_text())['all3_OPEN_N4_restoration_residues'];lift=[r for r in old if r['original_row']['first_post_RAW']=='C'];assert len(lift)==1 and lift[0]['original_row']['actor']=='U'and tuple(lift[0]['original_row']['pose'])==target and lift[0]['original_row']['K']==4
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'original_F_piece_firstpost_DC_2026-10-24/manifest.json',R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification_manifest.json'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual FIRST F then initial ordinary RAW C and ordinary-only suffix. A completed actual RAW U at postF-exit C4 cannot enter(-1,-1,N). This repairs ONLY the firstC→U residue in rejected143d; sourceD→V/U remains OPEN. No F-pair currentness at this head is claimed.',target_upper_input=dict(target_pose=target,cell=g,local=loc,first_physical_read=f,owner=o.describe('U',23),actual_produced_age_minimum=JO[7,0,3],outside_actual_target_ENTRY_CORE=True),actual_initial_C_run_at_most_two=limit,all6_real_first_BASE_guard_branches=branches,first_BASE_exists='TargetU is itself a BASE atclock4, while maximal initial C run<=2. Thus the first BASE enters atclock1 or2 and is strictly earlier, not a hypothetical predecessor.',fresh_ownership_argument='Select the factor at that first genuine BASE and end at actual targetU, with SAME real finalM11. Signed RAW-to-G8 bridge applies; a firstD has its ACTUAL precedingC. For m1 g is initially physicallyWHITE by firstBASE ownR6. For m2 g is initialCORE and physically L3-deleted. No old external entry identity can fund the target. At target g is a TRUE upper input outside entryCORE, so its BLACK owner is a genuine fullO identity born in this factor; a prior EXITCORE R cannot silently export an untouched original CORE lifetime. Every producer fullENTRY clock>=m, hence age<=4-m<=3<minimum4. Actual CORE R repairs remain allowed but have the same fresh produced clock bound.',exact_original_residue_lift=lift[0],original143d_full84_universal_pair_claim_still_NOT_PASSED=True,remaining_two_sourceD_N4_residues=[r for r in old if r['original_row']['first_post_RAW']=='D'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'C_N4_U_repair.json').write_text(json.dumps(out,indent=2)+'\n');print('FirstC N4 U(-1,-1):6 exact firstBASE cases, real upper min4 versus new produced age<=3. FirstD V/U remainOPEN.')
