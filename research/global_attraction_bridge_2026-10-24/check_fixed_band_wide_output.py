"""Exact two-ray witnesses plus named full-field controls; no parameter scan."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import twenty,DXY,future
P=Path(__file__).parent
G={(0,-1),(1,1),(1,3),(2,2)}
B=set(G);p=(0,0);h=1;Q=[];U=''
for t in range(286):
    if t>=182:Q.append(p)
    black=p in B
    if black:B.remove(p);h=(h-1)%4
    else:B.add(p);h=(h+1)%4
    if t>=182:U+='L' if black else 'R'
    p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
witnesses=[]
for phase,cell in [(20,(5,1)),(15,(8,1))]:
    assert Q[phase]==cell and U[phase]=='R'
    hits=[]
    for i,q in enumerate(Q):
        dx,dy=cell[0]-q[0],cell[1]-q[1]
        if dx==dy and dx%2==0 and dx>=0:
            m=dx//2;hits.append([m,i]);assert 104*m+i<=phase
    witnesses.append(dict(phase=phase,cell=cell,nonnegative_future_ray_equalities=hits))

controls=[]
for n in (210,400):
    e=624*n-1516;N=e+983
    upper=(-200,2*n+203);lower=(-200,-199)
    expected={104*n+10325:upper,624*n-11915:lower}
    B={q:-i-1 for i,q in enumerate(sorted(twenty(n)))};p=(0,0);h=1
    band_reads=0;turns=[];births=[];deaths=[];source=None
    for t in range(N):
        if t==e+774:source=(dict(B),p,h)
        if t<e and -300<=p[0]<=-151:band_reads+=1
        if t in expected:
            assert p==expected[t] and p not in B;births.append([t,p])
        old=B.pop(p,None)
        if old is None:B[p]=t;h=(h+1)%4;turns.append('R')
        else:
            h=(h-1)%4;turns.append('L')
            if old in expected:deaths.append([old,t])
        p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    assert len(births)==2 and not deaths and band_reads<=40188
    word,drift,tail,tests=future(B,p,h)
    for t,q in expected.items():assert B[q]==t and t not in tail
    sb,sp,sh=source;sw,sd,st,schecks=future(sb,sp,sh)
    phase=next(i for i in range(104) if U[i:]+U[:i]==sw)
    assert turns[e+773]!=sw[-1]
    serial=json.dumps(sorted((x,y,i) for (x,y),i in B.items()),separators=(',',':'))
    controls.append(dict(n=n,initial_black=sorted(twenty(n)),physical_updates=N,
         true_witness_births=births,all_future_witness_deaths=[None,None],
         full_terminal_black_count=len(B),full_terminal_black_sha256=hashlib.sha256(serial.encode()).hexdigest(),
         full_terminal_pose=[p,h],full_terminal_parity_tests=tests,
         exact_first_tail_start=e+774,first_tail_phase=phase,first_tail_parity_tests=schecks,
         last_preceding_actual_turn=turns[e+773],required_preceding_tail_turn=sw[-1],
         five_stage_band_read_count=band_reads,witness_transverse_span=2*n+402))
out=dict(status='AUTHOR; independent audit pending',period_word=U,period_read_positions=Q,
         reference_permanent_witnesses=witnesses,
         parameter_domain='even n=2k>=210, equivalently integer k>=105',
         upper_witness=dict(cell=['-200','2n+203'],stage=1,period_index='k+99',birth='104n+10325'),
         lower_witness=dict(cell=['-200','-199'],stage=4,period_index='3k-104',birth='624n-11915'),
         fixed_band=[-300,-151],band_width=150,
         all_parameter_five_stage_band_read_bound=5*182+5*104*75+61+71+61+71+14,
         controls=controls,
         scope='Unbounded transverse SPAN across a capturing family, while fixed-band read COUNT is uniformly bounded. No single-orbit eventual or global packing refutation.')
(P/'FIXED_BAND_WIDE_OUTPUT_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['period_word','period_read_positions']},indent=2))
