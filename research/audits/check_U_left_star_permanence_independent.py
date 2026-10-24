from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();C=ROOT/'core_periodicity_new';B=C/'U_left_star_permanence_frozen_20261023_1918';m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['path']).read_bytes()).hexdigest()==f['sha256']
for p,h in [('causal_cycle_renewal_20261023_1841/manifest.json','27db0bc457534074587a988c16bbf57c994464656df7c9aa06427ab23203d7d4'),('U_entry_simplicity_frozen_20261023_1616/manifest.json','127a00884b4a06af35a807ab76f6f6499b9427d56350a931c03cc0e8de65524d')]:assert hashlib.sha256((C/p).read_bytes()).hexdigest()==h
K={q for q,b in walk(mark)[2].items()if b};L={0j,1j,1+0j,1+1j};rB=3-1j;IDS=(0,1,4,5,6,7,8,9)
def chord(p,h,s):return(2*p+rotation(-1-1j,h),2*p+rotation((-1-1j)+(2+2j if s in(0,1)else 2+6j if s in(4,5,6)else 8j),h))
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def meet(A,B):
 a,b=A;c,d=B;u=b-a;v=d-c;z=det(u,v)
 if z:
  t=Fraction(det(c-a,v),z);s=Fraction(det(c-a,u),z)
  return('point',t,s)if 0<=t<=1 and 0<=s<=1 else None
 if det(c-a,u):return None
 f=(lambda q:int(q.real))if u.real else(lambda q:int(q.imag));ts=sorted([Fraction(f(c-a),f(u)),Fraction(f(d-a),f(u))]);lo=max(0,ts[0]);hi=min(1,ts[1]);return('interval',lo,hi)if lo<=hi else None
A=chord(0j,0,7);BB=chord(rB,0,7);rows=[];kept=[];mass=[];geo={}
for s in IDS:
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,b in req.items()if b};I=black-K;O=(black^flip)-{e+rotation(q,h)for q in K};white={q for q,b in req.items()if not b};geo[s]=(I,O)
 c={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}[s];v=s in(4,5,6);u=s in(7,8,9)
 assert len(O)-len(I)==3*c+4*v+4*u;mass.append((s,len(I),len(O),c))
 if u:
  assert L<=O
  # Literal source tails preserve the fresh star after its U base.
  p=0j;hd=0
  for tick,b in enumerate(raws[s]):
   if tick>=len(raws[7]):assert p not in L
   hd=(hd+(1 if b=='R'else-1))%4;p+=(1j,1,-1j,-1)[hd]
 for q in L:
  for i in I:
   for hd in range(4):
    p=q-rotation(i,hd);ci={p+rotation(z,hd)for z in I};ck={p+rotation(z,hd)for z in K};cw={p+rotation(z,hd)for z in white}
    if(sum(xy(p))+hd)%2:reason='sector'
    elif ck&L:reason='core'
    elif cw&L:reason='white'
    else:reason='candidate'
    row=dict(packet=s,pose=(*xy(p),hd),target=xy(q),input=xy(i),reason=reason)
    if reason=='candidate':
     touched=ci&L;assert len(touched)==1
     if touched&{0j,1j}:
      contact=meet(A,chord(p,hd,s));assert contact is not None
      if contact[0]=='point':assert contact[1]in(0,Fraction(1,2))
      else:assert contact[1]<contact[2] and contact[1]<=Fraction(1,2)<=contact[2]
      row.update(case='source_contact',contact=[str(x)for x in contact])
     elif touched=={1+1j}:
      contact=meet(BB,chord(p,hd,s));assert contact and contact[0]=='point'and 0<contact[1]<1
      row.update(case='breaker_contact',contact=[str(x)for x in contact])
     else:
      assert touched=={1+0j}and rB in cw
      assert meet(A,chord(p,hd,s))is None and meet(BB,chord(p,hd,s))is None
      local=rotation(rB-p,-hd);assert local in{2+0j,2+2j,1+3j};row.update(case='earlier_breaker_star_retirement',before_white=xy(local))
     kept.append(row)
    rows.append(row)
assert Counter(r['reason']for r in rows)==dict(sector=184,core=20,white=140,candidate=24)
assert Counter(r['case']for r in kept)==dict(source_contact=12,breaker_contact=6,earlier_breaker_star_retirement=6)
assert len({(r['packet'],*r['pose'])for r in kept})==24
for s in(7,8,9):
 I,O=geo[s];assert not{rB+q for q in I}&L and rB in{rB+q for q in O}
# All four even-primal edges are incident to the same residual-star vertex.
edges=[]
for q in L:
 x,y=xy(q);d=1+1j if(x+y)%2==0 else 1-1j;edges.append({2*q-d,2*q+d})
assert set.intersection(*edges)=={1+1j}
out=dict(status='PASS independent U-born left-star permanence by earliest retirement descent',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(Counter(r['reason']for r in rows)),candidate_cases=dict(Counter(r['case']for r in kept)),rows=rows,mass_rows=mass,analytic_induction='Choose earliest retiring packet of any genuine U-born star ID. Its creator has all4 star IDs current; source-contact candidates fail. West retirement forces a strictly earlier genuine right first breaker B. B-contact candidates fail by B-entry simplicity. Remaining candidates demand B-local0,0 before-white, requiring its star ID to retire strictly earlier, contradiction. Source tails are separately preserved; old entry identities are not included.',consequence='All4u fresh stars are disjoint and current until factor end. Unlocked residual count is r0+3c+4v, not a finite resource bound.',scope='Actual finite/infinite context-complete retained-eight factor only. No claim after leaving language, no original-root fuel, merger, global U bound or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
