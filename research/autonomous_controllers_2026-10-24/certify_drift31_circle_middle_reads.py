#!/usr/bin/env python3
"""Exact middle-read completion of the two supplied full-circle inventories.
All-cap and all-growth CONDITIONAL on those inventories; exterior stays open.
"""
import json,hashlib
from collections import Counter
from pathlib import Path
from partial_drift31_graph import graph
from certify_drift31_read_minimum import words,returns_to,depart
ROOT=Path(__file__).resolve().parent

def main():
 z=json.loads((ROOT/'drift31_single_used_g8_shapes_certificate.json').read_text());out=[];S=Counter();survivors=[]
 for q in z['all_quadruple_placements']:
  if q['outcome']!='OPEN_circle_interface':continue
  H=[q['complete_circle_histories'][str(t)]for t in range(6)]
  for v6 in q['first_exterior_cell_T6']['all_complete_domains']:
   A=H+[v6];k,G=graph(A,list(range(7)));assert k=='open';rel,paths=returns_to(A,G,7);assert all(p['outgoing_heading']==2 and p['incoming_heading']==3 for p in paths)
   I=len(depart(v6,3));J=3;bound=2*(I+J);item={'circle_histories':H,'T6_history':v6,'T7_incoming_W_outgoing_S':[I,J],'T7_derived_bound':bound,'actual_T7_first_returns':paths}
   # Signed first-arrival Rule B, properly rotated: first W after S1 makes
   # W0 the event S2; then a next W ordinal other than1 immediately after S2
   # skips a required W read. Full paths verify no hidden physical import.
   first=[i for i,(a,b,L)in enumerate(rel)if(a,b)==(1,0)];second=[i for i,(a,b,L)in enumerate(rel)if a==2 and b!=1]
   if first and second:
    item.update(outcome='rotated_first_arrival_Rule_B',rule_paths=[first[0],second[0]]);S['Rule_B_T6_modes']+=1;out.append(item);continue
   domain=words(1,bound,3,I,2,J,rel);item['complete_T7_domain']=domain;reject=[]
   for h7 in domain:
    kind,w=graph(A+[h7],list(range(8)));S[kind]+=1;entry={'history':h7,'outcome':kind}
    if kind=='open':survivors.append({'T5':H[5],'T6':v6,'T7':h7,'complete_named_histories':A+[h7],'open_graph':w})
    else:
     assert kind=='skipped_rank'and len(w['segment'])-1==4 and (w['rank_before'],w['rank_after'])in((1,4),(2,5));entry['witness']=w
    reject.append(entry)
   item.update(outcome='complete_T7_domain_checked',all_domain_outcomes=reject);out.append(item)
 assert len(out)==20 and S=={'Rule_B_T6_modes':10,'open':8,'skipped_rank':10}
 assert len([s for s in survivors if len(s['T5'])==3])==1
 s=next(s for s in survivors if len(s['T5'])==3);assert s['T6']==[0,0,0]and tuple(s['T7'])==(1,1,1,3)
 result={'scope':__doc__,'source_shape_certificate_sha256':hashlib.sha256((ROOT/'drift31_single_used_g8_shapes_certificate.json').read_bytes()).hexdigest(),'rule_B_source_note_sha256':hashlib.sha256((ROOT/'FIRST_N_RETURN_RULES_DIAGONAL_REDUCTION.md').read_bytes()).hexdigest(),'counts':dict(S),'all20_T6_cases':out,'eight_OPEN_interfaces':survivors,'warning':'No exterior completion, controller, or full d3,1 g8 exclusion. This local extension uses neither growth budget nor a global cap.'}
 (ROOT/'drift31_circle_middle_reads_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print(dict(S))
if __name__=='__main__':main()
