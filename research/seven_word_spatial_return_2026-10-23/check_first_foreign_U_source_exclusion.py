"""Dependency join for first foreign contacts with outgoing old U sources.
No new geometric scan, prefix tree, or global simplicity assertion.
"""
from pathlib import Path
from collections import Counter
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
P=json.loads((H/'foreign_first_contact_interface.json').read_text());T=json.loads((H/'foreign_tail_first_contact.json').read_text());A=json.loads((H/'complete8_foreign_adjacency.json').read_text())
assert A['locally_attained_pairs']==[['V','F'],['V','Q'],['U','F'],['U','Q'],['U','B']]
assert all(r['conflict'] is not None for r in A['rows']if r['source'].endswith('C'))
rows=[]
for name,rr in P['U_source_star_filters'].items():
 for r in rr:
  rows.append(dict(piece='F_prefix',foreign=name,pose=r['foreign_pose'],context_reason=r['reason'],ages=r['permitted_C_ages'],bits=r['preceding_C_bits']))
for name,rr in T['U_source_filters'].items():
 for r in rr:
  rows.append(dict(piece=name+'_tail',foreign=name,pose=r['foreign_pose'],context_reason=r['context_reason'],ages=r['permitted_C_ages'],bits=r['preceding_C_bits']))
assert len(rows)==72 and all(len(r['ages'])==len(r['bits'])==2 for r in rows)
assert sum(r['context_reason']=='unexcluded_necessary_interface'for r in rows)==12
rules={('F',-2,3,3):'signed_minimum_foreign_star_effect_age_two',('F',1,3,0):'signed_preforeign_cut_1_3_N_impossible',('Q',1,3,0):'signed_preforeign_cut_1_3_N_impossible',('B',1,3,0):'signed_preforeign_cut_1_3_N_impossible',('F',2,4,0):'signed_cut_2_4_N_forces_preceding_C_but_pair_table_forbids_it',('Q',2,4,0):'signed_cut_2_4_N_forces_preceding_C_but_pair_table_forbids_it',('F',3,3,0):'signed_original_age4_U_renewal_then_F_common_bud_obstruction',('Q',-4,3,3):'signed_minimum_foreign_star_effect_age_two',('B',2,6,0):'signed_minimum_foreign_star_effect_age_two',('B',-5,2,3):'signed_minimum_foreign_star_effect_age_two',('B',-3,6,3):'signed_q_survives_until_age2_but_foreign_requires_it_white',('B',3,0,1):'signed_all_age_B_core_guard'}
classified=[]
for row in rows:
 for age,bit in zip(row['ages'],row['bits']):
  if row['context_reason']!='unexcluded_necessary_interface':why=row['context_reason']
  elif bit:why='signed_complete8_foreign_adjacency_forbids_preceding_C'
  else:
   key=(row['foreign'],*row['pose']);assert key in rules;why=rules[key]
  classified.append(dict(**row,C_age=age,preceding_C_bit=bit,exclusion=why))
assert len(classified)==144
counts=Counter(r['exclusion']for r in classified)
assert counts['signed_complete8_foreign_adjacency_forbids_preceding_C']==12
assert sum(v for k,v in counts.items()if k not in('held_star_in_core','held_star_before_white'))==24
D=[H/'foreign_first_contact_manifest.json',H/'foreign_tail_first_contact_manifest.json',H/'complete8_foreign_adjacency_manifest.json',H/'foreign_U_predecessor_ports_manifest.json',H/'foreign_U_early_star_exclusion_manifest.json',H/'foreign_U_age4_renewal_branch_manifest.json',R/'foreign_renewal_bud_obstruction_2026-10-23/manifest.json',R/'foreign_B_core_guard_2026-10-23/manifest.json',R/'core_periodicity_new/U_recycled_q_consumer_frozen_20261023_1954/manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='The chronological first new contact of the first foreign repaired proxy with an actual simple complete-eight U-entry old path cannot have an outgoing earlier U-base source. Only full complete-eight adjacency is assumed. Not arbitrary U-chord avoidance after some earlier D/C/V contact; not global proxy simplicity, raw seven-word coverage or capture.',canonical_U_source_geometries=72,full_context_remaining_geometries=12,clock_label_count=144,classification_counts=dict(counts),all_classified_labels=classified,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'first_foreign_U_source_exclusion.json').write_text(json.dumps(o,indent=2)+'\n')
print('All144 U-source clock-labelled cases closed:120 context conflicts,12 previous-C adjacency conflicts,12 signed preforeign-history conflicts. First new contact, if any, has outgoing old D/C/V source.')
