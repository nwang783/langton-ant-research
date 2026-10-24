"""Direct finite-support periodic Langton-word constraints.

Coordinates, heading signs and exact leading-first visit parity are encoded
as finite bit-vectors/Booleans. All coordinates are bounded so no arithmetic
wrap is possible. A SAT word is independently reconstructed and replayed.
UNSAT/UNKNOWN are solver reports, not independently checked proof artifacts.
"""
import argparse
from collections import Counter,defaultdict
from functools import reduce
import json
from pathlib import Path
import sys,time

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'deps'))
import z3

DIR=((0,1),(1,0),(0,-1),(-1,0))


def walk(word):
    x=y=h=0;reads=[]
    for c in word:
        reads.append((x,y));h=(h+(1 if c=='R' else 3))%4
        x+=DIR[h][0];y+=DIR[h][1]
    return reads,(x,y),h


def cl_rank(p,d):
    x,y=p;dx,dy=d
    assert abs(dx) in (0,2) and abs(dy) in (0,2) and d!=(0,0)
    if dx:return (dx*y-dy*x,x%2),x//dx
    return (x,y%2),y//dy


def independently_verify(word,d):
    reads,end,h=walk(word)
    assert end==d and h==0
    classes=defaultdict(list)
    for i,p in enumerate(reads):
        cl,a=cl_rank(p,d);classes[cl].append((a,i,p))
    seed=set()
    for cl,ev in classes.items():
        ev.sort(key=lambda v:(-v[0],v[1]))
        assert all(word[i]==('R' if j%2==0 else 'L') for j,(_,i,_) in enumerate(ev))
        counts=Counter(a for a,_,_ in ev)
        low,high=min(counts),max(counts)
        p0=next(p for a,i,p in ev if a==low);par=0
        for a in range(high,low-1,-1):
            p=(p0[0]+(a-low)*d[0],p0[1]+(a-low)*d[1])
            if par:seed.add(p)
            par^=counts[a]%2
    # Direct physical replay and all-future discrepancy test.
    b=set(seed);x=y=h=0
    for i,c in enumerate(word):
        assert ((x,y) in b)==(c=='L')
        if (x,y) in b:b.remove((x,y))
        else:b.add((x,y))
        h=(h+(1 if c=='R' else 3))%4;x+=DIR[h][0];y+=DIR[h][1]
    assert (x,y)==d and h==0
    discrepancy=b ^ {(p[0]+d[0],p[1]+d[1]) for p in seed}
    ray_min={cl:min(a for a,i,p in ev)+1 for cl,ev in classes.items()}
    for p in discrepancy:
        cl,a=cl_rank(p,d)
        assert cl not in ray_min or a<ray_min[cl]
    return {'seed':sorted(seed),'seed_mass':len(seed),
            'wake_growth':len(b)-len(seed),'translation_classes':len(classes),
            'odd_classes':sum(len(ev)%2 for ev in classes.values()),
            'period':len(word),'drift':d,
            'infinite_tail_discrepancy_passed':True}


def model(P,d,timeout_ms,fixed=None,top_normalize=False):
    assert P%4==0 and P>=4
    width=(P+1).bit_length()
    s=z3.SolverFor('QF_BV');s.set(timeout=timeout_ms)
    x=[z3.BitVec(f'x{i}',width) for i in range(P+1)]
    y=[z3.BitVec(f'y{i}',width) for i in range(P+1)]
    neg=[z3.Bool(f'n{i}') for i in range(P+1)]
    turn=[]
    s.add(x[0]==0,y[0]==0,z3.Not(neg[0]),x[P]==d[0],y[P]==d[1],z3.Not(neg[P]))
    for i in range(P):
        t=z3.Xor(neg[i],neg[i+1])
        if i%2:t=z3.Not(t)
        turn.append(t)
        delta=z3.If(neg[i+1],z3.BitVecVal(-1,width),z3.BitVecVal(1,width))
        if i%2:s.add(x[i+1]==x[i],y[i+1]==y[i]+delta)
        else:s.add(y[i+1]==y[i],x[i+1]==x[i]+delta)
    for i in range(P+1):
        uh=(i+1)//2;uv=i//2;rh=P//2-uh;rv=P//2-uv
        s.add(x[i]>=max(-uh,d[0]-rh),x[i]<=min(uh,d[0]+rh),
              y[i]>=max(-uv,d[1]-rv),y[i]<=min(uv,d[1]+rv))
        if top_normalize:s.add(y[i]<=0)
    dx,dy=d
    if dx:
        along=x
        cross=[(dx//2)*z3.SignExt(1,y[i])-(dy//2)*z3.SignExt(1,x[i]) for i in range(P)]
        forward=(lambda j,i:x[j]>x[i]) if dx>0 else (lambda j,i:x[j]<x[i])
    else:
        along=y;cross=x
        forward=(lambda j,i:y[j]>y[i]) if dy>0 else (lambda j,i:y[j]<y[i])
    for i in range(P):
        terms=[]
        for j in range(i%4,P,4):
            if j==i:continue
            before=forward(j,i)
            if j<i:before=z3.Or(before,z3.And(x[j]==x[i],y[j]==y[i]))
            terms.append(z3.And(cross[j]==cross[i],before))
        s.add(turn[i]==reduce(z3.Xor,terms,z3.BoolVal(False)))
        if fixed is not None:s.add(turn[i]==(fixed[i]=='L'))
    return s,turn


def solve(P,d,timeout_ms,fixed=None,top_normalize=False):
    start=time.monotonic();s,t=model(P,d,timeout_ms,fixed,top_normalize)
    built=time.monotonic();ans=s.check();done=time.monotonic()
    out={'period':P,'drift':d,'solver':z3.get_version_string(),'result':str(ans),
         'timeout_ms':timeout_ms,'build_seconds':built-start,'solve_seconds':done-built,
         'fixed_word':fixed is not None,'top_normalize':top_normalize}
    if ans==z3.sat:
        m=s.model();word=''.join('L' if z3.is_true(m.eval(a,model_completion=True)) else 'R' for a in t)
        out['word']=word;out['independent_verification']=independently_verify(word,d)
    elif ans==z3.unknown:out['reason_unknown']=s.reason_unknown()
    print(json.dumps(out),flush=True)
    return out


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--period',type=int);ap.add_argument('--timeout',type=int,default=15000)
    ap.add_argument('--controls',action='store_true');args=ap.parse_args()
    if args.controls:
        ref=json.loads((ROOT.parents[1]/'ant_global/root/standard.json').read_text())
        # Rotate its W-facing input clockwise to N. Drift(-2,-2) becomes(-2,2).
        control=solve(104,(-2,2),args.timeout,fixed=ref['word'])
        assert control['result']=='sat'
        negative=solve(24,(0,-2),args.timeout,fixed='RRRRLLRLLRRRRLLRRRRLLRLL')
        assert negative['result']=='unsat'
    if args.period:
        solve(args.period,(2,0),args.timeout,top_normalize=True)
