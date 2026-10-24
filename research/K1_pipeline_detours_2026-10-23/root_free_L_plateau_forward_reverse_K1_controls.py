"""Exact forward L1/R2/L3 inventory for a WHITE-collar reverse-K1 birth contact.
All sixteen original four-read N/S histories, no front or period search.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
H='NESW';v={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)};rows=[]
for z in product('NS',repeat=4):
 h=''.join(z);outs=[H[(H.index(x)+(1 if i%2==0 else -1))%4]for i,x in enumerate(h)]
 rh=[H[(H.index(x)+2)%4]for x in outs[::-1]]
 if not(rh[0]==rh[1]and(H.index(rh[2])-H.index(rh[0]))%4==2):continue
 assert h[1]==h[2]and h[3]!=h[1]
 rs=Counter(h[::2]);inc=Counter(h);C={'NW':0,'SE':rs['N']-rs['S']};L={'NE':-inc['S'],'SW':C['SE']-inc['N']};assert len(set(L.values()))==1
 m=L['NE'];C={k:x-m for k,x in C.items()};L={k:x-m for k,x in L.items()}
 top=h[0]==h[1];assert sorted(C.values())==([1,3]if top else[2,2])
 d=(1,1)if h[1]=='N'else(-1,-1)
 def side(p):
  c=d[0]*p[1]-d[1]*p[0];assert c;return'LEFT'if c>0 else'RIGHT'
 sides=[]
 for i,(x,y)in enumerate(zip(h,outs)):
  b=v[x];b=(-b[0],-b[1]);e=v[y];sides.append([side(b),side(e)])
 assert sides[1]==['RIGHT','LEFT']and sides[2]==['RIGHT','RIGHT']and sides[3]==['LEFT','RIGHT']
 assert sides[0]==(['RIGHT','RIGHT']if top else['LEFT','LEFT'])
 rows.append(dict(forward_headings=h,forward_outgoing=''.join(outs),reverse_headings=''.join(rh),C_minus_m=C,L_minus_m=L,type='TOP'if top else'FLAT',forward_cut_direction=d,side_inventory=sides,reverse_LEFT_L3_bit=int(top)))
assert len(rows)==4 and sum(r['type']=='TOP'for r in rows)==2
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(dict(scope=__doc__,rows=rows),indent=2)+'\n');print('PASS four exact reverse-birth rows, with full forward crossing inventory')
