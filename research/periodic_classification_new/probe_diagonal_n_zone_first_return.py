#!/usr/bin/env python3
"""All-width finite zone relaxation for full drift(n,n), finite local cap.
UNKNOWN on state cap; whole-cycle candidate is a relaxation until replay.
"""
from pathlib import Path
from collections import deque
import json,sys,time
from probe_diagonal_n_window import rows
from probe_diagonal_n_first_return import bad_window
from probe_diagonal_zone_general import transitions

def run(cap,n,k=3,M=2,mod=2,max_states=200000):
 st=time.time();ss=[rows(p,cap,n) for p in (0,1)];adj={}
 for p in (0,1):
  ix={}
  for j,b in enumerate(ss[1-p]):
   B=b['cells']
   sig=tuple((B[c]['ins'][0],B[c]['outs'][1]) for c in range(n)) if p==0 else tuple((B[(c-1)%n]['ins'][3],B[c]['outs'][2]) for c in range(n))
   ix.setdefault(sig,[]).append(j)
  for i,a in enumerate(ss[p]):
   A=a['cells']
   sig=tuple((A[c]['outs'][0],A[(c+1)%n]['ins'][1]) for c in range(n)) if p==0 else tuple((A[c]['outs'][3],A[c]['ins'][2]) for c in range(n))
   adj[p,i]=ix.get(sig,[])
 print(json.dumps(dict(stage='static',cap=cap,n=n,states=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 start=(0,(0,)*(k-1),(),());states=[start];ix={start:0};q=deque([0]);parents={0:None};edges=[];reject={};badcache={};zcache={};end=None;unknown=False;lastreport=st
 while q:
  u=q.popleft();p,seq,paths,flat=states[u];lastpar=(p+k-2)%2
  for j in adj[lastpar,seq[-1]]:
   key=(p,seq,j)
   if key not in badcache:badcache[key]=bad_window(seq+(j,),p,ss,n)
   bad=badcache[key]
   if bad:reason='window_'+bad;reject[reason]=reject.get(reason,0)+1;continue
   key2=(lastpar,seq[-1],j,paths,flat)
   if key2 not in zcache:zcache[key2]=transitions(paths,flat,[c['h'] for c in ss[lastpar][seq[-1]]['cells']],[c['h'] for c in ss[1-lastpar][j]['cells']],lastpar,mod,M)
   outs,reason=zcache[key2]
   if not outs:reject[reason]=reject.get(reason,0)+1;continue
   if outs==['POTENTIAL_COMPLETE_FRONT']:end=(u,j);break
   for np,nd in outs:
    v=(1-p,(seq+(j,))[1:],np,nd)
    if v not in ix:
     ix[v]=len(states);states.append(v);q.append(ix[v]);parents[ix[v]]=(u,j)
     if len(states)>max_states:unknown=True;break
    edges.append((u,ix[v],j))
   if unknown:break
  if end or unknown:break
  if time.time()-lastreport>20:
   print(json.dumps(dict(stage='graph',states=len(states),queue=len(q),edges=len(edges),seconds=time.time()-st)),flush=True);lastreport=time.time()
 path=[]
 if end:
  u,j=end;path=[j]
  while parents[u] is not None:u,j=parents[u];path.append(j)
  path.reverse()
 result=dict(cap=cap,n=n,window=k,bound=M,modulus=mod,states=len(states),edges=len(edges),rejected=reject,cache_sizes=[len(badcache),len(zcache)],seconds=time.time()-st,status='POTENTIAL_COMPLETE_FRONT_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_ZONE_EXCLUSION_CERTIFICATE'),witness=path)
 base=Path(__file__).with_name(f'diagonal_n{n}_zone_first_return_cap{cap}_window{k}_bound{M}_mod{mod}')
 if not end and not unknown:base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,n=n,window=k,bound=M,modulus=mod),histories=ss,states=states,edges=edges))+'\n')
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
