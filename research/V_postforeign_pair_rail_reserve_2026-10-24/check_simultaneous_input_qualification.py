"""Explicit immutable qualification of the 36 held-r B rows in35815d85."""
from pathlib import Path
from collections import Counter
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;P=H/'check_pair_rail_reserve.py';ns={'__file__':str(P)};exec(P.read_text().split('# No ordinary r loss')[0],ns);G=ns['G'];rows=[]
for row in ns['Bqueries']:
 if row['reason']!='held_r_complete_context_contact':continue
 p=tuple(row['pose'][:2]);h=row['pose'][2];co={'D':0,'V':4,'U':7}[row['consumer']];src={'V':4,'VC':5,'VCC':6}[row['actual_old_source_full']];I={ns['place'](q,p,h)for q in G[co]['inputs']};K={ns['place'](q,p,h)for q in ns['l'].K};req={ns['place'](q[:2],p,h):bool(q[2])for q in G[co]['requirements']};r=(0,0)
 rec=dict(original_B_input_case=row)
 if not req[r]:rec['specific_reason']='SAME r BLACK before literal first-WHITE'
 elif r in K:rec['specific_reason']='SAME r CURRENT outside actual ENTRY core'
 else:
  assert r in I;hits=[]
  for i,old in enumerate(ns['chords'](src)):
   for j,new in enumerate(ns['chords'](co,p,h)):
    hit=ns['contact'](*old,*new)
    if hit:hits.append(dict(actual_old_source_atom_index0=i,actual_old_chord=old,new_plain_RAW_atom_index0=j,new_chord=new,exact_intersection=hit))
  assert hits
  rec.update(specific_reason='TRUE simultaneous r/B input already contacts actual old source proxy',literal_ENTRY_color_conflict_NOT_claimed=True,all_actual_source_contacts=hits,not_genuine_adjacency='Consumer is postFIRSTforeign; these old source atoms preceded it. Any old terminal point is still a forbidden nonadjacent old vertex, regardless outgoing-source attribution.')
 rows.append(rec)
ct=Counter(x['specific_reason']for x in rows);assert len(rows)==36 and sorted(ct.values())==[3,9,24]
out=dict(status='AUTHOR_EXPLICIT_DEPENDENCY_QUALIFICATION_ORIGINAL358_ALREADY_INDEPENDENTLY_PASS',original_manifest_sha256=hashlib.sha256((H/'manifest.json').read_bytes()).hexdigest(),scope='No theorem scope change. The36 held-r B rows are not all literal entry-color conflicts. Nine true simultaneous-input rows force SOURCE proxy contact and are excluded only under the simple-prefix/first-loss alternative, as independently verified in efde21f4.',all36_classified_rows=rows,counts=dict(ct),no_frozen_source_changed=True)
(H/'simultaneous_input_qualification.json').write_text(json.dumps(out,indent=2)+'\n');print(ct)
