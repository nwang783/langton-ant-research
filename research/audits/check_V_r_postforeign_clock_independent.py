from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'V_r_postforeign_contact_clock_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(D/'manifest.json')=='277cedd1f1b7d4c0c2c837aad2e9a619e40c5e6b46c19b7bac8fe76ed72137c7'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'r_contact_clock.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet,pieces=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet','pieces')];raw=lambda seq:''.join(W[a]for a in seq)
# Plain RAW consumer cover is independently checked, without importing full-tail
# exclusions that could occur only AFTER the loss atom.
counts=Counter();gates=[];bridge=(-1-1j,1+1j)
for full in('V','VC','VCC'):
 st=tr(raw(full));assert st['last'][0j]==('R',4);sourcepieces=pieces(full)
 for at in'DCVU':
  ctx=tr(W[at]+M);ins=[q for q,c in ctx['req'].items()if c and q not in K]
  if at=='C':assert not ins;continue
  for h,slot in product(range(4),ins):
   p=-slot*rot(h)
   if(int(p.real)+int(p.imag)+h)%2:counts['sector']+=1;continue
   z=tr(W[at],p,h);ch=(center(p,h),center(z['p'],z['h']));hit=any(meet(*ch,*old)is not None for old in sourcepieces)
   if hit:counts['source_contact']+=1;continue
   assert(at,p,h)in(('D',1,3),('V',3,3),('U',4+1j,3));counts['gate']+=1
   assert z['p']==1j and z['h']==3 and meet(*ch,*bridge)==(F(1),F(1))
   for i,old in enumerate(sourcepieces):assert meet(*old,*bridge)==((F(0),F(0))if i==0 else None)
   local=-p/rot(h);assert local not in tr(W[at])['req'];first=next(t for t,(q,hh,c)in enumerate(ctx['reads'])if q==local)
   assert ctx['reads'][first][2]=='L'and first-len(W[at])==1 and 0j in{z['p']+q*rot(z['h'])for q in K}
   ref=next(r for r in J['all9_actual_source_tail_and_plain_ordinary_r_first_loss_interfaces']if(r['actual_old_source_full'],r['first_loss_ordinary_RAW'])==(full,at));assert ref['same_r_local']==xy(local)and ref['actual_first_r_physical_read']['context_tick0']==first
   gates.append((full,at,xy(p),first))
assert counts=={'sector':48,'source_contact':39,'gate':9}
# beta/(pi/4) is strictly between0 and1. Actual terminal/closing/source angles:
# 4-aH ->5 ->2-beta; both principal turns stay in(-4,4).
for at in'DVU':
 for beta in(F(0),F(1),F(1,2)):
  aH={'D':F(1),'V':beta,'U':F(0)}[at]
  close1=1+aH;close2=-3-beta
  assert -4<=close1<=4 and -4<=close2<=4
  if beta==F(1,2):assert -4<close1<4 and -4<close2<4
  assert close1+close2==aH-beta-2
  for k in range(9):assert(2*k+4+beta-aH)+close1+close2==2*k+2
assert {k for k in range(20)if 2*k+2 in(-8,8)}=={3}
# Real containing source/next-base funnel; candidate ENTRY is already a cut
# of the first-two-return proxy, so repeated old vertex is excluded before b3.
target=4j;tk={target+q*rot(2)for q in K};tz=center(target,2);assert tz==1+9j
assert center(tr(raw('UC'))['p'],tr(raw('UC'))['h'])==tz
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 base=full[0]
 if base=='D':z=tr(W['D'],4j,0);assert center(z['p'],z['h'])==tz
 elif base=='U':assert{4j,5j}<=tk
 else:assert 4j in tk
rows=[];counter=Counter()
for b1,b2 in product('DCVU',repeat=2):
 n=4-(b1+b2).count('C')
 if n not in(3,4):continue
 for A in'FQB':
  ha=(-n)%4;delta=tr(raw(A+b1+b2),h=ha);pa=target-delta['p'];assert delta['h']==2
  local=(4j-pa)/rot(ha);assert local not in tr(W[A]+M)['req']
  suffix=tr(raw(A+b1+b2+'V')+M);counter[n]+=1
  if n==3 and b2=='C':
   z=tr(raw(A+b1),pa,ha);assert(z['p'],z['h'])==(1+4j,3)and z['p']!=5j
  rec=next(r for r in J['all45_actual_FOREIGN_b1_b2_inverse_interfaces']if(r['foreign'],r['first'],r['second'])==(A,b1,b2))
  assert rec['foreign_pose']==xy(pa)+[ha]and rec['complete_local_suffix_feasible']==(suffix['bad']is None)
  rows.append((A,b1,b2,n,xy(pa),suffix['bad']is None))
assert counter=={3:18,4:27}and sum(r[-1]for r in rows)==42
outj=dict(status='PASS conditional post-FIRSTforeign V-r TOTAL loss clock3 and stated old-U THIRD V0,4S application',manifest=sha(D/'manifest.json'),plain_RAW_first_loss_cover=dict(counts),all9_source_tail_gates=gates,inverse_foreign_contexts=45,local_CU_failures=3,r_guards=42,analytic_review=[
'Independently rebuilt96 plain-RAW current-loss alignments, not merely the signed full-consumer cover:48 wrong sector,39 actual past FULL-source chord contacts,9 plain D/V/U gates. C has no external input. Thus no exclusion relies on a consumer C tail occurring after the proposed loss atom.',
'Every gate misses r throughout its own RAW but captures SAME physical identity in EXIT CORE; first physical L is next word tick1/read2 (D11,V19,U29). All source V/VC/VCC own tails retain R4 identity and meet the held edge only at original source entry; consumer meets only at its RAW exit.',
'Given actual preforeign currentness, COMPLETE foreign MISS and simple proxy THROUGH the first loss atom, ordinary/current and repaired-foreign barriers preserve the SAME held edge until loss. The source-to-consumer subarc plus edge is Jordan. Actual non-C complete predecessor forbids the C/foreign wrap; source/terminal are non-C, so exact open lift is(K+2)pi/2+aV-aH. Independent principal closing turns total aH-aV-pi/2, givingK3, not a postforeign age law.',
'For a global first-contact candidate only earlier atoms are used in this Jordan application. The proof concludes currentness at candidate ENTRY, never simplicity or persistence through candidate itself.',
'Creator UC/UCC and next D/DC repeat actual earlier vertex at third entry; next U-family is blocked by signed young foreignSTAR-MISS plus SAMELEFT at candidate entry. Only genuine next V/VC/VCC survives, original r CURRENT before foreign at trueage3/4 by old law5. All45 COMPLETE foreign contexts literally miss this identity.',
'At n4 no postA gate can have totalK3. At n3 firstC is input-free; if secondC the only preC base has exit(1,4,W), not any r gate exit(0,5,W). All42 feasible contexts therefore retain SAME r in forbidden target entryCORE. Three localCU contexts separately fail.',
'Only specified old-U third targetV0,4,S and portable conditional clock are signed. No other target, arbitrary-tail simplicity, altered V cohort seal or postforeign maturity follows.'
]);S.with_suffix('.json').write_text(json.dumps(outj,indent=2)+'\n');print(outj['status']);print(sha(S.with_suffix('.json')))
