from pathlib import Path
from itertools import product
import json,hashlib,ast,random
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mp=D/'FINITE_RECORD_CLOCK_MANIFEST.json'
assert sha(mp)=='09b1ee22b19b6231f05cb3ddca593b49ec8e779391131c4a032a08584c9b8b04';M=json.loads(mp.read_text())
for f,h in M['files'].items():assert sha(D/f)==h
for f,h in M['dependencies'].items():assert sha(D/f)==h
J=json.loads((D/'RECORD_CLOCK_FINITE_BASIS_CHECKED.json').read_text());V=[(0,1),(1,0),(0,-1),(-1,0)]
# Independent finite assignment expansion. At each terminal branch enumerate ALL
# unassigned cylinder bits directly, rather than use the author's cofactoring.
def coverage(H,T,guards):
 cap=max([T]+[m for g in guards for m in g['bounds'].values()]+[abs(c)for g in guards for q,b in g['bits']for c in q])
 cells={tuple(q)for g in guards for q,b in g['bits']};leaves=0;valid=0;bounds_count=0
 def proj(q):return(q[1],q[0],-q[1],-q[0])
 for bds in product(list(range(cap+1))+[None],repeat=3):
  initial=(0,)+bds;bounds_count+=1
  def forced(q):return q[1]>=0 or any(m is not None and z>m for z,m in zip(proj(q),initial))
  stack=[(0,(0,0),0,initial,{},set(),(0,))]
  while stack:
   t,p,h,extent,bits,odd,records=stack.pop()
   if t:
    now=proj(p);record=any(m is not None and v>m for v,m in zip(now,extent))
    extent=tuple(None if m is None else max(m,v)for v,m in zip(now,extent))
    if record:records=records+(t,)
   # Direct block definition, independent of last-event shortcut.
   if any(not any(u<v<=u+H for v in records)for u in range(max(0,t-H+1))):continue
   if t==T:
    leaves+=1;unknown=sorted(q for q in cells if q not in bits and not forced(q))
    for vals in product((0,1),repeat=len(unknown)):
     assign=bits|dict(zip(unknown,vals));valid+=1
     ok=any(all(initial[int(a)]==m for a,m in g['bounds'].items())and all((0 if forced(tuple(q))else assign[tuple(q)])==v for q,v in g['bits'])for g in guards)
     if not ok:return dict(covered=False,cap=cap,bounds=bounds_count,leaves=leaves,witness=dict(offsets=initial,black=sorted(q for q,v in assign.items()if v),head=p,heading=h))
    continue
   values=[0]if forced(p)else[bits[p]]if p in bits else[0,1]
   for x in values:
    c=x^(p in odd);hh=(h+(-1 if c else 1))%4;pp=(p[0]+V[hh][0],p[1]+V[hh][1]);stack.append((t+1,pp,hh,extent,bits|{p:x},odd^{p},records))
 return dict(covered=True,cap=cap,bounds=bounds_count,leaves=leaves,assignments=valid)
empty=coverage(1,3,[]);assert empty['covered']and empty['bounds']==125 and empty['leaves']==0
nonempty=coverage(1,2,[]);assert not nonempty['covered']
boolean=coverage(1,2,[dict(bounds={1:0,2:0},bits=[])]);assert boolean['covered']and boolean['leaves']==4 and boolean['bounds']==64
# Extract just the author's pure finite-cover definition for differential testing.
source=ast.parse((D/'check_record_clock_finite_basis.py').read_text());fn=next(n for n in source.body if isinstance(n,ast.FunctionDef)and n.name=='finite_cover');ns={'product':product,'DXY':V};exec(compile(ast.Module(body=[fn],type_ignores=[]),'<pure author cover>','exec'),ns)
rng=random.Random(104);tests=[]
for i in range(60):
 H=rng.randint(1,3);T=rng.randint(0,3);guards=[]
 for j in range(rng.randint(0,3)):
  bounds={a:rng.randint(0,2)for a in range(1,4)if rng.randrange(3)==0};bits=[]
  for q in rng.sample([(x,y)for x in range(-2,3)for y in range(-2,1)],rng.randint(0,2)):bits.append((q,rng.randint(0,1)))
  guards.append(dict(bounds=bounds,bits=bits))
 own=coverage(H,T,guards);au=ns['finite_cover'](H,T,guards);assert own['covered']==au['covered'];tests.append((H,T,len(guards),own['covered']))
# Generic arbitrary-word infinite parity test, with direct testing of every
# integer period index up to the last possible change and its stable successor.
def verify(B,w,heading=0):
 p=(0,0);h=heading;Q=[]
 for c in w:
  Q.append(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 d=p;assert h==heading and d!=(0,0);axis=0 if d[0]else 1
 def multiple(z):
  if z[axis]%d[axis]:return None
  k=z[axis]//d[axis];return k if z==(k*d[0],k*d[1])else None
 checks=0;cutoffs=[]
 for i,q in enumerate(Q):
  flips=[];hits=[]
  for j,z in enumerate(Q):
   k=multiple((z[0]-q[0],z[1]-q[1]))
   if k is not None and(k>0 or k==0 and j<i):flips.append(k)
  for z in B:
   k=multiple((z[0]-q[0],z[1]-q[1]))
   if k is not None and k>=0:hits.append(k)
  cutoff=max([0]+flips+[k+1 for k in hits])+1;cutoffs.append(cutoff)
  for k in range(cutoff+1):
   if(bool(sum(v<=k for v in flips)%2)^((q[0]+k*d[0],q[1]+k*d[1])in B))!=(w[i]=='L'):return None
   checks+=1
 return Q,d,checks,cutoffs
sources=json.loads((D/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())['normal_catalog'][0]['records'];certs=[]
for r,au in zip(sources,J['outward_periodic_certificates']):
 B={(-q[1],q[0])for q in r['required_black']};w=r['cycle_word'];z=verify(B,w);assert z is not None;Q,d,checks,cutoffs=z;assert d==(2,2)and all(y<0 for x,y in B)
 # Exact half-plane footprint, including arbitrarily many phase translations.
 F=set()
 for q in Q:
  for k in range(max(0,(-q[1])//d[1]+1)):F.add((q[0]+k*d[0],q[1]+k*d[1]))
 guard=[[list(q),int(q in B)]for q in sorted(F)];assert guard==au['guard']and B<=F
 mutations=[]
 for q in sorted(B):assert verify(B-{q},w)is None;mutations.append(q)
 # Physical replay, with generalized only-N-finite records. Infinity is not
 # replaced by a finite guessed hull in this comparison.
 board=set(B);p=(0,0);h=0;maxy=0;last=0;gaps=[]
 for t in range(6*len(w)):
  if p[1]>maxy:gaps.append(t-last);last=t;maxy=p[1]
  assert(p in board)==(w[t%len(w)]=='L');board.symmetric_difference_update({p});h=(h+(1 if w[t%len(w)]=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 assert gaps==au['six_period_record_gaps']and max(gaps)<=104
 certs.append(dict(phase=r['phase'],drift=d,period=len(w),guard=guard,all_integer_parity_checks=checks,stable_thresholds=cutoffs,all_black_mutations_rejected=len(mutations),record_maxgap=max(gaps)))
assert len(certs)==2
O=dict(status='PASS effective finite record-clock forcing theorem, with arbitrary period and global full-seed hull premise',manifest=sha(mp),proof=M['files']['FINITE_RECORD_CLOCK_FORCES_TRANSLATION.md'],script=sha(S),H1_F3=empty,H1_T2=nonempty,Boolean_cover=boolean,differential_finite_cover_controls=tests,outward_certificates=certs,analytic_review=[
'X is compact: each forbidden BLACK outside a side is a clopen finite-valued offset condition. N side is exactly0 and whole y>=0 isWHITE. Infinity is one compactification value, not arithmetic infinity. Any finite support-compatible assignment extends by making unassigned cellsWHITE.',
'E_H,T is clopen and nested, using every block(u,u+H] withu+H<=T. RadiusT and offsets0..T/>T suffice. At arbitrary s,t on K_H, endpoint-inclusive event gaps are<=H, so signed last-direction recursion applies using only initially finite normals.',
'For p_t in generalizedR_s, duration<=H(H+1)^m, m<=4. Thus no original BLACK is ever read afterG. Only finitely many originals are read beforeG; deleting the remaining possibly infinite initial set preserves every finite future by first-discrepancy induction. Consumed R ages<=G and after originals retire the entire normalized relevant set lies in radiusG.',
'Finite normalized exact-pruning states force identical future words/poses at two cuts, hence translation. Infinite union records rule out zero drift and force positive drift against an INITIALLY FINITE side. If no finite side had positive drift, all finitely many finite maxima would eventually stop expanding.',
'An outward translating tail has FINITE read footprint in that finite old half-plane. Fix its offset EXACTLY and all initial colors on that footprint. Every field in the relative cylinder agrees forever, since outside the half-plane the full initial support promise forcesWHITE. Other offsets may vary without weakening the fixed side. This proves genuine relative openness, not merely local convergence.',
'K_H lies in the open unionO of all such forcing cylinders. If no E_H,T lay inO, the nested nonempty compact E_H,T intersect(X minusO) would contradict the inclusion. Thus some finite clock window forces translation.',
'Finite board/prefix/arbitrary period/side/offset enumeration is effective. Infinite periodic validation is decidable by all initial finite-field ray hits and all previous-period threshold coincidences. Each member ofK_H has an enumerated finite pruned initial comparison board, so the emitted cylinders cover it without an oracle for general attraction.',
'A finite cover test partitions all free offsets at a cutoff containingT, every exact guard offset and every inspected coordinate. The unbounded class>L has identical finite tests for all finite values and infinity. Enumerate compatible colors on the finite union of the T box and guard cells; extension byWHITE proves this finite decision complete. Compactness gives a finite emitted subcover, so dovetailing T and certificate prefixes TERMINATES for everyH.',
'Infinite H104 controls do not rely merely on six sampled periods: for a no-prefix positive-N repeated word, any running north maximum is attained among the most recentP cuts or the initialcut. Its translate one period later is higher, guaranteeing a new north record in everyP-block.',
'For a nontranslator and any startingcutv, either(v,v+H] isalready a drought or it containsrecord s<=v+H. Its F(H) test mustfail, yielding an H-block within(v,v+H+F(H)]. All quantifiers refer to the same complete orbit and augmented full initial-seed hull.'
],scope='Total computable but uncomputed F(H>=2). Finite H-dense record window at a pristine augmented-hull record forces eventual translating turns/poses, not complete-board equality. Every nontranslator has an H-drought in every interval lengthF(H)+H. No universal forcing-window occurrence, canonical104 uniqueness, practical bound or finite-seed noncapture decider. Undisclosed remote BLACK may change the global hull and invalidate the premise.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
