"""One fixed-history, exact-three-C protected color query. No age threshold run.
Starts immediately after the uniquely possible critical VCC VC D prefix.
"""
from pathlib import Path
import json,collections
R=Path(__file__).resolve().parent;D=R/'chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];ids=(0,1,4,5,6,7,8,9);DIR=((0,1),(1,0),(0,-1),(-1,0))
Pdeny={tuple(map(int,s.split()[:7]))for s in(D/'protected_patch2.tsv').read_text().splitlines()}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def minus(a,b):return(a[0]-b[0],a[1]-b[1])
def trace(w):
 p=(0,0);h=0;req={};last={};odd=set()
 for c in w:
  assert last.get(p)!=c,(w,p,c);req.setdefault(p,c=='L');last[p]=c
  if p in odd:odd.remove(p)
  else:odd.add(p)
  h=(h+(1 if c=='R'else-1))%4;p=plus(p,DIR[h])
 return p,h,req,odd
hist=[6,5,0];word=''.join(G[a]['word']for a in hist);_,_,req,odd=trace(word);_,_,reqctx,_=trace(word+G[0]['marker']);sourcepose=(-1,0);sourceh=1
norm=lambda q:rot(minus(q,sourcepose),-sourceh)
points=sorted(map(norm,reqctx));nb=len(points);assert nb<63;ix={p:i for i,p in enumerate(points)}
startvalue=sum(int(reqctx[q]^(q in odd))<<ix[norm(q)]for q in reqctx)
watch=(2,0);target=(0,1,1);geom={a:trace(G[a]['word'])for a in ids};ctx={a:trace(G[a]['word']+G[a]['marker'])[2]for a in ids}
heads=set()
for a in ids:
 for h in range(4):
  for q in ctx[a]:
   for z in points:
    p=minus(z,rot(q,h))
    if(sum(p)-h)%2==0:heads.add((*p,h))
heads=sorted(heads);hi={p:i for i,p in enumerate(heads)};NH=len(heads)
base=[(*p,)for p in heads]+[None]*4;far={h:NH+h for h in range(4)};Nbase=NH+4
pid=lambda p,c:p*4+c
np=Nbase*4+1;goal=np-1;edges=[];reentry=set()
for hpose,sid in hi.items():
 x,y,h=hpose;p=(x,y)
 for a in ids:
  end,dh,_,rawodd=geom[a];dest=(*plus(p,rot(end,h)),(h+dh)%4);to=hi.get(dest,far[dest[2]])
  K=V=F=0
  for q,v in ctx[a].items():
   j=ix.get(plus(p,rot(q,h)))
   if j is not None:K|=1<<j;V|=int(v)<<j
  for q in rawodd:
   j=ix.get(plus(p,rot(q,h)))
   if j is not None:F^=1<<j
  qq=rot(minus(watch,p),-h);touch=qq in ctx[a]
  targetrel=rot(minus(target[:2],p),-h);dhgoal=(target[2]-h)%4
  blocked=(0,a,*p,h,*watch)in Pdeny or(a,5,*targetrel,dhgoal,*qq)in Pdeny
  cc=G[a]['name'].count('C')
  for c in range(4):
   if a==5 and hpose==target and c==3:edges.append((pid(sid,c),goal,a,0,K,V,F,0,0))
   if not touch and not blocked and c+cc<=3:edges.append((pid(sid,c),pid(to,c+cc),a,0,K,V,F,0,0))
  preh=(h-dh)%4;prep=minus(p,rot(end,preh))
  if(*prep,preh)not in hi:reentry.add(sid)
for h in range(4):
 for c in range(4):
  for a in ids:
   cc=G[a]['name'].count('C')
   if c+cc<=3:edges.append((pid(far[h],c),pid(far[(h-cc)%4],c+cc),a,0,0,0,0,0,0))
  for sid in reentry:
   if heads[sid][2]==h:edges.append((pid(far[h],c),pid(sid,c),99,0,0,0,0,0,0))
startbase=hi.get((1,1,0),far[0]);out=D/'vcc_d_vc_joint_patch';out.mkdir(exist_ok=True)
with(out/'model.dat').open('w')as f:
 f.write(f'COLOROPS 0 {np} {len(edges)} 1 1 1 {nb}\n{pid(startbase,0)} {(1<<nb)-1} {startvalue}\n{goal}\n0\n')
 for e in edges:f.write(' '.join(map(str,e))+'\n')
J={'scope':'Guarded XOR patch relaxation after fixed literal VCC VC D history; source D output(2,0) protected; goal VC at(0,1,1), exact intervening Ccount3; far positions conservatively forgotten with heading retained.','points':points,'heads':heads,'Nbase':Nbase,'start':[pid(startbase,0),(1<<nb)-1,startvalue],'goal':goal,'edges':edges,'history':hist,'normalized_source_pose':[*sourcepose,sourceh],'target':target,'watch':watch,'C_count':3}
(out/'model.json').write_text(json.dumps(J,separators=(',',':'))+'\n');print({'bits':nb,'near_heads':NH,'controls':np,'edges':len(edges),'reentry':len(reentry)})
