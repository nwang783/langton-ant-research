from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'critical_mixed_boundary_requires_two_flat_RIGHT_classes.md';assert sha(P)=='7e054b53d2d71147fea3b86b4d923e76da4f529af7d9534c218d2ae3d713016c'
J=json.loads((D/'check_local_sink_Y_source_reader_gate.json').read_text());H='NESW';V=dict(N=1j,E=1,S=-1j,W=-1);out=lambda w:[H[(H.index(c)+(1 if r%2==0 else -1))%4]for r,c in enumerate(w)];words=lambda axis:[''.join(x)for n in range(1,5)for x in product(axis,repeat=n)]
source=[w for w in words('NS')if w[0]=='N'and w.count('N')==2 and out(w).count('E')in(3,4)];sink=[w for w in words('NS')if w[0]=='N'and w.count('N')in(3,4)and out(w).count('E')==2];assert set(source)=={'NSN','NSNS'}and set(sink)=={'NNN','NNNN'}
assert{(r['rail']['S'],r['rail']['B'])for r in J['all_four_local_rails']}==set(product(source,sink))
for a,b in product(source,sink):assert out(a).count('W')==0 and b.count('S')==0 and 'NSSN'.count('S')==out('NSSN').count('W')==2
# Uncapped algebra: zeroWinput makes all L0 lettersE; numberR=ceil(n/2)=2.
L0=['E'*n for n in range(1,5)if(n+1)//2==2];assert L0==['EEE','EEEE']
# ZeroSoutput forces every even rankW and oddrankE; Win=numberR=2.
L2=[''.join('W'if r%2==0 else'E'for r in range(n))for n in(3,4)];assert L2==['WEW','WEWE']
poss=[]
for a,b,q in product(L0,L2,words('NS')):
 if q.count('N')==out(b).count('N')and out(q).count('E')==a.count('E'):poss.append((a,b,q))
assert set(poss)=={('EEE','WEW','NNNS'),('EEE','WEW','NSNN')};routes=[]
for a,b,q in poss:
 hs={0j:'NSSN',-1+0j:b,-1+1j:q,1j:a};at=(0j,2);route=[at]
 for _ in range(4):
  p,r=at;dr=out(hs[p])[r];ordinal=[s for s,h in enumerate(out(hs[p]))if h==dr].index(r);z=p+V[dr];rank=[s for s,h in enumerate(hs[z])if h==dr][ordinal];at=(z,rank);route.append(at)
 assert route==[(0j,2),(-1+0j,0),(-1+1j,0),(1j,0),(0j,1)];routes.append(dict(Q=q,literal_route=[[[int(p.real),int(p.imag)],r]for p,r in route]))
assert routes==J['cap4_Q_profiles']
# Exact LL closing port mismatch for every one-flat/high endpoint pair.
Aflat=['EEWW','EWWE'];Ahigh=['EWE','EWEW'];Bflat=['SSNN','SNNS'];Bhigh=['SSS','SSSS'];mismatch=[]
for a,b in list(product(Aflat,Bhigh))+list(product(Ahigh,Bflat)):
 x,y=out(a).count('N'),b.count('N');assert{x,y}=={0,2};mismatch.append([a,b,x,y])
rr=json.loads((S.parent/'check_mixed_RR_closure_independent.json').read_text());pairs=rr['no_one_use_RIGHT_pairs']
for a,b,f in pairs:
 if a in Aflat or b in Bflat:assert a in Aflat and b in Bflat
obj=dict(status='PASS critical global-max no-one-use cap4 b-circle needs >=2 flat RIGHT full-quotient classes',proof=sha(P),script=sha(S),author_checker=sha(D/'check_local_sink_Y_source_reader_gate.py'),author_certificate=sha(D/'check_local_sink_Y_source_reader_gate.json'),derived_sources=source,derived_sinks=sink,uncapped_helpers=dict(L0=L0,L2=L2),local_routes=routes,all_one_flat_LL_port_mismatches=mismatch,dependencies={str((S.parent/f).relative_to(R)):sha(S.parent/f)for f in['check_mixed_flow2_flat_islands_independent.json','check_mixed_RR_closure_independent.json','check_mixed_first_track_pipeline_independent.json','check_one_flat_high_owner_independent.json']},analytic_review=[
'ZeroW-in atL0 forces every incomingE; Sout2 fixes ceil(n/2)=2, so n3/4 without any helper cap. ZeroS-out atL2 forbids evenE and oddW; Win2 again fixes n3/4. Thus the cap4 contradiction is specifically Q: its only exact3/4 count matches areNNNS/NSNN, yielding the actual first-ordinal fourR path F.R2->F.L1. No periodic or drift hypothesis is required for this local fifth-reader lemma.',
'Supposing oneflat, signed global-max localisland exclusion eliminates allflow2O/U roots. Actual transparent-lane argument fixes flatY, while nonempty LEFT plus one actualPevent orbit requires a crossing. With flow2 crossings absent it is LEFT3WEEE, belonging to an RLR3 macro with TWO nonflatRIGHT classes. Together with flatY and zero turning this gives at least3RIGHT/3LEFT, hence ell>=6; short full-quotient aliases are not silently excluded.',
'The complete RR pair cover shows a flat inRR would require a secondflat. Its two neighbors are thereforeLEFT, equalflow2, henceV with noO/U. If either neighboringV belongs toLL, the otherRIGHT end is distinct fromF since ell>=6 and is a high sink/source. The eight exact closing-port tests force flow2 versus0, impossible independently of other stock. Threeequalturns are excluded by embedded essential simplicity.',
'Both V neighbors are singletonLEFT. NormalizeF=NSSN at0,0; their outerRIGHTs are at-1,-1 and1,1 and, by complete cap4 boundary counts with nootherflat/nooneuse, are exactly NNN/NNNN and NSN/NSNS. The local fifthreader contradicts completecap4. Existing mandatoryflat theorem excludes0, so >=2flatFULLclasses follows.',
'The signed one-flat owner/voltage interface remains a valid conditional statement, but its complete criticalglobalM cap4 antecedent is now excluded. Multi-flat old-stock/exterior completions, K>=2, fronts withoneuse edges and generalglobalcapture remainOPEN.'
]);S.with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['status']);print(sha(S.with_suffix('.json')))
