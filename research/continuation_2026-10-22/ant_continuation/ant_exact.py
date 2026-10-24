"""Exact finite Langton dynamics and supplied periodic-word certification.

These routines are a mathematical checker, not a bounded-run permanence test.
Coordinates use east=(1,0), north=(0,1), and headings N,E,S,W=0,1,2,3.
"""
from collections import defaultdict

DIRS = ((0,1),(1,0),(0,-1),(-1,0))
P = {(0,-2),(0,-1),(0,0),(1,-1),(2,-1),(2,1),(3,-2),
     (3,1),(4,-2),(4,0),(5,-1),(5,0),(6,0)}
D = {(0,-3),(0,0),(1,-4),(1,-3),(1,-2),(2,-1),
     (2,0),(3,0),(6,-1),(7,-1),(7,0),(8,-1)}
W = 'LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR'
DRIFT = (2,-2)
PHASES = {W[i:]+W[:i]:i for i in range(len(W))}
LEGAL10 = {(W+W)[i:i+10] for i in range(len(W))}

def step(B,p,h):
    if p in B:
        h=(h-1)%4
        B.remove(p)
        letter='L'
    else:
        h=(h+1)%4
        B.add(p)
        letter='R'
    a,b=DIRS[h]
    return (p[0]+a,p[1]+b),h,letter

def inverse_step(B,p,h):
    a,b=DIRS[h]
    q=(p[0]-a,p[1]-b)
    if q in B:
        B.remove(q)
        return q,(h-1)%4,'R'
    B.add(q)
    return q,(h+1)%4,'L'

def plan(word,p=(0,0),h=0):
    points=[]
    heads=[]
    for c in word:
        points.append(p)
        heads.append(h)
        h=(h+(1 if c=='R' else -1))%4
        a,b=DIRS[h]
        p=(p[0]+a,p[1]+b)
    return points,heads,p,h

def multiple(v,d):
    if d==(0,0):
        raise ValueError('zero direction')
    i=0 if d[0] else 1
    if v[i]%d[i]:
        return None
    k=v[i]//d[i]
    return k if (k*d[0],k*d[1])==v else None

def certify_period(B,p,h,word):
    """Prove an entire infinite word from the complete supplied finite field.

    Return a finite exact certificate, or None upon a disproving read.
    At phase i, prior writes are step functions in epoch k. Initial black
    cells contribute single-epoch hits. Checking all breakpoints is complete.
    """
    q,_,end,eh=plan(word,p,h)
    d=(end[0]-p[0],end[1]-p[1])
    if eh!=h or d==(0,0):
        return None
    total=0
    for i,qi in enumerate(q):
        thresholds=[]
        for j,qj in enumerate(q):
            a=multiple((qj[0]-qi[0],qj[1]-qi[1]),d)
            if a is not None and (a>0 or a==0 and j<i):
                thresholds.append(a)
        hits=set()
        for b in B:
            k=multiple((b[0]-qi[0],b[1]-qi[1]),d)
            if k is not None and k>=0:
                hits.add(k)
        breaks={0,*thresholds,*hits,*(k+1 for k in hits)}
        for k in breaks:
            bit=(k in hits)^bool(sum(a<=k for a in thresholds)%2)
            if bit!=(word[i]=='L'):
                return None
        total+=len(breaks)
    return {'period':len(word),'drift':d,'breakpoints':total}

def ray_intersection(a,u,b,v,min_j=0,min_k=0):
    """Whether a+j*u=b+k*v, integer j>=min_j,k>=min_k.

    Used here only for nonzero standard drifts with components +/-2.
    """
    det=u[0]*v[1]-u[1]*v[0]
    w=(b[0]-a[0],b[1]-a[1])
    if det:
        nj=w[0]*v[1]-w[1]*v[0]
        nk=w[0]*u[1]-w[1]*u[0]
        if nj%det or nk%det:
            return False
        return nj//det>=min_j and nk//det>=min_k
    c=multiple(w,u)
    if c is None:
        return False
    ratio=multiple(v,u)
    if ratio==1:
        return True
    if ratio==-1:
        return c>=min_j+min_k
    raise ValueError('parallel ray ratio outside +/-1')

def avoids_old_tail(reads,p,h,word,N):
    """All finite reads and all future reads miss D-k*DRIFT, k>N."""
    for q in reads:
        for b in D:
            k=multiple((b[0]-q[0],b[1]-q[1]),DRIFT)
            if k is not None and k>N:
                return False
    points,_,end,_=plan(word,p,h)
    drift=(end[0]-p[0],end[1]-p[1])
    for q in points:
        for b in D:
            if ray_intersection(q,drift,b,(-2,2),0,N+1):
                return False
    return True

def canonical_source(n,r):
    B=set(P)
    for k in range(1,n+1):
        for x,y in D:
            q=(x-2*k,y+2*k)
            assert q not in B
            B.add(q)
    p=(0,0);h=2
    for i in range(r):
        p,h,c=step(B,p,h)
        assert c==W[i]
    return B,p,h

def first_read_seed(word,p=(0,0),h=0):
    points,_,_,_=plan(word,p,h)
    last={};B=set()
    for q,c in zip(points,word):
        if q in last and last[q]==c:
            return None
        if q not in last and c=='L':
            B.add(q)
        last[q]=c
    return B
