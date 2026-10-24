"""Test the stronger conjecture of no repeated pose in an internal episode."""
from pathlib import Path
from itertools import product
import json,random
from audit_white_episodes import active,adjacent,pose,edge,step,geometry,finite_vertices

HERE=Path(__file__).resolve().parent


def run(K,initial,p,h):
    B=set(initial);seen={};records=[];start=(p,h);first_repeat=None
    internal,boundary,a,b,bound=geometry(K)
    for t in range(bound):
        state=(p,h)
        if state in seen and first_repeat is None:
            first_repeat=(seen[state],t,state)
        seen.setdefault(state,t)
        records.append((t,p,h,int(p in B),len(B)))
        exit_now=p in boundary
        p,h=step(B,p,h)
        if exit_now:
            return {'steps':t+1,'initial_black':sorted(initial),'initial_pose':start,
                    'K':sorted(K),'first_pose_repeat':first_repeat,
                    'linear_bound_4N':4*len(K),'trace':records}
    raise AssertionError('escape bound')


def main():
    count=0
    for a,b in ((1,1),(1,2),(1,4),(2,2),(2,3),(3,3)):
        K=set(product(range(a),range(b)))
        internal,boundary,_,_,_=geometry(K)
        edges=sorted(internal)
        for mask in range(1<<len(edges)):
            B=boundary|{p for j,p in enumerate(edges) if (mask>>j)&1}
            for v in sorted(K):
                for w in adjacent(v):
                    p,h=pose(v,w)
                    out=run(K,B,p,h);count+=1
                    if out['first_pose_repeat'] is not None:
                        out['searched_cases']=count
                        out['rectangle']=[a,b]
                        (HERE/'internal_pose_repeat.json').write_text(json.dumps(out,indent=2)+'\n')
                        print(json.dumps({k:v for k,v in out.items() if k!='trace'},indent=2))
                        return
    print('no repeat in',count,'cases')


if __name__=='__main__':main()
