from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_interval_packet_grammar_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((D/'manifest.json').read_text());assert sha(D/'manifest.json')=='0edd9a1fd678fd4c90d0ae6b8b120e93b8f11d7919e01857ec607dd9dbc2a2ef'
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(R/'audits/check_old_V_second_age1_independent.py')};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,tr,xy=[ns[k]for k in('W','M','tr','xy')]
J=json.loads((D/'foreign_interval_grammar.json').read_text())
def trace(seq):return tr(''.join(W[a]for a in seq)+M)
def owner(seq,t):
 offset=0
 for j,a in enumerate(seq):
  if t<offset+len(W[a]):return j,a,t-offset,'RAW'
  offset+=len(W[a])
 return None,seq[-1],len(W[seq[-1]])+t-offset,'M11'
def conflict(seq,au):
 z=trace(seq);assert z['bad'];t,s,p,c=z['bad'];f=au['immutable_conflict'];assert(t,s,xy(p),c)==(f['conflict_read'],f['previous_read'],f['cell'],f['turn'])
 for tick,key in [(s,'previous_actual_reader'),(t,'new_actual_reader')]:
  j,a,local,kind=owner(seq,tick);v=au[key];assert v['actual_atom_index0']==j and v['global_tick0']==tick and v['actual_owner']['context_tick0']==local and v['actual_owner']['turn']==c
  assert v['actual_owner']['RAW_length']==len(W[a]);assert(kind=='RAW')==(local<len(W[a]))
 return dict(word=seq,first_bad_read0=t,previous_read0=s,cell=xy(p),turn=c,owners=[owner(seq,s),owner(seq,t)])
no_base=[a+'C'*n+b for n in(1,2)for a,b in product('FQB',repeat=2)]
assert len(no_base)==18 and set(no_base)=={z['packet']for z in J['all18_no_base_one_two_C_interval_conflicts']}
failed=[conflict(s,next(z for z in J['all18_no_base_one_two_C_interval_conflicts']if z['packet']==s))for s in no_base]
failed.extend(conflict(a+'CCC',next(z for z in J['all3_leading_triple_C_conflicts']if z['packet']==a+'CCC'))for a in'FQB')
packets=['D','DC','V','VC','VCC','U','UC','UCC'];allowed=[]
for a,b in product(packets,'FQB'):
 au=next(z for z in J['all24_actual_G8_last_packet_foreign_pairs']if(z['last_actual_G8_packet'],z['next_foreign'])==(a,b));ok=trace(a+b)['bad']is None;assert ok==au['feasible']
 if ok:allowed.append(a+b)
 else:failed.append(conflict(a+b,au))
assert set(allowed)=={'VF','VQ','UF','UQ','UB'}
empty=[]
for a,b in product('FQB',repeat=2):
 seq=a+b;au=next(z for z in J['all9_empty_interval_pairs']if z['packet']==seq);ok=trace(seq)['bad']is None;assert ok==au['feasible']
 if ok:empty.append(seq)
 else:failed.append(conflict(seq,au))
assert set(empty)=={'QF','BF'}
positive=[]
for au in J['all5_prepared_full_field_scope_controls']:
 seq=au['packet'];z=trace(seq);assert z['bad']is None;seed={p for p,c in z['req'].items()if c};assert sorted(map(xy,seed))==au['complete_seed'] and len(seed)==au['seed_mass'];black=set(seed)
 for p,h,c in z['reads']:
  assert(p in black)==(c=='L');black.symmetric_difference_update({p})
 assert len(black)==au['final_physical_mass']and len(z['reads'])==au['actual_reads'];assert[*xy(z['p']),z['h']]==list(au['after_actual_M_prefix']);raw=tr(''.join(W[a]for a in seq));assert[*xy(raw['p']),raw['h']]==list(au['RAW_EXIT'])
 positive.append(dict(word=seq,reads=len(z['reads']),seed=au['complete_seed'],complete_final=sorted(map(xy,black))))
failed.extend(conflict(z['packet'],z)for z in J['all2_immediate_U_prepend_conflicts_not_general_ancestry'])
review=[
'If a nonempty ordinary interval has no BASE, it is C^r. Literal A CCC with actual M forbids r>=3; every next actual RAW supplies this marker prefix, and no unexecuted next packet is required. Exact eighteen ACB/ACCB conflicts remove r1/2.',
'The selected BASE-start ordinary suffix begins at an actual D/V/U, with leading Cs excluded. Its first D has a genuine immediately preceding RAW (sourceFOREIGN or leadingC), so the incoming-bud DCCC guard has its actual supplier. Every internal marker is actual, and the terminal cut admits a genuinely COMPLETE nextFOREIGN plus its realM11.',
'Thus signed8a plus the nonterminal-cut7ae apply to exactly this selected suffix. TerminalDCC is excluded only by the actually completed nextFOREIGN, never by mistaking M11 alone for a whole nextG7. The final actual packet is in G8.',
'The literally reconstructed24 packet/FOREIGN pairs leave only VF,VQ,UF,UQ,UB, all plain V/U endings. This local immutable-pair fact has no FIRSTforeign or U-entry premise, even though some historic uses imposed those additional hypotheses.',
'For consecutive foreign atoms the interval is empty, and QF/BF remain complete prepared possibilities. Hence no laterFOREIGN has immediately precedingC. In an actual U-start seven-RAW factor, the first ordinary section has a genuine BASE start and actual nextFOREIGN, so the same parse handles its firstFOREIGN too.',
'CF/CQ/CB prepared full fields remain positive when the preceding foreign/base history is absent. Immediate UQF/UBF failures are only those two literal prepends, not a general ancestry exclusion. No word-language coverage, tag iteration, geometry or capture follows.'
]
out=dict(status='PASS scoped all-length actual foreign-interval grammar',manifest=sha(D/'manifest.json'),dependencies=m['dependencies'],literal_failures=failed,allowed_packet_boundaries=allowed,allowed_empty_intervals=empty,complete_positive_controls=positive,analytic_review=review,scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
