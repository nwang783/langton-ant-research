from pathlib import Path
import hashlib,json
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=D/'passive_packet_cannot_exit_through_another_passive_singleton.md';assert sha(proof).startswith('706a916f');C=D/'check_passive_packet_exit_ordinal_core.json';assert sha(C).startswith('f2554705')and sha(D/'check_passive_packet_exit_ordinal_core.py').startswith('6794662a')
V={'N':1j,'E':1,'S':-1j,'W':-1};turn=lambda d,r:d*(-1j if r%2==0 else 1j);out=lambda w:[turn(V[a],i)for i,a in enumerate(w)];ports=lambda w,d:[i for i,u in enumerate(out(w))if u==d];inc=lambda w,d:[i for i,a in enumerate(w)if V[a]==d]
assert ports('NNSS',-1)==[1,2]and inc('EWWE',-1)==[1,2]
assert ports('EWWE',-1j)==[0,1]and inc('NNSS',-1j)==[2,3]
assert ports('NNSS',1)==[0,3]
rows=[]
for w in('EEWW','EWWE'):
 er=inc(w,1)[1];nr=ports(w,1j)[1];assert er<=nr;rows.append(dict(C=w,second_E_rank=er,second_N_rank=nr,forced_second_E_minus_second_N=4))
# Entire RIGHT in-axis E cap-four domain with selectedout>=2 and N-output2.
words=[]
from itertools import product
for n in range(1,5):
 for s in product('EW',repeat=n-1):
  w='E'+''.join(s)
  if len(inc(w,1))==2 and len(ports(w,-1j))>=2 and len(ports(w,1j))==2:words.append(w)
assert words==['EEWW','EWWE']
files=['check_passive_LL_flat_cap_independent.json','check_LL_RR_matching_independent.json','check_mixed_LL_gate_independent.json','check_mixed_macro_backbone_independent.json'];deps={}
for f in files:
 p=S.with_name(f)
 assert p.exists()
 j=json.loads(p.read_text());assert j['status'].startswith('PASS');deps[f]=sha(p)
assert len(deps)==4
O={'status':'PASS exact passive-packet no-V exit gate in signed main boundary scope','proof':sha(proof),'certificate':sha(C),'script':sha(S),'signed_dependencies':deps,'ordinal_cases':rows,'analytic_review':['The unique already signed CYCLIC flat-passive inventory gives A=EWWE,R=NNSS and actual firstW edgeR.L1->A.L1. Actual A south ports0,1 feed the hypothesized passiveE S arrivals2,3, giving A.L1->E.L3, not the previously corrected wrongN ordinal.','If nextC wereLEFT, secondLEFT gate makes passiveVV. The complete mixedLL table with precedingflatA has flat followingend, so the mandatory FLAT-ended passivecap theorem applies and requires a RIGHT predecessor forA. Its actual precedingZ isLEFT, contradiction. High-high passiveVV is not used or erased.','Thus C isRIGHT. Complete capfour in-axisE histories with exactlytwo Einputs supplied by the completeE cell, two northoutputs and at leasttwo selectedsouthoutputs are exactlyEEWW/EWWE. The high targetEEEE has four Einputs and is explicitly rejected by this exact E2 count, not a claimed one-use property. Every source/sink alternative is excluded by physical counts or nooneuse, not an arbitrary chosenmode.','Exact secondE edgeE.L3->C and secondN edgeC->R.L1->A.L1 force CsecondE=A.L1+2 and CsecondN=A.L1-2. Both completeflat histories require secondE<=secondN, impossible even with arbitrary otherclockdelays or quotientvoltages; all four equalities are physical local lifts.','The packetendpointY cannot go toV, so it exits by RR, genuineLL, or singletonO. Saturated matching makes anRR atY the startof anotherpassiveP, not genuineX-start. Highgap requires passiveV, hence directP->H and P-V->P are excluded. ArbitraryPstrips, actualO exits and all olderstock/exterior completion remain open.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
