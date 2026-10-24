"""Finite boundary facts for the all-length at-most-four center overlap lemma."""
from pathlib import Path
import json
from verify_macro_word import check,D
out={}
for w in ['VB','VVVQU','VVUBU']:
 try:check(w)
 except AssertionError as e:out[w]=e.args[0]
 else:raise AssertionError(('boundary unexpectedly feasible',w))
# Coarse endpoint displacements in the initial north-facing center frame.
center0=(-1,1)
for a,want in [('Q',(-6,-10)),('B',(-4,-12))]:
 x,y,h=D[a]['end_pose'];assert h==2
 center1=(2*x+1,2*y-1)
 assert(center1[0]-center0[0],center1[1]-center0[1])==want
Path(__file__).with_name('uv_run_overlap_boundary_certificate.json').write_text(json.dumps(out,indent=2))
print('PASS: VB, VVVQU, VVUBU exact conflicts; Q/B coarse endpoint identities')
