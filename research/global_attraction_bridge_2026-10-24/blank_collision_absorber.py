"""Full infinite standard104 predicate and absorbing exact collision research map."""
from blank_collision_operator import *
def field_ray_changes(segments,q,d):
 changes={}
 def interval(lo,hi):
  lo=max(lo,0)
  if hi<lo:return
  changes[lo]=changes.get(lo,0)^1;changes[hi+1]=changes.get(hi+1,0)^1
 for b,v,n in segments:
  z=(b[0]-q[0],b[1]-q[1])
  if v==(0,0):
   k=multiple(z,d)
   if k is not None:interval(k,k)
  elif cross(d,v)==0:
   a=multiple(z,d)
   if a is None:continue
   s=multiple(v,d);assert s in(-1,1)
   b=a+s*(n-1);interval(min(a,b),max(a,b))
  else:
   det=cross(d,v);ka=cross(z,v);ja=cross(z,d)
   if ka%det or ja%det:continue
   k,j=ka//det,ja//det
   if 0<=j<n:interval(k,k)
 return changes

def certify_word(segments,p,h,w):
 Q,end,eh=geometry(p,h,w);d=(end[0]-p[0],end[1]-p[1])
 if eh!=h or d==(0,0):return None
 checked=0
 for i,q in enumerate(Q):
  changes=field_ray_changes(segments,q,d);changes.setdefault(0,0)
  for j,r in enumerate(Q):
   k=multiple((r[0]-q[0],r[1]-q[1]),d)
   if k is not None and(k>0 or k==0 and j<i):changes[k]=changes.get(k,0)^1
  parity=0
  for k in sorted(changes):
   parity^=changes[k];checked+=1
   if parity!=(w[i]=='L'):return None
 return dict(period=w,drift=d,phase_ray_change_points_checked=checked)

def standard_certificate(segments,p,h):
 for i in range(104):
  w=H[i:]+H[:i];c=certify_word(segments,p,h,w)
  if c is not None:c['cyclic_phase_in_blank_H']=i;return c
 return None

def absorbing_step(segments,p=(0,0),h=0):
 c=standard_certificate(segments,p,h)
 if c is not None:return dict(kind='ABSORBED exact full-board standard104',certificate=c)
 z=next_collision(segments,p,h)
 if z['kind']!='collision':return dict(kind='ABSORBED exact no-old-contact blank capture',certificate=z)
 return z
