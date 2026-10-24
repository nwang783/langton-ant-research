from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'critical_flat_RIGHT_two_ended_providers_and_exact_voltage.md';assert sha(F)=='6d8ef66c19610fd4038e58ef0989fc39b71c4ad259bbdff41c9b5262d6e805ff'
H='NESW';out=lambda w:[H[(H.index(c)+(1 if r%2==0 else-1))%4]for r,c in enumerate(w)];ports={}
for name,w in [('X','EEWW'),('Y','EWWE')]:
 inc=[r for r,c in enumerate(w)if c=='E'];dep=[r for r,c in enumerate(out(w))if c=='S'];assert len(inc)==len(dep)==2
 exitrank,entryrank=inc[1],dep[1];assert(exitrank,entryrank)==((1,3)if name=='X'else(3,1));ports[name]=dict(history=w,exit_rank=exitrank,entry_rank=entryrank,external_duration='P+A'if name=='X'else'P-A')
# Independently check invertibility of all allowed high macros and constant2 through profile.
J=json.loads((R/'audits/check_mixed_second_lane_independent.json').read_text())
through=[r['second_lane']for r in J['all10_flow3_scatterings']if r['flow3_turn_word']in('RR','RLR')]+[J['flow4']['second_lane']]
assert len(through)==3
for sc in through:assert sc['kind']=='THROUGH'and sc['output_ordinal']==2 and sc['route'][0]['rank']==sc['route'][-1]['rank']==2
assert next(r for r in J['flow2']if r['history']=='WWEE')['second_lane']['route'][0]['rank']==3
obj=dict(status='PASS dependent two-ended flat provider localization and exact full-drift voltage',proof=sha(F),flat_ports=ports,dependencies={str(p.relative_to(R)):sha(p)for p in[R/'audits/check_mixed_RR_closure_independent.json',R/'audits/check_critical_mixed_LL_exits_independent.json',R/'audits/check_mixed_first_track_pipeline_independent.json']},analytic_review=[
'The signed critical first-track identity P=sum RIGHTfactorlengths+sum crossing spans implies each SAME-PHYSICAL L1->R2 span<P. This is derived, not a global cap4 age assumption.',
'Forward and backward selected actual second-lane prefixes are unique/invertible through RR/RLR3,isolated4 andLEFTV, with all other channels retained. Backward stop is either a flat outgoing-second event or a rootL1. The latter at another physical cell would violate the same-contact excursion; a complete backward lap reaches u+d, not u. Thus both flat providers exist before a full lap.',
'Every flat stops the selected lane, and every other flow2 crossing would be a forbidden wrong physical endpoint. Hence the providers are nearest flats along the lifted b direction and each cyclic gap has at most1flow2root. Passive/exterior contacts after departure remain unrestricted.',
'Write v_(k+ell)=v_k-d, rootv0, forwardF=v_j with0<j<ell, backwardG=v_i with-ell<i<0. Same FULL quotient class forces j-i=ell, hence G=F+d. No representative/time modP reduction is used.',
'X has exitL1/entryL3, so actual connector duration P+(T3F-T1F)>P is impossible. Y has exitL3/entryL1, duration P-A>0. The two literal boundary paths contain j-i=ell steps, giving rootspan=P+ell-A. Rootspan<P forces ell<A, so ell<A<P.',
'If exactly1flat class and at least1flow2root, the first-hit injection gives exactly1root, the flat mustY, and the unresolved physical connector is F.L3->(F+d).L1. This is not a reversed same-cell clock, not a constructed exterior, and not a fuel or general oneuse/front exclusion.'
]);S.with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['status']);print(sha(S.with_suffix('.json')))
