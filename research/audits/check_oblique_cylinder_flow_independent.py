"""Independent event-outgoing incidence reconstruction and exact dual arithmetic.
No SciPy, optimization call, author incidence generator or author wake inventory.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,hashlib
R=Path(__file__).resolve().parents[1];D=R/'causal_reduction/unit_scale';H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
p=0j;h=1;hist=defaultdict(list)
for t,c in enumerate(H):
 x,y=int(p.real),int(p.imag);e=x%2;k=(x-e)//2;hist[x-y,e].append((t-104*k,c));h*=(-1j if c=='R'else 1j);p+=h
assert(p,h)==(2+2j,1)
wake=set()
for key,ts in hist.items():
 ts.sort();assert ts[0][1]=='R'and all(a[1]!=b[1]for a,b in zip(ts,ts[1:]));
 if len(ts)%2:wake.add(key)
assert len(wake)==12
vec=(1j,1,-1j,-1)
def xy(z):return int(z.real),int(z.imag)
def rep(z):x,y=xy(z);return complex(x%2,y-x+x%2)
results=[]
for height,off in[(4,-2),(13,-4)]:
 path=D/f'wake_return_flow_bounds_h{height}_off{off}.json';J=json.loads(path.read_bytes());positions=[complex(x,x+y+off)for y in range(height)for x in range(2)];index={p:i for i,p in enumerate(positions)}
 assert J['positions']==[list(xy(p))for p in positions]and J['sector']==1
 keys=[(i,h,s)for i,p in enumerate(positions)for h in range(4)if(sum(xy(p))+h)%2==1 for s in(1,-1)]
 num=len(keys);size=num+len(positions);rows={};rhs={}
 for i,p in enumerate(positions):
  rows[f'color{i}']=[0]*size;rhs[f'color{i}']=-int((int(p.real-p.imag),int(p.real)%2)in wake)
  rows[f'color{i}'][num+i]=-1
  for h in range(4):
   if(sum(xy(p))+h)%2==1:rows[f'edge{i}_{h}']=[0]*size;rhs[f'edge{i}_{h}']=0
  for h in range(4):
   if(sum(xy(p))+h)%2==0 and rep(p+vec[h])not in index:rows[f'exit{i}_{h}']=[0]*size;rhs[f'exit{i}_{h}']=0
 for ax in range(2):rows[f'displacement{ax}']=[0]*size;rhs[f'displacement{ax}']=-2
 for j,(i,h,s)in enumerate(keys):
  q=positions[i];hh=(h+s)%4;v=vec[hh];dest=index.get(rep(q+v))
  rows[f'color{i}'][j]=s;rows[f'edge{i}_{h}'][j]+=1
  if dest is None:rows[f'exit{i}_{hh}'][j]+=1
  else:rows[f'edge{dest}_{hh}'][j]-=1
  for ax in range(2):rows[f'displacement{ax}'][j]=xy(v)[ax]
 assert list(rows)==J['equality_names']
 A=list(rows.values());b=list(rhs.values());bounds=[]
 for target,r in zip([-1]+list(range(len(positions))),J['bounds']):
  objective=[int(target<0 or i==target)for i,h,s in keys]+[0]*len(positions)
  y=list(map(F,r['dual_equalities']));z=[F(0)]*num+list(map(F,r['dual_upper']));assert len(y)==len(A)and len(z)==size and all(v>=0 for v in z)
  lhs=[sum(y[i]*A[i][j]for i in range(len(A)))+z[j]for j in range(size)]
  assert all(a>=b for a,b in zip(lhs,objective))
  bound=sum(v*w for v,w in zip(y,b))+sum(z);assert bound==F(r['upper'])and bound.numerator//bound.denominator==r['integer_upper']
  bounds.append(r['integer_upper'])
 assert bounds[0]==(12 if height==4 else 224)
 results.append(dict(height=height,offset=off,input_sector_bit=1,multiplicative_sigma=-1,read_orbits=len(positions),variables=size,equalities=len(A),total_period_bound=bounds[0],site_visit_bounds=bounds[1:],certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
out=dict(status='PASS independent outgoing-event quotient incidence and every exact rational dual',results=results,scope='Prepared NE104 input in the specified finite cylinders, full drift(-2,-2), sector bit1. Output bits free. Necessary all-period bounds, not chronological existence or no-front proofs. General fixed-oblique decision lemma separately audited from the strict scalar clock.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
