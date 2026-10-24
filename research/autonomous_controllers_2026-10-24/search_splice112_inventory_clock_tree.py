#!/usr/bin/env python3
"""Exact all-WHITE-order search for ONE112-event full directed count inventory.
Transparent positive-cycle proof tree; a feasible leaf still requires full replay.
"""
import json,time,math,sys,ast
from itertools import combinations,product
from collections import Counter
from pathlib import Path
from check_extremal_read_coupling import quotient,D
from certify_standard_inventory_by_clocks import common,cycle
OUT=Path(__file__).resolve().parent
DRIFT=(2,-2);P=112

def setup():
 z=json.loads((OUT/'probe_standard_upper_splice112.json').read_text())
 H={ast.literal_eval(p):tuple('NESW'.index(x)for x in s)for p,s in z['complete_named_histories'].items() if s}
 points=sorted(H,key=lambda p:(sum(p),p[0]));ix={p:i for i,p in enumerate(points)};options=[];original=[]
 for p in points:
  hs=H[p];n=len(hs);axis=hs[0]%2;assert all(h%2==axis for h in hs)
  counts=Counter((j%2,h)for j,h in enumerate(hs));R=list(range(0,n,2));L=list(range(1,n,2));opts=[]
  for plusR,plusL in product(combinations(R,counts[0,axis]),combinations(L,counts[1,axis])):
   plus=set(plusR)|set(plusL);opts.append(tuple(axis if j in plus else axis+2 for j in range(n)))
  options.append(opts);original.append(opts.index(hs))
 assert sum(map(len,H.values()))==P
 var={};varmeta=[]
 for i,p in enumerate(points):
  hs=options[i][0]
  for heading in range(4):
   m=sum((hi+(1 if j%2==0 else-1))%4==heading for j,hi in enumerate(hs))
   for k in range(m):var[i,heading,k]=len(varmeta);varmeta.append([i,heading,k])
 assert len(var)==P
 allopts=[]
 for i,p in enumerate(points):
  oo=[]
  for hs in options[i]:
   cin=Counter();cout=Counter();incoming=[];outgoing=[];const=[]
   for j,hi in enumerate(hs):
    ho=(hi+(1 if j%2==0 else-1))%4
    q=(p[0]-D[hi][0],p[1]-D[hi][1]);r,k=quotient(q,DRIFT);ii=ix[r]
    ei=var[ii,hi,cin[hi]];cin[hi]+=1;eo=var[i,ho,cout[ho]];cout[ho]+=1
    incoming.append(ei);outgoing.append(eo);const.append(1+k*P)
   ee={}
   def add(u,v,w):ee[u,v]=max(ee.get((u,v),-10**9),w)
   for ei,eo,c in zip(incoming,outgoing,const):add(ei,eo,c);add(eo,ei,-c)
   for j in range(1,len(hs)):add(incoming[j-1],incoming[j],4+const[j-1]-const[j])
   oo.append(ee)
  allopts.append(oo)
 return points,options,original,varmeta,allopts

def merge(base,extra):
 d=dict(base)
 for e,w in extra.items():d[e]=max(d.get(e,-10**9),w)
 return d

def main():
 limit=float(sys.argv[1])if len(sys.argv)>1 else 120
 points,options,original,varmeta,allopts=setup();start=time.time();nodes=[];leaves=[];counts={'removed_options':0,'nodes':0,'positive_cycle_leaves':0,'feasible_complete_leaves':0}
 print('SETUP',len(points),'counts',list(map(len,options)),'product',math.prod(map(len,options)),flush=True)
 def propagate(domains):
  rounds=[]
  while True:
   base=common(allopts,domains);cc=cycle(base,P)
   if cc:return domains,rounds,cc
   removed=[]
   for i,dom in enumerate(domains):
    if len(dom)==1:continue
    for o in dom:
     cc=cycle(merge(base,allopts[i][o]),P)
     if cc:removed.append({'cell':i,'option':o,'cycle':cc})
   if not removed:return domains,rounds,None
   rounds.append({'removed':removed});counts['removed_options']+=len(removed)
   rr={(z['cell'],z['option'])for z in removed};domains=[[o for o in dom if(i,o)not in rr]for i,dom in enumerate(domains)]
   if any(not d for d in domains):return domains,rounds,'empty_domain'
 def dfs(domains):
  if time.time()-start>limit:raise TimeoutError()
  ident=len(nodes);node={'id':ident,'input_domains':domains};nodes.append(node);counts['nodes']+=1
  dom,rounds,bad=propagate(domains);node['propagation']=rounds;node['after_domains']=dom
  if bad:node.update(leaf='infeasible',reason=bad);counts['positive_cycle_leaves']+=1;return ident
  undec=[i for i,d in enumerate(dom)if len(d)>1]
  if not undec:
   leaf=[d[0]for d in dom];node.update(leaf='feasible_complete',options=leaf);leaves.append(leaf);counts['feasible_complete_leaves']+=1;print('SOLUTION',ident,leaf,'seconds',time.time()-start,flush=True);return ident
  branch=min(undec,key=lambda i:(len(dom[i]),i));node.update(branch_cell=branch,children=[])
  for o in dom[branch]:
   dd=[list(d)for d in dom];dd[branch]=[o];node['children'].append({'option':o,'node':dfs(dd)})
  if ident%20==0:print('DONE NODE',ident,'total',len(nodes),'seconds',time.time()-start,flush=True)
  return ident
 complete=True
 try:dfs([list(range(len(x)))for x in allopts])
 except TimeoutError:complete=False
 result={'scope':__doc__,'full_drift':DRIFT,'P':P,'points':points,'all_cell_heading_options':[[''.join('NESW'[h]for h in hs)for hs in oo]for oo in options],'original_options':original,'variables':varmeta,'complete':complete,'raw_option_product':math.prod(map(len,options)),'counts':counts,'seconds':time.time()-start,'feasible_complete_options':leaves,'nodes':nodes}
 (OUT/'splice112_inventory_clock_tree.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('FINISHED',complete,counts,'seconds',result['seconds'],flush=True)
if __name__=='__main__':main()
