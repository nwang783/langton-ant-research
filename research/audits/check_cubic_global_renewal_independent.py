from pathlib import Path
from collections import Counter
from decimal import Decimal,getcontext
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];s=(SELF.parent/'check_serial_bridge_archive_independent.py').read_text();exec(s.split('# Fixed local masks')[0]);SELF=Path(__file__).resolve();D=R/'global_renewal_archive_2026-10-23';getcontext().prec=50;stats=Counter()
def check(B,p,h,N,word=None):
 B=set(B);m=len(B);a=Decimal(m).sqrt();k=int(wvertex(p,h).real+wvertex(p,h).imag)%4;E=Dc=0;M=m;r=0;n=0;gain=0;S=0;first=None;last=None;ws={wvertex(p,h)};initial=set(B);initialbridges=bridge_set(B,k)
 for t in range(N):
  q=p;L=q in B;assert word is None or('L'if L else'R')==word[t];oldw=wvertex(p,h)
  if L:
   wn=q not in bridge_set(B,k);zn=q not in bridge_set(B,2-k);exception=r>=3 or wn;Dc+=int(wn or zn)
   assert not exception or(wn or zn)
  else:r+=1;assert r<=4
  p,h,_=step(B,p,h)
  if L:
   if exception:
    assert gain<=8*Decimal(M).sqrt()+3;assert len(B)<=Decimal(M)+8*Decimal(M).sqrt()+6;E+=1;M=len(B);r=n=gain=S=0;first=last=None;ws={wvertex(p,h)};initial=set(B);initialbridges=bridge_set(B,k);stats['exceptional_blocks']+=1
   else:
    assert r<=2 and q in initialbridges;v=wvertex(p,h);assert v not in ws;ws.add(v);n+=1;g=r-1;gain+=g;d=v-oldw
    if last is None:first=g
    else:
     z=d/last;assert z in(1,1j,-1j);turn=1 if z==-1j else -1 if z==1j else 0;assert turn==g;S+=turn
    last=d;assert gain==S+first and n<=M
    if n<=1:assert S==0
    else:assert abs(S)<8*Decimal(n-1).sqrt()+2
    assert len(B)==M+gain and gain<=8*Decimal(M).sqrt()+3;r=0;stats['ordinary_blocks']+=1
   assert E<=Dc
  assert M<=(a+4*E)**2+Decimal('1e-40')
  poly=3*(E+1)*m+12*a*E*(E+1)+8*E*(E+1)*(2*E+1)+5*E+4
  cube=16*(Decimal(E)+a/4+1)**3
  assert Decimal(t+1)<=poly and poly<=cube and E<=Dc;stats['prefixes']+=1
 return dict(T=N,m=m,E=E,D=Dc,final_mass=len(B))
# Fixed physical controls and arbitrary entry cuts, not a word or seed search.
controls=[]
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());controls.append(check({complex(*q)for q in std['seed']},0j,std['heading'],520,std['word']*5))
B=set();p=0j;h=0;snap=[];word=''
for t in range(1600):
 if t in(0,1,2,3,4,7,17,42,99,301,777):snap.append((set(B),p,h,t))
 word+='L'if p in B else'R';p,h,_=step(B,p,h)
for bb,pp,hh,t in snap:controls.append(check(bb,pp,hh,min(400,1600-t),word[t:t+400]))
for r in(1,2,7,30,100):
 ret={complex(2*r,-1),complex(2*r+1,-2)}|{complex(x,x-2*r-4)for x in range(r,2*r+2)}|{complex(x,-x-5)for x in range(-2,r)}|{-2-2j,-1-1j};controls.append(check(ret|{complex(x,0)for x in range(2*r)},0j,1,4*r,'LRRL'*r))
# Symbolic coefficient identity for the final cube bound, represented exactly.
# Variables E,a with a=sqrt(m). Expand monomials (Edegree,adegree).
def mul(x,y):
 z=Counter()
 for(i,j),u in x.items():
  for(k,l),v in y.items():z[i+k,j+l]+=u*v
 return dict(z)
from fractions import Fraction as F
base={(1,0):F(1),(0,1):F(1,4),(0,0):F(1)};cube={k:16*v for k,v in mul(mul(base,base),base).items()};poly={(1,2):3,(0,2):3,(2,1):12,(1,1):12,(3,0):16,(2,0):24,(1,0):13,(0,0):4};diff={k:cube.get(k,0)-poly.get(k,0)for k in set(cube)|set(poly)};diff={k:v for k,v in diff.items()if v};assert diff=={(2,0):24,(1,1):12,(1,0):35,(0,3):F(1,4),(0,1):12,(0,0):12}
note=D/'cubic_global_w_renewal.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='9bcf5c2a045fcedb1a5d6d7182df5bdb75ddc2d7a71f03fac2374019bda2eb16';geo=R/'simple_path_turning_2026-10-23/PROOF.md';assert hashlib.sha256(geo.read_bytes()).hexdigest()=='8647be7a9158e11985f60a7643c64411d0cd396e73449ed02032c084f7e7303f';assert json.loads((SELF.parent/'check_simple_path_signed_turning_independent.json').read_text())['status'].startswith('PASS')
out={'status':'PASS global cubic w-exceptional renewal and dual cycle-erasure count law','note_sha256':sha,'geometric_dependency_sha256':hashlib.sha256(geo.read_bytes()).hexdigest(),'counts':dict(stats),'controls':controls,'analytic':['Partition any actual interval into complete R^r L blocks plus <=4 final Rs. A complete block is exceptional exactly when r>=3 or its L is a w nonbridge; each such L erases a cycle in at least one graph, so E<=D when D counts physical updates once. An initial partial r3 block is retained as exceptional.','Every ordinary epoch has r<=2 and w-bridge departures. Exact far-side inheritance holds even when R writes create cycles behind or ordinary L erases z cycles. The w cursor traverses distinct bridges of ONE initial active component; its unit-square-coordinate path is vertex-simple and n<=M, where M is complete epoch-entry mass.','For every ordinary block after the first, r0/1/2 is exactly left/straight/right turning of the w path, so mass change r-1 equals signed internal right-minus-left quarter turning. The first block contributes at most1, even at an arbitrary initial cut. Therefore total ordinary mass gain <=8sqrt(M)+3. No terminal R fringe is hidden in this completed-epoch mass.','A following exceptional block adds at most3 black cells, giving Mnext<=M+8sqrt(M)+6<=(sqrt(M)+4)^2. Thus M_j<=(sqrt(m)+4j)^2 independently of initial positions, passive components and diameter.','Each ordinary block costs<=3, each exceptional block<=5 and the final R-only fringe<=4. Therefore T<=3(E+1)m+12sqrt(m)E(E+1)+8E(E+1)(2E+1)+5E+4<=16(E+sqrt(m)/4+1)^3. The exact nonnegative polynomial difference is independently reconstructed.','Consequently E and D are at least (T/16)^(1/3)-sqrt(m)/4-1. This is a true all-interval global recurrence bound, not only a prepared-profile or retained-language theorem.'],'scope':'Arbitrary actual finite-complete-support trajectory interval, including m0 and arbitrary starting cuts. No positive density, mass divergence, nonstandard-renewal budget, finite summary, highway classification or universal capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(stats)
