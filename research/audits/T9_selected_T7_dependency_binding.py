from pathlib import Path
import json,hashlib
S=Path(__file__);D=S.parents[1]/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();M=D/'T_PORT9_SELECTED_T7_DEPENDENCY_ADDENDUM.json';assert sha(M)=='2499db3d17cfb135413b43830a8675d28377223bfaeecbbd16bf662e732e11ed';j=json.loads(M.read_text())
for f,h in j['files'].items():assert sha(D/f)==h
T7=json.loads((D/'../audits/check_T_port7_absorber_independent.json').read_text());assert T7['manifest']=='0e8dbf82450a2109fc466a200dab7ec181603179f2397a979d8889cb532abaed'and T7['provenance_addendum']=='cae3dfd6e7e36b2a86f736b49cf3af53adf460442abec02d08c626c59dd52506'and T7['alternate_branch_proof_status']=='NOT REVIEWED OR SIGNED'
o={'status':'PASS mandatory selected-T7 provenance for the exact T9 one-extra cover','addendum':sha(M),'script':sha(S),'bindings':j['files'],'scope':'T9 mathematical PASS262ab3ac is bound to independently signed T7 V1_0e8dbf82 with reconciliationcae3dfd6 and durable audit4a0857db. Alternate current-path36a1328e proof is not signed or imported. No mathematical scope expansion.'};S.with_suffix('.json').write_text(json.dumps(o,indent=2)+'\n');print(sha(S.with_suffix('.json')))
