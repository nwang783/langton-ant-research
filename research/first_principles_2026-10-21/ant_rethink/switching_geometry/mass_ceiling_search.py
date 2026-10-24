"""Exact first-exceedance times for all seeds of cardinality <=K.

No bounding box on the initial seed is imposed. Hidden initial black cells
are placed outside the finite visited footprint. See bounded_mass_theorem.md.
"""
import argparse
import json
from pathlib import Path

DIRS=((1,0),(0,-1),(-1,0),(0,1))

def solve(K):
    best={'time':-1};nodes=0;counts=[]
    for m in range(K+1):
        known={};initial=set();word=[];local_best=0
        def dfs(x,y,h,unused,mass,t):
            nonlocal nodes,local_best,best
            nodes+=1
            z=(x,y);fresh=z not in known
            choices=([0,1] if unused else [0]) if fresh else [known[z]]
            for c in choices:
                known[z]=1-c
                if fresh and c:initial.add(z)
                word.append('L' if c else 'R')
                next_mass=mass+(1 if c==0 else -1)
                next_h=(h+(1 if c==0 else -1))%4
                if next_mass>K:
                    local_best=max(local_best,t+1)
                    if t+1>best['time']:
                        best={'time':t+1,'initial_mass':m,
                              'visible_initial_black':sorted(initial),
                              'unassigned_initial_black':unused-(c if fresh else 0),
                              'word':''.join(word)}
                else:
                    dx,dy=DIRS[next_h]
                    dfs(x+dx,y+dy,next_h,unused-(c if fresh else 0),next_mass,t+1)
                word.pop()
                if fresh:
                    del known[z]
                    if c:initial.remove(z)
                else:known[z]=c
        dfs(0,0,3,m,m,0)
        counts.append({'initial_mass':m,'max_first_exceedance':local_best})
    return {'ceiling':K,'T':best['time'],'nodes':nodes,'by_mass':counts,'witness':best}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('K',type=int)
    args=parser.parse_args()
    r=solve(args.K)
    path=Path(__file__).with_name(f'mass_ceiling_{args.K}.json')
    path.write_text(json.dumps(r,indent=2))
    print(json.dumps(r,indent=2))
