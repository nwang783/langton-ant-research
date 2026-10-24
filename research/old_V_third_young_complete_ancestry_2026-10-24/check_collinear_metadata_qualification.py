"""Mandatory metadata qualification; frozen young proof/boards remain unchanged."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;P=H/'young_ancestry.json';j=json.loads(P.read_text());records=[];hist=Counter()
for ci,c in enumerate(j['all100_complete_board_controls']):
 pieces=c['repaired_proxy_pieces'];nonadj=[]
 for check in c['all_proxy_pair_checks']:
  hit=check['contact'];i,k=check['old_piece'],check['new_piece'];p,q=pieces[i],pieces[k]
  truejoin=bool(hit and k==i+1 and p['b']==q['a']and(hit.get('old_s')=='1'and hit.get('new_t')=='0'or hit.get('collinear_old_interval')==['1','1']))
  if truejoin and not check['true_adjacent_endpoint']:
   assert hit.get('collinear_old_interval')==['1','1'];records.append(dict(control_index0=ci,tokens=c['tokens'],old_piece=i,new_piece=k,contact=hit,shared_vertex=p['b'],mandatory_true_adjacent_endpoint=True))
  if hit and not truejoin:nonadj.append(dict(old_piece=i,new_piece=k,contact=hit))
 hist[(c['actual_selected_old_source_index0'],len(nonadj))]+=1
assert records
out=dict(status='MANDATORY_COLLINEAR_JOIN_METADATA_QUALIFICATION',frozen_source_SHA256=hashlib.sha256(P.read_bytes()).hexdigest(),exact_semantics='Original all_proxy_pair_checks.true_adjacent_endpoint recognizes only nonparallel joins. A false value is NOT a statement that the contact is nonadjacent. Consecutive collinear point joins with old interval[1,1] and exact previous-end=next-start are legitimate true adjacent endpoints. The proof never uses this metadata flag to assert prepared-proxy simplicity; ancestry, masks, endpoint words and identities are unchanged.',all_corrected_legitimate_collinear_joins=records,number_corrected=len(records),actual_total_nonadjacent_contact_histogram=[dict(prependedD_index0=k[0],nonadjacent_contact_count_including_third=k[1],number_controls=v)for k,v in sorted(hist.items())],no_original_file_changed=True,no_new_simplicity_claim=True)
(H/'collinear_metadata_qualification.json').write_text(json.dumps(out,indent=2)+'\n');print('Mandatory collinear metadata qualifier:',len(records),'true joins; original flag false does not mean nonadjacent. No proof/board change.')
