"""Add exact head poses without adding color cells; outer excursions still collapsed.
CLI BASE.json PREFIX MARGIN. Add every sector-compatible head pose in patch bounding box + margin.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
base,out=map(Path,sys.argv[1:3]);margin=int(sys.argv[3]);J=json.loads(base.read_text());P,D,M=load_profile(J['resource_profile_file']);G=D['geometry']['geometry'];F=D['ordinary'];FP=D['protected'];points=list(map(tuple,J['points']));ix={p:i for i,p in enumerate(points)};heads=set(map(tuple,J['poses']));a0,b=J['source'],J['target'];tx,ty,th=J['target_pose'];q=tuple(J['protected_q'])
def rot(z,h):x,y=z;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def forbidden(a,b,p,h,qp):return(a,b,*p,h)in F or(a,b,*p,h,*qp)in FP
for x in range(min(p[0]for p in points)-margin,max(p[0]for p in points)+margin+1):
 for y in range(min(p[1]for p in points)-margin,max(p[1]for p in points)+margin+1):
  for h in range(4):
   if (x+y+h)%2==0:heads.add((x,y,h))
heads=sorted(heads);si={p:i for i,p in enumerate(heads)};OUT=len(heads);T=[];re=set()
for sid,(x,y,h)in enumerate(heads):
 p=(x,y)
 for a in J['keep']:
  g=G[a];e=g['endpoint'];dest=(*add(p,rot(e[:2],h)),(h+e[2])%4);to=si.get(dest,OUT);req={tuple(r[:2]):bool(r[2])for r in g['requirements']};k=v=f=0
  for c,val in req.items():
   i=ix.get(add(p,rot(c,h)))
   if i is not None:k|=1<<i;v|=int(val)<<i
  for c in g['raw_odd']:
   i=ix.get(add(p,rot(c,h)))
   if i is not None:f^=1<<i
  goal=a==b and(x,y,h)==(tx,ty,th);qq=rot(sub(q,p),-h)
  allowed=qq not in req and not forbidden(a0,a,p,h,q)and not forbidden(a,b,rot(sub((tx,ty),p),-h),(th-h)%4,qq)
  if allowed or goal:T.append([sid,to,k,v,f,int(goal),a])
  hh=(h-e[2])%4;pp=sub(p,rot(e[:2],hh))
  if (*pp,hh)not in si:re.add(sid)
e=G[a0]['endpoint'];obj={**J,'poses':heads,'out':OUT,'start':[si.get(tuple(e),OUT),*J['start'][1:]],'transitions':T,'reentry':sorted(re),'pose_expansion':{'base_file':str(base.resolve()),'base_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),'margin':margin,'rule':'all sector-compatible poses in patch bounding rectangle plus margin; preserve original near poses'}}
out.with_suffix('.json').write_text(json.dumps(obj,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{obj['n']} {OUT+1} {len(T)} {len(re)}\n");f.write(' '.join(map(str,obj['start']))+'\n')
 for r in T:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,sorted(re)))+'\n')
print(json.dumps({'poses':OUT,'transitions':len(T),'reentry':len(re)}))
