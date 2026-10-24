"""An explicit ordered PORT MODEL realization, NOT an autonomous ant seed."""
from pathlib import Path
from collections import Counter
import json,hashlib
P=Path(__file__).parent
C=[(0,0),(1,0),(1,1),(0,1)];D=[(0,1),(1,0),(0,-1),(-1,0)];mask=0;ports=[];episodes=[];counts=Counter();allreads=[]
def enter(v,label):
 global mask
 before=mask;p=C[v];h=[0,3,2,1][v];seq=[]
 while p in C:
  i=C.index(p);black=bool(mask>>i&1);ch='L'if black else'R';typ=('outer_L'if not seq else'inner_L')if black else('entry_R'if not seq else'exit_R')
  counts[i,typ]+=1;seq.append((i,ch,typ));allreads.append((i,ch,typ));mask^=1<<i;h=(h+(-1 if black else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);assert len(seq)<=6
 ports.append(v);episodes.append(dict(entry=v,label=label,before=before,after=mask,reads=seq,exit_pose=[p,h]))
# Three complete preparation/cleanup sweeps. One sweeps four starting vertices.
for sweep in range(3):
 for v in range(4):
  assert mask==0
  enter(v,'prepare RR');assert mask==(1<<v)|(1<<((v+1)%4))
  enter(v,'remove first prepared bit');r=(v+1)%4;assert mask==1<<r
  if sweep==0 and v==0:
   for k in range(15):
    for e in[(r+2)%4,(r+1)%4,r,(r-1)%4]:enter(e,f'inner circulation {k}')
    assert mask==1<<r
  enter(r,'remove root');assert mask==0
assert len(ports)==96 and len(allreads)==288
for v in range(4):assert {z:counts[v,z]for z in['inner_L','outer_L','entry_R','exit_R']}=={'inner_L':30,'outer_L':6,'entry_R':18,'exit_R':18}
for v in range(4):
 w=''.join(c for i,c,z in allreads if i==v);assert w=='RL'*36
assert Counter(ports)=={0:24,1:24,2:24,3:24}
# Exact four-cell radial r=1/2 flow, multiplied by32, has these turn counts.
from fractions import Fraction as F
A=lambda i,j:F(1,2)**(abs(i)+abs(j))
for x,y in C:
 faces=[(x,y),(x-1,y),(x-1,y-1),(x,y-1)];a=[A(*q)for q in faces]
 ts=[32*(3*a[k]+a[(k-1)%4]+a[(k+1)%4]-a[(k+2)%4])/4 for k in range(4)]
 inner=faces.index((0,0));outer=(inner+2)%4
 assert ts[inner]==30 and ts[outer]==6 and all(ts[k]==18 for k in[(inner+1)%4,(inner-1)%4])
fs=['SUMMABLE_BALANCED_TURN_FLOW_MANIFEST.json','../audits/check_summable_turn_flow_independent.json','ORDERED_SQUARE_CIRCULATION_MANIFEST.json','../audits/check_ordered_square_circulation_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR exact ordered port-model realization; independent audit pending',NOT_A_FINITE_SEED_CONSTRUCTION=True,initial_patch_black=[],final_patch_black=[],entry_ports=ports,episodes=episodes,per_cell_counts=[dict(cell=C[v],counts={z:counts[v,z]for z in['inner_L','outer_L','entry_R','exit_R']})for v in range(4)],patch_reads=288,external_entries=96,each_site_word='(RL)^36',radial_scale=32,dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},scope='Complete central2x2 radial flow projection has an exact WHITE-start ordered local realization under externally chosen entries. Exterior routes, colors, time, seed cost and causal full-board reachability are not supplied.')
(P/'RADIAL_SQUARE_ORDERED_PORTS_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS AUTHOR:96 entry ports,288 reads,each site(RL)^36; not an ant seed')
