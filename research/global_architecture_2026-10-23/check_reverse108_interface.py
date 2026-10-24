#!/usr/bin/env python3
"""Finite exact orbit-profile certificate, not a period/cap search."""
import hashlib, json, pathlib
from flat_collinear_validator import trace

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
SOURCE=ROOT/'causal_reduction/unit_scale/reverse108_prepared_control.json'
supplied=json.loads(SOURCE.read_text())
V=''.join('L' if c=='R' else 'R' for c in H[::-1])
assert V[31]=='L'
P=V[:31]+'LRRRR'+V[32:]
assert P==supplied['word'] and len(P)==108

def profile(w,h):
    rr,d,hh=trace(w,h)
    assert hh==h and d in ((2,2),(-2,-2))
    out={}
    for (x,y),i,c in rr:
        transverse=x-y; parity=x%2
        k=(x-parity)//d[0]
        assert (x,y)==(parity+k*d[0],parity-transverse+k*d[1])
        out.setdefault((transverse,parity),[]).append((i-len(w)*k,i,k,c))
    for rows in out.values(): rows.sort()
    assert all(all(a[3]!=b[3] for a,b in zip(rows,rows[1:])) for rows in out.values())
    return out

hp=profile(H,1); pp=profile(P,3)
assert all(v[0][3]=='R' for v in hp.values())
hblack={s for s,v in hp.items() if v[-1][3]=='R'}
pblack={s for s,v in pp.items() if v[0][3]=='L'}
pout={s for s,v in pp.items() if v[-1][3]=='R'}
assert len(hp)==22 and len(hblack)==12
assert len(pp)==23 and len(pblack)==11 and len(pout)==3
assert {(t-6,p) for t,p in pblack}==set(map(tuple,supplied['input_black_classes']))
assert {(t-6,p) for t,p in pout}==set(map(tuple,supplied['output_black_classes']))

translations=sorted({hs[0]-ps[0] for hs in hp for ps in pp if (hs[0]-ps[0])%2==0})
records=[]
for transverse in translations:
    for parity in (0,1):
        conflicts=[]; exterior_black=[]; intersections=[]
        for ps,rows in pp.items():
            hs=(ps[0]+transverse,(ps[1]+parity)%2)
            desired=rows[0][3]=='L'
            if hs in hp:
                intersections.append(hs)
                produced=hp[hs][-1][3]=='R'
                if desired!=produced:
                    conflicts.append(dict(P_class=ps,H_class=hs,
                                          P_required_black=desired,H_output_black=produced,
                                          P_rows=rows,H_rows=hp[hs]))
            elif desired: exterior_black.append(hs)
        assert intersections and conflicts
        records.append(dict(cap_transverse=transverse,cap_x_parity=parity,
                            overlapping_classes=len(intersections),
                            conflicting_classes=len(conflicts),
                            exterior_required_black_classes=len(exterior_black),
                            one_conflict=conflicts[0]))

allfactors={(H*2)[i:i+10] for i in range(len(H))}
periodic=P*3
kappa=sum(periodic[108+i-10:108+i] not in allfactors and
          periodic[108+i-9:108+i+1] not in allfactors for i in range(108))
widthsum=sum(max(row[2] for row in pp[s])-min(row[2] for row in pp[s]) for s in pblack)
assert len(translations)==11 and len(records)==22
assert translations==list(range(-10,11,2))
out=dict(status='PASS exact all-translation interface exclusion',
    architecture='H^n C P108^n, H starts E, C ends W, arbitrary fixed finite literal C; n unbounded',
    scope='Excludes a bounded-initial-fuel flat return pump, not P108 on its own prepared rail or universal capture.',
    H_word=H,P_word=P,H_heading=1,P_heading=3,
    H_drift=[2,2],P_drift=[-2,-2],cyclic_K=kappa,
    H_read_classes=len(hp),H_mature_black=sorted(hblack),
    P_read_classes=len(pp),P_required_black=sorted(pblack),P_output_black=sorted(pout),
    intersecting_sector_allowed_transverses=translations,
    cases=records,
    offstrip_lower_bound=f'initial mass >= 11*n - {widthsum} - |C|',
    offstrip_boundary_loss=widthsum,
    source_sha256={str(SOURCE.relative_to(ROOT)):hashlib.sha256(SOURCE.read_bytes()).hexdigest()})
(HERE/'reverse108_interface_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('cases','H_word','P_word','H_mature_black','P_required_black','P_output_black')},indent=2))
