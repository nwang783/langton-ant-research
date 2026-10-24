"""Extract exact active-component sizes, not merely whole frontier sizes."""
from active_flight import *
from pathlib import Path
import hashlib,json
P=Path(__file__).parent;SRC=P.parent/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json';SIGNED=P.parent/'standard_unread_cap_2026-10-23/SIGNED_MANIFEST.json'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()=='6c3294eede67916be8c7171e73683cf5009c9fe3846ed0bfb61580181186413a'
J=json.loads(SRC.read_text());rows=[]
for r in J['phases']:
 p,h=r['pose'];w=tuple(r['w_cursor']);assert sector(p,h)==0 and cursor(p,h)==w
 B=set(map(tuple,r['black_frontier']));C=comp(B,0,w)
 rows.append({'phase':r['phase'],'pose':r['pose'],'w_cursor':w,'frontier_mass':len(B),'complete_active_w_mass':len(C),'complete_active_component':sorted(C)})
peak=max(r['complete_active_w_mass']for r in rows);witness=[r['phase']for r in rows if r['complete_active_w_mass']==peak];assert peak==42 and witness==[64];assert rows[64]['frontier_mass']==42
out={'status':'AUTHOR_EXACT_EXTRACT_FROM_SIGNED_COMPLETE_FRONTIER_PENDING_INDEPENDENT_PEAK_CHECK','source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'signed_manifest_sha256':hashlib.sha256(SIGNED.read_bytes()).hexdigest(),'maximum_complete_active_w_mass':peak,'maximizing_phases':witness,'mass_sequence':[r['complete_active_w_mass']for r in rows],'phases':rows,'scope':'Exact every-period active peak after the signed finite-archive clearance threshold in an already-standard104 finite-board future; not attraction, not a pre-clearance bound.'};(P/'exact_standard_active_peak.json').write_text(json.dumps(out,indent=2)+'\n');print('exact peak',peak,'phases',witness)
