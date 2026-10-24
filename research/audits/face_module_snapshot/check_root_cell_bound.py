"""Complete finite interface check for the two root boundary cells.
Root and predecessor start in the same state. The two root faces are explicit;
their four children are arbitrary modules with return language G/B/GB.
Only the first child of either face can read the root as its last boundary.
No deeper interior can read either tracked boundary cell.
"""
from itertools import product
# parent,root,x,y,sign,c1,c2; root=0, predecessor=1.
mods=[(1,0,2,3,0,2,3),(1,0,4,5,1,4,5)]
leaves={2:(0,2,1),3:(2,3,1),4:(0,4,0),5:(4,5,0)}
maximum=[0,0];states=0

def read(c,i,n):
 c[i]^=1
 if i<2:n[i]+=1

def stop(n):
 for i in range(2):maximum[i]=max(maximum[i],n[i])

def walk(c,l,stack,n):
 global states
 states+=1
 while stack:
  m,pc=stack[-1]
  if m>=2:
   p,w,a=leaves[m];assert c[w]==a
   read(c,w,n);stop(n)
   if l[m-2]==2:return
   assert c[p]==a
   for out in ('G','B') if l[m-2]==0 else ('B',):
    cc,ll,nn=c.copy(),l.copy(),n.copy()
    if out=='B':cc[w]=a
    read(cc,p,nn);ll[m-2]=1 if out=='G' else 2
    walk(cc,ll,stack[:-1].copy(),nn)
   return
  p,w,x,y,a,c1,c2=mods[m]
  if pc==-1:
   assert c[w]==a
   read(c,w,n);stack[-1]=(m,0)
  elif pc in (0,1):
   v,ch=(x,c1) if pc==0 else (y,c2)
   if c[v]==a:read(c,v,n);stack[-1]=(m,pc+1)
   else:stack.append((ch,-1))
  else:
   assert c[p]==a
   read(c,p,n);stack.pop()
 # Continue with whichever root face the root lamp now requests.
 walk(c,l,[(c[0],-1)],n)

for bits in product(range(2),repeat=4):walk([0,0]+list(bits),[0]*4,[(0,-1)],[0,0])
assert maximum==[5,3],maximum
print('PASS: all16 initial root-face interior color states; maximum root/predecessor reads',maximum,'states',states)
