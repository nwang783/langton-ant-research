"""Deterministic verification of the explicit examples, not a proof by search."""
from math import isqrt
D=((1,0),(0,1),(-1,0),(0,-1))

def signed_turns(path):
    headings=[]
    for (x,y),(u,v) in zip(path,path[1:]):
        headings.append(D.index((u-x,v-y)))
    ccw=0
    for a,b in zip(headings,headings[1:]):
        d=(b-a)%4
        assert d!=2
        ccw += (d==1)-(d==3)
    return ccw

def spiral(q):
    p=[(0,0)]
    for j in range(1,q+1):
        dx,dy=D[(j-1)%4]
        for _ in range((j+1)//2):
            x,y=p[-1];p.append((x+dx,y+dy))
    return p

def crossing_chain(m):
    # Each clockwise unit square is followed by N1,E3 to the next base.
    p=[(0,0)]
    for i in range(m):
        for d in (0,3,2,1):
            x,y=p[-1];dx,dy=D[d];p.append((x+dx,y+dy))
        if i+1<m:
            for d in (1,0,0,0):
                x,y=p[-1];dx,dy=D[d];p.append((x+dx,y+dy))
    return p

for q in (1,2,3,4,7,20,100,1000):
    p=spiral(q)
    n=len(p)-1
    formula=((q+1)*(q+1))//4
    assert n==formula,(q,n,formula)
    assert len(set(p))==len(p)
    assert signed_turns(p)==q-1
    print(f'spiral q={q}: n={n}, CCW imbalance={q-1}, vertices distinct')
for m in (1,2,3,10,100):
    p=crossing_chain(m)
    edges=[tuple(sorted((u,v))) for u,v in zip(p,p[1:])]
    assert len(edges)==len(set(edges))
    assert len(p)-1==8*m-4
    assert signed_turns(p)==-(4*m-1)
    print(f'crossing chain m={m}: n={len(p)-1}, CW imbalance={4*m-1}, edges distinct')
