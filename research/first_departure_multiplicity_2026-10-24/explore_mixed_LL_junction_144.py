"""Exact mixed2/3/4 endpoint junction across a flow2 LEFT-LEFT pair.
Fixed144 complete corner choices; all external fields open, not a period scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
base=Path(__file__).parent;ss=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0]
ns={};exec(ss,ns);check=ns['check']
cc=Counter();rows=[]
for z,a,b,y in product(['NSS','NNSS','NSSN'],['EEWW','EWWE','EWE','EWEW'],['SSNN','SNNS','SSS','SSSS'],['EWW','EEWW','EWWE']):
 hs={(0,0):z,(1,0):a,(1,1):b,(0,1):y};ans=check(hs);cc[ans]+=1
 if ans=='open':rows.append(dict(Z=z,A=a,B=b,Y=y))
print('144 complete junctions',dict(cc),'open',len(rows))
for r in rows:print(r)
