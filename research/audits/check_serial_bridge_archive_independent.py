from pathlib import Path
from collections import Counter
import json,hashlib,sys
SELF=Path(__file__).resolve();R=SELF.parents[1];s=(SELF.parent/'check_cycle_birth_finite_fuel_independent.py').read_text();exec(s.split('cells=')[0]);SELF=Path(__file__).resolve();D=R/'global_renewal_archive_2026-10-23';stats=Counter();sys.setrecursionlimit(10000)
def bridge_set(B,k):
 g=graph(B,k);clock=0;tin={};low={};out=set()
 def dfs(v,parentedge=None):
  nonlocal clock
  tin[v]=low[v]=clock;clock+=1
  for u,e in g.get(v,()):
   if e==parentedge:continue
   if u in tin:low[v]=min(low[v],tin[u])
   else:
    dfs(u,e);low[v]=min(low[v],low[u])
    if low[u]>tin[v]:out.add(e)
 for v in g:
  if v not in tin:dfs(v)
 return out

def route(B,k,x,y):
 g=graph(B,k);prev={x:None};todo=[x]
 for v in todo:
  if v==y:break
  for u,e in g.get(v,()):
   if u not in prev:prev[u]=(v,e);todo.append(u)
 if y not in prev:return None
 out=[]
 while y!=x:y,e=prev[y];out.append(e)
 return out[::-1]

def run(B,p,h,steps,word=None):
 B=set(B);k=int(wvertex(p,h).real+wvertex(p,h).imag)%4;entry=set(B);ew=wvertex(p,h);arms=[];proper=False;chain=None;ci=0;left=False;erasures=[];maxrelease=0;consumed=0
 for t in range(steps):
  q=p;old=set(B);oldbr=bridge_set(old,k);oldw=wvertex(p,h);ch='L'if q in B else'R';assert word is None or ch==word[t]
  if ch=='L':
   wn=q not in oldbr;zn=q not in bridge_set(old,2-k);erasures.extend([t]if wn or zn else[])
   if chain is not None and not wn and len(arms)<=2:
    if q in chain:assert not left and ci<len(chain)and q==chain[ci];ci+=1;consumed+=1;stats['serial_prefix_edges']+=1
    else:left=True
  p,h,_=step(B,p,h);newbr=bridge_set(B,k);stats['fine_steps']+=1
  if ch=='R':
   arms.append(q);u,v=ends(q,k);path=route(old,k,u,v)
   if path is None:assert newbr==oldbr|{q};stats['bridge_insertions']+=1
   else:assert newbr==oldbr-set(path);stats['path_contractions']+=1
   assert wvertex(p,h)==oldw
  else:
   arrival=wvertex(p,h);assert{arrival,oldw}==set(ends(q,k))
   if wn:
    path=route(B,k,arrival,oldw);assert path is not None;newchain=[e for e in path if e in newbr];assert set(newchain)==newbr-oldbr and oldbr<=newbr;maxrelease=max(maxrelease,len(newchain));stats['serial_expansions']+=1
   else:assert newbr==oldbr-{q}
   if proper:
    r=len(arms);assert r in(0,1,2,4);stats['proper_r'+str(r)]+=1;C=component(entry,k,ew)[1];actual=component(B,k,arrival)[1]
    if r<=2:
     assert q in C
     if r==2:assert len(graph(entry,k).get(ew,()))==1 and q in bridge_set(entry,k)
     if not wn:assert actual==component(entry-{q},k,arrival)[1];stats['far_side_inheritances']+=1
     else:
      expected=(C-{q})|set(arms)
      for e in arms:
       v=next(v for v in ends(e,k)if v!=ew);expected|=component(entry,k,v)[1]
      expected.discard(q);assert actual==expected
      external=set()
      for e in arms:
       v=next(v for v in ends(e,k)if v!=ew);vs,es=component(entry,k,v)
       if not(v in component(entry,k,ew)[0]):external.add(frozenset(vs))
      assert len(external)<=1;stats['ordinary_external_imports']+=len(external)
    else:
     assert not C and len(arms)==4 and q==arms[0];targets=[next(v for v in ends(e,k)if v!=ew)for e in arms[1:]];av,ae=component(entry,k,arrival);rejoin=any(v in av for v in targets);assert rejoin==wn
     if not rejoin:assert actual==ae;stats['isolated_bridge_resets']+=1
     else:
      expected=set(arms[1:])|ae;ids={frozenset(av)}
      for v in targets:vs,es=component(entry,k,v);expected|=es;ids.add(frozenset(vs))
      assert actual==expected and len(ids)<=3;stats['isolated_nonbridge_splices']+=1
   if wn or len(arms)==4:chain=None;ci=0;left=False
   if wn:chain=newchain;ci=0;left=False
   entry=set(B);ew=arrival;arms=[];proper=True
 return {'mass':len(B),'erasures':erasures,'max_release':maxrelease,'consumed':consumed}
# Fixed local masks exercise arbitrary starting pose, including a partial first run.
cells=[complex(x,y)for x in range(-1,2)for y in range(-1,2)]
for mask in range(512):
 B={q for i,q in enumerate(cells)if mask>>i&1}
 for h in(0,1):run(B,0j,h,12)
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());run({complex(*q)for q in std['seed']},0j,std['heading'],312,std['word']*3)
rods=[]
for r in(1,2,3,10,30,100):
 ret={complex(2*r,-1),complex(2*r+1,-2)}|{complex(x,x-2*r-4)for x in range(r,2*r+2)}|{complex(x,-x-5)for x in range(-2,r)}|{-2-2j,-1-1j};rod={complex(x,0)for x in range(2*r)};B=ret|rod;assert len(ret)==2*r+8 and len(B)==4*r+8
 assert rank(B,2)==1 and len(component(B,2,ends(next(iter(B)),2)[0])[1])==len(B);assert all(len(es)==2 for es in graph(B,2).values())
 zr=graph(ret,0);zp=graph(rod,0);assert not set(zr)&set(zp)and rank(ret,0)==0;assert max(v.imag for v in zr)==-1;assert{int(v.real)for v in zr if v.imag==-1}=={-3,4*r+1}
 todo=set(ret);sizes=[]
 while todo:
  q=next(iter(todo));vs,es=component(ret,0,ends(q,0)[0]);todo-=es;sizes.append(len(es))
 assert Counter(sizes)=={1:2*r+2,2:3};assert rank(B,0)==0
 result=run(B,0j,1,4*r,'LRRL'*r);assert result['erasures']==[0]and result['max_release']==4*r+7 and result['consumed']==2*r-1;rods.append({'r':r,**result})
# Independent complete lifetime replay of the new 42-update non-LIFO witness.
B=set();p=0j;h=0;k=int(wvertex(p,h).real+wvertex(p,h).imag)%4;birth={};archives=[];word=''
for t in range(43):
 active=component(B,k,wvertex(p,h))[1];ids={birth[q]for q in active}
 for ar in archives:
  if ar['return']is None and set(ar['lifetimes'])&ids:
   assert all(q in B and birth[q]==b for q,b in ar['pairs']);ar['return']=t
 if t==42:break
 q=p;oldw=wvertex(p,h);L=q in B;word+='L'if L else'R'
 if not L:birth[q]=t
 p,h,_=step(B,p,h)
 if L:
  del birth[q]
  if not connected(B,k,*ends(q,k)):
   oldC=component(B,k,oldw)[1]
   if oldC:
    assert oldC.isdisjoint(component(B,k,wvertex(p,h))[1]);archives.append({'state':t+1,'cells':sorted((int(q.real),int(q.imag))for q in oldC),'lifetimes':sorted(birth[q]for q in oldC),'pairs':[(q,birth[q])for q in oldC],'return':None})
old=next(ar for ar in archives if ar['state']==17);assert old['cells']==[(1,-1),(1,0)]and old['lifetimes']==[1,2]and old['return']==42
for t,cs in[(18,[(-1,1),(0,1)]),(32,[(-2,0)]),(33,[(-3,-2),(-3,-1)])]:
 ar=next(ar for ar in archives if ar['state']==t);assert ar['cells']==cs and ar['return']is None
nonlifo={'word':word,'archives':[{k:v for k,v in ar.items()if k!='pairs'}for ar in archives]}
ref=json.loads((R/'global_cycle_birth_2026-10-23/bridge_archive_nonlifo.json').read_text());assert ref['word42']==word
notes={}
for name in ['serial_bridge_release_and_archive_splice.md','serial_bridge_release_and_archive_splice_v2.md']:
 p=D/name
 if p.exists():notes[name]=hashlib.sha256(p.read_bytes()).hexdigest()
assert notes['serial_bridge_release_and_archive_splice_v2.md']=='f1df38ca56a45ea5cbef0d318b6cc5942f8a27af35787387bf691bd178eee351'
out={'status':'PASS serial bridge release, exact proper-block archive splice and all-r one-erasure rod construction','notes':notes,'counts':dict(stats),'rods':rods,'nonlifo':nonlifo,'analytic':['Deleting a nonbridge e creates exactly the bridges separating its endpoints in G-e. They form the unique endpoint-to-endpoint bridge-tree path; every old bridge remains. Restoring/inserting an intracomponent edge contracts precisely that bridge path. All embedded blocks, attachment vertices and remote subtrees are retained.','The stronger chain-prefix law holds until the next proper r4 or w-nonbridge block, even across z-only erasures; every intervening proper r<=2 w-bridge block retains exact far-side inheritance. The 42-update complete-lifetime replay also verifies a bridge archive created at17 first reactivates42 while newer archives18,32,33 remain dormant.', 'After a w-erasure, the signed no-erasure zipper is a simple bridge path from the actual arrival vertex. Its new-chain edges form a prefix; leaving via an old side branch is irreversible until another erasure. The prefix may be empty if a nontrivial block separates the cursor from the next attachment.','A proper block starts immediately after L, so its incoming port is absent. Its R count is0,1,2,4, never3. For r2, the departure is the sole entry incident edge, hence a leaf bridge. If it is now nonbridge one new arm must reconnect its old far component, leaving at most one external-component import. For r0/1 the same at-most-one bound is immediate.','For r4 the entry cursor is isolated. After first-arm deletion, no remaining arm into the arrival old component gives exactly that unchanged component. Otherwise remaining three arms connect at most three whole old components. Isolated marked vertices are retained in these component identities. The arbitrary first interval block need not be proper.','The explicit return-cell formulas give a simple w cycle of4r+8 edges. In the opposite lattice its return edges form2r+2 isolated edges and three2-edge paths, disjoint from the original rod. All doubled return Y<=-1; the only Y=-1 vertices have X=-3 or4r+1, beyond the rod endpoints. New upper-row vertices have Y>=1, so no z cycle can appear.','In w, first L opens the unique cycle into the serial4r+7 chain. Return vertices have Y<=-1 while newly written upper-row vertices have Y>=1; the standard paired-forest rod induction attaches the growing written path only at the unwritten frontier. Thus every later L is a bridge in both lattices. The exact LRRL word consumes2r-1 further chain edges and has no second erasure for all r>=1.'],'scope':'Full-board graph calculus and finite growing-mass controls. No constant release-length, LIFO theorem, finite summary, renewal budget, capture distinction or universal capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(stats)
