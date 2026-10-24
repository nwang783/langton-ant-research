"""Independent exhaustive geometric controls, not a replacement for Whitney proof."""
import itertools,json,hashlib
from collections import defaultdict,Counter
from pathlib import Path
D=[1j,1,-1j,-1];total=Counter();examples={}
for length in range(2,17,2):
 for bits in itertools.product((0,1),repeat=length):
  excess=length-2*sum(bits)
  if excess%4:continue
  p=0j;h=0;vis=[]
  for i,L in enumerate(bits):
   vis.append((int(p.real),int(p.imag),h,L,i));h=(h+(3 if L else 1))%4;p+=D[h]
  if not p:continue
  dx,dy=int(p.real),int(p.imag);groups=defaultdict(list)
  for x,y,h,L,i in vis:
   if dx:
    rem=x%abs(dx);key=(dx*y-dy*x,rem);epoch=(x-rem)//dx
   else:
    rem=y%abs(dy);key=(x,rem);epoch=(y-rem)//dy
   groups[key].append((i-length*epoch,h,L))
  K=0
  for row in groups.values():
   row.sort()
   for i,(_,h,L) in enumerate(row):
    for _,g,M in row[i+1:]:
     assert (g-h)%2==0
     if L and not M:K+=1 if (g-h)%4==2 else -1
  assert 4*K==excess,(bits,p,K,excess)
  total[length]+=1
out={'status':'PASS independent all-word controls through length16','scope':'Every nonzero-drift, heading-restoring raw turn word, without color-feasibility filtering. Analytic proof remains chronological lane regularization plus Whitney Theorem2.','counts':dict(total),'total':sum(total.values()),'primary_source':'https://www.numdam.org/item/CM_1937__4__276_0.pdf','primary_pdf_sha256':hashlib.sha256(Path('/tmp/whitney1937.pdf').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
