"""Author controls, not an independent audit. Literal whole-board comparison."""
from active_flight import *
from pathlib import Path
import json,random,hashlib
OUT=Path(__file__).parent;ROOT=OUT.parent

def actual_event(B0,p,h,M,limit=100000):
    B=set(B0);k=sector(p,h)
    for t in range(limit):
        C=comp(B,k,cursor(p,h))
        if len(C)>M:return 'cap',t,B,p,h
        if p not in B:
            u,v=ends(p,k);other=v if u==cursor(p,h)else u
            # Independently identify an import by the COMPLETE post-R component.
            bn=set(B);pn,hn=step(bn,p,h)
            N=comp(bn,k,cursor(pn,hn))
            if N-C-{p}:return 'import',t,B,p,h
        p,h=step(B,p,h)
    raise RuntimeError('Finite control exceeded its explicit limit')

def check(B,p,h,M):
    a=plan(B,p,h,M);z=actual_event(B,p,h,M)
    assert a.status==z[0] and a.event==z[1],(a,z)
    bb,pp,hh=a.state_at(a.event)
    assert (bb,pp,hh)==z[2:],(bb,pp,hh,z)
    # Inspect complete intermediate fields as well; passive archives must remain.
    C=set(B);q=p;g=h
    for t in range(a.event+1):
        assert a.state_at(t)==(C,q,g),(t,a)
        if t<a.event:q,g=step(C,q,g)
    return a

def arithmetic_controls():
    # Synthetic ray arithmetic ONLY; these are not asserted ant cycles.
    rng=random.Random(404);cases=0
    for _ in range(2500):
        P=rng.randrange(1,13);d=(rng.randrange(-3,4),rng.randrange(-3,4))
        q=(rng.randrange(-10,11),rng.randrange(-10,11));v=(rng.randrange(-10,11),rng.randrange(-10,11))
        i=rng.randrange(P);j=rng.randrange(P)
        brute=next((k for k in range(50)if any((l*P+j<k*P+i)and(q[0]+k*d[0],q[1]+k*d[1])==(v[0]+l*d[0],v[1]+l*d[1])for l in range(k+1))),None)
        if d==(0,0):n=(0 if j<i else 1)if q==v else None
        else:n=ray_epoch(v,q,d)
        if n is not None and(n<0 or(n==0 and j>=i)):n=None
        assert n==brute,(q,v,d,i,j,n,brute);cases+=1
    N=10**30
    assert ray_epoch((2*N+7,-4*N-9),(7,-9),(2,-4))==N
    assert ray_epoch((2*N+7,-4*N-8),(7,-9),(2,-4))is None
    return {'synthetic_phase_pair_cases':cases,'huge_static_epoch':N,'scope':'Arithmetic tests only, not physical positive-cycle witnesses'}

def main():
    tally={};cases=0;maxevent=0;maxpredictor=0;actualcycles=set();witnesses=[]
    cells=[(x,y)for x in range(-1,2)for y in range(-1,2)]
    for mask in range(512):
        B={q for i,q in enumerate(cells)if mask>>i&1}
        for h in range(4):
            for M in range(7):
                a=check(B,(0,0),h,M);cases+=1;tally[a.status]=tally.get(a.status,0)+1
                maxevent=max(maxevent,a.event);maxpredictor=max(maxpredictor,len(a.phases))
                if a.period:actualcycles.add((a.period,a.drift))
    rng=random.Random(9282)
    for trial in range(100):
        B={(x,y)for x in range(-5,6)for y in range(-5,6)if rng.random()<.3};h=rng.randrange(4)
        a=check(B,(0,0),h,60);cases+=1;tally[a.status]=tally.get(a.status,0)+1
        maxevent=max(maxevent,a.event);maxpredictor=max(maxpredictor,len(a.phases))
        if a.period:actualcycles.add((a.period,a.drift))
    s=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
    B={tuple(q)for q in s['seed']};p=(0,0);h=s['heading']
    for phase in range(104):
        a=check(B,p,h,70);cases+=1;tally[a.status]=tally.get(a.status,0)+1
        if phase in(0,7,38,84):witnesses.append({'standard_phase':phase,'status':a.status,'first_import':a.event,'predictor_preperiod':a.preperiod,'predictor_period':a.period,'predictor_drift':a.drift,'witness':a.witness})
        p,h=step(B,p,h)
    a=check(set(),(0,0),0,10)
    assert a.status=='import'and a.event==8 and a.period==20 and a.drift==(0,0)
    witnesses.append({'blank_first_import':a.event,'zero_drift_predictor_period':a.period,'witness':a.witness})
    out={'status':'AUTHOR_CONTROLS_PASS','scope':'Finite literal controls and exact arithmetic tests. The universal totality proof is separate; no independent PASS claimed.','full_board_cases':cases,'outcomes':tally,'maximum_first_event':maxevent,'maximum_predictor_phases':maxpredictor,'observed_predictor_cycles':sorted((P,list(d))for P,d in actualcycles),'witnesses':witnesses,'arithmetic':arithmetic_controls()}
    (OUT/'active_flight_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
