"""Colored-token extension of the inherited twenty-cell feedback family.
The source's all-parameter geometric guards are a stated dependency.
This checker reconstructs the fixed protected colored field, exact recovery,
and all-future single-root ancestry without importing ant simulation code.
"""
from pathlib import Path
import json
from collections import Counter
HERE=Path(__file__).resolve().parent
DIR=((0,1),(1,0),(0,-1),(-1,0))
G=((0,-1),(1,1),(2,2),(1,3)) # A,B,C,D in their first-read order

def rot(q,n):
 x,y=q
 for _ in range(n%4):x,y=y,-x
 return x,y

def step(B,p,h,active):
 if p in B:
  active=B.pop(p);c='L';h=(h-1)%4
 else:
  B[p]=active;c='R';h=(h+1)%4
 d=DIR[h]
 return (p[0]+d[0],p[1]+d[1]),h,active,c

def motion(word,p,h):
 pp=[];hh=[]
 for c in word:
  pp.append(p);hh.append(h);h=(h+(1 if c=='R' else -1))%4;d=DIR[h];p=(p[0]+d[0],p[1]+d[1])
 return pp,hh,p,h

def mul(v,d):
 for a,b in zip(v,d):
  if b:
   if a%b:return None
   k=a//b;return k if (k*d[0],k*d[1])==v else None
 return 0 if v==(0,0) else None

def period_certificate(B,p,h,word):
 q,hs,end,eh=motion(word,p,h);d=(end[0]-p[0],end[1]-p[1]);P=len(word)
 assert eh==h and d!=(0,0)
 checks=0
 for i in range(P):
  earlier=[];breaks={0}
  for j in range(P):
   # q_j+ell*d=q_i; prior event at epoch k+ell.
   ell=mul((q[i][0]-q[j][0],q[i][1]-q[j][1]),d)
   if ell is not None and j+ell*P<i:
    earlier.append(ell);breaks.add(max(0,-ell))
  for x in B:
   k=mul((x[0]-q[i][0],x[1]-q[i][1]),d)
   if k is not None and k>=0:breaks|={k,k+1}
  for k in sorted(breaks):
   x=(q[i][0]+k*d[0],q[i][1]+k*d[1]);bit=(x in B) ^ (sum(k+ell>=0 for ell in earlier)%2==1)
   assert bit==(word[i]=='L'),(i,k,x)
   checks+=1
 return q,d,checks

def on_future(q,d,x):
 return any((k:=mul((x[0]-z[0],x[1]-z[1]),d)) is not None and k>=0 for z in q)

def omega(q):return q[0]>=-16 and -14<=q[0]+q[1]<=12

# Four-cell reference, symbolic source root X and four edge roots A0..D0.
B={q:f'{c}0' for c,q in zip('ABCD',G)};p=(0,0);h=1;active='X';trace=[];owners=[];positions=[]
for t in range(806):
 owners.append(active);positions.append(p);p,h,active,c=step(B,p,h,active);trace.append(c)
 if t+1==182:B182=dict(B);p182=p;h182=h;active182=active
U=''.join(trace[182:286]);q,d,checks=period_certificate(B182,p182,h182,U)
assert d==(2,2) and active182=='A0'
assert owners[171:]==['A0']*(806-171)
assert all(not on_future(q,d,x) for x,label in B182.items() if label!='A0')
assert positions[60]==(0,2) and trace[60]=='R' and owners[60]=='D0'
assert positions[53]==(2,5) and trace[53]=='R' and owners[53]=='A0'
assert (2,5) not in positions[54:] and not on_future(q,d,(2,5))
reference_X_last=max(t for t,label in enumerate(owners) if label=='X')
assert reference_X_last==13
reference_last_non_A=max(t for t,label in enumerate(owners) if label!='A0')
assert reference_last_non_A==170

# Eq.(7) of inherited scalable-feedback-circuit.md, extended to token root colors.
C={x:label for x,label in B.items() if omega(x)}
C0=dict(C);stage4reads=[]
for v in range(-26,1):
 for i in range(104 if v<0 else 14):
  x=(q[i][0]-8+2*v,q[i][1]+2*v)
  if not omega(x):continue
  stage4reads.append(x)
  assert x not in C0 # disjoint unchanged stage-0 black field
  if U[i]=='R':
   assert x not in C;C[x]='A4'
  else:
   assert x in C and C[x]=='A4';del C[x]
assert len(C)==90 and C[(0,2)]=='D0'
# The reference prefix's read set and stage4's protected reads do not overlap.
assert not set(positions)&set(stage4reads)

# Literal protected recovery; all reads stay in Omega.
BC=dict(C);p=(0,2);h=1;active='A4';recovery=[];recovery_owners=[];poses=[]
for t in range(774+104*4):
 assert omega(p);poses.append((p,h));recovery_owners.append(active)
 p,h,active,c=step(BC,p,h,active);recovery.append(c)
 if t+1==774:endC=dict(BC);endp=p;endh=h;endactive=active
word=''.join(recovery[774:878]);fq,fd,fchecks=period_certificate(endC,endp,endh,word)
assert fd==(2,-2) and all(omega(x) for x in fq)
assert all(not on_future(fq,fd,x) for x,label in endC.items() if label!='A0')
assert endactive=='A0' and recovery_owners[770:]==['A0']*(len(recovery_owners)-770)
assert min(t for t,l in enumerate(recovery_owners) if l=='A0')==234
assert poses[233][0]==(2,5) and recovery[233]=='L'
assert all(p[0]!=(2,5) for p in poses[:233])
assert max(t for t,l in enumerate(recovery_owners) if l!='A0')==769

# Independent finite family controls, not the all-parameter guard proof.
def seed(n):
 poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
 out={}
 for j,(p,h) in enumerate(poses):
  for c,g in zip('ABCD',G):
   x=rot(g,h-1);x=(p[0]+x[0],p[1]+x[1]);assert x not in out;out[x]=f'{c}{j}'
 return out
rows=[]
for n in (20,22,40,80,160):
 B=seed(n);p=(0,0);h=1;active='X';e=624*n-1516;lastA=-1
 for t in range(e):
  if active=='A0':lastA=t
  p,h,active,c=step(B,p,h,active)
 assert (p,h,active)==((0,2),1,'A4')
 assert {x:l for x,l in B.items() if omega(x)}==C
 assert lastA==52*n-160
 rows.append(dict(n=n,return_time=e,last_A0_before_return=lastA,first_A0_after_return=e+234))
output=dict(status='Exact colored-field certificate; all-parameter geometric separation is inherited.',
 source_dependency='sources/kehao95-core/memory_feedback/proof/scalable-feedback-circuit.md, Sections3-4',
 reference_last_non_A0=170,reference_last_entry_root_X=reference_X_last,reference_period_checks=checks,protected_color_counts=dict(Counter(C.values())),
 protected_field=[dict(cell=x,root=l) for x,l in sorted(C.items())],
 first_A0_after_return_offset=234,last_non_A0_after_return_offset=769,
 reactivating_lifetime=dict(cell=[2,5],birth=53,consumption='624*n-1283',age='624*n-1336'),
 all_future_root='A0',recovery_period_checks=fchecks,
 inactive_gap_between_A0_updates='572*n-1122',literal_controls=rows)
(HERE/'root_reactivation_certificate.json').write_text(json.dumps(output,indent=2))
print(json.dumps({k:v for k,v in output.items() if k!='protected_field'},indent=2))
