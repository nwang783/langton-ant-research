"""Exact two shortest balanced-turn one-use joins between even LL portals.
Two fixed geometric stencils, not a period/length/radius scan. Exterior open.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
check=L['check'];V=L['V'];out=L['out'];rows=[];ct=Counter()
upper={(1,1):'SN',(0,1):None,(0,0):'NNSS',(1,0):'EE'}
for join,up,lo,opt in product(['RL','LR'],['EWW','EWWE'],['EWW','EWWE'],[False,True]):
 lowerB=(0,-2)if join=='RL'else(2,-2);x,y=lowerB
 hs=upper|{(0,1):up,(x,y):'SN',(x-1,y):lo,(x-1,y-1):'NNSS',(x,y-1):'EE'}
 if join=='RL':hs|={(1,-1):'S',(0,-1):'EEWE'if opt else'EEW'}
 else:hs|={(1,-1):'NNSN'if opt else'NNS',(2,-1):'E'}
 ans=check(hs);ct[ans]+=1
 rows.append(dict(join=join,upper_root=up,lower_root=lo,LEFTfour=opt,result=ans,histories={str(p):h for p,h in sorted(hs.items())}))
print(dict(ct));print(*[{k:v for k,v in r.items()if k!='histories'}for r in rows if r['result']=='open'],sep='\n')
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(ct),rows=rows,warning='Even open joins are not real connectors or complete fronts; both one-use internal vertices are odd in any open3-readLEFT case.'),indent=2)+'\n')
