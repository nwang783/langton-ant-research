#!/usr/bin/env python3
"""Physical lower-strip transducers; exploratory, not a front certificate."""
from itertools import accumulate

def second(n,r):
 pi=list(range(n-1));pi[r],pi[r+1]=pi[r+1],pi[r]
 ans=[]
 for j,k in enumerate(pi):
  if j==r+1:w='SESWNEN'
  else:
   b=j%2 if j<=r+1 else 1-j%2
   w='S'+'EW'[1-b]+'N'
  ans.append((k,w))
 return ans

def extend(L,p,q,old):
 assert len(p)==len(q)==len(old)
 p=set(p);q=set(q)
 E=lambda marks,j:(j in marks) != (j%2==0)
 # Wait: E = marked xor odd, hence != odd, not != even.
 E=lambda marks,j:(j in marks) != (j%2==1)
 cs={True:[],False:[]};ds={True:[],False:[]}
 for j in range(L):cs[E(p,j)].append(j);ds[E(q,j)].append(j)
 assert all(len(cs[b])==len(ds[b]) for b in cs)
 hd={i:(j,'E' if b else 'W') for b in cs for i,j in zip(cs[b],ds[b])}
 ps=sorted(p);qs=sorted(q); lower={qs[j]:(ps[k],w) for j,(k,w) in enumerate(old)}
 cin=[j for j in range(L) if j not in p];dout=[j for j in range(L) if j not in q]
 out=[]
 for i in cin:
  w='S';seen=set()
  while True:
   if i in seen:raise ValueError(('sealed',i,w))
   seen.add(i);j,h=hd[i];w+=h
   if j not in lower:
    w+='N';out.append((dout.index(j),w));break
   i,v=lower[j];w+=v
 assert sorted(k for k,w in out)==list(range(len(out)))
 return out

def describe(t):
 return [(j,k,len(w),(sum(c=='E' for c in w)-sum(c=='W' for c in w)+1)//2,w) for j,(k,w) in enumerate(t)]
# The start D' is one east of endpoint C': dx=2 beta-1.
if __name__=='__main__':
 for a in (0,2,4):
  for L in (a+4,a+5,a+6,a+8):
   print('A',a,L,describe(extend(L,[a,a+1,a+2],[a,a+2,a+3],second(4,0))))
 for a,c,L in [(0,4,7),(0,4,8),(0,6,9),(2,6,9)]:
  print('B',a,c,L,describe(extend(L,[a,a+1,a+2,c+2],[a,a+2,a+3,c],second(5,0))))
 for a,b,L in [(0,4,7),(0,4,8),(0,6,9),(2,6,9)]:
  print('C',a,b,L,describe(extend(L,[a+2,b-1,b,b+2],[a,b,b+1,b+2],second(5,2))))
