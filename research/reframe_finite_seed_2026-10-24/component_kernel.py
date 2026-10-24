"""Exact finite local R-import/L-split kernel at a supplied active-w cap.
LP is exploratory only; a positive solution must pass exact rational checking.
Passive components retain geometry for each transition; only the ranking sums
weights by rigid graph type. No abstract cycle is an ant trajectory.
"""
from active_flight import *
from enumerate_small_caps import levels
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from fractions import Fraction
from math import lcm
from pathlib import Path
import json,sys
OUT=Path(__file__).parent

def canonical_active(C,p,h):
    return frozenset(rot((x-p[0],y-p[1]),(-h)%4)for x,y in C)

def module_type(C,k=1):
    if not C:return None
    es=[ends(q,k)for q in C];anchor=es[0][0]
    ge=[]
    for u,v in es:
        pp=[]
        for x,y in(u,v):
            dx=x-anchor[0];dy=y-anchor[1];assert (dx+dy)%4==0 and(dx-dy)%4==0
            pp.append(((dx+dy)//4,(dx-dy)//4))
        ge.append(pp)
    variants=[]
    for h in range(4):
        ee=[[rot(p,h)for p in e]for e in ge];xx=min(x for e in ee for x,y in e);yy=min(y for e in ee for x,y in e)
        variants.append(tuple(sorted(tuple(sorted((x-xx,y-yy)for x,y in e))for e in ee)))
    return min(variants)

def kernel(M):
    lev=list(levels(M));states=sorted(set.union(*lev),key=lambda z:(len(z),sorted(z)));index={C:i for i,C in enumerate(states)}
    modules={};trans=[];w=cursor((0,0),0)
    def typ(C):
        t=module_type(C)
        if t is None:return None
        if t not in modules:modules[t]=len(modules)
        return modules[t]
    def add(C,D):
        B=set(C)|set(D);p=(0,0);h=0;beforeC=comp(B,1,w);assert beforeC==set(C)
        c='L'if p in B else'R';pn,hn=step(B,p,h);N=comp(B,1,cursor(pn,hn))
        if len(N)>M:return
        lost=B-N
        if c=='R':assert not lost
        else:assert not D
        cn=canonical_active(N,pn,hn);assert cn in index
        trans.append({'source':index[C],'target':index[cn],'consume':typ(D),'emit':typ(lost),'turn':c,'input_component':sorted(C),'imported_component':sorted(D),'output_active':sorted(N),'emitted_component':sorted(lost),'output_pose':[pn,hn]})
    for C in states:
        if (0,0)in C:add(C,set());continue
        u,v=ends((0,0),1);other=v if u==w else u;V=vertices(C,1)|{w}
        add(C,set())
        if other in V:continue
        dx=(other[0]-w[0])//2;dy=(other[1]-w[1])//2
        for n in range(1,M-len(C)):
            for E in lev[n]:
                D={(x+dx,y+dy)for x,y in E}
                if vertices(D,1).isdisjoint(V):add(C,D)
    return states,modules,trans

def main():
    M=int(sys.argv[1])if len(sys.argv)>1 else 3
    states,mods,T=kernel(M);n=len(states);A=lil_matrix((len(T),n+len(mods)),dtype=float)
    for j,t in enumerate(T):
        A[j,t['source']]-=1;A[j,t['target']]+=1
        if t['consume']is not None:A[j,n+t['consume']]-=1
        if t['emit']is not None:A[j,n+t['emit']]+=1
    res=linprog([1]*(n+len(mods)),A_ub=A.tocsr(),b_ub=[-1]*len(T),bounds=(0,None),method='highs')
    out={'scope':'Exact local transition kernel; passive-weight LP is a relaxation, not a physical trajectory compiler.','active_cap':M,'active_states':n,'passive_types':len(mods),'transitions':len(T),'lp_status':res.message}
    if res.success:
        f=[Fraction(float(x)).limit_denominator(1000000)for x in res.x];den=lcm(*(x.denominator for x in f));a=[int(x*den)for x in f]
        assert all(x>=0 for x in a)
        margin=[]
        for t in T:
            x=a[t['source']]-a[t['target']]
            if t['consume']is not None:x+=a[n+t['consume']]
            if t['emit']is not None:x-=a[n+t['emit']]
            assert x>=den,(x,den,t);margin.append(x)
        out.update(status='EXACT_NONNEGATIVE_INTEGER_RANK_FOUND',minimum_step_drop=min(margin),scale=den,active_ranks=[{'C':sorted(C),'weight':a[i]}for i,C in enumerate(states)],passive_weights=[{'edges':t,'weight':a[n+i]}for t,i in sorted(mods.items(),key=lambda x:x[1])],max_active_rank=max(a[:n]))
    else:out['status']='NO_RANK_FROM_THIS_LP_CALL'
    (OUT/f'component_kernel_M{M}.json').write_text(json.dumps({'summary':out,'transitions':T},indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k not in('active_ranks','passive_weights')},indent=2))
if __name__=='__main__':main()
