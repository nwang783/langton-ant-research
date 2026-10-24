"""Targeted finite gate first-return controls, arbitrary colors away from u,v.
No translating-front, drift or period search; bounded checks certify only listed
short local exclusions and exact positive factors.
"""
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0));u=(0,0);v=(1,0)
reports=[]
for n in (4,8,12,16,20):
    nodes=[0];solutions=[]
    def dfs(p,h,t,last,counts,trace):
        nodes[0]+=1
        if p==u and t:
            if t==n and h==2 and counts.get(v)==2:
                # Source return L then target R2; both local colors fixed.
                assert last[u]==1 and last[v]==-1
                solutions.append(trace)
            return
        if t==n:return
        if abs(p[0])+abs(p[1])>n-t:return
        # u only at t0; its first R leaves E. v must R0 incoming E then L1 incoming W.
        if p==u:opts=(1,)
        elif p==v:
            rank=counts.get(v,0)
            if rank>1 or h!=(1 if rank==0 else 3):return
            opts=(1 if rank==0 else -1,)
        elif p in last:opts=(-last[p],)
        else:opts=(1,-1)
        for c in opts:
            hh=(h+c)%4;dx,dy=D[hh];q=(p[0]+dx,p[1]+dy)
            ll=last.copy();ll[p]=c;cc=counts.copy();cc[p]=cc.get(p,0)+1
            dfs(q,hh,t+1,ll,cc,trace+[(list(p),h,'R'if c==1 else'L')])
    dfs(u,0,0,{}, {},[])
    reports.append(dict(length=n,nodes=nodes[0],count=len(solutions),sample=solutions[0]if solutions else None))
    if solutions:break
res=dict(scope='Source u R0 -> neighboring v R0; u first return is L1 with opposite incoming heading, sends v R2; v history R(h),L(-h),R(h). Colors outside these two cells arbitrary. Lengths below are exact finite controls only.',reports=reports)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
