from pathlib import Path
from collections import defaultdict,Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'causal_archive_frontier_2026-10-23';K={q for q,b in walk(mark)[2].items()if b};G={}
for s in(4,6,9):
 e,h,_,flip=walk(raws[s]);r=walk(raws[s]+mark)[2];bl={q for q,b in r.items()if b};G[s]=(bl-K,(bl^flip)-{e+rotation(q,h)for q in K},r);assert raws[s].startswith(mark)
FIX=K|G[9][0];assert len(FIX)==10

def trace(word,p=0j,h=0):
 rows=[]
 for time,ch in enumerate(word):rows.append((p,ch,time));h=(h+(1 if ch=='R'else-1))%4;p+=rotation(1j,h)
 return rows,p,h
# Generate local affine cell families by actual translated/rotated raw traces.
slots=[]
for group,word,p,h in [(0,raws[9],0j,0),(1,raws[4],-1+5j,2),(2,raws[6],-1+5j,2),(3,raws[4],-1+1j,0),(4,mark,-2-2j,0)]:
 rr,_,_=trace(word,p,h)
 for q,ch,time in rr:
  t=int(q.imag-3*q.real);a=-int(q.real);key=time-18*a if group==1 else time+18*a if group==3 else time;slots.append((group,t,a,key,ch))
left_break=[];right_break=[]
for g,t,a,key,ch in slots:
 if g in(0,4):left_break.append(a)
 elif g==2:right_break.append(a)
 elif g==1:left_break.append(a);right_break.append(a-1)
 else:left_break.append(2+a);right_break.append(a)
left_break +=[-int(q.real)for q in FIX]+[1,2,2];right_break +=[1,2,0]
assert max(map(abs,left_break+right_break))==4
normals=sorted({t for g,t,a,key,ch in slots}|{int(q.imag-3*q.real)for q in FIX}|{3,5,9})
def seq(t,u,N):
 hits=[]
 for g,tt,a,key,ch in slots:
  if tt!=t:continue
  active=u==a if g in(0,4)else u==N+a if g==2 else a<=u<=N+a-1 if g==1 else 2+a<=u<=N+a
  if active:hits.append((g,key,ch))
 return ''.join(x[2]for x in sorted(hits))
def seed(t,u,N):return complex(-u,t-3*u)in FIX or t==5 and 1<=u<=N+1 or t==9 and 2<=u<=N+2 or t==3 and 2<=u<=N
def check(t,u,N):
 w=seq(t,u,N);assert all(x!=y for x,y in zip(w,w[1:]));assert seed(t,u,N)==bool(w and w[0]=='L');return (t,u,w,bool(seed(t,u,N)))
small=[]
for N in range(1,10):
 rows=[check(t,u,N)for t in normals for u in range(-4,N+5)];assert sum(x[3]for x in rows)==3*N+10;small.append(dict(N=N,cells=rows))
left=[check(t,u,10)for t in normals for u in range(-4,5)];bulk=[check(t,5,10)for t in normals];right=[check(t,10+v,10)for t in normals for v in range(-4,5)]
assert sum(x[3]for x in bulk)==3 and sum(x[3]for x in left+right)==37
# Exact regime inequalities for every slot, not a sampled large-N assumption.
for g,t,a,key,ch in slots:
 if g in(0,4):assert -4<=a<=4 # fixed points excluded from right/bulk
 elif g==2:assert -4<=a<=4 # N+a beyond left/bulk
 elif g==1:assert -4<=a<=4 and -4<=a-1<=4 # both moving interval boundaries
 else:assert -4<=2+a<=4 and -4<=a<=4
# Thus for N>=10: left eligibility is just left threshold; right just right;
# bulk includes every interval role and no fixed/far role. No other u can read.
# Exact identity family at t=7: only out/far O(0,1), only return I(0,3).
for s in(4,6):
 I,O,_=G[s]
 for kind,points in [('I',I),('O',O)]:
  hits=[q for q in points if int((-1+5j+rotation(q,2)).imag-3*(-1+5j+rotation(q,2)).real)==7]
  assert hits==([1j]if kind=='O'else[])
I,O,_=G[4];assert[q for q in I if int((-1+1j+q).imag-3*(-1+1j+q).real)==7]==[3j]
assert not[q for q in O if int((-1+1j+q).imag-3*(-1+1j+q).real)==7]
assert not[q for q in G[9][1]if int(q.imag-3*q.real)==7 and -q.real>=3]
controls=[]
for N in(1,2,3,10,100):
 S=FIX|{-1-i+(2-3*i)*1j for i in range(N+1)}|{-2-i+(3-3*i)*1j for i in range(N+1)}|{-k+(3-3*k)*1j for k in range(2,N+1)};assert len(S)==3*N+10
 board=set(S);ids={q:None for q in S-K};p=0j;h=0;clock=0;cut=None;consumed=[];ticks=0
 for j,s in enumerate([9]+[4]*N+[6]+[4]*(N-1)):
  I,O,req=G[s]
  assert board==ids.keys()|{p+rotation(q,h)for q in K}
  assert all((p+rotation(q,h)in board)==bool(b)for q,b in req.items())
  for q in I:
   cell=p+rotation(q,h);tag=ids.pop(cell)
   if tag is not None:consumed.append((j,xy(cell),clock-tag[0],tag[1]))
  for q in O:
   cell=p+rotation(q,h);assert cell not in ids;ids[cell]=(clock,j)
  for ch in raws[s]:
   assert(p in board)==(ch=='L');board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=rotation(1j,h);ticks+=1
  clock+=2 if s in(6,9) else 0
  if j==N+1:
   cut=dict(head=xy(p),h=h,C=clock,residual=len(ids),produced=sum(x is not None for x in ids.values()),entry=sum(x is None for x in ids.values()))
   assert cut==dict(head=(-1-N,1-3*N),h=0,C=4,residual=7*N+25,produced=6*N+26,entry=N-1)
 future=[x for x in consumed if x[0]>N+1];assert len(future)==N-1 and [x[1]for x in future]==[(-1-k,4-3*k)for k in range(N,1,-1)]and all(x[2]==2 for x in future)
 for ch in mark:
  assert(p in board)==(ch=='L');board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=rotation(1j,h)
 assert ticks==36*N+88;controls.append(dict(N=N,initial_mass=len(S),cut=cut,later_produced_consumptions=future))
ref=json.loads((D/'rail_frontier_family_controls.json').read_text());assert len(slots)==len(ref['all_local_slots']);groups={0:'initial',1:'out',2:'far',3:'return',4:'marker'}
assert{(groups[g],t,a,key,ch)for g,t,a,key,ch in slots}=={(r['group'],r['normal'],r['shift'],r['key'],r['letter'])for r in ref['all_local_slots']}
out=dict(status='PASS independent all-N young-rail affine seam proof and current-ID reuse',note_sha256=hashlib.sha256((D/'young_rail_reuse_all_N.md').read_bytes()).hexdigest(),K=4,N0=10,local_slots=slots,universal_left=left,universal_bulk=bulk,universal_right=right,small_cases=small,controls=controls,all_N_counts='mass3N+10, raw36N+88; farVCC cutC4 residual7N+25, produced6N+26, entryN-1. N-1 later reused IDs have age2 and remotest distance3N-3.',scope='Actual complete-eight factors with growing entry mass/radius and still-active entry funding. Refutes age-only uniformly bounded locality/token count, not post-expiration or fixed-input-board frontier, nor capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['note_sha256'])
