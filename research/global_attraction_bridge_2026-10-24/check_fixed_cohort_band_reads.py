"""Exact phase/parity annotations for the signed two-input decomposition corollary."""
from pathlib import Path
import json
P=Path(__file__).parent
U=json.loads((P/'FIXED_BAND_WIDE_OUTPUT_CHECKED.json').read_text())['period_word']
D=((0,1),(1,0),(0,-1),(-1,0))
def count_phase(q,d,L,w):
    if d<0:q=-q;d=-d;L=-L-w+1
    lo=max(0,-((q-L)//d));hi=(L+w-1-q)//d
    return max(0,hi-lo+1)
rows=[];tests=0;sharp=0
for shift in range(104):
    word=U[shift:]+U[:shift]
    for h0 in range(4):
        h=h0;p=(0,0);Q=[]
        for c in word:
            Q.append(p);h=(h+(1 if c=='R' else -1))%4
            p=(p[0]+D[h][0],p[1]+D[h][1])
        assert h==h0 and abs(p[0])==abs(p[1])==2
        for axis in range(2):
            counts=[sum(q[axis]%2==r for q in Q) for r in range(2)]
            assert counts==[52,52]
            for w in [1,2,3,150]:
                for L in [-10,0,10,(10**9 if p[axis]>0 else -10**9)]:
                    n=sum(count_phase(q[axis],p[axis],L,w) for q in Q)
                    assert n<=52*w;tests+=1
                    if abs(L)==10**9:assert n==52*w;sharp+=1
        rows.append(dict(phase=shift,heading=h0,drift=p,coordinate_parity_counts=[[52,52],[52,52]]))
g=json.loads((P/'../audits/generic_P104_fixed_cohort_independent.json').read_text())
c=json.loads((P/'../audits/two_black_canonical_completion_independent.json').read_text())
assert g['one_family_max_start']==270504 and g['two_family_max_start']==166816 and g['max_switches']==5
assert c['maximum_sufficient_start'][0]==270192
out=dict(status='AUTHOR analytic source-decomposition corollary; independent audit pending',
         all_phase_heading_cases=rows,exact_ray_band_tests=tests,sharp_forward_band_tests=sharp,
         inherited_family_arbitrary_length=270504,inherited_family_periodic_pieces=6,
         inherited_direct_arbitrary_length=270192,inherited_direct_periodic_pieces=1,
         fixed_cohort_before_third_band_read_bound=dict(constant=270504,width_coefficient=312),
         coordinate_line_bound=270816,width150_band_bound=317304,
         scope='Original fixed black-lifetime cohort; actual reads strictly BEFORE third distinct consumption. Axial bands only; no pristine, guard, time, or restarted-fuel claim.')
(P/'FIXED_COHORT_BAND_READS_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_phase_heading_cases'},indent=2))
