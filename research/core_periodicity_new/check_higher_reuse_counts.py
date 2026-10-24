"""Literal all-prefix controls for the analytic higher-R reuse/run ledger."""
import json,random
from collections import Counter
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
rng=random.Random(202610222103)
rows=[]
for case in range(40):
    rad=case%11;m0=case%20
    universe=[(x,y) for x in range(-rad,rad+1) for y in range(-rad,rad+1)]
    B=set(rng.sample(universe,min(m0,len(universe))));m=len(B)
    p=(0,0);h=case%4;visits=Counter();runs={'R':Counter(),'L':Counter()};last='';length=0;u=q=0
    maxmass=len(B)
    for t in range(1,10001):
        visits[p]+=1;c='L'if p in B else'R';q+=visits[p]>=3
        u+=c=='R'and visits[p]>=3
        if c==last:
            runs[c][length]-=1;length+=1
        else:last=c;length=1
        runs[c][length]+=1
        B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4
        p=(p[0]+D[h][0],p[1]+D[h][1]);maxmass=max(maxmass,len(B))
        r,l=runs['R'],runs['L']
        assert length<=4
        assert r[3]+l[3]<=2
        assert r[4]<=m+u+1 and l[4]<=m+u+1
        assert l[1]<=3*m+2*u-r[4]+3
        assert len(B)+r[1]+2*l[4]<=5*m+3*u+8
        E=r[1]+l[1]+r[3]+l[3]+r[4]+l[4]
        assert E<=9*m+6*u+14
        assert t<=90*m*m+114*m*u+36*u*u+348*m+222*u+326
        assert t<=(10*m+6*u+20)**2
    rows.append({'case':case,'initial_mass':m,'reads':t,'higher_reads':q,'higher_R_reads':u,'max_mass':maxmass})
out={'status':'finite controls, not the all-prefix proof','checked_prefixes':400000,'cases':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'checked_prefixes':out['checked_prefixes'],'status':out['status']},indent=2))
