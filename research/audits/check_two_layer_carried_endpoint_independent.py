from pathlib import Path
from itertools import product
import sys,hashlib,json
import sympy as S
ROOT=Path('/workspace/shared/langton');SELF=Path(__file__).resolve();D=ROOT/'new_constructive_2026-10-23'
sys.path.insert(0,str(ROOT/'computability/unit_inductive_certificates'));from presburger_read_set_solver import Context
C=Context(max_operations=100000000);r,k,i,j=S.symbols('r k i j',integer=True)
def rot(v):return(v[1],-v[0])
def add(a,b):return tuple(S.expand(x+y)for x,y in zip(a,b))
def scale(n,a):return tuple(S.expand(n*x)for x in a)
def literal(w,h):
 p=(0,0);rd=[]
 for ch in w:
  rd.append((p,ch));h=rot(h)if ch=='R'else scale(-1,rot(h));p=add(p,h)
 return rd,p,h
def domain(f,lower=10):
 p,n,t,ch=f;return C.set('[r,k]->{[x,y]:r>='+str(lower)+' and k>='+str(lower)+' and exists(i:0<=i<'+str(n)+' and x='+str(p[0])+' and y='+str(p[1])+')}')
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def compile(stages,p=(0,0),h=(1,0)):
 ans=[];time=0;charge=0
 for w,n in stages:
  rd,d,hh=literal(w,h)
  if n!=1:assert hh==h and d!=(0,0)
  for slot,(z,ch)in enumerate(rd):ans.append((add(add(p,scale(i,d)),z),n,S.expand(time+i*len(w)+slot),ch))
  p=add(p,scale(n,d));time=S.expand(time+n*len(w));charge=S.expand(charge+n*(w.count('R')-w.count('L')));h=hh
 return ans,p,h,time,charge
def frame(s):return compile([x for _ in range(4)for x in [('LRRL',r),('RL',k+s),('R',1)]],p=(0,s))[0]
empty=C.set('[r,k]->{[x,y]:false}')
def union(fs,ch=None,lower=10):
 a=empty
 for f in fs:
  if ch is None or f[3]==ch:a=a.union(domain(f,lower))
 return a.coalesce()
ff=[frame(s)for s in(0,1,2)];I=[union(fs,'L')for fs in ff];read0=union(ff[0]);assert I[0].intersect(I[2]).is_empty()and I[1].intersect(I[2]).is_empty()and read0.intersect(I[2]).is_empty();assert union(ff[0],'R').is_equal(I[1])
# Also check the asserted all-nonnegative outer ownership without relying on r,k>=10.
assert union(ff[0],lower=0).intersect(union(ff[2],'L',lower=0)).is_empty()
for aa,bb in product(range(28),repeat=2):
 if aa<bb:assert domain(ff[0][aa],0).intersect(domain(ff[0][bb],0)).is_empty()
A='RRRLLLLRLLLLRLRRRRLR';B='LLLLRRRRLR';CC='RRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLRLRRRRLLLLRLRRRRLRRRRLLLLRLR';Z='RRLRRRRLLLLRLLLLRLRRRRLRR';assert tuple(map(len,(A,B,CC,Z)))==(20,10,64,25)
stages=[(A,r),(B,1)]+[x for _ in range(3)for x in [('RL',k+2),('RRLL',r-1),('RRLRL',1)]]+[('RL',k-1),('R',1),(CC,1),('LRRL',r-1),('LLL',1),('RRLL',r-2),(Z,1)]
fs,p,h,tm,charge=compile(stages);assert len(fs)==166 and p==(0,2)and h==(1,0)and tm==40*r+8*k+104 and charge==16
initial=I[1].union(I[2]).coalesce();domains=[domain(f)for f in fs];pairs=nonempty=0
for a,(pos,n,tm,ch)in enumerate(fs):
 C.reset_operations();current=initial.intersect(domains[a])
 # Each family's copy position is injective (or its count is exactly1).
 if n!=1:assert any(S.expand(z).coeff(i)!=0 for z in pos)
 for b,(q,m,t,_)in enumerate(fs):
  if a==b:continue
  pairs+=1
  if domains[a].intersect(domains[b]).is_empty():continue
  q=tuple(S.sympify(z).subs(i,j)for z in q);t=S.sympify(t).subs(i,j)
  formula='[r,k]->{[x,y]:r>=10 and k>=10 and exists(i,j:0<=i<'+str(n)+' and 0<=j<'+str(m)+' and x='+str(pos[0])+' and y='+str(pos[1])+' and x='+str(q[0])+' and y='+str(q[1])+' and '+str(S.expand(t-tm))+'<0)}'
  prev=C.set(formula)
  if not prev.is_empty():current=xor(current,prev);nonempty+=1
 bad=domains[a].subtract(current)if ch=='L'else current
 assert bad.is_empty(),(a,str(bad))
ret=initial
for dom in domains:ret=xor(ret,dom)
author=json.loads((D/'two_layer_carried_endpoint.json').read_text());assert ret.is_equal(C.set(author['returned_relation']))and initial.is_equal(C.set(author['initial_relation']));assert pairs==27390 and nonempty==212
# Literal controls start from independently inferred first-L frame seeds.
def minframe(rr,kk,dy=0):
 p=complex(0,dy);h=1+0j;black=set();seen=set()
 for ch in ('LRRL'*rr+'RL'*kk+'R')*4:
  assert p not in seen;seen.add(p)
  if ch=='L':black.add(p)
  h*=(-1j if ch=='R'else 1j);p+=h
 return black
checks=[]
for rr,kk in[(10,10),(10,11),(13,17)]:
 board=minframe(rr,kk)|minframe(rr,kk+2,2);assert len(board)==16*rr+8*kk+8;p=0j;h=1+0j;N=0
 words=[('LRRL'*rr+'RL'*kk+'R')*4]+[w*int(S.sympify(n).subs({r:rr,k:kk}))for w,n in stages]
 for w in words:
  for ch in w:
   assert(ch=='L')==(p in board);board.symmetric_difference_update({p});h*=(-1j if ch=='R'else 1j);p+=h;N+=1
 assert p==2j and h==1 and N==56*rr+16*kk+108 and len(board)==16*rr+8*kk+28
 checks.append(dict(r=rr,k=kk,reads=N,initial_mass=16*rr+8*kk+8,final_mass=len(board)))
note=D/'two_layer_carried_endpoint.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='4f7337113a8992351d6b3bdbc8d16d36b4d29209e3c1bef809cd1f212ad61416'
out=dict(status='PASS all-r,k two-layer actual carried-endpoint finite excursion',note_sha256=sha,domain='integer r,k>=10; first outer ownership also allr,k>=0',families=len(fs),ordered_pairs=pairs,nonempty_prior_relations=nonempty,continuation_reads='40r+8k+104',total_reads='56r+16k+108',start=[0,0,'E'],end=[0,2,'E'],initial_mass='16r+8k+8',final_mass='16r+8k+28',complete_initial_relation=str(initial),complete_returned_relation=str(ret),literal_controls=checks,analytic='Independent literal heading-vector/Sympy compiler uses existential i,j strict temporal read comparisons, not author inverse-time formula. Every family is injective, every initial black and earlier same-cell read is included, and complete output is initial XOR every read domain. Full returned relation exactly equals frozen supplied contract.',scope='Finite two-layer supplied component, not a clean reset, renewal, all-family capture or counterexample. Separate r=k10 author capture is not used by this all-parameter proof.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(pairs,nonempty,checks)
