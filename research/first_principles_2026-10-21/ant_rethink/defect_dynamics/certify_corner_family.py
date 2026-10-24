"""All-size first-contact certificate for the four-corner endpoint family.

B_n={(-n,-n),(-n,n+1),(n+1,-n),(n+1,n+1)}, n>=0.
The head starts at the origin facing E.  A finite blank-prefix inventory and
an exact infinite-tail ray guard reduce all n to n=0,...,20.  These remaining
seeds are each checked with the complete physical board retained.
"""
import hashlib,json
from pathlib import Path
from first_marker_scattering import step,tail,FACT

ROOT=Path(__file__).resolve().parent


def corners(n):return {(-n,-n),(-n,n+1),(n+1,-n),(n+1,n+1)}


def memberships(p):
    x,y=p;out=set()
    if x==y:
        if x<=0:out.add(-x)
        if x>=1:out.add(x-1)
    if x+y==1:
        if x<=0:out.add(-x)
        if y<=0:out.add(-y)
    assert all(p in corners(n) for n in out)
    return out


def tail_mass_min(b,p,h,nt):
    base=len(b);bb=set(b);minimum=base
    for _ in range(104):
        p,h,c=step(bb,p,h);minimum=min(minimum,len(bb))
    assert len(bb)-base==12
    return minimum


def blank_guard():
    b=set();p=(0,0);h=1;first={};word=[];positive_min=10**9
    for t in range(10088):
        for n in memberships(p):first.setdefault(n,{'time':t,'cell':p})
        p,h,c=step(b,p,h);word.append(c);positive_min=min(positive_min,len(b))
    nt=tail(b,p,h)
    assert nt is not None and nt['drift']==(-2,2)
    sums=[x+y for x,y in nt['reads']];diffs=[x-y for x,y in nt['reads']]
    assert min(sums)==18 and max(sums)==28
    assert min(diffs)==-19 and max(diffs)==-9
    # Equal-coordinate corners have x-y=0; the future rays have x-y<=-9.
    # Other corners have x+y=1; all future rays have x+y in[18,28].
    assert max(first)==20 and positive_min==1
    mm=tail_mass_min(b,p,h,nt);assert mm>0
    return {'certificate_time':10088,'pose':(*p,h),'drift':nt['drift'],
            'mass':len(b),'prefix_positive_time_minimum_mass':positive_min,
            'tail_minimum_mass_first_period':mm,'tail_growth_per_period':12,
            'tail_sum_range':[min(sums),max(sums)],
            'tail_difference_range':[min(diffs),max(diffs)],
            'corner_first_hits':first,'max_corner_parameter_touched':20,
            'unread_among_0_through_20':[n for n in range(21) if n not in first],
            'word_sha256':hashlib.sha256(''.join(word).encode()).hexdigest()}


def finite_case(n,cap=100000):
    b=corners(n);p=(0,0);h=1;letters='';last_bad=0;low=[];return_targets=[];first_hit=None
    for t in range(1,cap+1):
        if first_hit is None and p in corners(n):first_hit={'time':t-1,'cell':p}
        p,h,c=step(b,p,h);letters=(letters+c)[-10:]
        if len(letters)==10 and letters not in FACT:last_bad=t
        if len(b)<=4:
            is_target=False;m=None
            if len(b)==4:
                m=-min(x for x,y in b)
                is_target=m>=0 and b==corners(m) and p==(0,0) and h==1
            low.append({'time':t,'mass':len(b),'pose':(*p,h),'target_corner_state':is_target})
            if is_target:return_targets.append({'time':t,'m':m})
        if t>=104 and t%104==0 and t-last_bad>=208:
            nt=tail(b,p,h)
            if nt:
                mm=tail_mass_min(b,p,h,nt);assert mm>4
                assert not return_targets
                if n==0:assert [(r['time'],r['mass']) for r in low]==[(1,3),(2,2),(3,3),(4,4)]
                else:assert not low
                return {'n':n,'first_corner_read':first_hit,'certificate_time':t,
                        'certificate_pose':(*p,h),'certificate_mass':len(b),
                        'certified_drift':nt['drift'],'tail_growth_per_period':12,
                        'tail_minimum_mass_first_period':mm,'low_mass_prefix_states':low,
                        'infinite_tail_check_passed':True}
    raise RuntimeError(f'uncertified n={n}, cap={cap}; no exclusion permitted')


if __name__=='__main__':
    blank=blank_guard();print(json.dumps({'kind':'blank_guard','result':blank}),flush=True)
    cases=[]
    for n in range(21):
        c=finite_case(n);cases.append(c);print(json.dumps({'kind':'finite_case','result':c}),flush=True)
    out={'status':'all_nonnegative_corner_parameters_certified',
         'initial_heading':'E','initial_position':[0,0],
         'blank_guard':blank,'finite_cases':cases,
         'conclusion':'No positive-time B_n to B_m transition at pose(origin,E), for any n,m>=0.'}
    (ROOT/'corner_family_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
