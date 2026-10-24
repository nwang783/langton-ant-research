"""Bulk-only exact interface for a translated time-reversed104 sweep.
Bi-infinite orbit profiles are local limits of long finite wakes, not initial seeds.
No cap or endpoint input is supplied by this test.
"""
from pathlib import Path
import json
from probe_perpendicular_highway_wake import H
from certify_highway_wake_reflector import trace
P=Path(__file__).resolve().parent
D=(2,2)
def key(p):return(p[0]-p[1],p[0]%2)
def prof(rows):
 out={}
 for j,(p,h,c) in enumerate(rows):
  # representative x in{0,1}; position p=rep+iD.
  i=(p[0]-p[0]%2)//2
  out.setdefault(key(p),[]).append((j-104*i,c,h,p))
 for v in out.values():v.sort()
 return out
rr,ep,eh=trace(H,(0,0),1);assert(ep,eh)==((2,2),1)
forward=prof(rr)
assert all(v[0][1]=='R'for v in forward.values())
assert all(all(a[1]!=b[1]for a,b in zip(v,v[1:]))for v in forward.values())
wake={k for k,v in forward.items()if len(v)%2}
rev=''.join('L'if c=='R'else'R'for c in H[::-1])
rows,ep,eh=trace(rev,(-1,0),3);assert(ep,eh)==((-3,-2),3)
# Reverse chronological direction means index correction is +104*i.
reverse={}
for j,(p,h,c) in enumerate(rows):
 i=(p[0]-p[0]%2)//2
 reverse.setdefault(key(p),[]).append((j+104*i,c,h,p))
for v in reverse.values():v.sort()
assert all(all(a[1]!=b[1]for a,b in zip(v,v[1:]))for v in reverse.values())
assert {k for k,v in reverse.items()if v[0][1]=='L'}==wake
# Translation classes moduloD represented by tx=0,1 and all possible transverse
# displacement ty. Every black-required class must hit finite wake support, which
# gives an exact finite candidate range, not an arbitrary radius bound.
black={k for k,v in reverse.items()if v[0][1]=='L'}
whites=set(reverse)-black
cands=[];allblack=[]
for tx in range(2):
 shifts=set()
 k0=next(iter(black))
 for k in wake:
  if(k0[1]+tx)%2==k[1]:shifts.add(tx+k0[0]-k[0])
 for ty in sorted(shifts):
  def trans(k):return(k[0]+tx-ty,(k[1]+tx)%2)
  missing=[k for k in black if trans(k)not in wake]
  polluted=[k for k in whites if trans(k)in wake]
  row=dict(translation=[tx,ty],sector_repaired=(tx+ty)%2==1,missing_black_classes=missing,extra_black_classes=polluted)
  cands.append(row)
  if not missing:allblack.append(row)
valid=[r for r in cands if not r['missing_black_classes']and not r['extra_black_classes']]
# All shifts with any black/black overlap have transverse displacement in[-10,10].
# Outside that exact difference range every one of the12 black classes is missing.
sector_rows=[]
for tx in range(2):
 for normal in range(min(k[0]for k in wake)-max(k[0]for k in black),max(k[0]for k in wake)-min(k[0]for k in black)+1):
  ty=tx-normal
  if(tx+ty)%2!=1:continue
  trans=lambda k:(k[0]+normal,(k[1]+tx)%2)
  missing=sorted(k for k in black if trans(k)not in wake)
  polluted=sorted(k for k in whites if trans(k)in wake)
  sector_rows.append(dict(translation=[tx,ty],missing=len(missing),polluted=len(polluted),total=len(missing)+len(polluted)))
assert min(r['missing']for r in sector_rows)==7
assert min(r['total']for r in sector_rows)==10
out=dict(scope=__doc__,forward_read_classes=len(forward),wake_black_classes=sorted(wake),reverse_black_classes=sorted(black),reverse_white_classes=sorted(whites),candidate_translation_classes=len(cands),black_compatible=allblack,fully_compatible=valid,same_sector_overlap_classes=sector_rows,minimum_missing_black_classes=7,minimum_total_changed_classes=10,outside_difference_range_missing=12)
(P/'shifted_reverse104_bulk.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
