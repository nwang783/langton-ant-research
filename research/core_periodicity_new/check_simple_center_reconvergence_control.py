"""Actual19-cell simple-center / beta1 control, direct physical and incidence replay.
Not a discovery-search certificate or minimality claim. No reuse of the probe output.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json';HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
word=[9,4,1,0,5,0,7]
seed={(-2,0),(-2,1),(-2,3),(-1,-1),(-1,0),(-1,1),(-1,2),(-1,4),(0,-2),(0,-1),(0,0),(0,2),(0,3),(1,-1),(1,0),(2,-1),(2,3),(3,1),(3,2)}
VEC=((0,1),(1,0),(0,-1),(-1,0))
def rot(z,h):
 x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def base(a):return 0 if a in[0,1]else 4 if a in[4,5,6]else 7
MARK=G[0]['marker'];CWORD=G[1]['word'][len(G[0]['word']):];assert len(CWORD)==15
raw=''.join(G[a]['word']for a in word);program=raw+MARK
# Derive the exact minimal first-L initial field from literal parity, not the probe.
p=(0,0);h=0;par=set();need={};poses={0:[0,0,0]}
for t,ch in enumerate(program):
 b=(ch=='L')^(p in par)
 assert p not in need or need[p]==b
 need[p]=b
 if p in par:par.remove(p)
 else:par.add(p)
 h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h]);poses[t+1]=[*p,h]
assert {p for p,b in need.items()if b}==seed and K<=seed and len(seed)==19
# Direct unconditioned fine-step simulation on that finite board.
B=set(seed);p=(0,0);h=0;boards={0:set(B)};rawticks=[];tick=0
for a in word:tick+=len(G[a]['word']);rawticks.append(tick)
for t,ch in enumerate(program):
 b=p in B;assert('L'if b else'R')==ch
 if b:B.remove(p)
 else:B.add(p)
 h=(h+(-1 if b else 1))%4;p=add(p,VEC[h]);assert poses[t+1]==[*p,h]
 if t+1 in rawticks:boards[t+1]=set(B)
assert len(raw)==182 and rawticks[-1]==182
# Exact complete all-input incidence forest/cycle replay, with ALL14 entry roots present.
roots=sorted(seed-K);assert len(roots)==14
P=list(range(len(roots)));T={q:dict(kind='entry',root=i,identity=['entry',i],birth_C=None)for i,q in enumerate(roots)}
def find(a):
 while P[a]!=a:a=P[a]
 return a
history=[];beta=0;p=(0,0);h=0;clock=0;tick=0;produced=[]
for j,a in enumerate(word):
 current=boards[tick];core={add(p,rot(q,h))for q in K};assert current==core|set(T)and not core&set(T)
 for x,y,b,*_ in G[a]['requirements']:assert(add(p,rot((x,y),h))in current)==bool(b)
 I=[add(p,rot(q,h))for q in G[a]['inputs']];tags=[T.pop(q)for q in I];cc={find(t['root'])for t in tags};inc=len(I)-len(cc);beta+=inc;rr=min(cc)
 for k in cc:P[k]=rr
 inrows=[]
 for q,z in zip(I,tags):
  age=None if z['birth_C']is None else clock-z['birth_C'];inrows.append(dict(cell=q,identity=z['identity'],source_C_age=age,component_at_consumption=rr))
  if z['kind']=='produced':
   sj,si=z['identity'];s=history[sj];sh=s['pose'][2];sp=tuple(s['pose'][:2]);rel=rot(sub(p,sp),-sh);dh=(h-sh)%4;ol=G[s['packet']]['outputs'][si];key=(s['packet'],a,*rel,dh,*ol);ck=(mp[s['packet']],mp[a],*rel,dh,*ol,min(age,5));assert key not in HB and ck not in COUNT;produced.append(dict(source_packet_index=sj,consumer_packet_index=j,source_output=ol,global_cell=q,full_source_age=age,HB_key=key,count5_key=ck,HB_excluded=False,count5_excluded=False))
 O=[]
 for si,z in enumerate(G[a]['outputs']):
  q=add(p,rot(z,h));assert q not in T;T[q]=dict(kind='produced',root=rr,identity=[j,si],birth_C=clock);O.append(dict(cell=q,identity=[j,si]))
 row=dict(packet_index=j,packet=a,name=G[a]['name'],pose=[*p,h],C_before=clock,inputs=inrows,input_distinct_components=sorted(cc),beta_increment=inc,outputs=O)
 history.append(row);dx,dy,dh=G[a]['endpoint'];p=add(p,rot((dx,dy),h));h=(h+dh)%4;clock+=G[a]['name'].count('C');tick+=len(G[a]['word']);assert poses[tick]==[*p,h]
 nextcore={add(p,rot(q,h))for q in K};assert boards[tick]==nextcore|set(T)and not nextcore&set(T)
assert beta==1 and history[-1]['beta_increment']==1 and len(produced)==3 and clock==4
assert[tuple(t['cell'])for t in history[-1]['inputs'][:2]]==[(2,0),(2,1)]
assert all(t['identity'][0]==0 and t['source_C_age']==4 for t in history[-1]['inputs'][:2])
components=sorted({find(i)for i in range(len(roots))});assert len(components)==5
v=sum(a in[4,5,6]for a in word);u=sum(a in[7,8,9]for a in word);assert beta==v+4*u-len(roots)+len(components)
assert len(T)==42 and len(boards[tick])==47
# Actual raw atomic cuts, reconstructed against the FINE path poses.
arcs=[];p=(0,0);h=0;clock=0;tt=0
for a in word:
 atoms=[base(a)]+['C']*G[a]['name'].count('C')
 for at in atoms:
  start=[*p,h];c=add((2*p[0],2*p[1]),rot((-1,-1),h));length=len(CWORD)if at=='C'else len(G[at]['word']);endpose=poses[tt+length];ep=tuple(endpose[:2]);eh=endpose[2];e=add((2*ep[0],2*ep[1]),rot((-1,-1),eh));expected=rot((2,2)if at in[0,'C']else(2,6)if at==4 else(0,8),h);assert sub(e,c)==expected
  arcs.append(dict(index=len(arcs),atom=at,entry_pose=start,entry_C=clock,center_start_twice=c,center_end_twice=e));p=ep;h=eh;tt+=length;clock+=at=='C'
assert len(arcs)==11 and tt==len(raw)
def on(z,p,q):return det(sub(q,p),sub(z,p))==0 and all(min(p[k],q[k])<=z[k]<=max(p[k],q[k])for k in[0,1])
pairs=[]
for i in range(len(arcs)):
 for j in range(i+1,len(arcs)):
  a=arcs[i];b=arcs[j];p=tuple(a['center_start_twice']);q=tuple(a['center_end_twice']);z=tuple(b['center_start_twice']);w=tuple(b['center_end_twice']);d=sub(q,p);e=sub(w,z);delta=sub(z,p);dd=det(d,e);rec=dict(i=i,j=j,adjacent=j==i+1,determinant=dd)
  if dd:
   s=F(det(delta,e),dd);t=F(det(delta,d),dd);rec['earlier_parameter']=str(s);rec['later_parameter']=str(t);touch=0<=s<=1 and 0<=t<=1
   if j==i+1:assert touch and s==1 and t==0
   else:assert not touch
  else:
   pts=sorted({k for k in[p,q,z,w]if on(k,p,q)and on(k,z,w)})
   if j==i+1:assert pts==[q]and q==z
   else:assert not pts
   rec['collinear_common_endpoints']=pts
  rec['status']='ADJACENT_ONLY_SHARED_ENDPOINT'if j==i+1 else'NONADJACENT_DISJOINT';pairs.append(rec)
assert len(pairs)==55 and sum(not r['adjacent']for r in pairs)==45
O=dict(status='AUTHOR_ACTUAL_SIMPLE_CENTER_BETA_ONE_CONTROL_PASS',scope='Actual finite19-cell UCC,V,DC,D,VC,D,U complete8 factor has simple corrected-center path but all-input incidence beta1. Direct raw+marker and all55 exact segment-pair replay. Refutes simplicity=>beta0, not all possible rank bounds. No minimal-mass claim, renewal or infinite trajectory.',word=word,names=[G[a]['name']for a in word],initial_actual_board=sorted(seed),entry_mass=len(seed),entry_residual_roots=roots,raw_length=len(raw),marker=MARK,raw_end_pose=poses[len(raw)],final_raw_black_count=len(boards[len(raw)]),final_raw_residual_count=len(T),C=clock,beta=beta,incidence_component_count=len(components),incidence_components=[[roots[i]for i in range(len(roots))if find(i)==c]for c in components],packet_history=history,all3_produced_age_HB_count_queries=produced,all11_actual_atomic_chords=arcs,all55_exact_segment_pairs=pairs,first_L_seed_exact=True,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/simple_center_reconvergence_control.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print({k:O[k]for k in['word','entry_mass','raw_length','raw_end_pose','final_raw_black_count','C','beta','incidence_component_count']})
