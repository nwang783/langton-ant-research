"""Finite residual obligations for the exact Gaussian base -1+i proof."""
import json
from pathlib import Path
disk={(a,b) for a in range(-3,4) for b in range(-3,4) if a*a+b*b<=9}
def divide(a,b):
 assert (a+b)%2==0
 return ((-a+b)//2,(-a-b)//2)
rows=[];edges=[]
for p in sorted(disk):
 q=p;seen=set();digits=[]
 while q!=(0,0):
  assert q in disk and q not in seen;seen.add(q);a,b=q;d=(a+b)%2;digits.append(d);q=divide(a-d,b)
 rows.append(dict(point=p,digits_lsd=digits,steps=len(digits)))
for p in sorted(disk):
 for d in (0,1):
  for e in (0,1):
   a,b=p[0]+d-e,p[1]
   if (a+b)%2==0:
    q=divide(a,b);assert q in disk;edges.append([p,d,e,q])
assert len(rows)==29 and len(edges)==58
out=dict(status='PASS',base=[-1,1],disk_radius=3,numeral_cases=rows,unit_carry_transitions=edges)
Path('/workspace/shared/langton/audits/complex_base_representation_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:29 finite division orbits,58 carry transitions; outside-disk contraction is analytic.')
