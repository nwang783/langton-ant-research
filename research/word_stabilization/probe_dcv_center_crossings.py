import json
from fractions import Fraction as F
from collections import Counter
P='/workspace/shared/langton/word_stabilization/'
J=json.load(open(P+'dcv_residual_core_resources.json')); G=J['geometry'];keep=J['kept_packet_types'];names=[g['name'] for g in G]
forbid={tuple(map(int,l.split()[:5])) for l in open(P+'seven_sub_dcv_star4_kernel.tsv')}
def rot(p,h):
 x,y=p
 return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def hit(a,b,c,d):
 u=sub(b,a);v=sub(d,c);w=sub(c,a);den=cross(u,v)
 if den:
  s=F(cross(w,v),den);t=F(cross(w,u),den)
  return 0<s<1 and 0<t<1
 if cross(w,u):return False
 k=0 if u[0] else 1
 lo=max(min(a[k],b[k]),min(c[k],d[k]));hi=min(max(a[k],b[k]),max(c[k],d[k]))
 return lo<hi
for offset in [(-1,-1),(0,0),(-1,0),(0,-1),(-2,-2),(-1,-2),(-2,-1),(1,1)]:
 paths=[]
 for name in names:
  p=(0,0);h=0;path=[add(p,rot(offset,h))]
  for m in name:
   e,dh=((2,2),0) if m=='D' else (((0,2),3) if m=='C' else ((2,6),0))
   p=add(p,rot(e,h));h=(h+dh)%4;path.append(add(p,rot(offset,h)))
  paths.append(path)
 survivors=[]
 for a in keep:
  for b in keep:
   for h in range(4):
    for x in range(-8,9):
     for y in range(-8,9):
      if (x+y-h)%2 or (a,b,x,y,h) in forbid:continue
      p=(2*x,2*y);B=[add(p,rot(z,h)) for z in paths[b]]
      if any(hit(u,v,r,s) for u,v in zip(paths[a],paths[a][1:]) for r,s in zip(B,B[1:])):
       survivors.append((a,b,x,y,h))
 print('offset',offset,'surviving proper crossings',len(survivors),'byheading',Counter(v[4] for v in survivors))
 if offset==(-1,-1):
  print(survivors[:100]);json.dump({'offset_doubled':offset,'surviving_proper_crossings':survivors},open(P+'dcv_center_crossings.json','w'),indent=2)
