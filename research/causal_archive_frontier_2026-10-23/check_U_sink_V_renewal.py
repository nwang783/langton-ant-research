"""Exact literal boundary bookkeeping and scalar renewal corollaries."""
from pathlib import Path
import json, hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry']
IDS=(0,1,4,5,6,7,8,9)
roles={0:(0,1),1:(0,1),4:(1,2),5:(1,2),6:(0,3),7:(0,3),8:(0,3),9:(0,3)}
rows=[]
for a in IDS:
    b=0 if a in (0,1) else 4 if a in (4,5,6) else 7
    full=set(map(tuple,G[a]['outputs'])); base=set(map(tuple,G[b]['outputs']))
    assert base<=full
    extra=full-base
    odd=lambda s:sorted(q for q in s if sum(q)%2)
    tails=G[a]['name'].count('C')
    assert len(odd(base))=={0:0,4:3,7:5}[b]
    assert len(odd(extra))=={0:0,1:2,2:3}[tails]
    assert roles[a] in set(map(tuple,G[a]['inputs']))
    rows.append(dict(packet=a,name=G[a]['name'],selected=roles[a],base=b,
      odd_base=odd(base),odd_extra=odd(extra),C_tails=tails))
SUP=ROOT/'core_periodicity_new/U_parallel_selected_supply_frozen_20261023_2026'
supply=json.loads((SUP/'U_parallel_selected_supply.json').read_text())
assert supply['forced_C_age']==6
assert len(supply['rows'])==432
assert len(supply['surviving_cases'])==3
for r in supply['surviving_cases']:
    assert r['consumer']==0 and r['head']==[1,3,2]
    assert r['source_base_output']==[1,2]
    assert r['distinguished_input_slot']==0
E=list(range(2,295,2)); A=4851+3*len(E)
assert len(E)==147 and A==5292
assert 2*A==10584 and 6*len(E)==882
for m in range(1,100):
    assert ((m-1)-2)-(-294)+1==m+292
    assert 4851*m+3*(m+292)==4854*m+876
# Numerical budget witness only, not physical geometry or a reachable word.
def v(a):
    return 2**(a//6) if a>=0 and a%6==0 else 0
for j in range(6,181):
    assert v(j)<=A+3*sum(v(j-e) for e in E)
deps=[GP,SUP/'manifest.json',HERE/'parallel_transport_manifest.json',HERE/'perpendicular_manifest.json',HERE/'manifest.json']
out=dict(status='AUTHOR_U_SINK_V_RENEWAL_PENDING_INDEPENDENT_AUDIT',
 scope='Actual post-entry U-entry complete-eight epochs; numerical witness is not a physical ant control.',
 rows=rows,even_source_ages=E,perpendicular_exceptions=4851,tail_capacity_per_source_epoch=3,
 per_epoch_constant=A,arm_source_age=6,
 total='N_j<=5292+3 sum_even2..294 v_(j-e)+u_(j-6)',
 nonD='v_j+u_j<=5292+3 sum_even2..294 v_(j-e)',
 block_nonD='sum(v+u)<=4854m+876+3 sum_padded_source_interval v',
 eventual_V_bound='v<=M eventually implies N<=10584+882M eventually',
 consequence='Infinite actual U-entry retained-eight factors require unbounded V-base epoch counts.',
 dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps})
(HERE/'U_sink_V_renewal_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','per_epoch_constant','arm_source_age','consequence')},indent=2))
