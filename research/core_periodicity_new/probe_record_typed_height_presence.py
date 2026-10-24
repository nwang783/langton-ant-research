"""May-set dataflow for HB-compatible historical producer roles, heights and C-ages.
CLI PETRI_GEOMETRY.json PREFIX [UPDATE_CAP]. A single union per control deliberately
forgets path correlations. No no-hit theorem without independent invariant replay.
"""
from pathlib import Path
from collections import deque
import sys,json,hashlib,time
src,out=map(Path,sys.argv[1:3]);limit=int(sys.argv[3])if len(sys.argv)>3 else 1000000
J=json.loads(src.read_text());S=json.loads(Path(J['source_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];keep=[0,1,4,5,6,7,8,9];F=J['initial_bound'];cap=J['height_cap'];phase=S['phase'];rules_path=Path('chronology_dcuv/counted_input_age_rules_complete.json');rules=json.loads(rules_path.read_text());ages={(a,x,y):r for a,x,y,r in rules};protected_path=Path('chronology_dcuv/protected_patch2.tsv');protected={tuple(map(int,s.split()[:7]))for s in protected_path.read_text().splitlines()if s and not s.startswith('#')}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
roles=[(a,h,tuple(o))for a in keep for h in range(4)for o in G[a]['outputs']];roleid={r:i for i,r in enumerate(roles)};nr=len(roles);allowed={}
for b in keep:
 for hb in range(4):
  for inp in G[b]['inputs']:
   mask=0
   for k,(a,ha,o)in enumerate(roles):
    dh=(hb-ha)%4;u,v=rot(inp,dh);tup=(a,b,o[0]-u,o[1]-v,dh,o[0],o[1])
    if tup not in protected:mask|=1<<k
   allowed[b,hb,tuple(inp)]=mask
poseops={}
for pi,(h,q)in enumerate(J['poses']):
 for a in keep:
  req=[];put=0;c=G[a]['name'].count('C')
  if q is not None:
   for p in G[a]['inputs']:
    lev=q+ht(rot(p,h))
    if lev>F:
     # An input above every permitted producer height can never be supplied.
     mask=0 if lev>cap else allowed[a,h,tuple(p)]<<(nr*(lev-F-1))
     req.append((ages[a,*p],mask))
   for p in G[a]['outputs']:
    lev=q+ht(rot(p,h))
    if F<lev<=cap:put|=1<<(nr*(lev-F-1)+roleid[a,h,tuple(p)])
  poseops[pi,a]=(c,req,put)
np=len(J['positions']);adj=[[]for _ in range(np)]
for ei,(p,q,a,_,_)in enumerate(J['transitions']):adj[p].append((q,a))
V=[None]*np;pending=[False]*np;todo=deque()
for p in J['initial_controls']:V[p]=(0,0,0,0,0);pending[p]=True;todo.append(p)
goal_controls={p for p,_ in J['goal_requirements']};updates=0;pops=0;hit=None;t0=time.time()
def enabled(v,req):
 for age,mask in req:
  if not any(v[j]&mask for j in range(age,5)):return False
 return True
while todo and hit is None:
 p=todo.popleft();pending[p]=False;pops+=1;v=V[p];pi=J['positions'][p][0]
 if p in goal_controls and enabled(v,poseops[pi,S['target']][1]):hit=p;break
 for q,a in adj[p]:
  c,req,put=poseops[pi,a]
  if not enabled(v,req):continue
  w=[0]*5
  for j in range(5):w[min(4,j+c)]|=v[j]
  w[c]|=put
  old=V[q];new=tuple(w)if old is None else tuple(x|y for x,y in zip(old,w))
  if new==old:continue
  V[q]=new;updates+=1
  if not pending[q]:pending[q]=True;todo.append(q)
  if updates>=limit:break
 if updates>=limit:break
 if pops%10000==0:print(json.dumps({'pops':pops,'updates':updates,'queue':len(todo),'seconds':round(time.time()-t0,2)}),flush=True)
status='MAY_GOAL_REACHED'if hit is not None else 'CAP'if todo else 'CLOSED_NO_MAY_GOAL';R={'format':'record_typed_height_may_presence_result_v1','status':status,'source_file':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'protected_file':str(protected_path.resolve()),'protected_sha256':hashlib.sha256(protected_path.read_bytes()).hexdigest(),'rules_file':str(rules_path.resolve()),'rules_sha256':hashlib.sha256(rules_path.read_bytes()).hexdigest(),'producer_roles':roles,'height_levels':J['places'],'updates':updates,'processed_controls':pops,'reached_controls':sum(v is not None for v in V),'goal_control':hit,'seconds':time.time()-t0,'scope':'Historical producer-role/height/C-age may sets, with exact HB input eligibility and deletion ignored. Joins union incompatible histories, so a reached may goal is not a path witness.'};out.with_suffix('.json').write_text(json.dumps(R,indent=2)+'\n')
if status=='CLOSED_NO_MAY_GOAL':out.with_suffix('.invariant.json').write_text(json.dumps([None if v is None else [hex(x)for x in v]for v in V],separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in R.items()if k not in ['producer_roles','height_levels']},indent=2))
