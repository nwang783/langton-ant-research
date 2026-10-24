"""Exact necessary local port/clock patterns at a strict-left K1 right turn.
Not a complete literal connector, translator, period or front search.
"""
from itertools import product
from pathlib import Path
from collections import Counter
import json
# N,E,S,W =0,1,2,3. A=(1,0), Z=(0,0), Y=(0,1), B=(1,1).
# Fi NW(A),NE(Z),SE(Y),SW(B). Selected A prefixN,N,S; B prefixE,E,W.
D=((0,1),(1,0),(0,-1),(-1,0)); phases={'A':0,'Z':1,'Y':2,'B':3}

def helper(h):
 for length in range(1,5):
  for ls in product((h,(h+2)%4),repeat=length//2):
   hs=[];j=0
   for r in range(length):
    if r%2:hs.append(ls[j]);j+=1
    else:hs.append(h)
   yield hs

def sel(h):
 for last in (None,h,(h+2)%4):yield [h,h,(h+2)%4]+([]if last is None else[last])

def outs(hs):return[(h+(1 if r%2==0 else-1))%4 for r,h in enumerate(hs)]

def feasible(hs):
 # Lower bound variables n=(time-phase)/4. all variable phase is vertex-specific.
 ns=[(v,r)for v in hs for r in range(len(hs[v]))];es=[]
 for v in hs:
  for r in range(len(hs[v])-1):es.append(((v,r),(v,r+1),1))
 def eql(a,b): # physical departure a to arrival b at +1 time
  pa,pb=phases[a[0]],phases[b[0]];assert (pa+1-pb)%4==0
  k=(pa+1-pb)//4;es.extend([(a,b,k),(b,a,-k)])
 oh={v:outs(x)for v,x in hs.items()}
 for a,out,b,inc in [('A',3,'Z',3),('Z',0,'Y',0),('Y',1,'B',1),('B',2,'A',2)]:
  src=[(a,r)for r,h in enumerate(oh[a])if h==out];tar=[(b,r)for r,h in enumerate(hs[b])if h==inc]
  if len(src)!=len(tar):return None
  for x,y in zip(src,tar):eql(x,y)
 # K1 requires A2 strictly before B1, retaining arbitrary detours outside Fi.
 a,b=('A',2),('B',1);k=(phases['A']+1-phases['B']+3)//4;es.append((a,b,k))
 dist={x:0 for x in ns}
 for it in range(len(ns)):
  changed=False
  for a,b,k in es:
   if dist[b]<dist[a]+k:dist[b]=dist[a]+k;changed=True
  if not changed:break
 else:return None
 off=dist[('A',1)]
 return {v:[4*(dist[(v,r)]-off)+phases[v]for r in range(len(hs[v]))]for v in hs}

rows=[]
for a,z,y,b in product(sel(0),helper(3),helper(0),sel(1)):
 hs=dict(A=a,Z=z,Y=y,B=b);t=feasible(hs)
 if t is None:continue
 rows.append(dict(headings=hs,turns={v:''.join('R'if r%2==0 else'L'for r in range(len(x)))for v,x in hs.items()},minimal_clock=t,Z_Rs=(len(z)+1)//2,Y_Rs=(len(y)+1)//2,Z_L1='absent'if len(z)<2 else'S'if z[1]==3 else'E',Y_L1='absent'if len(y)<2 else'S'if y[1]==0 else'E'))
summary=Counter((x['Z_Rs'],x['Y_Rs'],x['Z_L1'],x['Y_L1'])for x in rows)
res=dict(scope=__doc__,status='Exact local necessary port/clock table only; exterior connectors and whole-front sufficiency NOT claimed',coordinates=dict(A=[1,0],Z=[0,0],Y=[0,1],B=[1,1]),heading_key=['N','E','S','W'],count=len(rows),summary=[dict(Z_Rs=k[0],Y_Rs=k[1],Z_L1=k[2],Y_L1=k[3],count=v)for k,v in sorted(summary.items())],rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items()if k!='rows'},indent=2))
