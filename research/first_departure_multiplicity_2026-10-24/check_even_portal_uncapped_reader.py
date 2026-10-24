"""Uncapped C reader domain is bounded by exact port counts, not a cap scan.
Analytic entry-incidence proof is independent of the finite controls.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent;L={};exec((base/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],L)
out,exact=L['out'],L['exact'];rows=[];ct=Counter();opens=[]
for root,q in product(['EWW','EWWE'],['E','EE','EEW','EEWE']):
 k=sum(out(root,r)=='N' for r in range(len(root)));l=q.count('E')
 for n in range(1,2*(k+l)+2):
  for z in product('NS',repeat=n):
   if z.count('N')!=k or sum(out(z,r)=='E' for r in range(n))!=l:continue
   c=''.join(z);a=sum(c[r]=='N'for r in range(0,n,2));b=sum(c[r]=='N'for r in range(1,n,2));s=sum(c[r]=='S'for r in range(0,n,2));t=sum(c[r]=='S'for r in range(1,n,2));eps=n%2
   assert k==a+b and l==a+t and s==k+l-3*a+eps
   assert n==2*(k+l-2*a)+eps<=2*(k+l)+1
   hs={(1,1):'SN',(0,1):root,(0,0):'NNSS',(1,0):'EE',(1,2):q,(0,2):c}
   ans,cert=exact(hs);ct[ans]+=1
   row=dict(root=root,q=q,C=c,Nin=k,Eout=l,length=n,result=ans,R_S_minus_R_N=s-a,certificate=cert);rows.append(row)
   if ans=='open':
    assert c.startswith('SS') and out(c,0)=='W'
    opens.append((root,q,c,s-a))
assert len(rows)==131 and ct=={'rank':119,'open':12}
assert sum(z[3]==0 for z in opens)==5
assert all(z[3]>=1 for z in opens if len(z[2])>=5)
# Exact GLOBAL-M shield rejection for even root and even q, at arbitrary length.
shield_rows=[r for r in rows if r['root']=='EWWE'and r['q']=='EEWE'and r['C'].startswith('SS')]
assert shield_rows and all(r['R_S_minus_R_N']>=1 for r in shield_rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,count_derived_bound='n_C=2(k+l-2 R_N)+epsilon<=2(k+l)+1<=11',summary=dict(ct),open_profiles=opens,rows=rows,warning='Necessary local reader profiles only, not board factors, completed fronts or renewable shields.'),indent=2)+'\n')
print('PASS131 count-derived uncapped C histories:119 rank failures+12 open; analytic first-SS and positive-height shields')
