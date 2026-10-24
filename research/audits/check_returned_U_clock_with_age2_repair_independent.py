from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_one_foreign_return_U_star_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('ports={}')[0],ns)
W,M,K,L,walk,xy,center=[ns[k]for k in('W','M','K','L','walk','xy','center')]
names=['D','DC','V','VC','VCC','U','UC','UCC'];gids=[0,1,4,5,6,7,8,9]
raw={n:walk(''.join(W[c]for c in n))for n in names};ctx={n:walk(''.join(W[c]for c in n)+M)for n in names}
def out(a):
 final={q for q,b in a['req'].items()if b}
 for q,h,ch in a['reads']:final.symmetric_difference_update({q})
 return final-{a['p']+q*(-1j)**a['h']for q in K}
O={n:out(raw[n])for n in names};AR={n:walk(W[n])for n in'DCVU'};AC={n:walk(W[n]+M)for n in'DCVU'};AO={n:out(AR[n])for n in'DCVU'};assert sum(map(len,AO.values()))==19
G=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
for n,i in zip(names,gids):assert{xy(q)for q in O[n]}==set(map(tuple,G[i]['outputs']))
QPATH=ROOT/'audits/dcuv_count5_replay/queries.json';Q=json.loads(QPATH.read_text());assert Q['status'].startswith('PASS');mini={k:v['certified_minimum_C_age']for k,v in Q['slots'].items()}
def age(n,s):return mini[f'{gids[names.index(n)]}:{tuple(xy(s))}']
assert age('V',3j)==age('VC',3j)==2 and age('VCC',3j)==5 and age('VC',1+2j)==3
q0=3j;t0=4j;t1=2+5j;t2=1+6j;rp=-1+5j;h=2
assert AR['U']['req'][t0]is False and t1 not in AR['U']['req']and t2 not in AR['U']['req']
assert next((i,ch)for i,(q,hh,ch)in enumerate(AR['U']['reads'])if q==t0)==(24,'R')
for n in'DCVU':
 assert[(i,ch)for i,(q,hh,ch)in enumerate(AR[n]['reads'])if q==-1j]==[(3,'L')]
 assert next((i,ch)for i,(q,hh,ch)in enumerate(AR[n]['reads'])if q==2+1j)==(7,'R')
 assert all(q.imag>=0 and q.real+q.imag>=0 for q in AO[n])
for n in('U','UC','UCC'):assert q0 not in O[n]and t0 not in O[n]
foreign=[]
for f in'FQB':
 a=walk(W[f]);fp=rp-a['p'];assert a['h']==2
 cc={fp+q:b for q,b in walk(W[f]+M)['req'].items()};assert not L&cc.keys()and q0 not in cc
 foreign.append((f,fp,('U',)if f=='B'else('V','U')))
 for n in('U','UC'):
  assert rp+(-1+2j)*(-1j)**2==q0 and ctx[n]['req'][-1+2j]
  assert[(i,ch)for i,(q,hh,ch)in enumerate(ctx[n]['reads'])if q==-1+2j][:2]==[(13,'L'),(21,'R')]
  assert next((i,ch)for i,(q,hh,ch)in enumerate(ctx[n]['reads'])if q==-1+4j)==(29,'L')
assert[(f,xy(p))for f,p,last in foreign]==[('F',(3,7)),('Q',(3,9)),('B',(2,10))]
roles=[];sur=[]
for h in(2,1,0):
 for n in'DCVU':
  if h==0 and n=='C':continue
  for o in AO[n]:
   p=q0-o*(-1j)**h;ep=p+AR[n]['p']*(-1j)**h
   wrong=(int(p.real+p.imag)+h)%2;hit=L&{p+z*(-1j)**h for z in AC[n]['req']}
   roles.append((h,n,o,p,ep,bool(wrong),bool(hit)))
   if not wrong and not hit:sur.append((h,n,o,p,ep))
assert len(roles)==54 and len(sur)==13 and Counter(h for h,*_ in sur)=={2:2,1:7,0:4}
assert{(n,p)for h,n,o,p,ep in sur if h==2}=={('C',1+5j),('C',2+4j)}
# E3 origins: two old-vertex repetitions, three x-budget failures, two true input roles.
eproof=[]
for h,n,o,p,ep in sur:
 if h!=1:continue
 if n in'DC':assert center(p,h)==center(rp,2);why='earlier center equals first foreign terminal'
 elif ep.real>=3:assert ep.real+1>max(p.real for f,p,last in foreign);why='remaining C4 x budget'
 elif n=='U':assert p==-3+4j and p+3j*(-1j)==t0 and age('U',3j)==5;why='initial-white upper d minimum5'
 else:assert n=='V'and p==-2+5j and p+(1+2j)*(-1j)==t0 and age('V',1+2j)==3;why='clock0 t0 actual r/star guardian'
 eproof.append(why)
assert Counter(eproof)=={'earlier center equals first foreign terminal':2,'remaining C4 x budget':3,'initial-white upper d minimum5':1,'clock0 t0 actual r/star guardian':1}
# t0 possible full origins at the first C0 head: true V r / U star, not residual D.
for n in names:
 assert all(q.imag>=0 for q in O[n]);assert (0 in O[n])==(n[0]in'VU')
 if 0 in O[n]:assert[(i,ch)for i,(q,hh,ch)in enumerate(raw[n]['reads'])if q==0][-1]==(4,'R')
# C3 tail-index interfaces: exact completed full packet, not generic V slot minimum.
tails=[]
for p in(1+5j,2+4j):
 for b in'DVU':
  bp=p-AR[b]['p']*(-1j)**2
  if p==1+5j:
   s={'D':1j,'V':3j,'U':-1+4j}[b];assert bp+s*(-1j)**2==t1
   variants={'D':['DC'],'V':['VC','VCC'],'U':['UC','UCC']}[b]
   for n in variants:
    minimum=age(n,s)
    if n=='VC':assert minimum==2 and bp==2+8j;why='SEPARATE exact age2 repair required'
    else:assert minimum>2;why='actual full-packet input minimum exceeds2'
    tails.append((xy(p),n,xy(bp),minimum,why))
  elif b=='D':tails.append((xy(p),'DCC',xy(bp),None,'not a retained packet; next C4 forced by x budget'))
  else:
   n=b+'CC';s=1+2j if b=='V'else 3j;assert bp+s*(-1j)**2==t1 and age(n,s)>2
   tails.append((xy(p),n,xy(bp),age(n,s),'actual full-packet input minimum exceeds2'))
 for b in'VU':
  bp=p+1-AR[b]['p']*(-1j)**3;assert bp.imag-bp.real<5
  tails.append((xy(p),b+'CC-second',xy(bp),None,'C1 W head halfplane'))
assert (2+4j)+AR['C']['p']*(-1j)**2==2+3j
assert all((AR[b]['p']*(-1j)).real>=1 for b in'DVU')
# N4 actual endpoints and unbounded zero-C counts; none has a legal last V/U.
obligations=[]
def counts(delta):
 x,y=xy(delta);out=[]
 for d in range(max(x+1,0)):
  v=x-d;rem=y-d-3*v
  if rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
for h,n,o,p,ep in sur:
 if h!=0:continue
 for f,fp,last in foreign:
  sols=counts(fp-ep);assert all(not any(c and name in last for name,c in zip('DVU',t))for t in sols)
  obligations.append((n,xy(p),f,sols))
assert len(obligations)==12
# Genuine repair: t1 initially WHITE, VC upper min2 implies full-source birth clock0.
assert next((i,ch)for i,(q,h,ch)in enumerate(AR['C']['reads'])if q==1+2j)==(13,'R')
for n in('U','UC','UCC'):assert (t1 in O[n])==(n!='U')
# Original UC/UCC C1 origin forces t2 initially white; selected VC minimum3 kills it.
assert age('VC',1+2j)==3
vcctx=ctx['VC'];target=2+8j
origins=[]
for n in names:
 for slot in O[n]:
  bp=t1-slot
  if int(bp.real+bp.imag)%2:continue
  sols=counts(bp-4j)
  if not sols:continue
  assert n[0]in'VU'and (bp,slot)in((4j,2+1j),(1+5j,1))
  assert sols==([(0,0,0)]if bp==4j else[(1,0,0)])
  local=(bp-target)/((-1j)**2);assert vcctx['req'][local]is False
  first=next((i,ch)for i,(q,h,ch)in enumerate(vcctx['reads'])if q==local)
  assert first==((24,'R')if bp==4j else(14,'R'))
  assert bp not in{target+k*(-1j)**2 for k in K}and 0 in O[n]
  origins.append((n,xy(bp),xy(slot),first))
assert len(origins)==12 and Counter(p for n,p,s,r in origins)=={(0,4):6,(1,5):6}
D=ROOT/'one_foreign_return_U_clock_2026-10-23';bindings={}
for name,expected in [('manifest.json','510187883f9d8e67183f167030b57a2d778dc180aadb87eeaa5ef95b267e5c91'),('rejected_candidate_correction_manifest.json','7fd723780206f3a2fcc2327b6537195d6e390cc1dd2685025afcf91459c6ab15'),('upper_age2_repair_manifest.json','163676a04fc197385d4f95beb34b227972410e5c7fa22c2f46cb26f41938e3f4')]:
 sh=hashlib.sha256((D/name).read_bytes()).hexdigest();assert sh==expected;bindings[name]=sh
out={'status':'PASS QUALIFIED COMPOSITION ONLY; original51018788 remains NOT PASSED','bindings':bindings,'actual_upper_V_VC_minimum':2,'actual_selected_V_VC_minimum':3,'VCC_both_inputs_minimum':5,'full_output_masks_freshly_reconstructed':8,'atomic_q0_roles':54,'survivors_by_heading':dict(Counter(h for h,*_ in sur)),'E_origin_split':dict(Counter(eproof)),'actual_C3_tail_interfaces':tails,'unbounded_N4_obligations':obligations,'separate_age2_repair_origins':origins,'analytic':['The original candidate contains a false upper V/VC minimum3 and is explicitly not signed. The separate correction and repair replace precisely that rejection. The lower V/VC selected minimum is3; VCC both slots are5; U uppers are5. No slot law is transplanted.','q0 is actually deleted by the first postcreator atom, which may be internal C1. All first foreign contexts miss q0. Its last current birth is therefore before foreign, in a genuine old-eight packet. Atomic output reconstruction exhausts those possible origins through C4, including both C3 tail indices and real full-source entry clocks. No retirement law is applied after foreign.','Initial-white t0 and t1 are established by creator U R24 and first-postatom R7, with the actual preceding RAW misses. The E3 V selected t0 case can only be supplied at C0 by a true V r or U star at first head(0,4), both current when the later consumer would need them.','For the exact VC(2,8,S) upper-age2 branch, original UC/UCC output origin forces selected t2 initially white at internal C1 R13, so its age<=2 contradicts the genuine selected minimum3. Every other clock0 full-output origin solves the exact unbounded N-head equations and is one of12 V/U-family sources at(0,4) or(1,5). Their fresh r/star is required before-WHITE by the target VC and cannot retire by C2. Full C tails and original creator origins are kept separate.','The remaining E and N endpoint constraints account for mandatory C4, all nonnegative zero-C run lengths, true last V/U adjacency and old-vertex versus first-foreign terminal simplicity. The correct clock0 exclusion is the already signed72-row theorem with both mandatory errata.'],'conclusion':'In the stated genuine U-family / first foreign context-miss / immediately returned U or UC(-1,5,S) mechanism, foreign clock>=8. Necessary lower bound only; no attained clock8, returned simplicity, postforeign permanence, later-age induction or universal capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
