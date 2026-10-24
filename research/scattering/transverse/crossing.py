"""Discovery simulator and exact future validator on XOR periodic line/ray fields.

No finite-support theorem follows without additional geometric guards.
"""
import json,sys
from pathlib import Path
from collections import defaultdict
from bisect import bisect_right
BASE=Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json')
DATA=json.loads(BASE.read_text());WORD=DATA['word'];H0=DATA['heading'];D=tuple(DATA['drift'])
DIRS=((0,1),(1,0),(0,-1),(-1,0))
PHASES={WORD[i:]+WORD[:i]:i for i in range(104)}

def rotate(p,j):
 x,y=p
 for _ in range(j%4):x,y=y,-x
 return x,y

def plus(p,q):return p[0]+q[0],p[1]+q[1]
def minus(p,q):return p[0]-q[0],p[1]-q[1]
def times(k,p):return k*p[0],k*p[1]
def multiple(p,d):
 i=0 if d[0] else 1
 if p[i]%d[i]:return None
 k=p[i]//d[i]
 return k if times(k,d)==p else None

def trace(word,h=H0,p=(0,0)):
 reads=[]
 for c in word:
  reads.append(p);h=(h+(1 if c=='R' else -1))%4;p=plus(p,DIRS[h])
 return reads,p,h
READS,END,EH=trace(WORD);assert END==D and EH==H0

def orbitkey(q,d):
 # d has components +/-2, sign normalized along d.x.
 residue=q[0]%2;k=(q[0]-residue)//d[0]
 return minus(q,times(k,d)),k

def settled_lines(rotation,offset=(0,0)):
 groups=defaultdict(int);d=rotate(D,rotation)
 for q in READS:
  q=plus(rotate(q,rotation),offset);key,k=orbitkey(q,d);groups[key]^=1
 return [(key,d,None,None) for key,bit in groups.items() if bit]

def incoming_past():
 # Past periods indexed j<0; each phase contributes q+jD. XOR overlap exact.
 return [(minus(q,D),times(-1,D),0,None) for q in READS]

class Field:
 def __init__(self,rays=(),changes=()):
  self.rays=list(rays);self.changes=set(changes);acc={}
  for base,d,lo,hi in self.rays:
   e=d if d[0]>0 else times(-1,d);key,z=orbitkey(base,e)
   if d==e:a=None if lo is None else z+lo;b=None if hi is None else z+hi
   else:a=None if hi is None else z-hi;b=None if lo is None else z-lo
   v=acc.setdefault((e,key),[False,set()])
   if a is None:v[0]^=True
   else:v[1].symmetric_difference_update({a})
   if b is not None:v[1].symmetric_difference_update({b+1})
  self.index={key:(v[0],sorted(v[1])) for key,v in acc.items()}
  self.directions=set(key[0] for key in self.index)
 def background(self,p):
  bit=False
  for d in self.directions:
   key,z=orbitkey(p,d)
   base,edges=self.index.get((d,key),(False,()))
   bit^=base^(bisect_right(edges,z)%2!=0)
  return bit
 def color(self,p):return self.background(p)^(p in self.changes)
 def flip(self,p):self.changes.symmetric_difference_update({p})
 def step(self,p,h):
  c='L' if self.color(p) else 'R';self.flip(p)
  h=(h+(1 if c=='R' else -1))%4;return plus(p,DIRS[h]),h,c

def intersect(q,d,base,e,lo,hi):
 """Epoch interval k>=0 in q+k*d intersecting one line/ray/segment."""
 delta=minus(base,q);det=d[0]*e[1]-d[1]*e[0]
 if det:
  nk=delta[0]*e[1]-delta[1]*e[0];nj=delta[0]*d[1]-delta[1]*d[0]
  if nk%det or nj%det:return None
  k=nk//det;j=nj//det
  if k<0 or lo is not None and j<lo or hi is not None and j>hi:return None
  return k,k
 m=multiple(delta,d)
 if m is None:return None
 r=multiple(e,d);assert r in (-1,1)
 if r==1:a=None if lo is None else m+lo;b=None if hi is None else m+hi
 else:a=None if hi is None else m-hi;b=None if lo is None else m-lo
 a=0 if a is None else max(0,a)
 if b is not None and b<a:return None
 return a,b

def tail(field,p,h,word):
 if not word or not set(word)<={'R','L'}:return None
 qs,end,eh=trace(word,h,p);d=minus(end,p)
 if eh!=h or d==(0,0):return None
 checks=0
 for i,q in enumerate(qs):
  boundaries=set()
  def interval(v):
   if v is None:return
   l,r=v;boundaries.symmetric_difference_update({l})
   if r is not None:boundaries.symmetric_difference_update({r+1})
  if word[i]=='L':interval((0,None))
  for b,e,lo,hi in field.rays:interval(intersect(q,d,b,e,lo,hi))
  for b in field.changes:
   k=multiple(minus(b,q),d)
   if k is not None and k>=0:interval((k,k))
  for j,r in enumerate(qs):
   a=multiple(minus(r,q),d)
   if a is not None and (a>0 or a==0 and j<i):interval((a,None))
  checks+=1
  if boundaries:return None
 return {'period':len(word),'drift':d,'phase':PHASES.get(word),'ray_checks':checks}

def first_contact(rotation,a,s,n=20):
 offset=(a,s-a-4*n)
 static=settled_lines(rotation,offset)
 p=(0,0);h=H0
 staticf=Field(static)
 for t in range(104*(4*n+10)):
  if staticf.color(p):return t,p,h,static
  c=WORD[t%104];h=(h+(1 if c=='R' else -1))%4;p=plus(p,DIRS[h])
 raise AssertionError('no transverse contact')

def run(rotation,a,s,cap=300000):
 t0,p,h,static=first_contact(rotation,a,s)
 field=Field(incoming_past()+static)
 p=(0,0);h=H0;letters=[];readset=set();first=None
 for t in range(cap):
  readset.add(p)
  p,h,c=field.step(p,h);letters.append(c)
  if t<t0:assert c==WORD[t%104]
  if t==t0:assert c!=WORD[t%104];first=(t0,p,h)
  if t>t0+312 and (t-t0)%104==0:
   last=''.join(letters[-312:]);w=last[-104:]
   if last[-12:] in ('RL'*6,'LR'*6):w=last[-4:]
   if (w in PHASES and last==w*3) or len(w)==4:
    cert=tail(field,p,h,w)
    if cert:
     return dict(rotation=rotation,a=a,s=s,t0=t0,capture=t+1,recovery=t+1-t0,
       pose=(p,h),cert=cert,changes=len(field.changes),reads=len(readset),
       limits=[min(q[0] for q in readset),max(q[0] for q in readset),min(q[1] for q in readset),max(q[1] for q in readset)],
       word=''.join(letters[t0:]))
 return dict(rotation=rotation,a=a,s=s,t0=t0,status='cap',p=p,h=h,changes=len(field.changes))

if __name__=='__main__':
 # Control the infinite incoming past really supplies WORD forever.
 b=Field(incoming_past());assert tail(b,(0,0),H0,WORD)
 rows=[]
 for r in (1,3):
  for a in (0,1):
   for s in range(4):
    row=run(r,a,s);rows.append(row)
    print(json.dumps({k:v for k,v in row.items() if k!='word'}),flush=True)
    Path(__file__).with_name('crossings_discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
