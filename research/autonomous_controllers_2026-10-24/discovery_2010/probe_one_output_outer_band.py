import sys,json,itertools
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from certify_drift31_read_minimum import words
from partial_drift31_graph import graph
low=[(),(),(),(2,),(3,1),(2,2),(1,1,3,1),(2,2,0,0,2,2)]
H5=[z for z in words(1,10,3,3,2,2)if len(z)%2==0 and z[-1]==3]
V6=[z for z in words(0,13,0,3,1,3)if len(z)%2==0 and z[-1]==2]
print('domains',H5,len(V6))
rows=[]
for h5,v6 in itertools.product(H5,V6):
 k,G=graph(low+[h5,v6]);rows.append({'H5':h5,'V6':v6,'outcome':k,'witness':G})
from collections import Counter
print(Counter(x['outcome']for x in rows))
for r in rows:
 if r['outcome']=='open':print('OPEN',''.join('NESW'[x]for x in r['H5']),''.join('NESW'[x]for x in r['V6']))
Path(__file__).with_suffix('.json').write_text(json.dumps({'low':low,'H5_domain':H5,'V6_domain':V6,'rows':rows},indent=2)+'\n')
