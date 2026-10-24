"""Four named discovery controls; shifted four remote ports, not added guides."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent
G={(0,-1),(1,1),(1,3),(2,2)}
B=set(G);p=(0,0);h=1;source=''
for t in range(286):
    old=p in B
    if old:B.remove(p);h=(h-1)%4
    else:B.add(p);h=(h+1)%4
    source+='L' if old else 'R';p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
A,U=source[:182],source[182:]
out=[]
for n,K in [(20,10),(40,10),(80,40),(80,80)]:
    z=(2*K,2*K);k=n//2;seed=set(G)
    ports=[((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
    for a,h in ports:
        for q in G:
            r=rot(q,h-1);seed.add((a[0]+r[0]+z[0],a[1]+r[1]+z[1]))
    assert len(seed)==20
    rs=[K+k-4,2*k-5,4*k-6,2*k-7,3*k-4];parts=[61,71,61,71,14]
    stages=[A+U*r+U[:j] for r,j in zip(rs,parts)];nominal=''.join(stages)
    assert len(nominal)==624*n-1516+104*K
    target=(2*K,2*K+2);N=len(nominal)+40000
    B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;born={};dead={};word=[];target_reads=[];divergence=None
    for t in range(N):
        old=B.pop(p,None);c='R' if old is None else 'L'
        if p==target:target_reads.append(dict(time=t,turn=c,old_lifetime=old))
        if t<len(nominal) and c!=nominal[t] and divergence is None:
            j=0;r=t
            while r>=len(stages[j]):r-=len(stages[j]);j+=1
            divergence=dict(time=t,cell=p,heading=h,wanted=nominal[t],actual=c,old_lifetime=old,
                            nominal_stage=j,stage_offset=r,black_before_count=len(B)+int(old is not None))
        if old is None:B[p]=t;born[t]=p;h=(h+1)%4
        else:dead[old]=t;h=(h-1)%4
        word.append(c);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    try:
        tailword,drift,tail,tests=future(B,p,h)
        assert any(tailword==U[i:]+U[:i] for i in range(104))
        dead.update({i:N+t for i,t in tail.items()});L=sum(i in dead for i in range(-20,0));M=L
        for t,c in enumerate(word):L+=int(t in dead) if c=='R' else -1;M=max(M,L)
        cert=dict(status='AUTHOR exact canonical tail at chosen final cut',time=N,pose=[p,h],drift=drift,
                  black_count=len(B),parity_tests=tests,relevant_peak=M)
    except AssertionError:
        cert=dict(status='UNKNOWN beyond physical cutoff',time=N,pose=[p,h],black_count=len(B))
    target_births=[dict(birth=b,cell=q,death=dead.get(b),age=dead[b]-b if b in dead else None) for b,q in born.items() if q==target]
    row=dict(n=n,K=K,initial_black=sorted(seed),nominal_return_time=len(nominal),nominal_marker=target,
             expected_first_marker_birth=104*K-40,first_nominal_divergence=divergence,target_reads=target_reads,
             target_lifetimes=target_births,chosen_future_certificate=cert,
             physical_word_sha256=hashlib.sha256(''.join(word).encode()).hexdigest())
    out.append(row);print(json.dumps(row),flush=True)
(P/'TRANSLATED_RETURN_MODULE_PROBES.json').write_text(json.dumps({'status':'AUTHOR named discovery controls; no all-parameter claim or independent audit','controls':out},indent=2)+'\n')
