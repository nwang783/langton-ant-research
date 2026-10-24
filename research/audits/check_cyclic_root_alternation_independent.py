"""No-import finite-state proof for two infinite-background substitution paths.
Rebuild joint controls and Euclidean carry closure directly from literal turns.
No claim of finite initial support.
"""
from pathlib import Path
import json,math,hashlib,time
ROOT=Path('/workspace/shared/langton')
PAIRS=[('LRLRLRRLRLRLRLRRL','RLRRLRRLRLRLRLRLR'),('LRLRLRLRLRLRRLRRL','RLRRLRLRLRLRRLRLR')]

def pairmul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def minus(a,b):return(a[0]-b[0],a[1]-b[1])
def square(a):return a[0]*a[0]+a[1]*a[1]
def literal(w):
 p=(0,0);h=(0,1);r=[]
 for c in w:
  r.append((p,h,c));h=pairmul(h,(0,-1) if c=='R' else (0,1));p=plus(p,h)
 return r,p,h

def verify(u,v):
 words={'R':u,'L':v};tr={c:literal(w) for c,w in words.items()};a=tr['R'][1];k=len(u)
 assert len(v)==k and u[0]=='L' and v[0]=='R'
 assert tr['R'][2]==(1,0) and tr['L'][2]==(-1,0) and tr['L'][1]==(-a[0],-a[1])
 # Rotation from north to h is complex multiplication by h/i.
 states=[((0,1),'R',(0,1),'L')];index={states[0]:0};nxt=[];offs=[]
 for hr,cr,hl,cl in states:
  row=[];offsetrow=[]
  for j in range(k):
   pr,qr,lr=tr[cr][0][j];pl,ql,ll=tr[cl][0][j]
   rotr=pairmul(hr,(0,-1));rotl=pairmul(hl,(0,-1))
   state=(pairmul(rotl,ql),ll,pairmul(rotr,qr),lr)
   if state not in index:index[state]=len(states);states.append(state)
   row.append(index[state]);offsetrow.append((pairmul(rotl,pl),pairmul(rotr,pr)))
  nxt.append(row);offs.append(offsetrow)
 assert len(states)==20 and nxt[0][0]==0 and offs[0][0]==((0,0),(0,0))
 # Independent literal controls for both fixed points of the squared substitution.
 def control(n):
  ds=[]
  while n:ds.append(n%k);n//=k
  s=0
  for d in reversed(ds):s=nxt[s][d]
  return s
 def point(n,c):
  if n==0:return(0,0)
  q,j=divmod(n,k)
  return plus(pairmul(a,point(q,1-c)),offs[control(q)][j][c])
 for c,root in enumerate('RL'):
  w=root
  for _ in range(2):
   w=''.join(words[z] for z in w);w=''.join(words[z] for z in w)
  raw,_,_=literal(w)
  for n,(p,h,z) in enumerate(raw[:4096]):
   st=states[control(n)]
   assert point(n,c)==p and st[2*c:2*c+2]==(h,z)
 max2=max(square(z) for row in offs for cell in row for z in cell)
 ceil=math.isqrt(max2)+(math.isqrt(max2)**2<max2);delta=2*ceil
 radius=0
 while square(a)*radius*radius<(radius+delta)**2:radius+=1
 work=[(0,0,c,0,0,False) for c in (0,1)];seen=set(work);edges=overflow=0;equal_opposite=0
 for s,t,c,x,y,less in work:
  if less and x==0 and y==0:
   assert states[s][2*c+1]!=states[t][2*c+1]
   equal_opposite+=1
  cc=1-c;adx,ady=pairmul(a,(x,y))
  for d in range(k):
   bx,by=offs[s][d][cc]
   for e in range(0 if less else d,k):
    edges+=1;cx,cy=offs[t][e][cc];xx,yy=adx+bx-cx,ady+by-cy
    if xx*xx+yy*yy>radius*radius:overflow+=1;continue
    ns=(nxt[s][d],nxt[t][e],cc,xx,yy,less or d<e)
    if ns not in seen:seen.add(ns);work.append(ns)
 # Compare only the resulting invariants, not implementation internals.
 return dict(R=u,L=v,scale=a,controls=len(states),radius=radius,closed_states=len(seen),checked_edges=edges,overflow_edges=overflow,opposite_turn_equal_cell_states=equal_opposite,literal_controls=8192)

start=time.monotonic();out=[]
reference=json.loads((ROOT/'computability/cyclic_root_alternation_certificate.json').read_text())['cases']
for u,v in PAIRS:
 r=verify(u,v);expected=next(z for z in reference if z['R']==u and z['L']==v)
 for a,b in [('controls','control_states'),('radius','carry_radius'),('closed_states','closed_states'),('checked_edges','checked_edges'),('overflow_edges','overflow_edges')]:assert r[a]==expected[b],(a,r[a],expected[b])
 out.append(r);print(json.dumps(r),flush=True)
result={'status':'independently verified infinite-background alternation; no finite-seed realization','cases':out,'seconds':time.monotonic()-start,'source_certificate_sha256':hashlib.sha256((ROOT/'computability/cyclic_root_alternation_certificate.json').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
