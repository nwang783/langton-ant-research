#!/usr/bin/env python3
"""Literal dual process and exact finite ribbon-boundary cycle diagnostics."""
import json, random
DIR=((1,0),(0,1),(-1,0),(0,-1))
def edge(v,d):
    w=(v[0]+DIR[d][0],v[1]+DIR[d][1]);return tuple(sorted((v,w)))
def perm(dart,B):
    v,d=dart
    if edge(v,d) not in B:
        v=(v[0]+DIR[d][0],v[1]+DIR[d][1]);d=(d+2)%4
    return v,(d+1)%4

def cycle(dart,B):
    out=[];q=dart
    while not out or q!=dart:
        out.append(q);q=perm(q,B)
        if len(out)>8*len(B)+20:raise RuntimeError('unexpected cycle bound')
    return out

def simulate(B,T,samples):
    B=set(B);dart=((0,0),0);out=[]
    for t in range(T+1):
        if t in samples:
            cyc=cycle(dart,B); vs=[v for v,d in cyc]
            out.append(dict(t=t,mass=len(B),cycle_length=len(cyc),box=[min(v[0] for v in vs),max(v[0] for v in vs),min(v[1] for v in vs),max(v[1] for v in vs)],head=dart))
        if t==T:break
        E=edge(*dart);nxt=perm(dart,B)
        if E in B:B.remove(E)
        else:B.add(E)
        dart=nxt
    return out
if __name__=='__main__':
    samples={0,100,1000,10000,12000,20000,50000,100000}
    rng=random.Random(271828)
    seeds=[set()]
    for i in range(5):
        seeds.append({edge((rng.randrange(-5,6),rng.randrange(-5,6)),rng.randrange(4)) for j in range(25)})
    ans=[simulate(B,100000,samples) for B in seeds]
    print(json.dumps(ans,indent=2))
