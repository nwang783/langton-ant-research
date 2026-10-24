"""Derive candidate post-core exceptional parity from existing one-bit records.
This is a reduction diagnostic, not a new complete-field multi-impact proof.
"""
import json,sys
from pathlib import Path
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import plan,W,canonical_source
SRC=Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/one_bit_certificate_restored.json')
D=json.loads(SRC.read_text());FR=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
rows=[]
for phase in FR:
 age=D['thresholds'][phase];R=next(x for x in D['cases'] if x['n']==age and x['r']==phase)
 _,impact,_=canonical_source(age,phase)
 core=(-15-impact[0],29-impact[1]);ep=(-15-R['position'][0],29-R['position'][1]);eh=(R['heading']+2)%4
 tw=W[R['phase']:]+W[:R['phase']];skip=(72-R['phase'])%104;exc=plan(tw[:skip],ep,eh)[2]
 row=dict(phase=phase,core_ray_base=core,source_age=age,recovery_updates=R['steps'],outgoing_drift=[-v for v in R['tail']['drift']],outgoing_exceptional_ray_base=exc,outgoing_exceptional_x_parity=exc[0]%2)
 rows.append(row);print(json.dumps(row))
Path(__file__).with_name('parity_diagnostic.json').write_text(json.dumps(dict(status='diagnostic from existing single-bit certificates; no complete-parent theorem',rows=rows),indent=2)+'\n')
