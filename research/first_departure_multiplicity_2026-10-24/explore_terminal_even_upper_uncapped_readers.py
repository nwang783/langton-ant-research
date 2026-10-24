"""Discovery: uncapped WHITE outer L/K at signed five-mode Q square.
Finite domains follow exact two-port counts, not a multiplicity cutoff.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json
b=Path(__file__).parent;S={'__file__':str(b/'check_terminal_LL_upper_side_collision.py')};exec((b/'check_terminal_LL_upper_side_collision.py').read_text().split('# Shift the physical Q')[0],S)
analyze,out=S['analyze'],S['out']
def sparse(axis,n,k):
 for pos in combinations(range(n),k):
  p=set(pos);yield ''.join(axis[0] if r in p else axis[1] for r in range(n))
Ls=[h for n in range(2,9) for h in sparse('WE',n,2) if sum(out(h,r)=='S' for r in range(n))==2]
assert len(Ls)==18
Ks={}
for m in sorted({h.count('E') for h in Ls}):
 Ks[m]=[h for n in range(2,2*(2+m)+2) for h in sparse('NS',n,2) if sum(out(h,r)=='E' for r in range(n))==m]
tops=[('SNN','SSNN','EE'),('SNN','SSNN','EEW'),('SNNS','SNN','WWE'),('SNNS','SNNS','WWEE'),('SNNS','SSNN','EEWW')]
ct=Counter();pr=Counter();ans=[]
for (r,a,z),ll in product(tops,Ls):
 for k in Ks[ll.count('E')]:
  hs={(-2,-1):'EEWW',(-1,-1):'SNNS',(0,-1):'WWEE',(1,-1):r,(0,0):a,(1,0):z,(-1,0):ll,(-2,0):k}
  res,cert=analyze(hs);ct[res]+=1;pr[(r,a,z),res]+=1
  if res=='open':ans.append(dict(R=r,U=a,W=z,L=ll,K=k,certificate=cert))
print('L',len(Ls),'K',{m:len(z) for m,z in Ks.items()},'counts',dict(ct),'open',len(ans));print([(r['R'],r['U'],r['W'],r['L'],r['K']) for r in ans])
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,L_domain=Ls,K_domains=Ks,counts=dict(ct),profile_counts={str(k):v for k,v in pr.items()},open=ans),indent=2)+'\n')
