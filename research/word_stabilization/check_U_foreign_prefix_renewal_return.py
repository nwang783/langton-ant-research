"""One dependency-bound causal retirement / exact vertex-return assembly."""
from pathlib import Path
import json, hashlib, importlib.util
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent;W=ROOT/'core_periodicity_new'
sp=importlib.util.spec_from_file_location('literal',HERE/'check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
C=G[1]['word'][len(G[0]['word']):];tr=lit.trace(C);assert tr['feasible']
goal=(3,3,0);lastC=(2,3,1);east=(2,1)
local=lit.rot((east[0]-lastC[0],east[1]-lastC[1]),-lastC[2])
assert local==(2,0) and tr['first'][local]==('R',8)
d=lit.rot(tr['pose'][:2],lastC[2])
assert (lastC[0]+d[0],lastC[1]+d[1],(lastC[2]+tr['pose'][2])%4)==goal
breaker=(3,-1,0);u=lit.trace(G[7]['word']);assert u['feasible']
assert (breaker[0]+u['pose'][0],breaker[1]+u['pose'][1],u['pose'][2])==goal
assert tr['pose'][2]==3
def center(p):
 r=lit.rot((-1,-1),p[2]);return 2*p[0]+r[0],2*p[1]+r[1]
assert center(goal)==(5,5)
deps=[GP,HERE/'check_foreign_return_interfaces.py',
 HERE/'U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',
 ROOT/'seven_word_spatial_return_2026-10-23/foreign_first_contact_manifest.json',
 W/'causal_cycle_renewal_20261023_1841/manifest.json',
 W/'U_renewal_exact_clock_frozen_20261023_1902/manifest.json',
 W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',
 W/'atomic_common_4C_frozen_20261023_1344/manifest.json']
out=dict(status='AUTHOR_DEPENDENCY_BOUND_EXACT_RETURN_ASSEMBLY_PENDING_INDEPENDENT_REPLAY',
 scope='Genuine U-family creator followed by retained-eight packets until FIRST foreign, U-source/common-F-prefix first contact. No Q/B tail or D/C/V source claim.',
 excluded=dict(foreign='F',pose=goal,source_age=8,preceding_C=True,
   preceding_C_pose=lastC,preceding_C_entry_clock=7,
   original_east_identity=east,foreign_predecessor_local=local,first_required_read=['R',8],
   required_earlier_right_breaker=breaker,breaker_full_entry_clock=4,
   breaker_U_base_exit_pose=goal,breaker_U_base_exit_clock=4,
   final_last_C_exit_pose=goal,final_last_C_exit_clock=8,
   repeated_corrected_center_doubled=center(goal),
   contradiction='Strictly earlier nonadjacent vertex of the actual uninterrupted eight atomic path; alternatively exact four-C marked-pose nonreturn.'),
 remaining=[dict(foreign=f,pose=(2,4,0),source_age=8,preceding_C=True) for f in ('F','Q')],
 dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps})
(HERE/'U_foreign_prefix_renewal_return.json').write_text(json.dumps(out,indent=2)+'\n')
print('C(2,3,E) before-white old east(2,1) => renewal U(3,-1,N) at4 => repeated exit pose(3,3,N) at8.')
