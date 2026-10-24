import json
from collections import Counter
G=json.load(open('/workspace/shared/langton/core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'))['geometry']
IDS=(0,1,4,5,6,7,8,9)
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def cross(a,b,c):return(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def on(a,b,c):return cross(a,b,c)==0 and min(a[0],b[0])<=c[0]<=max(a[0],b[0])and min(a[1],b[1])<=c[1]<=max(a[1],b[1])
def meet(a,b,c,d):
 s,t,u,v=cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)
 return(s*t<0 and u*v<0)or(s==0 and on(a,b,c))or(t==0 and on(a,b,d))or(u==0 and on(c,d,a))or(v==0 and on(c,d,b))
ST=sorted({rot(v,h)for v in((1,1),(1,3),(0,4))for h in range(4)})
def candidates(d):
 # All candidate atomic entry centers differ from A by an even-sum integer.
 out=[]
 for x in range(min(0,d[0])-4,max(0,d[0])+5):
  for y in range(min(0,d[1])-4,max(0,d[1])+5):
   if(x+y)%2:continue
   vs=[v for v in ST if meet((0,0),d,(x,y),add((x,y),v))]
   if vs:out.append(((x,y),vs))
 return out
cache={};rows=[]
for a in IDS:
 for o in G[a]['outputs']:
  for b in IDS:
   for i in G[b]['inputs']:
    for h in range(4):
     p=sub(o,rot(i,h))
     if(sum(p)+h)%2:continue
     # A=(-1/2,-1/2); use doubled center correction then divide difference.
     r=rot((-1,-1),h);d=(p[0]+(r[0]+1)//2,p[1]+(r[1]+1)//2)
     assert(sum(d))%2==0
     if d not in cache:cache[d]=candidates(d)
     M=len(cache[d]);rows.append((4*M+13,a,b,o,i,h,p,d,M))
print('deltas',len(cache),'maxM',max(map(len,cache.values())),'maxBound',max(r[0]for r in rows))
print('hist',Counter(r[0]for r in rows))
for r in rows:
 if r[0]==max(x[0]for x in rows):print(r)
print('maxd',max(abs(x)+abs(y)for x,y in cache))
json.dump({'steps':ST,'rows':rows,'candidates':{str(k):v for k,v in cache.items()}},open('/workspace/shared/langton/causal_white_archive_2026-10-23/probe_chord_age.json','w'),indent=2)
