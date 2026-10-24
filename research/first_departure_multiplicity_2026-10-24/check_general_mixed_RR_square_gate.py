"""Complete mixed-flow LRRL first-ordinal square gate.
All cap-four boundary profiles, arbitrary exterior histories. No period scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def rr(h,dr,kin):return[i for i in range(len(h))if(h[i]if kin=='in'else out(h,i))==dr]
rights=['E'+''.join(x)for n in range(1,5)for x in product('EW',repeat=n-1)]
rot=lambda h:''.join(H[(H.index(x)+1)%4]for x in h)
zwords=['NNS','NNSN','NSS','NSSN','NNSS','NSSS'];ywords=['EEW','EEWE','EWW','EWWE','EEWW','EWWW']
counts=Counter();ep=set();no1=set();examples={}
for z,a,b,y in product(zwords,rights,[rot(h)for h in rights],ywords):
 hs=dict(Z=z,A=a,B=b,Y=y);dirs=[('Z','A','E'),('A','B','S'),('B','Y','W'),('Y','Z','N')]
 ins={};outs={};flows=[];bad=False
 for u,v,dr in dirs:
  sr=rr(hs[u],dr,'out');tr=rr(hs[v],dr,'in')
  if len(sr)!=len(tr)or not sr:bad=True;break
  outs[u]=sr[0];ins[v]=tr[0];flows.append(len(sr))
 if bad:counts['port mismatch']+=1;continue
 assert[(ins[u],outs[u])for u in['Z','A','B']]==[(0,0)]*3
 if(ins['Y'],outs['Y'])==(1,2):counts['positive first-ordinal clock']+=1;continue
 assert(ins['Y'],outs['Y'])==(2,1)
 # Delta12(Y)=4; its first/second N outputs1,2 give consecutive N arrivals at Z.
 assert rr(y,'N','out')[:2]==[1,2]
 zn=rr(z,'N','in')
 if zn[1]!=1:counts['Z first-to-rank3 gap forced4']+=1;continue
 counts['necessary first-ordinal survivors']+=1;ep.add((z,y));examples.setdefault((z,y),[z,a,b,y])
 # These are b path flows, not the missing-edge flow at index3.
 if min(flows[:3])>=2:
  assert z=='NNSS'and y=='EEWW';no1.add((a,b,flows[1]))
assert sum(counts.values())==8100
assert ep=={('NNS','EEW'),('NNS','EEWW'),('NNSS','EEW'),('NNSS','EEWW'),('NNSN','EEWE')}
assert no1=={('EEWW','SSNN',2),('EEWW','SNNS',2),('EWWE','SSNN',2),('EWWE','SNNS',2),('EWE','SSS',3),('EWEW','SSSS',4)}
obj=dict(scope=__doc__,all8100_counts=dict(counts),necessary_LEFT_endpoint_pairs=[dict(Z=z,Y=y,example_profile=examples[z,y])for z,y in sorted(ep)],no_one_use_RIGHT_pairs=[dict(A=a,B=b,internal_flow=f)for a,b,f in sorted(no1)],conclusion='Both LEFT endpoints are flow1 or flow2 V, never flow3/O/U. At no-one-use both are V2. The checked conditions are necessary first-ordinal constraints; no surviving complete-front or exterior realization is asserted.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS8100 mixed LRRL choices:',dict(counts),'five endpoint pairs/six no1 RIGHT pairs')
