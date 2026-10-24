"""Prepare a finite anchored-patch overapproximation; only no-hit exhaustion proves exclusion."""
import json,sys
from pathlib import Path
from resource_profile import load_profile
profile,data,profile_meta=load_profile(sys.argv.pop(1));OUT=Path('.')
M=data['macro_words']['macro_words'];F=data['ordinary'];FP=data['protected'];D=((0,1),(1,0),(0,-1),(-1,0));keep=profile['keep']
# CLI: SOURCE TARGET X Y H QX QY PREFIX [source|both|radiusN]
assert len(sys.argv)>=9, 'PROFILE SOURCE TARGET X Y H QX QY PREFIX [patch mode]'
source,target,tx,ty,th,qx,qy=map(int,sys.argv[1:8]);tp=(tx,ty);q=(qx,qy);prefix=sys.argv[8]
assert source in keep and target in keep
assert (tx+ty-th)%2==0, 'target pose is outside the source checkerboard sector'

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def rot(a,h):
 x,y=a
 return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def tr(w):
 p=(0,0);h=0;first={};last={};odd=set()
 for c in w:
  first.setdefault(p,c=='L');assert last.get(p)!=c;last[p]=c
  if p in odd:odd.remove(p)
  else:odd.add(p)
  h=(h+(1 if c=='R'else-1))%4;p=add(p,D[h])
 return p,h,first,odd
G=[]
for a in M:
 e,h,_,odd=tr(a['word']);req=tr(a['word']+a['end_marker'])[2];G.append((e,h,req,odd))
mode=sys.argv[9]if len(sys.argv)>9 else'source'
S=G[source][2];P=set(S)
if mode=='both' or mode.startswith('bothplus:'):P|={add(tp,rot(c,th))for c in G[target][2]}
if mode.startswith('mask'):
 mask=int(mode[4:],16);P={v for i,v in enumerate(sorted(S))if mask>>i&1}
if mode.startswith('radius'):
 r=int(mode[6:]);P={(x,y)for x in range(q[0]-r,q[0]+r+1)for y in range(q[1]-r,q[1]+r+1)}
if mode.startswith('sourceplus:') or mode.startswith('bothplus:'):
 P|={tuple(p)for p in json.loads(Path(mode.split(':',1)[1]).read_text())}
P=sorted(P);ix={p:i for i,p in enumerate(P)};n=len(P)
heads=set()
for a in keep:
 e,dh,req,odd=G[a]
 for h in range(4):
  for c in req:
   for p in P:
    v=sub(p,rot(c,h))
    if (sum(v)+h)%2==0:heads.add((*v,h))
heads=sorted(heads);si={v:i for i,v in enumerate(heads)};out=len(heads)

def forbidden(a,b,p,h,qp):return (a,b,*p,h)in F or(a,b,*p,h,*qp)in FP
T=[];reentry=set()
for sid,(x,y,h)in enumerate(heads):
 p=(x,y)
 for a in keep:
  e,dh,req,odd=G[a];dest=(*add(p,rot(e,h)),(h+dh)%4);to=si.get(dest,out);known=val=flip=0
  for c,v in req.items():
   j=ix.get(add(p,rot(c,h)))
   if j is not None:known|=1<<j;val|=int(v)<<j
  for c in odd:
   j=ix.get(add(p,rot(c,h)))
   if j is not None:flip^=1<<j
  isgoal=(a==target and p==tp and h==th)
  qq=rot(sub(q,p),-h)
  allowed=(qq not in req and not forbidden(source,a,p,h,q) and not forbidden(a,target,rot(sub(tp,p),-h),(th-h)%4,qq))
  if allowed or isgoal:T.append([sid,to,known,val,flip,int(isgoal),a])
  hh=(h-dh)%4;pp=sub(p,rot(e,hh))
  if (*pp,hh)not in si:reentry.add(sid)
e,dh,req,odd=G[source];known=val=0
for c,v in req.items():
 j=ix.get(c)
 if j is not None:known|=1<<j;val|=int(v^(c in odd))<<j
obj={'mode':mode,'n':n,'points':P,'poses':heads,'out':out,'start':[si.get((*e,dh),out),known,val],'transitions':T,'reentry':sorted(reentry),'keep':keep,'source':source,'target':target,'target_pose':[*tp,th],'protected_q':q,'scope':'abstract only unless exhaustive no-hit; q protected; source and target signed pair guards'}
obj.update(profile_meta)
(OUT/f'{prefix}.json').write_text(json.dumps(obj,separators=(',',':')))
with(OUT/f'{prefix}.dat').open('w')as f:
 f.write(f'{n} {len(heads)+1} {len(T)} {len(reentry)}\n');f.write(' '.join(map(str,obj['start']))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write(' '.join(map(str,sorted(reentry)))+'\n')
print({k:obj[k]for k in['mode','n','out','start']},'transitions',len(T),'reentry',len(reentry))
