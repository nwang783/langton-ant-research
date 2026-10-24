"""Bounded literal controls for the retrospective two-leg output inequality."""
from pathlib import Path
import json,collections
P=Path(__file__).parent
DXY=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,k):
    x,y=q
    for _ in range(k%4):x,y=y,-x
    return x,y
def twenty(n):
    G={(0,-1),(1,1),(1,3),(2,2)};B=set()
    for p,h in [((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]:
        for z in G:
            q=rot(z,h-1);B.add((p[0]+q[0],p[1]+q[1]))
    assert len(B)==20
    return B
def future(B,p,h):
    C=set(B);q=p;hh=h;Q=[];word=[]
    for i in range(104):
        Q.append(q);b=q in C
        if b:C.remove(q);hh=(hh-1)%4
        else:C.add(q);hh=(hh+1)%4
        word.append('L' if b else 'R');q=(q[0]+DXY[hh][0],q[1]+DXY[hh][1])
    drift=(q[0]-p[0],q[1]-p[1]);assert abs(drift[0])==abs(drift[1])==2 and hh==h
    def multiple(v):
        if v[0]%drift[0]:return None
        k=v[0]//drift[0]
        return k if v[1]==k*drift[1] else None
    checks=0
    for i,q in enumerate(Q):
        thresholds=[];hits=[];critical={0}
        for z,r in enumerate(Q):
            m=multiple((r[0]-q[0],r[1]-q[1]))
            if m is not None and (m>0 or (m==0 and z<i)):thresholds.append(m);critical.add(m)
        for r in B:
            k=multiple((r[0]-q[0],r[1]-q[1]))
            if k is not None and k>=0:hits.append(k);critical|={k,k+1}
        for k in critical:
            assert (sum(k==a for a in hits)+sum(k>=a for a in thresholds))%2==(word[i]=='L');checks+=1
    deaths={}
    for q,identity in B.items():
        times=[]
        for i,r in enumerate(Q):
            k=multiple((q[0]-r[0],q[1]-r[1]))
            if k is not None and k>=0:times.append(104*k+i)
        if times:deaths[identity]=min(times)
    return ''.join(word),drift,deaths,checks

def case(name,seed,h0,N,targets=()):
    B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=h0;pos=[];heads=[];turns=[];births={};deaths={};masses=[];state61=None
    for t in range(N):
        pos.append(p);heads.append(h);masses.append(len(B))
        if t==61:state61=dict(B)
        old=B.pop(p,None)
        if old is None:B[p]=t;births[t]=p;h=(h+1)%4;turns.append('R')
        else:deaths[old]=t;h=(h-1)%4;turns.append('L')
        p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    pos.append(p);heads.append(h);masses.append(len(B))
    word,drift,tail,tests=future(B,p,h)
    deaths.update({i:N+t for i,t in tail.items()})
    relevant=[sum(i in deaths for i in range(-len(seed),0))];permanent=[0]
    for t,w in enumerate(turns):
        relevant.append(relevant[-1]+((1 if t in deaths else 0) if w=='R' else -1))
        permanent.append(permanent[-1]+int(w=='R' and t not in deaths))
    assert relevant[-1]==len(tail)
    # Range-extrema tree: each tuple gives earliest min-x,max-x,min-y,max-y.
    def merge(a,b):
        if a is None:return b
        if b is None:return a
        return tuple(min((a[k],b[k]),key=lambda i:((1 if k%2==0 else -1)*pos[i][k//2],i)) for k in range(4))
    size=1
    while size<len(pos):size*=2
    tree=[None]*(2*size)
    for i in range(len(pos)):tree[size+i]=(i,i,i,i)
    for i in range(size-1,0,-1):tree[i]=merge(tree[2*i],tree[2*i+1])
    def query(a,b):
        a+=size;b+=size+1;v=None
        while a<b:
            if a%2:v=merge(v,tree[a]);a+=1
            if b%2:b-=1;v=merge(v,tree[b])
            a//=2;b//=2
        return v
    count=0;minimum=None;selected=[];excess_sum=0;charged_P=0;large_count=0;diff=[0]*(N+1);M=max(relevant)
    for b,q in births.items():
        d=deaths.get(b)
        if d is None or d>N:continue
        a=b+1;ix=query(a,d)
        radius=max(max(abs(pos[t][0]-q[0]),abs(pos[t][1]-q[1])) for t in ix)
        tau=min(t for t in ix if max(abs(pos[t][0]-q[0]),abs(pos[t][1]-q[1]))==radius)
        Pcount=permanent[d]-permanent[a]
        L0,Lstar,L1=relevant[a],relevant[tau],relevant[d]
        lhs=Pcount+L0+2*Lstar+L1;assert lhs>=4*radius
        axis=next(k for k in range(2) if abs(pos[tau][k]-q[k])==radius)
        # Doubled incoming midpoints give exact integral transport terms.
        mu=lambda t:2*pos[t][axis]-DXY[heads[t]][axis]
        exact=4+abs(mu(tau)-mu(a))+abs(mu(tau)-mu(d))
        assert lhs>=exact>=4*radius
        row=dict(birth=b,death=d,cell=q,age=d-b,peak_cut=tau,peak_pose=pos[tau],radius=radius,permanent_births=Pcount,relevant_at_birth=L0,relevant_at_peak=Lstar,relevant_at_death=L1,lhs=lhs,rhs=4*radius,midpoint_rhs=exact,slack=lhs-4*radius)
        count+=1
        if radius>M:
            excess_sum+=radius-M;charged_P+=Pcount;large_count+=1;diff[a]+=1;diff[d]-=1
        if minimum is None or row['slack']<minimum['slack']:minimum=row
        if b in targets:selected.append(row)
    live=0;double_count=0;max_overlap=0
    for t in range(N):
        live+=diff[t]
        if turns[t]=='R' and t not in deaths:
            assert live<=relevant[t]<=M
            double_count+=live;max_overlap=max(max_overlap,live)
    assert 4*excess_sum<=charged_P==double_count<=M*permanent[-1]
    if name=='protected_recovery90':
        assert all(x>=-16 and -16<=x+y<=10 for x,y in pos)
        assert drift==(2,-2)
    return dict(name=name,initial_black=sorted(seed),initial_pose=[[0,0],h0],physical_updates=N,terminal_black=[dict(cell=q,lifetime=i,first_future_read=N+tail[i] if i in tail else None) for q,i in sorted(B.items())],terminal_pose=[p,h],terminal_word=word,terminal_drift=drift,all_period_parity_tests=tests,checked_consumed_R_lifetimes=count,relevant_mass_max=M,amortized_large_returns=dict(count=large_count,sum_radius_excess=excess_sum,four_times_excess=4*excess_sum,permanent_births_with_multiplicity=charged_P,maximum_permanent_birth_overlap=max_overlap,upper_bound=M*permanent[-1]),initial_read_fates=[dict(cell=q,lifetime=-i-1,death=deaths.get(-i-1)) for i,q in enumerate(sorted(seed))],state61=[dict(cell=q,lifetime=i,death=deaths.get(i)) for q,i in sorted(state61.items())] if state61 is not None else None,minimum_slack_control=minimum,selected_returns=selected,permanent_births_through_run=permanent[-1],selected_mass_relevance={str(t):dict(full=masses[t],relevant=relevant[t],permanent=permanent[t]) for t in sorted({0,N}|{v for r in selected for v in [r['birth']+1,r['peak_cut'],r['death']]})})

if __name__=='__main__':
    seed=set(map(tuple,json.loads((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_text())['initial_seed']))
    G={(0,-1),(1,1),(1,3),(2,2)}
    C=twenty(20);p0=(0,0);h0=1
    for t in range(624*20-1516):
        if p0 in C:C.remove(p0);h0=(h0-1)%4
        else:C.add(p0);h0=(h0+1)%4
        p0=(p0[0]+DXY[h0][0],p0[1]+DXY[h0][1])
    assert p0==(0,2) and h0==1
    recovery={(x,y-2) for x,y in C if x>=-16 and -14<=x+y<=12};assert len(recovery)==90
    jobs=[('four_cell_reference',G,1,390,()),('protected_recovery90',recovery,1,983,()),('defect14',seed,1,500,(44,46,52,58)),('filled15',seed|{(-3,-2)},1,500,()),('blank',set(),0,10081,())]
    for n in (20,80,400):jobs.append((f'twenty_n{n}',twenty(n),1,624*n-1516+983,(60,)))
    out=[]
    for args in jobs:
        r=case(*args);out.append(r)
        print(json.dumps({k:v for k,v in r.items() if k not in ['terminal_black','initial_black','terminal_word','initial_read_fates','state61']}),flush=True)
    report=dict(status='AUTHOR exact resource inequality controls; independent audit pending',controls=out,total_fine_updates=sum(r['physical_updates'] for r in out),total_consumed_lifetimes_checked=sum(r['checked_consumed_R_lifetimes'] for r in out),scope='Named full-future controls only; no all-n inference from sampling. Universal inequality has an analytic two-leg proof using retained axial transport.')
    (P/'RETURN_PERMANENT_OUTPUT_DEBT_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
