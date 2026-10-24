#!/usr/bin/env python3
"""Nonvacuous literal standard fronts for the optional departure monitor."""
from pathlib import Path
from collections import defaultdict
import json
from frontier_drift_geometry import Geometry
from first_departure_backbone_frontier import transition
ROOT=Path(__file__).parent
WORD=(ROOT.parent/'word_stabilization/standard_word.txt').read_text().strip()
DIR=((0,1),(1,0),(0,-1),(-1,0));out=[]
for copies in (1,2,3):
    P=104*copies;a=2*copies
    for sign in (1,-1):
        b=sign*a;g=Geometry(a,b);p,h=((-1,0),0) if sign==1 else((0,0),1)
        start=p;hist=defaultdict(list)
        for t,ch in enumerate(WORD*copies):
            assert h%2==1-(sum(p)%2)
            k=p[0]//a;v=p[0]-k*a,p[1]-k*b
            hist[v].append((t-k*P,h,ch));h=(h+(1 if ch=='R' else-1))%4
            p=p[0]+DIR[h][0],p[1]+DIR[h][1]
        assert p==(start[0]+a,start[1]+b)
        lo=min(y-g.base[x] for x,y in hist);hi=max(y-g.base[x] for x,y in hist)
        rows={}
        for r in range(lo-1,hi+2):
            rows[r]=[]
            for c in range(a):
                es=sorted(hist[c,g.base[c]+r]);hs=tuple(h for t,h,ch in es)
                assert all(ch==('R' if j%2==0 else'L') for j,(t,h,ch) in enumerate(es))
                assert all(h%2==1-g.parity(r%2,c) for h in hs)
                rows[r].append({'h':hs})
        for S in (16,64,120,512):
            state=();rank=0;counter=min(S,2*a);increments=[];nonempty=0
            for r in range(lo-1,hi+1):
                state,z,inc,why=transition(state,rows[r],rows[r+1],r%2,g,S)
                assert why is None,(copies,sign,S,r,why)
                rank=max(rank,z);counter=min(S,counter+inc)
                if inc:increments.append(inc)
                nonempty+=bool(state)
            assert state==() and nonempty>0
            assert rank==min(S,12*copies)
            assert counter==min(S,20*copies)
            out.append(dict(period=P,full_drift=[a,b],saturation=S,
                            rank_period_lower=rank,cumulative_counterflow_lower=counter,
                            nonempty_frontiers=nonempty,cycle_increments=increments,status='PASS'))
result=dict(status='AUTHOR_FIRST_DEPARTURE_FRONTIER_POSITIVES_PASS',controls=out)
(ROOT/'first_departure_frontier_positive.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
