from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[1];P=R/'scattering/return_ne_frontier'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((P/'manifest.json').read_text());assert all(sha(P/f)==h for f,h in manifest['files'].items())
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,plan
T=json.loads((R/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json').read_text());assert len(T['segments'][0]['word'])==9977 and len(T['segments'][2]['word'])==51118
assert 9977+104*8+51118==61927
reads=plan(W,(6,-43),1)[0];assert (min(x-y for x,y in reads),max(x-y for x,y in reads))==(42,52)
expected={28:(69617,[[37,-6],3],32),60:(62729,[[-13,-76],1],0),61:(92513,[[7,-94],1],0),70:(68063,[[-12,-77],1],0),75:(113611,[[46,1],1],0)}
b=json.loads((P/'bridge.json').read_text())
for row in b['rows']:
 t,p,ph=expected[row['phase']];assert row['capture_time_n_constant']==[208,t] and row['capture_pose']==p and row['capture_phase']==ph and row['drift']==[2,2]
 assert max(row['discarded_component_z_upper'].values())<-250
out={'status':'return-NE 14-class package independent analytic review and fresh exact replays pass','manifest_sha256':sha(P/'manifest.json'),'additional_bindings':'Full incoming NE u range [42,52], inherited 51118 recovery length, derived 61927 time constant, and all five displayed capture times/poses/phases checked independently.','scope':'Five complete two-cell all-age captures and fourteen fixed-core mass-five recurrence exclusions. The separate opposite package and six unfinished classes are not included.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
