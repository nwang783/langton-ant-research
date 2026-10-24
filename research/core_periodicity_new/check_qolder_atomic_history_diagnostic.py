"""Cross-check an already signed free-relocation control under the new history.
This NEVER repairs or hides the spatial discontinuities.
"""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
RP=W/'qolder_low_record_relocation_frozen_20261023_1219/02_qolder_low_record_relocation.json'
if not RP.exists():
 RP=next(p for p in (W/'qolder_low_record_relocation_frozen_20261023_1219').glob('*.json')if p.name!='manifest.json')
AP=W/'atomic_core_record_interface_frozen_20261023_1359/02_atomic_core_record_interface.json'
J=json.loads(RP.read_text());A=json.loads(AP.read_text());T={(r['packet'],r['global_phase']):r['enlarged_peak']for r in A['rows']}
rows=[];broken=[]
for i,r in enumerate(J['schedule']):
 x,y,h=r['head'];peak=2*(y-x)+T[r['packet'],(h+1)%4]
 rows.append(dict(index=i,packet=r['packet'],head=r['head'],old_entering_core=r['record'][0],old_created=r['record'][1],atomic_enlarged_created=peak))
 if i:
  if J['schedule'][i-1]['raw_exit']!=r['head']:broken.append(i-1)
assert len(rows)==797 and len(broken)==796
assert max(r['atomic_enlarged_created']for r in rows[:-1])==26
assert all(max(r['old_entering_core'],r['atomic_enlarged_created'])<30 for r in rows[:-1])
assert rows[-1]['atomic_enlarged_created']==30
O=dict(status='AUTHOR_EXISTING_RELOCATION_CONTROL_ATOMIC_HISTORY_PASS',scope='Cross-check only of a signed LOCAL free-core-relocation limitation. ALL796 positional junctions remain broken. Not a physical word, unfunded physical U1 event, infinite renewal or confinement counterexample.',rows=rows,nonphysical_junction_indices=broken,prior_atomic_peak_max=26,goal_atomic_peak=30,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[RP,AP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/qolder_atomic_history_diagnostic.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(dict(packets=len(rows),broken_junctions=len(broken),prior_atomic_peak=26,goal_atomic_peak=30))
