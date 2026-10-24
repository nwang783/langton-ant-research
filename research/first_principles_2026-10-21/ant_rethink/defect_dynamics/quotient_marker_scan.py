"""Finite-prefix counterexample search for Phi <= 2m+1.
No cutoff is interpreted as a theorem.
"""
import json
from pathlib import Path
from first_marker_scattering import step,DR

def check(seed,heading=3,capsteps=200000):
    b=set(seed);p=(0,0);h=heading;vis={};mass={};record=0;best=(-100000,None)
    for t in range(capsteps):
        s=p[0]+p[1];vis[s]=vis.get(s,0)+1;mass[s]=mass.get(s,0)+( -1 if p in b else 1)
        p,h,c=step(b,p,h);record=max(record,p[0]+p[1]);cap=record
        if cap<4 or (heading-cap)%2!=1 or p[0]+p[1]>cap-4:continue
        if any(x+y in (cap,cap-1) for x,y in seed):continue
        M=vis.get(cap,0)
        if not M:continue
        # mass is delta; row A started white by the check above.
        phi=M-2*mass.get(cap-1,0)
        if phi>best[0]:best=(phi,{'t':t+1,'cap':cap,'M':M,'A':mass.get(cap-1,0),'p':p,'h':h})
    return {'seed':sorted(seed),'steps':capsteps,'max_phi':best[0],'witness':best[1]}

def main():
    b=set();p=(0,0);h=3
    for _ in range(9977+50*104):p,h,c=step(b,p,h)
    rays=[]
    for i in range(104):
        if p not in b:rays.append((i,p))
        p,h,c=step(b,p,h)
    # Use every white phase; duplicates remove themselves.
    targets=sorted(set(q for i,q in rays))
    for q in targets:
        result=check({q});print(json.dumps(result),flush=True)

if __name__=='__main__':main()
