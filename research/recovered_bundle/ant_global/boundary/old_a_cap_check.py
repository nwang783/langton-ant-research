from collections import defaultdict,Counter
from itertools import product
import json,random
from pathlib import Path
DIR=[(1,0),(0,-1),(-1,0),(0,1)]

def inspect(seed,steps=400):
    black=set(seed); initial=set(seed); x,y,d=0,-4,2
    visits=defaultdict(list); events=[]; stats=Counter(); H=0; EB=0
    IA=sum(x+y==-1 for x,y in initial)
    checked=[]
    for t in range(steps):
        lev=x+y
        if lev>0: break
        c=(x,y) in black
        out=(d+(-1 if c else 1))%4
        ev=(t,x,y,d,int(c),out)
        events.append(ev); visits[(x,y)].append(ev)
        stats[('N',lev)]+=1;stats[('Delta',lev)]+=1-2*c
        if lev==-1 and c and d==1 and out==0: H+=1
        if lev==-2 and not c and d==2 and out==3: EB+=1
        if c:black.remove((x,y))
        else:black.add((x,y))
        dx,dy=DIR[out];x+=dx;y+=dy;d=out
        if lev==-3 and x+y<=-4:
            M=stats[('N',0)];DA=stats[('Delta',-1)];DB=stats[('Delta',-2)];DC=stats[('Delta',-3)]
            NA=stats[('N',-1)];NB=stats[('N',-2)];NC=stats[('N',-3)]
            D=EB-M+2*H
            assert stats[('Delta',0)]==M,(seed,events)
            assert 0<=H<=IA,(seed,events)
            for p,es in visits.items():
                if sum(p)==0: assert len(es)==1
                if sum(p)==-1 and any(e[3]==1 and e[4] and e[5]==0 for e in es):
                    assert p in initial and len(es)==1,(seed,events)
            assert D>=0,(seed,events)
            assert NA==4*M-DA-4*H,(seed,events)
            assert NB==8*M-4*DA+DB-8*H-4*D,(seed,events)
            base=12*M-8*DA+4*DB-DC-8*D
            assert NC<=base+4*H+4*IA,(seed,events)
            checked.append(dict(t=t+1,IA=IA,H=H,M=M,NA=NA,NB=NB,NC=NC,DA=DA,DB=DB,DC=DC,D=D,EB=EB,residual=NC-base))
    return checked,events,(x,y,d)

rng=random.Random(20261021)
cells=[(r,l-r) for l in (-1,-2,-3) for r in range(-1,3)]
results=[];total=0;best=None;Htotal=0
for mask in range(1<<len(cells)):
    seed={p for i,p in enumerate(cells) if mask>>i&1}
    checks,events,end=inspect(seed)
    total+=len(checks)
    for q in checks:
        if best is None or q['residual']>best['counts']['residual']:
            best=dict(seed=sorted(seed),counts=q,events=events[:q['t']])
        Htotal+=q['H']>0
for j in range(10000):
    cells2=[(r,l-r) for l in range(-1,-7,-1) for r in range(-5,6)]
    seed={p for p in cells2 if rng.random()<.24}
    checks,events,end=inspect(seed,2000)
    total+=len(checks)
    for q in checks:
        if q['IA'] and (best is None or q['residual']/q['IA']>best['counts']['residual']/max(1,best['counts']['IA'])):
            best=dict(seed=sorted(seed),counts=q,events=events[:q['t']])
        Htotal+=q['H']>0
out=dict(exhaustive_seed_count=1<<len(cells),random_seed_count=10000,completed_prefixes=total,prefixes_with_bridges=Htotal,best=best)
Path('ant_global/boundary/old_a_cap_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='best'},indent=2))
print('Best:',best['seed'],best['counts'])
