#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,importlib.util,contextlib,io,subprocess,re
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'audits';C=ROOT/'core_periodicity_new'
spec=importlib.util.spec_from_file_location('ownchecker',A/'check_protected_patch_model_independent.py');own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
summary=json.loads((C/'protected_vc24_batch_summary.json').read_text());results=[];total=0;hashes={}
for row in summary:
 if 'EXHAUSTED_NO_HIT' not in row['status']:continue
 path=Path(row['prefix']+'.json')
 with contextlib.redirect_stdout(io.StringIO()):own.main(path)
 dat=A/'protected_patch_replays'/path.with_suffix('.dat').name
 model=json.loads(dat.with_suffix('.model_check.json').read_text());assert model['frozen_bad_list_index_zero_based']==row['index']-1
 r=subprocess.run([str(A/'check_patch_sparse_reachability_independent'),str(dat)],check=True,capture_output=True,text=True)
 outcome=json.loads(r.stdout);assert outcome['reachable_states']==int(re.search(r'states (\d+)',row['status']).group(1))
 dat.with_suffix('.reachability.json').write_text(json.dumps(outcome,indent=2)+'\n')
 total+=outcome['reachable_states'];results.append({'case_index_one_based':row['index'],**outcome})
 for p in (path,path.with_suffix('.dat')):hashes[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
 print('independent sparse checked',row['index'],outcome['reachable_states'],flush=True)
indices=[r['case_index_one_based'] for r in results];assert indices==list(range(45,57))+[69]
old=json.loads((A/'replay_dcv_anchored_v2_independent.json').read_text())['excluded_case_indices_one_based'];assert not set(indices)&set(old)
out={'status':'PASS independent literal model reconstruction and explicit-state closure, without using BDD results as premises','new_exclusions_one_based':indices,'new_exclusions':len(indices),'total_exclusions':len(old)+len(indices),'remaining_unproved':69-len(old)-len(indices),'total_explicitly_exhausted_states':total,'results':results,'source_hashes':hashes,'scope':'These are finite-state all-length transfer exclusions, not physical witnesses for remaining cases and not a DCV tail theorem.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['results','source_hashes']},indent=2))
