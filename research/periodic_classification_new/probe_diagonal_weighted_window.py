#!/usr/bin/env python3
"""Exact finite-window shortest-voltage necessary automaton.
Rejects separated active row blocks, which cannot belong to one event cycle.
No width bound; a state limit gives UNKNOWN, never a theorem.
"""
from pathlib import Path
from collections import deque
import json,sys,time
from probe_diagonal_window_transfer import histories,bad_window

def run(cap,k,max_states=200000):
 st=time.time();ss=[histories(p,cap) for p in (0,1)];adj={}
 for p in (0,1):
  idx={}
  for j,b in enumerate(ss[1-p]):
   sig=(b['ins'][0],b['outs'][1]) if p==0 else (b['ins'][3],b['outs'][2]);idx.setdefault(sig,[]).append(j)
  for i,a in enumerate(ss[p]):
   sig=(a['outs'][0],a['ins'][1]) if p==0 else (a['outs'][3],a['ins'][2]);adj[p,i]=idx.get(sig,[])
 start=(0,(0,)*(k-1),0);states=[start];index={start:0};q=deque([0]);edges=[];badcounts={};goals=[];unknown=False
 while q:
  u=q.popleft();p,seq,phase=states[u]
  if phase==2 and not any(seq):goals.append(u);continue
  lastpar=(p+k-2)%2;newpar=1-lastpar
  for j in adj[lastpar,seq[-1]]:
   if phase==2 and j:continue
   window=seq+(j,);bad=bad_window(window,p,ss)
   if bad:badcounts[bad['kind']]=badcounts.get(bad['kind'],0)+1;continue
   ph=1 if j else (2 if phase else 0);v=(1-p,window[1:],ph)
   if v not in index:
    index[v]=len(states);states.append(v);q.append(index[v])
    if len(states)>max_states:unknown=True;break
   edges.append((u,index[v],ss[newpar][j]['voltage']))
  if unknown:break
  if len(states)//10000>(len(states)-1)//10000:print(json.dumps(dict(stage='graph',states=len(states),edges=len(edges),seconds=time.time()-st)),flush=True)
 result=dict(cap=cap,window=k,states=len(states),edges=len(edges),goals=len(goals),bad_window_counts=badcounts,seconds=time.time()-st,status='UNKNOWN_STATE_LIMIT' if unknown else 'GRAPH_COMPLETE')
 if not unknown:
  rev=[[] for _ in states]
  for u,v,w in edges:rev[v].append(u)
  core=set(goals);q=deque(core)
  while q:
   for u in rev[q.popleft()]:
    if u not in core:core.add(u);q.append(u)
  result['returning_states']=len(core)
  if 0 not in core:result['status']='ALL_WIDTH_NO_NONEMPTY_RETURN_WEIGHTED_CERTIFICATE'
  else:
   adj2=[[] for _ in states]
   for u,v,w in edges:
    if u in core and v in core:adj2[u].append((v,w))
   dist={0:0};pred={};q=deque([0]);inq={0};relaxations=0;negative=None
   while q:
    u=q.popleft();inq.remove(u)
    for v,w in adj2[u]:
     d=dist[u]+w
     if v not in dist or d<dist[v]:
      dist[v]=d;pred[v]=(u,w);relaxations+=1
      if v not in inq:q.append(v);inq.add(v)
      if relaxations%max(1,len(core))==0:
       x=v;seen={};trail=[]
       while x in pred and x not in seen:
        seen[x]=len(trail);trail.append(x);x=pred[x][0]
       if x in seen:
        cyc=trail[seen[x]:];wt=sum(pred[a][1] for a in cyc)
        if wt<0:negative=dict(nodes=cyc,weight=wt);break
    if negative:break
   result['relaxations']=relaxations
   if negative:result.update(status='NEGATIVE_CYCLE_RELAXATION',negative_cycle=negative)
   else:
    assert all(v in dist and dist[v]<=dist[u]+w for u in core for v,w in adj2[u])
    minimum=min(dist[g] for g in goals if g in dist);result.update(status='ALL_WIDTH_MINIMUM_VOLTAGE_CERTIFICATE' if minimum>1 else 'VOLTAGE_ONE_NOT_EXCLUDED',minimum_voltage=minimum)
    if minimum>1:
     cert=dict(cap=cap,window=k,histories=ss,states=states,edges=edges,goals=goals,returning=sorted(core),potential=sorted(dist.items()))
     Path(__file__).with_name(f'diagonal_weighted_cap{cap}_window{k}.certificate.json').write_text(json.dumps(cert)+'\n')
 result['seconds']=time.time()-st;Path(__file__).with_name(f'diagonal_weighted_cap{cap}_window{k}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
