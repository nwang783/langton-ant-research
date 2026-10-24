from fractions import Fraction
from random import Random
from pathlib import Path
import json

D=((0,1),(1,0),(0,-1),(-1,0))

def step(B,p,h):
    h=(h+(-1 if p in B else 1))%4
    B.symmetric_difference_update((p,))
    return (p[0]+D[h][0],p[1]+D[h][1]),h

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(P):
    P=sorted(set(P))
    if len(P)<=1:return tuple(P)
    lower=[]
    for p in P:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(P):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return tuple(lower[:-1]+upper[:-1])

def pow3(n):
    return Fraction(3**n) if n>=0 else Fraction(1,3**(-n))

def clocks(B,p,h,normal=0):
    # normal=0 uses s=x+y, normal=1 uses s=x-y after a quarter-turn
    # heading relabeling. Both formulas are literal rotations of one clock.
    chi=lambda q:1 if (q[0]+q[1])%2==0 else -1
    sigma=chi(p)*(1 if h%2==0 else -1)
    if normal==0:
        s=lambda q:q[0]+q[1]
        e=1 if h in (0,1) else -1
    else:
        s=lambda q:q[0]-q[1]
        e=1 if h in (1,2) else -1
        sigma=-sigma
    P=-sigma*sum((chi(q)*pow3(s(q)) for q in B),Fraction())
    M=-sigma*sum((chi(q)*pow3(-s(q)) for q in B),Fraction())
    P+=Fraction(1 if e==1 else -3,2)*pow3(s(p))
    M+=Fraction(1 if e==-1 else -3,2)*pow3(-s(p))
    return P,M

def main():
    rng=Random(842)
    hull_cases=clock_cases=0
    for case in range(50):
        B={(x,y) for x in range(-4,5) for y in range(-4,5) if rng.randrange(4)==0}
        p=(rng.randrange(-3,4),rng.randrange(-3,4));h=rng.randrange(4)
        states=[(B.copy(),p,h)]
        for t in range(400):
            before=[clocks(B,p,h,k) for k in (0,1)]
            oldp,oldh=p,h
            p,h=step(B,p,h)
            after=[clocks(B,p,h,k) for k in (0,1)]
            for k in (0,1):
                e=(1 if oldh in ((0,1) if k==0 else (1,2)) else -1)
                ep=(1 if h in ((0,1) if k==0 else (1,2)) else -1)
                s=oldp[0]+oldp[1] if k==0 else oldp[0]-oldp[1]
                gains=(4*pow3(s) if (e,ep)==(-1,1) else 0,
                       4*pow3(-s) if (e,ep)==(1,-1) else 0)
                assert tuple(after[k][i]-before[k][i] for i in (0,1))==gains
                clock_cases+=1
            states.append((B.copy(),p,h))
        for j in range(100):
            a=rng.randrange(400);b=rng.randrange(a+1,401)
            Ba,pa,ha=states[a];Bb,pb,hb=states[b]
            P=[state[1] for state in states[a:b+1]]
            assert hull(P)==hull((Ba^Bb)|{pa,pb})
            hull_cases+=1
    B={(0,-1),(1,1),(1,3),(2,2)};p=(0,0);h=1
    for _ in range(182):p,h=step(B,p,h)
    assert (p,h,len(B))==((5,1),1,36)
    before=clocks(B,p,h,1);p0=p;h0=h;B0=B.copy()
    word=''
    for _ in range(104):
        word+='L' if p in B else 'R'
        p,h=step(B,p,h)
    assert (p[0]-p0[0],p[1]-p0[1],h)==(2,2,h0)
    gain=tuple(b-a for a,b in zip(before,clocks(B,p,h,1)))
    out={'hull_checks':hull_cases,'local_clock_checks':clock_cases,
         'standard_word':word,'standard_start_pose':{'p':p0,'h':h0},
         'standard_mass_gain':len(B)-len(B0),
         'standard_transverse_clock_gain':[str(x) for x in gain],
         'standard_transverse_clock_start':[str(x) for x in before]}
    print(json.dumps(out,indent=2))
    Path(__file__).with_name('check_results.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
