from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new';B=D/'U_recycled_q_return_frozen_20261023_1939';m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,sha in m['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==sha
K={q for q,b in walk(mark)[2].items()if b};G={}
for s in(7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,b in req.items()if b};G[s]=(black-K,(black^flip)-{e+rotation(q,h)for q in K},set(req)|K)
q=-1+2j;AA=-1+3j;BB=-3+5j;source=(-1-1j,-1+7j);star={0j,1j,1+0j,1+1j};assert{2*q-1+1j,2*q+1-1j}=={AA,BB}
def cross(a,b):return int(a.real*b.imag-a.imag*b.real)
def point(z):return(int(z.real),int(z.imag))
def meet(ab,cd):
 a,b=ab;c,d=cd;u=b-a;v=d-c;den=cross(u,v)
 if den:
  t=Fraction(cross(c-a,v),den);s=Fraction(cross(c-a,u),den)
  if 0<=t<=1 and 0<=s<=1:return (t,s,(Fraction(int(a.real))+t*int(u.real),Fraction(int(a.imag))+t*int(u.imag)))
  return None
 if cross(c-a,u):return None
 # All present collinear cases are single endpoint or disjoint; handle generally.
 ix=0 if u.real else 1;get=lambda z:int(z.real if ix==0 else z.imag);ts=sorted([Fraction(get(c-a),get(u)),Fraction(get(d-a),get(u))]);lo=max(0,ts[0]);hi=min(1,ts[1])
 return None if lo>hi else('collinear',lo,hi)
rows=[]
for s in(7,8,9):
 for h in range(4):
  for slot,i in enumerate(sorted(G[s][0],key=xy)):
   p=q-rotation(i,h);start=2*p+rotation(-1-1j,h);end=start+rotation(8j,h)
   if(sum(xy(p))+h)%2:reason='wrong_sector'
   elif{p+rotation(z,h)for z in G[s][2]}&star:reason='permanent_source_L_star_context'
   elif meet((start,end),source):
    contact=meet((start,end),source);assert contact==(Fraction(1,4),Fraction(3,4),(Fraction(-1),Fraction(5)));reason='consumer_base_hits_source_U_strict_interior'
   else:
    assert s in(7,8)and h==2 and(p,i)in[(-2+4j,-1+2j),(-2+6j,-1+4j)]
    fr=Fraction(1,2)if i==-1+2j else Fraction(1);assert start+float(fr)*(end-start)==BB
    assert meet((start,BB),(BB,AA))==(Fraction(1),Fraction(0),(Fraction(-3),Fraction(5)))
    reason='Jordan_forces_Cgap2_below_true_input_minimum'
   rows.append(dict(consumer=s,head=(*xy(p),h),input_slot=slot,reason=reason))
counts=Counter(r['reason']for r in rows);assert counts==dict(wrong_sector=30,permanent_source_L_star_context=23,consumer_base_hits_source_U_strict_interior=3,Jordan_forces_Cgap2_below_true_input_minimum=4)
ref=json.loads((B/'02_U_recycled_q_return.json').read_text());assert{(r['consumer'],r['head'],r['input_slot'],r['reason'])for r in rows}=={(r['consumer'],tuple(r['head']),r['input_slot'],r['reason'])for r in ref['all_60_U_consumer_alignments']}
C=raws[1][len(raws[0]):];prefix=[]
for s in(7,8,9):
 assert q in G[s][1]
 e,h,_,_=walk(raws[7]);P=2*e+rotation(-1-1j,h);assert P==-1+7j
 assert meet((AA,P),(BB,AA))==(Fraction(0),Fraction(1),(Fraction(-1),Fraction(3)))
 tails=[]
 for _ in range(s-7):
  old=P;ep,dh,_,_=walk(C);e+=rotation(ep,h);h=(h+dh)%4;P=2*e+rotation(-1-1j,h);assert meet((old,P),(BB,AA))is None;tails.append([xy(old),xy(P)])
 prefix.append(dict(source=s,tails=tails))
# Principal directions in eighth-turn units: S6 -> SE7 -> N2 gives +1,+3.
principal=lambda b,a:(b-a+4)%8-4
joins=[principal(7,6),principal(2,7)];assert joins==[1,3]
assert [n for n in range(20)if 2*n+sum(joins)in(-8,8)]==[2]
out=dict(status='PASS protected recycled-q single-edge Jordan exclusion',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),all_rows=rows,partial_source_tails=prefix,join_eighth_turns=joins,forced_source_inclusive_age=2,scope='Same actual complete-eight factor, genuine earlier U-family output(-1,2) cannot feed any later U-family input. No permanence against D/V, entry/replacement exclusion, record or component claim.',analytic='U-entry suffix simplicity plus current-edge barrier makes A-to-B arc disjoint from bridge except endpoints. Pre-full-installation partial U and C tails are separately literal. Same full-source clock includes all source Cs, full target entry excludes target tails. Closed turn n*pi/2+pi forces n2, contradicting produced lower3/upper5.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],dict(counts))
