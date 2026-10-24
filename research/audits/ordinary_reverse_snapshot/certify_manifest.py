"""Verify the frozen ordinary/reverse interface artifact set."""
import json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
M=json.loads((P/'manifest.json').read_text())
for name,digest in M['files'].items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,name
I=json.loads((P/'interfaces.json').read_text());phases=sorted(I['protected_phases']+I['unprotected_backward_phases'])
assert len(phases)==len(set(phases))==21
assert phases==[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,75,89]
assert len(I['blank_realizations'])==13 and len(I['adverse_history_controls'])==8
print(json.dumps(dict(status='manifest and exact channel partition pass',channels=21,protected=13,backward=8,manifest_sha256=hashlib.sha256((P/'manifest.json').read_bytes()).hexdigest())))
