#!/usr/bin/env python3
"""Fresh literal controls and exact infinite-tail oracle; no author engine imports."""
import json, random, hashlib
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
G={(0,-1),(1,1),(1,3),(2,2)}
BASE=Path(__file__).resolve().parent

def add(p,q): return (p[0]+q[0],p[1]+q[1])
def scale(n,p): return (n*p[0],n*p[1])
def step(B,p,h):
    h=(h+(-1 if p in B else 1))%4
    if p in B: B.remove(p)
    else: B.add(p)
    return add(p,D[h]),h

def invstate(B,p,h): return set(B),add(p,scale(-1,D[h])),(h+2)%4

def sigma(p,h): return (-1 if (p[0]+p[1])%2 else 1)*(1 if h%2==0 else -1)
def rotpoint(p,r):
    x,y=p
    for _ in range(r%4): x,y=y,-x
    return x,y

def gate(e,h): return {add(e,rotpoint(p,h-1)) for p in G}
def trace(B,p,h,n):
    B=set(B); reads=[]; word=''
    for _ in range(n):
        reads.append(p); word+='L' if p in B else 'R'
        p,h=step(B,p,h)
    return B,p,h,word,reads

def exact_period(B,p,h,w):
    q=[]; hh=h; pp=p
    for a in w:
        q.append(pp); hh=(hh+(-1 if a=='L' else 1))%4; pp=add(pp,D[hh])
    if hh!=h: return False
    d=(pp[0]-p[0],pp[1]-p[1])
    if d==(0,0): return False
    def mult(v):
        m=None
        for a,b in zip(v,d):
            if b:
                if a%b: return None
                z=a//b
                if m is not None and m!=z:return None
                m=z
            elif a:return None
        return m
    for i,qi in enumerate(q):
        earlier=[]; zero=0; hits=set(); cuts={0}
        for j,qj in enumerate(q):
            m=mult((qj[0]-qi[0],qj[1]-qi[1]))
            if m is not None:
                if m>0: earlier.append(m);cuts.add(m)
                elif m==0 and j<i:zero^=1
        for b in B:
            k=mult((b[0]-qi[0],b[1]-qi[1]))
            if k is not None and k>=0:hits.add(k);cuts.update((k,k+1))
        for k in cuts:
            color=(k in hits)^bool(zero)^bool(sum(m<=k for m in earlier)%2)
            if color!=(w[i]=='L'):return False
    return True

BB,pp,hh,trans,gr=trace(G,(0,0),1,182)
BT,pt,ht,W,qr=trace(BB,pp,hh,104)
assert pp==(5,1) and hh==1 and len(BB)==36
assert pt==(7,3) and ht==1 and exact_period(BB,pp,hh,W)
assert min(x for x,y in gr+qr)==0 and min(y for x,y in gr+qr)==-2
assert all(x>=0 and y>=-2 for x,y in G)
source_standard=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text())
# Bind retained word without assuming a particular source JSON shape.
assert W in json.dumps(source_standard)

def quadrant_port(e,g,k):
    assert (k-g)%4 in (1,3)
    w='LRLR' if k==(g-1)%4 else 'RLRLR'
    p=e;h=g;B=set();reads=[]
    for a in w:
        assert p not in reads
        reads.append(p)
        if a=='L':B.add(p)
        h=(h+(-1 if a=='L' else 1))%4;p=add(p,D[h])
    gg=gate(p,h)
    assert not gg.intersection(reads)
    assert len(B)==2 and len(gg)==4
    return B|gg,w,p,h

def inquad(q,e,g,k):
    r=(q[0]-e[0],q[1]-e[1])
    return sum(a*b for a,b in zip(r,D[g]))>=0 and sum(a*b for a,b in zip(r,D[k]))>=0

def tangents(e1,g1,e2,g2):
    if g2==g1:
        l=D[(g1-1)%4]
        diff=sum((b-a)*c for a,b,c in zip(e1,e2,l))
        assert diff
        return ((g1+1)%4,(g2-1)%4) if diff>0 else ((g1-1)%4,(g2+1)%4)
    if g2==(g1+2)%4: return (g1-1)%4,(g2-1)%4
    return (g2+2)%4,(g1+2)%4

def intervals(e,g,k):
    out=[]
    for a in range(2):
        v=D[g][a]+D[k][a]
        out.append((e[a],None) if v==1 else (None,e[a]))
    return out

def disjoint(e1,g1,k1,e2,g2,k2):
    for (l1,u1),(l2,u2) in zip(intervals(e1,g1,k1),intervals(e2,g2,k2)):
        if u1 is not None and l2 is not None and u1<l2:return True
        if u2 is not None and l1 is not None and u2<l1:return True
    return False

def qexit(B,p,h,R):
    B=set(B);t=0
    while max(abs(p[0]),abs(p[1]))<=R:
        p,h=step(B,p,h);t+=1
        if t>2000000:raise AssertionError('Control budget exceeded, not a theorem failure')
    return B,p,h,t

ports=0
for g in range(4):
    for k in ((g-1)%4,(g+1)%4):
        e=(13,-7);B,w,p,h=quadrant_port(e,g,k)
        C,p2,h2,ww,reads=trace(B,e,g,len(w)+182)
        assert ww.startswith(w)
        std=''
        CC,ppp,hhh,std,tailreads=trace(C,p2,h2,104)
        assert std==W and exact_period(C,p2,h2,std)
        assert all(inquad(q,e,g,k) for q in list(B)+reads+tailreads)
        dd=(ppp[0]-p2[0],ppp[1]-p2[1])
        assert dd==scale(2,add(D[g],D[k]))
        ports+=1

pair_cases=0; opposite_sector_cases=0; literal_pairs=0
for R in range(0,7):
    exits=[]
    for v in range(-R,R+1):
        exits.extend([((R+1,v),1),((-R-1,v),3),((v,R+1),0),((v,-R-1),2)])
    for i,(e1,g1) in enumerate(exits):
        for e2,g2 in exits[i+1:]:
            k1,k2=tangents(e1,g1,e2,g2)
            assert disjoint(e1,g1,k1,e2,g2,k2)
            pair_cases+=1
            if sigma(e1,g1)!=sigma(e2,g2):opposite_sector_cases+=1
            # Literal pair run on the tight R<=1 boundary, including every corner.
            if R<=1:
                B1,w1,p1,h1=quadrant_port(e1,g1,k1)
                B2,w2,p2,h2=quadrant_port(e2,g2,k2)
                assert len(B1|B2)==12
                for e,g,k,w in ((e1,g1,k1,w1),(e2,g2,k2,w2)):
                    C,p,h,ww,reads=trace(B1|B2,e,g,len(w)+182)
                    assert ww.startswith(w) and all(inquad(q,e,g,k) for q in reads)
                    _,_,_,ww2,rr=trace(C,p,h,104)
                    assert ww2==W and exact_period(C,p,h,W)
                    assert all(inquad(q,e,g,k) for q in rr)
                literal_pairs+=1

rng=random.Random(2026102310)
fullcases=0;maxexit=0
seeds=[set(),{(0,0)},{(1,0),(0,1)},G]
for _ in range(80):
    pool=[(x,y) for x in range(-3,4) for y in range(-3,4)]
    seeds.append(set(rng.sample(pool,rng.randrange(21))))
for i,B in enumerate(seeds):
    p=(0,0);h=i%4;R=4+i%3
    IB,ip,ih=invstate(B,p,h)
    C1,e1,g1,t1=qexit(B,p,h,R)
    C2,e2,g2,t2=qexit(IB,ip,ih,R)
    assert e1!=e2 and sigma(e1,g1)!=sigma(e2,g2)
    k1,k2=tangents(e1,g1,e2,g2)
    P1,w1,_,_=quadrant_port(e1,g1,k1)
    P2,w2,_,_=quadrant_port(e2,g2,k2)
    E=P1|P2
    assert len(E)==12 and not (E&B) and all(max(abs(x),abs(y))>R for x,y in E)
    assert disjoint(e1,g1,k1,e2,g2,k2)
    for startp,starth,e,g,t,w in ((p,h,e1,g1,t1,w1),(ip,ih,e2,g2,t2,w2)):
        U,up,uh,uw,ur=trace(B,startp,starth,t)
        V,vp,vh,vw,vr=trace(B|E,startp,starth,t)
        assert (up,uh,uw,ur)==(vp,vh,vw,vr) and U^V==E
        C,pp,hh,ww,rr=trace(V,vp,vh,len(w)+182)
        assert ww.startswith(w) and exact_period(C,pp,hh,W)
    fullcases+=1;maxexit=max(maxexit,t1,t2)

proof=BASE/'two_sided_quadrant_completion.md'
report={'status':'PASS','scope':'Exact gate-tail and finite controls; all-square routing proof is analytic',
        'gate_seed_count':4,'gate_entry':182,'gate_entry_mass':len(BB),
        'gate_read_minimum':[min(x for x,y in gr+qr),min(y for x,y in gr+qr)],
        'standard_word':W,'quadrant_ports':ports,'boundary_pair_controls':pair_cases,
        'opposite_sector_boundary_pairs':opposite_sector_cases,'literal_tight_pairs':literal_pairs,
        'full_original_seed_controls':fullcases,'maximum_control_first_exit':maxexit,
        'added_black_count_each_full_control':12,
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}
(BASE/'check_two_sided_quadrant_completion.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
