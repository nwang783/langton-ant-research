"""End-to-end audit of the SAME frozen family and all its required invariants."""
from pathlib import Path
import json,hashlib
from check_producer_quotient_model_independent import ROOT,W,digest,relation,signed,check
mp=W/'dcv_producer_closed_family_manifest.json';manifest=json.loads(mp.read_text());hp=Path(manifest['family_file']);stage=Path(manifest['stage_family_file']);sp=Path(manifest['fixed_signed_file'])
assert digest(hp)==manifest['family_sha256']=='c4585979213b8f6bdec63aee6daec119ab16226bce6a9d5401a3ae5968d994e4'
assert hp.read_bytes()==stage.read_bytes()
assert digest(sp)==manifest['fixed_signed_sha256']=='8da1a5e5fc5c1162c1938890c836602ffd7ea4fa8d91831d0510425bcc16368e'
H=relation(hp);S=relation(sp);assert S==signed and len(S)==102 and len(H)==198 and S<=H
assert not H&relation(W/'dcv_companion_observed19.tsv')
clauses=manifest['clauses'];assert len(clauses)==96 and len({tuple(r['tuple'])for r in clauses})==96 and {tuple(r['tuple'])for r in clauses}==H-S
tm=Path(manifest['snapshot_tools_manifest']);assert digest(tm)==manifest['snapshot_tools_manifest_sha256']
required=relation(W/'dcv_directional25_targets.tsv');assert len(required)==25 and required<=H and not required&S
assert {tuple(r)for r in manifest['directional25_covered']}==required and manifest['directional25_not_covered']==[]
results=[];totalstates=0;totalchecks=0
for r in clauses:
 for p,h in r['files'].items():assert digest(Path(p))==h,p
 p=Path(r['model']);J=json.loads(p.read_text());assert p.with_suffix('.bdd')==Path(r['invariant'])
 assert(J['source'],J['target'],*J['target_pose'],*J['protected_q'])==tuple(r['tuple'])
 assert J['format']=='guarded_xor_reset_producer_quotient_v1'
 assert Path(J['candidate_hypothesis_file']).resolve()==stage.resolve() and J['candidate_hypothesis_sha256']==digest(hp) and {tuple(z)for z in J['candidate_hypotheses']}==H
 assert Path(J['extra_guard_file']).resolve()==sp.resolve() and J['extra_guard_sha256']==digest(sp)
 assert r['variables']==J['n'] and r['watched_cells']==[L['cell']for L in J['producer_label_classes']]
 out=check(p,True);assert 'invariant'in out;assert out['invariant']['invariant_states']==r['verified_states']
 totalstates+=out['invariant']['invariant_states'];totalchecks+=out['invariant']['checks'];results.append({'tuple':r['tuple'],'candidate_index':r['candidate_index'],'independent_result':out})
 report={'status':'PARTIAL_NOT_SIGNED','family_count':198,'already_signed_count':102,'new_obligations':96,'completed_obligations':len(results),'directional25_covered':25,'total_invariant_states':totalstates,'total_inclusion_checks':totalchecks,'family_sha256':digest(hp),'manifest_sha256':digest(mp),'clauses':results}
 (ROOT/'audits/closed_producer_family_independent.partial.json').write_text(json.dumps(report,indent=2)+'\n')
assert len(results)==96
old=json.loads((W/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers']
oldrows=[(r['source_packet'],r['target_packet'],*r['target_pose'],*r['source_output'])for r in old]
report['original69_covered_indices']=[i for i,r in enumerate(oldrows,1)if r in H]
report['original69_not_covered_indices']=[i for i,r in enumerate(oldrows,1)if r not in H]
report['status']='PASS complete simultaneous chronological-producer family; all25 directional obligations proved'
(ROOT/'audits/closed_producer_family_independent.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()if k!='clauses'}))
