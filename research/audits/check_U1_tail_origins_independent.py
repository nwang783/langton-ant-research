from pathlib import Path
from collections import Counter
import hashlib,json
ROOT=Path('/workspace/shared/langton');SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new';B=D/'U1_U_tail_origins_frozen_20261023_1945';m=json.loads((B/'manifest.json').read_text())
for z in m['files']:assert hashlib.sha256((B/z['file']).read_bytes()).hexdigest()==z['sha256']
for p,s in m['dependencies'].items():assert hashlib.sha256((D/p).read_bytes()).hexdigest()==s
old=json.loads((SELF.parent/'check_U1_U_origins_diagnostic_independent.json').read_text());rows=[r for r in old['all_rows']if r['reason']=='necessary_origin_template_not_attainment'];assert len(rows)==36
q=[r for r in rows if r['output']==[-1,2]];arm=[r for r in rows if r['output']==[1,2]];left=[r for r in rows if r not in q+arm];assert len(q)==6 and len(arm)==1 and len(left)==29
assert Counter(r['source']for r in left)=={8:11,9:18}
slots={8:{(2,4),(2,5),(1,6)},9:{(2,4),(2,5),(1,6),(-2,6),(-1,7),(0,7)}}
assert all(tuple(r['output'])in slots[r['source']]for r in left)
atomic=[r for r in left if r['survives_atomic']];assert len(atomic)==23 and Counter(r['source']for r in atomic)=={8:8,9:15}
ref=json.loads((B/'02_U1_U_tail_origins.json').read_text())['results'];key=lambda r:(r['source'],tuple(r['output']),tuple(r['input']),tuple(r['pose']))
for name,lst in [('original_U1_necessary_templates',left),('enlarged_history_necessary_templates',atomic)]:
 if name not in ref:continue
 assert{key(r)for r in lst}=={(r['source'],tuple(r['source_output']),tuple(r['goal_input']),tuple(r['source_pose']))for r in ref[name]['necessary_templates']}
out=dict(status='PASS original U1 U-family tail-only origin assembly',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),original_count=29,original_type_counts=dict(Counter(r['source']for r in left)),enlarged_count=23,enlarged_type_counts=dict(Counter(r['source']for r in atomic)),removed_q=q,removed_arm=arm,remaining=left,scope='Individual necessary original strict unfunded U1 origins only; no plain U origin. UC/UCC C-tail roles remain possible but not jointly attained. No funding coverage increase, component separation, U bound or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['original_type_counts'],out['enlarged_type_counts'])
