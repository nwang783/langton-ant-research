#!/usr/bin/env python3
"""Look for a counterexample to a proposed stronger sign lemma.
A bounded negative result is not a theorem. Exact positive words are checked
with the full displacement-class chronology criterion, allowing input L.
"""
import itertools,math,json,time
D=((0,1),(1,0),(0,-1),(-1,0))
def egcd(a,b):
 if b==0:return (abs(a),1 if a>0 else -1,0)
 g,x,y=egcd(b,a%b);return g,y,x-(a//b)*y
def check(w):
 h=0;p=(0,0);P=[]
 for c in w:
  P.append(p);h=(h+(1 if c=='R' else-1))%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy
 if h or p==(0,0):return
 a,b=p;g=math.gcd(a,b);ux,uy=a//g,b//g;_,s,t=egcd(ux,uy);C={}
 for i,((x,y),c) in enumerate(zip(P,w)):
  z=s*x+t*y;r=z%g;k=(z-r)//g;key=(uy*x-ux*y,r)
  C.setdefault(key,[]).append((-k,i,c))
  if len(C[key])>3:return
 for v in C.values():
  v.sort()
  if any(v[j][2]==v[j-1][2] for j in range(1,len(v))):return
 return dict(word=w,drift=p,excess=w.count('R')-w.count('L'),multiplicities=sorted(map(len,C.values())),input_L_classes=sum(v[0][2]=='L' for v in C.values()))
def words(T):
 # Positive excess permits cyclic rotation to a R-run start.
 # Enumerate cyclic alternating run lengths 1,2,4.
 def go(left,runs,total):
  if left==0:
   if len(runs)%2==0 and total>0 and total%4==0:
    yield ''.join(('R' if i%2==0 else'L')*n for i,n in enumerate(runs))
   return
  for n in (1,2,4):
   if n<=left:
    yield from go(left-n,runs+[n],total+(n if len(runs)%2==0 else-n))
 yield from go(T,[],0)
if __name__=='__main__':
 counts=[];start=time.time()
 for T in range(4,27,2):
  n=0
  for w in words(T):
   n+=1;r=check(w)
   if r:
    print(json.dumps(r),flush=True)
    open(__file__.replace('.py','.json'),'w').write(json.dumps(dict(result='COUNTEREXAMPLE',front=r,prior=counts),indent=2)+'\n')
    raise SystemExit
  counts.append(dict(period=T,checked=n));print(T,n,'none',round(time.time()-start,2),flush=True)
 open(__file__.replace('.py','.json'),'w').write(json.dumps(dict(result='BOUNDED_NEGATIVE_ONLY',counts=counts),indent=2)+'\n')
