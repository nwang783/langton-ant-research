"""Mandatory partial correction: original143d full84 claim is NOT PASSED.
Keep81, openly retain3 actual N4 shared-entry restoration residues.
"""
from pathlib import Path
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
orig=json.loads((H/'F_piece_DC.json').read_text());rows=orig['all84_firstpostD_C_proper_F_contact_closures'];assert len(rows)==84
OPEN={('D','V',(-1,-1,0)),('D','U',(-1,-1,0)),('C','U',(-1,-1,0))};special=[];kept=[];opened=[]
for r in rows:
 key=r['first_post_RAW'],r['actor'],tuple(r['pose'])
 if key in OPEN:opened.append(dict(original_row=r,status='OPEN_necessary_not_attained',reason='The possible earlier F47 loss RAW exits exactly the actor ENTRY(-1,-1,N). Original F47 may be aliveCORE there. No independent source-output before-WHITE/core guard is present. D/V/U loss→V/U actor local pairs are literal-consistent.'))
 elif tuple(r['pose'])==(-1,-1,0):
  assert key==('C','V',(-1,-1,0));guard=[g for g in r['guards']if tuple(g.get('SAME_CURRENT_BLACK',()))==(1,2)];assert len(guard)==1 and guard[0]['actual_first']==['R',15]
  special.append(dict(original_row=r,status='EXCLUDED_without_F_pair',independent_source_C_bud_guard=guard[0]));kept.append(special[-1])
 else:
  assert r['K']!=4 or r['pose'][1]<=-2
  kept.append(dict(original_row=r,status='EXCLUDED_with_pair_only_under_restricted_target_hypothesis'))
assert len(opened)==3 and len(kept)==81 and len(special)==1
# Shared ENTRY is an attained local color interface, not just an imprecise
# support bound. Every loss/tag lifetime belongs to actual physical reads.
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('lit',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('own',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
pairs=[]
for x in'DVU':
 for a in'VU':
  t=l.trace(W[x]+W[a]+l.M);assert t['feasible'];g=(0,1)if x=='D'else(0,3)if x=='V'else(-1,4);tr=l.trace(W[x]+l.M);assert tr['first'][g]==('L',len(W[x])+1)
  pairs.append(dict(loss_RAW=x,actor_RAW=a,complete_local_pair_feasible=True,old_input_local=g,old_CURRENT_loss_at_loss_RAW_EXIT=True,physical_L_owner=o.describe(x,len(W[x])+1),original_identity_aliveCORE_at_actor_ENTRY=True,physical_death_at_actor_tick0=1,physical_death_at_actor_read1=2,complete_minimal_seed=sorted(q for q,(c,k)in t['first'].items()if c=='L'),genuine_FOREIGN_or_U_ancestry_NOT_claimed=True))
assert len(pairs)==6
out=dict(status='MANDATORY_PARTIAL_SCOPE_CORRECTION_ORIGINAL_FULL84_NOT_PASSED',original_manifest_sha256=hashlib.sha256((H/'manifest.json').read_bytes()).hexdigest(),original_files_unchanged=True,original_universal_pair_claim_withdrawn='Not all42 N4 heads lie belowy=-1. V/U(-1,-1,N) coincide with genuine F47-current-loss RAW exits. Do not claim F46/F47 CURRENT at these heads.',corrected_pair_scope='Use coupled pair only at source-output-supported targets with K2/3, or N4 heady<=-2, or W5 heady<=-1. The sourceC→V(-1,-1,N) case uses independent SAME C bud and does not invoke the pair.',all81_retained_exclusions=kept,all3_OPEN_N4_restoration_residues=opened,all6_literal_colour_consistent_loss_actor_pairs=pairs,no_genuine_U_entry_countercontrol_or_three_residue_exclusion=True,no_arbitrary_tail_simplicity_or_original_full84_signoff=True)
(H/'partial_scope_qualification.json').write_text(json.dumps(out,indent=2)+'\n');print('Mandatory correction: original84 NOTPASSED;81 scoped exclusions,3 OPEN N4 activeCORE restoration residues;6 local positive pairs.')
