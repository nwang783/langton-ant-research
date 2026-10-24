"""Mandatory wording precision only; do not alter original frozen b224."""
from pathlib import Path
import importlib.util,json,hashlib
H=Path(__file__).resolve().parent;R=H.parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l)
s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o)
C=l.trace(o.WORDS['C']);x,y,h=C['pose'];exitK={(x+l.rot(q,h)[0],y+l.rot(q,h)[1])for q in l.K};rows=[]
for q in sorted(exitK):
 first=C['first'][q];last=C['last'][q];assert last[0]=='R'
 if q in l.K:assert first[0]=='L';why='Already in ENTRY CORE: an external CURRENT tag cannot be here at C ENTRY. This site does NOT require WHITE before C.'
 else:assert first[0]=='R';why='Outside ENTRY CORE: actual first-R requires WHITE, contradicting a held external CURRENT BLACK tag.'
 rows.append(dict(actual_exit_CORE_site=q,already_in_ENTRY_CORE=q in l.K,actual_first=first,first_owner=o.describe('C',first[1]),actual_final_R=last,external_CURRENT_capture_exclusion=why))
assert sum(r['already_in_ENTRY_CORE']for r in rows)==2 and len(rows)==5
j=dict(status='MANDATORY_WORDING_PRECISION_NO_NEW_EXCLUSION',original_manifest_sha256=hashlib.sha256((H/'manifest.json').read_bytes()).hexdigest(),original_files_unchanged=True,all5_actual_C_EXIT_CORE_R_sites_with_exact_ENTRY_distinction=rows,correction='Replace any original b224 phrase that all five C exitCORE R sites require before-WHITE: exactly THREE external sites have actual first-R/WHITE; TWO are already ENTRY-CORE first-L sites, unavailable to an external CURRENT tag at ENTRY. Together this proves no silent CURRENT absorption. Ordinary C still has no external true input. No new source/age or contact exclusion is inferred.',bound_independent_report_sha256='eb61d924d5633fac2b1c88318e1eb95cfc7f6315a8a7aabb24e000e131b8f50b')
(H/'C_CORE_wording.json').write_text(json.dumps(j,indent=2)+'\n')
