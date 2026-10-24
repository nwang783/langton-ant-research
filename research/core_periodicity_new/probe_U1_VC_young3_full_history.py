"""One-shot VC-young3 full-history discovery, not an exclusion from a cap.
Exact literal predecessor constraints, k7, physical residual-origin obligations,
JO/KV/count5 and complete initial-activation cutoff. No fixed middle word.
"""
from pathlib import Path
import json,hashlib,heapq,time,sys
R=Path(__file__).resolve().parent;D=R/'chronology_dcuv';GP=D/'literal_residual_geometry.json';RP=D/'delayed_height_probe/u1_residue_cegar/root_out.json';FP=D/'critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';KP=D/'literal_factor_dfa_k7.json'
G=json.loads(GP.read_text())['geometry'];RJ=json.loads(RP.read_text());A=RJ['core_offsets'];T={(a,h):t for a,h,t in RJ['created_peaks']};Z=json.loads(KP.read_text());KT=Z['transitions'];KI=Z['initial_class'];keep=Z['keep'];kid={a:i for i,a in enumerate(keep)};del Z
M={0:0,1:1,4:2,5:3,6:4,7:5,8:6,9:7};F={tuple(map(int,s.split()[:8]))for s in FP.read_text().splitlines()};DIR=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};S=28;Iweight=28;CAP=int(sys.argv[1])if len(sys.argv)>1 else 100000
# Selected VC source fixed at0,N; its lower outputs feed U(0,-1,E), exactage3.
goalpose=(0,-1,1);lower={(1,0),(2,0)};upper={(4,0),(2,-1),(3,-1)}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plus(p,q):return p[0]+q[0],p[1]+q[1]
def core(p,h):return{plus(p,rot(q,h))for q in K}
def badblack(B,p,h):return{q for q in B-core(p,h)if Iweight+2*sum(q)>=S}
def k7ok(word):
 s=KI
 for a in word:
  s=KT[s][kid[a]]
  if s<0:return False
 return True
ops={}
for a in keep:
 for h in range(4):
  cb={rot(q[:2],h)for q in G[a]['requirements']if q[2]};cw={rot(q[:2],h)for q in G[a]['requirements']if not q[2]};X={rot(q,h)for q in G[a]['raw_odd']};O={rot(q,h):tuple(q)for q in G[a]['outputs']};e=rot(G[a]['endpoint'][:2],h);cc=G[a]['name'].count('C');ops[a,h]=(cb,cw,X,O,e,cc)
cb,cw,_,_,_,_=ops[7,1];B=frozenset(plus(goalpose[:2],q)for q in cb);W=frozenset(plus(goalpose[:2],q)for q in cw)
# Current residual obligation: cell ->(consumerID,consumerheading,localIx,localIy,Cage_so_far).
ob={plus(goalpose[:2],rot(q,1)):(7,1,*q,0)for q in G[7]['inputs']}
def cone0(p):
 # sourceVC raw exit(1,4,W), zero-C D/V/U endpoints(-1,1),(-3,1),(-4,0).
 dx=p[0]-1;dy=p[1]-4;z=-dx-dy
 if dy<0 or z<0 or z%2:return False
 z//=2
 # b+2c=z and a=dy-b>=0.
 return z%2<=min(dy,z)
def replay(word,start):
 # Build the exact initial board from the backward requirements; all unseen cells white.
 p,h=start;seed=set(nodes[current]['B']);C0=core(p,h);assert C0<=seed
 Board=set(seed);L={q:('entry',None)for q in seed-C0};clock=0;rows=[];source_index=None
 for j,a in enumerate(word):
  C=core(p,h);assert C.isdisjoint(L)and Board==C|set(L)
  inp=[plus(p,rot(q,h))for q in G[a]['inputs']];births=[L[q]for q in inp]
  for q,v in zip(inp,births):
   if v[0]=='entry':assert Iweight+2*sum(q)<S,(j,q,'initial activation')
  ev=2*sum(p)+A[h];cr=2*sum(p)+T[a,h]
  assert max(ev,cr)<S if j<len(word)-1 else cr==S
  if a==5 and p==(0,0)and h==0:
   # The exact source is identified by final lower identity births below.
   pass
  rows.append(dict(index=j,packet=a,pose=[*p,h],C_clock=clock,entry_core=ev,created_peak=cr,input_cells=inp,input_births=births))
  if j==len(word)-1:
   assert a==7 and(p,h)==(goalpose[:2],goalpose[2]);assert all(v[0]!='entry'for v in births)
   assert births[0][0]==births[1][0];source_index=births[0][0];sr=rows[source_index]
   assert sr['packet']==5 and sr['pose']==[0,0,0]and[clock-v[1]for v in births[:2]]==[3,3]
   assert all(v[0]<source_index and clock-v[1]>=5 for v in births[2:])
   sv=sr['input_births'];assert all(v[0]!='entry'for v in sv);assert[sr['C_clock']-v[1]for v in sv][0]>=2 and[sr['C_clock']-v[1]for v in sv][1]>=3
  for q in inp:del L[q]
  for q in G[a]['outputs']:
   z=plus(p,rot(q,h));assert z not in L;L[z]=(j,clock)
  for ch in G[a]['word']:
   assert(ch=='L')==(p in Board)
   if p in Board:Board.remove(p)
   else:Board.add(p)
   h=(h+(-1 if ch=='L'else 1))%4;p=plus(p,DIR[h])
  clock+=G[a]['name'].count('C')
 for ch in G[7]['marker']:
  assert(ch=='L')==(p in Board)
  if p in Board:Board.remove(p)
  else:Board.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;p=plus(p,DIR[h])
 return dict(word=word,initial_pose=[*start[0],start[1]],seed=sorted(seed),mass=len(seed),source_index=source_index,rows=rows)
nodes=[];seen=set();todo=[];stats=dict(pops=0,attempts=0,record_cuts=0,k7_cuts=0,origin_cuts=0,count5_cuts=0,source_cuts=0,cone_cuts=0,color_cuts=0,duplicates=0)
def add(B,W,p,h,ob,found,c,headword,parent,a):
 O=tuple(sorted(ob.items()));key=(B,W,p,h,O,found,c,headword)
 if key in seen:stats['duplicates']+=1;return
 seen.add(key);depth=0 if parent<0 else nodes[parent]['depth']+1;bad=badblack(B,p,h);high=sum(Iweight+2*sum(q)>=S for q in ob);idx=len(nodes)
 nodes.append(dict(B=B,W=W,p=p,h=h,ob=ob,found=found,c=c,headword=headword,parent=parent,a=a,depth=depth,bad=bad))
 score=depth+25*len(bad)+8*high+(20 if not found else 0);heapq.heappush(todo,(score,depth,idx))
add(B,W,goalpose[:2],goalpose[2],ob,False,0,(7,),-1,-1);t0=time.time();hit=None;current=-1
while todo and len(nodes)<CAP:
 score,depth,current=heapq.heappop(todo);n=nodes[current];stats['pops']+=1
 if n['found']and not n['bad']:
  word=[];q=current
  while nodes[q]['parent']>=0:word.append(nodes[q]['a']);q=nodes[q]['parent']
  word.append(7);hit=replay(word,(n['p'],n['h']));break
 for a in keep:
  stats['attempts']+=1
  if not k7ok((a,)+n['headword']):stats['k7_cuts']+=1;continue
  h=(n['h']-G[a]['endpoint'][2])%4;cb,cw,x,o,e,cc=ops[a,h];p=n['p'][0]-e[0],n['p'][1]-e[1]
  if 2*sum(p)+max(A[h],T[a,h])>=S:stats['record_cuts']+=1;continue
  found=n['found'];c=n['c']+cc
  is_source=not found and a==5 and p==(0,0)and h==0 and c==3
  if not found and c>=3 and not is_source:stats['source_cuts']+=1;continue
  O={plus(p,q):z for q,z in o.items()};C={plus(p,q)for q in cb|cw};nob={};bad=False
  for q,v in n['ob'].items():
   b,hb,ix,iy,age=v;age=min(5,age+cc)
   if q in O:
    if not found and q in lower and not is_source:stats['source_cuts']+=1;bad=True;break
    ox,oy=O[q];dh=(hb-h)%4;rx,ry=rot((ix,iy),dh);query=(M[a],M[b],ox-rx,oy-ry,dh,ox,oy,age)
    if query in F:stats['count5_cuts']+=1;bad=True;break
   elif q in C:stats['origin_cuts']+=1;bad=True;break
   else:nob[q]=(b,hb,ix,iy,age)
  if bad:continue
  if is_source:
   if any(q in nob for q in lower):stats['source_cuts']+=1;continue
   found=True
  for inp in G[a]['inputs']:
   q=plus(p,rot(inp,h));assert q not in nob;nob[q]=(a,h,*inp,0)
  if not found:
   if c==2 and not cone0(p):stats['cone_cuts']+=1;continue
   if c==1 and p[0]>0:stats['cone_cuts']+=1;continue
  X={plus(p,q)for q in x};BB=(n['B']-X)|(n['W']&X);WW=(n['W']-X)|(n['B']&X);QB={plus(p,q)for q in cb};QW={plus(p,q)for q in cw}
  if BB&QW or WW&QB:stats['color_cuts']+=1;continue
  add(frozenset(BB|QB),frozenset(WW|QW),p,h,nob,found,0 if found else c,(a,)+n['headword'][:5],current,a)
  if len(nodes)>=CAP:break
 if stats['pops']%1000==0:print(json.dumps(dict(**stats,labels=len(nodes),queue=len(todo),depth=depth,score=score,source_found=n['found'],pending_origins=len(n['ob']),forbidden_initial=len(n['bad']),seconds=round(time.time()-t0,2))),flush=True)
status='ACTUAL_UNFUNDED_U1_VC_YOUNG3_CONTROL'if hit else'CAP_UNKNOWN'if todo else'EXACT_STATE_EXHAUSTION_PENDING_AUDIT'
J=dict(status=status,scope='Only fixedVC source0,N younger lower pair age3 to U(0,-1,E), arbitrary middle and past complete8; exact backward literal requirements+k7+count5 current-origin chronology, all initial activations I28/S28. Cap UNKNOWN.',I=Iweight,S=S,labels=len(nodes),queue=len(todo),stats=stats,seconds=time.time()-t0,control=hit,best_queued=[]if not todo else[dict(score=s,depth=d,pose=[*nodes[q]['p'],nodes[q]['h']],source_found=nodes[q]['found'],pending_origin_count=len(nodes[q]['ob']),forbidden_initial=sorted(nodes[q]['bad']),first_packets=nodes[q]['headword'])for s,d,q in heapq.nsmallest(5,todo)],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,FP,KP,Path(__file__).resolve()]})
(D/'U1_VC_young3_full_history.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps({k:v for k,v in J.items()if k not in('control','best_queued')},indent=2))
