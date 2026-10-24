from pathlib import Path
import json,hashlib,time
P=Path(__file__).resolve().parent;O=P/'dcv_mutual_family'
while True:
 J=json.loads((O/'summary.json').read_text())
 if J.get('stable'):break
 if len(J['stages'])>=20 and J['stages'][-1].get('supported_count')is not None:raise SystemExit('No stable family found within discovery stages; nothing frozen.')
 time.sleep(5)
s=J['stages'][-1];d=O/f"stage{s['stage']:02}";h=d/'hypotheses.tsv';H={tuple(map(int,l.split()))for l in h.read_text().splitlines()};Sfile=P/'dcv_anchored_signed41.tsv';S={tuple(map(int,l.split()))for l in Sfile.read_text().splitlines()};assert S<=H;dest=P/'dcv_companion_closed_family.tsv';dest.write_bytes(h.read_bytes());orig=json.loads((P/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers'];idx={(r['source_packet'],r['target_packet'],*r['target_pose'],*r['source_output']):i for i,r in enumerate(orig,1)}
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
manifest={'status':'PROVISIONAL CLOSED MUTUAL FAMILY: independent global family, literal-model and invariant audit required','family_file':str(dest),'family_sha256':sha(dest),'known_signed_file':str(Sfile),'known_signed_sha256':sha(Sfile),'family_count':len(H),'known_signed_count':len(S),'new_count':len(H-S),'stage':s['stage'],'protocol':'dcv_companion_mutual_induction.md','new_clauses':[]}
for r in s['results']:
 row=tuple(r['tuple'])
 if row in S:continue
 assert row in H and r['status']=='EXHAUSTED_NO_HIT';i=r['candidate_index'];base=O/f'base{i:03}.json';model=d/f'candidate{i:03}.json';graph=d/f'candidate{i:03}.dat';inv=d/f'candidate{i:03}.bdd';ver=d/f'candidate{i:03}.verified.json';m=json.loads(model.read_text());assert m['candidate_hypothesis_sha256']==sha(dest)
 rec={'tuple':row,'candidate_index':i,'original_bad_index':idx.get(row),'state_count':json.loads(ver.read_text())['states'],'files':{str(f):sha(f)for f in[base,model,graph,inv,ver]}};manifest['new_clauses'].append(rec)
assert{tuple(r['tuple'])for r in manifest['new_clauses']}==H-S;manifest['new_original_bad_indices']=[r['original_bad_index']for r in manifest['new_clauses']if r['original_bad_index']is not None];manifest['scripts']={str(f):sha(f)for f in[P/'run_dcv_mutual_family.py',P/'dcv_companion_mutual_induction.md',P.parent/'core_periodicity_new/add_protected_source_flags.py',P.parent/'core_periodicity_new/generate_protected_transfer_patch.py']};(P/'dcv_companion_closed_family_manifest.json').write_text(json.dumps(manifest,indent=2));print({k:v for k,v in manifest.items()if k not in['new_clauses','scripts']})
