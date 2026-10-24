from pathlib import Path
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent
P=W/'chronology_dcuv/U1_U_origins_after_permanence.json';R=json.loads(P.read_text());out={}
for key in['original_U1_necessary_templates','enlarged_history_necessary_templates']:
 before=R[key];removed_q=[x for x in before if x['source_output']==[-1,2]];removed_t=[x for x in before if x['source_output']==[1,2]];remaining=[x for x in before if x not in removed_q+removed_t]
 assert len(removed_q)==6 and len(removed_t)==1
 assert all(x['source']in[8,9]for x in remaining)
 assert all(tuple(x['source_output'])in({(2,4),(2,5),(1,6)}if x['source']==8 else{(2,4),(2,5),(1,6),(-2,6),(-1,7),(0,7)})for x in remaining)
 out[key]=dict(before=len(before),recycled_q_removed=len(removed_q),arm_removed=len(removed_t),remaining_count=len(remaining),source_counts=dict(Counter(x['source']for x in remaining)),slot_counts=dict(Counter(x['goal_input_slot']for x in remaining)),necessary_templates=remaining)
assert out['original_U1_necessary_templates']['remaining_count']==29
assert out['enlarged_history_necessary_templates']['remaining_count']==23
D=[P]+[W/s/'manifest.json'for s in['U1_U_origins_diagnostic_frozen_20261023_1930','U_recycled_q_return_frozen_20261023_1939','U_arm_return_frozen_20261023_1943']]+[Path(__file__).resolve()]
T=dict(status='AUTHOR_DEPENDENCY_ASSEMBLY_PENDING_AUDIT',scope='Under the ORIGINAL strict unfunded U1 record premise, any input genuinely produced earlier by a U-family packet must be a C-tail output of UC/UCC; plain U cannot supply it. This removes7 of the36 signed individual-origin templates, leaving29 necessary templates, NOT attainment or joint feasibility. Under the separately enlarged-history premise23 remain. V1/U1 funding coverage remains11/13.',results=out,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U1_U_tail_origins.json').write_text(json.dumps(T,indent=2)+'\n');print(json.dumps({k:{a:b for a,b in v.items()if a!='necessary_templates'}for k,v in out.items()},indent=2))
