#!/usr/bin/env python3
"""Exhaustive branch certificate over exact finite local clock options."""
import json,time,sys,math
from pathlib import Path
from certify_standard_inventory_by_clocks import constraints,common,cycle,P
OUT=Path(__file__).resolve().parent
START=time.time();LIMIT=float(sys.argv[1])if len(sys.argv)>1 else 120
ALL,ORIGINAL,VARS=constraints();NODES=[];LEAVES=[];COUNTS={'removed_options':0,'nodes':0,'positive_cycle_leaves':0,'feasible_complete_leaves':0}

def merge(base,extra):
 d=dict(base)
 for e,w in extra.items():d[e]=max(d.get(e,-10**9),w)
 return d

def propagate(domains):
 rounds=[]
 while True:
  base=common(ALL,domains);cc=cycle(base)
  if cc:return domains,rounds,cc
  removed=[]
  for i,dom in enumerate(domains):
   if len(dom)==1:continue
   for o in dom:
    cc=cycle(merge(base,ALL[i][o]))
    if cc:removed.append({'cell':i,'option':o,'cycle':cc})
  if not removed:return domains,rounds,None
  rounds.append({'removed':removed});COUNTS['removed_options']+=len(removed)
  rr={(z['cell'],z['option'])for z in removed};domains=[[o for o in dom if(i,o)not in rr]for i,dom in enumerate(domains)]
  if any(not d for d in domains):return domains,rounds,'empty_domain'

def dfs(domains):
 if time.time()-START>LIMIT:raise TimeoutError()
 ident=len(NODES);node={'id':ident,'input_domains':domains};NODES.append(node);COUNTS['nodes']+=1
 dom,rounds,bad=propagate(domains);node['propagation']=rounds;node['after_domains']=dom
 if bad:
  node['leaf']='infeasible';node['reason']=bad;COUNTS['positive_cycle_leaves']+=1;return ident
 undec=[i for i,d in enumerate(dom)if len(d)>1]
 if not undec:
  node['leaf']='feasible_complete';node['options']=[d[0]for d in dom];LEAVES.append(node['options']);COUNTS['feasible_complete_leaves']+=1;print('SOLUTION',ident,'standard',node['options']==ORIGINAL,'seconds',time.time()-START,flush=True);return ident
 branch=min(undec,key=lambda i:(len(dom[i]),i));node['branch_cell']=branch;node['children']=[]
 for o in dom[branch]:
  dd=[list(d)for d in dom];dd[branch]=[o];node['children'].append({'option':o,'node':dfs(dd)})
 if ident%20==0:print('DONE NODE',ident,'total',len(NODES),'seconds',time.time()-START,flush=True)
 return ident

def main():
 complete=True
 try:dfs([list(range(len(x)))for x in ALL])
 except TimeoutError:complete=False
 result={'scope':__doc__,'complete':complete,'counts':COUNTS,'seconds':time.time()-START,'variables':VARS,'standard_options':ORIGINAL,'feasible_complete_options':LEAVES,'nodes':NODES}
 (OUT/'standard_inventory_clock_tree.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('FINISHED',complete,COUNTS,'seconds',result['seconds'],flush=True)
if __name__=='__main__':main()
