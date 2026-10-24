#!/usr/bin/env python3
"""Independent physical-cell open-window generator and low-pivot GF(2) closure."""
from pathlib import Path
from collections import defaultdict,Counter
import json
R=Path(__file__).resolve().parents[1]
W=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
def trace(w,p=(0,0),d=(0,1)):
 out=[]
 for c in w:
  out.append((p,d,c));dx,dy=d;d=(dy,-dx) if c=='R' else (-dy,dx);p=(p[0]+d[0],p[1]+d[1])
 return out,p,d
base,end,eh=trace(W);assert len(base)==104 and end==(-2,2) and eh==(0,1)
local=[]
for i,(p,d,c) in enumerate(base):
 o='L' if c=='R' else 'R'
 for j,w in enumerate((o*4,c*4+o*4)):
  ev,ep,ed=trace(w,p,d);assert (ep,ed)==(p,d)
  for t,(q,_,letter) in enumerate(ev):local.append((q,(i,j,t),letter,2*i+j))
 local.append((p,(i,2,0),c,None))
def cr(p):
 x,y=p;par=x%2
 return (x+y,par),(par-x)//2
span={}
for p,*_ in local:
 cl,a=cr(p)
 if cl not in span:span[cl]=(a,a)
 lo,hi=span[cl];span[cl]=(min(lo,a),max(hi,a))
F=set()
for (z,par),(lo,hi) in span.items():
 for a in range(hi-3,lo+4):
  x=par-2*a;F.add((x,z-x))
events=defaultdict(list)
for k in range(-3,4):
 for p,t,c,var in local:
  q=(p[0]-2*k,p[1]+2*k)
  if q in F:events[q].append(((k,)+t,c,None if var is None else 208*(k+3)+var))
assert set(events)==F and len(F)==143
# Direct completeness: all possible epochs for every local point in a class
# are exactly rank(target)-rank(local), hence checked against [-3,3].
for q in F:
 cl,a=cr(q)
 for p,*_ in local:
  c,b=cr(p)
  if c==cl:assert -3<=a-b<=3
N=1456;eq=[];imp=[[] for _ in range(N)]
for es in events.values():
 parity=0;mask=0
 for _,c,v in sorted(es):
  row=(mask,parity^(c=='L'))
  if v is None:eq.append(row);parity^=1
  else:imp[v].append(row);mask^=1<<v
for k in range(7):
 for i in range(104):
  a=208*k+2*i;b=a+1
  imp[a].append((1<<b,0));imp[b].append((1<<a,0))
assert len(eq)==533 and all(b==0 for _,b in eq)
B={}
def reduce(m,b):
 while m:
  low=m&-m
  if low not in B:return m,b
  r,s=B[low];m^=r;b^=s
 return m,b
def add(m,b):
 m,b=reduce(m,b)
 if not m:assert not b;return
 B[m&-m]=(m,b)
def val(v):
 m,b=reduce(1<<v,0)
 return None if m else b
for row in eq:add(*row)
activated=set();forced=[]
while True:
 changed=False
 for v in range(N):
  x=val(v)
  if x==1 and v not in activated:
   activated.add(v);changed=True
   for r in imp[v]:add(*r)
  elif x is None and any(reduce(*r)==(0,1) for r in imp[v]):
   add(1<<v,0);forced.append(v);changed=True
 if not changed:break
assert all(val(v)==0 for v in range(624,832))
mult=max(Counter(cr(q)[0] for q in F).values());assert mult==7
saved=json.loads((R/'causal_reduction/front_surgery/window_rigidity_certificate.json').read_text())
assert sorted(F)==[tuple(p) for p in saved['cells']]
out=dict(status='PASS',variables=N,complete_cells=len(F),equations=len(eq),rank=len(B),forced_zero_count=len(forced),central_forced_zero=208,multiplicity=mult,positive_guard_activations=len(activated))
(R/'audits/detour_window_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
