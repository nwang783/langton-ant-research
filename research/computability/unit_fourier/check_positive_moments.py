import json,pathlib
from positive_moments import *
p=pathlib.Path(__file__).parent
controls=json.loads((p/'unit9_fourier.json').read_text())['geometric_controls'];checks=0
for a,images in controls:
 for x,y in ((Q(2),Q(1)),(Q(1,2),Q(2)),(Q(3,2),Q(2,3))):
  mats,z=matrices(images,a,x,y)
  for r in range(4):
   for j,root in enumerate('RL'):
    occ,_,_=literal_occupation(images,root,r)
    val=sum(c*x**q[0]*y**q[1] for q,c in occ.items())
    assert z[j]==val;checks+=1
   z=mv(mats[r%len(mats)],z)
synthetic=[]
for base in (2,3,Q(3,2)):
 for m in(1,2,3):
  for sign in(-1,1):
   seq=[sign*Q(base)**n*(n+1)**(m-1)+(-1)**n for n in range(60)]
   c=negative_divergence(seq,8)
   assert c['certified']==(sign<0)
   assert c['dominant_root']==str(base) and c['multiplicity']==m
   synthetic.append(dict(base=str(base),multiplicity=m,sign=sign,certificate=c))
out=dict(direct_rational_transfer_checks=checks,synthetic_cases=len(synthetic),synthetic=synthetic)
(p/'check_positive_moments.json').write_text(json.dumps(out,indent=2)+'\n');print(checks,len(synthetic))
