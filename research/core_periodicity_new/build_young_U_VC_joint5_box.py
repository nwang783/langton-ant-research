"""One exact-two-C VC young-lower-pair query, with all five target inputs protected.
Sound convex exterior relaxation, no packet/space/mass cutoff theorem.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;D=R/'chronology_dcuv';GP=D/'literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];ids=(0,1,4,5,6,7,8,9);DIR=((0,1),(1,0),(0,-1),(-1,0))
RP=D/'delayed_height_probe/u1_residue_cegar/root_out.json';RJ=json.loads(RP.read_text());T={(a,h):t for a,h,t in RJ['created_peaks']};A=RJ['core_offsets'];assert A==[0,22,20,10]
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[0],a[1]-b[1]
def trace(w):
 p=(0,0);h=0;req={};last={};odd=set()
 for c in w:
  assert last.get(p)!=c,(p,c);req.setdefault(p,c=='L');last[p]=c
  if p in odd:odd.remove(p)
  else:odd.add(p)
  h=(h+(1 if c=='R'else-1))%4;p=plus(p,DIR[h])
 return p,h,req,odd
source=5;target=7;goalpose=(0,-1,1);end,eh,_,odd=trace(G[source]['word']);assert(end,eh)==((1,4),3)
_,_,sourcectx,_=trace(G[source]['word']+G[source]['marker']);P={plus(goalpose[:2],rot(q,goalpose[2]))for q in G[target]['inputs']};assert P=={(1,0),(2,0),(4,0),(2,-1),(3,-1)}
upper={(4,0),(2,-1),(3,-1)};assert upper.isdisjoint(sourcectx)
startcolors={q:v^(q in odd)for q,v in sourcectx.items()};startcolors.update({q:True for q in upper});assert all(startcolors[q]for q in P)
points=sorted(startcolors);nb=len(points);assert nb<63;ix={p:i for i,p in enumerate(points)};startvalue=sum(int(v)<<ix[q]for q,v in startcolors.items());geom={a:trace(G[a]['word'])for a in ids};ctx={a:trace(G[a]['word']+G[a]['marker'])[2]for a in ids}
sensitive=set()
for a in ids:
 for h in range(4):
  for q in ctx[a]:
   for z in points:
    p=minus(z,rot(q,h))
    if(sum(p)-h)%2==0:sensitive.add((*p,h))
xmin=min(p[0]for p in sensitive);xmax=max(p[0]for p in sensitive);ymin=min(p[1]for p in sensitive);ymax=max(p[1]for p in sensitive)
heads=sorted((x,y,h)for x in range(xmin,xmax+1)for y in range(ymin,ymax+1)for h in range(4)if(x+y-h)%2==0);hi={p:i for i,p in enumerate(heads)};NH=len(heads);far={(h,flag):NH+2*h+flag for h in range(4)for flag in range(2)};Nbase=NH+8;NC=3;pid=lambda p,c:p*NC+c;np=Nbase*NC+1;goal=np-1;edges=[];reentry=set();deleted_record=0;S=28
for hpose,sid in hi.items():
 x,y,h=hpose;p=(x,y)
 for a in ids:
  e,dh,_,rawodd=geom[a];dest=(*plus(p,rot(e,h)),(h+dh)%4);cc=G[a]['name'].count('C');to=hi.get(dest,far[dest[2],int(cc>0)])
  K=V=F=0
  for q,v in ctx[a].items():
   j=ix.get(plus(p,rot(q,h)))
   if j is not None:K|=1<<j;V|=int(v)<<j
  for q in rawodd:
   j=ix.get(plus(p,rot(q,h)))
   if j is not None:F^=1<<j
  touch=any(rot(minus(q,p),-h)in ctx[a]for q in P)
  record_ok=2*sum(p)+max(A[h],T[a,h])<S
  if not record_ok:deleted_record+=1
  for c in range(NC):
   if a==target and hpose==goalpose and c==2:edges.append((pid(sid,c),goal,a,0,K,V,F,0,0))
   if not touch and record_ok and c+cc<=2:edges.append((pid(sid,c),pid(to,c+cc),a,0,K,V,F,0,0))
  preh=(h-dh)%4;prep=minus(p,rot(e,preh))
  if(*prep,preh)not in hi:reentry.add(sid)
for h in range(4):
 for flag in range(2):
  for c in range(NC):
   for a in ids:
    cc=G[a]['name'].count('C')
    if cc and c+cc<=2:edges.append((pid(far[h,flag],c),pid(far[(h-cc)%4,1],c+cc),a,0,0,0,0,0,0))
   if flag:
    for sid in reentry:
     if heads[sid][2]==h:edges.append((pid(far[h,flag],c),pid(sid,c),99,0,0,0,0,0,0))
startbase=hi[(*end,eh)];out=D/'young_U_VC_joint5_box';out.mkdir(exist_ok=True)
with(out/'model.dat').open('w')as f:
 f.write(f'COLOROPS 0 {np} {len(edges)} 1 1 1 {nb}\n{pid(startbase,0)} {(1<<nb)-1} {startvalue}\n{goal}\n0\n')
 for e in edges:f.write(' '.join(map(str,e))+'\n')
J=dict(scope='Only sourceVC0,N lower outputs(1,0),(2,0) consumed by U at(0,-1,E), exactsourceage3, strict2C. All5 target identities protected; upper3 predate source. Strict near packets obey full-recordscore<28; far ignores score conservatively.',points=points,heads=heads,Nbase=Nbase,start=[pid(startbase,0),(1<<nb)-1,startvalue],goal=goal,edges=edges,source=source,target=target,target_pose=goalpose,protected_points=sorted(P),older_upper_points=sorted(upper),C_count=2,head_box=[xmin,xmax,ymin,ymax],record_threshold=S,core_offsets=A,created_peaks=RJ['created_peaks'],far_flag_semantics='Any outside start misses patch. A zero-C-caused exit cannot reenter before a positive-C packet by convex-box oriented monotonicity. Positive-C exit/far edges permit arbitrary conservative reentry in matching heading/count; colors unchanged.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,Path(__file__).resolve()]})
(out/'model.json').write_text(json.dumps(J,separators=(',',':'))+'\n');print(dict(bits=nb,near_heads=NH,controls=np,edges=len(edges),record_deleted_packet_heads=deleted_record,box=J['head_box']))
