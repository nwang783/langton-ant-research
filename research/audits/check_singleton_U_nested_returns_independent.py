from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');P=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=P/'critical_global_max_singleton_U_resets_force_nested_returns.md';assert sha(proof)=='ee51c399c689937786a7067ddcff0097f60da5da4f0d3af736c8da7d89b93a7c'
J=json.loads((P/'singleton_U_nested_return_ordinal_control.json').read_text());S=json.loads((P/'flat_flow2_symbolic_row_with_odd_left.json').read_text());openrows=[r for r in S['rows']if r['open_completions']]
keys=['Bprev','A','B','Anext','Bnext'];words=[tuple(r[k]for k in keys)for r in openrows];assert len(words)==8
assert all(w[3]=='X'and w[4]in['O','U']for w in words if w[2]=='U')
second=[r for r in openrows if r['Bprev']=='U'and r['B']in['O','U']];assert len(second)==4
V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()};out=lambda w:[I[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)]
pos={'u':-1j,'a':0j,'v':1+0j,'d':1-1j};iv={p:k for k,p in pos.items()}
for row in J['rows']:
 r=next(r for r in second if[r[k]for k in keys]==row['primary']);helper='NNS'if r['B']=='O'else'NNSS';assert row['helper']==helper and len(r['open_completions'])==row['open_completions']and all(c['D0']==helper for c in r['open_completions'])
 hs={'u':'WEEW','a':'NNSS','v':'WEE'if r['B']=='O'else'WEEW','d':helper};succ={}
 for name,w in hs.items():
  for hh in V:
   z=iv.get(pos[name]+V[hh])
   if z is None:continue
   ss=[i for i,h in enumerate(out(w))if h==hh];tt=[i for i,h in enumerate(hs[z])if h==hh];assert len(ss)==len(tt)
   for s,t in zip(ss,tt):succ[name,s]=(z,t)
 for a,r,b,s in row['actual_edges']:assert succ[a,r]==(b,s)
 assert row['actual_edges']==[['u',0,'a',0],['a',0,'v',1],['v',2,'d',2],['d',2,'u',3]]
# Mixed LL escape is checked from full signed RLLR inventory, not homogeneous continuation.
LL=json.loads((P/'check_flow2_LL_reset_square.json').read_text())
for row in LL['necessary_open_rows']:
 if row['histories']['Y']in['EWW','EWWE']:
  assert row['histories']['B']=='SNNS' # half-turn to local precedingRIGHT NSSN=Y, neverNNSS=X
report={'status':'PASS critical global-max singleton U reset impossible by two-contact interval nesting','proof_sha256':sha(proof),'ordinal_control_sha256':sha(P/'singleton_U_nested_return_ordinal_control.json'),'script_sha256':sha(Path(__file__)),'four_second_window_profiles':[r['primary']for r in J['rows']],'analytic_checks':['First globalM staircase window forces singletonU followedRIGHTX,nextLEFT O/U. The next LEFT cannot startLL because exhaustive LLfirstreset inventory requires precedingRIGHTY; it cannot be LLsecond afterRIGHT. Thus second alternatingwindow genuinely exists, includingmixedcase.','All four signed second-window completions force helperNNS orNNSS; freshphysicalport-ordinal matching gives uR0->aR0->vL1 andvR2->dR2->uL3. OddhelperNNS isretained.','Actualsamecellgaps>=4 yield T1v=T0u+2<=T1u-2 andT2v=T3u-2>=T2u+2. Therefore v interval strictlycontainsu, contradicting signedcriticalpairwisedisjointphysicalLEFTreturns. Everytranslate covered; no globaltimebound or infinite descent.','Together signed728ad all-shortexclusion nowforces singletonO=WEE oddRLR root with actualsamecontactreturn>=8. LL-firstU fourLcleanup remainspossible, and unknownolderstock/longoddcompletion remainsopen.'],'not_claimed':['allflow2circlesexcluded','noncritical or nonglobalextension','newdisjointoutputpayment','fuel orattraction']}
p=R/'audits/singleton_U_nested_returns_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
