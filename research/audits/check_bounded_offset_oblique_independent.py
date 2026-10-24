"""Independent current-color verification of both horizontal offset branches."""
from itertools import product
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];C=P/'computability';D=[1j,1,-1j,-1]
N=[];E=[]
for west in range(4):N.append(tuple(0 if i%2==0 else 3 if i//2==west else 1 for i in range(9)))
for west,south in product(range(5),range(4)):E.append(tuple((3 if i//2==west else 1)if i%2==0 else(2 if i//2==south else 0)for i in range(9)))
domains=[sorted(N),sorted(E),sorted(tuple((d+2)%4 for d in w)for w in N),sorted(tuple((d+2)%4 for d in w)for w in E)]
records=json.loads((C/'check_bounded_offset_oblique.records.json').read_text());expected={(r['horizontal'],r['first'],r['second']):r for r in records};assert len(expected)==160
latest={1:0,3:0}
for branch in[1,3]:
 for i,u in enumerate(domains[branch]):
  for j,v in enumerate(domains[2]):
   p=0j;h=1j;colors={};initial={};count={};last={}
   for t,d in enumerate(u+v):
    out=D[d];want=out/h==1j;assert out/h in[1j,-1j]
    default=False if -2*p.real+3*p.imag>=0 else want
    current=colors.get(p,default)
    if current!=want:
     result=dict(horizontal=branch,first=i,second=j,read=t,cell=[int(p.real),int(p.imag)],requested_initial=int(want^(count.get(p,0)%2)),available_initial=int(initial.get(p,False)),previous=last.get(p))
     assert result==expected[branch,i,j];latest[branch]=max(latest[branch],t);break
    initial.setdefault(p,current);colors[p]=not current;count[p]=count.get(p,0)+1;last[p]=t;p+=out;h=out
   else:raise AssertionError('survivor')
assert latest=={1:15,3:9}
out={'status':'PASS independent all160 bounded-tangent-offset local conflicts','domains':list(map(len,domains)),'latest_by_horizontal_branch':latest,'source_sha256':{f:hashlib.sha256((C/f).read_bytes()).hexdigest()for f in['bounded_offset_dual_record_bridge.md','check_bounded_offset_oblique.json','check_bounded_offset_oblique.records.json']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
