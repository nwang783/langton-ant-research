from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D30_UC_deleted_core_guard_2026-10-24';p=SELF.with_name('check_D15_UCC_V_core_guard_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('xp=')[0],ns)
W,M,walk,xy,K,trace,at,raw=[ns[k]for k in('W','M','walk','xy','K','trace','at','raw')]
xp=-5+0j;hole=-1+1j;goal=3-4j
req,par,ep,dh,reads=trace(W['U']+W['C']);assert at(ep,xp,1)==0 and(dh+1)%4==0
assert reads[-1+4j]==[(29,'L')]and at(-1+4j,xp,1)==hole
EK={at(q,ep,dh)for q in K};O=({q for q,b in trace(W['U']+W['C']+M)[0].items()if b}^par)-EK
assert -1+4j not in O|EK
fr=trace(W['F']);both=trace(W['F']+W['V']+M);local=(hole-goal)*1j
assert local not in fr[0]and local not in K and both[0][local]and both[4][local][0]==(69,'L')
star={at(q,xp,1)for q in[0j,1j,1+0j,1+1j]};uq=at(-1+2j,xp,1);ubud=at(1+3j,xp,1);beta=1-1j;b=2+0j;bp=3+1j;held=star|{uq,ubud,beta,b,bp};assert len(held)==9
# Exact unbounded E counts: down=d+v, dx=d+3v+4u.
def counts(ep):
 dx=int((goal-ep).real);down=int((ep-goal).imag);out=[]
 for v in range(max(0,down+1)):
  d=down-v;rem=dx-d-3*v
  if rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
buds=[]
for q in[beta,b,bp]:
 for a in'DVU':
  for slot in sorted(raw[a]['I'],key=xy):
   p=q-at(slot,0j,1);end=at(raw[a]['end'],p,1);sol=counts(end);assert end!=goal and all(v==u==0 for d,v,u in sol)
   buds.append((xy(q),a,xy(slot),xy(p),xy(end),sol))
assert len(buds)==24
N=[];West=[]
for a in'DCVU':
 for slot in raw[a]['fresh']:
  p=hole-slot;assert p.real<0 or p.imag<0;N.append((a,xy(slot),xy(p)))
  p=hole-at(slot,0j,3)
  if p.imag>=2:West.append((a,xy(slot),xy(p)))
assert set(West)=={('U',(-1,2),(1,2)),('U',(-1,3),(2,2))}
cu=walk(W['C']+W['U']+M);assert not cu['feasible']
roles=[];surv=[]
for h in[2,1]:
 for a in'DCVU':
  for slot in sorted(raw[a]['fresh'],key=xy):
   p=hole-at(slot,0j,h);end=at(raw[a]['end'],p,h);hits=held&{at(q,p,h)for q in raw[a]['ctx']};sector=(int(p.real+p.imag)+h)%2
   z={'h':h,'atom':a,'slot':xy(slot),'pose':xy(p),'end':xy(end),'core':slot in raw[a]['core'],'hits':sorted(map(xy,hits)),'reason':'sector'if sector else'held'if hits else'candidate'};roles.append(z)
   if z['reason']=='candidate':surv.append(z)
assert len(roles)==72 and len(surv)==4
assert {(r['h'],r['atom'],r['slot'],r['pose'],r['end'])for r in surv if not(r['h']==1 and r['atom']=='C')}=={(2,'C',(0,2),(-1,3),(-1,2)),(1,'D',(2,1),(-2,3),(-1,2))}
assert all(r['core']for r in surv if not(r['h']==1 and r['atom']=='C'))
traps=[]
for a,q,ti in [('D',beta,17),('V',b,15),('U',bp,25)]:
 p=-1+2j;loc=(q-p)*1j;ctx=trace(W[a]+M);assert ctx[0][loc]is False and ctx[4][loc][0]==(ti,'R');traps.append((a,xy(q),xy(loc),ti,'own_RAW'if ti<len(W[a])else'next_word',ti if ti<len(W[a])else ti-len(W[a])))
A=json.loads((D/'D30_UC_deleted_core_guard.json').read_text());assert[(r['h'],r['atom'],r['slot'],r['pose'],r['end'],r['core'],r['hits'])for r in roles]==[(r['heading'],r['atom'],tuple(r['last_R_slot']),tuple(r['pose'][:2]),tuple(r['endpoint']),r['is_exit_core'],list(map(tuple,r['held_contacts'])))for r in A['all72_S_E_final_R_CORE_and_residual_repair_roles']]
label='UCDC'+'D'*9+'CD'+'U'*3+'CD'+'U'*3+'FV';word=''.join(W[a]for a in label)+M;r=walk(word);assert not r['feasible']and(r['i'],r['q'])==(445,-1+4j)
good=walk(word[:445]);seed={q for q,b in good['req'].items()if b};assert seed==set(complex(*q)for q in A['failed_constructive_UC_entry_history']['complete_initial_black_board'])
board=set(seed);p=0j;h=0
for i,c in enumerate(word[:445]):
 assert(p in board)==(c=='L');board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
assert p==-1+4j and p not in board and word[445]=='L'
mp=D/'manifest.json';mf=json.loads(mp.read_text())
for r in mf['files']:assert hashlib.sha256((D/r['file']).read_bytes()).hexdigest()==r['sha256']
for f,h in A['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS immediate genuineUC boundary at D30 excluded by source deletion and core-inclusive repair trap','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'all24_held_bud_endpoint_obligations':buds,'all36_N0_repair_poses':N,'only_two_W_y_ge2_roles':West,'all72_core_inclusive_SE_roles':roles,'four_remaining_roles':surv,'all3_core_endpoint_traps':traps,'actual_near_control':{'initial_mass':len(seed),'successful_reads':445,'failure_cell':xy(p),'expected':'L','actual':'R'},'analytic':['UC(-5,0,E) starts old clock-1 and finishes selectedD at0. Its own C-tail tick1/read2 genuinely deletes local upper(-1,4), global(-1,1); full exit leaves it WHITE outside both O and K. F(3,-4,E) RAW misses it, and returnedV selected RAWtick13/read14 requires it BLACK beforeF. No postforeign produced-input age law is used.','The source four-star, genuine UC q and actual source exitbud remain current through foreign sourceage4 by their signed laws. Three genuine clock0 target buds beta,b,bp stay current: ages<3 are excluded by atomic minima, and all24 exact age3 full-consumer E endpoint equations cannot lead to F with permitted lastV/U. Source internalC ownership is retained.','Choose the first later actual atomic marked cut with the holeBLACK. Its immediately preceding RAW must have lastR there, so all36 atomic lastR slots are exhaustive even when the write is into EXITCORE. No N0 head reaches it. W1 can only use U q at(1,2) or U core at(2,2): y2 forces the firstW head(1,2), no laterW can increase x, and immediate C-to-U is a literal contradiction. This covers arbitrary earlier N/W lengths.','All72 S/E alignments retain exit-core writes and the complete held-identity contexts. Two E-C writes complete atclock4, too late; the genuine S-C3 and E-D3 core writes both end(-1,2,E). A later E base is required beforeF. D there requires heldbetaWHITE at context17, actual followingwordtick7/read8; V requires bWHITE own15; U requires bpWHITE own25. D cannot be the final packet beforeF, so its marker contact is within the actual old factor. Each contradicts a current same identity beforeF.','The445-read finite seed control is genuinely replayed, not a completed returned contact: the prescribed returnedV fails at its selected tick13 on the original source deletion. The universal guard is independent of this failed candidate.'],'scope':mf['scope'],'dependencies':A['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
