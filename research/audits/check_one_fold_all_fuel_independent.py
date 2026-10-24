"""Independent exact downward sweep and conservative horizontal quotient.
Literal complex-heading geometry; separate first/last/source/tip fields.
"""
from pathlib import Path
from collections import deque
import json,itertools,hashlib
R=Path('/workspace/shared/langton');P=R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'
W={a:d['word']for a,d in json.loads(P.read_text()).items()}
DATA={}
for a in 'UVQB':
 p=0j;h=1j;events=[]
 for c in W[a]:
  events.append(((int(p.real),int(p.imag)),c));h*=(-1j if c=='R'else 1j);p+=h
 DATA[a]=(events,(int(p.real),int(p.imag)),h)
 assert h==(1j if a in'UV'else-1j)
 if a in'UV':assert max(q[1]for q,c in events)==p.imag and min(q[1]for q,c in events)==-1

# source tags1=old,2=fold,4=new; each record(first,last,sources,tip)
def packed(dx,dy,flags,f):return dx,dy,flags,tuple(sorted((x,y,*v)for(x,y),v in f.items()))
def unpack(s):return{(z[0],z[1]):tuple(z[2:])for z in s[3]}
def trim(dx,dy,flags,f):
 top=max(([0]if flags&1 else[])+([dy+1]if flags&2 else[]))
 f={q:v for q,v in f.items()if q[1]<=top}
 if flags==1 and not any(v[3]for v in f.values()):return None
 if flags==2 and not any(v[2]&3 for v in f.values()):return None
 return packed(dx,dy,flags,f)
SEAM={(0,0),(-1,-1),(0,-1),(1,0)}
MARKS={}
for a in DATA:
 first={}
 for q,c in DATA[a][0]:first.setdefault(q,c)
 assert SEAM <= {q for q,c in first.items() if c=='L'}
 MARKS[a]={q for q,c in first.items() if c=='L'}-SEAM
assert {a:len(v)for a,v in MARKS.items()}=={'U':5,'V':2,'Q':15,'B':18}
for a,b in list(itertools.product('UV',repeat=2))+list(itertools.product('UV','QB'))+list(itertools.product('QB','UV')):
 old={q for q,c in DATA[a][0]};ex,ey=DATA[a][1];h=DATA[a][2]
 transform=lambda q:(ex+q[0],ey+q[1])if h==1j else(ex-q[0],ey-q[1])
 assert {transform(q) for q in SEAM}<=old,(a,b)
 if a in'UV' and b in'UV':assert not {transform(q)for q in MARKS[b]}&old

def seed(a):
 f={}
 for q,c in DATA[a][0]:
  if q in f:
   first,last,tags,tip=f[q];assert last!=c;f[q]=(first,c,tags,tip)
  else:f[q]=(c,c,2,False)
 for q in MARKS[a]:
  first,last,tags,_=f[q];f[q]=(first,last,tags,True)
 dx,dy=DATA[a][1];return trim(dx,dy,3,f)
def exact_steps(s):
 dx,dy,flags=s[:3];f=unpack(s)
 if flags==3:
  for flag in[1,2]:
   q=trim(dx,dy,flag,f)
   if q is not None:yield 'stop'+str(flag),q,False
 prepend=(flags==1 or flags==3 and dy+1<=0)
 for a in'UV':
  events,(ex,ey),_=DATA[a];g=dict(f);hit=False
  if prepend:
   for (x,y),c in reversed(events):
    q=(x-ex,y-ey)
    if q in g:
     first,last,tags,tip=g[q]
     if first==c:break
     hit|=tip;g[q]=(c,last,tags|1,tip)
    else:g[q]=(c,c,1,False)
   else:
    g={(x+ex,y+ey):v for(x,y),v in g.items()};q=trim(dx+ex,dy+ey,flags,g)
    if q is not None or hit:yield 'X'+a,q,hit
  else:
   noses=[(dx-x,dy-y)for x,y in MARKS[a]]
   if any(q in g for q in noses):hit=True
   for (x,y),c in events:
    q=(dx-x,dy-y)
    if q in g:
     first,last,tags,tip=g[q]
     if last==c:break
     g[q]=(first,c,tags|4,tip)
    else:g[q]=(c,c,4,False)
   else:
    for nose in noses:
     first,last,tags,_=g[nose];g[nose]=(first,last,tags,True)
    q=trim(dx-ex,dy-ey,flags,g)
    if q is not None or hit:yield 'Y'+a,q,hit

def slide_new(s,k):
 dx,dy,flags=s[:3];f=unpack(s);g={}
 for (x,y),(first,last,tags,tip)in f.items():
  assert tags in(1,4),(s,tags)
  assert -2<=(x if tags==1 else x-dx)<=3
  q=(x+(k if tags==4 else 0),y);assert q not in g
  g[q]=(first,last,tags,tip)
 return packed(dx+k,dy,flags,g)
def abstract(s):
 dx=s[0]
 if abs(dx)<8:return s
 rep=(8+(dx-8)%4)if dx>0 else -(8+(-dx-8)%4)
 return slide_new(s,rep-dx)
def successors(s):
 if abs(s[0])>=8:slide_new(s,0)
 for action,t,hit in exact_steps(s):
  assert not hit,('V TIP REUSE',s,action)
  if s[0]==-8 and t[0]==-7:yield action,abstract(slide_new(t,-4))
  if s[0]==8 and t[0]==7:yield action,abstract(slide_new(t,4))
  yield action,abstract(t)
q=deque([seed('Q'),seed('B')]);seen={s:i for i,s in enumerate(q)};edges=[]
while q:
 s=q.popleft()
 for a,t in successors(s):
  if t not in seen:seen[t]=len(seen);q.append(t)
  edges.append((seen[s],a,seen[t]))
assert len(seen)==82 and len(edges)==147
out={'status':'PASS','states':len(seen),'edges':len(edges),'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'independent_representation':'literal complex headings and separate first/last/source/tip records','state_records':list(seen),'transitions':edges}
(R/'audits/one_fold_all_fuel_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS independent82-state147-edge all-fuel closure and exact seam decomposition')
