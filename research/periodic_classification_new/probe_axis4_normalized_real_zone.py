#!/usr/bin/env python3
from collections import deque
from pathlib import Path
import sys,time,json
from probe_axis4_fast_zone import rows
from probe_axis_zone_core import splice
from probe_normalized_real_zone_core import transitions

def run(cap,N=8,M=16,mod=2,max_states=200000):
 st=time.time();ss=[rows(p,cap,4) for p in (0,1)];adj={}
 for p in (0,1):
  ix={}
  for j,B in enumerate(ss[1-p]):
   sig=tuple(B[c]['ins'][0] if (c+p)%2==0 else B[c]['outs'][2] for c in range(4));ix.setdefault(sig,[]).append(j)
  for i,A in enumerate(ss[p]):
   sig=tuple(A[c]['outs'][0] if (c+p)%2==0 else A[c]['ins'][2] for c in range(4));adj[p,i]=ix.get(sig,[])
 print(json.dumps(dict(stage='static',cap=cap,rows=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 start=(0,0,(),());states=[start];ix={start:0};q=deque([0]);parents={0:None};edges=[];reject={};end=None;unknown=False;last=st;attempts=0
 while q:
  u=q.popleft();p,i,paths,flat=states[u]
  for j in adj[p,i]:
   attempts+=1;outs,reason=transitions(paths,flat,[a['h'] for a in ss[p][i]],[b['h'] for b in ss[1-p][j]],p,splice,mod,M,N)
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
  if time.time()-last>20:
   print(json.dumps(dict(stage='graph',states=len(states),edges=len(edges),queue=len(q),attempts=attempts,seconds=time.time()-st)),flush=True);last=time.time()
 path=[]
 if end:
  u,j=end;path=[j]
  while parents[u] is not None:u,j=parents[u];path.append(j)
  path.reverse()
 result=dict(cap=cap,full_drift=[4,0],clock_scale=N,bound=M,modulus=mod,states=len(states),edges=len(edges),attempts=attempts,rejected=reject,seconds=time.time()-st,status='POTENTIAL_COMPLETE_FRONT_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_NORMALIZED_REAL_ZONE_CANDIDATE'),witness=path)
 base=Path(__file__).with_name(f'axis4_normalized_real_cap{cap}_N{N}_M{M}_mod{mod}')
 if not end and not unknown:base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,full_drift=[4,0],clock_scale=N,bound=M,modulus=mod),histories=ss,states=states,edges=edges))+'\n')
 if end:
  parity=0;result['witness_rows']=[]
  for j in path:parity=1-parity;result['witness_rows'].append([a['h'] for a in ss[parity][j]])
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
