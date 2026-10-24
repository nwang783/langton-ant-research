from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'critical_mixed_LL_roots_require_distinct_LEFT_lane_exits.md';assert sha(F)=='9941a4b157ea1465b4b7a353e3acc3c989184f62b70e0a5ca4f35c6d633c5d30'
M=json.loads((R/'audits/check_mixed_second_lane_independent.json').read_text());L=json.loads((R/'audits/check_mixed_LL_gate_independent.json').read_text());J=json.loads((D/'critical_LL_LEFT_exit_template_control.json').read_text())
left=[]
for row in M['all10_flow3_scatterings']:
 s=row['second_lane'];nodes=row['complete_nodes']
 for e in s['route'][:-1]if s['kind']=='EXIT'else s['route']:
  assert e['rank']in(2,3)
  if nodes[e['vertex']]['turn']=='L':assert e['rank']==3
 if s['kind']=='EXIT':
  q=nodes[s['at_vertex']]
  if s['side']=='LEFT':assert q['turn']=='R';left.append(row)
  else:assert q['turn']=='L'and s['at_rank']==2
assert left==J['eligible_long_flow3_LEFT_exits']and len(left)==5
assert [(x['flow3_turn_word'],x['internal_RIGHT_histories'])for x in left]==[('RLRR',['EEEW']),('RLRR',['EWEE']),('RRLR',['EWEE']),('RRLRR',['EWEE','EEEW']),('RRLRR',['EWEE','EWEE'])]
flat=[]
for row in M['flow2']:
 s=row['second_lane']
 if s['kind']=='EXIT'and s['side']=='LEFT':assert row['turn']=='R';flat.append((row['history'],s['at_rank']))
 elif s['kind']=='EXIT':assert row['turn']=='L'and s['at_rank']==2
 else:assert row['history']=='WWEE'and s['route'][0]['rank']==3
assert flat==[('EEWW',1),('EWWE',3)]
assert all(e['rank']==2 for e in M['flow4']['second_lane']['route'])
out=dict(status='PASS dependent critical mixed LL first-hit LEFT-exit injection',proof=sha(F),author_control=sha(D/'critical_LL_LEFT_exit_template_control.json'),dependencies={str(p.relative_to(R)):sha(p)for p in[R/'audits/check_mixed_second_lane_independent.json',R/'audits/check_mixed_LL_gate_independent.json',R/'audits/check_mixed_first_track_pipeline_independent.json']},eligible5=left,flat_RIGHT_exits=flat,analytic_review=[
'Each first-LL O/U root starts actual L1->secondLEFT V.L3->followingRIGHT second incoming rank. Both old-flat and zero-chord mixed cases retained. Signed actual second-lane table then selects uninterrupted sigma edges, not repaired jumps.',
'All THROUGH reads are R2 or L3 and remain geometric LEFT; none is any other LEFT-root L1. At a first non-boundary departure, LEFT exits are precisely the2 flatRIGHT event types and5 long3 sign templates; RIGHT exits are a crossing R2.',
'The critical same-PHYSICAL return from uL1 must end at uR2. A forward lifted embedded gamma segment cannot reach u again. A wrong-crossing RIGHT exit contradicts this, and a complete boundary lap reaches u-d with time shift-P despite positive actual length. Thus an eligible LEFT exit occurs before a complete lap.',
'Nonlocal physical chords are stopped at the first non-boundary departure. They may land on gamma elsewhere or use arbitrary old stock afterward, but cannot change the literal prefix or invalidate the first-hit map.',
'On the full P-event permutation, two root classes sharing the same exit class force one root start inside the other selected prefix by unique backward tracing. These prefixes have no LL-root L1 except their own start, including translated representatives, so the map is injective. One prescribed entry/scattering exit per long3 macro gives the stated macro/event reservation.',
'Only a reservation of distinct actual LEFT-exit junction event classes under completeWHITEcap4,criticalGLOBALM and no-one-use is established. No output/root fuel, exterior completion, period bound or global one-use/capture conclusion.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
