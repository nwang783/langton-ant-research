#!/usr/bin/env python3
"""Literal finite controls. The proof is the charge and hull argument."""
from collections import Counter
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def delta4(x): return min(x%4,(-x)%4)
def rowG(y,h,r):
    if y<r: return 0
    if y>r: return 2
    k=-((-1)**r)
    return (0,k,2,-k)[h]
def colF(x,h,c):
    if x<c: return 0
    if x>c: return 2
    k=-((-1)**c)
    return (k,0,-k,2)[h]
def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(P):
    P=sorted(set(P)); low=[]; up=[]
    for q in P:
        while len(low)>1 and cross(low[-2],low[-1],q)<=0: low.pop()
        low.append(q)
    for q in reversed(P):
        while len(up)>1 and cross(up[-2],up[-1],q)<=0: up.pop()
        up.append(q)
    return low[:-1]+up[:-1]
def inside(P,p):
    H=hull(P)
    return len(H)>=3 and all(cross(H[i],H[(i+1)%len(H)],p)>=0 for i in range(len(H)))
seeds=[set(),{(0,0)},{(1,1),(-2,0),(0,-2)},
       {(x,y) for x in range(-3,4) for y in range(-2,3) if (x*x+3*y)%5<2}]
checks=0; return_checks=0
for B0 in seeds:
    B=set(B0); x=y=0; h=3; old={}
    for t in range(4001):
        if t%37==0:
            for n in range(1,6):
                a,b=-30,-30; w=2*n+1; z=4*n+1
                F={(a,b),(a+w,b),(a,b+z),(a+w,b+z)}
                assert B0.isdisjoint(F)
                A=B0|F; E=B^A
                assert len(E)>=max(abs(2*x-D[h][0]+D[3][0]),abs(2*y-D[h][1]+D[3][1]))
                R=Counter(); C=Counter()
                for px,py in E:
                    v=1 if (px,py) in B else -1
                    R[py]+=v*((-1)**px); C[px]+=v*((-1)**py)
                for r in range(min(0,y)-1,max(0,y)+2):
                    diff=rowG(y,h,r)-rowG(0,3,r)
                    assert (R[r]-diff)%4==0
                    assert sum(py==r for px,py in E)>=delta4(diff)
                for c in range(min(0,x)-1,max(0,x)+2):
                    diff=colF(x,h,c)-colF(0,3,c)
                    assert (C[c]-diff)%4==0
                    assert sum(px==c for px,py in E)>=delta4(diff)
                checks+=1
        pose=x,y,h
        if pose in old and return_checks<300:
            t0,Bstart=old[pose]
            F={(100,100),(101,100),(100,101),(101,101)}
            assert Bstart.isdisjoint(F)
            A=Bstart|F; E=B^A
            assert len(E)>=4
            assert inside(F|E,(x,y))
            # The stronger retained closed-pose identity itself.
            assert inside(B^Bstart,(x,y))
            return_checks+=1
        else: old[pose]=(t,set(B))
        q=(x,y); black=q in B
        B.symmetric_difference_update({q}); h=(h+(-1 if black else 1))%4
        dx,dy=D[h]; x+=dx; y+=dy
result={'status':'PASS','comparison_cases':checks,'closed_pose_companion_cases':return_checks,
        'trajectories':len(seeds),'updates_per_trajectory':4000}
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
