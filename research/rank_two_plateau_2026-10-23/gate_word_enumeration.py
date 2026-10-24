"""Independent turn-word enumeration for the exact synchronized gate bound.
No target-DFS implementation imported. First two turns RR are fixed; all
other finite input colors are unrestricted but repeated cells must alternate.
"""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json,hashlib
D=((0,1),(1,0),(0,-1),(-1,0));u=(0,0);v=(1,0)
reports=[]
for n in (4,8,12,16):
    candidates=[];gates=[]
    for tail in product((1,-1),repeat=n-2):
        turns=(1,1)+tail;p=u;h=0;seen={};vs=[];trace=[];valid=True
        for t,c in enumerate(turns):
            if seen.get(p)==c:valid=False;break
            seen[p]=c;trace.append(dict(t=t,p=list(p),h=h,turn='R'if c==1 else'L'))
            if p==v:vs.append(dict(t=t,h=h,turn='R'if c==1 else'L'))
            h=(h+c)%4;dd=D[h];p=(p[0]+dd[0],p[1]+dd[1])
            if p==u and t<n-1:valid=False;break
        if not valid or p!=u or h!=2:continue
        word=''.join('R'if c==1 else'L'for c in turns)
        gate=len(vs)==2 and vs[0]==dict(t=1,h=1,turn='R')and vs[1]['h']==3 and vs[1]['turn']=='L'
        row=dict(word=word,v_reads=vs,is_synchronized_gate=gate)
        candidates.append(row)
        if gate:gates.append(dict(**row,trace=trace))
    reports.append(dict(span=n,turn_suffixes_checked=2**(n-2),opposite_first_return_candidates=candidates,gate_count=len(gates),gates=gates))
assert [x['gate_count']for x in reports]==[0,0,0,1]
assert [x['word']for x in reports[2]['opposite_first_return_candidates']]==['RRRLRRLRRLRR','RRLLRLLRLLRL']
assert reports[3]['gates'][0]['word']=='RRLLLLRLRRLRRLRR'
# Independent physical seed replay through source return and target second R.
seed={(-1,-1),(-1,0),(0,-1),(1,-1),(2,-1),(2,0)}
black=set(seed);p=u;h=0;hist=defaultdict(list);seed_trace=[]
for t in range(18):
    c=-1 if p in black else 1
    e=dict(t=t,p=list(p),h=h,turn='R'if c==1 else'L',rank=len(hist[p]));hist[p].append(e);seed_trace.append(e)
    if c==1:black.add(p)
    else:black.remove(p)
    h=(h+c)%4;dd=D[h];p=(p[0]+dd[0],p[1]+dd[1])
assert ''.join(x['turn']for x in seed_trace)=='RRLLLLRLRRLRRLRRLR'
assert [(e['t'],e['h'],e['turn'])for e in hist[u]]==[(0,0,'R'),(16,2,'L')]
assert [(e['t'],e['h'],e['turn'])for e in hist[v]]==[(1,1,'R'),(5,3,'L'),(17,1,'R')]
seed_max_reads=max(map(len,hist.values()))
# Independent blank input control at times 2,3,15,50,51.
black=set();p=u;h=0;hist=defaultdict(list);blank_trace=[]
for t in range(52):
    c=-1 if p in black else 1;out=(h+c)%4
    e=dict(t=t,p=list(p),h=h,out=out,turn='R'if c==1 else'L',rank=len(hist[p]));hist[p].append(e);blank_trace.append(e)
    if c==1:black.add(p)
    else:black.remove(p)
    dd=D[out];p=(p[0]+dd[0],p[1]+dd[1]);h=out
blank_source=hist[1,-1];blank_target=hist[0,-1]
assert [(e['t'],e['h'],e['turn'])for e in blank_source]==[(2,2,'R'),(50,0,'L')]
assert [(e['t'],e['h'],e['turn'])for e in blank_target]==[(3,3,'R'),(15,1,'L'),(51,3,'R')]
res=dict(status='PASS independent exact finite gate table and physical positive controls',scope='The >=16 synchronized gate span is a local exact claim with arbitrary other-cell colors; no front existence or global defect budget asserted.',returns=reports,six_black_control=dict(initial_black=sorted(map(list,seed)),trace=seed_trace,all_cell_prefix_max_reads=seed_max_reads),blank_control=dict(initial_black=[],initial_pose=dict(p=[0,0],h=0),source=blank_source,target=blank_target,trace=blank_trace,prefix_max_reads=max(map(len,hist.values()))))
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(dict(status=res['status'],return_counts=[(x['span'],len(x['opposite_first_return_candidates']),x['gate_count'])for x in reports],minimum_gate_span=16,blank_gate_span=48)))
