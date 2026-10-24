"""Exact finite-seam proof controls for UCC V^N VCC V^(N-1), every N>=1.

All-N completeness follows from the affine orbit-list partition proved in the
companion note. This is not extrapolation from finite word simulations.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
D=Path(__file__).resolve().parent;R=D.parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];CORE=set(map(tuple,J['core']))
DIR=((0,1),(1,0),(0,-1),(-1,0));MARK=G[0]['marker']
def rot(z,h):
 x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def rawslots(w):
 p=(0,0);h=0;out=[]
 for tick,ch in enumerate(w):
  out.append((p,ch,tick));h=(h+(-1 if ch=='L' else 1))%4;p=add(p,DIR[h])
 return out
# Coordinates of a physical cell: t=y-3x, u=-x. Translation(-1,-3)
# increments u once and keeps t fixed. The group A/B/C eligibility is exact.
slots=[]
for p,ch,tick in rawslots(G[9]['word']):
 x,y=p;slots.append(dict(group='initial',normal=y-3*x,shift=-x,letter=ch,key=tick))
for p,ch,tick in rawslots(G[4]['word']):
 x,y=p;alpha=1+x;slots.append(dict(group='out',normal=8+3*x-y,shift=alpha,letter=ch,key=tick-18*alpha))
for p,ch,tick in rawslots(G[6]['word']):
 x,y=p;slots.append(dict(group='far',normal=8+3*x-y,shift=1+x,letter=ch,key=tick))
for p,ch,tick in rawslots(G[4]['word']):
 x,y=p;beta=1-x;slots.append(dict(group='return',normal=4+y-3*x,shift=beta,letter=ch,key=tick+18*beta))
for p,ch,tick in rawslots(MARK):
 x,y=p;slots.append(dict(group='marker',normal=4+y-3*x,shift=2-x,letter=ch,key=tick))
ORDER={'initial':0,'out':1,'far':2,'return':3,'marker':4}
# All left-boundary breakpoints and right-relative breakpoints are in[-K,K].
breaks=[]
for s in slots:
 a=s['shift'];g=s['group']
 breaks += [a] if g in('initial','marker','far') else [a,a-1] if g=='out' else [2+a,a]
# Include initial seed fixed cells and all three seed-rail interval endpoints.
FIXED=CORE|set(map(tuple,G[9]['inputs']));assert len(FIXED)==10
breaks += [-q[0]for q in FIXED]+[1,1,2,2,2,0]
K=max(map(abs,breaks));assert K==4
N0=2*K+2;assert N0==10
NORMALS=sorted({s['normal']for s in slots}|{q[1]-3*q[0]for q in FIXED}|{3,5,9})
def enabled(s,u,n):
 a=s['shift'];g=s['group']
 if g in('initial','marker'):return u==a
 if g=='out':return a<=u<=n-1+a
 if g=='far':return u==n+a
 if g=='return':return 2+a<=u<=n+a
 assert False

def seq(t,u,n):
 ss=[s for s in slots if s['normal']==t and enabled(s,u,n)]
 ss.sort(key=lambda s:(ORDER[s['group']],s['key']))
 return ''.join(s['letter']for s in ss)
def seed(t,u,n):
 q=(-u,t-3*u)
 return q in FIXED or (t==5 and 1<=u<=n+1) or(t==9 and 2<=u<=n+2)or(t==3 and 2<=u<=n)

def checkcell(t,u,n):
 w=seq(t,u,n)
 assert all(w[j]!=w[j+1]for j in range(len(w)-1)),(n,t,u,w)
 assert seed(t,u,n)==bool(w and w[0]=='L'),(n,t,u,w,'seed')
 return dict(normal=t,axial=u,word=w,initial_black=seed(t,u,n))
small=[]
for n in range(1,N0):
 rows=[checkcell(t,u,n)for t in NORMALS for u in range(-K,n+K+1)]
 m=sum(r['initial_black']for r in rows);assert m==3*n+10
 small.append(dict(N=n,mass=m,cells=rows))
# The affine eligibility partition makes these three lists universal for N>=10.
left=[checkcell(t,u,N0)for t in NORMALS for u in range(-K,K+1)]
bulk=[checkcell(t,K+1,N0)for t in NORMALS]
right=[dict(relative_axial=v,**checkcell(t,N0+v,N0))for t in NORMALS for v in range(-K,K+1)]
assert sum(r['initial_black']for r in bulk)==3
assert sum(r['initial_black']for r in left+right)==37
# Explicit symbolic-template invariance checks, with eligibility expressions
# unchanged on the three proven ranges (see note); these extra n are controls.
for n in(11,17,100):
 for r in left:assert seq(r['normal'],r['axial'],n)==r['word']and seed(r['normal'],r['axial'],n)==r['initial_black']
 for r in right:assert seq(r['normal'],n+r['relative_axial'],n)==r['word']and seed(r['normal'],n+r['relative_axial'],n)==r['initial_black']
 for u in range(K+1,n-K):
  for r in bulk:assert seq(r['normal'],u,n)==r['word']and seed(r['normal'],u,n)==r['initial_black']
# Direct raw chronology and fresh identity controls independently of orbit lists.
controls=[]
for n in(1,2,3,4,10,23,100):
 S=set(FIXED)|{(-1-i,2-3*i)for i in range(n+1)}|{(-2-i,3-3*i)for i in range(n+1)}|{(-k,3-3*k)for k in range(2,n+1)}
 assert len(S)==3*n+10
 packets=[9]+[4]*n+[6]+[4]*(n-1);program=''.join(G[a]['word']for a in packets)+MARK
 B=set(S);p=(0,0);h=0;T={q:('entry',None,None)for q in S-CORE};c=0;tick=0;produced=[];cut=None
 for j,a in enumerate(packets):
  before=set(B);currentcore={add(p,rot(q,h))for q in CORE};assert before==currentcore|set(T)and not currentcore&set(T)
  for x,y,b,*_ in G[a]['requirements']:assert(add(p,rot((x,y),h))in B)==bool(b)
  for i in G[a]['inputs']:
   q=add(p,rot(i,h));tag=T.pop(q)
   if tag[0]=='produced':produced.append(dict(consumer=j,source=tag[2],cell=q,age=c-tag[1]))
  for o in G[a]['outputs']:
   q=add(p,rot(o,h));assert q not in T;T[q]=('produced',c,j)
  for ch in G[a]['word']:
   isblack=p in B;assert isblack==(ch=='L')
   if isblack:B.remove(p)
   else:B.add(p)
   h=(h+(-1 if isblack else 1))%4;p=add(p,DIR[h]);tick+=1
  c+=G[a]['name'].count('C');aftercore={add(p,rot(q,h))for q in CORE};assert B==aftercore|set(T)and not aftercore&set(T)
  if j==n+1:
   cut=dict(head=p,heading=h,C=c,residual=len(T),produced=sum(tag[0]=='produced'for tag in T.values()),entry=sum(tag[0]=='entry'for tag in T.values()))
   assert cut==dict(head=(-1-n,1-3*n),heading=0,C=4,residual=7*n+25,produced=6*n+26,entry=n-1)
 future=[z for z in produced if z['consumer']>n+1];assert len(future)==n-1
 assert [z['cell']for z in future]==[(-1-k,4-3*k)for k in range(n,1,-1)]and all(z['age']==2 for z in produced)
 for ch in MARK:
  isblack=p in B;assert isblack==(ch=='L')
  if isblack:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if isblack else 1))%4;p=add(p,DIR[h])
 assert tick==36*n+88
 controls.append(dict(N=n,entry_mass=len(S),raw_length=tick,C=c,cut=cut,future_produced_inputs=future))
out=dict(status='AUTHOR_ALL_N_AFFINE_ORBIT_LIST_FINITE_SEAM_CERTIFICATE',scope='Actual finite seeds with mass3N+10; C=4 and young produced archive of unbounded spatial extent. Entry roots still fund return, so not a post-entry-expiration counterexample or noncapture.',word='UCC V^N VCC V^(N-1), N>=1',K=K,N0=N0,small_cases=small,universal_left=left,universal_bulk=bulk,universal_right=right,all_local_slots=slots,controls=controls,geometry_sha256=hashlib.sha256(GP.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(D/'rail_frontier_family_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in('status','scope','word','K','N0')},indent=2));print('PASS exact finite seams; mass=3N+10, raw=36N+88, cut produced=6N+26; future N-1 produced reads age2.')
