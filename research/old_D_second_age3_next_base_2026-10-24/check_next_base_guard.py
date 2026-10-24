"""Twelve genuine plain-D residues blocked by its actual next N base.
No depth scan, no postforeign maturation, no inferred physical WHITE reserve.
"""
from pathlib import Path
import hashlib,json,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS;P=R/'old_D_second_age3_common_beta_2026-10-24/D_age3_common_beta.json';j=json.loads(P.read_text());rows=j['remaining12_necessary_states'];assert len(rows)==12

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def raw(tokens):return ''.join(W[a]for a in tokens)
def physical_owner(tokens,tick):
 n=0
 for i,a in enumerate(tokens):
  if tick<n+len(W[a]):return dict(actual_atom_index0=i,actual_atom=a,canonical=o.describe(a,tick-n))
  n+=len(W[a])
 return dict(actual_atom='next actual word',next_word_tick0=tick-n,next_word_read_number1=tick-n+1,turn=l.M[tick-n])
# Actual source plainD ends (1,1,N), with unchanged C clock0. Its next
# complete-eight packet is a real D/V/U-family full source, not a new mark.
D=l.trace(W['D']);assert D['pose']==(1,1,0)
next_entry=(1,1,0);actual_next_fulls=('D','DC','V','VC','VCC','U','UC','UCC')
source_roles=[]
for full in actual_next_fulls:
 base=full[0];geo=l.literal_geometry(raw(full));tr=l.trace(raw(full));base_tr=l.trace(W[base]);outputs=set(map(tuple,geo['outputs']))
 tags={'D':[(2,0)],'V':[(0,0),(1,0)],'U':[(0,0),(0,1),(1,0),(1,1)]}[base]
 records=[]
 for tag in tags:
  assert tag in outputs and tr['last'][tag]==base_tr['last'][tag]and tr['last'][tag][0]=='R'
  # No tail reread of the same original identity.
  pos=(0,0);heading=0;reads=[]
  for tick,turn in enumerate(raw(full)):
   if pos==tag:reads.append((tick,turn))
   heading=(heading+(1 if turn=='R'else-1))%4;pos=add(pos,l.DIRS[heading])
  assert reads[-1]==(tr['last'][tag][1],tr['last'][tag][0])and all(t<len(W[base])for t,c in reads)
  proof={'D':'Reader-independent66aa: every genuine D/DC common R8 is CURRENT through full-source-entry age3 at a complete8 to FIRSTforeign boundary.','V':'Signed2036/2043: original r first retirement5 and original B first retirement4.','U':'Signed1918: four SAME original left-star residual identities remain CURRENT within the uninterrupted old complete-eight factor.'}[base]
  records.append(dict(actual_next_base_slot=tag,SAME_current_cell=add(next_entry[:2],tag),actual_base_last_R_tick0=tr['last'][tag][1],actual_base_last_R_read_number1=tr['last'][tag][1]+1,own_C_tails_preserve_same_identity=True,CURRENT_before_foreign_proof=proof))
 source_roles.append(dict(actual_next_full=full,actual_base=base,actual_full_entry_pose=next_entry,actual_full_entry_clock=0,actual_full_completion_clock=full.count('C'),true_full_entry_to_foreign_age=3,genuine_current_tags=records))
assert len(source_roles)==8
checks=[];base_checks=[]
for row in rows:
 assert row['first']in'VU'and row['second']in'VU'and row['second_pose']==[1,0,3]
 tokens=row['foreign']+row['first']+row['second'];trace=l.trace(raw(tokens)+l.M);assert trace['feasible'];pa=row['foreign_pose']
 for role in source_roles:
  hits=[]
  for fact in role['genuine_current_tags']:
   cell=tuple(fact['SAME_current_cell']);local=l.rot(sub(cell,pa[:2]),-pa[2]);first=trace['first'].get(local)
   if local in l.K:hits.append(dict(fact=fact,foreign_local=local,conflict='genuine CURRENT identity in foreign ENTRY core'))
   elif first and first[0]=='R':hits.append(dict(fact=fact,foreign_local=local,conflict='actual first combined read needs WHITE',combined_tick0=first[1],actual_owner=physical_owner(tokens,first[1])))
  assert hits,(row,role)
  checks.append(dict(base_row_index0=row['base_row_index0'],foreign=row['foreign'],first=row['first'],second=row['second'],foreign_pose=pa,second_pose=row['second_pose'],actual_next_full=role['actual_next_full'],exact_genuine_current_tag_conflicts=hits))
  if role['actual_next_full']in'DVU':base_checks.append(checks[-1])
assert len(checks)==96 and len(base_checks)==36
# The sourceDC counterpart uses the separately signed genuine full-DC reserve.
CP=R/'second_old_C_age3_2026-10-24/C_age3_source_reserve.json'
cr=json.loads(CP.read_text())['all7_genuine_C_roles_and18_same_identity_source_reserves'][0]
assert cr['actual_full']=='DC'and cr['actual_full_ENTRY_age_at_FOREIGN']==3
cf=next(f for f in cr['selected_reserves']if f['full_output_slot']==[3,1]);assert cf['actual_last_R_tick0']==18
DCchecks=[]
for row in rows:
 tokens=row['foreign']+row['first']+row['second'];trace=l.trace(raw(tokens)+l.M);pa=row['foreign_pose'];local=l.rot(sub((3,1),pa[:2]),-pa[2]);first=trace['first'][local]
 assert first[0]=='R'and local not in l.K
 DCchecks.append(dict(base_row_index0=row['base_row_index0'],actual_full_source='DC',SAME_current_source_cell=(3,1),genuine_source_C1_common_birth_tick0=18,birth_read_number1=19,source_full_entry_clock=0,foreign_clock=3,source_full_completion_clock=1,signed_reader_independent_full_DC_reserve=cf,actual_combined_first_read=first,actual_owner=physical_owner(tokens,first[1]),conflict='actual first read requires WHITE'))
assert len(DCchecks)==12
all108=[]
for full in('D','DC'):
 for r in j['all54_foreign_typed_masks']:
  row=dict(actual_full_source=full,base_row_index0=r['base_row_index0'],foreign=r['foreign'],first=r['first'],second=r['second'],foreign_pose=r['foreign_pose'],second_pose=r['second_pose'])
  if r['classification']!='necessary_only_unresolved':row['proof']=r['classification']
  elif full=='D':row['proof']='actual next D/V/U-family current reserve; all8 next fulls excluded'
  else:row['proof']='signed sourceDC C1 common(3,1) current reserve'
  all108.append(row)
assert len(all108)==108
paths=[CP,R/'second_old_C_age3_2026-10-24/manifest.json',R/'audits/old_C_age3_reserve_independent.json',R/'audits/old_D_age3_common_beta_independent.json',P,R/'old_D_second_age3_common_beta_2026-10-24/manifest.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'audits/check_V_parallel_reproductive_supply_independent.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'audits/check_V_C_same_heading_exclusion_independent.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'audits/check_U_left_star_permanence_independent.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',R/'audits/check_first_foreign_returned_simplicity_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in paths),[str(p)for p in paths if not p.exists()]
out=dict(status='AUTHOR_ALL_OLD_D_AGE3_NEXT_BASE_CLOSURE_PENDING_INDEPENDENT_AUDIT',scope='All54 masks for each actual old D/DC full source at true preforeign age3, chronological FIRST new SECOND ordinary RAW contact. PlainD twelve residues use actual next-base reserve; sourceDC twelve use separately signed genuine C1 common. No second simplicity or postforeign maturation.',actual_selected_source=dict(full='D',entry_pose=(0,0,0),entry_clock=0,actual_RAW_exit=(1,1,0),actual_next_base_entry_pose=next_entry,actual_next_base_entry_clock=0,next_atom_really_exists='There are three C turns before the first foreign; source is plain complete D, so its actual next full word starts D/V/U, not an internal C or foreign.'),all8_genuine_actual_next_full_sources_and_tag_births=source_roles,all36_next_BASE_type_mask_checks=base_checks,all96_actual_full_tail_mask_checks=checks,all12_actual_source_DC_C1_guard_lifts=DCchecks,all108_actual_source_role_contact_cases=all108,conclusion='Each of the twelve plain-D residues fails for every possible actual next full packet: D/DC held common(3,1), V/VC/VCC held r/B(1,1)/(2,1), or U/UC/UCC held star. With42 signed common/beta cuts this exhausts all54 PLAIN-D masks. The same twelve sourceDC cases fail its separately signed genuine C1 common(3,1) reserve. Thus all54 geometric masks close for both actual source D and DC; no outgoing-old-D source remains in this FIRST SECOND-RAW slice.',no_prepared_countercontrol_or_unbounded_prefix_search_or_recursive_historical_reset=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'next_base_guard.json').write_text(json.dumps(out,indent=2)+'\n');print('Twelve plain-D residues x3 actual next bases=36 checks; all8 actual containing next full tails=96 checks, all fail genuine same-current tags before foreign.')
