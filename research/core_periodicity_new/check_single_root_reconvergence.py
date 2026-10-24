"""Direct literal controls and finite all-length closure for entry mass <=8.
The all-input cycle is a residual-identity graph, not physical token ownership.
"""
from pathlib import Path
from collections import deque
import json,hashlib
W=Path(__file__).resolve().parent;P=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(P.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9);VEC=((0,1),(1,0),(0,-1),(-1,0));MARK=G[0]['marker'];assert MARK=='LLLLRLRRRRL'
def requirements(word):
 raw=''.join(G[a]['word']for a in word);program=raw+MARK
 col={};initial={};x=y=h=0;conflict=None;bound=[];endraw=None
 for t,ch in enumerate(program):
  p=(x,y);b=ch=='L'
  if p in col:
   if col[p]!=b:conflict=[t,list(p),ch,'L'if col[p]else'R'];break
  else:col[p]=b;initial[p]=b
  col[p]=not b;h=(h+(-1 if b else 1))%4;dx,dy=VEC[h];x+=dx;y+=dy
  if t+1==len(raw):endraw=[x,y,h]
 return dict(consistent=conflict is None,conflict=conflict,initial_black_cells=sorted(p for p,b in initial.items()if b),raw_length=len(raw),raw_end_pose=endraw,after_marker_pose=[x,y,h])
# Every accepted node has all 8 next packet extensions accounted for. No depth cap.
Q=deque([()]);accepted=[()];rejections=[]
while Q:
 word=Q.popleft()
 for a in IDS:
  w=word+(a,);r=requirements(w)
  if r['consistent']and len(r['initial_black_cells'])<=8:
   Q.append(w);accepted.append(w)
  else:rejections.append(dict(word=w,reason='literal_conflict'if not r['consistent']else'needs_at_least_nine_black',minimum_black=len(r['initial_black_cells'])if r['consistent']else None,conflict=r['conflict']))
assert len(accepted)==31 and max(map(len,accepted))==3
word=(1,6,4,4);R=requirements(word);seed=[(-2,2),(-1,-1),(-1,0),(-1,1),(-1,3),(0,-1),(0,0),(0,1),(1,0)]
assert R['consistent']and R['initial_black_cells']==seed and R['raw_length']==109 and R['raw_end_pose']==[3,0,1]
# Direct unconditioned ant run on the explicit nine-cell board, including final marker.
B=set(seed);x=y=h=0;program=''.join(G[a]['word']for a in word)+MARK;boundaries=[];ticks={25,73,91,109}
for t,ch in enumerate(program):
 p=(x,y);b=p in B;assert('L'if b else'R')==ch
 if b:B.remove(p)
 else:B.add(p)
 h=(h+(-1 if b else 1))%4;dx,dy=VEC[h];x+=dx;y+=dy
 if t+1 in ticks:boundaries.append([t+1,x,y,h,len(B)])
# Independent all-input graph replay: initial roots label themselves; component union.
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};roots=[p for p in seed if p not in K];T={p:('root',i,i)for i,p in enumerate(roots)};P0=list(range(len(roots)));head=(0,0);h=0;history=[];beta=0
rot=lambda p,h:((p[0],p[1]),(p[1],-p[0]),(-p[0],-p[1]),(-p[1],p[0]))[h%4]
add=lambda p,q:(p[0]+q[0],p[1]+q[1])
def find(a):
 while P0[a]!=a:a=P0[a]
 return a
for j,a in enumerate(word):
 I=[add(head,rot(p,h))for p in G[a]['inputs']];inp=[T.pop(p)for p in I];comps={find(t[-1])for t in inp};inc=len(I)-len(comps);beta+=inc;z=min(comps)
 for k in comps:P0[k]=z
 O=[]
 for si,p in enumerate(G[a]['outputs']):
  q=add(head,rot(p,h));assert q not in T;T[q]=(j,si,z);O.append(q)
 history.append(dict(packet=a,pose=[*head,h],inputs=[list(p)for p in I],input_identities=inp,input_components=sorted(comps),beta_increment=inc))
 dx,dy,dh=G[a]['endpoint'];head=add(head,rot((dx,dy),h));h=(h+dh)%4
assert beta==1 and history[-1]['beta_increment']==1
assert all(t[0]==0 for t in history[-1]['input_identities'])
assert len({find(i)for i in range(len(roots))})==2
# Both final input identities descend from the first DC's SINGLE initial input.
componentroots=[[roots[i]for i in range(len(roots))if find(i)==c]for c in sorted({find(i)for i in range(len(roots))})]
assert [(0,1)]in componentroots
# Every one of the 30 nonempty low-mass accepted words also has beta zero.
lowbetas=[]
for lowword in accepted[1:]:
 lowseed=set(map(tuple,requirements(lowword)['initial_black_cells']));lr=sorted(lowseed-K);lt={p:i for i,p in enumerate(lr)};lp=list(range(len(lr)));lh=(0,0);ld=0;lb=0
 def lf(a):
  while lp[a]!=a:a=lp[a]
  return a
 for a in lowword:
  ii=[add(lh,rot(p,ld))for p in G[a]['inputs']];cc={lf(lt.pop(p))for p in ii};lb+=len(ii)-len(cc);zz=min(cc)
  for k in cc:lp[k]=zz
  for p in G[a]['outputs']:q=add(lh,rot(p,ld));assert q not in lt;lt[q]=zz
  dx,dy,dh=G[a]['endpoint'];lh=add(lh,rot((dx,dy),ld));ld=(ld+dh)%4
 assert lb==0
 lowbetas.append(lb)
O=dict(status='AUTHOR_DIRECT_LITERAL_AND_INCIDENCE_PASS',word=word,names=[G[a]['name']for a in word],entry_total_mass=9,initial_black_cells=seed,requirements=R,boundaries=boundaries,beta=beta,final_residual_count=len(T),final_incidence_components=componentroots,history=history,minimality_scope='For entry total mass <=8, every complete recurrent-eight prefix tree is finite with maximum3 packets, hence no incidence cycle. This is an exact 31-node/248-extension closure, not a depth cap and not a global ant theorem.',low_mass_prefix_tree=dict(mass_cap=8,accepted_words=accepted,accepted_nonempty_betas=lowbetas,max_packet_length=3,rejected_extensions=rejections),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[W/'chronology_dcuv/literal_residual_geometry.json',Path(__file__).resolve()]})
TGT=W/'all_input_literal_probe/single_root_reconvergence_certificate.json';TGT.write_text(json.dumps(O,indent=2)+'\n');print(json.dumps({k:v for k,v in O.items()if k not in('low_mass_prefix_tree','history')},indent=2));print(TGT)
