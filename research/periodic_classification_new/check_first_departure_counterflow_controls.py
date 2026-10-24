#!/usr/bin/env python3
"""Author literal controls for the first-departure counterflow candidate.
No Geometry or frontier module is imported. This is not a classification.
"""
from pathlib import Path
from collections import defaultdict, Counter
import json
ROOT=Path(__file__).parent
WORD=(ROOT.parent/'word_stabilization/standard_word.txt').read_text().strip()
DIR=((0,1),(1,0),(0,-1),(-1,0))

def cycles_of(f):
    seen=set();ans=[]
    for v in f:
        if v in seen:continue
        path=[];at={};u=v
        while u not in seen and u not in at:
            at[u]=len(path);path.append(u);u=f[u][0]
        if u in at:ans.append(path[at[u]:])
        seen.update(path)
    return ans

out=[]
for copies in (1,2,3):
    for sign in (1,-1):
        P=104*copies;d=(2*copies,sign*2*copies);D=max(map(abs,d))
        start,h=((-1,0),0) if sign==1 else ((0,0),1)
        p=start;hist=defaultdict(list);flow=Counter()
        def quotient(p):
            k=p[0]//d[0]
            return (p[0]-k*d[0],p[1]-k*d[1]),k
        for t,ch in enumerate(WORD*copies):
            assert h%2==1-(sum(p)%2)
            u,k=quotient(p);hist[u].append((t-k*P,h,ch))
            hh=(h+(1 if ch=='R' else -1))%4
            q=(p[0]+DIR[hh][0],p[1]+DIR[hh][1]);v,l=quotient(q)
            flow[u,v,l-k]+=1
            p,h=q,hh
        assert p==(start[0]+d[0],start[1]+d[1])
        hist={v:sorted(hh) for v,hh in hist.items()}
        for hh in hist.values():
            assert all(ch==('R' if j%2==0 else 'L') for j,(t,h,ch) in enumerate(hh))
        b={};edge_rank={};edge_q={}
        for u,hh in hist.items():
            T,h,ch=hh[0];assert ch=='R';direction=(h+1)%4
            v,k=quotient((u[0]+DIR[direction][0],u[1]+DIR[direction][1]))
            j=next(j for j,(t,h,ch) in enumerate(hist[v]) if h==direction)
            assert hist[v][j][0]+k*P==T+1
            q,r=divmod(T+1-hist[v][0][0]-k*P,4);assert r==0 and q>=j
            out_heading=(hist[v][0][1]+1)%4
            turn=(out_heading-direction)%4
            assert (turn==1 and j==q==0) or (turn==3 and q>=j>=1)
            b[u]=(v,k);edge_rank[u]=j;edge_q[u]=q
        cycles=cycles_of(b);residual=flow.copy();details=[]
        for cyc in cycles:
            k=sum(b[v][1] for v in cyc);ell=len(cyc)
            assert k==-1 and ell%2==0
            Q=sum(edge_q[v] for v in cyc)
            assert P==4*Q-ell
            for u in cyc:
                v,k0=b[u];residual[u,v,k0]-=1;assert residual[u,v,k0]>=0
            details.append(dict(length=ell,winding=k,exact_q_sum=Q,
                                ordinal_period_lower=sum(0 if edge_rank[v]==0 else 4*edge_rank[v]-2 for v in cyc),vertices=cyc))
        balance=Counter();dx=dy=H=V=0
        for (u,v,k),n in residual.items():
            balance[u]+=n;balance[v]-=n
            ex=v[0]+k*d[0]-u[0];ey=v[1]+k*d[1]-u[1]
            assert abs(ex)+abs(ey)==1
            dx+=n*ex;dy+=n*ey;H+=n*abs(ex);V+=n*abs(ey)
        assert not any(balance.values()) and H==V
        assert (dx,dy)==((1+len(cycles))*d[0],(1+len(cycles))*d[1])
        lower=sum(a['length'] for a in details)+2*D*(1+len(cycles))
        assert lower<=P
        out.append(dict(period=P,drift=d,classes=len(hist),cycles=details,
                        additive_counterflow_period_lower=lower,residual_mass=sum(residual.values()),
                        residual_homology=1+len(cycles),status='PASS'))
result=dict(status='AUTHOR_LITERAL_FIRST_DEPARTURE_COUNTERFLOW_CONTROLS_PASS',scope=__doc__,controls=out)
(ROOT/'first_departure_counterflow_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
