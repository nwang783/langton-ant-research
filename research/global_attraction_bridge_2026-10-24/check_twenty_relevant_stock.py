"""Finite annotations for an all-n proof using retained disjoint read sets."""
from pathlib import Path
import json
from check_return_permanent_output_debt import case, future, twenty, DXY
P=Path(__file__).parent

def step(B,p,h,t):
    old=B.pop(p,None)
    if old is None:B[p]=t;h=(h+1)%4
    else:h=(h-1)%4
    return (p[0]+DXY[h][0],p[1]+DXY[h][1]),h,old

def close_relevant_period(r):
    """Full-field infinite parity + identical translated pruned state."""
    N=r['physical_updates'];B={tuple(z['cell']):z['lifetime'] for z in r['terminal_black']}
    p=tuple(r['terminal_pose'][0]);h=r['terminal_pose'][1]
    w,drift,tail,tests=future(B,p,h)
    C0={q for q,i in B.items() if i in tail};initial=dict(B);deaths={};events=[]
    for s in range(104):
        p,h,old=step(B,p,h,N+s);events.append(old)
        if old is not None:deaths[old]=s
    w1,drift1,tail1,tests1=future(B,p,h)
    assert w1==w and drift1==drift
    deaths.update({i:104+s for i,s in tail1.items()})
    C1={q for q,i in B.items() if i in tail1}
    assert C1=={(q[0]+drift[0],q[1]+drift[1]) for q in C0}
    assert C0=={q for q,i in initial.items() if i in deaths}
    L=len(C0);profile=[L]
    for s,old in enumerate(events):
        L+=int(N+s in deaths) if old is None else -1;profile.append(L)
    assert L==len(C1) and max(profile)<=r['relevant_mass_max']
    return dict(pruned_state=sorted(C0),translated_pruned_state=sorted(C1),drift=drift,
                relevant_profile=profile,all_future_relevant_max=r['relevant_mass_max'],
                parity_tests=tests+tests1)

G={(0,-1),(1,1),(1,3),(2,2)}
g=case('four_cell_reference',G,1,390)
B={q:-i-1 for i,q in enumerate(sorted(twenty(20)))};p=(0,0);h=1
for t in range(624*20-1516):p,h,_=step(B,p,h,t)
assert p==(0,2) and h==1
C={(x,y-2) for x,y in B if x>=-16 and -14<=x+y<=12};assert len(C)==90
c=case('protected_recovery90',C,1,983)
closures={r['name']:close_relevant_period(r) for r in (g,c)}
assert closures['four_cell_reference']['all_future_relevant_max']==22
assert closures['protected_recovery90']['all_future_relevant_max']==77
assert sum(z['death'] is not None for z in c['initial_read_fates'])==61

B={q:-i-1 for i,q in enumerate(sorted(G))};p=(0,0);h=1;word=''
for t in range(286):
    p,h,old=step(B,p,h,t);word+='R' if old is None else 'L'
A,U=word[:182],word[182:]
balance=lambda w:w.count('R')-w.count('L')
balances={'A':balance(A),'U':balance(U),'U14':balance(U[:14]),'U61':balance(U[:61]),'U71':balance(U[:71])}
assert balances=={'A':32,'U':12,'U14':0,'U61':11,'U71':11}
g61=g['state61'];assert len(g61)==15
internal=[z for z in g61 if z['death'] is not None]
rescued=[z for z in g61 if z['death'] is None]
assert len(internal)==11 and max(z['death'] for z in internal)==157
assert len(rescued)==4
c_deaths={tuple(z['cell']):z['death'] for z in c['initial_read_fates']}
rescues=[]
for z in rescued:
    x,y=z['cell'];assert x>=-16 and -14<=x+y<=12
    death=c_deaths[x,y-2];assert death is not None
    rescues.append(dict(cell=z['cell'],birth=z['lifetime'],recovery_death=death))
assert {tuple(z['cell']):z['recovery_death'] for z in rescues}=={(0,-2):464,(0,2):0,(1,-2):471,(2,5):233}

# Polynomial coefficients are exact stage-word balance, not sampled fitting.
# sum R_i = 12k-26 = 6n-26.
constant=20+5*balances['A']-26*balances['U']+2*balances['U61']+2*balances['U71']+balances['U14']
linear=6*balances['U'];assert (linear,constant)==(72,-88)
out=dict(status='AUTHOR finite annotations; all-n conclusions additionally use retained guarded stage and protected-field theorems',
         all_future_reference_closures=closures,source_word_balances=balances,
         reference_cut61_current=g61,reference_cut61_later_internal=internal,
         reference_cut61_restored_by_actual_recovery=rescues,recovery_initial_relevant=61,
         entire_relevant_stock_bound=20+22+90,
         full_endpoint_mass_polynomial=dict(n_coefficient=linear,constant=constant),
         target_lifetime_permanent_birth_polynomial=dict(n_coefficient=linear,constant=constant-61),
         exact_source_claims_used=['pairwise disjoint COMPLETE stage read sets for every even n>=20',
          'stage words A U^R U[:j] and endpoint e=624n-1516',
          'full B_e restriction to Omega equals fixed C90',
          'entire post-e read trace remains in Omega'],
         scope='Bound132 for all cuts of this capturing family, not a universal or eventual-age counterexample.')
(P/'TWENTY_RELEVANT_STOCK_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['all_future_reference_closures','reference_cut61_current','reference_cut61_later_internal']},indent=2))
