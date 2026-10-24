"""Exact local table supporting the separately reviewed cylinder-topology proof.
No finite test is represented as proving arbitrary-cylinder topology.
"""
from pathlib import Path
from itertools import product
import hashlib,json
R=Path(__file__).resolve().parents[1];rows=[]
# At an even vertex the two allowed incoming headings E,W correspond to the
# two clockwise corners. The common constant is immaterial.
for n in range(1,5):
 for incoming in product((0,1),repeat=n):
  rr=[sum(j%2==0 and h==a for j,h in enumerate(incoming))for a in(0,1)]
  ll=[sum(j%2==1 and h==a for j,h in enumerate(incoming))for a in(0,1)]
  assert sum(rr)<=2 and rr[incoming[0]]==max(rr)
  if rr[0]==rr[1]:assert n>=3
  shifted=[rr[0],rr[1],1-ll[0],1-ll[1]];mx=max(shifted)
  unique=shifted.count(mx)==1
  if unique:assert n>=3 and rr[0]!=rr[1] and shifted.index(mx)<2
  rows.append(dict(n=n,headings=incoming,R=rr,L=ll,first_R_at_max=True,unique_shifted_max=unique))
assert len(rows)==30
note=R/'periodic_classification_new/cap_four_first_read_stream_backbone.md'
out=dict(status='PASS complete local cap-four table; global functional-cycle and zero-turning arguments separately reviewed analytically',rows=rows,note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),scope='Complete initially-white cap-four full-drift fronts. Every first-read predecessor weakly raises maximal incident clockwise height. Essential maximal-height backbones give P>=4D+2, rounded to P=2D modulo4. No cap-four exclusion or universal capture.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
