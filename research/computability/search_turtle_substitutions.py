#!/usr/bin/env python3
"""Exhaust a small, exactly specified self-similar turn-morphism family.
No finite simulation is accepted as a positive infinite certificate.
"""
from itertools import product
from collections import defaultdict
import json,time
D=((0,1),(1,0),(0,-1),(-1,0))
def spec(w):
    p=(0,0);h=0;seen={};firstL=set()
    for t,c in enumerate(w):
        if p in seen and seen[p][1]==c:return None
        if p not in seen and c=='L':firstL.add(p)
        seen[p]=(t,c);h=(h+(1 if c=='R' else -1))%4;p=p[0]+D[h][0],p[1]+D[h][1]
    return p,h,len(firstL)
def letter(t,k,u,v):
    ds=[]
    while t:ds.append(t%k);t//=k
    c='R'
    for digit in reversed(ds):c=(u if c=='R' else v)[digit]
    return c

def trial(u,v,limit):
    k=len(u);p=(0,0);h=0;seen={};nfirst=0
    for t in range(limit):
        c=letter(t,k,u,v)
        if p in seen and seen[p][1]==c:
            return {'failure_time':t,'previous_time':seen[p][0],'cell':p,'turn':c,'first_L_count':nfirst}
        if p not in seen and c=='L':nfirst+=1
        seen[p]=(t,c);h=(h+(1 if c=='R' else -1))%4;p=p[0]+D[h][0],p[1]+D[h][1]
    return {'inconclusive_prefix':limit,'first_L_count':nfirst}

def run(k,limit=20000):
    by=defaultdict(list)
    for bits in product('LR',repeat=k):
        w=''.join(bits);s=spec(w)
        if s is not None:
            p,h,m=s
            if p[0]*p[0]+p[1]*p[1]==k and h in [1,3]:by[(p,h)].append(w)
    cases=[];survivors=[];maximum=-1;witness=None
    for (p,h),us in by.items():
        if h!=1:continue
        vs=by.get(((-p[0],-p[1]),3),[])
        for u in us:
            if u[0]!='R':continue
            for v in vs:
                result=trial(u,v,limit);record={'R':u,'L':v,'scale':p,**result};cases.append(record)
                if 'inconclusive_prefix' in result:survivors.append(record)
                elif result['failure_time']>maximum:maximum=result['failure_time'];witness=record
    return {'length':k,'candidate_pairs':len(cases),'all_rejected_by_finite_alternation_failure':not survivors,'latest_failure_time':maximum,'latest_failure_example':witness,'survivors':survivors,'certificates':cases}
if __name__=='__main__':
    start=time.monotonic();result=[run(k) for k in [5,9,13]]
    out={'status':'Exact exhaustive finite candidate family; positive prefixes are inconclusive','family':'Uniform R->u,L->v; length k; u startsR; net turns+90,-90; displacements a,-a; |a|^2=k; each u,v internally realizable. Fixed point startingR.','results':result,'elapsed_seconds':time.monotonic()-start}
    from pathlib import Path
    (Path(__file__).resolve().parent/'turtle_substitution_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    for r in result:r.pop('certificates')
    print(json.dumps(out,indent=2))
