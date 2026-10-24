#!/usr/bin/env python3
"""Strengthens frozen finite windows by exact first physical return ranks."""
from pathlib import Path
from collections import deque
import json,sys,time
from probe_diagonal_n_window import rows,bad_window as prior_bad

def bad_window(seq,p,ss,n):
 old=prior_bad(seq,p,ss,n)
 if old:return old
 hs=[[c['h'] for c in ss[(p+i)%2][s]['cells']] for i,s in enumerate(seq)]
 ev=[(i,c,j) for i,rr in enumerate(hs) for c,h in enumerate(rr) for j in range(len(h))];succ={}
 for i in range(len(seq)-1):
  par=(p+i)%2
  for c in range(n):
   arcs=[(i,c,i+1,c,0,0),(i+1,c,i,(c+1)%n,1,int(c==n-1))] if par==0 else [(i,c,i+1,(c-1)%n,3,-int(c==0)),(i+1,c,i,c,2,0)]
   for a,ac,b,bc,d,k in arcs:
    os=[j for j,h in enumerate(hs[a][ac]) if (h+(1 if j%2==0 else -1))%4==d];ins=[j for j,h in enumerate(hs[b][bc]) if h==d]
    assert len(os)==len(ins)
    for j,l in zip(os,ins):succ[a,ac,j]=((b,bc,l),k)
 for s in ev:
  u=s;w=0;seen={u}
  while u in succ:
   u,k=succ[u];w+=k
   if u in seen:break
   seen.add(u)
   if u[:2]==s[:2] and w==0:
    if u[2]!=s[2]+1:return 'physical_rank_skip'
    break
 return None

def run(cap,n,k=3,max_states=300000):
 st=time.time();ss=[rows(p,cap,n) for p in (0,1)];adj={}
 for p in (0,1):
  ix={}
  for j,b in enumerate(ss[1-p]):
   B=b['cells'];sig=tuple((B[c]['ins'][0],B[c]['outs'][1]) for c in range(n)) if p==0 else tuple((B[(c-1)%n]['ins'][3],B[c]['outs'][2]) for c in range(n));ix.setdefault(sig,[]).append(j)
  for i,a in enumerate(ss[p]):
   A=a['cells'];sig=tuple((A[c]['outs'][0],A[(c+1)%n]['ins'][1]) for c in range(n)) if p==0 else tuple((A[c]['outs'][3],A[c]['ins'][2]) for c in range(n));adj[p,i]=ix.get(sig,[])
 print(json.dumps(dict(stage='static',cap=cap,n=n,row_states=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 start=(0,(0,)*(k-1),0);states=[start];ix={start:0};q=deque([0]);parent={0:None};edges=[];reject={};cache={};end=None;unknown=False;last=st
 while q:
  u=q.popleft();p,seq,w=states[u];lastpar=(p+k-2)%2;newpar=1-lastpar
  for j in adj[lastpar,seq[-1]]:
   key=p,seq,j
   if key not in cache:cache[key]=bad_window(seq+(j,),p,ss,n)
   bad=cache[key]
   if bad:reject[bad]=reject.get(bad,0)+1;continue
   v=(1-p,(seq+(j,))[1:],(w+ss[newpar][j]['voltage'])%2)
   if v not in ix:
    ix[v]=len(states);states.append(v);q.append(ix[v]);parent[ix[v]]=(u,j)
    if len(states)>max_states:unknown=True;break
    if not any(v[1]) and v[2]==1:end=ix[v];break
   edges.append((u,ix[v],j))
  if end or unknown:break
  if time.time()-last>20:print(json.dumps(dict(stage='graph',states=len(states),edges=len(edges),queue=len(q),seconds=time.time()-st)),flush=True);last=time.time()
 path=[]
 if end:
  u=end
  while parent[u] is not None:u,j=parent[u];path.append(j)
  path.reverse()
 result=dict(cap=cap,n=n,window=k,states=len(states),edges=len(edges),rejected=reject,seconds=time.time()-st,status='ODD_EMPTY_REACHABLE_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_FIRST_RETURN_WINDOW_CERTIFICATE'),witness=path)
 base=Path(__file__).with_name(f'diagonal_n{n}_first_return_cap{cap}_window{k}')
 if not end and not unknown:base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,n=n,window=k),histories=ss,states=states,edges=edges))+'\n')
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='witness'}),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
