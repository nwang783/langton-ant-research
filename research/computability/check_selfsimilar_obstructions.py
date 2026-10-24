#!/usr/bin/env python3
"""Exact finite hypothesis checks for the analytic self-similar obstructions.
No finite simulation is accepted as an infinite ant certificate.
"""
from search_turtle_substitutions import spec, D
from pathlib import Path
import json

def check(u,v):
    assert len(u)==len(v)>1 and set(u+v)<={'R','L'}
    su,sv=spec(u),spec(v)
    assert su is not None and sv is not None
    a,hu,_=su;av,hv,_=sv
    assert hu==1 and hv==3 and av==(-a[0],-a[1]) and u[0]=='R'
    norm=a[0]*a[0]+a[1]*a[1];assert norm>1
    internal=[]
    for w in (u,v):
        x=y=h=0;hits=[]
        for j,c in enumerate(w):
            if j and (x*a[0]+y*a[1])%norm==0 and (y*a[0]-x*a[1])%norm==0:
                hits.append({'phase':j,'position':[x,y]})
            h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
        internal.append(hits)
    k=len(u);eu=2*u.count('R')-k;ev=2*v.count('R')-k
    alpha=(eu+ev)//2;lam=(eu-ev)//2
    return {'R':u,'L':v,'length':k,'scale':a,'scale_norm_squared':norm,
            'excesses':[eu,ev],'alpha':alpha,'lambda':lam,
            'internal_sublattice_hits':internal,
            'symmetric_mass_exclusion':alpha==0 and(lam<0 or lam*lam<=norm),
            'area_exclusion_any_background':bool((alpha!=0 and k>norm)or(alpha==0 and abs(lam)>norm)),
            'negative_mass_exclusion_finite_support':alpha<0,
            'first_visit_exclusion_finite_support':v[0]=='L' and not any(internal)}

if __name__=='__main__':
    results=[check('RRL','LRL'),check('RRRLRRRRL','LRRLRRRRL'),
             check('RRRLRRLRLRLRR','LRRLRRLRLRLRR')]
    assert all(r['first_visit_exclusion_finite_support'] for r in results)
    assert not results[-1]['symmetric_mass_exclusion']
    assert not results[-1]['area_exclusion_any_background']
    assert not results[-1]['negative_mass_exclusion_finite_support']
    out={'status':'Exact hypothesis controls, not an exhaustive search or an infinite-trace simulation proof.', 'results':results}
    (Path(__file__).resolve().parent/'selfsimilar_obstruction_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
