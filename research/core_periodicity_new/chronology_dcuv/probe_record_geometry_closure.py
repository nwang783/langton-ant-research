"""Color-free exact pose reachability with protected q and historical-record cuts.
Finite exhausted closure proves the event impossible; caps/witnesses do not.
"""
from pathlib import Path
import json,sys,hashlib,collections,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from resource_profile import load_profile
inv,out=map(Path,sys.argv[1:3]);cap=int(sys.argv[3]);J=json.loads(inv.read_text());P,D,M=load_profile(J['resource_profile_file']);G=D['geometry']['geometry'];F=D['ordinary'];FP=D['protected'];A=J['core_offsets'];T={(a,h):v for a,h,v in J['created_peaks']};direction=J['direction'];keep=P['keep'];contexts=[set(tuple(r[:2])for r in g['requirements'])for g in G]
def rot(q,h):x,y=q;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(q):return sum(a*b for a,b in zip(direction,q))
def bad(a,b,p,h,q):return(a,b,*p,h)in F or(a,b,*p,h,*q)in FP
summary=[];start=time.time()
for index,row in enumerate(J['rows']):
 a0,b,tx,ty,th,qx,qy,phase,S=row;q=(qx,qy);st=tuple(G[a0]['endpoint']);seen={st};Q=collections.deque([st]);hit=False;capped=False
 while Q:
  x,y,h=Q.popleft()
  if (x,y,h)==(tx,ty,th):hit=True;break
  old=2*L(rot((x,y),phase))+A[(h+phase)%4]
  if old>=S:continue
  qq=rot((qx-x,qy-y),-h)
  for a in keep:
   if qq in contexts[a]:continue
   if 2*L(rot((x,y),phase))+T[a,(h+phase)%4]>=S:continue
   if bad(a0,a,(x,y),h,q):continue
   rel=rot((tx-x,ty-y),-h)
   if bad(a,b,rel,(th-h)%4,qq):continue
   ex,ey,dh=G[a]['endpoint'];rx,ry=rot((ex,ey),h);dest=(x+rx,y+ry,(h+dh)%4)
   if dest not in seen:
    seen.add(dest);Q.append(dest)
    if len(seen)>cap:capped=True;break
  if capped:break
 status='ABSTRACT_POSE_PATH'if hit else'CAP'if capped else'EXHAUSTED_NO_HIT';r={'index':index+1,'row':row,'status':status,'states':len(seen)}
 if status=='EXHAUSTED_NO_HIT':r['closed_pose_set']=sorted(seen)
 summary.append(r)
 if index%100==0:print(index+1,dict(collections.Counter(r['status']for r in summary)),round(time.time()-start,1),flush=True)
 if index%100==0:out.write_text(json.dumps({'inventory_file':str(inv.resolve()),'inventory_sha256':hashlib.sha256(inv.read_bytes()).hexdigest(),'cap':cap,'results':summary},separators=(',',':')))
out.write_text(json.dumps({'inventory_file':str(inv.resolve()),'inventory_sha256':hashlib.sha256(inv.read_bytes()).hexdigest(),'cap':cap,'results':summary},separators=(',',':')));print(collections.Counter(r['status']for r in summary),time.time()-start)
