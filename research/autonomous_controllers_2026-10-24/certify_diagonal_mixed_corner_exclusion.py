#!/usr/bin/env python3
"""All-cap local completion cover for all12 mixed diagonal-minimum interfaces."""
import json,hashlib
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import certify_diagonal_read_minimum as base
from certify_first_N_return_rules import return_paths
ROOT=Path(__file__).parent

def qwords(I,J,relations):
 out=[];raw=0
 for n in range(2*(I+J)+1):
  z=I+(n+1)//2-J
  if z%2:continue
  X=z//2;Y=I-X
  if not 0<=X<=(n+1)//2 or not 0<=Y<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),X),combinations(range(1,n,2),Y)):
   nn=set(rr)|set(ll);h=tuple(0 if j in nn else 2 for j in range(n));N=sorted(nn);W=[j for j,x in enumerate(h)if(x+(1 if j%2==0 else-1))%4==3];assert len(N)==I and len(W)==J;raw+=1
   if all(N[r['N_ordinal']]==W[r['W_ordinal']]+1 for r in relations):out.append(h)
 return out,raw

def main():
 src=(ROOT/'certify_diagonal_read_minimum.json').read_bytes();domain=json.loads(src);cases=[];stats=Counter();ids=set()
 for c in domain['cases']:
  if c['case']not in(7,11,16,17):continue
  for s in c['survivors']:
   H=c['lower_headings']+s['A_headings'];kind,G=base.graph(H);assert kind=='open';rels=return_paths(H,G);a,b=H[-2:];oc=lambda hs,d:sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(hs));ports=[(oc(a,0),b.count(3)),(oc(b,0),a.count(3))]
   q,nq=qwords(*ports[0],rels[0]);r,nr=qwords(*ports[1],rels[1]);cc=Counter();reject=[]
   for qi,ri in product(range(len(q)),range(len(r))):
    HH=H+[q[qi],r[ri]];kind,wit=base.graph(HH)
    assert kind in('skipped_rank','closed_component'),(c['case'],s['A_indices'],qi,ri,kind)
    if kind=='skipped_rank':assert len(wit['segment'])==5 and wit['rank_after']>=wit['rank_before']+2
    else:assert len(wit['cycle'])==4 and wit['other_local_events']>0 and wit['open_chains']>0
    cc[kind]+=1;stats[kind]+=1;reject.append({'helper_indices':[qi,ri],'reason':kind,'witness':wit})
   id=(c['case'],tuple(s['A_indices']));ids.add(id)
   cases.append({'lower_case':c['case'],'A_indices':s['A_indices'],'complete_lower_histories':H,'next_Q_port_counts':ports,'derived_max_helper_lengths':[2*sum(z)for z in ports],'actual_first_return_paths':rels,'raw_complete_helper_word_counts':[nq,nr],'filtered_helper_words':[q,r],'paired_candidates':len(q)*len(r),'outcomes':dict(cc),'rejections':reject})
 prior=json.loads((ROOT/'first_N_return_rules_certificate.json').read_text());prev155={(a,tuple(b))for a,b in prior['explicit_set_difference']['exact_final155_ids']};prev157={(x['lower_case'],tuple(x['A_indices']))for x in prior['remaining_before_other_signed_reductions']}-{(3,(1,0)),(3,(1,1))}
 assert len(ids)==12 and ids<=prev155 and ids<=prev157 and sum(stats.values())==4692
 serial=lambda zs:[[a,list(b)]for a,b in sorted(zs)]
 result={'scope':__doc__,'signed227_input_sha256':hashlib.sha256(src).hexdigest(),'selected_complete_interfaces':12,'total_helper_pairs':sum(stats.values()),'outcomes':dict(stats),'no_growth_budget_used':True,'explicit_removed_ids':serial(ids),'previous155_intersection':serial(ids&prev155),'remaining_g8_143_ids':serial(prev155-ids),'remaining_all_growth_145_ids':serial(prev157-ids),'cases':cases,'conclusion':'If both minimum-row classes are read, the two next cells both startS and form a single-used negative F4 circle. The one-singleton minimum case remains open.'}
 (ROOT/'diagonal_mixed_corner_exclusion_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('cases','remaining_g8_143_ids','remaining_all_growth_145_ids','explicit_removed_ids','previous155_intersection')},indent=2))
if __name__=='__main__':main()
