#!/usr/bin/env python3
"""Exact finite all-placement reconstruction for the P108 rail-bundle lemma.

No words, periods, cap lengths, or numerical spatial radii are searched.
Placements are generated exhaustively by black-class intersection anchors.
"""
import hashlib, itertools, json, pathlib
from flat_collinear_validator import trace

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
P_SOURCE=ROOT/'causal_reduction/unit_scale/reverse108_prepared_control.json'
P=json.loads(P_SOURCE.read_text())['word']

def profile(word,h):
    rr,d,hh=trace(word,h);assert hh==h and d in ((2,2),(-2,-2))
    groups={}
    for (x,y),i,c in rr:
        cls=(x-y,x%2);k=(x-cls[1])//d[0]
        groups.setdefault(cls,[]).append((i-len(word)*k,c))
    for vv in groups.values():
        vv.sort();assert all(a[1]!=b[1] for a,b in zip(vv,vv[1:]))
    return groups

def shift(s,t,p):return {(a+t,(e+p)%2) for a,e in s}

def main():
    pp=profile(P,3);readP=set(pp);blackP={s for s,a in pp.items() if a[0][1]=='L'}
    whiteP=readP-blackP
    writers={}
    for name,h in [('NE',1),('SW',3)]:
        hp=profile(H,h);assert all(a[0][1]=='R' for a in hp.values())
        R=set(hp);B={s for s,a in hp.items() if a[-1][1]=='R'}
        lo=min(t for t,e in R);hi=max(t for t,e in R)
        assert hi-lo==10 and R=={(t,e) for t in range(lo,hi+1) for e in (0,1)}
        assert all((t,e) in B for t in (lo,hi) for e in (0,1))
        assert len(R)==22 and len(B)==12
        writers[name]=(R,B)
    assert len(readP)==23 and len(blackP)==11
    assert max(t for t,e in blackP)-min(t for t,e in blackP)==10
    opts=[]
    for name,(R,B) in writers.items():
        placements={(tp-tw,(ep-ew)%2) for tp,ep in blackP for tw,ew in B if (tp-tw)%2==0}
        for t,p in sorted(placements):
            opts.append(dict(writer=name,normal=t,x_parity=p,read=shift(R,t,p),black=shift(B,t,p)))
    singles=[];pairs=[]
    def discrepancy(B):
        return sorted(blackP-B),sorted(whiteP&B)
    def label(o):return {k:v for k,v in o.items() if k not in ('read','black')}
    for o in opts:
        missing,polluted=discrepancy(o['black']);assert missing or polluted
        singles.append(dict(**label(o),missing_black=missing,polluted_white=polluted))
    for a,b in itertools.combinations(opts,2):
        if a['read']&b['read']:continue
        missing,polluted=discrepancy(a['black']|b['black']);assert missing or polluted
        pairs.append(dict(writers=[label(a),label(b)],missing_black=missing,polluted_white=polluted))
    # Exact endpoint-window constants in the common (2,2) orbit gauge.
    Pk=[(q[0]-q[0]%2)//2 for q,i,c in trace(P,3)[0]]
    pwidth=max(Pk)-min(Pk);assert pwidth==2
    hw=[]
    for h in (1,3):
        for offset_parity in (0,1):
            kk=[(offset_parity+q[0]-(offset_parity+q[0])%2)//2 for q,i,c in trace(H,h)[0]]
            hw.append(max(kk)-min(kk))
    assert max(hw)==3
    pnormal_lo=min(t for t,e in readP);pnormal_hi=max(t for t,e in readP)
    enlarged_normals=(pnormal_lo-10,pnormal_hi+10)
    enlarged_class_count=2*(enlarged_normals[1]-enlarged_normals[0]+1)
    assert enlarged_normals==(-17,14) and enlarged_class_count==64
    out=dict(status='PASS exhaustive finite all-placement rail-bundle reconstruction',
             scope='Fixed P108, all conserved-sector unions of compatible parallel standard-white rails; no pump or cap synthesis.',
             consumer_heading=3,consumer_word=P,required_black_classes=sorted(blackP),
             full_read_classes=sorted(readP),anchored_single_cases=len(singles),
             compatible_unordered_pair_cases=len(pairs),matching_cases=0,
             singles=singles,pairs=pairs,
             completeness='Every contributing rail hits one required-black class, generating an anchor. At most two disjoint11-normal bands meet the11-normal required-black span. Noncontributors cannot repair missing blacks and can only pollute whites. Rotation by180 degrees covers the other consumer orientation.',
             common_gauge_consumer_endpoint_loss=pwidth,
             maximum_parallel_writer_phase_width=max(hw),
             enlarged_relevant_writer_normal_band=enlarged_normals,
             enlarged_relevant_writer_full_drift_classes=enlarged_class_count,
             finite_flight_lower_bound='|B| >= n-2-6*r_parallel-L-1408*r_nonparallel',
             per_nonparallel_flight_exception_bound=22*enlarged_class_count,
             source_sha256={str(P_SOURCE.relative_to(ROOT)):hashlib.sha256(P_SOURCE.read_bytes()).hexdigest(),
                            pathlib.Path(__file__).name:hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()})
    (HERE/'standard_flight_P108_obstruction_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('consumer_word','required_black_classes','full_read_classes','singles','pairs')},indent=2))

if __name__=='__main__':main()
