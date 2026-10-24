from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D15_UCC_V_core_guard_2026-10-24';p=SELF.with_name('check_foreign_kinked_barrier_turn_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('geometries=[]')[0],ns)
W,M,walk,xy=[ns[k]for k in('W','M','walk','xy')];K={-1-1j,-1+0j,-1j,0j,1+0j}
def trace(w):
 p=0j;h=0;reads={};par=set();req={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b;req[p]=b;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h
 return req,par,p,h,reads
def at(q,p,h):return p+q*(-1j)**h
raw={}
for a in'DCVU':
 req,par,ep,dh,reads=trace(W[a]);ctx=trace(W[a]+M)[0];fresh={q for q,rr in reads.items()if rr[-1][1]=='R'};core={at(q,ep,dh)for q in K};I={q for q,b in ctx.items()if b}-K
 assert all(q.imag>=0 and q.real+q.imag>=0 for q in fresh)
 raw[a]={'end':ep,'turn':dh,'reads':reads,'ctx':ctx,'fresh':fresh,'core':core,'I':I}
assert sum(len(z['fresh'])for z in raw.values())==36
xp=-2+2j;hp=-1-3j;goal=2-5j;hole=-2-4j
xreq,xpar,xe,xh,xrd=trace(W['U']+W['C']*2);assert at(xe,xp,2)==hp and(xh+2)%4==0
assert hp+raw['V']['end']==0j and raw['V']['reads'][-1-1j]==[(2,'L')]
assert hp-1-1j==hole and hole not in K
star={at(q,xp,2)for q in[0j,1j,1+0j,1+1j]};Hr=hp;HB=hp+1;Hb=hp+2;beta=1-1j;b=2+0j;bp=3+1j;held=star|{Hr,HB,Hb,beta,b,bp};assert len(held)==10
# Genuine births and their raw continuations, rather than introduced black guards.
for q in[0j,1+0j,2+0j,2+2j]:assert raw['V']['reads'][q][-1][1]=='R'
assert raw['D']['reads'][2+0j][-1][1]=='R'
for a in'DCVU':assert raw[a]['reads'][2+0j][0]==(8,'R')
# Arbitrary-length E count equations exhausted from exact nonnegative vertical budget.
def counts(ep,goal=goal):
 dx=int((goal-ep).real);down=int((ep-goal).imag);out=[]
 for v in range(max(0,down+1)):
  d=down-v;rem=dx-d-3*v
  if rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
budrows=[]
for q in[Hb,beta,b,bp]:
 for a in'DVU':
  for slot in sorted(raw[a]['I'],key=xy):
   p=q-at(slot,0j,1);ep=at(raw[a]['end'],p,1);sol=counts(ep)
   assert ep!=goal and all(v==u==0 for d,v,u in sol)
   budrows.append({'tag':xy(q),'base':a,'slot':xy(slot),'entry':xy(p),'exit':xy(ep),'counts':sol})
assert len(budrows)==32
last=[]
for a in'VU':
 p=goal-at(raw[a]['end'],0j,1);loc=(hole-p)*1j
 assert loc in K and raw[a]['reads'][loc][0][1]=='L'
 last.append({'base':a,'entry':xy(p),'hole_local':xy(loc),'read':raw[a]['reads'][loc][0]})
assert last==[{'base':'V','entry':(-1,-4),'hole_local':(0,-1),'read':(3,'L')},{'base':'U','entry':(-2,-5),'hole_local':(-1,0),'read':(1,'L')}]
roles=[];kept=[]
for h in[2,1]:
 for a in'DCVU':
  for slot in sorted(raw[a]['fresh'],key=xy):
   p=hole-at(slot,0j,h);ep=at(raw[a]['end'],p,h);hits=held&{at(q,p,h)for q in raw[a]['ctx']};sector=(int(p.real+p.imag)+h)%2
   typ='sector'if sector else'held_context'if hits else'candidate'
   z={'h':h,'atom':a,'slot':xy(slot),'entry':xy(p),'exit':xy(ep),'core':slot in raw[a]['core'],'hits':sorted(map(xy,hits)),'type':typ};roles.append(z)
   if typ=='candidate':kept.append(z)
assert len(roles)==72 and len(kept)==8
expect={(2,'C',(0,2),(-2,-2),(-2,-3),True),(2,'V',(0,2),(-2,-2),(-3,-5),True),(2,'U',(-1,3),(-3,-1),(-3,-5),True),(1,'D',(2,1),(-3,-2),(-2,-3),True),(1,'V',(2,3),(-5,-2),(-2,-3),True),(1,'U',(1,4),(-6,-3),(-2,-3),True),(1,'V',(0,1),(-3,-4),(0,-5),False),(1,'U',(-1,2),(-4,-5),(0,-5),False)}
assert{(z['h'],z['atom'],z['slot'],z['entry'],z['exit'],z['core'])for z in kept}==expect
assert raw['U']['reads'][-1+2j]==[(13,'L'),(21,'R')]and -1+2j in raw['U']['I']
assert counts(-2-3j)==[(1,1,0)]and not counts(-5j)
assert at(1j,-2-3j,1)==Hr
# Compare all actual role geometry and held contacts with the immutable author table.
author=json.loads((D/'D15_UCC_V_core_guard.json').read_text())
assert[(z['h'],z['atom'],z['slot'],z['entry'],z['exit'],z['core'],z['hits'])for z in roles]==[(z['heading'],z['atom'],tuple(z['last_R_local']),tuple(z['pose'][:2]),tuple(z['endpoint']),z['birth_is_exit_core'],list(map(tuple,z['held_tag_contacts'])))for z in author['all72_S_E_final_R_BLACK_cut_birth_roles']]
mp=D/'manifest.json';mf=json.loads(mp.read_text())
for z in mf['files']:assert hashlib.sha256((D/z['file']).read_bytes()).hexdigest()==z['sha256']
out={'status':'PASS D15 actual UCC,V boundary deleted-core repair obstruction','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'held_tags':sorted(map(xy,held)),'all32_bud_endpoint_tests':budrows,'last_foreign_predecessor_core_reads':last,'all72_atomic_last_R_roles':roles,'eight_surviving_roles':kept,'analytic':['Actual UCC at(-2,2,S) begins clock-2, ends H=V(-1,-3,N)clock0, then selectedD/DC starts(0,0,N)clock0. Ustar permanence and H originalr/B first-retirement5/4 laws hold throughout preforeign clocks<=3. H really deletes its entry-corez(-2,-4) at RAWtick2, leaves it WHITE at exit and outside exitcore. Both possible last plainV/U beforeF require this veryz BLACK in their entryK.','H common and exitbud, selectedD common and the first actual postD atomic common are genuine clock0 births. Signed minimum3 excludes earlier full consumption. At clock3 any first fullconsumer finishing beforeF must be plainE D/V/U; all32 exact residual-input alignments have no E continuation ending with permitted lastV/U. Marker-only/core-absorption input roles are included. Thus these four identities are TARGET-specifically held throughFentry, not globally permanent or held afterF.','Any earliest postH atomic cut withzBLACK has a previous actual RAW lastR atz; unreadz would already have beenBLACK at the preceding cut. Including ALL36 lastR slots of D/C/V/U covers exit-core writes as well as residual outputs. N0 y>=0 and W1(y-x)>=1, with all these slots y>=0 and x+y>=0, exclude those phases. Fresh72 S/E alignment rows leave exactly8 after sector and genuinely held-tag complete-context tests. Containing-full-packet clocks remain real; no independent C marker is inserted.','The two S2 V/U core writes endy=-5 and must still pass C3 droppingy, so cannot reach foreigny=-5. C3 and three E3 core writers all exit(-2,-3,E). Only subsequent countsD1,V1,U0 reachF(2,-5,E): orderVD violates lastpacket, orderDV consumes genuineH r at age3<5. The E3 residualV ends(0,-5), whose same-y gap2 cannot be covered by U strides4. The E3 recycledUq requiresz as actual entryinput before its R rewrite, contradicting the earliestBLACK-cut choice.','This is a BLACK-at-actual-cut descent, not a false physical whiteness invariant and not a residual-only ancestry assertion. All held identities are used only beforeF; F may later rewrite beta or core. The resulting contradiction removes exactly horizon UCC,V,D/DC at D15, for arbitrary earlier history and arbitrary allowed old connector.'],'scope':'One finite boundary interface only. No allD15 exclusion, returned simplicity, postforeign maturity, positiveUentry attainment or general source-history bound.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
