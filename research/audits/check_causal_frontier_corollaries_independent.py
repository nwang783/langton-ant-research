from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
P=ROOT/'causal_archive_spatial_lifetime_2026-10-23/causal_frontier_corollaries.md';K={q for q,b in walk(mark)[2].items()if b};c=(-1-1j)/2;rows=[]
for s in(0,1,4,5,6,7,8,9):
 I={q for q,b in walk(raws[s]+mark)[2].items()if b}-K
 for i in sorted(I,key=xy):
  for h in range(4):
   z=rotation(c-i,h)-c;rows.append(dict(source=s,input=xy(i),h=h,offset=xy(z),norm=max(abs(z.real),abs(z.imag))))
assert len(rows)==92 and max(x['norm']for x in rows)==5
out=dict(status='PASS additive same-simple-factor spatial frontier corollaries',note_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),all_slot_rows=rows,entry_horizon='20R+211 with R containing ALL entry residual identities',sealing_scope='A current produced residual boundary frozen from full clock s through a full clock greater than s+294 is unretirable subsequently in the same simple factor. Actual outside dual cursor and genuine separating boundary required; no historical connector.',nonreturn='Cgap<=20*center Linfty displacement+111 for actual atomic subarcs; zero-C word length not bounded.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['note_sha256'])
