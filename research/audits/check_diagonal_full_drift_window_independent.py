"""All-width window reconstruction with unpruned histories and physical seams.
Parameters cap,n,window refer to full drift(n,n), not a primitive quotient.
"""
from pathlib import Path
from itertools import product
from collections import Counter,deque
import json,hashlib,sys
CAP,N,K=map(int,sys.argv[1:]);ROOT=Path(__file__).resolve().parents[1];F=ROOT/'periodic_classification_new';stem=f'diagonal_n{N}_cap{CAP}_window{K}'
J=json.loads((F/(stem+'.certificate.json')).read_text());dirs=(1j,1,-1j,-1)
states={}
for par in (0,1):
 hs=[h for m in range(CAP+1)for h in product((1,-1)if not par else(1j,-1j),repeat=m)]
 for row in product(hs,repeat=N):
  ins=[Counter(h)for h in row];outs=[Counter(x*(-1j if j%2==0 else 1j)for j,x in enumerate(h))for h in row]
  volt=sum(((c+int(d.real))//N)*v for c,co in enumerate(outs)for d,v in co.items())
  states[par,row]=(ins,outs,volt)
# Matching signatures from physical outgoing and incoming edges across the upper boundary.
def signature(s,upper):
 ins,outs,vol=states[s];a=[]
 for c in range(N):
  for d in dirs:
   dest=(c+int(d.real))%N
   if d.imag-d.real==1:a.append(outs[c][d]if upper else ins[dest][d])
   else:a.append(ins[dest][d]if upper else outs[c][d])
 return tuple(a)
index={}
for s in states:index.setdefault((s[0],signature(s,False)),[]).append(s)
adj={s:index.get((1-s[0],signature(s,True)),[])for s in states}
static={(0,((),)*N),(1,((),)*N)};q=deque(static)
while q:
 for s in adj[q.popleft()]:
  if s not in static:static.add(s);q.append(s)
for par,row in static:
 co=Counter(x for h in row for x in(h[::2]if not par else h[1::2]));assert co[1 if not par else 1j]==co[-1 if not par else -1j]

def inspect(window):
 events={(i,c,r)for i,s in enumerate(window)for c,h in enumerate(s[1])for r in range(len(h))};succ={}
 for i,(par,row) in enumerate(window):
  for c,h in enumerate(row):
   for rank,inc in enumerate(h):
    out=inc*(-1j if rank%2==0 else 1j);dest=i+int(out.imag-out.real)
    if not 0<=dest<len(window):continue
    col=(c+int(out.real))%N;seam=(c+int(out.real))//N
    ordinal=sum(x*(-1j if j%2==0 else 1j)==out for j,x in enumerate(h[:rank]))
    arrivals=[j for j,x in enumerate(window[dest][1][col])if x==out]
    assert ordinal<len(arrivals);succ[i,c,rank]=((dest,col,arrivals[ordinal]),seam)
 assert len({v for v,k in succ.values()})==len(succ)
 processed=set()
 for e in events:
  trail=[];where={};u=e
  while u in succ and u not in processed and u not in where:
   where[u]=len(trail);trail.append(u);u=succ[u][0]
  if u in where:
   cyc=trail[where[u]:];vol=sum(succ[x][1]for x in cyc)
   if set(cyc)!=events or vol!=1:return 'closed'
   period=len(cyc);times={cyc[0]:0}
   for a in cyc[:-1]:
    b,k=succ[a];times[b]=times[a]+1-k*period
   if all(all(times[i,c,r]<times[i,c,r+1]for r in range(len(h)-1))for i,s in enumerate(window)for c,h in enumerate(s[1])):raise AssertionError(('POTENTIAL WHOLE FRONT',window))
   return 'closed'
  processed.update(trail)
 for start in events:
  u=start;L=0;w=0
  while u in succ:
   u,k=succ[u];L+=1;w+=k;assert L<len(events)
   if u[:2]==start[:2]and((u[2]>start[2]and w>=1)or(u[2]<start[2]and w<=0)):return 'order'
 return None
start=tuple((i%2,((),)*N)for i in range(K-1))+(0,);seen={start};q=deque([start]);edges=set();badcounts=Counter()
while q:
 u=q.popleft();rows=u[:-1];vol=u[-1]
 for new in adj[rows[-1]]:
  bad=inspect(rows+(new,))
  if bad:badcounts[bad]+=1;continue
  v=rows[1:]+(new,(vol+states[new][2])%2);edges.add((u,v))
  if v not in seen:seen.add(v);q.append(v)
empty={u for u in seen if not any(h for s in u[:-1]for h in s[1])};assert len(empty)==2 and all(u[-1]==0 for u in empty)
rev={u:[]for u in seen}
for u,v in edges:rev[v].append(u)
returning=set(empty);q=deque(returning)
while q:
 for u in rev[q.popleft()]:
  if u not in returning:returning.add(u);q.append(u)
def translate(u):
 p,ix,w=u;return tuple(((p+i)%2,tuple(tuple(dirs[d]for d in c['h'])for c in J['histories'][(p+i)%2][a]['cells']))for i,a in enumerate(ix))+(w,)
assert seen==set(map(translate,J['states']))
assert edges=={(translate(a),translate(b))for a,b in J['accepted']}
assert returning==set(map(translate,J['returning_states']))
out=dict(status='PASS all-width window obstruction for the specified FULL drift',cap=CAP,full_drift=[N,N],window=K,unpruned_row_states=len(states),unpruned_static_edges=sum(map(len,adj.values())),static_reachable=len(static),window_states=len(seen),accepted_edges=len(edges),rejected_extensions=sum(badcounts.values()),returning_states=len(returning),odd_empty_states=0,sha256=hashlib.sha256((F/(stem+'.certificate.json')).read_bytes()).hexdigest(),scope='Every width and period, quarter rotations included; no primitive-drift quotient inference.')
p=Path(__file__).with_name(stem+'_independent.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
