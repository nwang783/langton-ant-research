"""Replay the stopped worker's seven frozen exact all-parameter certificates.
This is a source audit plus fresh exact-engine replay, not a recurrence claim.
All generated outputs are kept in the audit directory, leaving source untouched.
"""
import hashlib, importlib.util, json, pathlib, time
ROOT=pathlib.Path('/workspace/shared/langton')
SRC=ROOT/'scattering/return_ne_frontier/adjacent'
OUT=ROOT/'audits/return_ne_adjacent_replay'
OUT.mkdir(exist_ok=True)
for f in SRC.iterdir():
    if f.name.startswith(('template_', 'r15_', 'r29_', 'r45_', 'r56_', 'r62_', 'r72_', 'cycle72_m')) and f.is_file():
        q=OUT/f.name
        if not q.exists(): q.symlink_to(f)
results=[]; started=time.time()
for name,r,cert in [('certify.py',r,f'certificate_r{r}.json') for r in [15,29,45,56,62,72]]+[('certify_cycle72.py',72,'certificate_cycle72.json')]:
    print('BEGIN',name,r,flush=True)
    before=json.loads((SRC/cert).read_text())
    spec=importlib.util.spec_from_file_location('frozen_ne_'+str(len(results)),SRC/name)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.HERE=OUT
    t=time.time();module.main(r)
    after=json.loads((OUT/cert).read_text())
    assert after==before,cert
    row=dict(file=cert,seconds=time.time()-t,source_sha256=hashlib.sha256((SRC/name).read_bytes()).hexdigest(),certificate_sha256=hashlib.sha256((SRC/cert).read_bytes()).hexdigest(),statistics=after['statistics'])
    results.append(row)
    (OUT/'replay_manifest.json').write_text(json.dumps(dict(status='running' if len(results)<7 else 'all seven matched',results=results,total_seconds=time.time()-started),indent=2)+'\n')
    print('MATCH',cert,row['seconds'],flush=True)
