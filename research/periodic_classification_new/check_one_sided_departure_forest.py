#!/usr/bin/env python3
"""Finite literal controls, not a bound on nested cycles or trajectory length."""
from pathlib import Path
from collections import Counter
import random,json
ROOT=Path(__file__).parent;DIR=((0,1),(1,0),(0,-1),(-1,0))
def in_closed_polygon(p,cyc):
    if p in cyc:return True
    x,y=p;inside=False
    for (x1,y1),(x2,y2) in zip(cyc,cyc[1:]+cyc[:1]):
        if (y1>y)!=(y2>y) and x < x1+(y-y1)*(x2-x1)/(y2-y1):inside=not inside
    return inside

def test(seed,steps=4000):
    initial=set(seed);black=set(seed);p=(0,0);h=0;first={};edge={}
    for t in range(steps):
        color=p in black;new=p not in first
        if new:first[p]=(t,h)
        if color:black.remove(p)
        else:black.add(p)
        hh=(h+(-1 if color else 1))%4;q=p[0]+DIR[hh][0],p[1]+DIR[hh][1]
        if new and p not in initial:edge[p]=q
        p,h=q,hh
    all_edges=edge.copy()
    edge={u:v for u,v in edge.items() if v in edge}
    seen=set();cycles=[]
    for v in edge:
        if v in seen:continue
        path=[];at={};u=v
        while u in edge and u not in seen and u not in at:
            at[u]=len(path);path.append(u);u=edge[u]
        if u in at:cycles.append(path[at[u]:])
        seen.update(path)
    for cyc in cycles:
        assert len(cyc)==4 and (0,0) in cyc
        assert sorted(first[v][0] for v in cyc)==[0,1,2,3]
        area2=sum(x1*y2-y1*x2 for (x1,y1),(x2,y2) in zip(cyc,cyc[1:]+cyc[:1]))
        assert area2<0 and in_closed_polygon((0,0),cyc)
        Q=L=0
        for i,v in enumerate(cyc):
            u=cyc[i-1];w=cyc[(i+1)%len(cyc)]
            incoming=DIR.index((v[0]-u[0],v[1]-u[1]));outgoing=DIR.index((w[0]-v[0],w[1]-v[1]));turn=(outgoing-incoming)%4
            Tv,I=first[v];Tu=first[u][0];q,r=divmod(Tu+1-Tv,4);assert r==0
            if turn==1:
                assert incoming==I and(q>=0 if v==(0,0) else q==0)
            else:
                assert turn==3 and incoming==(I+2)%4 and q>=1;L+=1
            Q+=q
        assert len(cyc)==4*Q
    for i,A in enumerate(cycles):
        for B in cycles[i+1:]:
            assert not(set(A)&set(B))
            assert in_closed_polygon(A[0],B) or in_closed_polygon(B[0],A)
    # Resolve every finite-prefix orbit with iterative memoization. Only the
    # final four first-read times can legitimately have an open target.
    fate={v:('black',v) for v in initial if v in first}
    for cyc in cycles:
        for v in cyc:fate[v]=('initial_cycle',min(cyc))
    for start in all_edges:
        if start in fate:continue
        path=[];at=set();u=start
        while u not in fate and u in all_edges and u not in at:
            at.add(u);path.append(u);u=all_edges[u]
        assert u not in at
        value=fate.get(u,('open',u))
        for v in path:fate[v]=value
    for v,(t,h) in first.items():
        if v not in initial and t<=steps-5:assert fate[v][0]!='open'
    roots={fate[v] for v,(t,h) in first.items() if v not in initial and t<=steps-5}
    assert len(roots)<=len(initial)+1
    return cycles
rng=random.Random(20261023);stats=Counter();best=[];count=0
for z in range(240):
    mass=z%9;seed=set(rng.sample([(x,y)for x in range(-3,4)for y in range(-3,4)],mass))
    cyc=test(seed);stats[len(cyc)]+=1;count+=len(cyc)
    if len(cyc)>len(best):best=cyc;best_seed=sorted(seed)
result=dict(status='AUTHOR_FINITE_LITERAL_WHITE_DEPARTURE_FOREST_CONTROLS_PASS',scope=__doc__,boards=240,steps_each=4000,total_cycles=count,cycle_count_distribution=dict(sorted(stats.items())),largest_observed_nested_count=len(best),largest_example_seed=best_seed,largest_example_cycles=best)
(ROOT/'one_sided_departure_forest_controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
