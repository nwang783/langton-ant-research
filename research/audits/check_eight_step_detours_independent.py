#!/usr/bin/env python3
"""Independent complete loop enumeration, physical window, low-pivot proof."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1];t0=time.monotonic()
W=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
def trace(w,p=(0,0),d=(0,1)):
 out=[]
 for c in w:
  out.append((p,d,c));dx,dy=d;d=(dy,-dx) if c=='R' else (-dy,dx);p=p[0]+d[0],p[1]+d[1]
 return out,p,d
lib=[]
for n in range(1,9):
 for letters in product('RL',repeat=n):
  w=''.join(letters);ev,p,d=trace(w)
  if (p,d)!=((0,0),(0,1)):continue
  last={};valid=True
  for q,_,c in ev:
   if last.get(q)==c:valid=False;break
   last[q]=c
  if valid:lib.append(w)
assert len(lib)==10
base,end,dh=trace(W);assert end==(-2,2) and dh==(0,1)
local=[];options=[];byphase=[]
for i,(p,d,c) in enumerate(base):
 allowed=[]
 for w in lib:
  es,_,_=trace(w);last=next(letter for q,_,letter in reversed(es) if q==(0,0))
  if last!=c:allowed.append(w)
 assert len(allowed)==5;ids=[]
 for j,w in enumerate(allowed):
  v=len(options);options.append((i,w));ids.append(v)
  ev,ep,ed=trace(w,p,d);assert (ep,ed)==(p,d)
  for s,(q,_,letter) in enumerate(ev):local.append((q,(i,j,s),letter,v))
 local.append((p,(i,5,0),c,None));byphase.append(ids)
P=len(options);assert P==520

def cr(p):
 x,y=p;r=x%2;return (x+y,r),(r-x)//2
span={}
for p,*_ in local:
 cl,a=cr(p);lo,hi=span.get(cl,(a,a));span[cl]=min(lo,a),max(hi,a)
F=set()
for (z,r),(lo,hi) in span.items():
 for a in range(hi-4,lo+5):x=r-2*a;F.add((x,z-x))
events=defaultdict(list)
for k in range(-4,5):
 for p,tag,c,v in local:
  q=p[0]-2*k,p[1]+2*k
  if q in F:events[q].append(((k,)+tag,c,None if v is None else P*(k+4)+v))
assert set(events)==F and len(F)==206
for q in F:
 cl,a=cr(q)
 for p,*_ in local:
  cc,b=cr(p)
  if cc==cl:assert -4<=a-b<=4
N=P*9;eq=[];imp=[[] for _ in range(N)]
for es in events.values():
 mask=par=0
 for _,c,v in sorted(es):
  row=mask,par^(c=='L')
  if v is None:eq.append(row);par^=1
  else:imp[v].append(row);mask^=1<<v
for k in range(9):
 for ids in byphase:
  for a in ids:
   for b in ids:
    if a!=b:imp[k*P+a].append((1<<(k*P+b),0))
assert len(eq)==663 and all(rhs==0 for _,rhs in eq)
def red(m,b,B):
 while m:
  low=m&-m
  if low not in B:return m,b
  r,s=B[low];m^=r;b^=s
 return m,b
def add(m,b,B):
 m,b=red(m,b,B)
 if not m:return not b
 B[m&-m]=m,b;return True
def val(v,B):
 m,b=red(1<<v,0,B);return None if m else b
def close(rows):
 B={};active=set()
 for m,b in rows:
  if not add(m,b,B):return None
 while True:
  change=False
  for v in range(N):
   x=val(v,B)
   if x==1 and v not in active:
    active.add(v);change=True
    for m,b in imp[v]:
     if not add(m,b,B):return None
   elif x is None and any(red(m,b,B)==(0,1) for m,b in imp[v]):
    assert add(1<<v,0,B);change=True
  if not change:return B
B=close(eq);assert B is not None
central=list(range(4*P,5*P));unknown=[v for v in central if val(v,B) is None]
assert sum(val(v,B)==0 for v in central)==514 and len(unknown)==6
for v in unknown:assert close(list(B.values())+[(1<<v,1)]) is None
mult=max(Counter(cr(q)[0] for q in F).values());assert mult==8
saved=json.loads((R/'causal_reduction/front_surgery/eight_step_detour_certificate.json').read_text())
assert lib==saved['library'] and sorted(F)==[tuple(p) for p in saved['complete_cells']]
out=dict(status='PASS',library=lib,variables=N,equations=len(eq),complete_cells=len(F),direct_central_zero=514,failed_literal_options=[options[v-4*P] for v in unknown],window_multiplicity=mult,seconds=time.monotonic()-t0)
(R/'audits/eight_step_detours_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
