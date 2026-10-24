from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=P/'FIXED_COHORT_BAND_READS_MANIFEST.json';assert sha(MF)=='b333989c447ca83d9797442e790173bbcba0b2bf9d661b676d34c440e2e46ef8'
M=json.loads(MF.read_text())
for key in('files','signed_dependencies'):
 for name,d in M[key].items():assert sha(P/name)==d
J=json.loads((P/'FIXED_COHORT_BAND_READS_CHECKED.json').read_text());U=json.loads((P/'FIXED_BAND_WIDE_OUTPUT_CHECKED.json').read_text())['period_word'];V=(1j,1,-1j,-1);tests=sharp=0;geoms=[]
for phase in range(104):
 word=U[phase:]+U[:phase]
 for head in range(4):
  p=0j;h=V[head];Q=[]
  for c in word:Q.append(p);h*=(-1j if c=='R'else 1j);p+=h
  assert h==V[head]and abs(p.real)==abs(p.imag)==2
  for axis in range(2):
   coord=lambda z:int(z.real if axis==0 else z.imag)
   qs=list(map(coord,Q));d=coord(p);assert[sum(q%2==r for q in qs)for r in range(2)]==[52,52]
   for w in(1,2,3,150):
    for L in(-10,0,10,10**9 if d>0 else-10**9):
     # Independent column-by-column exact divisibility, not author's floor interval formula.
     n=sum(1 for x in range(L,L+w)for q in qs if(x-q)%d==0 and(x-q)//d>=0)
     assert n<=52*w;tests+=1
     if abs(L)==10**9:assert n==52*w;sharp+=1
  geoms.append(dict(phase=phase,heading=head,drift=[int(p.real),int(p.imag)],coordinate_parity_counts=[[52,52],[52,52]]))
assert geoms==J['all_phase_heading_cases']and tests==13312==J['exact_ray_band_tests']and sharp==3328==J['sharp_forward_band_tests']
g=json.loads((R/'audits/generic_P104_fixed_cohort_independent.json').read_text());c=json.loads((R/'audits/two_black_canonical_completion_independent.json').read_text());assert(g['one_family_max_start'],g['two_family_max_start'],g['max_switches'])==(270504,166816,5);assert c['maximum_sufficient_start'][0]==270192
assert 52*6==312 and 270504+312==270816 and 270504+312*150==317304
out=dict(status='PASS unrestricted fixed-cohort axial-band read budget, inherited complete two-black cover',manifest=sha(MF),proof=M['files']['FIXED_COHORT_AXIAL_BAND_READ_BUDGET.md'],all416_geometries=True,exact_ray_counts=tests,sharp_forward_counts=sharp,bound='270504+312w',scope='Actual reads T<=t<c3 in a fixed w-row or w-column band, where c3 is third distinct consumption of the ENTIRE black-lifetime cohort fixed once at original cut T.',dependencies=M['signed_dependencies'],analytic_review=[
'Heading alternates incoming axes every step, so each coordinate parity repeats a cyclic two-even/two-odd pattern. Any104 consecutive read positions therefore contain52 of each parity, independent of the word colors. Drift coordinate +/-2 makes each phase hit an eligible physical column/row at most once, yielding52w for any finite/infinite diagonal104 piece.',
'The signed full observation corridor transport gives at most6 such pieces and arbitrary total word length<=270504 for ALL one/two-corridor parameter members. Direct-leaf full-field completion gives prefix<=270192 and onepiece; empty/singleton envelopes are smaller. Original22-channel Main/PartData source cover is attributed and independently source-bound by prior reports, not silently replaced by representative phase tests or newly Lean-compiled here.',
'From ORIGINAL cut T, keep exactly the first two actually consumed C0 identities (or fewer if fewer ever consumed). Every omitted initialBLACK is unread until c3, so first-difference induction gives the exact full physical word, with all fresh writes/revisits retained. No causal-wake deletion or restart at an intermediate collision occurs.',
'Truncating the comparison at c3 only decreases arbitrary length and periodic piece count. The read at c3 itself is excluded. If c3=infinity, the same comparison is valid forever. No pristine, guard or active/relevant-cap hypothesis is used.',
'The band is fixed and AXIAL. Tangential diagonal bands already fail on an ordinary standard tail. New cohorts can contain fresh births, so this does not supply a cumulative original-seed fuel charge, elapsed-time bound, universal return-age bound or capture.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
