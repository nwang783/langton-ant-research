"""Three named sixteen-cell transverse-return probes, keeping all archives."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)}
B=set(G);p=(0,0);h=1;s=''
for t in range(286):
    old=p in B
    if old:B.remove(p);h=(h-1)%4
    else:B.add(p);h=(h+1)%4
    s+='L' if old else 'R';p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
A,U=s[:182],s[182:]
out=[]
for n in (20,40,80):
    K=2*n;k=n//2;seed=set(G);z=(2*K,2*K)
    for a,h in [((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2)]:
        for q in G:
            r=rot(q,h-1);seed.add((a[0]+r[0]+z[0],a[1]+r[1]+z[1]))
    assert len(seed)==16
    pieces=[A+U*(K+k-4)+U[:61],A+U*(2*k-5)+U[:71],A+U*(4*k-6)+U[:61]]
    nominal=''.join(pieces)+A+U*(n+1000);N=676*n+50000
    B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;dead={};born={};word=[];first=None
    for t in range(N):
        old=B.pop(p,None);c='R' if old is None else 'L'
        if c!=nominal[t] and first is None:
            first=dict(time=t,cell=p,heading=h,wanted=nominal[t],actual=c,old_lifetime=old,
                       old_birth_cell=born.get(old),age=t-old if old is not None and old>=0 else None)
        if old is None:B[p]=t;born[t]=p;h=(h+1)%4
        else:dead[old]=t;h=(h-1)%4
        word.append(c);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    try:
        tw,dr,tail,tests=future(B,p,h);assert any(tw==U[i:]+U[:i] for i in range(104))
        dead.update({i:N+t for i,t in tail.items()});L=sum(i in dead for i in range(-16,0));M=L;firstL=None
        for t,c in enumerate(word):
            if first and t==first['time']:firstL=L
            L+=int(t in dead) if c=='R' else -1;M=max(M,L)
        cert=dict(status='AUTHOR exact canonical infinite future',time=N,pose=[p,h],drift=dr,black_count=len(B),
                  relevant_peak=M,relevant_at_first_contact=firstL,parity_tests=tests)
    except AssertionError:cert=dict(status='UNKNOWN beyond cutoff',time=N,pose=[p,h],black_count=len(B))
    row=dict(n=n,initial_black=sorted(seed),first_nominal_disagreement=first,certificate=cert,
             word_sha256=hashlib.sha256(''.join(word).encode()).hexdigest())
    out.append(row);print(json.dumps(row),flush=True)
(P/'TRANSVERSE_MOVING_MODULE_PROBES.json').write_text(json.dumps({'status':'AUTHOR three named discovery controls, no all-n inference','controls':out},indent=2)+'\n')
