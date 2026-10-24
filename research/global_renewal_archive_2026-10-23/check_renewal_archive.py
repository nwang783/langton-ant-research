"""Targeted complete-board graph checks on named standard/nonstandard controls.
No word/cap search and no cropping. General theorems have separate proofs.
"""
from pathlib import Path
import json,sys,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'global_cycle_birth_2026-10-23'))
from check_cycle_birth import *
OUT=Path(__file__).parent
sys.setrecursionlimit(200000)

def bridges(B,k):
 g=graph(B,k);tin={};lo={};ans=set();clock=0
 def dfs(v,pe=None):
  nonlocal clock
  tin[v]=lo[v]=clock;clock+=1
  for u,e in g[v]:
   if e==pe:continue
   if u in tin:lo[v]=min(lo[v],tin[u])
   else:
    dfs(u,e);lo[v]=min(lo[v],lo[u])
    if lo[u]>tin[v]:ans.add(e)
 for v in g:
  if v not in tin:dfs(v)
 return ans

def path(B,k,s,t):
 g=graph(B,k);par={s:None};todo=[s]
 for v in todo:
  if v==t:break
  for u,e in g.get(v,()):
   if u not in par:par[u]=(v,e);todo.append(u)
 if t not in par:return None
 es=[]
 while t!=s:t,e=par[t];es.append(e)
 return es[::-1]

def vertices(B,k):return {u for q in B for u in endpoints(q,k)}

def check_run(name,B0,p0,h0,word):
 B=set(B0);p=p0;h=h0;k=wwhich(p,h);counts={x:0 for x in ['w_erasure','z_only_erasure','w_cycle_birth','z_cycle_birth','exposed_bridges','exposed_consumed','old_branch_exits','r0','r1','r2','r4','r4_bridge','r4_nonbridge','external_imports']};maxchain=0
 oldbr=bridges(B,k);phase=None;phaseindex=0;branched=False
 # The arbitrary first run may be a partial compressed block. Later entry is after L.
 entryB=set(B);entryw=cursors(p,h)[1];r=0;arms=[];proper=False
 for t,wanted in enumerate(word):
  assert ('L' if p in B else 'R')==wanted,(name,t,p,h,wanted)
  q=p;z,w=cursors(p,h);assert k==wwhich(p,h)
  pre=set(B);nb0=nb1=False
  if wanted=='L':
   nb0=q not in oldbr;nb1=connected(B-{q},1-k,*endpoints(q,1-k))
   if nb0:counts['w_erasure']+=1
   elif nb1:counts['z_only_erasure']+=1
   if phase is not None and not (nb0 or nb1):
    if q in phase:
     assert not branched and phaseindex<len(phase) and q==phase[phaseindex],(name,t,phaseindex,q,phase)
     phaseindex+=1;counts['exposed_consumed']+=1
    else:
     if not branched:counts['old_branch_exits']+=1
     branched=True
  else:
   r+=1;arms.append(q)
   wb=connected(B,k,*endpoints(q,k));zb=connected(B,1-k,*endpoints(q,1-k))
   counts['w_cycle_birth']+=wb;counts['z_cycle_birth']+=zb
  p,h=step(B,p,h);newbr=bridges(B,k)
  if wanted=='R':
   u,v=endpoints(q,k);pa=path(pre,k,u,v)
   if pa is None:assert newbr==oldbr|{q}
   else:
    lost=oldbr-newbr;assert lost==oldbr.intersection(pa)
    assert newbr==oldbr-lost
  elif not nb0:
   assert newbr==oldbr-{q}
  else:
   arrival=cursors(p,h)[1];depart=next(u for u in endpoints(q,k) if u!=arrival)
   pa=path(B,k,arrival,depart);assert pa is not None
   added=newbr-oldbr;assert added==newbr.intersection(pa)
   assert oldbr<=newbr
   chain=[e for e in pa if e in added];maxchain=max(maxchain,len(chain));counts['exposed_bridges']+=len(chain)
  if wanted=='L':
   if proper:
    assert r in (0,1,2,4);counts['r'+str(r)]+=1
    dep=endpoints(q,k);arr=cursors(p,h)[1]
    C0=component(entryB,k,entryw);actual=component(B,k,arr)
    if r<=2:
     assert q in C0
     if r==2:
      assert sum(entryw in endpoints(e,k) for e in C0)==1
      assert q in bridges(entryB,k)
     if not nb0:assert actual==component(C0-{q},k,arr)
     else:
      # Count full entry components OTHER than original active component imported.
      rem=actual-entryB.intersection(C0)-set(arms)
      seen=set();imports=0
      for e in rem:
       if e in seen:continue
       c=component(entryB,k,endpoints(e,k)[0]);seen|=c;imports+=1
      assert imports<=1
      counts['external_imports']+=imports
    else:
     assert not C0 and all(entryw not in endpoints(e,k) for e in entryB)
     assert q==arms[0] and len(arms)==4
     C1=component(entryB,k,arr)
     # Component identifiers retain isolated endpoint vertices as well.
     def cid(v):return frozenset(component(entryB,k,v)) or ('isolated',v)
     targets=[next(v for v in endpoints(e,k) if v!=entryw) for e in arms[1:]]
     revisit=any(cid(v)==cid(arr) for v in targets)
     assert revisit==nb0
     if not revisit:
      counts['r4_bridge']+=1;assert actual==C1
     else:
      counts['r4_nonbridge']+=1
      expected=set(arms[1:])|C1
      for v in targets:expected|=component(entryB,k,v)
      assert actual==expected
      assert len({cid(v) for v in targets}|{cid(arr)})<=3
   if nb0 or nb1:
    phase=None;phaseindex=0;branched=False
   if nb0:
    phase=chain;phaseindex=0;branched=False
   entryB=set(B);entryw=cursors(p,h)[1];r=0;arms=[];proper=True
  oldbr=newbr
 return {'name':name,'time':len(word),'initial_mass':len(B0),'final_mass':len(B),'max_exposed_chain':maxchain,**counts}

def cycle_rod(r):
 # w lattice k=0, transformed coordinates (a,b).
 def xy(a,b):return (2*a+2*b+1,2*a-2*b+1)
 verts=[]
 def seg(a,b,c,d):
  while (a,b)!=(c,d):
   verts.append(xy(a,b));a+=(c>a)-(c<a);b+=(d>b)-(d<b)
  return a,b
 at=(r-1,r)
 for dest in [(r-1,r+2),(-3,r+2),(-3,0),(-1,0)]:at=seg(*at,*dest)
 verts.append(xy(*at));ret={((u[0]+v[0])//4,(u[1]+v[1])//4) for u,v in zip(verts,verts[1:])}
 assert all(y<=-1 for x,y in ret)
 B={(x,0) for x in range(2*r)}|ret;assert len(B)==4*r+8
 assert rank(B,0)==1 and rank(B,1)==0
 return B

def actual_producer_wave(which):
 U=ROOT/'causal_reduction/unit_scale';sys.path.insert(0,str(U))
 if which==1564:
  import check1564_noncrossing_producer as mod
  p,B,segments,_=mod.setup(100,1);h=3
 else:
  import check4352_noncrossing_producer as mod
  p,B,segments,_=mod.setup(252,1);h=3
 for s in segments:
  assert [p,h]==s['start']
  if s['kind']=='wave':return B,p,h,mod.W
  word=mod.H*s['count'] if s['kind']=='H' else s['word']
  for c in word:
   assert ('L'if p in B else'R')==c
   p,h=step(B,p,h)
 raise AssertionError('no wave')

if __name__=='__main__':
 results=[]
 S=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
 results.append(check_run('standard104_seed13_three_periods',{tuple(q)for q in S['seed']},(0,0),S['heading'],S['word']*3))
 for r in [1,2,3,10,30,100]:
  res=check_run('one_erasure_LRRL_rod_'+str(r),cycle_rod(r),(0,0),1,'LRRL'*r)
  assert res['w_erasure']==1 and res['z_only_erasure']==0
  assert res['max_exposed_chain']==4*r+7 and res['exposed_consumed']==2*r-1
  results.append(res)
 for which in [1564,4352]:
  B,p,h,w=actual_producer_wave(which)
  results.append(check_run('finite_full_field_wave_'+str(which),B,p,h,w))
 out={'scope':__doc__,'status':'all targeted complete-board insertion/deletion/path-prefix/star-splice controls PASS','results':results}
 (OUT/'renewal_archive_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
