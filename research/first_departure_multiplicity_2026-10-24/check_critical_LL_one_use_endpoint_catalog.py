"""Complete constant-selected-C LL interface allowing one-use endpoint
edges. Fixed typed108 product after critical second-LEFT-V theorem;
all first/second/late physical ranks retained, exterior unfilled.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
check=L['check'];ct=Counter();rs=[]
for B,A,Y in product(['SN','SNN','SSNN','SNNS','SSS','SSSS'],['EE','EEW','EEWW','EWWE','EWE','EWEW'],['EWW','EWWE','EEWW']):
 hs={(0,0):'NNSS',(0,1):Y,(1,0):A,(1,1):B};z=check(hs);ct[z]+=1
 if z=='open':rs.append(dict(B=B,Y=Y,Z='NNSS',A=A))
filtered=[r for r in rs if not(r['Y']in['EWW','EWWE']and r['B']in['SSS','SSSS'])]
assert dict(ct)=={'open':24,'skipped_rank':18,'port':66}and len(filtered)==16
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(ct),local_open=rs,critical_high_sink_rejected=[r for r in rs if r not in filtered],critical_necessary_rows=filtered,critical_necessary_count=16,warning='The high-sink rejection is an analytic extension of signedf59 actual nesting; no other open row is an attained factor/front or full cyclic interface.'),indent=2)+'\n');print('PASS108 local:24open; critical high-sink nesting leaves16, including even one-use portal')
