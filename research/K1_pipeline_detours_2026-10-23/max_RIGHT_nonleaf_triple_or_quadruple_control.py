"""Complete local physical ports and middle-sheet repair for nonleaf stock holes.
No front, drift, period or radius scan; all thirty E/W WHITE histories.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
H='NESW'
def local(h):
    # E/W incoming phase. Normalize the higher C height to zero.
    rs=Counter(h[::2]);a=-max(rs['E'],rs['W'])
    C={'E':rs['E']+a,'W':rs['W']+a,'N':rs['W']+a,'S':rs['E']+a}
    out=[H[(H.index(x)+(1 if i%2==0 else -1))%4] for i,x in enumerate(h)]
    ic=Counter();oc=Counter();e=[]
    for i,(x,y) in enumerate(zip(h,out)):
        ic[x]+=1;oc[y]+=1
        e.append(dict(rank=i,incoming=x,outgoing=y,in_ordinal=ic[x],out_ordinal=oc[y],in_label=C[x]-ic[x]+1,out_label=C[y]-oc[y]+1))
    assert all(e[i]['in_label']==e[i]['out_label'] for i in range(len(h)) if i not in (1,2) or len(h)<3)
    if len(h)>=3:assert e[1]['in_label']==e[2]['out_label'] and e[2]['in_label']==e[1]['out_label']
    return dict(headings=h,inputs=dict(Counter(h)),outputs=dict(Counter(out)),events=e)
rows=[local(''.join(h)) for n in range(1,5) for h in product('EW',repeat=n)]
right=[];triple=[]
for r in rows:
    h=r['headings'];e=r['events'];ins=r['inputs'];outs=r['outputs']
    if len(h)>=3 and h[0]==h[2]:
        incoming=[x for x,n in ins.items() if n>=3]
        outgoing=[x for x,n in outs.items() if n>=3]
        assert len(incoming)+len(outgoing)>=1
        mid_in=next(q for q in e if q['in_label']==-1)
        mid_out=next(q for q in e if q['out_label']==-1)
        assert {mid_in['rank'],mid_out['rank']}=={1,2}
        high_ports=[('in',x,ins[x]) for x in incoming]+[('out',x,outs[x]) for x in outgoing]
        assert any((mid_in['incoming']==x and mid_in['in_ordinal']==2) if side=='in' else (mid_out['outgoing']==x and mid_out['out_ordinal']==2) for side,x,n in high_ports)
        right.append(dict(headings=h,middle_in_rank=mid_in['rank'],middle_out_rank=mid_out['rank'],high_ports=high_ports))
    it=[x for x,n in ins.items() if n==3];ot=[x for x,n in outs.items() if n==3]
    if it or ot:
        assert (len(it),len(ot)) in ((1,0),(0,1),(1,1))
        # Every triple input/output ordinal two belongs to level -1.
        ei=next((q for q in e if it and q['incoming']==it[0] and q['in_ordinal']==2),None)
        eo=next((q for q in e if ot and q['outgoing']==ot[0] and q['out_ordinal']==2),None)
        if ei:assert ei['in_label']==-1 and ei['rank'] in (1,2)
        if eo:assert eo['out_label']==-1 and eo['rank'] in (1,2)
        if ei and eo:assert ei['rank']!=eo['rank']
        else:assert len(h)==3 and h[0]==h[2]
        triple.append(dict(headings=h,type='internal' if ei and eo else 'source' if eo else 'sink',incoming_middle_rank=ei['rank'] if ei else None,outgoing_middle_rank=eo['rank'] if eo else None))
assert len(right)==12 and len(triple)==12
# A flow-four edge has source EWEW departing S and target SSSS.
s=local('EWEW')['events'];target=[];ic=Counter();oc=Counter();C={'S':0,'N':-2,'W':0,'E':-2}
for i,x in enumerate('SSSS'):
    y=H[(H.index(x)+(1 if i%2==0 else -1))%4];ic[x]+=1;oc[y]+=1
    target.append(dict(rank=i,incoming=x,outgoing=y,in_ordinal=ic[x],out_ordinal=oc[y],in_label=C[x]-ic[x]+1,out_label=C[y]-oc[y]+1))
for i in range(4):assert s[i]['out_label']==target[i]['in_label']==-i
assert s[1]['out_label']==target[2]['out_label']==-1
assert s[2]['out_label']==target[1]['out_label']==-2
assert s[2]['in_label']==s[1]['out_label'] and target[1]['in_label']==target[2]['out_label']
assert s[1]['in_label']==s[2]['out_label'] and target[2]['in_label']==target[1]['out_label']
p=Path(__file__).with_suffix('.json')
p.write_text(json.dumps(dict(scope=__doc__,right_count=len(right),right_rows=right,triple_rows=triple,quadruple=dict(source=s,target=target,upper_sheet=-1,lower_sheet=-2,exchange_edges='two distinct parallel graph edges')),indent=2)+'\n')
print('PASS',len(rows),'complete rows;',len(right),'max-RIGHT rows;',len(triple),'triple-path rows; flow-four parallel pair')
