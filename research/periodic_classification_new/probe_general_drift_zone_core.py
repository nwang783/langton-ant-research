#!/usr/bin/env python3
"""Arbitrary full-drift frontier-zone core. Exploratory producer.
Uses exact row geometry, supports controls and future all-width searches.
"""
from itertools import permutations
from probe_diagonal_zone_frontier import INF,close,rotations_ok

def splice(paths,old,new,p,mod,geometry):
 n=len(old);assert len(new)==n
 nodes={(0,e) for a,b,w in paths for e in (a,b)}|{(1,(c,j)) for c,h in enumerate(new) for j in range(len(h))}
 succ={};pred={};physical=[];old_starts={(0,a):i for i,(a,b,w) in enumerate(paths)}
 def arc(a,b,w,real):
  assert a in nodes and b in nodes and a not in succ and b not in pred,(a,b,paths,old,new)
  succ[a]=(b,w%mod);pred[b]=a
  if real:physical.append((a,b,w))
 for a,b,w in paths:
  if a!=b:arc((0,a),(0,b),w,False)
  else:assert w==0
 hs=[old,new]
 for a,ac,b,bc,d,w in geometry.splice_arcs(p):
  out=[j for j,h in enumerate(hs[a][ac]) if (h+(1 if j%2==0 else -1))%4==d]
  ins=[j for j,h in enumerate(hs[b][bc]) if h==d]
  assert len(out)==len(ins),(p,a,ac,b,bc,d,w,old,new)
  for i,j in zip(out,ins):arc((a,(ac,i)),(b,(bc,j)),w,True)
 seen=set();pieces=[];cycles=[]
 for s in sorted(nodes):
  if s in pred:continue
  u=s;w=0;walk=[u];seen.add(u)
  while u in succ:
   u,k=succ[u];w=(w+k)%mod;assert u not in seen;seen.add(u);walk.append(u)
  assert s[0]==1 and u[0]==1
  pieces.append(dict(walk=walk,voltage=w,old=[old_starts[a] for a in walk if a in old_starts]))
 for s in sorted(nodes-seen):
  if s in seen:continue
  u=s;w=0;walk=[]
  while u not in seen:walk.append(u);seen.add(u);u,k=succ[u];w=(w+k)%mod
  assert u==s
  cycles.append(dict(walk=walk,voltage=w,old=[old_starts[a] for a in walk if a in old_starts]))
 if cycles:
  if len(cycles)!=1 or pieces or cycles[0]['voltage']!=1%mod:return None
  c=cycles[0];newnodes=[a for a in c['walk'] if a[0]==1];assert newnodes
  pivot=c['walk'].index(min(newnodes));c['walk']=c['walk'][pivot:]+c['walk'][:pivot]
  c['old']=[old_starts[a] for a in c['walk'] if a in old_starts]
  return nodes,physical,[c],True
 return nodes,physical,pieces,False

def transitions(paths,flat,old,new,p,geometry,mod=2,M=2,phase_times=None,P=None):
 sp=splice(paths,old,new,p,mod,geometry)
 if sp is None:return [],'sealed_cycle'
 nodes,physical,pieces,terminal=sp
 if not pieces:return [((),())],None
 if terminal:orders=[tuple(pieces)]
 else:
  pieces.sort(key=lambda c:c['walk'][0])
  if phase_times is not None:
   anchor=phase_times[pieces[0]['walk'][0][1]]
   orders=[tuple(sorted(pieces,key=lambda c:(phase_times[c['walk'][0][1]]-anchor)%P))]
  else:orders=((pieces[0],)+tail for tail in permutations(pieces[1:]))
 oldvars=sorted({j for a,b,w in paths for j in (a,b)});nv=len(oldvars);assert len(flat)==nv*nv
 oldowner={j:i for i,(a,b,w) in enumerate(paths) for j in (a,b)}
 ns=sorted(nodes);index={a:i for i,a in enumerate(ns)};output=[];reasons=set()
 for ordered in orders:
  oldseq=[i for c in ordered for i in c['old']];cut=rotations_ok(oldseq,len(paths))
  if cut is None:reasons.add('cyclic_order');continue
  phase=[a for c in ordered for a in c['walk']];rank={a:i for i,a in enumerate(phase)};assert len(rank)==len(phase)==len(nodes)
  D=[[0 if i==j else INF for j in range(len(ns))] for i in range(len(ns))]
  for i,a in enumerate(oldvars):
   da=-int(oldowner[a]<cut)
   for j,b in enumerate(oldvars):
    bound=flat[i*nv+j]
    if bound<INF:D[index[0,a]][index[0,b]]=bound+da+int(oldowner[b]<cut)
  for a,b,w in physical:
   v=-w+int(rank[b]<rank[a]);ia=index[a];ib=index[b]
   D[ib][ia]=min(D[ib][ia],v);D[ia][ib]=min(D[ia][ib],-v)
  for c,h in enumerate(new):
   for j in range(len(h)-1):
    a=(1,(c,j));b=(1,(c,j+1));ia=index[a];ib=index[b]
    D[ia][ib]=min(D[ia][ib],-int(rank[b]<rank[a]))
  if not close(D):reasons.add('clock_zone');continue
  if terminal:return ['POTENTIAL_COMPLETE_FRONT'],None
  nxt=tuple((c['walk'][0][1],c['walk'][-1][1],c['voltage']) for c in ordered)
  newvars=sorted({j for a,b,w in nxt for j in (a,b)})
  def abstract(x):return INF if x>M else max(x,-M)
  mat=tuple(abstract(D[index[1,a]][index[1,b]]) for a in newvars for b in newvars)
  output.append((nxt,mat))
 return output,','.join(sorted(reasons)) or None
