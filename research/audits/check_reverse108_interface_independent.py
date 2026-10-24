#!/usr/bin/env python3
"""Independent literal full-drift histories and all-translation interface audit."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
NOTE=ROOT/'global_architecture_2026-10-23/reverse108_flat_interface_exclusion.md'
CERT=ROOT/'global_architecture_2026-10-23/reverse108_interface_certificate.json'
SUP=ROOT/'causal_reduction/unit_scale/reverse108_prepared_control.json'
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
cert=json.loads(CERT.read_text()); P=json.loads(SUP.read_text())['word']
rev=''.join({'R':'L','L':'R'}[c] for c in H[::-1]); assert rev[31]=='L'
assert P==rev[:31]+'LRRRR'+rev[32:]
def literal(w,h):
    p=0j; rows=[]; dirs=[1j,1,-1j,-1]
    for i,c in enumerate(w):
        rows.append((int(p.real),int(p.imag),i,c))
        h=(h+(1 if c=='R' else -1))%4;p+=dirs[h]
    return rows,(int(p.real),int(p.imag)),h

def histories(w,h):
    raw,d,hh=literal(w,h); assert hh==h and d[0]==d[1] and abs(d[0])==2
    groups={}
    for x,y,i,c in raw:
        key=(x-y,x%2); rep=(key[1],key[1]-key[0]); k=(x-rep[0])//d[0]
        assert (rep[0]+k*d[0],rep[1]+k*d[1])==(x,y)
        groups.setdefault(key,[]).append((i-len(w)*k,i,k,c))
    for rows in groups.values():
        rows.sort(); assert all(a[0]<b[0] and a[3]!=b[3] for a,b in zip(rows,rows[1:]))
    return groups,d
A,da=histories(H,1);B,db=histories(P,3)
assert da==(2,2) and db==(-2,-2)
assert all(v[0][3]=='R' for v in A.values())
Ab={s for s,v in A.items() if v[-1][3]=='R'}
Bi={s for s,v in B.items() if v[0][3]=='L'}
Bo={s for s,v in B.items() if v[-1][3]=='R'}
assert (len(A),len(Ab),len(B),len(Bi),len(Bo))==(22,12,23,11,3)
assert sorted(map(list,Ab))==cert['H_mature_black']
assert sorted(map(list,Bi))==cert['P_required_black']
assert sorted(map(list,Bo))==cert['P_output_black']
# Rebuild overlap domains from exact full quotient classes, including x parity.
records=[]
for parity in (0,1):
    shifts=sorted({a[0]-b[0] for a in A for b in B if (a[0]-b[0])%2==0 and (b[1]+parity)%2==a[1]})
    assert shifts==list(range(-10,11,2))
    for t in shifts:
        overlaps=[];conflicts=[];external=[]
        for b,rows in B.items():
            a=(b[0]+t,(b[1]+parity)%2)
            if a in A:
                overlaps.append(a)
                if (rows[0][3]=='L')!=(A[a][-1][3]=='R'):conflicts.append((b,a))
            elif rows[0][3]=='L':external.append(a)
        assert conflicts
        ref=next(r for r in cert['cases'] if r['cap_transverse']==t and r['cap_x_parity']==parity)
        assert (len(overlaps),len(conflicts),len(external))==(ref['overlapping_classes'],ref['conflicting_classes'],ref['exterior_required_black_classes'])
        one=ref['one_conflict'];b=tuple(one['P_class']);a=tuple(one['H_class']);assert (b,a) in conflicts
        assert list(map(list,B[b]))==one['P_rows'] and list(map(list,A[a]))==one['H_rows']
        records.append({'t':t,'parity':parity,'conflicts':len(conflicts)})
assert len(records)==22
loss=sum(max(row[2] for row in B[s])-min(row[2] for row in B[s]) for s in Bi)
assert loss==6==cert['offstrip_boundary_loss']
# Independently check exact finite-copy full-history intersection formula.
checks=0
for row in cert['cases']:
    b=tuple(row['one_conflict']['P_class']);a=tuple(row['one_conflict']['H_class'])
    pk=[v[2] for v in B[b]];hk=[v[2] for v in A[a]]
    for K in range(-7,8):
        for n in range(1,31):
            fullp=set.intersection(*({j+k for j in range(n)} for k in pk))
            # Physical position along +d is n+K-l; H copy index is n+K-l-hk.
            fullh=set.intersection(*({n+K-k-j for j in range(n)} for k in hk))
            lo=max(max(pk),K-min(hk)+1);hi=n+min(min(pk)-1,K-max(hk))
            D=lo-min(min(pk)-1,K-max(hk))-1
            assert fullp&fullh==set(range(lo,hi+1))
            assert len(fullp&fullh)==max(0,n-D)
            checks+=1
F={(H+H)[i:i+10] for i in range(104)}
triple=P*3
kap=sum(triple[108+i-10:108+i] not in F and triple[108+i-9:108+i+1] not in F for i in range(108))
assert kap==49==cert['cyclic_K']
out={'status':'PASS','sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (NOTE,CERT,SUP)},'all_full_drift_translation_cases':records,'offstrip_black_classes':11,'offstrip_width_loss':loss,'exact_boundary_interval_controls':checks,'cyclic_K':kap,'scope':'Every fixed cap in H^n C P108^n fails eventual all-n bounded-fuel legality. Prepared P108 remains valid. No cap synthesis or universal ant theorem.'}
path=ROOT/'audits/check_reverse108_interface_independent.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
