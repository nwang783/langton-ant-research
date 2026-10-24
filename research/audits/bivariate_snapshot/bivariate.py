"""Exact affine-XOR engine in two independent nonnegative integer variables.

Scalars (a,b,c) mean a*u+b*v+c, u,v>=0. Ordering is accepted only if a
coefficientwise guard proves it. Diophantine incidences are checked exactly,
not tested on a parameter grid. Existing finite/ray parity code is reused only
through the scalar/geometry interface replaced here.
"""
import sys,math
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation/wake_clock')
import certify_four_scatterer_prefix as A
ZERO=(0,0,0);ONE=(0,0,1)
def add(a,b):assert len(a)==len(b)==3;return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def scale(a,k):return tuple(x*k for x in a)
def val(a):return a[2]
def nonneg(a):return all(x>=0 for x in a)
def negative(a):return a[0]<=0 and a[1]<=0 and a[2]<0
def point(x,y):return (0,0,x),(0,0,y)
def translate_local(q,base,j):
 x,y=A.rotate(q,j);return add(base[0],(0,0,x)),add(base[1],(0,0,y))

def has_nonnegative_zero(f):
 """Whether a*u+b*v+c=0 has u,v nonnegative integers."""
 a,b,c=f;t=-c
 if a==0 and b==0:return t==0
 if a==0:return t%b==0 and t//b>=0
 if b==0:return t%a==0 and t//a>=0
 g=math.gcd(a,b)
 if t%g:return False
 if a*b<0:return True
 if a<0:a,b,t=-a,-b,-t
 if t<0:return False
 # Least nonnegative solution u of (a/g)u=t/g mod(b/g).
 aa,bb,tt=a//g,b//g,t//g
 u=0 if bb==1 else (tt*pow(aa,-1,bb))%bb
 return a*u<=t

def no_point_collision(p,q):
 dx,dy=A.psub(p,q)
 if dx==ZERO and dy==ZERO:return False
 A.STATS['excluded_isolated_equalities']+=1
 if dx[:2]==(0,0) and dx[2]!=0 or dy[:2]==(0,0) and dy[2]!=0:return True
 a,b,c=dx;d,e,f=dy;det=a*e-b*d
 if det:
  un=b*f-c*e;vn=c*d-a*f
  collision=un%det==0 and vn%det==0 and un//det>=0 and vn//det>=0
 else:
  if a*f!=c*d or b*f!=c*e:return True
  collision=has_nonnegative_zero(dx if dx!=ZERO else dy)
 assert not collision,('bivariate point incidence',p,q)
 return True

def integer_affine(a,k):
 assert a[0]%k==a[1]%k==0,('parameter residue class required',a,k)
 if a[2]%k:return None
 return tuple(x//k for x in a)
def line_coordinate(delta,d):
 cr=A.cross(delta,d)
 if cr!=ZERO:
  assert not has_nonnegative_zero(cr),('bivariate line incidence needs partition',delta,d,cr)
  return None
 return integer_affine(delta[0],d[0])

def apply_periods(field,data,base,j,N,label):
 required,odd,end,eh=data;d=A.rotate(end,j)
 local_flips=[translate_local(q,base,j) for q in odd]
 for q0,bit in required.items():
  q=translate_local(q0,base,j);boundaries=set()
  if bit:A.toggle_boundary(boundaries,(ZERO,sub(N,ONE)))
  for b in field.points:
   k=line_coordinate(A.psub(b,q),d)
   if k is not None:A.toggle_boundary(boundaries,A.clip(k,k,N))
  for b,e,M,_ in field.rays:A.toggle_boundary(boundaries,A.previous_ray_interval(q,d,b,e,M,N))
  for b in local_flips:
   m=line_coordinate(A.psub(b,q),d)
   if m is not None:
    assert m[:2]==(0,0)
    if m[2]>0:A.toggle_boundary(boundaries,A.clip(m,sub(N,ONE),N))
  assert not boundaries,('bivariate period color mismatch',label,q0,sorted(boundaries))
  A.STATS['periodic_read_constraints']+=1;A.READ_RAYS.append((q,d,N))
 field.add_rays(local_flips,d,N,label)
 return A.padd(base,(scale(N,d[0]),scale(N,d[1])))

def clip_infinite(lo,hi,unused):
 if negative(hi):return None
 lo=A.maximum(lo,ZERO);A.STATS['affine_guards']+=1
 if negative(sub(hi,lo)):return None
 assert nonneg(sub(hi,lo)),('infinite interval order needs partition',lo,hi)
 return lo,hi

def infinite_tail(field,data,base):
 required,odd,d,eh=data;flips=[translate_local(q,base,0) for q in odd];old=A.clip;A.clip=clip_infinite
 try:
  for q0,bit in required.items():
   q=translate_local(q0,base,0);bounds={ZERO} if bit else set()
   for b in field.points:
    k=line_coordinate(A.psub(b,q),d)
    if k is not None:A.toggle_boundary(bounds,A.clip(k,k,None))
   for b,e,N,_ in field.rays:A.toggle_boundary(bounds,A.previous_ray_interval(q,d,b,e,N,None))
   for b in flips:
    m=line_coordinate(A.psub(b,q),d)
    if m is not None:
     assert m[:2]==(0,0)
     if m[2]>0:bounds.symmetric_difference_update({m})
   assert not bounds,('bivariate infinite-tail mismatch',q0,sorted(bounds))
   A.STATS['periodic_read_constraints']+=1
 finally:A.clip=old
 return dict(drift=d,heading=eh,required_cells=len(required),odd_cells=len(odd))

for key in ('ZERO','ONE','add','neg','sub','scale','val','nonneg','negative','point','translate_local','no_point_collision','integer_affine','line_coordinate','apply_periods'):
 setattr(A,key,globals()[key])
