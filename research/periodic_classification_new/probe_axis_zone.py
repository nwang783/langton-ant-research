#!/usr/bin/env python3
"""All-width finite necessary zone automaton, full drift(2n,0)."""
from pathlib import Path
from itertools import product
from collections import deque
import time,sys,json
from probe_diagonal_n_window import histories
from probe_axis_zone_core import transitions

def rows(p,cap,n):
 hs=[histories((p+c)%2,cap) for c in range(n)];out=[]
 for ids in product(range(2**(cap+1)-1),repeat=n):
  cc=[hs[c][i] for c,i in enumerate(ids)]
  if any(cc[c]['outs'][d]!=cc[(c+dx)%n]['ins'][d] for c in range(n) if (c+p)%2==1 for d,dx in [(1,1),(3,-1)]):continue
  out.append(cc)
 return out

def run(cap,n=1,M=2,mod=2,max_states=200000):
 st=time.time();n*=2;ss=[rows(p,cap,n) for p in (0,1)];adj={}
 for p in (0,1):
  ix={}
  for j,B in enumerate(ss[1-p]):
   sig=tuple(B[c]['ins'][0] if (c+p)%2==0 else B[c]['outs'][2] for c in range(n));ix.setdefault(sig,[]).append(j)
  for i,A in enumerate(ss[p]):
   sig=tuple(A[c]['outs'][0] if (c+p)%2==0 else A[c]['ins'][2] for c in range(n));adj[p,i]=ix.get(sig,[])
 print(json.dumps(dict(stage='static',cap=cap,full_drift=[n,0],rows=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 start=(0,0,(),());states=[start];ix={start:0};q=deque([0]);parents={0:None};edges=[];reject={};cache={};end=None;unknown=False;last=st
 while q:
  u=q.popleft();p,i,paths,flat=states[u]
  for j in adj[p,i]:
   key=p,i,j,paths,flat
   if key not in cache:cache[key]=transitions(paths,flat,[a['h'] for a in ss[p][i]],[b['h'] for b in ss[1-p][j]],p,mod,M)
   outs,reason=cache[key]
   if not outs:reject[reason]=reject.get(reason,0)+1;continue
   if outs==['POTENTIAL_COMPLETE_FRONT']:end=(u,j);break
   for np,nd in outs:
    v=(1-p,j,np,nd)
    if v not in ix:
     ix[v]=len(states);states.append(v);q.append(ix[v]);parents[ix[v]]=(u,j)
     if len(states)>max_states:unknown=True;break
    edges.append((u,ix[v],j))
   if unknown:break
  if end or unknown:break
  if time.time()-last>20:print(json.dumps(dict(stage='graph',states=len(states),edges=len(edges),queue=len(q),seconds=time.time()-st)),flush=True);last=time.time()
 path=[]
 if end:
  u,j=end;path=[j]
  while parents[u] is not None:u,j=parents[u];path.append(j)
  path.reverse()
 result=dict(cap=cap,full_drift=[n,0],bound=M,modulus=mod,states=len(states),edges=len(edges),rejected=reject,seconds=time.time()-st,status='POTENTIAL_COMPLETE_FRONT_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_AXIS_ZONE_CERTIFICATE'),witness=path)
 base=Path(__file__).with_name(f'axis_d{n}_0_zone_cap{cap}_bound{M}_mod{mod}')
 if not end and not unknown:base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,full_drift=[n,0],bound=M,modulus=mod),histories=ss,states=states,edges=edges))+'\n')
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
