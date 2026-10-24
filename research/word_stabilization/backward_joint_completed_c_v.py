"""Backward first-marked-reuse with unconditional C-free run-local guards.
The local mask clears before crossing C; its color constraints do not clear.
Marked inputs in earlier macros prohibit every still-earlier patch read.
Forbidden-past cells need no retained current-color constraint: their initial
black color can be chosen freely, and no earlier macro is allowed to read them.
This is research code pending independent audit; abstract witnesses are not physical.
"""
from collections import deque,defaultdict
from pathlib import Path
import sys,json,time,os
from verify_macro_word import D,rot,check
PACKET=os.environ.get('TARGET_PACKET','VCV')
assert PACKET=='V'or(PACKET[0]in'UVQB'and PACKET[1:]in('CV','CCV'))
check(PACKET)
pp=(0,0);hh=0;tr=[];vmarks=[];q=(1,2)if PACKET=='V'else None
for jj,a in enumerate(PACKET):
 if jj==1:
  dx,dy=rot((-1,0),hh);q=pp[0]+dx,pp[1]+dy
 if a=='V':
  dx,dy=rot((1,2),hh);vmarks.append((pp[0]+dx,pp[1]+dy))
 for z in D[a]['trace']:
  dx,dy=rot(z['p'],hh);tr.append({'i':len(tr),'p':[pp[0]+dx,pp[1]+dy],'h':(hh+z['h'])%4,'c':z['c']})
 dx,dy,dh=D[a]['end_pose'];dx,dy=rot((dx,dy),hh);pp=pp[0]+dx,pp[1]+dy;hh=(hh+dh)%4
D['T']={'trace':tr,'word':''.join(D[a]['word']for a in PACKET),'end_pose':[*pp,hh]}
assert PACKET=='V'or not any(tuple(z['p'])==q for z in D[PACKET[0]]['trace'])
A='CUVQBT';HISTORY='CUVQB';GOAL='T'
R=int(sys.argv[1])if len(sys.argv)>1 else 2
CAP=int(sys.argv[2])if len(sys.argv)>2 else 1000000
P=[(x,y)for x in range(q[0]-R,q[0]+R+1)for y in range(q[1]-R,q[1]+R+1)]
if os.environ.get('PATCH_MODE'):
 mode=os.environ['PATCH_MODE'];P=set(tuple(z['p'])for z in D[GOAL]['trace'])
 if mode=='footprint_plus':P|={(0,0),(0,2),(1,2),(2,0),(2,1)}
 if mode=='cvb5':P={(0,0),(0,2),(1,2),(2,0),(2,1)}
 if mode=='vshape':P={(z['p'][0]+q[0]-1,z['p'][1]+q[1]-2)for z in D['V']['trace']}
 if mode=='ufoot':P={tuple(z['p'])for z in D['U']['trace']}
 P=sorted(P)
ix={p:i for i,p in enumerate(P)};qb=1<<ix[q]
seam={(0,0),(-1,-1),(0,-1),(1,0)};S={}
for a in A:
 first={}
 for z in D[a]['trace']:first.setdefault(tuple(z['p']),z['c'])
 S[a]={(1,2)}if a=='V'else set()
if os.environ.get('FRESH_MARKS'):
 S.update({a:set(map(tuple,p))for a,p in json.load(open(os.environ['FRESH_MARKS'])).items()})
LOCAL={a:set(map(tuple,ps)) for a,ps in json.load(open(Path(__file__).with_name('cfree_kernel_current_marks.json'))).items()};LOCAL['C']=set()
LOCAL['T']=set(LOCAL[PACKET[0]])
VMARKS_T=set(vmarks)if PACKET[0]in'VB'else set()
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
left_good={g for g in range(len(prefix)) if any(gtrans[g,a]>=0 for a in HISTORY if a!='C')}
while True:
 new=left_good|{g for g in range(len(prefix)) if any(gtrans[g,a]in left_good for a in HISTORY)}
 if new==left_good:break
 left_good=new
# The finite sensitive-head box contains every pose that can read the patch.
# Beyond it, retain coordinate interval classes instead of an arbitrary OUT.
# Singleton interior classes are exact; the four infinite coordinate rays are
# translated by each macro displacement and intersected with the classes.
xmin=min(p[0]for p in heads);xmax=max(p[0]for p in heads)
ymin=min(p[1]for p in heads);ymax=max(p[1]for p in heads)
def exterior(x,y):return x<xmin or x>xmax or y<ymin or y>ymax
def shift_interval(v,d,lo,hi):
 if lo<=v<=hi:return [max(lo-1,min(hi+1,v+d))]
 if v==lo-1:
  end=lo-1+d
  return [lo-1]+list(range(lo,min(hi,end)+1))+([hi+1]if end>hi else[])
 assert v==hi+1
 start=hi+1+d
 return ([lo-1]if start<lo else[])+list(range(max(lo,start),hi+1))+[hi+1]
heads=[(x,y,h)for x in range(xmin-1,xmax+2)for y in range(ymin-1,ymax+2)for h in H if exterior(x,y)or allowed(x,y,h)]
hi={p:i for i,p in enumerate(heads)};OUT=len(heads);incoming=defaultdict(list);empty_predecessors=defaultdict(set);data={}
print('INTERVAL BOX',xmin,xmax,ymin,ymax,'abstract poses',len(heads),flush=True)
for sid,(px,py,h)in enumerate(heads):
 for a in A:
  first={};last={};mb=0;lb=0;vb=0;cb=0
  for z in ([]if exterior(px,py)else D[a]['trace']):
   dx,dy=rot(z['p'],h);j=ix.get((px+dx,py+dy))
   if j is not None:first.setdefault(1<<j,z['c']=='L');last[1<<j]=z['c']=='L'
  mask=sum(first);pre=sum(b for b,c in first.items()if c);post=sum(b for b,c in last.items()if not c)
  for p in ([]if exterior(px,py)else S[a]):
   dx,dy=rot(p,h);j=ix.get((px+dx,py+dy))
   if j is not None:mb|=1<<j
  for p in ([]if exterior(px,py)else LOCAL[a]):
   dx,dy=rot(p,h);j=ix.get((px+dx,py+dy))
   if j is not None:lb|=1<<j
  for p in ([]if exterior(px,py)else [(1,2)]if a=='V'else VMARKS_T if a=='T'else[]):
   dx,dy=rot(p,h);j=ix.get((px+dx,py+dy))
   if j is not None:vb|=1<<j
  if a=='C'and not exterior(px,py):
   dx,dy=rot((-1,0),h);j=ix.get((px+dx,py+dy))
   if j is not None:cb=1<<j
  dx,dy,dh=D[a]['end_pose'];dx,dy=rot((dx,dy),h);nh=(h+dh)%4
  tos=[hi[x,y,nh]for x in shift_interval(px,dx,xmin,xmax)for y in shift_interval(py,dy,ymin,ymax)if (x,y,nh)in hi]
  islastR=bool(mask&qb and post&qb)
  row=(sid,a,mask,pre,post,mb,lb,vb,cb,islastR);data[sid,a]=row
  for to in tos:incoming[to].append(row)
  ph=(h-dh)%4;dx,dy=rot(D[a]['end_pose'][:2],ph)
  assert not empty_predecessors
sid=hi[0,0,0];_,_,known,val,_,_,local,vlocal,_,_=data[sid,GOAL]
g0=0
for a in PACKET[::-1]:g0=gtrans[g0,a];assert g0>=0
gf=(1<<ix[(1,2)])if PACKET!='V'and PACKET[0]=='V'and(1,2)in ix else 0
start=(sid,known&~gf,val&~gf,gf,local&~gf,vlocal&~gf,0,g0)
# For a source C, replay the entire immediately preceding C run and its
# first non-C predecessor. This is necessary because the factor starts non-C.
# Earlier history of that predecessor is safely forgotten.
def prefix_exists(start):
 queue=[start];seen={start}
 while queue:
  sid,known,val,forbid,local,vlocal,pending,g=queue.pop()
  for old,a,mask,pre,post,mb,lb,vb,cb,islastR in incoming[sid]:
   if a not in HISTORY:continue
   ng=gtrans[g,a]
   if ng<0:continue
   af=forbid if a=='C'else forbid|pending
   al=0 if a=='C' else local
   av=0 if a in'UQ' else vlocal
   if mask&(af|al|av) or (val^post)&known&mask:continue
   if a!='C':return True
   nk=(known|mask)&~af;nv=((val&~mask)|pre)&nk
   t=(old,nk,nv,af,0,av,cb,ng)
   if t not in seen:seen.add(t);queue.append(t)
  opts=[(a,(sid-OUT-D[a]['end_pose'][2])%4)for a in HISTORY]if sid>=OUT else list(empty_predecessors[sid])
  for a,ph in opts:
   if a not in HISTORY:continue
   ng=gtrans[g,a]
   if ng<0:continue
   if a!='C':return True
   t=(OUT+ph,known,val,forbid,0,vlocal,0,ng)
   if t not in seen:seen.add(t);queue.append(t)
 return False
Q=deque([start]);parent={start:None};beg=time.time();hit=None;processed=0
print('CONFIG',A,PACKET,q,'patch',len(P),'heads',len(heads),'markers',sum(map(len,S.values())),'grammar',len(prefix),flush=True)
while Q:
 s=Q.popleft();sid,known,val,forbid,local,vlocal,pending,g=s;processed+=1
 if len(parent)>CAP:print('CAP',len(parent),'pending',len(Q),'seconds',time.time()-beg,flush=True);break
 for old,a,mask,pre,post,mb,lb,vb,cb,islastR in incoming[sid]:
  if a not in HISTORY:continue
  ng=gtrans[g,a]
  af=forbid if a=='C'else forbid|pending
  active_local=0 if a=='C' else local
  active_vlocal=0 if a in'UQ' else vlocal
  if ng<0 or mask&(af|active_local|active_vlocal) or (val^post)&known&mask:continue
  if islastR:
   nk=(known|mask)&~af;nv=((val&~mask)|pre)&nk
   before=(old,nk,nv,af,active_local,active_vlocal,cb if a=='C'else 0,ng)
   if a!='C' or (ng in left_good and prefix_exists(before)):hit=(s,old,a);break
   continue
  if mask&qb:continue
  nf=af|mb;nl=(active_local|lb)&~nf;nk=(known|mask)&~nf;nv=((val&~mask)|pre)&nk;t=(old,nk,nv,nf,nl,(active_vlocal|vb)&~nf,cb if a=='C'else 0,ng)
  if t not in parent:parent[t]=(s,a);Q.append(t)
 if hit:break
 if sid>=OUT:
  for a in HISTORY:
   ng=gtrans[g,a]
   if ng<0:continue
   ph=(sid-OUT-D[a]['end_pose'][2])%4
   nf=forbid if a=='C'else forbid|pending
   t=(OUT+ph,known&~nf,val&~nf,nf,0 if a=='C' else local,0 if a in'UQ' else vlocal,0,ng)
   if t not in parent:parent[t]=(s,'OUT'+a);Q.append(t)
 for a,ph in empty_predecessors[sid]:
  if a not in HISTORY:continue
  ng=gtrans[g,a]
  if ng<0:continue
  nf=forbid if a=='C'else forbid|pending
  t=(OUT+ph,known&~nf,val&~nf,nf,0 if a=='C' else local,0 if a in'UQ' else vlocal,0,ng)
  if t not in parent:parent[t]=(s,'OUT'+a);Q.append(t)
else:print('EXCLUDED',len(parent),'seconds',time.time()-beg,flush=True)
if hit:
 s,old,a=hit;path=[(heads[old],a)]
 while parent[s]is not None:
  after,a=parent[s];path.append(('OUT'+str(s[0]-OUT)if s[0]>=OUT else heads[s[0]],a));s=after
 path.append((heads[s[0]],GOAL));print('ABSTRACT WITNESS',len(parent),'seconds',time.time()-beg,path,flush=True)
