#!/usr/bin/env python3
"""All-width finite necessary automaton: row windows + exact path connectivity.
Path voltages retained modulo m, default2. A sole closed cycle is explicitly
retained as a potential complete-front outcome when voltage is1 modulo m.
No such outcome is an actual front without independent integer/clock replay.
"""
from pathlib import Path
from collections import deque
import json,sys,time
from probe_diagonal_window_transfer import histories,bad_window

def extend(paths,old,new,p,mod):
 # Old path endpoints and all new events. A compressed edge preserves voltage.
 nodes={(0,j) for a,b,w in paths for j in (a,b)}|{(1,j) for j in range(len(new))}
 succ={};pred={}
 def arc(a,b,w):
  assert a in nodes and b in nodes and a not in succ and b not in pred,(a,b,paths,old,new)
  succ[a]=(b,w%mod);pred[b]=a
 for a,b,w in paths:
  if a!=b:arc((0,a),(0,b),w)
  else:assert w==0
 for a,b,d,w in ([(0,1,0,0),(1,0,1,1)] if p==0 else [(0,1,3,-1),(1,0,2,0)]):
  hs=[old,new]
  out=[j for j,h in enumerate(hs[a]) if (h+(1 if j%2==0 else -1))%4==d]
  ins=[j for j,h in enumerate(hs[b]) if h==d]
  assert len(out)==len(ins)
  for i,j in zip(out,ins):arc((a,i),(b,j),w)
 seen=set();outpaths=[]
 for s in nodes:
  if s in pred:continue
  u=s;w=0;seen.add(u)
  while u in succ:
   u,k=succ[u];w=(w+k)%mod;assert u not in seen;seen.add(u)
  assert s[0]==1 and u[0]==1,('forgotten_open_endpoint',s,u,old,new,paths)
  outpaths.append((s[1],u[1],w))
 cycles=[]
 for s in nodes-seen:
  if s in seen:continue
  u=s;w=0
  while u not in seen:
   seen.add(u);u,k=succ[u];w=(w+k)%mod
  assert u==s;cycles.append(w)
 if cycles:
  if len(cycles)==1 and not outpaths and cycles[0]==1%mod:return 'POTENTIAL_COMPLETE_FRONT'
  return 'sealed_cycle'
 return tuple(sorted(outpaths))

def run(cap,k=3,mod=2,max_states=500000):
 st=time.time();ss=[histories(p,cap) for p in (0,1)];adj={}
 for p in (0,1):
  idx={}
  for j,b in enumerate(ss[1-p]):
   sig=(b['ins'][0],b['outs'][1]) if p==0 else (b['ins'][3],b['outs'][2]);idx.setdefault(sig,[]).append(j)
  for i,a in enumerate(ss[p]):
   sig=(a['outs'][0],a['ins'][1]) if p==0 else (a['outs'][3],a['ins'][2]);adj[p,i]=idx.get(sig,[])
 # First-row parity of remembered k-1 rows, row-state ids, compressed paths.
 start=(0,(0,)*(k-1),());states=[start];index={start:0};parent={0:None};q=deque([0]);edges=[];reject={};end=None;unknown=False;badcache={};splicecache={}
 while q:
  u=q.popleft();p,seq,paths=states[u];lastpar=(p+k-2)%2
  for j in adj[lastpar,seq[-1]]:
   key=(p,seq,j)
   if key not in badcache:badcache[key]=bad_window(seq+(j,),p,ss)
   bad=badcache[key]
   if bad:reject['window_'+bad['kind']]=reject.get('window_'+bad['kind'],0)+1;continue
   key2=(lastpar,seq[-1],j,paths)
   if key2 not in splicecache:splicecache[key2]=extend(paths,ss[lastpar][seq[-1]]['h'],ss[1-lastpar][j]['h'],lastpar,mod)
   nxt=splicecache[key2]
   if nxt=='sealed_cycle':reject[nxt]=reject.get(nxt,0)+1;continue
   if nxt=='POTENTIAL_COMPLETE_FRONT':end=(u,j);break
   v=(1-p,(seq+(j,))[1:],nxt)
   if v not in index:
    index[v]=len(states);states.append(v);q.append(index[v]);parent[index[v]]=(u,j)
    if len(states)>max_states:unknown=True;break
   edges.append((u,index[v],j))
  if end or unknown:break
 path=[]
 if end:
  u,j=end;path=[j]
  while parent[u] is not None:u,j=parent[u];path.append(j)
  path.reverse()
 result=dict(cap=cap,window=k,modulus=mod,states=len(states),edges=len(edges),rejected=reject,cache_sizes=[len(badcache),len(splicecache)],seconds=time.time()-st,status='POTENTIAL_COMPLETE_FRONT_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_CONNECTIVITY_EXCLUSION_CERTIFICATE'),witness=path)
 base=Path(__file__).with_name(f'diagonal_connectivity_cap{cap}_window{k}_mod{mod}')
 if not end and not unknown:
  base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,window=k,modulus=mod),histories=ss,states=states,edges=edges))+'\n')
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
