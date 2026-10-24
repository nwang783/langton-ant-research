#!/usr/bin/env python3
from collections import deque
from functools import lru_cache
from general_first_return_window import bad_window
from pathlib import Path
import sys,time,json
from frontier_zero_flux_rows import rows
from frontier_drift_geometry import Geometry
from probe_general_drift_zone_core import splice as general_splice
from probe_normalized_real_zone_core import transitions

def run(cap,a,b,N=18,M=36,mod=2,max_states=150000):
 st=time.time();g=Geometry(a,b);ss=[rows(p,cap,g) for p in (0,1)];adj={}
 splice=lambda paths,old,new,p,mod:general_splice(paths,old,new,p,mod,g)
 for p in (0,1):
  cross=[e for e in g.splice_arcs(p) if e[0]!=e[2]];ix={}
  for j,B in enumerate(ss[1-p]):
   sig=tuple(B[bc]['ins'][d] if ar==0 else B[ac]['outs'][d] for ar,ac,br,bc,d,k in cross);ix.setdefault(sig,[]).append(j)
  for i,A in enumerate(ss[p]):
   sig=tuple(A[ac]['outs'][d] if ar==0 else A[bc]['ins'][d] for ar,ac,br,bc,d,k in cross);adj[p,i]=ix.get(sig,[])
 @lru_cache(maxsize=500000)
 def literal_bad(p,i,j):return bad_window([[a['h'] for a in ss[p][i]],[b['h'] for b in ss[1-p][j]]],p,g)
 print(json.dumps(dict(stage='static',cap=cap,rows=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 start=(0,0,(),());states=[start];ix={start:0};q=deque([0]);parents={0:None};edges=[];reject={};end=None;unknown=False;last=st;attempts=0
 while q:
  u=q.popleft();p,i,paths,flat=states[u]
  for j in adj[p,i]:
   attempts+=1;reason=literal_bad(p,i,j)
   if reason:reject['window_'+reason]=reject.get('window_'+reason,0)+1;continue
   outs,reason=transitions(paths,flat,[a['h'] for a in ss[p][i]],[b['h'] for b in ss[1-p][j]],p,splice,mod,M,N)
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
 result=dict(cap=cap,full_drift=[a,b],clock_scale=N,bound=M,modulus=mod,window=2,states=len(states),edges=len(edges),attempts=attempts,rejected=reject,seconds=time.time()-st,status='POTENTIAL_COMPLETE_FRONT_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_NORMALIZED_REAL_ZONE_CANDIDATE'),witness=path)
 base=Path(__file__).with_name(f'general_flux_d{a}_{b}_first_return_real_cap{cap}_N{N}_M{M}_mod{mod}')
 if not end and not unknown:base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,full_drift=[a,b],clock_scale=N,bound=M,modulus=mod,window=2),histories=ss,states=states,edges=edges))+'\n')
 if end:
  parity=0;result['witness_rows']=[]
  for j in path:parity=1-parity;result['witness_rows'].append([a['h'] for a in ss[parity][j]])
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
