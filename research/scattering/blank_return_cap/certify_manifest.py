import json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text())
for name,digest in M['files'].items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,name
B=json.loads((P/'bridge.json').read_text());R=json.loads((P/'r28_complete_certificate.json').read_text());V=json.loads((P/'r28_provenance.json').read_text())
assert [r['phase'] for r in B['rows'] if r['permanent_transfer']]==[13,14,27,60,70,75,89]
assert R['capture_time']==[312,208,163801] and R['capture_pose']==[[[-2,0,-155],[-2,0,-226]],3] and R['tail_phase']==99
assert V['black_lifetime_age']==[208,208,99456]
assert V['source_certificate_sha256']==hashlib.sha256((P/'r28_complete_certificate.json').read_bytes()).hexdigest()
print(json.dumps(dict(status='five-cap and exact nested-return manifest passes',manifest_sha256=hashlib.sha256((P/'manifest.json').read_bytes()).hexdigest())))
