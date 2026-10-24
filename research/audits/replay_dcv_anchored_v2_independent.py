#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,importlib.util,contextlib,io,subprocess,re
ROOT=Path(__file__).resolve().parents[1];W=ROOT/'word_stabilization';A=ROOT/'audits';D=W/'dcv_anchored_transfer_v2'
spec=importlib.util.spec_from_file_location('ownchecker',A/'check_protected_patch_model_independent.py');own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
manifest=json.loads((D/'manifest.json').read_text())
for rel,digest in manifest['files'].items():assert hashlib.sha256((W/rel).read_bytes()).hexdigest()==digest,rel
summary=json.loads((D/'summary.json').read_text());results=[];total=0
assert sorted(r['index'] for r in summary['results'])==list(range(1,70))
for row in summary['results']:
 path=W/(row['prefix']+'.json')
 with contextlib.redirect_stdout(io.StringIO()):own.main(path)
 model=json.loads((A/'protected_patch_replays'/path.with_suffix('.model_check.json').name).read_text())
 assert model['frozen_bad_list_index_zero_based']==row['index']-1
 if 'EXHAUSTED_NO_HIT' not in row['result']:continue
 dat=A/'protected_patch_replays'/path.with_suffix('.dat').name
 r=subprocess.run([str(A/'check_patch_reachability_independent'),str(dat)],check=True,capture_output=True,text=True)
 outcome=json.loads(r.stdout);expected=int(re.search(r'states (\d+)',row['result']).group(1));assert outcome['reachable_states']==expected
 (dat.with_suffix('.reachability.json')).write_text(json.dumps(outcome,indent=2)+'\n')
 total+=expected;results.append({'case_index_one_based':row['index'],'model':str(path.relative_to(ROOT)),**outcome})
 print('checked exclusion',row['index'],expected,flush=True)
assert [r['case_index_one_based'] for r in results]==summary['excluded']==manifest['excluded_case_indices']
out={'status':'PASS independent literal reconstruction of all 69 v2 graphs and complete closure of all 22 exclusion graphs','excluded_case_indices_one_based':summary['excluded'],'excluded':len(results),'remaining_unproved':69-len(results),'total_independently_exhausted_states':total,'source_manifest_sha256':hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),'results':results,'scope':'Each accepted tuple matches the frozen 69 list exactly. Other abstract witnesses are not physical realizations. No D/C/V finite-tail exclusion follows yet.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
