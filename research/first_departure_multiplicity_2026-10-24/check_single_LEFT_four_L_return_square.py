"""Fixed complete four-L return cover at a singleton-LEFT flow-two contact.
All three neighboring named histories remain WHITE cap four. No period scan.
"""
from pathlib import Path
from itertools import product
import json
base=Path(__file__).parent
# Reuse only the generic local rank/ordinal/clock checker, not its old fixed cover.
ns={};exec((base/'check_flow2_LL_reset_square.py').read_text().split('rows=[];bad=Counter()')[0],ns)
pos={'Y':(0,1),'A':(0,2),'B':(-1,2),'C':(-1,1)}
ns['pos']=pos;ns['inv']={p:u for u,p in pos.items()};check=ns['check']
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
bs=[''.join(x)for n in range(1,5)for x in product('EW',repeat=n)]
rows=[];counts={};total=0
for y,a,c,b in product(['WEE','WEEW'],['NNSS','NSSN'],['NNSS','NSSN'],bs):
 total+=1;hs=dict(Y=y,A=a,B=b,C=c);ans,data=check(hs)
 if ans=='open':
  succ={(u,r):(v,s)for u,r,v,s,_,_ in data['edges']};cur=('Y',1);route=[cur]
  for _ in range(4):
   if cur not in succ:break
   cur=succ[cur];route.append(cur)
  if len(route)!=5 or route[-1]!=('Y',2)or any(r%2!=1 for _,r in route[:-1]):ans='not the prescribed four-L return'
  else:rows.append(dict(histories=hs,route=route,**data))
 counts[ans]=counts.get(ans,0)+1
assert total==240 and len(rows)==4
assert {tuple(r['histories'][u]for u in ['Y','A','B','C'])for r in rows}=={(y,'NSSN',b,'NSSN')for y in ['WEE','WEEW']for b in ['WWE','WWEE']}
obj=dict(scope=__doc__,candidates=total,classification=counts,necessary_open_rows=rows,consequence='Every such four-L return has both adjacent RIGHT profiles Y, while root O/U remains possible locally. At global M the signed five-contact staircase language permits the O root with V caps, but excludes the U root because a current U requires following RIGHT X.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',counts)
