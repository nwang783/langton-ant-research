#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,importlib.util,contextlib,io,re,collections
ROOT=Path(__file__).resolve().parents[1];W=ROOT/'word_stabilization';A=ROOT/'audits';D=W/'dcv_anchored_transfer_min'
spec=importlib.util.spec_from_file_location('ownchecker',A/'check_protected_patch_model_independent.py');own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
manifest=json.loads((D/'manifest.json').read_text())
for rel,digest in manifest['files'].items():assert hashlib.sha256((W/rel).read_bytes()).hexdigest()==digest,rel
summary=json.loads((D/'summary.json').read_text());results=[];total=0
for row in summary['results']:
 path=W/(row['prefix']+'.json')
 with contextlib.redirect_stdout(io.StringIO()):own.main(path)
 dat=A/'protected_patch_replays'/path.with_suffix('.dat').name
 model=json.loads(dat.with_suffix('.model_check.json').read_text());assert model['frozen_bad_list_index_zero_based']==row['index']-1
 v=iter(map(int,dat.read_text().split()));n,np,nt,nr=[next(v) for _ in range(4)];sp,sk,sv=[next(v) for _ in range(3)];edges=collections.defaultdict(list)
 for _ in range(nt):
  p,to,k,c,x,g,a=[next(v) for _ in range(7)];edges[p].append((to,k,c,x,g))
 reentry=[next(v) for _ in range(nr)];assert not list(v)
 initial={(sp,c) for c in range(1<<n) if c&sk==sv};seen=set(initial);todo=collections.deque(initial);checks=0
 while todo:
  p,c=todo.popleft();successors=[]
  if p==np-1:successors=[(r,c) for r in reentry]
  else:
   for to,k,vv,x,g in edges[p]:
    checks+=1
    if c&k!=vv:continue
    assert not g,(row['index'],p,c)
    successors.append((to,c^x))
  for state in successors:
   if state not in seen:seen.add(state);todo.append(state)
 expected=int(re.search(r'states (\d+)',row['final_result']).group(1));assert len(seen)==expected
 result={'case_index_one_based':row['index'],'patch_cells':n,'reachable_states':len(seen),'packet_checks':checks};results.append(result);total+=len(seen)
 dat.with_suffix('.python_reachability.json').write_text(json.dumps(result,indent=2)+'\n')
old=json.loads((A/'replay_dcv_anchored_v2_independent.json').read_text())['excluded_case_indices_one_based'];assert [r['case_index_one_based'] for r in results]==old
assert total==summary['total_final_reached_states']==manifest['total_reached_states']==40041
out={'status':'PASS independent literal reconstruction and separate Python explicit closure','cases':len(results),'total_reached_states':total,'patch_cell_range':[min(r['patch_cells'] for r in results),max(r['patch_cells'] for r in results)],'source_manifest_sha256':hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),'results':results,'scope':'Smaller replacement certificates for the same signed22 cases; no new transfer exclusions.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
