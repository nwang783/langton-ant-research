"""Dependency-explicit 40-interface join: last positive-C parent is DC orVC.
No recursive restriction to older epochs and no complete history enumeration.
"""
from pathlib import Path
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';HP=R/'returned_D_Jordan_ancestry_horizon_2026-10-24/D_Jordan_horizon.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];A=json.loads(HP.read_text());C=json.loads(CP.read_text());M='LLLLRLRRRRL';VEL=((0,1),(1,0),(0,-1),(-1,0));mp={c:i for i,c in enumerate('DCVUFQB')};K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def literal(w):
 p=(0,0);h=0;par=set();req={};rd={};first={}
 for t,ch in enumerate(w):
  initial=(ch=='L')^(p in par)
  if p in req and req[p]!=initial:return dict(feasible=False,tick0=t,read_number1=t+1,cell=p,first_read=first[p])
  if p not in req:req[p]=initial;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L' else 1))%4;p=add(p,VEL[h])
 return dict(feasible=True,requirements=req,reads=rd)
OP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';spec=importlib.util.spec_from_file_location('own',OP);own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
fences={(15,'DDD'),(15,'V'),(30,'DD'),(15,'DD'),(30,'D')};rows=[];bud=[]
for f in A['all40_exhaustive_last_positive_C_packet_and_short_run_interfaces']:
 ix=f['catalogue_id'];parent=f['last_positive_C_full_packet'];run=f['actual_pre_D_zero_C_word'];ns=parent+run+'D';check=literal(''.join(W[mp[c]]['word']for c in ns)+M);reason=None
 if not check['feasible']:reason='literal_X_plus_short_N_run_plus_selectedD_complete_context_conflict'
 elif ix==30 and run=='':assert parent in('DC','VC','UC');reason='signed_actual_prior_C_deleted_core_guard_51160142'
 elif parent=='UCC':assert(ix,run)==(15,'V');reason='signed_genuine_UCC_V_deleted_core_guard_c3a6b525'
 elif parent=='UC':
  if(ix,run)in fences:reason='signed_CURRENT_star_or_intact_cycle_support_fence_45eee17d'
  elif ix==30:raise AssertionError(('unclassified_UC',run))
  else:
   assert run in('','D');p=tuple(f['packet_entry'][:2]);h=f['packet_entry'][2];tag=at((1,3),p,h);r=C['old_source_contact_cases'][ix];fp=tuple(r['foreign_pose'][:2]);loc=rot(sub(tag,fp),-1)
   full=literal(W[4]['word']+W[1]['word']+M);fr=literal(W[4]['word']);assert full['requirements'][loc]is False and loc not in fr['requirements']and loc not in K
   t=full['reads'][loc][0][0];owner=own.describe('C',t-len(W[4]['word']))
   if t<len(W[4]['word'])+len(W[1]['word']):owner.update(owner='immediate returned C RAW (no C-tail parent inferred)',label='actual returned C RAW tick'+str(owner['owner_tick0'])+'/read'+str(owner['owner_read_number1']))
   bud.append(dict(catalogue_id=ix,UC_N_run=run,genuine_original_U_bud=tag,UC_full_entry_to_foreign_C_age=4,foreign_RAW_misses=True,combined_before='WHITE',combined_tick0=t,physical_owner=owner))
   reason='signed_original_U_bud_unretirable_through_full_age4_plus_literal_WHITE'
 else:
  assert parent in('DC','VC');reason='OPEN_genuine_DC_or_VC_parent_necessary_only'
 rows.append(dict(**f,actual_minimal_prefix=ns,minimal_complete_context_result=check if not check['feasible']else dict(feasible=True),classification=reason))
from collections import Counter
counts=Counter(r['classification']for r in rows);remain=[r for r in rows if r['classification'].startswith('OPEN')]
assert len(rows)==40 and len(remain)==14 and len(bud)==2
assert counts['literal_X_plus_short_N_run_plus_selectedD_complete_context_conflict']==15
assert counts['signed_CURRENT_star_or_intact_cycle_support_fence_45eee17d']==5
assert sorted((x['catalogue_id'],x['last_positive_C_full_packet'],x['actual_pre_D_zero_C_word'])for x in remain)==sorted([(15,p,w)for p in('DC','VC')for w in('','D','DD','DDD','V')]+[(30,p,w)for p in('DC','VC')for w in('D','DD')])
D=[GP,QP,HP,CP,OP,R/'returned_D_Jordan_ancestry_horizon_2026-10-24/manifest.json',R/'returned_D15_UCC_V_core_guard_2026-10-24/manifest.json',R/'returned_D30_prior_C_core_guard_2026-10-24/manifest.json',R/'returned_D_UC_current_fence_guards_2026-10-24/manifest.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'seven_word_spatial_return_2026-10-23/D_family_immediate_UC_bud_guard_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_ASSEMBLY_PENDING_INDEPENDENT_AUDIT_COMPONENT_GUARDS_SIGNED',scope='The two remaining D-source FIRST-returned-contact coarse targets have only14 necessary last-positive-C interfaces, all DC/VC. D15 allows five short N words, D30 only D orDD. No recursive restriction on older parents or bounded whole prefix; all14 remain necessary-only, not attained/excluded.',all40_actual_last_positive_C_interfaces=rows,classification_counts=dict(counts),two_shifted_UC_bud_WHITE_contradictions=bud,fourteen_remaining_genuine_DC_VC_interfaces=remain,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D_last_C_parent_reduction.json').write_text(json.dumps(o,indent=2)+'\n');print('40 interfaces:26 excluded,14 necessary DC/VC parents; signed generic-C guard removes empty D30 run.')
