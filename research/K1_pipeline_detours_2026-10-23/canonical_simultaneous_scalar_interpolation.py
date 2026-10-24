"""One simultaneous scalar interpolation for every canonical WHITE cap-four sheet.
Complete local inventory only; no period, width, drift or front search.
"""
from pathlib import Path
from collections import Counter
import json
r=Path(__file__).parent
base=json.loads((r/'canonical_sheet_two_level_contact_barriers.json').read_text())['checks']
rows=[]
for q in base:
 h=q['headings'];rs=Counter(h[::2]);ls=Counter(h[1::2]);a=-max(rs['E'],rs['W']);C=q['C'];L=q['L'];j=q['j']
 assert C==dict(NE=a+rs['W'],SW=a+rs['E'])
 assert L==dict(NW=a-ls['E'],SE=a-ls['W'])
 assert 4*a==sum(C.values())+sum(L.values())-(len(h)%2)
 assert min(C.values())>=a>=max(L.values())
 for p in q['pairs']:assert p['turn']==('R'if j>a else'L')
 rows.append(dict(headings=h,C=C,L=L,center=a,threshold=[2*j-1,2],canonical_turns=[p['turn']for p in q['pairs']],interpolation_turn='R'if j>a else'L'))
out=dict(scope=__doc__,local_sheets=len(rows),canonical_arcs=sum(len(q['pairs'])for q in base),rows=rows)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(rows),'local sheets and',out['canonical_arcs'],'arcs agree with the one scalar interpolation')
