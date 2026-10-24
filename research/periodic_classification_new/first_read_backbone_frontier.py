#!/usr/bin/env python3
"""Finite first-read CELL-graph monitor; implementation candidate.
The reverse-dependency graph has indegree1, unrestricted outdegree. Every
completed component cycle must be simple full-cylinder winding+1. Mod3
therefore detects exactly its allowed sign among0,+/-1. Rooted-tree depths
store a saturated lower period debt; all additions are nonnegative.
This is NOT the event-orbit connectivity monitor.
"""
def transition(state,old,new,p,geometry,S=120):
 rows=(old,new);active=lambda rr:{c for c,a in enumerate(rr) if a['h']}
 A=active(old);B=active(new);covered={c for root,es in state for c,w,z in es}
 assert covered==A,(covered,A)
 components=[];at={};bound=0
 def put(root,entries):
  obj={'root':root,'es':entries};components.append(obj)
  for v in entries:at[v]=obj
  return obj
 for root,es in state:
  entries={(0,c):(w,z) for c,w,z in es}
  rt=None if root<0 else(0,root)
  if rt is not None:assert entries[rt]==(0,0)
  put(rt,entries)
 for c in B:put((1,c),{(1,c):(0,0)})
 for ar,ac,br,bc,d,k in geometry.splice_arcs(p):
  hs=rows[br][bc]['h']
  if not hs or hs[0]!=d:continue
  u=(ar,ac);v=(br,bc);cu=at[u];cv=at[v]
  if cv['root']!=v:return None,0,'first_incoming_already_exposed'
  hu=rows[ar][ac]['h'];j=next(j for j,h in enumerate(hu) if(h+(1 if j%2==0 else-1))%4==d)
  debt=1+4*j;wu,zu=cu['es'][u];wv,zv=cv['es'][v]
  if cu is cv:
   winding=(wu+k-wv)%3
   if winding!=1:return None,0,'first_cycle_wrong_winding'
   bound=max(bound,min(S,zu+debt));cu['root']=None
   cu['es']={a:(w,0) for a,(w,z) in cu['es'].items()}
  else:
   shift=(wu+k-wv)%3;offset=min(S,zu+debt)
   for a,(w,z) in cv['es'].items():
    cu['es'][a]=((w+shift)%3,0 if cu['root'] is None else min(S,offset+z));at[a]=cu
   components.remove(cv)
 out=[]
 for comp in components:
  entries=sorted((c,w,z) for (r,c),(w,z) in comp['es'].items() if r==1)
  if not entries:
   if comp['root'] is not None:return None,0,'closed_first_tree'
   continue
  if comp['root'] is None:
   base=entries[0][1];entries=[(c,(w-base)%3,0) for c,w,z in entries];root=-1
  else:
   rr,root=comp['root']
   if rr!=1:return None,0,'forgotten_first_root'
  out.append((root,tuple(entries)))
 return tuple(sorted(out,key=lambda a:a[1][0][0])),bound,None
