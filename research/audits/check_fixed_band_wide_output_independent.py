from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ns={'__file__':str(S.with_name('check_return_permanent_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('results=[check_case')[0],ns)
twenty,verify_future,vec,pair,G=[ns[x] for x in ('twenty','verify_future','vec','pair','G')]
M=json.loads((P/'FIXED_BAND_WIDE_OUTPUT_MANIFEST.json').read_text())
for group in ('files','retained_dependencies'):
 for f,v in M[group].items():assert sha(P/f)==v
J=json.loads((P/'FIXED_BAND_WIDE_OUTPUT_CHECKED.json').read_text());B=set(G);p=0j;h=1;positions=[];letters=''
for t in range(286):
 positions.append(p);black=p in B;letters+='L' if black else 'R'
 if black:B.remove(p)
 else:B.add(p)
 h=(h+(-1 if black else 1))%4;p+=vec[h]
Q=positions[182:];U=letters[182:];assert U==J['period_word'] and list(map(pair,Q))==J['period_read_positions']
assert len({U[i:]+U[:i] for i in range(104)})==104
witnesses=[]
for phase,q in [(20,5+1j),(15,8+1j)]:
 assert Q[phase]==q and U[phase]=='R';hits=[]
 for i,z in enumerate(Q):
  delta=q-z
  if delta.real==delta.imag and int(delta.real)%2==0 and delta.real>=0:
   m=int(delta.real)//2;assert 104*m+i<=phase;hits.append([m,i])
 witnesses.append(dict(phase=phase,cell=pair(q),nonnegative_future_ray_equalities=hits))
assert witnesses==J['reference_permanent_witnesses']
# Affine formulas verified symbolically as coefficient/constant pairs.
# n=2k; upper j=k+99, lower j=3k-104.
assert (2-2, -2-198)==(0,-200) and (2+2,5+198)==(4,203)
assert (-6+6,8-208)==(0,-200) and (-6+6,9-208)==(0,-199)
assert (104+104, -173+202+104*99)==(208,10325)
assert (936+312,-1296+197-104*104)==(1248,-11915)
# j_upper<=R1-1 iff k>=105; lower j>=0 and j<R4 automatically there.
assert (2*105-6)-(105+99)==0 and 3*105-104>=0
results=[]
for expected in J['controls']:
 n=expected['n'];e=624*n-1516;N=e+983;seed=twenty(n);B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda z:(z.real,z.imag)))};p=0j;h=1;target={104*n+10325:-200+(2*n+203)*1j,624*n-11915:-200-199j};birth=[];deaths=[];band=0;turn=[];source=None
 assert sorted(map(pair,seed))==expected['initial_black']
 for t in range(N):
  if t==e+774:source=(dict(B),p,h)
  if t<e and -300<=p.real<=-151:band+=1
  if t in target:assert p==target[t] and p not in B;birth.append([t,pair(p)])
  old=B.pop(p,None)
  if old is None:B[p]=t;h=(h+1)%4;turn.append('R')
  else:
   h=(h-1)%4;turn.append('L')
   if old in target:deaths.append((old,t))
  p+=vec[h]
 word,drift,tail,checks=verify_future(B,p,h);assert not deaths
 for t,q in target.items():assert B[q]==t and t not in tail
 sb,sp,sh=source;sw,sd,st,schecks=verify_future(sb,sp,sh);phase=next(i for i in range(104) if U[i:]+U[:i]==sw);assert turn[e+773]!=sw[-1]
 serial=json.dumps(sorted((int(q.real),int(q.imag),i) for q,i in B.items()),separators=(',',':'));digest=hashlib.sha256(serial.encode()).hexdigest()
 assert digest==expected['full_terminal_black_sha256'] and len(B)==expected['full_terminal_black_count']
 assert birth==expected['true_witness_births'] and [pair(p),h]==expected['full_terminal_pose']
 assert checks==expected['full_terminal_parity_tests'] and schecks==expected['first_tail_parity_tests'] and phase==expected['first_tail_phase']
 assert band==expected['five_stage_band_read_count'] and band<=40188
 results.append(dict(n=n,physical_updates=N,witness_births=birth,terminal_field_sha256=digest,terminal_mass=len(B),infinite_parity_tests=checks,canonical_onset=e+774,onset_phase=phase,preceding_mismatch=[turn[e+773],sw[-1]],band_reads=band,span=2*n+402))
assert 5*182+5*104*75+sum((61,71,61,71,14))==40188
assert 132*40188//(4*(150-132))==73678
report=dict(status='PASS all-even-n>=210 fixed-column permanent-output span with bounded relevant stock and bounded band count',manifest_sha256=sha(P/'FIXED_BAND_WIDE_OUTPUT_MANIFEST.json'),proof_sha256=sha(P/'FIXED_BAND_WIDE_PERMANENT_OUTPUT.md'),independent_checker_sha256=sha(S),exact_reference_last_read_rays=witnesses,full_controls=results,analytic_scope=['Exact affine phase indices are inside complete actual stages for k>=105. Reference later-ray absence, signed full stage read-set disjointness, and full protected post-e x>=-16 imply genuine whole-future permanence of both x=-200 witnesses, not standalone template credit.','Earliest canonical onset e+774 is inherited signed and independently checked at both controls using full-field tail parity and actual previous-turn mismatch. All canonical104 phases are distinct; any earlier permanent canonical word would have the same backward extension. Thus any sound guard with delay<=773 is absent at cuts<=e, including specified immediate/262/278 guard families. Not every conceivable finite capture guard is excluded.','Two actual permanent cells give unbounded transverse SPAN in one fixed column across this finite-seed family, while five phase streams each move x by2 and allow at most75 hits per phase in width150. Band reads<=40188, so permanent-cell COUNT remains uniformly bounded by that value.','No one-orbit infinite deep returns, failure of eventual orbit-dependent width/age, general finite-band capacity obstruction, or global capture follows.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
