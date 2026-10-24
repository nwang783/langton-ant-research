from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_one_foreign_return_U_star_independent.py')};exec(Path(ns['__file__']).read_text().split('ports={}')[0],ns)
W,M,K,L,inv,raw,walk,xy,center=[ns[k]for k in('W','M','K','L','inv','raw','walk','xy','center')]
results=[];endpoint_rows=[]
for base,ry in [('D',2),('V',4)]:
 for name in (base,base+'C'):
  p=ry*1j;h=2;loc=(1-ry)*1j;hits=[(i,ch)for i,(z,hh,ch)in enumerate(inv[name]['reads'])if z==-loc];assert hits[0]==({'D':11,'V':19}[base],'L')
  for f in'FQB':
   fp=p-raw.get(f,walk(W[f]))['p'];ctx=walk(W[f]+M);assert not L&{fp+z for z in ctx['req']}
   guard=(2+4j if f=='F'else 1+3j)if base=='D'else 4j
   g=guard-fp;assert ctx['req'][g]is False;ph=next(i for i,(z,hh,ch)in enumerate(ctx['reads'])if z==g);assert ph=={'D':{'F':44,'Q':58,'B':68},'V':{'F':52,'Q':60,'B':70}}[base][f]
   sols=[];x,y=xy(fp)
   for d in range(x+1):
    v=x-d;r=y-4-d-3*v
    if r>=0 and r%4==0:
     u=r//4;allowed=[b for b,c in [('V',v),('U',u)]if c and(f!='B'or b=='U')];assert not allowed;sols.append((d,v,u))
   results.append({'returned':name,'foreign':f,'pose':[*xy(fp),0],'before_white_guard':xy(guard),'phase':ph,'zero_C_solutions':sols,'necessary_clock':8})
# D clock4 common-bud obstruction: all possible base-consumer endpoints, no bounded connector search.
for target in (3+1j,4):
 for age,h in ((3,1),(4,0)):
  for n in ('D','V','U'):
   for slot in {q for q,b in inv[n]['req'].items()if b}-K:
    p=2+4j-slot*(-1j)**h;ep=p+raw[n]['p']*(-1j)**h
    if age==4:assert ep.imag>=4>complex(target).imag;why='N height'
    elif ep.real+1>complex(target).real:why='C4 x overflow'
    elif target==3+1j:assert ep==2+3j;why='exact x, y>=3'
    elif ep.real==3:assert ep.imag==4;why='exact x, y>=4'
    else:assert ep==2+3j;why='one extra x permits y>=2 only'
    endpoint_rows.append((str(target),age,n,xy(slot),xy(ep),why))
assert len(endpoint_rows)==32
for n in ('V','U'):
 lp=4+4j-raw[n]['p'];assert lp=={'V':3+1j,'U':4}[n];assert 2+4j not in {lp+z for z,b in inv[n]['req'].items()if b}- {lp+z for z in K}
# All first actual atoms preserve the common R8 birth; V/U first r at R4.
first=[]
for n in'DCVU':
 z=walk(W[n]);hits=[(i,ch)for i,(q,h,ch)in enumerate(z['reads'])if q==2];assert hits[-1]==(8,'R')
 ep=4j+z['p'];ch=z['h']
 if n in'DC':assert center(ep,ch)==1+9j
 else:
  rr=[(i,c)for i,(q,h,c)in enumerate(z['reads'])if q==0];assert rr[-1]==(4,'R')
 first.append((n,xy(ep),ch))
for n in ('V','VC','VCC','U','UC','UCC'):
 rr=[(i,c)for i,(q,h,c)in enumerate(raw[n]['reads'])if q==0];assert rr[-1]==(4,'R')
# Bound unchanged author contracts and all explicit dependencies.
bindings={}
for d,pref,data in [('one_foreign_return_D_clock_2026-10-23','ec07dfb3','return_D_clock.json'),('one_foreign_return_V_clock_2026-10-23','128d48ee','return_V_clock.json')]:
 dd=R/d;man=dd/'manifest.json';sh=hashlib.sha256(man.read_bytes()).hexdigest();assert sh.startswith(pref);bindings[d]=sh
 for f,h in json.loads(man.read_text())['files'].items():assert hashlib.sha256((dd/f).read_bytes()).hexdigest()==h
 for f,h in json.loads((dd/data).read_text())['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS returned D/DC and V/VC old-w foreign-clock lower bounds8','bindings':bindings,'twelve_cases':results,'D_common_bud_endpoint_rows':endpoint_rows,'V_first_atom_interfaces':first,'analytic':['Foreign heading N permits only clocks0 mod4. Exact no-C head equations and signed last-V/U adjacency exclude clock0 in all twelve cases. All actual COMPLETE foreign contexts miss the original U star, so no earlier marker absorption is silently included.','D/DC: Q/B require original creator exit bud(1,3) before-white at RAW58/68 while signed maturity keeps it current through clock4. F instead requires actual first-post-U-base common bud(2,4) white at RAW44. That first atom begins at clock0 even for internal C1 of UC/UCC, and all four atoms freshly install it at R8.','Only plain V(3,1,N) or U(4,0,N) can be last before F(4,4,N); neither has the common bud as an input. Thus a full retiring packet must complete earlier. Maturity excludes ages<3. At3 every E base-consumer endpoint has x>=2; the one remaining C and nonnegative E/N cones cannot reach either target. At4 all N endpoints have y>=4. Positive tails are included in the remaining-C budget rather than resetting source clocks.','V/VC: the first actual atom after creating U base starts(0,4,N). D/C ends at the first foreigners eventual terminal corrected center(1,9), contradicting already signed simplicity through first foreign. U freshly installs permanent r=(0,4); V freshly installs r with exact first-retirement age5. In both cases it stays current at foreign clock4, contradicting the first before-white RAW52/60/70.','Every maturity or permanence argument stops at FOREIGN ENTRY. No returned-path simplicity or postforeign lifetime law is used. Plain D/V old-w reads are phases11/19 in the following word after exit-core absorption; DC/VC own those reads in their RAW tails.'],'scope':'Twelve exact one-first-foreign then D/DC or V/VC suffix cases. Necessary age>=8 only, no actual attainment or later age iteration.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
