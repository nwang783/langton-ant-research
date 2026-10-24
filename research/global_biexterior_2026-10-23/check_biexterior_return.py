"""Literal controls for a proposed all-word simultaneous-white-exterior lemma.
No imports from existing ant implementations. Finite checks are not the proof.
"""
from collections import deque
from itertools import combinations
from pathlib import Path
import json, random

OUT=Path(__file__).parent
DIR=((0,1),(1,0),(0,-1),(-1,0))

def rot(v,h):
    x,y=v
    for _ in range(h): x,y=y,-x
    return x,y

def cursors(p,h):
    a=rot((-1,-1),h); b=rot((1,-1),h)
    return ((2*p[0]+a[0],2*p[1]+a[1]),(2*p[0]+b[0],2*p[1]+b[1]))

def white_infinite(B,v):
    if not B:return True
    loX=2*min(x for x,y in B)-1; hiX=2*max(x for x,y in B)+1
    loY=2*min(y for x,y in B)-1; hiY=2*max(y for x,y in B)+1
    seen={v}; todo=deque([v])
    while todo:
        x,y=todo.popleft()
        if not(loX<=x<=hiX and loY<=y<=hiY):return True
        for dx,dy in ((2,2),(2,-2),(-2,2),(-2,-2)):
            q=(x+dx,y+dy)
            assert (2*x+dx)%4==0 and (2*y+dy)%4==0
            cell=((2*x+dx)//4,(2*y+dy)//4)
            if cell not in B and q not in seen:seen.add(q);todo.append(q)
    return False

def exterior(B,p,h):
    z,w=cursors(p,h)
    return white_infinite(B,z),white_infinite(B,w)

def gap(a,b):
    return max(0,a[0]-b[1],b[0]-a[1])

def rect_dist(a,b):
    return max(gap(a[:2],b[:2]),gap(a[2:4],b[2:4]))

def closure(B):
    rs=[(x,x,y,y,1) for x,y in sorted(B)]
    while True:
        pair=next(((i,j) for i in range(len(rs)) for j in range(i+1,len(rs)) if rect_dist(rs[i],rs[j])<=1),None)
        if pair is None:break
        i,j=pair;a,b=rs[i],rs[j]
        c=(min(a[0],b[0]),max(a[1],b[1]),min(a[2],b[2]),max(a[3],b[3]),a[4]+b[4])
        rs=[r for k,r in enumerate(rs) if k not in (i,j)]+[c]
    for a in rs:
        assert a[1]-a[0]+1+a[3]-a[2]+1<=2*a[4]
        assert sum(1 for x,y in B if a[0]<=x<=a[1] and a[2]<=y<=a[3])==a[4]
    assert all(rect_dist(a,b)>=2 for i,a in enumerate(rs) for b in rs[i+1:])
    return rs

def inside(p,r):return r[0]<=p[0]<=r[1] and r[2]<=p[1]<=r[3]

def step(B,p,h):
    h=(h+(-1 if p in B else 1))%4
    if p in B:B.remove(p)
    else:B.add(p)
    dx,dy=DIR[h]
    return (p[0]+dx,p[1]+dy),h

def first_return(B0,p0,h0,limit=50000):
    B=set(B0); p=p0; h=h0;m=len(B)
    rs=closure(B)
    ext=exterior(B,p,h)
    if all(ext):return 0,0,None
    matches=[r for r in rs if inside(p,r)]
    assert len(matches)==1,(B,p,h,ext,rs)
    r=matches[0]; k=r[4];area=(r[1]-r[0]+1)*(r[3]-r[2]+1)
    rad=(r[1]-r[0]+r[3]-r[2]+1)//2
    # ceil((width+height-2)/2)
    assert rad<=k-1
    bound=(area+2)*(3**rad-1)+1
    outside0={q for q in B if not inside(q,r)}
    for t in range(1,min(limit,bound)+1):
        assert inside(p,r),(t,B,p,h,r)
        p,h=step(B,p,h)
        assert {q for q in B if not inside(q,r)}==outside0
        assert len(B)<=m-k+area<=m*m
        assert abs(p[0]-p0[0])+abs(p[1]-p0[1])<=2*k-1
        ext=exterior(B,p,h)
        if all(ext):return t,len(B),r
    raise AssertionError(('return limit reached',len(B0),bound,limit,p,h))

def main():
    counts={'pose_exterior_tests':0,'nonexterior_starts':0,'returns':0,'max_delay':0,'max_return_mass':0}
    witnesses=[]
    # All masks on a 3x3 block, all nearby physical cells, all headings.
    cells=[(x,y) for x in range(-1,2) for y in range(-1,2)]
    for mask in range(1<<len(cells)):
        B={q for i,q in enumerate(cells) if mask>>i&1};rs=closure(B)
        for p in cells:
            for h in range(4):
                ez,ew=exterior(B,p,h);counts['pose_exterior_tests']+=1
                if not (ez and ew):
                    counts['nonexterior_starts']+=1
                    assert any(inside(p,r) for r in rs)
                    t,mm,r=first_return(B,p,h)
                    counts['returns']+=1;counts['max_delay']=max(counts['max_delay'],t);counts['max_return_mass']=max(counts['max_return_mass'],mm)
                    if len(witnesses)<8:witnesses.append({'B':sorted(B),'p':p,'h':h,'exterior':(ez,ew),'delay':t,'mass':mm,'rectangle':r})
    rng=random.Random(20261023)
    # Independent, spatially separated clusters: verify the external test and
    # fixed rectangle confinement on random states as well as a full blank orbit.
    for _ in range(100):
        B={(rng.randrange(-4,5),rng.randrange(-4,5)) for _ in range(24)}
        B|={(100+x,-100+y) for x,y in list(B)[:5]}
        p=(rng.randrange(-3,4),rng.randrange(-3,4));h=rng.randrange(4)
        rs=closure(B);ext=exterior(B,p,h);counts['pose_exterior_tests']+=1
        if not all(ext):
            assert any(inside(p,r) for r in rs)
            t,mm,r=first_return(B,p,h)
            counts['returns']+=1;counts['max_delay']=max(counts['max_delay'],t);counts['max_return_mass']=max(counts['max_return_mass'],mm)
    B=set();p=(0,0);h=0
    observed={'steps':2000,'both_exterior':0,'one_exterior':0,'neither_exterior':0}
    bad_examples=[]
    for t in range(observed['steps']):
        ext=exterior(B,p,h)
        observed['both_exterior' if all(ext) else 'one_exterior' if any(ext) else 'neither_exterior']+=1
        if not all(ext) and len(bad_examples)<12:
            delay,mm,r=first_return(B,p,h)
            bad_examples.append({'t':t,'mass':len(B),'p':p,'h':h,'exterior':ext,'delay':delay,'return_mass':mm,'rectangle':r})
        p,h=step(B,p,h)
    result={'status':'literal controls passed, not an exhaustive all-size proof','counts':counts,'witnesses':witnesses,'blank_observed':observed,'blank_nonexterior_returns':bad_examples}
    (OUT/'biexterior_return_controls.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
