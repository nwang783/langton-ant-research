#!/usr/bin/env python3
"""Proof-producing application of three all-cap ordinal return rules."""
import json,hashlib
from pathlib import Path
from collections import Counter
import certify_diagonal_read_minimum as base
from check_extremal_read_coupling import D,quotient
ROOT=Path(__file__).parent

def return_paths(H,G):
 pts=G['points'];rel=[[],[]]
 for chain in G['chains']:
  (i,j),k=chain[0];assert k==0;hi=H[i][j];p=pts[i];source=tuple(p[z]-D[hi][z]for z in(0,1))
  (ii,jj),kk=chain[-1];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;p=pts[ii];target=(p[0]+2*kk+D[ho][0],p[1]-2*kk+D[ho][1])
  assert sum(source)==sum(target)==2 and hi==3 and ho==0
  if source!=target:continue
  q,voltage=quotient(source,(2,-2));lane=q[0];assert lane in(0,1)
  a=[r for r,h in enumerate(H[i])if h==hi].index(j)
  b=[r for r,h in enumerate(H[ii])if(h+(1 if r%2==0 else-1))%4==ho].index(jj)
  events=[]
  for(c,r),v in chain:
   p=(pts[c][0]+2*v,pts[c][1]-2*v);assert p!=source
   events.append({'physical_cell':p,'class_index':c,'complete_rank':r,'voltage':v,'heading':H[c][r],'turn':'R'if r%2==0 else'L'})
  rel[lane].append({'W_ordinal':a,'N_ordinal':b,'duration':len(chain)+1,'physical_base':source,'internal_events':events})
 return rel

def reject_rule(J,rels):
 for f,first in enumerate(rels):
  a=first['W_ordinal']
  if first['N_ordinal']!=0:continue
  if J<=a+1:return {'rule':'A_first_N_exceeds_total_W','first_relation':f,'a':a,'total_W':J}
  for s,second in enumerate(rels):
   c=second['W_ordinal'];b=second['N_ordinal']
   if c==a+1 and b!=1:return {'rule':'B_immediate_N_ordinal_skip','first_relation':f,'second_relation':s,'a':a,'b':b}
   if c==a+2 and b==2 and J==a+3:return {'rule':'C_consecutive_LN_events','first_relation':f,'second_relation':s,'a':a,'total_W':J}
 return None

def main():
 raw=(ROOT/'certify_diagonal_read_minimum.json').read_bytes();domain=json.loads(raw);rejected=[];remaining=[];stats=Counter();family=Counter()
 for c in domain['cases']:
  for s in c.get('survivors',[]):
   H=c['lower_headings']+s['A_headings'];kind,G=base.graph(H);assert kind=='open';relations=return_paths(H,G);a,b=H[-2:]
   oc=lambda h,d:sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(h))
   counts=[{'incoming_N':oc(a,0),'outgoing_W':b.count(3)},{'incoming_N':oc(b,0),'outgoing_W':a.count(3)}]
   rule=None;lane=None
   for r in(0,1):
    z=reject_rule(counts[r]['outgoing_W'],relations[r])
    if z is not None:rule=z;lane=r;break
   item={'lower_case':c['case'],'A_indices':s['A_indices'],'complete_named_histories':H,'next_Q_counts':counts,'actual_first_return_paths':relations}
   if rule is not None:
    item.update({'contradictory_lane':lane,'witness':rule});rejected.append(item);stats[rule['rule']]+=1;family[c['case']]+=1
   else:remaining.append({'lower_case':c['case'],'A_indices':s['A_indices']})
 assert len(rejected)==68 and len(remaining)==159
 # Previously signed independent all-period exclusions. No SMT premise.
 skipped={(3,(1,0)),(3,(1,1))}
 after_skipped=[z for z in remaining if(z['lower_case'],tuple(z['A_indices']))not in skipped]
 g8=[z for z in after_skipped if z['lower_case']!=4]
 assert len(after_skipped)==157 and len(g8)==155
 key=lambda z:(z['lower_case'],tuple(z['A_indices']))
 all_ids={key(z)for z in rejected+remaining};new_ids={key(z)for z in rejected}
 cyclic={z for z in all_ids if z[0]==4};assert len(all_ids)==227 and len(cyclic)==9
 assert skipped<=all_ids and not(new_ids&skipped) and len(new_ids&cyclic)==7
 prior216=all_ids-cyclic-skipped;new_additional=prior216&new_ids;final=prior216-new_ids
 assert len(prior216)==216 and len(new_additional)==61 and len(final)==155 and final==set(map(key,g8))
 serial=lambda zs:[[a,list(b)]for a,b in sorted(zs)]
 overlaps={'all_nine_prior_cyclic_E_ids':serial(cyclic),'both_prior_skipped_middle_ids':serial(skipped),'new_68_intersection_cyclic_E':serial(new_ids&cyclic),'new_68_intersection_skipped_middle':serial(new_ids&skipped),'new_61_ids_relative_to_prior216':serial(new_additional),'exact_final155_ids':serial(final)}
 result={'scope':__doc__,'signed_lower_domain_sha256':hashlib.sha256(raw).hexdigest(),'input_open_interfaces':227,'newly_rejected_interfaces':68,'rule_counts':dict(stats),'explicit_set_difference':overlaps,'rejected_by_lower_family':dict(family),'remaining_before_other_signed_reductions':remaining,'all_growth_remaining_after_skipped_middle':157,'g8_remaining_after_signed_cyclic_E':155,'g8_remaining_case_ids':g8,'rejections':rejected,'limitations':'Necessary local interface reduction only. No higher field completion, period or width bound, g8 existence, or full controller classification.'}
 (ROOT/'first_N_return_rules_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('remaining_before_other_signed_reductions','g8_remaining_case_ids','rejections')},indent=2))
if __name__=='__main__':main()
