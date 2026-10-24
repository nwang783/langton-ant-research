"""Fixed odd eight-step return plus its forced following RR gate.
Necessary complete WHITE cap-four neighborhood; no period, length or front scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
base=Path(__file__).parent
ss=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0]
# The selected root clockwise face has LL(0,1), normalized global M=0.
ss=ss.replace("val={(0,-1):0};q=deque([(0,-1)])", "val={(0,1):0};q=deque([(0,1)])")
ns={};exec(ss,ns);check=ns['check'];out=ns['out']
words=lambda axis:[ ''.join(x)for n in range(1,5)for x in product(axis,repeat=n)]
counts=Counter();rows=[]
for b,d,e,p,q in product(['WWE','WWEE'],words('NS'),words('EW'),['NNSS','NSSN'],['EEWW','EWWE']):
 hs={(0,1):'WEE',(0,2):'NNSS',(-1,1):'NSSN',(-1,2):b,(-1,3):d,(0,3):e,(1,2):'WWEE',(1,3):p,(2,3):q,(2,2):'NNSS'}
 ans=check(hs);counts[ans]+=1
 if ans=='open':
  # The prescribed eight-turn word must use R, not L, at D and E.
  di=[i for i,x in enumerate(d)if x=='N'][0]
  ei=[i for i in range(len(d))if out(d,i)=='E'].index(di) if out(d,di)=='E' else -1
  er=[i for i,x in enumerate(e)if x=='E']
  if di%2 or ei<0 or ei>=len(er) or er[ei]%2:counts['open']-=1;counts['wrong literal turn']+=1
  else:rows.append(dict(B=b,D=d,E=e,P=p,Q=q,D_current_rank=di,E_current_rank=er[ei]))
print('7200 candidates',dict(counts),'open rows',len(rows))
for r in rows:print(r)
cc=Counter();added=[]
for r in rows:
 for k in ['SS','SSN']:
  hs={(0,1):'WEE',(0,2):'NNSS',(-1,1):'NSSN',(-1,2):r['B'],(-1,3):r['D'],(0,3):r['E'],(1,2):'WWEE',(1,3):r['P'],(2,3):r['Q'],(2,2):'NNSS',(1,1):k}
  aa=check(hs);cc[aa]+=1
  if aa=='open':added.append(r|dict(K=k))
print('K extension',dict(cc),'open',len(added))
for r in added:print(r)
