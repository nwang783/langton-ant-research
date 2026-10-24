"""Invert the signed four-cell reverse rail and reconstruct its G3 port ordinals.
One exact local interface; no period, drift or front scan.
"""
from pathlib import Path
import json
H='NESW'
rev={'Z':'WWWE','A':'NNSN','B':'EEWE','Y':'NNNS'}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def inverse(h):return ''.join(H[(H.index(out(h,r))+2)%4]for r in range(3,-1,-1))
ori={c:inverse(h)for c,h in rev.items()}
assert ori==dict(Z='SSNS',A='EEEW',B='SSSN',Y='WWEW')
step={'Z':('A','E',0),'A':('B','S',-1),'B':('Y','W',0),'Y':('Z','S',0)}
rows=[]
for c,h in ori.items():
 t,p,dk=step[c];sh=[r for r in range(4)if out(h,r)==p];th=[r for r in range(4)if ori[t][r]==p]
 assert len(sh)==len(th)==3
 assert sh[1]==2 and th[1]==1
 assert not(sh.index(1)==th.index(1)and sh.index(2)==th.index(2))if 1 in sh and 2 in th else True
 rows.append(dict(source=c,target=t,target_k_shift=dk,travel=p,source_ranks=sh,target_ranks=th,actual_rank_pairs=list(zip(sh,th)),middle_source_rank=sh[1],middle_target_rank=th[1],matched_rank12=False))
# One lifted four-edge unit goes Z_k -> A_k -> B_(k-1) -> Y_(k-1) -> Z_(k-1).
pos=(0,0)
for p in ['E','S','W','S']:
 d={'E':(1,0),'S':(0,-1),'W':(-1,0)}[p];pos=(pos[0]+d[0],pos[1]+d[1])
assert pos==(0,-2)
obj=dict(scope=__doc__,reverse_histories=rev,original_histories=ori,physical_unit_displacement=pos,ports=rows,canonical_middle='Every edge ordinal2 is source R2 -> target L1; repaired node is everywhere incoming L1 -> outgoing R2.',scope_warning='Necessary original-WHITE front interface conditional on the signed root-free M-3 reverse rail, not a complete-front or autonomous realization.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
