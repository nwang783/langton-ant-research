import json,time
from collections import Counter
from itertools import product
from certify_one_minimum_three_branches import domains,allowed,inventory
from partial_complete_histories_graph import graph
z=json.load(open('one_minimum_fourth_branch_discovery.json'));parents=z['rounds'][1]['survivors'];stats=Counter();remain=[];start=time.time()
for ind,H in enumerate(parents):
 k,G=graph(H);assert k=='open';ds,ports,rels,bounds=domains(H,G);pts=G['points'];nextT=len(H)//2-1;new=[]
 for lane,domain in enumerate(ds):
  kept=[]
  for oi,hs in enumerate(domain):
   pp=pts+[(lane,nextT-lane)];HH=H+[hs]
   # Full parity budget on arbitrary point lists, not packed two-lane index.
   v=[0]*4
   for p,h in zip(pp,HH):
    if len(h)%2:v[2*(p[0]%2)+p[1]%2]+=1
   from certify_one_minimum_three_branches import TARGETS
   if not any(all(a<=b for a,b in zip(v,t))for t in TARGETS):kind='residue_budget'
   else:kind,w=graph(HH,pp)
   if kind=='closed_component'and w['winding']>0 and w['other_local_events']==0:kind='open'
   stats['single_'+kind]+=1
   if kind=='open':kept.append(oi)
  new.append(kept)
 n=len(new[0])*len(new[1]);stats['remaining_pairs']+=n;stats['initial_pairs']+=len(ds[0])*len(ds[1]);stats['parents_with_pairs']+=bool(n)
 remain.append({'parent':ind,'original_domain_sizes':list(map(len,ds)),'remaining_indices':new,'remaining_pairs':n})
print(dict(stats),'seconds',time.time()-start,flush=True)
json.dump({'scope':'Discovery only; partial complete cells','stats':dict(stats),'parents':remain},open('one_minimum_fourth_partial_pruning_discovery.json','w'),indent=2)
