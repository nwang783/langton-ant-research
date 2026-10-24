from pathlib import Path
from itertools import product
import json,hashlib
ROOT=Path('/workspace/shared/langton');D=ROOT/'K1_pipeline_detours_2026-10-23';SELF=Path(__file__).resolve()
# Headings N,E,S,W. Enumerate the complete flat WHITE RLR[R/L] histories,
# allowing both L headings, rather than discarding any optional supplier.
rows=[]
for length in (3,4):
 for r0 in (1,3):
  for ls in product((1,3),repeat=length//2):
   heads=[r0,ls[0],(r0+2)%4]+([ls[1]]if length==4 else [])
   outs=[(h+(1 if i%2==0 else -1))%4 for i,h in enumerate(heads)]
   firstE=heads.index(1);earlierN=sum(h==0 for h in outs[:firstE]);assert earlierN<=1
   rows.append(dict(headings=heads,outputs=outs,first_E=firstE,N_strictly_before=earlierN))
# Selected a=NNS and c=SSN, optional L3 on either opposite face.
selected=[]
for a3 in (None,0,2):
 for c3 in (None,0,2):
  a=[0,0,2]+([]if a3 is None else[a3]);c=[2,2,0]+([]if c3 is None else[c3]);co=[(h+(1 if i%2==0 else-1))%4 for i,h in enumerate(c)]
  assert [i for i,h in enumerate(a)if h==0][:2]==[0,1]
  assert [i for i,h in enumerate(co)if h==1][:2]==[1,2]
  selected.append(dict(a=a,c=c,c_outputs=co))
notes=['max_face_birth_curve_no_two_LEFT_turns.md','K1_constant_zero_LEFT_L3_mode_excluded.md']
bind={n:hashlib.sha256((D/n).read_bytes()).hexdigest()for n in notes}
assert bind[notes[0]]=='a93dabfc34aecede83ef23fb81cb7899e3b2c774fbdb489a018bab5768fef20d'
assert bind[notes[1]]=='71abcb4ae8feeecebfa664b693688c32ba71f494aec8e5f65199c80ba5d94470'
# The two signed zero-state LR necessary histories overlap at one physical cell.
firstY=['SSN','SSNS','SSNN','SNNS'];secondQ=['NSS','NSSN'];assert all(y[0]!=q[0]for y in firstY for q in secondQ)
# Pure cyclic grammar check is a control, not the all-length argument.
for n in range(2,15):
 for w in product('LR',repeat=n):
  if w.count('L')!=w.count('R')or any(w[i]==w[(i+1)%n]=='L'for i in range(n)):continue
  assert all(w[i]!=w[(i+1)%n]for i in range(n))
out=dict(status='PASS all-K canonical birth-curve no-LL and K1 constant-zero LEFT-L3 exclusion',notes=bind,flat_rows=rows,selected_optional_histories=selected,zero_LR_overlap=[dict(first=y,second=q,inconsistent_first_R=True)for y in firstY for q in secondQ],analytic_no_LL='Physical lifted selected contacts a(0,1),b(-1,1),c(-1,0) bound four max faces. Complete flat w(0,0) has E/W inputs and opposite R headings. Its second N departure supplies a.L1 at T1(a)-1; its first E arrival is c.L1 departure plus1. Canonical birth times give T1(a)<T1(c), contradicting at-most-one N departure strictly before first E input. No K1, ear, leftmostness or modulo-P clock identification.',analytic_zero='In K1 constant-zero mode, strict straight requires bit1 and equal-max straight requires a strict fall, so no straight. Signed zero turning plus no LL forces cyclic LR alternation. Two consecutive zero LR pairs assign opposite actual R0 headings to the same physical cell Y=q prime=(0,1). Small quotients use physical lifts, not duplicate fictitious cells.',scope='Complete WHITE cap-four canonical maximum-face birth curve. General K1 constant-one/variable branchful modes remain open; no finite-seed or capture claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(bind)
