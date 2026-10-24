"""One finite MAY pilot, reusing the existing typed-height dataflow.
Adds already signed cap5 role eligibility, KV minima and boundary-height min4.
Union joins and deletion forgetting remain: a MAY goal is NOT a path witness.
No larger ant-search cap or new geometric model is introduced.
CLI PETRI_GEOMETRY.json PREFIX [UPDATE_CAP]
"""
from pathlib import Path
from collections import deque
import sys,json,hashlib,time
src,out=map(Path,sys.argv[1:3]);limit=int(sys.argv[3])if len(sys.argv)>3 else 1000000
J=json.loads(src.read_text());S=json.loads(Path(J['source_file']).read_text());W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];keep=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(keep)};F=J['initial_bound'];cap=J['height_cap'];phase=S['phase'];HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';protected={tuple(map(int,s.split()[:7]))for s in HP.read_text().splitlines()};counted={tuple(map(int,s.split()[:8]))for s in CP.read_text().splitlines()}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
def age_min(a,p):
 if a in[0,1]:return 3
 if a==6 or (a in[7,8,9]and p in[[-1,4],[0,2],[0,3]]):return 5
 return 2 if a in[4,5]and p==[0,3]else 3
roles=[(a,h,tuple(o))for a in keep for h in range(4)for o in G[a]['outputs']];rid={r:i for i,r in enumerate(roles)};nr=len(roles);allowed={}
for b in keep:
 for hb in range(4):
  for inp in G[b]['inputs']:
   masks=[0]*6
   for k,(a,ha,o)in enumerate(roles):
    dh=(hb-ha)%4;u,v=rot(inp,dh);x,y=o[0]-u,o[1]-v;key=(a,b,x,y,dh,*o)
    if (x+y+dh)%2 or key in protected:continue
    for n in range(6):
     if n<5 and(hb-ha+n)%4:continue
     if(mp[a],mp[b],x,y,dh,*o,n)not in counted:masks[n]|=1<<k
   allowed[b,hb,tuple(inp)]=masks
poseops={};guarded=0
# Boundary-height theorem is specialized to H=y-x (global phase1).
assert phase==1
kappa=[4,4,-4,-2]
for pi,(h,q)in enumerate(J['poses']):
 for a in keep:
  req=[];put=0;c=G[a]['name'].count('C')
  if q is not None:
   for p in G[a]['inputs']:
    lev=q+ht(rot(p,h))
    if lev>F:
     mn=age_min(a,p)
     if a in[7,8,9]and p in[[-1,1],[-1,2]]and q>F-kappa[h]:mn=4;guarded+=1
     masks=allowed[a,h,tuple(p)]
     req.append(tuple((masks[n]<<(nr*(lev-F-1)))if lev<=cap and(n==5 or n>=mn)else 0 for n in range(6)))
   for p in G[a]['outputs']:
    lev=q+ht(rot(p,h))
    if F<lev<=cap:put|=1<<(nr*(lev-F-1)+rid[a,h,tuple(p)])
  poseops[pi,a]=(c,req,put)
np=len(J['positions']);adj=[[]for _ in range(np)]
for p,q,a,_,_ in J['transitions']:adj[p].append((q,a))
V=[None]*np;pending=[False]*np;todo=deque()
for p in J['initial_controls']:V[p]=(0,)*6;pending[p]=True;todo.append(p)
goals={p for p,_ in J['goal_requirements']};updates=pops=0;hit=None;t0=time.time()
def enabled(v,req):return all(any(v[n]&m[n]for n in range(6))for m in req)
while todo and hit is None:
 p=todo.popleft();pending[p]=False;pops+=1;v=V[p];pi=J['positions'][p][0]
 if p in goals and enabled(v,poseops[pi,S['target']][1]):hit=p;break
 for q,a in adj[p]:
  c,req,put=poseops[pi,a]
  if not enabled(v,req):continue
  w=[0]*6
  for j in range(6):w[min(5,j+c)]|=v[j]
  w[c]|=put;old=V[q];new=tuple(w)if old is None else tuple(x|y for x,y in zip(old,w))
  if new==old:continue
  V[q]=new;updates+=1
  if not pending[q]:pending[q]=True;todo.append(q)
  if updates>=limit:break
 if updates>=limit:break
status='MAY_GOAL_REACHED'if hit is not None else'CAP'if todo else'CLOSED_NO_MAY_GOAL';R=dict(status=status,source_file=str(src.resolve()),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),producer_roles=nr,height_levels=J['places'],age_classes='0..4 exact,5 overflow',updates=updates,processed_controls=pops,reached_controls=sum(v is not None for v in V),goal_control=hit,seconds=time.time()-t0,guarded_U_lower_pose_slots=guarded,scope='One finite historical producer-role/height/C-age MAY pilot; deletion and path correlation forgotten. Reaching a may goal is NOT a path witness or physical counterexample.',dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,W/'boundary_origin_height_guard_frozen_20261023_1258/manifest.json',Path(__file__).resolve()]});out.with_suffix('.json').write_text(json.dumps(R,indent=2)+'\n')
if status=='CLOSED_NO_MAY_GOAL':out.with_suffix('.invariant.json').write_text(json.dumps([None if v is None else[hex(x)for x in v]for v in V],separators=(',',':'))+'\n')
print(json.dumps(R,indent=2))
