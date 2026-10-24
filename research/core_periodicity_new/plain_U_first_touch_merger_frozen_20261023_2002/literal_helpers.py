"""Finite first-touch gate inventory and protected-tree exact clocks. No path search."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,deque
import math,json,hashlib
ROOT=Path('/workspace/shared/langton/core_periodicity_new');HERE=Path(__file__).resolve().parent
GP=ROOT/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];IDS=(0,1,4,5,6,7,8,9);K=set(map(tuple,J['core']));MARK=G[0]['marker'];W=(-1,3)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def place(q,p,h):return add(p,rot(q,h))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and dot(sub(p,a),sub(p,b))<=0
def contact(a,b,c,d):
 u=sub(b,a);v=sub(d,c);r=sub(c,a);z=cross(u,v)
 if z:
  s=F(cross(r,v),z);t=F(cross(r,u),z)
  return [[str(F(a[k])+s*u[k])for k in range(2)]]if 0<=s<=1 and 0<=t<=1 else[]
 return[list(p)for p in sorted({a,b,c,d})if on(p,a,b)and on(p,c,d)]
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def edge(q):
 x,y=q;d=(1,1)if(x+y)%2==0 else(1,-1)
 return((2*x-d[0],2*y-d[1]),(2*x+d[0],2*y+d[1]))
def reconstruct(word):
 p=(0,0);h=0;par=set();req={}
 for ch in word:
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b
  req[p]=b;par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=place((0,1),p,h)
 return req,par,p,h
for a in IDS:
 req,par,p,h=reconstruct(G[a]['word']+MARK);assert req=={(x,y):bool(b)for x,y,b,*_ in G[a]['requirements']}
 req,par,p,h=reconstruct(G[a]['word']);assert[*p,h]==G[a]['endpoint'];board=(K|set(map(tuple,G[a]['inputs'])))^par;assert board-{place(q,p,h)for q in K}==set(map(tuple,G[a]['outputs']))
def chords(a,p=(0,0),h=0):
 out=[];base=0 if a in(0,1)else 4 if a in(4,5,6)else 7
 start=center(p,h);end=add(start,rot((2,2)if base==0 else(2,6)if base==4 else(0,8),h));out.append((start,end))
 ep=G[base]['endpoint'];p=place(ep[:2],p,h);h=(h+ep[2])%4
 for _ in range(G[a]['name'].count('C')):
  start=center(p,h);p=place((0,1),p,h);h=(h+3)%4;out.append((start,center(p,h)))
 return out

def unique_tree_bridge(cells,E):
 adj={}
 for q in cells:
  a,b=edge(q);adj.setdefault(a,[]).append((b,q));adj.setdefault(b,[]).append((a,q))
 # All six gates sit on one attached tree. The source west-top route is the
 # unique shortest path to W, no traversal of the source cycle is needed.
 todo=deque([(E,[E],[])]);seen={E};paths=[]
 while todo:
  v,p,qs=todo.popleft()
  if v==W:return p,qs
  for z,q in adj.get(v,[]):
   if z not in seen:seen.add(z);todo.append((z,p+[z],qs+[q]))
 raise AssertionError('no bridge')
