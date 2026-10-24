#!/usr/bin/env python3
"""Exact black-class deficiency for one signed standard-rail profile instance.

This is interval scheduling only because a covered class physically lies in
its writer's read band. It is NOT a solver for arbitrary interval set cover.
No supplied word, period, cap or prepared profile is searched.
"""
from bisect import bisect_left

def interval_black_deficiency(candidates, black_normals):
    black_normals=list(black_normals);b=len(black_normals);target=(1<<b)-1
    if any(type(t) is not int for t in black_normals):
        raise ValueError('integer physical normal per distinct black class required')
    usable=[]
    for i,c in enumerate(candidates):
        band=c['band'];mask=c['cover_mask']
        if len(band)!=2 or any(type(t) is not int for t in band) or band[0]>band[1]:
            raise ValueError('invalid physical closed read band')
        if type(mask) is not int or mask<0 or mask>target:
            raise ValueError('black cover mask outside supplied classes')
        # This semantic condition is essential. Disjoint bands then have
        # disjoint masks, and popcounts are additive in a compatible bundle.
        if any(not band[0]<=black_normals[j]<=band[1]
               for j in range(b) if mask>>j&1):
            raise ValueError('covered class is outside its physical read band')
        if not c['polluted_white']:
            usable.append((band[1],band[0],i,mask))
    usable.sort();ends=[x[0] for x in usable];best=[0];pred=[];take=[]
    for j,(hi,lo,original,mask) in enumerate(usable):
        previous=bisect_left(ends,lo,0,j)-1
        pred.append(previous)
        include=mask.bit_count()+best[previous+1]
        if include>best[-1]:best.append(include);take.append(True)
        else:best.append(best[-1]);take.append(False)
    chosen=[];j=len(usable)-1
    while j>=0:
        if take[j]:chosen.append(usable[j][2]);j=pred[j]
        else:j-=1
    chosen.reverse();covered=0
    for i in chosen:
        mask=candidates[i]['cover_mask']
        if covered&mask:raise ArithmeticError('physical disjoint-cover invariant failed')
        covered|=mask
    if covered.bit_count()!=best[-1] or best[-1]>b:
        raise ArithmeticError('interval coverage count invariant failed')
    return dict(required_black_classes=b,maximum_standard_covered=best[-1],
                black_deficiency=b-best[-1],selected_candidate_indices=chosen,
                covered_mask=covered,
                uncovered_black_indices=[j for j in range(b) if not(covered>>j&1)],
                interval_dp=dict(sorted_original_indices=[x[2] for x in usable],
                                 previous_compatible=pred,best_prefix_weight=best))

def supplied_profile_deficiency(result):
    if not result.get('parallel_standard_direction') or result['status'] not in (
            'INCOMPATIBLE','MATCH_EMPTY_WHITE_PROFILE','MATCH_STANDARD_RAIL_BUNDLE'):
        return dict(status='NOT_APPLICABLE',reason='A complete diagonal bulk-profile instance is required.')
    black=result['required_black_classes'];candidates=result.get('candidates',[])
    r=interval_black_deficiency(candidates,[t for t,e in black])
    compatible=r['black_deficiency']==0
    if compatible!=(result['status']!='INCOMPATIBLE'):
        raise ArithmeticError('independent interval optimum disagrees with selector decision')
    constants=result['constants'];q=constants['superperiod_copies'];w=constants['consumer_endpoint_loss']
    cp=constants['parallel_flight_loss'];ct=constants['nonparallel_flight_loss'];delta=r['black_deficiency']
    return dict(status='EXACT_BLACK_DEFICIENCY',**r,constants=constants,
                stronger_lower_bound=f'|B|>={delta}*(floor(n/{q})-{w}-L-{cp}*F_parallel-{ct}*F_perpendicular)',
                scope='Signed complete bulk-profile hypothesis and common-gauge physical lift; no launch or general rewriter search.')
