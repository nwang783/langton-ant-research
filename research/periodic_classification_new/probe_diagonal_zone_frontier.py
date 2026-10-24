#!/usr/bin/env python3
"""Finite sound frontier relaxation: connectivity, cyclic block order, integer DBM.
This is exploratory until independently audited. No bounded-width inference.
A surviving terminal zone is a relaxation, not a verified ant front.
"""
from pathlib import Path
from collections import deque
from itertools import permutations
import json,sys,time
from probe_diagonal_window_transfer import histories,bad_window
INF=10**6

def splice(paths,old,new,p,mod):
 nodes={(0,j) for a,b,w in paths for j in (a,b)}|{(1,j) for j in range(len(new))}
 succ={};pred={};physical=[];old_starts={(0,a):i for i,(a,b,w) in enumerate(paths)}
 def arc(a,b,w,real):
  assert a in nodes and b in nodes and a not in succ and b not in pred,(a,b,paths,old,new)
  succ[a]=(b,w%mod);pred[b]=a
  if real:physical.append((a,b,w))
 for a,b,w in paths:
  if a!=b:arc((0,a),(0,b),w,False)
  else:assert w==0
 for a,b,d,w in ([(0,1,0,0),(1,0,1,1)] if p==0 else [(0,1,3,-1),(1,0,2,0)]):
  hs=[old,new]
  out=[j for j,h in enumerate(hs[a]) if (h+(1 if j%2==0 else -1))%4==d]
  ins=[j for j,h in enumerate(hs[b]) if h==d]
  assert len(out)==len(ins)
  for i,j in zip(out,ins):arc((a,i),(b,j),w,True)
 seen=set();pieces=[];cycles=[]
 for s in sorted(nodes):
  if s in pred:continue
  u=s;w=0;walk=[u];seen.add(u)
  while u in succ:
   u,k=succ[u];w=(w+k)%mod;assert u not in seen;seen.add(u);walk.append(u)
  assert s[0]==1 and u[0]==1,('forgotten_open_endpoint',s,u,old,new,paths)
  pieces.append(dict(walk=walk,voltage=w,old=[old_starts[a] for a in walk if a in old_starts]))
 for s in sorted(nodes-seen):
  if s in seen:continue
  u=s;w=0;walk=[]
  while u not in seen:
   walk.append(u);seen.add(u);u,k=succ[u];w=(w+k)%mod
  assert u==s
  cycles.append(dict(walk=walk,voltage=w,old=[old_starts[a] for a in walk if a in old_starts]))
 if cycles:
  if len(cycles)!=1 or pieces or cycles[0]['voltage']!=1%mod:return None
  c=cycles[0];newnodes=[a for a in c['walk'] if a[0]==1];assert newnodes
  pivot=c['walk'].index(min(newnodes));c['walk']=c['walk'][pivot:]+c['walk'][:pivot]
  c['old']=[old_starts[a] for a in c['walk'] if a in old_starts]
  return (nodes,physical,[c],True)
 return (nodes,physical,pieces,False)

def rotations_ok(seq,n):
 if not n:return 0 if not seq else None
 if len(seq)!=n:return None
 off=seq[0]
 return off if seq==list(range(off,n))+list(range(off)) else None

def close(D):
 n=len(D)
 for k in range(n):
  dk=D[k]
  for i in range(n):
   di=D[i];v=di[k]
   if v>=INF:continue
   for j in range(n):
    if dk[j]<INF and v+dk[j]<di[j]:di[j]=v+dk[j]
   if di[i]<0:return False
 return all(D[i][i]>=0 for i in range(n))

def transitions(paths,flat,old,new,p,mod,M):
 sp=splice(paths,old,new,p,mod)
 if sp is None:return [],'sealed_cycle'
 nodes,physical,pieces,terminal=sp
 if not pieces:return [((),())],None
 if terminal:orders=[tuple(pieces)]
 else:
  # Canonical cyclic anchor: smallest new frontier path-start event.
  pieces.sort(key=lambda c:c['walk'][0]);orders=((pieces[0],)+tail for tail in permutations(pieces[1:]))
 oldvars=sorted({j for a,b,w in paths for j in (a,b)});nv=len(oldvars)
 assert len(flat)==nv*nv
 oldowner={j:i for i,(a,b,w) in enumerate(paths) for j in (a,b)}
 ns=sorted(nodes);index={a:i for i,a in enumerate(ns)};output=[];reasons=set()
 for ordered in orders:
  oldseq=[i for c in ordered for i in c['old']];cut=rotations_ok(oldseq,len(paths))
  if cut is None:reasons.add('cyclic_order');continue
  phase=[a for c in ordered for a in c['walk']];rank={a:i for i,a in enumerate(phase)}
  assert len(rank)==len(phase)==len(nodes)
  D=[[0 if i==j else INF for j in range(len(ns))] for i in range(len(ns))]
  for i,a in enumerate(oldvars):
   da=-int(oldowner[a]<cut)
   for j,b in enumerate(oldvars):
    bound=flat[i*nv+j]
    if bound<INF:D[index[0,a]][index[0,b]]=bound+da+int(oldowner[b]<cut)
  for a,b,w in physical:
   # A physical successor crosses the selected phase cut iff its rank drops.
   v=-w+int(rank[b]<rank[a]);ia=index[a];ib=index[b]
   D[ib][ia]=min(D[ib][ia],v);D[ia][ib]=min(D[ia][ib],-v)
  for j in range(len(new)-1):
   a=(1,j);b=(1,j+1);ia=index[a];ib=index[b]
   D[ia][ib]=min(D[ia][ib],-int(rank[b]<rank[a]))
  if not close(D):reasons.add('clock_zone');continue
  if terminal:return ['POTENTIAL_COMPLETE_FRONT'],None
  nxt=tuple((c['walk'][0][1],c['walk'][-1][1],c['voltage']) for c in ordered)
  newvars=sorted({j for a,b,w in nxt for j in (a,b)})
  def abstract(x):return INF if x>M else max(x,-M)
  mat=tuple(abstract(D[index[1,a]][index[1,b]]) for a in newvars for b in newvars)
  output.append((nxt,mat))
 return output,','.join(sorted(reasons)) or None

def run(cap,k=3,M=2,mod=2,max_states=500000):
 st=time.time();ss=[histories(p,cap) for p in (0,1)];adj={}
 for p in (0,1):
  ix={}
  for j,b in enumerate(ss[1-p]):
   sig=(b['ins'][0],b['outs'][1]) if p==0 else (b['ins'][3],b['outs'][2]);ix.setdefault(sig,[]).append(j)
  for i,a in enumerate(ss[p]):
   sig=(a['outs'][0],a['ins'][1]) if p==0 else (a['outs'][3],a['ins'][2]);adj[p,i]=ix.get(sig,[])
 start=(0,(0,)*(k-1),(),());states=[start];ix={start:0};q=deque([0]);parents={0:None};edges=[];reject={};badcache={};zcache={};end=None;unknown=False;lastreport=st
 while q:
  u=q.popleft();p,seq,paths,flat=states[u];lastpar=(p+k-2)%2
  for j in adj[lastpar,seq[-1]]:
   key=(p,seq,j)
   if key not in badcache:badcache[key]=bad_window(seq+(j,),p,ss)
   bad=badcache[key]
   if bad:reason='window_'+bad['kind'];reject[reason]=reject.get(reason,0)+1;continue
   key2=(lastpar,seq[-1],j,paths,flat)
   if key2 not in zcache:zcache[key2]=transitions(paths,flat,ss[lastpar][seq[-1]]['h'],ss[1-lastpar][j]['h'],lastpar,mod,M)
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
  if time.time()-lastreport>15:
   print(json.dumps(dict(stage='graph',states=len(states),queue=len(q),edges=len(edges),seconds=time.time()-st)),flush=True);lastreport=time.time()
 path=[]
 if end:
  u,j=end;path=[j]
  while parents[u] is not None:u,j=parents[u];path.append(j)
  path.reverse()
 result=dict(cap=cap,window=k,bound=M,modulus=mod,states=len(states),edges=len(edges),rejected=reject,cache_sizes=[len(badcache),len(zcache)],seconds=time.time()-st,status='POTENTIAL_COMPLETE_FRONT_RELAXATION' if end else ('UNKNOWN_STATE_LIMIT' if unknown else 'ALL_WIDTH_ZONE_EXCLUSION_CERTIFICATE'),witness=path)
 base=Path(__file__).with_name(f'diagonal_zone_cap{cap}_window{k}_bound{M}_mod{mod}')
 if not end and not unknown:base.with_suffix('.certificate.json').write_text(json.dumps(dict(parameters=dict(cap=cap,window=k,bound=M,modulus=mod),histories=ss,states=states,edges=edges))+'\n')
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
