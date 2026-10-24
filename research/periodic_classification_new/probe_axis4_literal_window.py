#!/usr/bin/env python3
"""Literal finite row-window rank/winding tests, exact necessary conditions.
A passing window is not a front. Resource limits remain UNKNOWN.
"""
from pathlib import Path
from collections import deque
from functools import lru_cache
import sys,time,json
from probe_axis4_fast_zone import rows
D=((0,1),(1,0),(0,-1),(-1,0))

def bad_window(hs):
 H=len(hs);n=4;events=[];ins={};outs={}
 for y,row in enumerate(hs):
  for x,h in enumerate(row):
   for j,a in enumerate(h):
    e=(y,x,j);events.append(e);ins.setdefault((y,x,a),[]).append(e);g=(a+(1 if j%2==0 else -1))%4;outs.setdefault((y,x,g),[]).append(e)
 succ={}
 for (y,x,g),es in outs.items():
  dx,dy=D[g];xx=x+dx;yy=y+dy
  if not 0<=yy<H:continue
  ts=ins.get((yy,xx%4,g),[]);assert len(es)==len(ts)
  for a,b in zip(es,ts):succ[a]=(b,xx//4)
 for start in events:
  cur=start;w=0;seen={start}
  while cur in succ:
   cur,k=succ[cur];w+=k
   if cur in seen:
    cyc=[];a=cur;cw=0
    while True:
     cyc.append(a);a,k=succ[a];cw+=k
     if a==cur:break
    if len(cyc)!=len(events) or cw!=1:return 'closed_cycle'
    # Whole-window voltage-one cycle is not rejected as a proper subcycle.
    break
   seen.add(cur)
   if cur[:2]==start[:2] and ((cur[2]>start[2] and w>0) or (cur[2]<start[2] and w<=0)):return 'wrong_order_segment'
 return None

def run(cap,k=2,max_states=200000):
 st=time.time();ss=[rows(p,cap,4) for p in (0,1)];adj={}
 for p in (0,1):
  ix={}
  for j,B in enumerate(ss[1-p]):
   sig=tuple(B[c]['ins'][0] if(c+p)%2==0 else B[c]['outs'][2] for c in range(4));ix.setdefault(sig,[]).append(j)
  for i,A in enumerate(ss[p]):
   sig=tuple(A[c]['outs'][0] if(c+p)%2==0 else A[c]['ins'][2] for c in range(4));adj[p,i]=ix.get(sig,[])
 print(json.dumps(dict(stage='static',cap=cap,window=k,rows=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 @lru_cache(maxsize=500000)
 def bad(p,seq):return bad_window([[a['h'] for a in ss[(p+z)%2][j]] for z,j in enumerate(seq)])
 voltage=[[sum(r[3]['outs'][1]-r[0]['outs'][3] for _ in range(1)) for r in rr] for rr in ss]
 start=(0,(0,)*(k-1),0);states=[start];ix={start:0};q=deque([0]);parents={0:None};edges=[];reject={};end=None;unknown=False;last=st;attempts=0
 while q:
  u=q.popleft();p,seq,w=states[u];lastp=(p+k-2)%2
  for j in adj[lastp,seq[-1]]:
   attempts+=1;reason=bad(p,seq+(j,))
   if reason:reject[reason]=reject.get(reason,0)+1;continue
   v=(1-p,(seq+(j,))[1:],(w+voltage[1-lastp][j])%2)
   if v not in ix:
    ix[v]=len(states);states.append(v);q.append(ix[v]);parents[ix[v]]=(u,j)
    if len(states)>max_states:unknown=True;break
   edges.append((u,ix[v],j))
   if not any(v[1]) and v[2]==1:end=ix[v];break
  if end or unknown:break
  if time.time()-last>20:print(json.dumps(dict(stage='graph',states=len(states),edges=len(edges),queue=len(q),attempts=attempts,seconds=time.time()-st)),flush=True);last=time.time()
 path=[]
 if end:
  u=end
  while parents[u] is not None:u,j=parents[u];path.append(j)
  path.reverse()
 result=dict(cap=cap,full_drift=[4,0],window=k,states=len(states),edges=len(edges),attempts=attempts,rejected=reject,seconds=time.time()-st,status='ODD_EMPTY_REACHABLE_RELAXATION' if end else('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_AXIS4_WINDOW_CANDIDATE'),witness=path)
 base=Path(__file__).with_name(f'axis4_literal_window_cap{cap}_k{k}')
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
