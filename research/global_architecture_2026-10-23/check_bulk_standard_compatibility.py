#!/usr/bin/env python3
"""Controls for one-supplied-word finite bulk criterion; not a word search."""
import hashlib,json,time
from bulk_standard_compatibility import *

def main():
    start=time.monotonic();V=''.join('L' if c=='R' else 'R' for c in H[::-1])
    P108=V[:31]+'LRRRR'+V[32:]
    cases=[('standard',H,3,'MATCH_EMPTY_WHITE_PROFILE'),
           ('standard_scale4',H*2,3,'MATCH_EMPTY_WHITE_PROFILE'),
           ('P108',P108,3,'INCOMPATIBLE'),
           ('reverse104',V,3,'INCOMPATIBLE'),
           ('reverse_scale4',V*2,3,'INCOMPATIBLE'),
           ('D10','LLLLRLRRRR',0,'INCOMPATIBLE'),
           ('odd_LR','LR',3,'INCOMPATIBLE'),
           ('odd_scale3','LR'*3,3,'INCOMPATIBLE'),
           ('axis_RLLR','RLLR',3,'INCOMPATIBLE'),
           ('nonrestoring','R',3,'FINITE_POWER_CONFLICT'),
           ('zero','RRRR',3,'FINITE_POWER_CONFLICT')]
    records=[];rotation_controls=0;joint_profile_controls=0
    for name,P,h,want in cases:
        r=criterion(P,h);assert r['status']==want,(name,r['status'])
        for rotate in range(4):
            z=criterion(P,(h+rotate)%4);assert z['status']==want,(name,rotate)
            if 'constants' in r:assert z['constants']==r['constants'],(name,rotate,'constants')
            rotation_controls+=1
        if r.get('parallel_standard_direction'):
            hn=r['normalized_heading'];a=r['diagonal_scale'];q=r['constants']['superperiod_copies'];l=r['constants']['common_drift'][0]
            pp,d,hh=orbit_histories(P,hn)
            qq=diagonal_profile(P*q,hn,l)
            for (t,e),vv in qq.items():
                rep=(e,e-t)
                matches=[v for base,v in pp if multiple((rep[0]-base[0],rep[1]-base[1]),d) is not None]
                assert len(matches)==1 and matches[0][0][3]==vv[0][3]
                joint_profile_controls+=1
        if '_clauses' in r:r['cnf_certificate']=certify_cnf(r,HERE/('generic_bulk_'+name))
        (HERE/('generic_bulk_'+name+'.json')).write_text(json.dumps(public(r),indent=2)+'\n')
        records.append(dict(name=name,status=r['status'],constants=r.get('constants'),
                            rail_variables=r.get('selector_variables'),rail_clauses=r.get('selector_clauses'),
                            RUP=r.get('cnf_certificate',{}).get('checker')))
    x=criterion(P108,3);assert all(c['polluted_white'] for c in x['candidates'])
    assert x['constants']['consumer_endpoint_loss']==2
    assert x['constants']['parallel_flight_loss']==6
    assert x['constants']['nonparallel_flight_loss']==1408
    # Nontrivial SAT control of selector search independent of a P word:
    # two disjoint rails are both necessary to cover the two target bits.
    synthetic=[dict(band=[0,10],cover_mask=1,polluted_white=[]),
               dict(band=[11,21],cover_mask=2,polluted_white=[]),
               dict(band=[5,15],cover_mask=3,polluted_white=[(0,0)])]
    model,stats=solve_cover(synthetic,2);assert set(model)=={0,1}
    synthetic[1]['band']=[10,20]
    model,stats=solve_cover(synthetic,2);assert model is None
    out=dict(status='PASS supplied-word bulk controls',records=records,
             supplied_words=len(cases),rotation_controls=rotation_controls,
             joint_profile_class_controls=joint_profile_controls,
             synthetic_selector_positive_and_negative=True,
             scope='No consumer enumeration or arbitrary-period classification; generic implementation audit separate.',
             seconds=time.monotonic()-start,
             source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                            (HERE/'bulk_standard_compatibility.py',HERE/'check_bulk_standard_compatibility.py')})
    (HERE/'bulk_standard_compatibility_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
