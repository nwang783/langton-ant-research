"""Four literal104 involution templates against the exact mature wake input.
Only bulk profile compatibility; no finite head correction or cap is inferred.
"""
from pathlib import Path
import json
from certify_highway_wake_reflector import trace
from probe_perpendicular_highway_wake import H
P=Path(__file__).resolve().parent
W=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
key=lambda p:(p[0]-p[1],p[0]%2)
comp=lambda w:''.join('L'if c=='R'else'R'for c in w)
words={'H':H,'reverseH':H[::-1],'complementH':comp(H),'reverseComplementH':comp(H[::-1])};out=[]
for name,w in words.items():
 for h in range(4):
  rows,ep,eh=trace(w,(0,0),h)
  if ep!=(-2,-2)or eh!=h:continue
  hist={}
  for j,(p,hh,c)in enumerate(rows):
   e=p[0]%2;i=(p[0]-e)//2;hist.setdefault(key(p),[]).append((j+104*i,c))
  for v in hist.values():v.sort()
  assert all(all(a[1]!=b[1]for a,b in zip(v,v[1:]))for v in hist.values())
  B={k for k,v in hist.items()if v[0][1]=='L'};V=set(hist)-B;matches=[]
  # Nonempty required black support bounds the transverse shift exactly.
  if not B:
   out.append(dict(name=name,head=h,black_classes=0,read_classes=len(hist),comment='White bulk only; any compatible lane misses all wake black classes.'));continue
  for tx in range(2):
   for normal in range(min(z for z,e in W)-max(z for z,e in B),max(z for z,e in W)-min(z for z,e in B)+1):
    ty=tx-normal;f=lambda k:(k[0]+normal,(k[1]+tx)%2)
    if all(f(k)in W for k in B)and all(f(k)not in W for k in V):matches.append(dict(translation=[tx,ty],same_sector=(tx+ty+h)%2==1))
  out.append(dict(name=name,head=h,black_classes=sorted(B),white_classes=sorted(V),matches=matches))
(P/'wake_dihedral_words.json').write_text(json.dumps(dict(scope=__doc__,results=out),indent=2)+'\n')
print(json.dumps(out,indent=2))
