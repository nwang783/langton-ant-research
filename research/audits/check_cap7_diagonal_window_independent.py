"""Independent all-width cap-seven unit-diagonal finite-window audit.
No imports from the certificate producer; use physical complex edges and clocks.
"""
from pathlib import Path
from itertools import product
from collections import Counter,deque
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'periodic_classification_new'
J=json.loads((F/'diagonal_cap7_window4.certificate.json').read_text());dirs=(1j,1,-1j,-1)
states={}
for par in (0,1):
 for m in range(8):
  for hist in product((1,-1) if not par else (1j,-1j),repeat=m):
   ins=Counter(hist);outs=Counter(x*(-1j if rank%2==0 else 1j)for rank,x in enumerate(hist))
   states[par,hist]=(ins,outs,int(sum(d.real*n for d,n in outs.items())))
adj={s:[]for s in states}
for a,(ai,ao,av) in states.items():
 for b,(bi,bo,bv) in states.items():
  if a[0]!=b[0] and all((ao[d]==bi[d] if d.imag-d.real==1 else bo[d]==ai[d])for d in dirs):adj[a].append(b)
# Reachability from either empty parity is necessary at every finite-support strip row.
static=set([(0,()),(1,())]);q=deque(static)
while q:
 for s in adj[q.popleft()]:
  if s not in static:static.add(s);q.append(s)
for par,h in static:
 co=Counter(h[::2] if not par else h[1::2]);assert co[1 if not par else 1j]==co[-1 if not par else -1j]

def inspect(window):
 events={(i,r)for i,s in enumerate(window)for r in range(len(s[1]))};succ={}
 for i,(par,h) in enumerate(window):
  for rank,inc in enumerate(h):
   out=inc*(-1j if rank%2==0 else 1j)
   dest=i+int(out.imag-out.real);seam=int(out.real)
   if not 0<=dest<len(window):continue
   ordinal=sum(x*(-1j if j%2==0 else 1j)==out for j,x in enumerate(h[:rank]))
   arrivals=[j for j,x in enumerate(window[dest][1])if x==out]
   assert ordinal<len(arrivals)
   succ[i,rank]=((dest,arrivals[ordinal]),seam)
 assert len({v for v,k in succ.values()})==len(succ)
 # Detect cycles independently using physical clock reconstruction.
 processed=set()
 for e in events:
  trail=[];where={};u=e
  while u in succ and u not in processed and u not in where:
   where[u]=len(trail);trail.append(u);u=succ[u][0]
  if u in where:
   cyc=trail[where[u]:];vol=sum(succ[x][1]for x in cyc)
   if set(cyc)!=events or vol!=1:return 'closed'
   P=len(cyc);times={cyc[0]:0}
   for a in cyc[:-1]:
    b,k=succ[a];times[b]=times[a]+1-k*P
   if all(all(times[i,r]<times[i,r+1]for r in range(len(s[1])-1))for i,s in enumerate(window)):
    raise AssertionError(('POTENTIAL WHOLE FRONT must not discard',window))
   return 'closed'
  processed.update(trail)
 # Acyclic internal paths have length strictly below the global event period.
 for start in events:
  u=start;L=0;w=0
  while u in succ:
   u,k=succ[u];L+=1;w+=k
   assert L<len(events)
   if u[0]==start[0] and ((u[1]>start[1] and w>=1)or(u[1]<start[1] and w<=0)):return 'order'
 return None

start=((0,()),(1,()),(0,()),0);seen={start};q=deque([start]);edges=set();reject=[]
while q:
 u=q.popleft();rows=u[:3];vol=u[3]
 for new in adj[rows[-1]]:
  full=rows+(new,);bad=inspect(full)
  if bad:reject.append((u,new,bad));continue
  v=(rows[1],rows[2],new,(vol+states[new][2])%2);edges.add((u,v))
  if v not in seen:seen.add(v);q.append(v)
rev={u:[]for u in seen}
for u,v in edges:rev[v].append(u)
returning={u for u in seen if not any(s[1]for s in u[:3])};q=deque(returning)
while q:
 for u in rev[q.popleft()]:
  if u not in returning:returning.add(u);q.append(u)
assert len(returning)==2 and all(not any(s[1]for s in u[:3])for u in returning)
assert all(u[3]==0 for u in returning)
# Match the frozen graph, without using its pruning or witnesses in discovery.
def translate(u):
 p,ix,w=u;return tuple(((p+i)%2,tuple(dirs[d]for d in J['histories'][(p+i)%2][a]['h']))for i,a in enumerate(ix))+(w,)
assert seen==set(map(translate,J['states']))
assert edges=={(translate(a),translate(b))for a,b in J['accepted']}
assert returning==set(map(translate,J['returning_states']))
actualreject={(translate(r['source']),((r['source'][0]+3)%2,tuple(dirs[d]for d in J['histories'][(r['source'][0]+3)%2][r['added']]['h'])))for r in J['rejected']}
assert {(u,n)for u,n,b in reject}==actualreject
out=dict(status='PASS all-width cap-seven full-unit-diagonal exclusion',unpruned_states=len(states),unpruned_static_edges=sum(map(len,adj.values())),static_reachable=len(static),window_states=len(seen),accepted_edges=len(edges),rejected_extensions=len(reject),returning_states=len(returning),returning_active_states=0,scope='Full drift(1,1) and quarter rotations, any period or width; cap seven only; no primitive-diagonal quotient inference.',sha256={f:hashlib.sha256((F/f).read_bytes()).hexdigest()for f in ['diagonal_cap7_window4.certificate.json','probe_diagonal_window_transfer.py']})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
