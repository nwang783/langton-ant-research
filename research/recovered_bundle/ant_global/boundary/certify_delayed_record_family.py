"""Exact finite certificate for a translated remote-marker record family.

The infinite quantifiers use translation-orbit thresholds, not a long test.
Coordinates/headings follow check.py: E,S,W,N = 0,1,2,3.
"""
import json
from pathlib import Path
from check import DIR, run

ROOT=Path(__file__).resolve().parent
SEED={(1,-7),(-1,-6),(-3,-6),(-2,-5)}
HEAD=(0,-7); HEADING=3
P=104; START=182; DRIFT=(-2,2)
MARKER=(-18,13); IMPACT=852; EXIT=970

def add(v,k=1): return (v[0]+k*DRIFT[0],v[1]+k*DRIFT[1])

def ray_index(v,w):
    """Return k if v=w+k*DRIFT, otherwise None."""
    dx=v[0]-w[0];dy=v[1]-w[1]
    if dx%DRIFT[0]: return None
    k=dx//DRIFT[0]
    return k if dy==k*DRIFT[1] else None

def main():
    pre, base, pose=run(SEED,HEAD,HEADING,START)
    period, endboard, endpose=run(base,pose[:2],pose[2],P)
    assert endpose==(*add(pose[:2]),pose[2])
    positions=[(e[1],e[2]) for e in period]
    colors=[e[4] for e in period]
    word=''.join('L' if c else 'R' for c in colors)

    # At phase i in period k, previous hits arise from p_j=p_i+m*d,
    # with m>0,k>=m, or m=0,j<i. Initial-board membership also changes
    # only at finitely many indices k. Check beyond every such threshold.
    K=0
    for i,v in enumerate(positions):
        for w in positions:
            m=ray_index(w,v)
            if m is not None and m>0: K=max(K,m)
        for w in base:
            m=ray_index(w,v)
            if m is not None and m>=0: K=max(K,m+1)
    checks=0
    for k in range(K+1):
        for i,v in enumerate(positions):
            c=int(add(v,k) in base)
            for j,w in enumerate(positions):
                m=ray_index(w,v)
                if m is not None and ((m>0 and k>=m) or (m==0 and j<i)):
                    c^=1
            assert c==colors[i],(k,i,c,colors[i])
            checks+=1
    assert max(x+y for x,y in positions)==0
    assert max(e[1]+e[2] for e in pre)<=0

    baseline, baseline_board, baseline_pose=run(SEED,HEAD,HEADING,IMPACT)
    assert baseline_pose[:2]==MARKER
    # Every marker n has its first baseline hit at IMPACT+n*P.
    for e in pre:
        k=ray_index((e[1],e[2]),MARKER)
        assert k is None or k<0
    hits=[]
    for i,v in enumerate(positions):
        k=ray_index(MARKER,v)
        if k is not None:
            assert k>=0
            hits.append(START+k*P+i)
    assert min(hits)==IMPACT

    actual, actualboard, actualpose=run(SEED|{MARKER},HEAD,HEADING,EXIT)
    assert all(e[1]+e[2]<=0 for e in actual)
    assert sum(actualpose[:2])==1
    assert actual[:IMPACT]==baseline
    legal10={(word+word)[i:i+10] for i in range(P)}
    actualword=''.join('L' if e[4] else 'R' for e in actual)
    forbidden10=sum(actualword[i:i+10] not in legal10 for i in range(len(actualword)-9))
    assert len(legal10)==84 and forbidden10==96
    suffix=actual[IMPACT:]
    footprint={(e[1],e[2]) for e in suffix}

    # At t_n=IMPACT+n*P, the baseline color of v+n*d is an explicit
    # finite-threshold function of n. All thresholds are tested, so the
    # translated suffix sees the same colors for every n>=0.
    k0,phase=divmod(IMPACT-START,P)
    N=0
    for v in footprint:
        for w in base:
            n=ray_index(w,v)
            if n is not None and n>=0: N=max(N,n+1)
        for j,w in enumerate(positions):
            m=ray_index(v,w)
            if m is not None and (m<k0 or (m==k0 and j<phase)):
                N=max(N,max(0,-m))
    orbit_checks=0
    for v in footprint:
        reference=int(v in baseline_board)
        for n in range(N+1):
            c=int(add(v,n) in base)
            for j,w in enumerate(positions):
                m=ray_index(v,w)
                if m is not None and m+n>=0 and (m<k0 or (m==k0 and j<phase)):
                    c^=1
            assert c==reference,(v,n,c,reference)
            orbit_checks+=1

    # Locate the preceding record cut, entering cap zero from cap -2.
    black_old=next(e[0] for e in baseline if e[1]+e[2]==-2 and e[4] and e[3]==0)
    cut0=black_old-(2 if baseline[black_old-1][4]==0 else 4)
    assert sum(baseline[cut0][1:3])==-4
    prefix0,board0,pose0=run(SEED,HEAD,HEADING,cut0)
    assert all(x+y<=-2 for x,y in board0)
    q0=4*sum(x+y==-2 for x,y in board0)-sum(x+y==-3 for x,y in board0)
    black_top=EXIT-1
    assert actual[black_top][4] and actual[black_top][1]+actual[black_top][2]==0
    cut1=black_top-(2 if actual[black_top-1][4]==0 else 4)
    assert sum(actual[cut1][1:3])==-2
    na=sum(e[1]+e[2]==-1 for e in actual[cut0:cut1])
    m=sum(e[1]+e[2]==0 for e in actual[cut0:cut1])
    da=sum(1-2*e[4] for e in actual[cut0:cut1] if e[1]+e[2]==-1)
    assert na==4*m-da
    period_na=sum(x+y==-1 for x,y in positions)
    period_m=sum(x+y==0 for x,y in positions)
    assert (period_na,period_m)==(7,2)
    record={
      'status':'exact_infinite_family_certificate_passed',
      'seed':sorted(SEED),'head':[*HEAD,HEADING],
      'period_start':START,'period':P,'drift':DRIFT,'word':word,
      'periodic_ray_last_threshold':K,'periodic_ray_checks':checks,
      'marker':MARKER,'marker_n':'marker+n*drift, n>=0',
      'impact_time':'852+104*n','first_cap_exit_time':'970+104*n',
      'exit_pose_n':[actualpose[0],actualpose[1],actualpose[2]],
      'translated_suffix_steps':len(suffix),'suffix_footprint':len(footprint),
      'suffix_last_threshold':N,'suffix_color_checks':orbit_checks,
      'initial_adaptive_cut':cut0,'initial_cut_pose':pose0,
      'initial_active_energy':q0,'initial_active_rows':{
        str(row):sorted((x,y) for x,y in board0 if x+y==row) for row in [-2,-3]},
      'final_adaptive_cut':'%d+104*n'%cut1,
      'final_adaptive_cut_pose':actual[cut1][1:4],
      'inherited_next_energy':'%d+7*n'%na,
      'top_visits':'%d+2*n'%m,
      'initial_marker_row':sum(MARKER),
      'legal_cyclic_standard_10_windows':len(legal10),
      'forbidden_10_windows_before_first_exit':forbidden10,
      'forbidden_window_scope':'Exactly 96 for every n>=0 by insertion of complete periodic copies; only windows wholly before first exit, not future events.',
      'scope':'No bound on next active energy from current active rows alone; not a counterexample to highway capture.'
    }
    (ROOT/'delayed_record_family_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))

if __name__=='__main__': main()
