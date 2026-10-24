#!/usr/bin/env python3
"""Independent standard104 control of the representative-voltage convention."""
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0))
root=Path(__file__).parent
word=(root.parent/'word_stabilization/standard_word.txt').read_text().strip()
P=len(word);d=(-2,-2);p=(1,0);h=2;hist={}
for i,c in enumerate(word):
 r=p[0]%2;k=(p[0]-r)//-2;b=(r,r+p[1]-p[0]);tau=i-k*P
 hist.setdefault(b,[]).append((tau,h,c))
 h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy
assert p==(-1,-2) and h==2
out={}
for b,vis in hist.items():
 vis.sort()
 assert ''.join(z[2] for z in vis)==''.join('R' if j%2==0 else 'L' for j in range(len(vis)))
 for t,h,c in vis:
  assert h%2==(1 if sum(b)%2==0 else 0)
  hh=(h+(1 if c=='R' else -1))%4;dx,dy=D[hh];q=b[0]+dx,b[1]+dy
  r=q[0]%2;k=(q[0]-r)//-2;qb=(r,r+q[1]-q[0]);out.setdefault((b,qb,k),[]).append(t)
for (u,v,k),ts in out.items():
 physical=(v[0]+k*d[0],v[1]+k*d[1]);vec=(physical[0]-u[0],physical[1]-u[1]);hh=D.index(vec)
 us=[t for t,h,c in hist[u] if (h+(1 if c=='R' else -1))%4==hh]
 vs=[t+k*P for t,h,c in hist[v] if h==hh]
 assert [t+1 for t in us]==vs
res=dict(control='standard104 rotated by 180 degrees and shifted one cell',drift=d,period=P,classes=len(hist),max_multiplicity=max(map(len,hist.values())),clock_equations='PASS',white_stable_order='PASS',scope='Verifies the cut-voltage convention and local clocks above cap three; not a positive cap-three example.')
(root/'cylinder_clock_standard_control.json').write_text(json.dumps(res,indent=2)+'\n')
print(res)
