#!/usr/bin/env python3
"""All-width geometry-only flow automaton for fixed positive non-axis drift.
No time/period/support bound. A zero integer edge-potential on the empty
state's recurrent component certifies zero flux for EVERY finite support.
This is discovery code, not yet independently audited.
"""
from itertools import product
from collections import defaultdict,deque
from pathlib import Path
import json,sys,time
from probe_one_a_local_constraints import states

def digits(n,a):
 out=[]
 for _ in range(a):out.append(n%3);n//=3
 return tuple(out)
def enc(xs):
 k=0
 for x in reversed(xs):k=3*k+x
 return k

def celltypes(parity):
 vals={}
 for name,hist in states((0,parity)):
  ins=[sum(h==d for c,h in hist) for d in range(4)];out=[sum((h+c)%4==d for c,h in hist) for d in range(4)]
  N=out[0]+ins[2];E=out[1]+ins[3];S=out[2]+ins[0];W=out[3]+ins[1]
  vals[(N,E,S,W)]=name
 assert len(vals)==9
 return [(key,name) for key,name in vals.items()]
CT=[celltypes(p) for p in range(2)]
def rowtypes(a,p):
 rows={}
 def rec(k,ns,ss,e,w,names):
  if k==a:
   rows[(enc(ns),enc(ss),e,w)]=names;return
  for (N,E,S,W),name in CT[(k+p)%2]:
   if k and W!=e:continue
   rec(k+1,ns+(N,),ss+(S,),E,W if not k else w,names+(name,))
 rec(0,(),(),0,0,())
 by=defaultdict(list)
 for (N,S,E,W),names in rows.items():by[S,E].append((N,W,names))
 return by,len(rows)

def run(a,b):
 assert a>0 and b>0 and (a+b)%2==0
 start=time.time();rs=[];rns=[]
 for p in range(2):r,n=rowtypes(a,p);rs.append(r);rns.append(n)
 # State=(parity, north boundary of previous row, W queue of previous b rows).
 root=(0,0,0);seen={root:0};nodes=[root];adj=[];rev=[[]];powb=3**(b-1)
 for state in nodes:
  p,N,q=state;e=q%3;opts=rs[p].get((N,e),[]);edges=[]
  for n,w,names in opts:
   dest=(1-p,n,q//3+w*powb)
   if dest not in seen:seen[dest]=len(nodes);nodes.append(dest);rev.append([])
   j=seen[dest];i=seen[state];weight=e*(1 if (a+p)%2==0 else -1)
   edges.append((j,weight,names));rev[j].append(i)
  adj.append(edges)
 # Exactly those root-reachable states that can return to root matter.
 core={0};todo=[0]
 while todo:
  j=todo.pop()
  for i in rev[j]:
   if i not in core:core.add(i);todo.append(i)
 phi={0:0};todo=[0];conflict=None;coreedges=0
 while todo:
  i=todo.pop()
  for j,w,names in adj[i]:
   if j not in core:continue
   coreedges+=1
   if j not in phi:phi[j]=phi[i]+w;todo.append(j)
   elif phi[j]!=phi[i]+w:conflict=(i,j,w,phi[i],phi[j]);break
  if conflict:break
 res=dict(drift=[a,b],row_type_counts=rns,reachable_states=len(nodes),empty_scc_states=len(core),core_edges_checked=coreedges,status='NONZERO_CYCLE_RELAXATION' if conflict else'ZERO_FLUX_ALL_WIDTHS_STATIC',seconds=time.time()-start)
 if conflict:res['conflict']=[list(nodes[conflict[0]]),list(nodes[conflict[1]]),*conflict[2:]]
 else:
  cert=dict(drift=[a,b],states=[dict(state=list(nodes[i]),potential=phi[i]) for i in sorted(core)])
  Path(__file__).with_name(f'cap3_static_row_d{a}_{b}_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
  res['potential_range']=[min(phi.values()),max(phi.values())]
 Path(__file__).with_name(f'cap3_static_row_d{a}_{b}.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
 return res
if __name__=='__main__':run(*map(int,sys.argv[1:]))
