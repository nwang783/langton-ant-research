"""One explicit charged return guide, preserving complete passive board."""
from check_staircase_backbone import *

def fine_of(coarse):
 fine=[(coarse[0][0]-coarse[0][1],sum(coarse[0]))]
 for u,v in zip(coarse,coarse[1:]):
  x,y=fine[-1];dx=v[0]-u[0];dy=v[1]-u[1];a=dx-dy;b=dx+dy;fine.extend([(x+a,y),(x+a,y+b)])
 return fine

def axis_join(corners):
 vs=[corners[0]]
 for v in corners[1:]:
  u=vs[-1];dx=v[0]-u[0];dy=v[1]-u[1];assert dx==0 or dy==0
  for _ in range(abs(dx)+abs(dy)):
   x,y=vs[-1];vs.append((x+(dx>0)-(dx<0),y+(dy>0)-(dy<0)))
 return vs

def setup_guide(q,scale=12,d=2):
 assert q%2==1
 coarse=vertices(q,scale);fine=fine_of(coarse);es=[(v[0]-u[0],v[1]-u[1])for u,v in zip(fine,fine[1:])];tr=[a[0]*b[1]-a[1]*b[0]for a,b in zip(es,es[1:])];C=set()
 for i in range(1,len(fine)-2):
  if tr[i-1]==tr[i]==1:
   x,y=fine[i];dx,dy=es[i-1];C|=cells_of([(x+dx,y+dy),(fine[i+1][0]+dx,fine[i+1][1]+dy)])
 x,y=fine[-1];dx,dy=es[-1];fine.append((x+dy,y-dx));es.append((dy,-dx));U=fine[-1]
 P=cells_of(fine);p=next(iter(cells_of(fine[:2])));h=next(h for h in range(4)if cursors(p,h)[1]==xy(fine[0]));word='L'
 for a,b in zip(es,es[1:]):word+='R'*(1+a[0]*b[1]-a[1]*b[0])+'L'
 # Left offset of coarse CCW spiral, then reverse it.
 runs=[]
 for j in range(1,q+1):
  dd=D[(j-1)%4];runs.append(dd)
 ends=[];idx=0
 for j in range(q):idx+=scale*((j+2)//2);ends.append(coarse[idx])
 corners=[(0,d)]
 for j,V in enumerate(ends[:-1]):
  a=runs[j];b=runs[j+1];corners.append((V[0]-d*(a[1]+b[1]),V[1]+d*(a[0]+b[0])))
 V=ends[-1];a=runs[-1];corners.append((V[0]-d*a[1],V[1]+d*a[0]));K=list(reversed(fine_of(axis_join(corners))))
 # Normalize local outer patch by half-turn when final coarse run is W.
 sg=1 if runs[-1]==(1,0)else -1
 def rel(a,b):return(U[0]+sg*a,U[1]+sg*b)
 patch=axis_join([rel(1,0),rel(1,-1),rel(3,-1),rel(3,4),rel(-3,4),rel(-3,2)])
 assert patch[-1]==K[0],(patch[-1],K[0])
 K=patch+K[1:]
 inner=axis_join([K[-1],(-4,2),(-4,-3),(0,-3),(0,-1)])
 K+=inner[1:]
 # Smooth every 3-edge unit-U in the guide before execution.
 changed=True
 while changed:
  changed=False
  for i in range(len(K)-3):
   if abs(K[i][0]-K[i+3][0])+abs(K[i][1]-K[i+3][1])==1:
    K=K[:i+1]+K[i+3:];changed=True;break
 cyc=axis_join([U,rel(1,0),rel(1,1),rel(0,1),U]);G=cells_of(K)|cells_of(cyc)
 assert len(K)==len(set(K));assert not(P&G or C&G or P&C)
 B=P|C|G
 return B,p,h,word,P,C,G,K,U


