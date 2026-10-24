"""Six actual early-ancestor modes and common first-branch leaf profiles.
No new search; projects the complete signed72-row ancestor inventory.
"""
from pathlib import Path
from collections import Counter
import json
root=Path(__file__).parent
rows=json.loads((root/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows']
modes=Counter()
for r in rows:
 h=r['headings']; ancestor='S'if h['j']=='W'else'R';assert h['j']in['W','EEWE']
 lower='3'if h['x']=='EWW'else'4a'if h['r']=='WEW'else'4b'
 assert (h['x'],h['r'],h['q'],h['e'])=={'3':('EWW','WEEW','SSS','SNN'),'4a':('EWWW','WEW','SSS','SNNN'),'4b':('EWWW','WEWW','SSSN','SNNN')}[lower]
 modes[ancestor+lower]+=1
assert set(modes)=={'S3','S4a','S4b','R3','R4a','R4b'}and all(n==12 for n in modes.values())
weights=dict(S3=4,S4a=3,S4b=1,R3=3,R4a=4,R4b=2)
out=dict(scope=__doc__,row_count=len(rows),mode_counts=dict(modes),disjoint_odd_union_weights=weights,capacity='Nodd >= 4*nS3 + 3*nS4a + nS4b + 3*nR3 + 4*nR4a + 2*nR4b')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
