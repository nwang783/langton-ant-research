#!/usr/bin/env python3
"""Last one-minimum g8 interface: two full rows, then one-cell open-boundary cover.
All bounds follow mandatory port counts; no period, support, or global visit cap.
"""
import json,hashlib,time,random
from collections import Counter
from pathlib import Path
from certify_one_minimum_three_branches import domains,allowed,inventory,TARGETS
from partial_complete_histories_graph import graph
ROOT=Path(__file__).resolve().parent

def subset_budget(H,pts):
 v=[0]*4
 for p,hs in zip(pts,H):
  if len(hs)%2:v[2*(p[0]%2)+p[1]%2]+=1
 if any(all(a<=b for a,b in zip(v,t))for t in TARGETS):return None
 return {'named_odd_parity_inventory':v,'violated_bins':[next(i for i,(x,y)in enumerate(zip(v,t))if x>y)for t in TARGETS]}

def check(H,pts=None):
 if pts is None:pts=[(r,t-r)for t in range(-1,len(H)//2-1)for r in(0,1)]
 w=subset_budget(H,pts)
 if w:return'residue_budget',w
 k,w=graph(H,pts)
 if k=='closed_component':assert w['winding']<=0 or w['other_local_events']>0
 return k,w

def main():
 start=time.time();source=json.loads((ROOT/'certify_diagonal_read_minimum.json').read_text());c=source['cases'][3];s=next(x for x in c['survivors']if x['A_indices']==[3,1]);initial=[tuple(h)for h in c['lower_headings']+s['A_headings']];frontier=[initial];rounds=[];stats=Counter();winds=Counter()
 for row in range(2):
  details=[];nxt=[];ss=Counter()
  for H in frontier:
   k,G=graph(H);assert k=='open'and allowed(H);(AA,BB),ports,rels,bounds=domains(H,G);pairs=[]
   for ai,a in enumerate(AA):
    for bi,b in enumerate(BB):
     HH=H+[a,b];kind,w=check(HH);ss[kind]+=1;stats[kind]+=1;item={'helper_indices':[ai,bi],'outcome':kind}
     if kind=='open':nxt.append(HH)
     else:
      item['witness']=w
      if kind=='closed_component':winds[w['winding']]+=1
     pairs.append(item)
   details.append({'complete_histories':H,'port_counts':ports,'derived_read_bounds':bounds,'actual_first_return_paths':rels,'complete_helper_domains':[AA,BB],'all_pairs':pairs})
  rounds.append({'parent_count':len(frontier),'outcomes':dict(ss),'parents':details});frontier=nxt
  print('FULL ROW',row,dict(ss),flush=True)
 assert len(frontier)==1312
 terminal=[];ts=Counter();maxbound=0
 for ind,H in enumerate(frontier):
  k,G=graph(H);assert k=='open';ds,ports,rels,bounds=domains(H,G);pts=G['points'];level=len(H)//2-1;chosen=None
  # Lane-selection order is only a certificate-size heuristic. Whatever lane
  # is selected, ALL of its exact complete words must have explicit rejections.
  for lane in sorted((0,1),key=lambda r:(len(ds[r]),r)):
   pp=pts+[(lane,level-lane)];fail=[];ok=False
   for oi,hs in enumerate(ds[lane]):
    kind,w=check(H+[hs],pp)
    if kind=='open':ok=True;break
    fail.append({'helper_index':oi,'outcome':kind,'witness':w})
   if not ok:chosen=(lane,pp,fail);break
  assert chosen is not None,ind
  lane,pp,fail=chosen;ts['empty_domain_parents'if not ds[lane]else'nonempty_domain_parents']+=1;maxbound=max(maxbound,bounds[lane])
  for item in fail:
   ts[item['outcome']]+=1
   if item['outcome']=='closed_component':winds[item['witness']['winding']]+=1
  terminal.append({'parent_index':ind,'complete_lower_histories':H,'selected_lane':lane,'all_complete_points_with_selected_cell':pp,'both_mandatory_port_counts':ports,'selected_derived_bound':bounds[lane],'selected_actual_first_return_paths':rels[lane],'selected_complete_helper_domain':ds[lane],'all_word_rejections':fail,'unselected_lane':'UNRESTRICTED outside mandatory ports; not assumed empty or capped'})
 assert ts['empty_domain_parents']==791 and ts['nonempty_domain_parents']==521 and sum(len(x['all_word_rejections'])for x in terminal)==13968
 # Positive controls for the new arbitrary-complete-subset graph.
 std=json.loads((ROOT/'check_single_used_first_circle.json').read_text())['all_standard_stable_histories'];ps=[tuple(x['point'])for x in std];hs=[tuple('NESW'.index(h)for h in x['headings'])for x in std];rng=random.Random(112);subsets=[]
 for i in range(22):subsets.append([j for j in range(22)if j!=i])
 for _ in range(300):subsets.append(sorted(rng.sample(range(22),rng.randrange(1,22))))
 for ids in subsets:k,w=graph([hs[i]for i in ids],[ps[i]for i in ids]);assert k=='open'
 k,w=graph(hs,ps);assert k=='closed_component'and w['winding']==1 and w['other_local_events']==0
 old=json.loads((ROOT/'diagonal_selected_pair_exclusions_certificate.json').read_text());three=json.loads((ROOT/'one_minimum_three_branches_certificate.json').read_text());oldids={(a,tuple(b))for a,b in old['remaining100_ids']};rem97={(a,tuple(b))for a,b in three['exact_remaining97_ids']};assert(3,(3,1))in rem97;rem96=rem97-{(3,(3,1))};assert len(rem96)==96 and all(a in(5,8,9)for a,b in rem96)
 result={'scope':__doc__,'full_drift':[2,-2],'growth':8,'excluded_coarse_id':[3,[3,1]],'initial_complete_histories':initial,'source227_sha256':hashlib.sha256((ROOT/'certify_diagonal_read_minimum.json').read_bytes()).hexdigest(),'prior100_sha256':hashlib.sha256((ROOT/'diagonal_selected_pair_exclusions_certificate.json').read_bytes()).hexdigest(),'other_three_certificate_sha256':hashlib.sha256((ROOT/'one_minimum_three_branches_certificate.json').read_bytes()).hexdigest(),'ten_full_g8_parity_vectors':TARGETS,'two_full_row_outcomes':dict(stats),'full_rows':rounds,'terminal_parent_count':len(terminal),'terminal_selected_single_helper_word_count':sum(len(x['all_word_rejections'])for x in terminal),'terminal_outcomes':dict(ts),'maximum_selected_derived_bound':maxbound,'closed_windings':dict(winds),'terminal_one_cell_covers':terminal,'partial_graph_controls':{'proper_standard_subsets':subsets,'full_standard_cycle_length':104,'full_standard_winding':1,'full_standard_outside_events':0},'exact_remaining96_coarse_ids':[[a,list(b)]for a,b in sorted(rem96)],'seconds':time.time()-start,'limitations':'All g8 full diagonal-two fronts must have both minimum singleton classes, hence the signed single-used F4 circle. Its96 necessary interfaces are not completed or excluded here. No other drift or universal classification follows.'}
 (ROOT/'one_minimum_last_branch_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('FINAL',dict(ts),'max derived bound',maxbound,'closed windings',dict(winds),'seconds',result['seconds'],flush=True)
if __name__=='__main__':main()
