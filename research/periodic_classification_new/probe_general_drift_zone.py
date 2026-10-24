#!/usr/bin/env python3
"""All-width zone relaxation for full drift(a,b), normalized a>0, |b|<=a."""
from pathlib import Path
from itertools import product
from collections import deque
import time,sys,json
from probe_diagonal_n_window import histories
from frontier_drift_geometry import Geometry
from probe_general_drift_zone_core import transitions

def rows(p,cap,g):
 n=g.a;hs=[histories(g.parity(p,c),cap) for c in range(n)];out=[]
 internal=[e for e in g.arcs[p] if e[4]==0]
 for ids in product(range(2**(cap+1)-1),repeat=n):
  cc=[hs[c][i] for c,i in enumerate(ids)]
  if any(cc[c]['outs'][d]!=cc[bc]['ins'][d] for c,bc,d,k,dr in internal):continue
  out.append(cc)
 return out

def run(cap,a,b,M=2,mod=2,max_states=200000):
 st=time.time();g=Geometry(a,b);ss=[rows(p,cap,g) for p in (0,1)];adj={}
 for p in (0,1):
  cross=[e for e in g.splice_arcs(p) if e[0]!=e[2]];ix={}
  for j,B in enumerate(ss[1-p]):
   sig=tuple(B[bc]['ins'][d] if ar==0 else B[ac]['outs'][d] for ar,ac,br,bc,d,k in cross);ix.setdefault(sig,[]).append(j)
  for i,A in enumerate(ss[p]):
   sig=tuple(A[ac]['outs'][d] if ar==0 else A[bc]['ins'][d] for ar,ac,br,bc,d,k in cross);adj[p,i]=ix.get(sig,[])
 print(json.dumps(dict(stage='static',cap=cap,full_drift=[a,b],rows=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 start=(0,0,(),());states=[start];ix={start:0};q=deque([0]);parents={0:None};edges=[];reject={};cache={};end=None;unknown=False;last=st
 while q:
  u=q.popleft();p,i,paths,flat=states[u]
  for j in adj[p,i]:
   key=p,i,j,paths,flat
   if key not in cache:cache[key]=transitions(paths,flat,[c['h'] for c in ss[p][i]],[c['h'] for c in ss[1-p][j]],p,g,mod,M)
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
 result=dict(cap=cap,full_drift=[a,b],bound=M,modulus=mod,states=len(states),edges=len(edges),rejected=reject,seconds=time.time()-st,status='POTENTIAL_COMPLETE_FRONT_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_GENERAL_DRIFT_ZONE_CERTIFICATE'),witness=path)
 base=Path(__file__).with_name(f'general_d{a}_{b}_zone_cap{cap}_bound{M}_mod{mod}')
 if not end and not unknown:base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,full_drift=[a,b],bound=M,modulus=mod),histories=ss,states=states,edges=edges))+'\n')
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
