"""Conditional potential discovery: fixed max-policy MILP, exact checker required."""
from pathlib import Path
import json,sys,math,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
P=Path(__file__).resolve().parents[1]/'core_periodicity_new/chronology_dcuv';f=Path(sys.argv[1]);pref=Path(sys.argv[2]);limit=float(sys.argv[3])if len(sys.argv)>3 else 90
m=json.loads(f.read_text());v=m['values'];names=[k for k in v if k not in ['ax','ay']];N={n:i for i,n in enumerate(names)};G=json.loads((P/'literal_residual_geometry.json').read_text())['geometry'];inv=json.loads((P/'transfer_inventory.json').read_text());rows=inv['protected_survivors'];n=len(names);d=(v['ax'],v['ay']);B=max(100,max(abs(v[k])for k in names)+20);M=2*B
ri=[];ci=[];da=[];ub=[]
def add(terms,b):
 z=len(ub);ub.append(b)
 for c,a in terms.items():ri.append(z);ci.append(c);da.append(a)
def difference(lhs,rhs,b,relax=None):
 t={N[lhs]:1.0};t[N[rhs]]=t.get(N[rhs],0)-1
 if relax is not None:t[relax]=-M
 add(t,b)
def r(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(z):return d[0]*z[0]+d[1]*z[1]
policy=[]
for a,g in enumerate(G):
 for h in range(4):
  anchor=L(r((-1,1),h));old=[(f'c{h}',0)]+[(f'u_{a}_{k}_{h}',2*L(r(p,h))-anchor)for k,p in enumerate(g['inputs'])];e=g['endpoint'];new=[(f'c{(h+e[2])%4}',2*L(r(e[:2],h))+L(r((-1,1),h+e[2]))-anchor)]+[(f'w_{a}_{k}_{h}',2*L(r(p,h))-anchor)for k,p in enumerate(g['outputs'])];choice=max(range(len(old)),key=lambda k:v[old[k][0]]+old[k][1]);ov,oc=old[choice];policy.append([a,h,choice])
  for nv,nc in new:difference(nv,ov,oc-nc)
by={tuple(e['tuple']):e for e in inv['ordinary_survivors']}
for line in Path(m['observed_file']).read_text().splitlines():
 e=by[tuple(map(int,line.split()))];a,b,x,y,dh,*q=e['tuple'];k=e['source_output_slot'];j=e['target_input_slot']
 for h in range(4):difference(f'u_{b}_{j}_{(h+dh)%4}',f'w_{a}_{k}_{h}',0)
for z,e in enumerate(rows):
 a,b,x,y,dh,*q=e['tuple'];k=e['source_output_slot'];j=e['target_input_slot']
 for h in range(4):difference(f'u_{b}_{j}_{(h+dh)%4}',f'w_{a}_{k}_{h}',0,n+z)
mat=coo_matrix((da,(ri,ci)),shape=(len(ub),n+len(rows))).tocsc();lower=np.r_[np.full(n,-B),np.zeros(len(rows))];upper=np.r_[np.full(n,B),np.ones(len(rows))];lower[N['c0']]=upper[N['c0']]=0;c=np.r_[np.zeros(n),np.ones(len(rows))];t=time.time();res=milp(c,integrality=np.r_[np.zeros(n),np.ones(len(rows))],bounds=Bounds(lower,upper),constraints=LinearConstraint(mat,-np.inf,ub),options={'time_limit':limit,'mip_rel_gap':0.01})
out={k:m[k]for k in ['observed_file','observed_sha256','profile_sha256']};out.update(status='conditional MILP discovery; exact replay required',parent=str(f),direction=d,policy=policy,bound=B,milp_status=int(res.status),message=res.message,seconds=time.time()-t)
if res.x is not None:
 out['objective']=float(res.fun);out['gap']=float(res.mip_gap);out['dual_bound']=float(res.mip_dual_bound);out['values']={name:math.floor(float(res.x[i])+1e-6)for name,i in N.items()};out['values'].update(ax=d[0],ay=d[1])
pref.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:x for k,x in out.items()if k not in['values','policy']},indent=2),flush=True)
