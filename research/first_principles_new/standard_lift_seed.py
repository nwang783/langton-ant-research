"""Exact finite replay of the literal periodic W104 in the free-product coset model."""
import json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent
W=json.loads((P.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
ns=[(-1,2,0,0)];intern={};memo={}
def step(s,a):
 p,b,n,d=ns[s]
 if b==a:
  if n==3:return p
  n+=1
 else:p,n=s,1
 key=(p,a,n)
 if key not in intern:
  intern[key]=len(ns);ns.append((p,a,n,ns[p][3]+1))
 return intern[key]
def u(s,sign):
 for a in ([0,1,1,1] if sign>0 else [1,0,0,0]):s=step(s,a)
 return s
def cell(s):
 if s in memo:return memo[s]
 a,b=u(s,1),u(s,-1);m=min(ns[x][3] for x in (s,a,b));best=min(x for x in (s,a,b) if ns[x][3]==m)
 memo[s]=cell(best) if m<ns[s][3] else best
 return memo[s]
state=0;read={};records=[]
for epoch in range(100):
 c=Counter();phases=[]
 for i,a in enumerate(W):
  bit=int(a=='L');v=cell(state)
  if v not in read:
   c['new_'+a]+=1
   if a=='L':phases.append(i)
  else:assert read[v]!=bit
  read[v]=bit;state=step(state,bit)
 records.append(dict(epoch=epoch,**c,black_first_phases=phases))
print(json.dumps(records[:5]+records[-1:],indent=2))
(P/'standard_lift_seed.json').write_text(json.dumps(records,indent=2)+'\n')
