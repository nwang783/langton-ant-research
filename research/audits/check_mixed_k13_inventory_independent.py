from pathlib import Path
from itertools import product
import json
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'causal_reduction/matrix_candidates';J=json.loads((F/'mixed_k13_3_2_2_7_inventory.json').read_text());dirs=(1j,1,-1j,-1);endpoints=(2+7j,3+2j,-2-7j,-3-2j);domains=[];features=[];rawcounts=[]
def legal(w,h):
 p=0j;colors={}
 for d in w:
  c=int(d/h==1j);assert d/h in(1j,-1j)
  if p in colors and colors[p]!=c:return False
  colors[p]=1-c;p+=d;h=d
 return True
for s in range(4):
 raw=0;dom=[];feat=[]
 for signs in product((-1,1),repeat=13):
  w=tuple(sign*(1j if (r+s)%2==0 else 1)for r,sign in enumerate(signs))
  if sum(w)!=endpoints[s]:continue
  raw+=1
  if not any(legal(w,h)for h in dirs if h/w[0]in(1j,-1j)):continue
  p=0j;first=None
  for t,d in enumerate(w,1):
   p+=d;x=int(p.real);y=int(p.imag)
   if p==endpoints[s]and first is None:first=dirs.index(d)
   if (7*x-2*y)%17==0 and(-2*x+3*y)%17==0:assert p in(0j,endpoints[s])
  dom.append(tuple(dirs.index(d)for d in w));feat.append((dirs.index(w[0]),first))
 assert set(dom)==set(map(tuple,J['domains'][s]));domains.append(dom);features.append(feat);rawcounts.append(raw)
assert rawcounts==[15,315,15,315]and list(map(len,domains))==[15,91,15,91]
assert all(f==(s,s)for s in(0,2)for f in features[s])
# Every image contains a horizontal symbol, and every horizontal image all four.
assert all(any(z%2 for z in w)for dom in domains for w in dom)
assert all(set(w)==set(range(4))for s in(1,3)for w in domains[s])
lines=[]
for dom,fs in zip(domains,features):
 lines.append(str(len(dom)))
 for w,(f,h)in zip(dom,fs):lines.append(''.join(map(str,w))+' '+str(h))
(ROOT/'audits/mixed_k13_independent_domains.txt').write_text('\n'.join(lines)+'\n')
out=dict(status='PASS exact mixing k13 inventories, source/target-only coarse overlap and two-level primitivity',raw_counts=rawcounts,domain_counts=list(map(len,domains)))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
