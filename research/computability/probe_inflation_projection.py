"""Finite-field obstruction to an arbitrary finite linear coarse-board map.
This is a scoped auxiliary test, not an inflation exclusion.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
R=next(z for z in json.load(open(ROOT/'causal_reduction/morphic_candidates/free_inflations_k9.json'))['results'] if z['scale']==[3,0])
D=[(0,1),(1,0),(0,-1),(-1,0)]
def poly(w,h=0):
 x=y=0;s=set()
 for c in w:
  if (x,y)in s:s.remove((x,y))
  else:s.add((x,y))
  h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return s
# F4 = F2[a]/(a^2+a+1), values 0,1,a,a+1.
def mul(x,y):
 r=0
 while y:
  if y&1:r^=x
  x<<=1
  if x&4:x^=7
  y>>=1
 return r
def pw(x,n):
 n%=3;r=1
 for _ in range(n):r=mul(r,x)
 return r
def solve(x,y):
 rows=[];labels=[]
 for c,ws in R['images'].items():
  for w in ws:
   for h in range(4):
    row=[0]*10
    for i,j in poly(w,h):
     q,r=divmod(i+1,3);z,s=divmod(j+1,3)
     row[3*r+s]^=mul(pw(x,q),pw(y,z))
    row[-1]=1;rows.append(row);labels.append((c,w,h))
 base={}
 for k,row0 in enumerate(rows):
  row=row0.copy();witness={k:1}
  for i in range(9):
   if not row[i]:continue
   if i in base:
    other,comb=base[i];v=row[i]
    row=[a^mul(v,b)for a,b in zip(row,other)]
    for j,t in comb.items():
     witness[j]=witness.get(j,0)^mul(v,t)
     if not witness[j]:del witness[j]
   else:
    inv=pw(row[i],2);row=[mul(inv,v)for v in row]
    witness={j:mul(inv,t)for j,t in witness.items()};base[i]=(row,witness);break
  else:
   if row[-1]:return dict(x=x,y=y,status='INCONSISTENT',rank=len(base),witness=[dict(coefficient=v,label=labels[j])for j,v in witness.items()],rhs=row[-1])
 return dict(x=x,y=y,status='CONSISTENT',rank=len(base))
if __name__=='__main__':
 out=[solve(x,y)for x in [1,2,3]for y in [1,2,3]]
 print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
