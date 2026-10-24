"""Literal controls for the exact same-pose discrepancy clock deduction.
No search, reachability solver or proof of universal capture.
"""
from pathlib import Path
import json, random
OUT=Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0))
def f(s): return 3**abs(s)-1
def J(s,e): return f(s)//2 if e*s>=0 else -3*f(s)//2
def theta(B,p,h,c,axis):
    sig=1 if (p[0]+p[1]+h)%2==0 else -1
    if axis=='v': z=lambda q:q[0]+q[1]; eps=1 if h in (0,1) else -1; sg=sig
    else: z=lambda q:q[0]-q[1]; eps=1 if h in (1,2) else -1; sg=-sig
    return -sg*sum((1 if (q[0]+q[1])%2==0 else -1)*f(z(q)-c) for q in B)+J(z(p)-c,eps)
def step(B,p,h):
    h=(h+(-1 if p in B else 1))%4
    B=B^{p}; p=(p[0]+D[h][0],p[1]+D[h][1])
    return B,p,h
rng=random.Random(20261023)
transitions=0; returns=0; clock_checks=0
for trial in range(20):
    B={(x,y) for x in range(-3,4) for y in range(-3,4) if rng.randrange(4)==0}
    p=(0,0); h=0; seen={}
    for t in range(1500):
        key=(p,h)
        if key in seen:
            s,A=seen[key]; E=A^B
            assert E
            for ax in ('v','u'):
                z=lambda q:q[0]+(q[1] if ax=='v' else -q[1])
                lo=min(map(z,E)); hi=max(map(z,E)); c=(lo+hi)//2
                exact=theta(B,p,h,c,ax)-theta(A,p,h,c,ax)
                unsigned=sum(f(z(q)-c) for q in E)
                bound=len(E)*(3**((hi-lo+1)//2)-1)
                assert t-s<=exact<=unsigned<=bound, (trial,t,s,ax,lo,hi,exact,unsigned,bound,p,h)
                clock_checks+=1
            returns+=1
        seen[key]=(t,set(B))
        C,q,g=step(B,p,h)
        for ax in ('v','u'):
            for c in (-2,0,3):
                assert theta(C,q,g,c,ax)-theta(B,p,h,c,ax)>=1
                clock_checks+=1
        B,p,h=C,q,g; transitions+=1
# An exact fixed-pose endpoint relaxation, not a legal concatenation.
fixed={(-10,-10),(-10,-11),(-11,-10)}
def board(n): return fixed|{(0,2*n),(1,2*n)}
control=[]
for n in range(1,21):
    A=board(n); B=board(n+1); p=(0,0); h=0
    for ax in ('v','u'):
        vals=[]
        for c in range(-2*n-8,2*n+8):
            delta=theta(B,p,h,c,ax)-theta(A,p,h,c,ax)
            assert delta>=8
            vals.append(delta)
        assert min(vals)==8
    # All exact alternating line sums are preserved.
    for k in range(-12,2*n+5):
        assert sum((1 if x%2==0 else -1) for x,y in A if y==k)==sum((1 if x%2==0 else -1) for x,y in B if y==k)
        assert sum((1 if y%2==0 else -1) for x,y in A if x==k)==sum((1 if y%2==0 else -1) for x,y in B if x==k)
    # A changed new cell is at Manhattan distance 2n+2; with alternating
    # movement axes it cannot be read before tick 4n+4.
    assert 4*n+5>8
    control.append({'n':n,'black_mass':len(A),'minimum_radial_clock_gain':8,
                    'actual_duration_upper_if_reachable':8,
                    'duration_lower_to_read_new_cell':4*n+5})
result={'status':'all literal controls passed','transitions':transitions,
        'same_pose_intervals_checked':returns,'clock_checks':clock_checks,
        'fixed_pose_endpoint_chain':control,
        'scope':'Analytic discrepancy bound; chain is a nonreachable endpoint relaxation, not an ant orbit.'}
(OUT/'return_discrepancy_clock_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='fixed_pose_endpoint_chain'},indent=2))
