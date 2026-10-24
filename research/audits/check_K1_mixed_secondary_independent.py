from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parents[1];note=R/'K1_pipeline_detours_2026-10-23/K1_mixed_secondary_ports_force_left_branch.md'
def outs(h):return tuple((v+(1 if i%2==0 else-1))%4 for i,v in enumerate(h))
# O: NE face b, SW<=b; incoming horizontal. R(W) selects NE.
O=[]
for n in range(1,5):
 for h in product((1,3),repeat=n):
  if h.count(3)!=1:continue
  rs=Counter(h[::2]);gap=rs[3]-rs[1]
  if gap<0:continue
  w=h.index(3);north=[i for i,o in enumerate(outs(h))if o==0]
  assert w%2==0 and north and min(north)<=w
  O.append(dict(h=h,height_gap=gap,unique_W_rank=w,first_N_output=min(north)))
# e: SE face b, NW<=b; exactly one E output and an N input before it.
E=[]
for n in range(1,5):
 for h in product((0,2),repeat=n):
  oo=outs(h)
  if oo.count(1)!=1:continue
  rs=Counter(h[::2]);gap=rs[0]-rs[2]
  if gap<0 or 0 not in h:continue
  e=oo.index(1);firstN=h.index(0)
  if firstN>=e:continue
  assert gap==0 and h in((2,0,0),(2,0,0,0))
  E.append(dict(h=h,unique_E_rank=e,first_N_input=firstN,early_S_rank=0))
assert len(E)==2
assert outs((3,3,3,1)).count(2)==1 and outs((3,3,3,1))[1]==2
# Exact shared physical-port ordinal equalities for the displayed main cells.
assert [i for i,x in enumerate(outs((0,0,0,2)))if x==1]==[0,2,3] # Y->B E0/E1/E3
assert outs((1,1,3,1))[1]==0 # B.L1->C.R0
assert outs((0,0,2,0))[2]==3 # D.R2->z.L1 W
out=dict(status='PASS complete local secondary-port inventories and analytic finite RLS contradiction',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),O=O,e=E,chronology=['Y.R2 -> B.L1 -> C.R0 precedes C.L1 and Zs.L3','O first N output <= S_time; first N arrival e <= S_time+1 < F_time','e.R0(S) earlier than its first N input','z.L1 at T2(D)+1 is sole supplier, so e.R0 at T2(D)+2 > S_time+1'],scope='Complete WHITE cap4 K1, leftmost canonical maximum curve. Signed branch-free collar plus S/RL grammar leads to contradiction, hence LEFT maximum branch necessary. No general K1 exclusion or branch fuel payment.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out['note_sha256'])
