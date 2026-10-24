"""Exact finite packet tables used in alternating_boundary_exclusion.md."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
D=[(0,1),(1,0),(0,-1),(-1,0)]
def replay(w,pose):
 x,y,h=pose; first={};last={};counts={};reads=[]
 for a in w:
  p=x,y
  if p in last:assert last[p]!=a
  else:first[p]=a
  last[p]=a;counts[p]=counts.get(p,0)+1;reads.append([x,y,a])
  h=(h+(1 if a=='R' else-1))%4;x+=D[h][0];y+=D[h][1]
 assert (x,y,h)==pose
 return first,counts,reads
R,RC,RR=replay('RLLLLRRR',(0,0,0))
L,LC,LR=replay('LRRRRLLL',(1,0,1))
assert {p for p,a in R.items() if a=='L'}=={(1,0),(1,1),(0,1)}
assert {p for p,a in R.items() if a=='R'}=={(0,0),(1,-1),(0,-1)}
assert {p for p,a in L.items() if a=='L'}=={(1,0),(0,1),(0,0)}
assert {p for p,a in L.items() if a=='R'}=={(1,1),(2,1),(2,0)}
assert {p for p,c in RC.items() if c==2}=={(0,0),(1,0)}
assert {p for p,c in LC.items() if c==2}=={(1,0),(1,1)}
# Exact symbolic separation: the only points on x-y=-1 in either footprint
# are u_0=(0,1). Translation by (k,k) preserves x-y.
for F in [R,L]:assert {p for p in F if p[0]-p[1]==-1}=={(0,1)}
assert RC[0,1]==LC[0,1]==1 and R[0,1]==L[0,1]=='L'
out={'status':'PASS','R_packet_reads':RR,'L_packet_reads':LR,
 'unique_off_diagonal_read_in_each_packet':[0,1],
 'off_diagonal_read':'L','off_diagonal_net_flip':1}
print(json.dumps(out,indent=2));(P/'alternating_spine_local.json').write_text(json.dumps(out,indent=2)+'\n')
