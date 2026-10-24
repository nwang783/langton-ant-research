"""Exact finite-board translating-word tail checker. Standard library only."""
from collections import defaultdict
V=((0,1),(1,0),(0,-1),(-1,0))
def periodic(B,p,h,w):
 """Return EXACT earliest mismatch, or None, for w repeated from finite B."""
 start=p;heading=h;reads=[]
 for i,c in enumerate(w):
  reads.append((p,i,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 assert h==heading
 d=p[0]-start[0],p[1]-start[1];assert d!=(0,0);n=len(w)
 def orbit(q):
  axis=0 if d[0] else 1;a=q[axis]%abs(d[axis]);k=(q[axis]-a)//d[axis]
  return (q[0]-k*d[0],q[1]-k*d[1]),k
 groups=defaultdict(list);blacks=defaultdict(set)
 for q,i,c in reads:
  a,k=orbit(q);groups[a].append((i-n*k,k,c))
 for q in B:
  a,k=orbit(q);blacks[a].add(k)
 earliest=None;critical=0
 for a,slots in groups.items():
  slots.sort();lo=min(k for _,k,_ in slots);hi=max(k for _,k,_ in slots)
  levels=set(range(lo,hi+1))|{k for k in blacks[a] if k>=lo}
  free=hi+1
  while free in blacks[a]:free+=1
  levels.add(free)
  for m in levels:
   seq=[(offset+n*m,c)for offset,k,c in slots if k<=m];assert seq
   actual='L' if m in blacks[a] else 'R'
   for time,c in seq:
    if c!=actual:earliest=time if earliest is None else min(earliest,time);break
    actual='R' if actual=='L' else 'L'
   critical+=1
  # Outside the finitely checked eligibility levels and black exceptions,
  # every full slot list starts on white and has precisely the same chronology.
  seq=[c for _,_,c in slots]
  if seq[0]!='R' or any(x==y for x,y in zip(seq,seq[1:])):
   assert earliest is not None
 return earliest,d,groups,critical
