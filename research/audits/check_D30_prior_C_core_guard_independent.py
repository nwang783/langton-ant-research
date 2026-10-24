from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D30_prior_C_core_guard_2026-10-24';p=SELF.with_name('check_D15_UCC_V_core_guard_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('xp=')[0],ns)
W,M,walk,xy,K,trace,at,raw=[ns[k]for k in('W','M','walk','xy','K','trace','at','raw')]
def center(p,h):return 2*p+(-1-1j)*(-1j)**h
def cross(a,b):return int(a.real*b.imag-a.imag*b.real)
def params(a,b,c,d):
 u=b-a;v=d-c;den=cross(u,v);assert den;return Fraction(cross(c-a,v),den),Fraction(cross(c-a,u),den)
prior=-1+0j;hole=-1+1j;goal=3-4j;oldC=(center(prior,1),center(0j,0));oldD=(center(0j,0),center(1+1j,0));assert oldC==(-3+1j,-1-1j)
c=trace(W['C']);assert at(c[2],prior,1)==0 and(c[3]+1)%4==0 and c[4][-1]==[(1,'L')]and at(-1,prior,1)==hole and hole not in K
fr=trace(W['F']);combined=trace(W['F']+W['V']+M);loc=(hole-goal)*1j;assert loc not in fr[0]and loc not in K and combined[0][loc]and combined[4][loc][0]==(69,'L')
held={1-1j,2+0j,3+1j}
def counts(ep):
 dx=int((goal-ep).real);down=int((ep-goal).imag);out=[]
 for v in range(max(0,down+1)):
  d=down-v;rem=dx-d-3*v
  if rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
bud=[]
for q in sorted(held,key=xy):
 for a in'DVU':
  for slot in sorted(raw[a]['I'],key=xy):
   p=q-at(slot,0j,1);end=at(raw[a]['end'],p,1);sol=counts(end);assert end!=goal and all(v==u==0 for d,v,u in sol);bud.append((xy(q),a,xy(slot),xy(p),xy(end),sol))
assert len(bud)==24
# Source-D input is physically deleted by the actual immediately following atom.
for a in'DCVU':assert raw[a]['reads'][-1]==[(1,'L')]and at(-1,1+1j,0)==1j
full=[]
for n in ['D','DC','V','VC','VCC','U','UC','UCC']:
 r=trace(''.join(W[a]for a in n));cx=trace(''.join(W[a]for a in n)+M)[0];ek={at(q,r[2],r[3])for q in K};O=({q for q,b in cx.items()if b}^r[1])-ek
 assert all(q.imag>=0 for q in O)and all(q.real>=0 for q in O if q.imag==0)
 if n in['D','DC']:assert 1j not in O
 full.append((n,sorted(map(xy,O))))
mins=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text())['slots'];locks=[]
for a,p,slot,m,gi in [('D',2j,1j,3,0),('V',4j,3j,2,4),('U',-1+5j,-1+4j,5,7)]:
 assert at(slot,p,2)==1j and at(raw[a]['end'],p,2)==-1+1j
 for ii in [gi,gi+1]:assert mins[f'{ii}:{xy(slot)}']['certified_minimum_C_age']==m
 locks.append((a,xy(p),xy(slot),m,2-m))
N=[];West=[]
for a in'DCVU':
 for slot in sorted(raw[a]['fresh'],key=xy):
  p=hole-slot;assert p.real<0 or p.imag<0;N.append((a,xy(slot),xy(p)))
  p=hole-at(slot,0j,3)
  if p.imag>=2:West.append((a,xy(slot),xy(p)))
assert set(West)=={('U',(-1,2),(1,2)),('U',(-1,3),(2,2))};assert not walk(W['C']+W['U']+M)['feasible']
roles=[];counts_by=Counter()
for h in[2,1]:
 for a in'DCVU':
  for slot in sorted(raw[a]['fresh'],key=xy):
   p=hole-at(slot,0j,h);end=at(raw[a]['end'],p,h);he=(h+raw[a]['turn'])%4;hits=held&{at(q,p,h)for q in raw[a]['ctx']};why=None
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif hits:why='held'
   elif h==1 and a=='C':why='too_late_C4'
   elif center(end,he)==oldC[0]:why='old_C_entry_repeat'
   elif center(end,he)==oldD[1]:why='old_D_exit_repeat'
   elif h==2 and (a,p)in[('D',2j),('V',4j),('U',-1+5j)]:why='source_D_input_deadline'
   elif h==2 and p==hole and a=='V':assert params(*oldC,center(p,h),center(end,he))==(Fraction(1,2),Fraction(1,2));why='strict_old_C_cross'
   elif h==2 and p==hole and a=='U':assert params(*oldD,center(p,h),center(end,he))==(Fraction(0),Fraction(1,2));why='old_D_start_in_new_chord'
   else:assert end==-1+2j and he==1 and slot in raw[a]['core'];why='triple_bud_endpoint'
   counts_by[why]+=1;roles.append({'h':h,'atom':a,'slot':xy(slot),'entry':xy(p),'exit':xy(end),'core':slot in raw[a]['core'],'held':sorted(map(xy,hits)),'reason':why})
assert len(roles)==72 and counts_by['old_C_entry_repeat']==4 and counts_by['old_D_exit_repeat']==3 and counts_by['source_D_input_deadline']==3 and counts_by['strict_old_C_cross']==counts_by['old_D_start_in_new_chord']==1
traps=[]
for a,q,t in [('D',1-1j,17),('V',2+0j,15),('U',3+1j,25)]:
 loc=(q-(-1+2j))*1j;cx=trace(W[a]+M);assert not cx[0][loc]and cx[4][loc][0]==(t,'R');traps.append((a,xy(q),t,'ownRAW'if t<len(W[a])else'nextword',t if t<len(W[a])else t-len(W[a])))
A=json.loads((D/'D30_prior_C_core_guard.json').read_text());assert[(z['h'],z['atom'],z['slot'],z['entry'],z['exit'],z['core'],z['held'])for z in roles]==[(z['heading'],z['atom'],tuple(z['last_R_slot']),tuple(z['pose'][:2]),tuple(z['endpoint']),z['is_exit_core'],list(map(tuple,z['held_tag_contacts'])))for z in A['all72_S_E_final_R_CORE_and_residual_roles']]
mp=D/'manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='511601425123e8d9d7f85fcad9a2c4566f48cc09057106a47c0e84d302c0292b'
for f in mf['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,h in A['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS D30 any actual immediately preceding E-to-N C excluded','manifest_sha256':mh,'24_bud_endpoint_guards':bud,'eight_genuine_full_output_cones':full,'three_true_full_input_deadlines':locks,'36_N0_roles':N,'two_W_roles':West,'72_core_inclusive_SE_roles':roles,'counts':dict(counts_by),'endpoint_bud_traps':traps,'analytic_review':[
'The genuine prior E-to-N C, whether first or second final tail of any containing fullpacket, ends at selectedD0,N and has actually deleted(-1,1) at own tick1/read2. No invented standalone full-C context is needed. The hole is outside selectedD entrycore; F RAW misses it and combined returnedV13/read14 requires it BLACK outside foreign core.',
'The three held tags are ordinary genuine prior atomic EXIT bud beta and D/first-postD COMMON births. Exit/common source clocks are kept distinct. The signed min3 protection and all24 actual age3 E full-input endpoint equations preserve these same IDs up toF, including marker-only absorptions. They do not rely on any V/U cohort.',
'Input(0,1) is physically deleted at the first postD atom tick1/read2. A replacement residual input must have a genuine full-output source after this deletion. A source whose full entry predates selectedD cannot export after deletion, because no full packet crosses the selectedD full entry; sourceD/DC itself does not output the cell. Any other clock0 full source starts on the zero-C N run with headx,y>=1, and all eight full output masks, including both tails, have y>=0 and x>=0 at y0, hence miss(0,1). This is FULL source entry reasoning, not an atomic birth-clock shortcut.',
'The three S2 predecessors require true input ages3,2,5, giving deadlines-1,0,-3. The correct V upper minimum is2. For a C at the candidate S pose, actual containing DC/VC/UC starts at the same clock2 and has the same lower/upper slots; the preceding W-C alternative lies below W-stage y>=2. Thus the source-input lock covers all actual containing-tail cases.',
'The first later BLACK atomic cut must follow a literal finalR, including a write into exitCORE. All36 N and36 W roles and72 S/E roles are reconstructed. Remaining S cases repeat the old C entry or D exit, cross the genuine old C strict midpoint, or cross the old D start in a later chord interior. These are nonadjacent within the signed simple OLD factor, not assumptions about the returned chord.',
'All remaining timely core repairs end at(-1,2,E). Every next old D/V/U requires a different held tagWHITE at17/15/25. D17 is NEXT actual word tick7/read8 and D cannot be last beforeF, so the physical owner is still old. No first BLACK repair cut exists. This removes only the empty preceding-N-run D30 boundary; positive preceding N-runs and other targets remain distinct.'
],'scope':mf['scope'],'dependencies':A['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],dict(counts_by))
