"""Independent residue-group transfer and exact scalar certificate audit.
Works in Z[C_q], reducing to a cyclotomic basis only at output.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'computability/unit_fourier';J=json.loads((F/'unit9_fourier.json').read_text());R=json.loads((F/'unit9_fourier.records.json').read_text());heads=(1j,1,-1j,-1)
def trace(word,head=1j):
 p=0j;reads=[]
 for s in word:
  reads.append((p,head,s));head*=(-1j if s=='R'else 1j);p+=head
 return reads,p,head

def reduce(v):
 q=len(v)
 if q==1:return v[:]
 if q in (2,3,5):return [x-v[-1]for x in v[:-1]]
 if q==4:return[v[0]-v[2],v[1]-v[3]]
 raise ValueError(q)
def initial(q):return [[(1 if s==0 else -1)if j==0 else 0 for j in range(q)]for h in heads for s in range(2)]
def action(images,a,r,q,u,v,z):
 out=[[0]*q for _ in range(8)]
 for hi,h in enumerate(heads):
  for s,word in enumerate(images):
   reads,end,last=trace(word,h)
   assert end==(1j**a)*h*(-1j if s==0 else 1j)and last==h*(-1j if s==0 else 1j)
   for p,hj,sj in reads:
    off=(1j**((a*r)%4))*p;shift=(u*int(off.real)+v*int(off.imag))%q
    src=z[2*heads.index(hj)+(sj=='L')];dest=out[2*hi+s]
    for n,c in enumerate(src):dest[(n+shift)%q]+=c
 return out

def literal(word,q,u,v,h=1j):
 out=[0]*q
 for p,hh,s in trace(word,h)[0]:out[(u*int(p.real)+v*int(p.imag))%q]+=1 if s=='R'else -1
 return reduce(out)
checks=letters=0
for a,images in J['geometric_controls']:
 for q,u,v in ((2,1,0),(2,1,1),(3,1,2),(4,1,0),(5,2,3)):
  z=initial(q);words=['R','L']
  for r in range(5):
   for hi,h in enumerate(heads):
    for s,w in enumerate(words):
     assert reduce(z[2*hi+s])==literal(w,q,u,v,h);checks+=1;letters+=len(w)
   z=action(images,a,r,q,u,v,z);words=[''.join(images[c=='L']for c in w)for w in words]
# Inventory coverage is independent of the saved pairs.
def antlegal(w):
 colors={}
 for p,h,s in trace(w)[0]:
  need=s=='L'
  if p in colors and colors[p]!=need:return False
  colors[p]=not need
 return True
right=[];left=[]
for tup in product('LR',repeat=9):
 w=''.join(tup);e=w.count('R')-w.count('L');_,end,last=trace(w)
 if e not in(-1,1)or end!=e or last!=e or not antlegal(w):continue
 (right if e==1 else left).append(w)
assert len(right)==6 and len(left)==6
assert {(r['R'],r['L'])for r in R}=={(x,y)for x in right if x[0]=='R'for y in left}

def det(A):
 A=[[Q(x)for x in row]for row in A];z=Q(1)
 for i in range(len(A)):
  j=next((j for j in range(i,len(A))if A[j][i]),None)
  if j is None:return Q(0)
  if i!=j:A[i],A[j]=A[j],A[i];z=-z
  v=A[i][i];z*=v
  for j in range(i+1,len(A)):
   f=A[j][i]/v
   for k in range(i+1,len(A)):A[j][k]-=f*A[i][k]
 return z
# All supplied polynomials have degree <=3, so these are ALL cyclotomic
# irreducibles of possible degree (Euler phi has no odd value >1).
cyclos=[[Q(-1),Q(1)],[Q(1),Q(1)],[Q(1),Q(1),Q(1)],[Q(1),Q(0),Q(1)],[Q(1),Q(-1),Q(1)]]
def divide(p,q):
 a=p[:]
 for i in range(len(a)-len(q),-1,-1):
  f=a[i+len(q)-1]/q[-1]
  for j,v in enumerate(q):a[i+j]-=f*v
 return not any(a[:len(q)-1])
def quotient(p,q):
 a=p[:];out=[Q(0)]*(len(p)-len(q)+1)
 for i in range(len(out)-1,-1,-1):
  out[i]=a[i+len(q)-1]/q[-1]
  for j,v in enumerate(q):a[i+j]-=out[i]*v
 assert not any(a);return out
certcount=0;unbounded=0
for row in R:
 bad=False
 for char in row['characters']:
  q=char['modulus'];u,v=char['character'];assert q in (1,2,3)
  z=initial(q);seq=[];D=8*q # our independently built group-ring state dimension
  for r in range(3*D+8):
   seq.append(reduce(z[0]));z=action([row['R'],row['L']],0,r,q,u,v,z)
  for cert in char['certificates']:
   assert cert['phase']==cert['state']==0;b=cert['basis'];s=[v[b]for v in seq];c=list(map(Q,cert['recurrence']));L=len(c)-1;assert L<=3 and c[0]==1
   assert all(sum(c[j]*s[t-j]for j in range(L+1))==0 for t in range(L,len(s)))
   hd=det([[s[i+j]for j in range(L)]for i in range(L)])if L else Q(1)
   assert hd and hd==Q(cert['hankel_determinant'])
   p=c[::-1]
   while len(p)>1 and not p[0]:p=p[1:]
   for cp in cyclos:
    if len(p)>=len(cp)and divide(p,cp):p=quotient(p,cp)
   bounded=len(p)==1
   assert bounded==cert['bounded'];bad|=not bounded;certcount+=1
  assert char['bounded']==all(c['bounded']for c in char['certificates'])
 assert bad==row['ruled_out'];unbounded+=bad
# Explicit Jordan control in the group ring, not extrapolated from short terms.
z=initial(3)
for r in range(80):
 assert reduce(z[0])==[1-4*r,-2*r]
 z=action(['RLLRRRRLL','RRLLLLRRL'],0,r,3,0,1,z)
out=dict(status='PASS periodic occupation transfer and all frozen Fourier recurrence certificates',independent_representation='Integral residue group ring, then explicit small-order cyclotomic reduction',literal_checks=checks,literal_letters=letters,inventory_pairs=len(R),recurrences_checked=certcount,unbounded_pairs=unbounded,jordan_formula='F_r=(1-4r)-2r*zeta_3',scope='Necessary finite-support test, charge-preserving heading-preserving unit-scale images; unequal lengths allowed explicitly; genuine root phases only; no complete decision theorem.',hashes={f:hashlib.sha256((F/f).read_bytes()).hexdigest()for f in ['bridge.md','unit9_fourier.records.json','fourier_transfer.py']})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
