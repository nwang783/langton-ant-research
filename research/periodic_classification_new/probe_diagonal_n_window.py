#!/usr/bin/env python3
"""Finite-window necessary row transfer for full drift(n,n).
No width cutoff. Finite graph obstructions require independent audit.
"""
from itertools import product
from collections import deque
from pathlib import Path
import json,sys,time

def histories(p,cap):
 a=1-p;out=[]
 for h in [()]+[h for m in range(1,cap+1) for h in product((a,a+2),repeat=m)]:
  ins=[h.count(d) for d in range(4)];outs=[sum((x+(1 if j%2==0 else -1))%4==d for j,x in enumerate(h)) for d in range(4)]
  balance=h[::2].count(1)-h[::2].count(3) if not p else h[1::2].count(0)-h[1::2].count(2)
  out.append(dict(h=h,ins=ins,outs=outs,balance=balance))
 return out

def rows(p,cap,n):
 hs=histories(p,cap);out=[]
 for ids in product(range(len(hs)),repeat=n):
  cs=[hs[i] for i in ids]
  if sum(c['balance'] for c in cs):continue
  out.append(dict(cells=cs,voltage=cs[-1]['outs'][1]-cs[0]['outs'][3] if p else 0))
 return out

def bad_window(seq,p,ss,n):
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
 for start in ev:
  v=start;w=0;seen={v}
  while v in succ:
   v,k=succ[v];w+=k
   if v in seen:
    cyc=[];u=v;cw=0
    while True:
     cyc.append(u);u,k=succ[u];cw+=k
     if u==v:break
    if len(cyc)==len(ev) and cw==1:
     ok=True
     for e in cyc:
      u=e;ww=0
      while True:
       u,k=succ[u];ww+=k
       if u==e:break
       if u[:2]==e[:2] and ((u[2]>e[2] and ww>0) or (u[2]<e[2] and ww<=0)):ok=False
     if ok:raise RuntimeError(('POTENTIAL_COMPLETE_FRONT',p,seq,hs))
    return 'closed_cycle'
   seen.add(v)
   if v[:2]==start[:2] and ((v[2]>start[2] and w>0) or (v[2]<start[2] and w<=0)):return 'wrong_order_segment'
 return None

def run(cap,n,k,max_states=1000000):
 assert k>=2;st=time.time();ss=[rows(p,cap,n) for p in (0,1)];adj={}
 for p in (0,1):
  index={}
  for j,b in enumerate(ss[1-p]):
   B=b['cells']
   sig=tuple((B[c]['ins'][0],B[c]['outs'][1]) for c in range(n)) if p==0 else tuple((B[(c-1)%n]['ins'][3],B[c]['outs'][2]) for c in range(n))
   index.setdefault(sig,[]).append(j)
  for i,a in enumerate(ss[p]):
   A=a['cells']
   sig=tuple((A[c]['outs'][0],A[(c+1)%n]['ins'][1]) for c in range(n)) if p==0 else tuple((A[c]['outs'][3],A[c]['ins'][2]) for c in range(n))
   adj[p,i]=index.get(sig,[])
 print(json.dumps(dict(stage='static_graph',cap=cap,n=n,k=k,row_states=list(map(len,ss)),edges=sum(map(len,adj.values())),seconds=time.time()-st)),flush=True)
 start=(0,(0,)*(k-1),0);q=deque([start]);seen={start};parents={start:None};badcounts={};edges=0;end=None;accepted=[]
 while q:
  p,seq,w=q.popleft();lastpar=(p+k-2)%2;newpar=1-lastpar
  for j in adj[lastpar,seq[-1]]:
   window=seq+(j,);bad=bad_window(window,p,ss,n)
   if bad:badcounts[bad]=badcounts.get(bad,0)+1;continue
   edges+=1;v=(1-p,window[1:],(w+ss[newpar][j]['voltage'])%2);accepted.append(((p,seq,w),v))
   if v not in seen:
    parents[v]=(p,seq,w);seen.add(v);q.append(v)
    if len(seen)>max_states:break
    if not any(v[1]) and v[2]==1:end=v;break
  if end or len(seen)>max_states:break
 rev={u:[] for u in seen}
 for a,b in accepted:rev[b].append(a)
 core={u for u in seen if not any(u[1])};rq=deque(core)
 while rq:
  for u in rev[rq.popleft()]:
   if u not in core:core.add(u);rq.append(u)
 returning_active=[u for u in core if any(u[1])]
 path=[];v=end
 while v is not None:path.append(v);v=parents[v]
 path.reverse()
 result=dict(cap=cap,n=n,window=k,row_states=list(map(len,ss)),static_edges=sum(map(len,adj.values())),reachable_lifted_states=len(seen),accepted_edges=edges,bad_window_counts=badcounts,status='ODD_EMPTY_REACHABLE_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if len(seen)>max_states else 'ALL_WIDTH_EVEN_VOLTAGE_WINDOW_CERTIFICATE'),seconds=time.time()-st,returning_states=len(core),returning_active_states=len(returning_active),witness=path)
 if not end and len(seen)<=max_states and not returning_active:result['status']='ALL_WIDTH_NO_NONEMPTY_RETURN_WINDOW_CERTIFICATE'
 if not end and len(seen)<=max_states:
  cert=dict(parameters=dict(cap=cap,n=n,window=k),histories=ss,states=sorted(seen),accepted=accepted,returning_states=sorted(core))
  Path(__file__).with_name(f'diagonal_n{n}_cap{cap}_window{k}.certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
 Path(__file__).with_name(f'diagonal_n{n}_cap{cap}_window{k}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({a:b for a,b in result.items() if a!='witness'}),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
