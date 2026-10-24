"""Exploratory opposed clean half-wakes, exact infinite fields.

Both are canonical mature incoming-past profiles; the abandoned tip ahead is
rotated180degrees. This is NOT a finite-seed theorem, and no family coverage
is claimed until every normalization and finite-tail guard is checked.
"""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'transverse'))
import crossing as c

def abandoned(a,z,n=20,rotation=2):
 v=c.plus((a,a-z),c.times(n,c.D))
 return [(c.plus(v,c.rotate(b,rotation)),c.rotate(d,rotation),lo,hi) for b,d,lo,hi in c.incoming_past()]

def first_contact(static):
 earliest=None
 for i,q in enumerate(c.READS):
  edges=set()
  for b,e,lo,hi in static:
   v=c.intersect(q,c.D,b,e,lo,hi)
   if v:
    lo,hi=v;edges.symmetric_difference_update({lo})
    if hi is not None:edges.symmetric_difference_update({hi+1})
  if edges:
   t=104*min(edges)+i
   if earliest is None or t<earliest:earliest=t
 return earliest

def run(a,z,n=20,cap=400000):
 static=abandoned(a,z,n);t0=first_contact(static)
 if t0 is None:return dict(a=a,z=z,n=n,status='no contact')
 f=c.Field(c.incoming_past()+static);p=(0,0);h=c.H0;letters=[];readset=set()
 for t in range(cap):
  readset.add(p);p,h,ch=f.step(p,h);letters.append(ch)
  if t<t0:assert ch==c.WORD[t%104]
  if t==t0:assert ch!=c.WORD[t%104]
  if t>t0+312 and (t-t0)%104==0:
   last=''.join(letters[-312:]);w=last[-104:]
   if last[-12:] in ('RL'*6,'LR'*6):w=last[-4:]
   if w in c.PHASES and last==w*3 or len(w)==4:
    cert=c.tail(f,p,h,w)
    if cert:return dict(a=a,z=z,n=n,sector='same' if z%2==0 else 'opposite',t0=t0,capture=t+1,recovery=t+1-t0,pose=(p,h),tail=cert,read_count=len(readset),changes=len(f.changes),word=''.join(letters[t0:]))
 return dict(a=a,z=z,n=n,sector='same' if z%2==0 else 'opposite',t0=t0,status='cap',p=p,h=h,read_count=len(readset),changes=len(f.changes))

if __name__=='__main__':
 rows=[]
 for z in range(-20,21):
  for a in (0,1):
   row=run(a,z);rows.append(row)
   print(json.dumps({k:v for k,v in row.items() if k!='word'}),flush=True)
   (HERE/'discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
