from pathlib import Path
import json,hashlib,runpy
S=Path(__file__);R=S.parents[1];D=R/'first_postforeign_V_first_contact_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
M=D/'portable_F_reserve_scope_lift_manifest.json';assert sha(M)=='15e279a79eec60032af6782cf8c2311406aae0ceaab029c7e1e498a514aa0650'
m=json.loads(M.read_text())
for name,h in {**m['files'],**m['dependencies']}.items():assert sha(D/name)==h
J=json.loads((D/'portable_F_reserve_scope_lift.json').read_text());old=json.loads((D/'first_V_contact.json').read_text());assert sha(D/'first_V_contact.json')==J['source_JSON_SHA256']
assert set(J['exact_unchanged_fields'])=={'SAME_F_tag_births','all64_coupled_F_two_tag_first_loss_roles','F_reserve_statement','all104_physical_first_R_repair_roles_for_F_hole','F_WHITE_hole_statement'}
for k,v in J['exact_unchanged_fields'].items():assert v==old[k]
# Fresh replay of the already independent literal role reconstruction, never author code.
runpy.run_path(str(S.with_name('check_first_postforeign_V_contact_independent.py')))
assert sha(S.with_name('check_first_postforeign_V_contact_independent.json'))==m['dependencies']['../audits/check_first_postforeign_V_contact_independent.json']
out=dict(status='PASS source-owner-independent F reserve at GLOBAL-first-contact ENTRY only',manifest=sha(M),script=sha(S),copied_fields=list(J['exact_unchanged_fields']),loss_roles=64,physical_hole_R_roles=104,analytic_review=[
'At every earlier completed ordinary cut, the globally first-contact prefix is simple and has the actual immediate next completed G7 RAW with M11. Thus signed25a supplies the SAME first-V r/A CURRENT, regardless of eventual old owner, target kind, coordinates or C clock.',
'Choose the first earlier CURRENT loss among both F outputs. The independent64-role reconstruction uses only the two held F outputs, guarded V pair, sector and earlier actual F/V contact. Simultaneous TRUE inputs are not color contradictions; here they would cause an earlier forbidden loss of the SAME guarded pair. Marker-owned capture counts at RAW EXIT even if physical death is in next RAW.',
'After source V L1, choose the earliest physical R repair at the hole. Its earlier local read cannot be L without a preceding repair, so it is a first local RAW read. All104 physical R placements include CORE writes. Their exclusions use only four held BLACK identities and no earlier F/V contact, not any eventual target window. A marker read lying inside the contact atom is not an earlier repair.',
'The stopped contact ENTRY is the last earlier simple cut. Therefore both F R46/R47 remain CURRENT and the V-deleted hole is physically WHITE there. No persistence during contact, owner-specific target exclusion, F-alone guard, firstpostD/C/U extension, tail simplicity or capture is asserted.' ])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
