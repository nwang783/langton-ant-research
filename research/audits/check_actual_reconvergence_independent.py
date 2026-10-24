"""Independent literal fine steps, explicit incidence graph and complete low-mass tree."""
from pathlib import Path
from collections import deque
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
F=ROOT/'core_periodicity_new/all_input_reconvergence_frozen_20261023_0945';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((F/'02_single_root_reconvergence_certificate.json').read_text());IDS=(0,1,4,5,6,7,8,9);K={q for q,b in walk(mark)[2].items()if b};G={}
for a in IDS:
 assert(raws[a]+mark).startswith(mark)
 e,h,_,f=walk(raws[a]);B={q for q,b in walk(raws[a]+mark)[2].items()if b};post={e+rotation(q,h)for q in K};G[a]=(B-K,(B^f)-post,e,h)
def program(w):return ''.join(raws[a]for a in w)+mark
def seed(w):
 try:return{q for q,b in walk(program(w))[2].items()if b}
 except AssertionError:return None
def graph(w,B):
 # Every packet and every birth is a separate vertex; cycle rank computed by
 # undirected DFS only after all edges are explicitly installed.
 live={q:('r',i)for i,q in enumerate(sorted(B-K,key=xy))};adj={v:set()for v in live.values()};origin={v:{q}for q,v in live.items()};birth={v:None for v in live.values()};p=0j;h=0;clock=0;hist=[];edges=0
 for j,a in enumerate(w):
  I,O,e,dh=G[a];qs=sorted((p+rotation(z,h)for z in I),key=xy);inputs=[live.pop(q)for q in qs];pn=('p',j);adj[pn]=set(inputs)
  for v in inputs:adj[v].add(pn)
  parents=set().union(*(origin[v]for v in inputs));out=[]
  for i,q in enumerate(sorted((p+rotation(z,h)for z in O),key=xy)):
   v=('o',j,i);assert q not in live;live[q]=v;adj[v]={pn};adj[pn].add(v);origin[v]=parents.copy();birth[v]=clock;out.append(v)
  edges+=len(inputs)+len(out);hist.append(dict(packet=a,pose=[*xy(p),h],inputs=list(map(xy,qs)),ids=inputs,roots=sorted(map(xy,parents)),ages=[None if birth[v]is None else clock-birth[v]for v in inputs]));p+=rotation(e,h);h=(h+dh)%4;clock+={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}[a]
 seen=set();components=[]
 for v in adj:
  if v in seen:continue
  stack=[v];seen.add(v);component=[]
  while stack:
   u=stack.pop();component.append(u)
   for t in adj[u]:
    if t not in seen:seen.add(t);stack.append(t)
  components.append(component)
 return edges-len(adj)+len(components),hist,len(live),components
w=(1,6,4,4);B=seed(w);assert sorted(map(xy,B))==list(map(tuple,J['initial_black_cells']))and len(B)==9
# Execute actual turns from membership, rather than replaying prescribed toggles.
p=0j;h=0;board=B.copy();bound=[];t=0
for a in w:
 for ch in raws[a]:
  got='L'if p in board else'R';assert got==ch;board.symmetric_difference_update({p});h=(h+(1 if got=='R'else-1))%4;p+=rotation(1j,h);t+=1
 bound.append([t,*xy(p),h,len(board)])
assert bound==J['boundaries']and len(board)==30 and(p,h)==(3+0j,1)
for ch in mark:
 got='L'if p in board else'R';assert got==ch;board.symmetric_difference_update({p});h=(h+(1 if got=='R'else-1))%4;p+=rotation(1j,h)
beta,hist,res,comps=graph(w,B);assert beta==1 and res==25 and len(comps)==2
assert hist[-1]['roots']==[(0,1)]and hist[-1]['ages']==[3,3]and all(v[:2]==('o',0)for v in hist[-1]['ids'])
Q=deque([()]);accepted=[()];extensions=0;conflicts=mass=0
while Q:
 v=Q.popleft()
 for a in IDS:
  extensions+=1;ww=v+(a,);bb=seed(ww)
  if bb is None:conflicts+=1
  elif len(bb)>8:mass+=1
  else:assert graph(ww,bb)[0]==0;accepted.append(ww);Q.append(ww)
assert set(accepted)==set(map(tuple,J['low_mass_prefix_tree']['accepted_words']))and len(accepted)==31 and extensions==248
out=dict(status='PASS actual nine-cell single-residual-root reconvergence and complete mass<=8 prefix closure',word=w,raw_steps=109,actual_marker_steps=11,entry_mass=9,beta=beta,final_residual_mass=res,incidence_components=len(comps),last_input_roots=hist[-1]['roots'],last_input_ages=hist[-1]['ages'],low_mass_nodes=len(accepted),extensions=extensions,literal_conflicts=conflicts,over_mass_rejections=mass,max_packets=max(map(len,accepted)),manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),scope='Minimal boundary mass for reconvergence in this complete recurrent-eight language only. Other physical helper roots genuinely participate; no repeated renewal or infinite finite-seed trajectory.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
