from itertools import product
from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton')
# Clockwise heading order. A complete white cell has turns R,L,R,L.
def out(h): return tuple((x+(1 if j%2==0 else -1))%4 for j,x in enumerate(h))
def histories(axis,flat=False):
 for n in range(1,5):
  for h in product(axis,repeat=n):
   if flat and (n<3 or h[2]!=(h[0]+2)%4):continue
   yield h,out(h)
N,E,S,W=range(4)
z=[h for h,o in histories((E,W),True) if h.count(W)==2]
assert set(z)=={(W,W,E),(E,W,W),(W,W,E,E),(W,E,E,W),(E,W,W,E),(E,E,W,W)}
assert all(out(h).count(S)==2 for h in z)
# Last S cannot precede first W arrival, though the first S may.
assert all(max(j for j,x in enumerate(out(h)) if x==S)>=h.index(W) for h in z)
q=[h for h,o in histories((N,S),True) if h.count(S)==2 and o.count(E)==2]
early=[h for h in q if [j for j,x in enumerate(out(h)) if x==E][1]<[j for j,x in enumerate(h) if x==S][1]]
assert set(early)=={(N,S,S),(N,S,S,N)}
# Before the first W source arrival, an S departure at Z can only be R0(E).
for h in z:
 for j,o in enumerate(out(h)):
  if o==S and j<h.index(W):assert j==0 and h[0]==E
strict=[h for h,o in histories((E,W)) if all(h[j]==W for j in range(0,len(h),2)) and h.count(W)==2]
assert set(strict)=={(W,W),(W,E,W),(W,E,W,E)}
assert [out(h).count(N) for h in strict]==[1,3,4]
y_three=[h for h,o in histories((N,S),True) if h.count(N)==3]
assert all(out(h).count(E)==1 for h in y_three)
assert not [h for h,o in histories((N,S),True) if h.count(N)==4]
def enc(h):return ''.join('NESW'[x] for x in h)
note=ROOT/'K1_pipeline_detours_2026-10-23/K1_zero_state_left_right_launch.md'
r={'status':'PASS','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'equal_Z':list(map(enc,z)),'q_complete':list(map(enc,q)),'q_early':list(map(enc,early)),'strict_Z':list(map(enc,strict)),'flat_Y_three_N':list(map(enc,y_three)),'scope':'Local complete-history inventory only; analytic ordinal chronology and face-birth argument reviewed separately. No exterior realization.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
