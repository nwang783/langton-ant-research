"""Exact integer replay of the constructive theorem, not a simulation proof."""
from collections import defaultdict
import random,json

def eps(x,y):return 1 if (x+y)%2 else -1

def construct(D):
 D={p:z for p,z in D.items() if z}
 if not D:return {},{}
 n=sum(map(abs,D.values()));rho={}
 nx=max(x for x,y in D)+4;ny=max(y for x,y in D)+4
 def fresh_x(parity):
  nonlocal nx
  nx+=1
  if nx%2!=parity%2:nx+=1
  return nx
 def fresh_y(parity):
  nonlocal ny
  ny+=1
  if ny%2!=parity%2:ny+=1
  return ny
 for (x,y),v in D.items():
  s=1 if v>0 else -1
  for _ in range(abs(v)):
   if s!=eps(x,y):
    c=fresh_x(x+1);r=fresh_y(y+1)
    path=[(c,y,s),(c,r,-s),(x,r,s)]
   else:
    c1=fresh_x(x);c2=fresh_x(x+1);r1=fresh_y(y+1);r2=fresh_y(y)
    path=[(c1,y,s),(c1,r1,-s),(c2,r1,s),(c2,r2,-s),(x,r2,s)]
   for a,b,z in path:
    assert (a,b) not in rho and z==eps(a,b)
    rho[a,b]=z
 F=defaultdict(int,rho)
 for p,z in D.items():F[p]-=z
 F={p:z for p,z in F.items() if z}
 marginsx=defaultdict(int);marginsy=defaultdict(int)
 for (x,y),z in F.items():marginsx[x]+=z;marginsy[y]+=z
 assert not any(marginsx.values()) and not any(marginsy.values())
 xmin=min(x for x,y in F);xmax=max(x for x,y in F)
 ymin=min(y for x,y in F);ymax=max(y for x,y in F)
 K0={}
 for x in range(xmin,xmax+1):
  for y in range(ymin,ymax+1):
   z=F.get((x,y),0)+K0.get((x-1,y),0)+K0.get((x,y-1),0)-K0.get((x-1,y-1),0)
   if z:K0[x,y]=z
 N=max(0,-min(K0.values(),default=0));assert N<=3*n
 K=defaultdict(int,K0)
 M0=max(abs(q) for p in set(rho)|set(K0) for q in p)+3
 for j in range(N):
  M=M0+j
  for x in range(-M,M+1):
   for y in range(-M-1,M+2):K[x,y]+=1
  for p,z in [((-M,-M-1),1),((M+1,-M-1),-1),((-M,M+2),-1),((M+1,M+2),1)]:
   assert p not in rho and z==eps(*p)
   rho[p]=z
 K={p:z for p,z in K.items() if z}
 assert all(z>0 for z in K.values()) and len(rho)<=17*n
 out=defaultdict(int,D)
 for (x,y),z in K.items():
  out[x,y]+=z;out[x+1,y]-=z;out[x,y+1]-=z;out[x+1,y+1]+=z
 out={p:z for p,z in out.items() if z}
 assert out==rho
 return rho,K

if __name__=='__main__':
 rng=random.Random(20261022);reports=[]
 cases=[{(0,0):1},{(0,0):-1},{(0,0):3},{(0,0):-3}]
 for _ in range(30):
  D=defaultdict(int)
  for i in range(1+rng.randrange(7)):D[rng.randrange(-3,4),rng.randrange(-3,4)]+=rng.choice([-2,-1,1,2])
  cases.append(dict(D))
 for D in cases:
  rho,K=construct(D)
  reports.append({'deposit_l1':sum(map(abs,D.values())),'black_mass':len(rho),'height_support':len(K),'max_height':max(K.values(),default=0)})
 out={'cases':len(reports),'all_exact_integer_checks_pass':True,'reports':reports}
 print(json.dumps(out,indent=2))
 open('/workspace/shared/langton/core_periodicity_new/static_vacuity_constructor_checks.json','w').write(json.dumps(out,indent=2))
