from pathlib import Path
import hashlib,json
R=Path('/workspace/shared/langton')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
entries=[]
for m,b in [
('first_principles_2026-10-21/SHA256SUMS.txt','first_principles_2026-10-21'),
('continuation_2026-10-21/ant_continuation/MANIFEST.json','continuation_2026-10-21'),
('continuation_2026-10-22/ant_continuation2/MANIFEST.json','continuation_2026-10-22'),
('recovered_bundle/ant_global/manifest_sha256.json','recovered_bundle/ant_global')]:
 p=R/m
 if p.suffix=='.txt':pairs=[(s.split(maxsplit=1)[1].lstrip('*'),s.split()[0]) for s in p.read_text().splitlines() if s.strip()]
 else:pairs=[(k,v['sha256'] if isinstance(v,dict) else v) for k,v in json.loads(p.read_text())['files'].items()]
 bad=[k for k,h in pairs if not (R/b/k).is_file() or sha(R/b/k)!=h]
 assert not bad,(m,bad)
 entries.append(dict(manifest=m,manifest_sha256=sha(p),verified=len(pairs),failed=bad))
assert sum(x['verified'] for x in entries)==541
files=['RECOVERY_INDEX.md','sources/handoff_2026-10-21.txt','sources/continuation_2026-10-22.md','recovered_bundle/ant_global/README.txt','recovered_bundle/ant_global/sources/source_status.md','sources/kehao95-core/wake_synthesis/proof/periodic-growth-closure.md','sources/kehao95-core/wake_synthesis/proof/mixed-wake-interleaving.md','sources/kehao95-core/wake_synthesis/proof/thin-wake.md']
report=dict(status='RECONCILED: historical reported computation, not independently re-certified in recovered package; unchanged from 22 October audit.',scope='All periods, full drift (2,-2), diagonal width 10, wake growth 8. This is not the general growth >=8 theorem or growth12 thin-wake rigidity.',integrity=entries,total=541,sources={f:sha(R/f) for f in files},old_workspace_exists=Path('/workspace/scratch/e9806c664975/ant_research/phase2').exists(),foundations_files=sorted(p.name for p in (R/'recovered_bundle/ant_global/foundations').iterdir()),historical_counts={'total':55812,'arithmetic_local':55348,'visit_count':74,'chronology':390,'exact_searches':352,'equivalence':1,'local_contradictions':3,'earlier_subfamily':34},not_claimed=['counterexample','refutation of historical theorem','fresh exhaustive search','recovery of missing original raw runs','new downgrade of an independently signed result'])
assert 55348+74+390==55812 and 352+1+3+34==390
out=R/'audits/check_width10_growth8_evidence_status.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('REPORT_SHA256',sha(out))
