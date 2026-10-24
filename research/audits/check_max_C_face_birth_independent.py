from pathlib import Path
from itertools import product
import json,hashlib
R=Path(__file__).resolve().parents[1];B=R/'rank_two_plateau_2026-10-23';rows=[]
# North incoming/east outgoing are F's clockwise ports. Complete first-input
# traversal occurs one fine step before that cell read, not at the read time.
for n in range(1,5):
 for bits in product((0,1),repeat=n):
  h=tuple(2*b for b in bits);out=tuple((q+(1 if j%2==0 else-1))%4 for j,q in enumerate(h));rf=h[::2].count(0);rg=h[::2].count(2)
  if not rf or rf<rg:continue
  assert 0 in h and 1 in out
  ii=h.index(0);oo=out.index(1);negative=oo<ii
  assert negative==(n>=3 and h[:3]==(2,2,0))
  if negative:assert(rf,rg,ii,oo)==(1,1,2,1)
  # Check the symbolic first-port curl on independent positive return spans.
  for a,b,c in product((1,2,7),repeat=3):
   T=(0,4*a,4*(a+b),4*(a+b+c));curl=T[oo]-T[ii]+1
   if h[0]==0:assert curl==1
   elif negative:assert curl==1-4*b
   else:assert curl==1+4*b
  rows.append(dict(incoming=list(h),rF=rf,rG=rg,first_F_input_rank=ii,first_F_output_rank=oo,first_output_before_first_input=negative))
J=json.loads((B/'face_birth_local_controls.json').read_text());key=lambda q:tuple(q['incoming']);assert {key(q):q for q in rows}=={key(q):q for q in J['rows']}
assert len(rows)==21 and sum(q['first_output_before_first_input']for q in rows)==3
out=dict(status='PASS independent first-port rank and exact chronological curl reconstruction',note_sha256=hashlib.sha256((B/'max_C_first_L_face_birth_backbone.md').read_bytes()).hexdigest(),rows=rows,scope='Complete white cap4 global-max C faces. Earliest boundary departure is L1 from another max face with birth decrease>=5; the finite equivariant diagonal face graph yields a positive essential first-L switch cycle. P>=5*cycle_length is not a stronger global speed bound and diagonal edges are not physical flow for subtraction.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='rows'})
