#!/usr/bin/env python3
"""All-width finite-window necessary transfer graph, no period cutoff.
A parity obstruction is rigorous only after independent construction audit.
Reachability without such obstruction is only a local-window relaxation.
"""
from itertools import product
from collections import deque
from pathlib import Path
import json,sys,time

def histories(p,cap):
 a=1-p;out=[]
 for h in [()]+[h for m in range(1,cap+1) for h in product((a,a+2),repeat=m)]:
  R=h[::2];L=h[1::2]
  if (R.count(1)!=R.count(3) if p==0 else L.count(0)!=L.count(2)):continue
  ins=[h.count(d) for d in range(4)];outs=[sum((x+(1 if j%2==0 else -1))%4==d for j,x in enumerate(h)) for d in range(4)]
  out.append(dict(h=h,ins=ins,outs=outs,voltage=outs[1]-outs[3] if p else 0))
 return out

def bad_window(seq,p,ss):
 hs=[ss[(p+i)%2][s]['h'] for i,s in enumerate(seq)];ev=[(i,j) for i,h in enumerate(hs) for j in range(len(h))];succ={}
 for i in range(len(seq)-1):
  par=(p+i)%2
  for a,b,d,k in ([(i,i+1,0,0),(i+1,i,1,1)] if par==0 else [(i,i+1,3,-1),(i+1,i,2,0)]):
   os=[j for j,h in enumerate(hs[a]) if (h+(1 if j%2==0 else -1))%4==d];ins=[j for j,h in enumerate(hs[b]) if h==d]
   assert len(os)==len(ins)
   for j,l in zip(os,ins):succ[a,j]=((b,l),k)
 for start in ev:
  v=start;w=0;seen={v}
  while v in succ:
   v,k=succ[v];w+=k
   if v in seen:
    # A cycle is a sealed successor component. The separately verified
    # finite formulas find no small complete front, but retain a special
    # status rather than silently rejecting a potential all-event cycle.
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
       if u[0]==e[0] and ((u[1]>e[1] and ww>0) or (u[1]<e[1] and ww<=0)):ok=False
     if ok:raise RuntimeError(('POTENTIAL_COMPLETE_FRONT',p,seq,hs))
    return dict(kind='closed_cycle',cycle=cyc,voltage=cw,active_events=len(ev),all_window_events=len(cyc)==len(ev))
   seen.add(v)
   if v[0]==start[0] and ((v[1]>start[1] and w>0) or (v[1]<start[1] and w<=0)):
    return dict(kind='wrong_order_segment',start=start,end=v,voltage=w)
 return None

def run(cap,k,max_states=1000000):
 assert k>=2;ss=[histories(p,cap) for p in (0,1)];adj={}
 for p in (0,1):
  for i,a in enumerate(ss[p]):
   adj[p,i]=[]
   for j,b in enumerate(ss[1-p]):
    ok=(a['outs'][0]==b['ins'][0] and a['ins'][1]==b['outs'][1]) if p==0 else (a['outs'][3]==b['ins'][3] and a['ins'][2]==b['outs'][2])
    if ok:adj[p,i].append(j)
 # Node: parity of first row, last k-1 states, voltage parity so far.
 # Padding begins with k-1 empty rows whose first parity is zero.
 start=(0,(0,)*(k-1),0);q=deque([start]);seen={start};parents={start:None};badcounts={};edges=0;end=None;st=time.time();accepted=[];rejected=[]
 while q:
  p,seq,w=q.popleft();lastpar=(p+k-2)%2;newpar=1-lastpar
  for j in adj[lastpar,seq[-1]]:
   window=seq+(j,);bad=bad_window(window,p,ss)
   if bad:
    badcounts[bad['kind']]=badcounts.get(bad['kind'],0)+1
    if cap<=7:rejected.append(dict(source=[p,seq,w],added=j,proof=bad))
    continue
   edges+=1;v=(1-p,window[1:],(w+ss[newpar][j]['voltage'])%2)
   accepted.append(([p,seq,w],[v[0],v[1],v[2]]))
   if v not in seen:
    parents[v]=(p,seq,w);seen.add(v);q.append(v)
    if len(seen)>max_states:break
    if not any(v[1]) and v[2]==1:end=v;break
  if end or len(seen)>max_states:break
 rev={u:[] for u in seen}
 for a,b in accepted:
  a=(a[0],tuple(a[1]),a[2]);b=(b[0],tuple(b[1]),b[2]);rev[b].append(a)
 core={u for u in seen if not any(u[1])};rq=deque(core)
 while rq:
  for u in rev[rq.popleft()]:
   if u not in core:core.add(u);rq.append(u)
 returning_active=[u for u in core if any(u[1])]
 path=[];v=end
 while v is not None:path.append(v);v=parents[v]
 path.reverse()
 result=dict(cap=cap,window=k,local_states=list(map(len,ss)),static_edges=sum(map(len,adj.values())),reachable_lifted_states=len(seen),accepted_edges=edges,bad_window_counts=badcounts,status='ODD_EMPTY_REACHABLE_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if len(seen)>max_states else 'ALL_WIDTH_EVEN_VOLTAGE_WINDOW_CERTIFICATE'),seconds=time.time()-st,returning_states=len(core),returning_active_states=len(returning_active),witness=path)
 if not end and len(seen)<=max_states and not returning_active:result['status']='ALL_WIDTH_NO_NONEMPTY_RETURN_WINDOW_CERTIFICATE'
 if not end and len(seen)<=max_states:
  cert=dict(parameters=dict(cap=cap,window=k),histories=ss,states=sorted(seen),accepted=accepted,rejected=rejected,returning_states=sorted(core))
  Path(__file__).with_name(f'diagonal_cap{cap}_window{k}.certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
 Path(__file__).with_name(f'diagonal_cap{cap}_window{k}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({a:b for a,b in result.items() if a!='witness'}),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
