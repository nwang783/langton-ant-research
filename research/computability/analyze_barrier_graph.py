#!/usr/bin/env python3
"""Exploration of finite driven-barrier graphs. No all-height inference."""
from pathlib import Path
import sys,json
from collections import deque,Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'frontier_exploration'))
from certify_blank_strip_barrier import pair_visit

def analyze(H,W):
    queue=deque([0]);idx={0:0};masks=[0];edges=[];right=[];maxdepth=0
    while queue:
        m=queue.popleft();es=[]
        for y in range(1,H,2):
            side,n,z,t=pair_visit(m,W,H,y)
            if side=='right':right.append((idx[m],y))
            if side=='left':
                if n not in idx:idx[n]=len(masks);masks.append(n);queue.append(n)
                es.append(idx[n])
        edges.append(es)
    indeg=[0]*len(masks)
    for es in edges:
        for j in es:indeg[j]+=1
    q=deque(i for i,d in enumerate(indeg) if not d);order=[];depth=[0]*len(masks)
    while q:
        i=q.popleft();order.append(i)
        for j in edges[i]:
            depth[j]=max(depth[j],depth[i]+1);indeg[j]-=1
            if not indeg[j]:q.append(j)
    return dict(H=H,W=W,states=len(masks),left_edges=sum(map(len,edges)),right_edges=len(right),acyclic=len(order)==len(masks),dag_processed=len(order),max_return_count=max(depth) if len(order)==len(masks) else None,black_counts=sorted(Counter(m.bit_count() for m in masks).items()))
if __name__=='__main__':
    out=[analyze(H,W) for H,W in [(2,1),(3,1),(4,3),(5,3),(6,5),(7,6),(8,8)]]
    print(json.dumps(out,indent=2))
