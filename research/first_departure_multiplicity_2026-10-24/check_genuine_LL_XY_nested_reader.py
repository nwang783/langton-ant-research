"""Exact complete reader domain after all six signed LL reactions.
All WHITE 1..4 C histories, B flat choices, ordinal ports and global heights
retained. OPEN patches are necessary only, not actual factors/fronts.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import ast,json
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
out=L['out'];check=L['check'];H=L['H'];V=L['V']
def rr(h,d,k):return[r for r in range(len(h))if(h[r]if k=='in'else out(h,r))==d]
Cs=[h for h in L['dom']((2,-1))if len(rr(h,'E','in'))==2 and len(rr(h,'N','out'))==2]
assert set(Cs)=={'EEW','WEE','EEWW','EWWE','WEEW','WWEE'}
j=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());rows=[];tot=Counter()
for rs in j['roots']:
 for rx in rs['cyclic_necessary_profiles']:
  hs0={ast.literal_eval(p):h for p,h in rx['histories'].items()};ct=Counter();kept=[]
  for B,C in product(['SSNN','SNNS'],Cs):
   hs=hs0|{(1,-1):B,(2,-1):C};a=check(hs);ct[a]+=1
   if a!='open':continue
   assert B=='SNNS'and C in['WEE','WEEW']
   su={}
   for p,h in hs.items():
    for d,v in V.items():
     q=p[0]+v[0],p[1]+v[1]
     if q not in hs:continue
     sr=rr(h,d,'out');tr=rr(hs[q],d,'in');assert len(sr)==len(tr)
     su.update({(p,r):(q,s)for r,s in zip(sr,tr)})
   n=((2,-1),1);pa=[n]
   while n!=((2,-1),2):
    assert n in su and len(pa)<20;n=su[n];pa.append(n)
   w=''.join('R'if r%2==0 else'L'for p,r in pa[:-1]);want='LLRRRRLL'if rx['kind']=='P'else'LLRRLLLLRRLL'
   assert w==want and len(pa)-1==rx['X_age23']+4
   kept.append(dict(B=B,C=C,word=w,literal_return=pa,Delta12=len(pa)-1))
  assert len(kept)==2
  rows.append(dict(root=rs['root'],reaction=rx['kind'],counts=dict(ct),survivors=kept));tot.update(ct)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,C_complete_domain=Cs,all72_counts=dict(tot),rows=rows,all_six_XY=True,warning='Off-Gamma role and global injection are human signed-dependency arguments. No actual physical exterior factor or front constructed.'),indent=2)+'\n');print('PASS',dict(tot),'all six XY, two complete C stock alternatives, exact8/12 literal returns')
