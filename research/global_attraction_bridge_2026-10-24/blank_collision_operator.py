"""Total exact empty-reference first-collision operator on finite XOR diagonal segments.
A segment is (base, drift, length); point terms have drift(0,0), length1.
No term or archive is dropped. No termination/capture claim for iteration.
"""
import json
from pathlib import Path
from check_fresh_record_trap_bridge import D,geometry,multiple
P=Path(__file__).parent
DATA=json.loads((P/'PRISTINE_COHORT_ADVANCE_CHECKED.json').read_text())
C=DATA['blank_prefix'];H=DATA['blank_tail_word'];T=len(C)
CP,CE,CH=geometry((0,0),0,C)
HP,HE,HH=geometry(CE,CH,H);DR=tuple(HE[j]-CE[j]for j in range(2))
HEAD=[];h=0
for a in C:HEAD.append(h);h=(h+(1 if a=='R'else-1))%4
HHEAD=[]
for a in H:HHEAD.append(h);h=(h+(1 if a=='R'else-1))%4
FIRST={}
for i,q in enumerate(CP):FIRST.setdefault(q,i)
FIRST=sorted([(t,q)for q,t in FIRST.items()])
E=set(map(tuple,DATA['blank_tail_state']['black']));M=set()
for q in HP:M^={q}

def rotate(v,r):
 x,y=v
 for _ in range(r%4):x,y=y,-x
 return(x,y)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def transform(v,p,h):
 r=rotate(v,h);return(p[0]+r[0],p[1]+r[1])
def contains(segments,x):
 parity=0
 for b,d,n in segments:
  if d==(0,0):hit=x==b
  else:
   k=multiple((x[0]-b[0],x[1]-b[1]),d);hit=k is not None and 0<=k<n
  parity^=bool(hit)
 return bool(parity)
def first_on_ray(segments,q,d):
 """First k>=0 with XOR board black at q+k*d, or None. No coordinate scan."""
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
   offset=multiple(z,d)
   if offset is None:continue
   sign=multiple(v,d);assert sign in(-1,1)
   end=offset+sign*(n-1);interval(min(offset,end),max(offset,end))
  else:
   det=cross(d,v);ka=cross(z,v);ja=cross(z,d)
   if ka%det or ja%det:continue
   k=ka//det;j=ja//det
   if 0<=j<n:interval(k,k)
 parity=0
 for k in sorted(changes):
  parity^=changes[k]
  if parity:return k
 return None

def emission(t,p,h):
 """Complete blank black field BEFORE update t, as exact finite XOR terms."""
 terms=[]
 if t<=T:
  mask=set()
  for q in CP[:t]:mask^={q}
  terms=[(q,(0,0),1)for q in sorted(mask)]
 else:
  k,r=divmod(t-T,104);terms=[(q,(0,0),1)for q in sorted(E)]
  if k:terms +=[(q,DR,k)for q in sorted(M)]
  mask=set()
  for q in HP[:r]:mask^={q}
  terms +=[((q[0]+k*DR[0],q[1]+k*DR[1]),(0,0),1)for q in sorted(mask)]
 return[(transform(b,p,h),rotate(d,h),n)for b,d,n in terms]

def next_collision(segments,p=(0,0),h=0):
 """First old black read; exact emitted field; actual L successor. None means certified blank capture."""
 hit=None
 for t,q in FIRST:
  x=transform(q,p,h)
  if contains(segments,x):hit=(t,x,(HEAD[t]+h)%4);break
 if hit is None:
  d=rotate(DR,h)
  for i,q in enumerate(HP):
   x=transform(q,p,h);k=first_on_ray(segments,x,d)
   if k is not None:
    candidate=(T+104*k+i,(x[0]+k*d[0],x[1]+k*d[1]),(HHEAD[i]+h)%4)
    if hit is None or candidate[0]<hit[0]:hit=candidate
 if hit is None:return dict(kind='no old contact; exact blank-prefix and standard tail forever',reference_prefix_duration=T,canonical_drift=rotate(DR,h))
 t,x,hin=hit;out=emission(t,p,h);assert not contains(out,x)
 hout=(hin-1)%4;pout=(x[0]+D[hout][0],x[1]+D[hout][1])
 return dict(kind='collision',blank_duration=t,total_duration=t+1,consumed_cell=x,incoming_heading=hin,new_pose=(pout,hout),emitted_terms=out,new_terms=segments+out+[(x,(0,0),1)])

def materialize(segments):
 B=set()
 for b,d,n in segments:
  for j in range(n):B^={(b[0]+j*d[0],b[1]+j*d[1])}
 return B

def blank_birth(q,t):
 """Last R birth at q in the canonical emission E_t. Caller requires q black in E_t."""
 latest=None
 for i,x in enumerate(CP[:min(t,T)]):
  if x==q:latest=(i,C[i])
 if t>T:
  for i,x in enumerate(HP):
   k=multiple((q[0]-x[0],q[1]-x[1]),DR)
   if k is not None and k>=0:
    when=T+104*k+i
    if when<t and(latest is None or when>latest[0]):latest=(when,H[i])
 assert latest is not None and latest[1]=='R'
 return latest[0]
