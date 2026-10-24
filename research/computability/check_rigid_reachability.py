#!/usr/bin/env python3
"""Independent controls for the rigid-complete-state reachability corollary.

This is not a highway solver. The proof is in rigid_reachability.md.
Only the Python standard library is used.
"""
from dataclasses import dataclass
from itertools import product
import json, random

D=((0,1),(1,0),(0,-1),(-1,0))
@dataclass(frozen=True)
class State:
    black: frozenset
    p: tuple
    h: int

def forward(s):
    b=set(s.black); bit=s.p in b
    h=(s.h+(-1 if bit else 1))%4
    b.symmetric_difference_update((s.p,))
    dx,dy=D[h]
    return State(frozenset(b),(s.p[0]+dx,s.p[1]+dy),h)

def backward(s):
    dx,dy=D[s.h]; q=(s.p[0]-dx,s.p[1]-dy)
    h=(s.h+(-1 if q in s.black else 1))%4
    return State(s.black.symmetric_difference((q,)),q,h)

def sector(s):
    return (-1 if (sum(s.p)+(s.h%2))%2 else 1)

def theta(s):
    sig=sector(s)
    field=-sig*sum((-1 if sum(q)%2 else 1)*(3**abs(sum(q))-1) for q in s.black)
    z=sum(s.p); f=3**abs(z)-1; eps=1 if s.h<2 else -1
    head=f//2 if eps*z>=0 else -3*f//2
    return field+head

def rot_point(p,r):
    x,y=p
    for _ in range(r%4): x,y=y,-x
    return x,y

def transform(s,r=0,z=(0,0)):
    def point(p):
        a,b=rot_point(p,r); return a+z[0],b+z[1]
    return State(frozenset(point(q) for q in s.black),point(s.p),(s.h+r)%4)

def shift_candidates(x,y):
    mass=len(x.black)+len(y.black)
    lo=[]; hi=[]
    for j in range(2):
        a=2*(y.p[j]-x.p[j])-D[y.h][j]+D[x.h][j]
        lo.append(-((mass+a)//2)) # ceil((-mass-a)/2)
        hi.append((mass-a)//2)
    return product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1))

def full_offset(x,y):
    """Return the unique signed orbit time, or None. Always halts."""
    if x==y: return 0
    if sector(x)!=sector(y): return None
    gap=theta(y)-theta(x)
    if gap==0:return None
    if gap<0:
        ans=full_offset(y,x)
        return None if ans is None else -ans
    z=x
    for t in range(1,gap+1):
        z=forward(z)
        if z==y:return t
    return None

def rigid_offset(x,y):
    """Return (t,r,z) iff F^t x = translation_z rotation_r y."""
    for r in range(4):
        yr=transform(y,r)
        for z in shift_candidates(x,yr):
            ans=full_offset(x,transform(yr,z=z))
            if ans is not None:return ans,r,z
    return None

def main():
    rng=random.Random(20261022)
    checked=0; candidate_checked=0; offset_checked=0
    for _ in range(120):
        pts=[(x,y) for x in range(-2,3) for y in range(-2,3)]
        s=State(frozenset(rng.sample(pts,rng.randrange(7))),
                (rng.randrange(-2,3),rng.randrange(-2,3)),rng.randrange(4))
        initial=s
        for t in range(1,61):
            old=s;s=forward(s)
            assert backward(s)==old
            z=sum(old.p); f=3**abs(z)-1
            e=1 if old.h<2 else -1; ep=1 if s.h<2 else -1
            expected=1+4*f*int(ep!=e and e*z<0)
            assert theta(s)-theta(old)==expected
            checked+=1
            r=rng.randrange(4); v=(rng.randrange(-20,21),rng.randrange(-20,21))
            target=transform(s,r,v)
            # Invert the target's rotation and translation to recover actual s.
            yr=transform(target,(-r)%4)
            zv=rot_point((-v[0],-v[1]),(-r)%4)
            assert transform(yr,z=zv)==s
            assert zv in set(shift_candidates(initial,yr))
            candidate_checked+=1
        # Exact offsets on actual modest examples, not all rigid candidates.
        s=initial
        for t in range(9):
            assert full_offset(initial,s)==t
            assert full_offset(s,initial)==-t
            offset_checked+=2
            s=forward(s)
    blank=State(frozenset(),(0,0),0)
    s=blank
    rigid=[]
    for t in range(5):
        moved=transform(s,(t+1)%4,(9,-7))
        ans=rigid_offset(blank,moved)
        assert ans is not None
        tt,r,z=ans
        dest=transform(moved,r,z)
        actual=blank
        for _ in range(abs(tt)):
            actual=forward(actual) if tt>=0 else backward(actual)
        assert actual==dest
        rigid.append({'known_time':t,'returned_time':tt,'rotation':r,'shift':z})
        s=forward(s)
    result={'status':'finite implementation controls passed; analytic proof separate',
            'clock_and_inverse_checks':checked,
            'all_time_translation_candidate_checks':candidate_checked,
            'exact_signed_offset_checks':offset_checked,'rigid_examples':rigid}
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
