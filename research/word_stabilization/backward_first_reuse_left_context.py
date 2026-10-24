"""Backward local first-marked-reuse overapproximation.
Marked inputs in earlier macros prohibit every still-earlier patch read.
Forbidden-past cells need no retained current-color constraint: their initial
black color can be chosen freely, and no earlier macro is allowed to read them.
This is research code pending independent audit; abstract witnesses are not physical.
"""
from collections import deque,defaultdict
from pathlib import Path
import sys,json,time,os
from verify_macro_word import D,rot,check
A=os.environ.get('MACRO_ALPHABET','CUVQB');GOAL=sys.argv[1]if len(sys.argv)>1 else'V';R=int(sys.argv[2])if len(sys.argv)>2 else 2
CAP=int(sys.argv[3])if len(sys.argv)>3 else 1000000
q=tuple(map(int,sys.argv[4:6]))if len(sys.argv)>5 else{'V':(1,2),'U':(0,3),'Q':(-4,-3),'B':(-3,-4)}[GOAL]
P=[(x,y)for x in range(q[0]-R,q[0]+R+1)for y in range(q[1]-R,q[1]+R+1)]
if os.environ.get('PATCH_MODE'):
 mode=os.environ['PATCH_MODE'];P=set(tuple(z['p'])for z in D[GOAL]['trace'])
 if mode=='footprint_plus':P|={(0,0),(0,2),(1,2),(2,0),(2,1)}
 if mode=='cvb5':P={(0,0),(0,2),(1,2),(2,0),(2,1)}
 if mode=='vshape':P={(z['p'][0]+q[0]-1,z['p'][1]+q[1]-2)for z in D['V']['trace']}
 P=sorted(P)
ix={p:i for i,p in enumerate(P)};qb=1<<ix[q]
seam={(0,0),(-1,-1),(0,-1),(1,0)};S={}
for a in A:
 first={}
 for z in D[a]['trace']:first.setdefault(tuple(z['p']),z['c'])
 S[a]={p for p,c in first.items()if c=='L'and p not in seam}if a!='C'else set()
if os.environ.get('FRESH_MARKS'):
 S.update({a:set(map(tuple,p))for a,p in json.load(open(os.environ['FRESH_MARKS'])).items()})
cfree='C'not in A;H=(0,2)if cfree else range(4)
def allowed(px,py,h):return (px+py)%4==0 if cfree else(px+py-h)%2==0
heads=set()
for p in P:
 for a in A:
  for h in H:
   for z in D[a]['trace']:
    dx,dy=rot(z['p'],h);px,py=p[0]-dx,p[1]-dy
    if allowed(px,py,h):heads.add((px,py,h))
allowed_gap={'UU':[0],'UV':[0,1,2],'UQ':[0],'UB':[0],'VU':[0],'VV':[0,1,2],'VQ':[0],'VB':[],'QU':[0],'QV':[0,1,2],'QQ':[],'QB':[],'BU':[0],'BV':[0,1,2],'BQ':[0],'BB':[]}
bad=['CCCCC','CU','CCQ','CCB']+['CCCC'+a for a in'UVQB']
bad += [a+'C'*k+b for a in'UVQB'for b in'UVQB'for k in range(4)if k not in allowed_gap[a+b]]
if os.environ.get('EXTRA_FORBIDDEN'):
 extra=json.load(open(os.environ['EXTRA_FORBIDDEN']))
 bad+=extra.get('forbidden',extra)if isinstance(extra,dict)else extra
bad=sorted(set(w for w in bad if not any(v!=w and v in w for v in bad)))
for w in bad:
 try:check(w)
 except AssertionError:pass
 else:raise AssertionError(('grammar factor feasible',w))
rev=[w[::-1]for w in bad];prefix=sorted({w[:i]for w in rev for i in range(len(w))},key=lambda w:(len(w),w));pi={p:i for i,p in enumerate(prefix)};gtrans={}
for g,p in enumerate(prefix):
 for a in A:
  w=p+a
  gtrans[g,a]=-1 if any(w.endswith(b)for b in rev)else pi[max((z for z in prefix if w.endswith(z)),key=len)]
# A source C cannot be the first macro of a factor stipulated to begin non-C.
# Forget physical/color constraints on its earlier prefix, but require a legal
# reverse-grammar path whose final letter is non-C.
left_good={g for g in range(len(prefix)) if any(gtrans[g,a]>=0 for a in A if a!='C')}
while True:
 new=left_good|{g for g in range(len(prefix)) if any(gtrans[g,a]in left_good for a in A)}
 if new==left_good:break
 left_good=new
heads=sorted(heads);hi={p:i for i,p in enumerate(heads)};OUT=len(heads);incoming=defaultdict(list);empty_predecessors=defaultdict(set);data={}
for sid,(px,py,h)in enumerate(heads):
 for a in A:
  first={};last={};mb=0
  for z in D[a]['trace']:
   dx,dy=rot(z['p'],h);j=ix.get((px+dx,py+dy))
   if j is not None:first.setdefault(1<<j,z['c']=='L');last[1<<j]=z['c']=='L'
  mask=sum(first);pre=sum(b for b,c in first.items()if c);post=sum(b for b,c in last.items()if not c)
  for p in S[a]:
   dx,dy=rot(p,h);j=ix.get((px+dx,py+dy))
   if j is not None:mb|=1<<j
  dx,dy,dh=D[a]['end_pose'];dx,dy=rot((dx,dy),h);to=hi.get((px+dx,py+dy,(h+dh)%4),OUT)
  islastR=bool(mask&qb and post&qb)
  row=(sid,a,mask,pre,post,mb,islastR);incoming[to].append(row);data[sid,a]=row
  ph=(h-dh)%4;dx,dy=rot(D[a]['end_pose'][:2],ph)
  if (px-dx,py-dy,ph)not in hi:empty_predecessors[sid].add(a)
sid=hi[0,0,0];_,_,known,val,_,_,_=data[sid,GOAL];start=(sid,known,val,0,gtrans[0,GOAL])
Q=deque([start]);parent={start:None};beg=time.time();hit=None;processed=0
print('CONFIG',A,GOAL,q,'patch',len(P),'heads',len(heads),'markers',sum(map(len,S.values())),'grammar',len(prefix),flush=True)
while Q:
 s=Q.popleft();sid,known,val,forbid,g=s;processed+=1
 if len(parent)>CAP:print('CAP',len(parent),'pending',len(Q),'seconds',time.time()-beg,flush=True);break
 for old,a,mask,pre,post,mb,islastR in incoming[sid]:
  ng=gtrans[g,a]
  if ng<0 or mask&forbid or (val^post)&known&mask:continue
  if islastR:
   if a!='C' or ng in left_good:hit=(s,old,a);break
   continue
  if mask&qb:continue
  nf=forbid|mb;nk=(known|mask)&~nf;nv=((val&~mask)|pre)&nk;t=(old,nk,nv,nf,ng)
  if t not in parent:parent[t]=(s,a);Q.append(t)
 if hit:break
 if sid==OUT:
  for a in A:
   ng=gtrans[g,a]
   if ng<0:continue
   t=(OUT,known,val,forbid,ng)
   if t not in parent:parent[t]=(s,'OUT'+a);Q.append(t)
 for a in empty_predecessors[sid]:
  ng=gtrans[g,a]
  if ng<0:continue
  t=(OUT,known,val,forbid,ng)
  if t not in parent:parent[t]=(s,'OUT'+a);Q.append(t)
else:print('EXCLUDED',len(parent),'seconds',time.time()-beg,flush=True)
if hit:
 s,old,a=hit;path=[(heads[old],a)]
 while parent[s]is not None:
  after,a=parent[s];path.append(('OUT'if s[0]==OUT else heads[s[0]],a));s=after
 path.append((heads[s[0]],GOAL));print('ABSTRACT WITNESS',len(parent),'seconds',time.time()-beg,path,flush=True)
