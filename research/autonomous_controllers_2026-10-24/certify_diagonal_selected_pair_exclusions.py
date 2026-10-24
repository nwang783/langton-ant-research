#!/usr/bin/env python3
"""Exact local paired-helper cover for43 specified g8 boundary interfaces."""
import json,hashlib
from pathlib import Path
from itertools import product
from collections import Counter
import certify_diagonal_read_minimum as base
from certify_first_N_return_rules import return_paths
from certify_diagonal_mixed_corner_exclusion import qwords
ROOT=Path(__file__).parent
SELECTED=[(5,(3,1)),(5,(6,0)),(5,(6,1)),(5,(6,2)),(8,(0,6)),(8,(1,3)),(8,(1,6)),(8,(2,6)),(9,(0,6)),(9,(0,11)),(9,(1,6)),(9,(1,11)),(9,(2,6)),(9,(2,11)),(9,(3,11)),(9,(4,6)),(9,(4,11)),(9,(5,6)),(9,(5,11)),(9,(6,0)),(9,(6,1)),(9,(6,2)),(9,(6,4)),(9,(6,5)),(9,(6,6)),(9,(6,9)),(9,(6,10)),(9,(6,11)),(9,(8,11)),(9,(9,6)),(9,(9,11)),(9,(10,6)),(9,(10,11)),(9,(11,0)),(9,(11,1)),(9,(11,2)),(9,(11,3)),(9,(11,4)),(9,(11,5)),(9,(11,6)),(9,(11,8)),(9,(11,9)),(9,(11,10))]
TARGETS=[z for z in product(range(9),repeat=4)if sum(z)==8 and all(v%4==2 for v in[z[0]-z[1],z[3]-z[2],z[0]-z[2],z[3]-z[1]])]

def budget(H):
 v=[0]*4
 for i,h in enumerate(H):
  if len(h)%2:
   t=i//2-1;r=i%2;v[2*r+(t-r)%2]+=1
 if any(all(a<=b for a,b in zip(v,z))for z in TARGETS):return None
 return {'named_odd_counts_00_01_10_11':v,'incompatible_each_target_at_bin':[next(i for i in range(4)if v[i]>z[i])for z in TARGETS]}

def main():
 src=(ROOT/'certify_diagonal_read_minimum.json').read_bytes();domain=json.loads(src);selected=set(SELECTED);assert len(selected)==43;cases=[];stats=Counter();ids=set()
 for c in domain['cases']:
  for s in c.get('survivors',[]):
   key=c['case'],tuple(s['A_indices'])
   if key not in selected:continue
   H=c['lower_headings']+s['A_headings'];kind,G=base.graph(H);assert kind=='open';rels=return_paths(H,G);a,b=H[-2:];oc=lambda hs,d:sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(hs));ports=[(oc(a,0),b.count(3)),(oc(b,0),a.count(3))];q,nq=qwords(*ports[0],rels[0]);r,nr=qwords(*ports[1],rels[1]);cc=Counter();rejections=[]
   for qi,ri in product(range(len(q)),range(len(r))):
    HH=H+[q[qi],r[ri]];wit=budget(HH)
    if wit is not None:kind='full_g8_signed_residue_budget'
    else:
     kind,wit=base.graph(HH);assert kind in('skipped_rank','closed_component')
     if kind=='closed_component':assert wit['other_local_events']>0 and wit['open_chains']>0
    cc[kind]+=1;stats[kind]+=1;rejections.append({'helper_indices':[qi,ri],'reason':kind,'witness':wit})
   cases.append({'lower_case':c['case'],'A_indices':s['A_indices'],'complete_lower_histories':H,'next_Q_counts':ports,'derived_max_lengths':[2*sum(z)for z in ports],'actual_first_return_paths':rels,'raw_helper_word_counts':[nq,nr],'filtered_helper_words':[q,r],'paired_candidates':len(q)*len(r),'outcomes':dict(cc),'rejections':rejections});ids.add(key)
 assert ids==selected and sum(stats.values())==2896
 prior=json.loads((ROOT/'first_N_return_rules_certificate.json').read_text());a155={(a,tuple(b))for a,b in prior['explicit_set_difference']['exact_final155_ids']};mixed=json.loads((ROOT/'diagonal_mixed_corner_exclusion_certificate.json').read_text());m12={(a,tuple(b))for a,b in mixed['explicit_removed_ids']};a143=a155-m12;assert len(a143)==143 and ids<=a143
 serial=lambda z:[[a,list(b)]for a,b in sorted(z)]
 result={'scope':__doc__,'signed227_source_sha256':hashlib.sha256(src).hexdigest(),'all_ten_signed_residue_compatible_g8_vectors':TARGETS,'selected43_ids':serial(ids),'overlap_with_mixed12':serial(ids&m12),'previous143_intersection':serial(ids&a143),'remaining100_ids':serial(a143-ids),'total_helper_pairs':sum(stats.values()),'outcomes':dict(stats),'cases':cases,'limitations':'Only these43 specified complete lower interfaces are excluded, at g8. All bounds are derived local counts; higher region and total period unrestricted. Remaining100 are necessary interfaces only, not physical completions.'}
 (ROOT/'diagonal_selected_pair_exclusions_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('cases','remaining100_ids','selected43_ids','previous143_intersection','all_ten_signed_residue_compatible_g8_vectors')},indent=2))
if __name__=='__main__':main()
