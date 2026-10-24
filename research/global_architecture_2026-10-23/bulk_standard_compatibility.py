#!/usr/bin/env python3
"""Exact finite bulk-input criterion for ONE supplied periodic word P.

Does not search consumers, periods, refinements, caps, or finite itineraries.
MATCH is only a necessary bulk preparation interface, not a physical compiler.
INCOMPATIBLE supplies the hypothesis of the finite-flight fuel/routing lemma.
"""
import argparse, hashlib, itertools, json, math, pathlib, subprocess, time
from flat_collinear_validator import trace, multiple

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']

def finite_conflict(word,h):
    last={}
    for p,i,c in trace(word,h)[0]:
        if p in last and last[p][1]==c:
            return dict(cell=p,earlier=last[p][0],later=i,turn=c)
        last[p]=(i,c)
    return None

def orbit_histories(word,h):
    rows,d,hh=trace(word,h)
    if d==(0,0):raise ValueError('nonzero drift required')
    groups=[]
    for p,i,c in rows:
        for rep,gg in groups:
            k=multiple((p[0]-rep[0],p[1]-rep[1]),d)
            if k is not None:break
        else:rep=p;gg=[];groups.append((rep,gg));k=0
        gg.append((i-len(word)*k,i,k,c))
    for rep,gg in groups:gg.sort()
    return groups,d,hh

def diagonal_profile(word,h,l):
    rr,d,hh=trace(word,h)
    assert hh==h and d in ((l,l),(-l,-l))
    out={}
    for (x,y),i,c in rr:
        s=(x-y,x%l);k=(x-s[1])//d[0]
        out.setdefault(s,[]).append((i-len(word)*k,i,k,c))
    for a in out.values():a.sort()
    return out

def solve_cover(candidates,black_count):
    """Complete finite search on rail selectors, not a consumer search."""
    target=(1<<black_count)-1
    usable=[i for i,c in enumerate(candidates) if not c['polluted_white']]
    bybit=[[i for i in usable if candidates[i]['cover_mask']>>b&1] for b in range(black_count)]
    memo=set();nodes=0
    def compatible(a,b):
        aa=candidates[a]['band'];bb=candidates[b]['band']
        return aa[1]<bb[0] or bb[1]<aa[0]
    def visit(chosen,covered):
        nonlocal nodes
        nodes+=1
        if covered==target:return chosen
        key=tuple(sorted(chosen))
        if key in memo:return None
        memo.add(key)
        best=None
        for b in range(black_count):
            if covered>>b&1:continue
            choices=[i for i in bybit[b] if all(compatible(i,j) for j in chosen)]
            if not choices:return None
            if best is None or len(choices)<len(best):best=choices
        for i in best:
            r=visit(chosen+[i],covered|candidates[i]['cover_mask'])
            if r is not None:return r
        return None
    return visit([],0),dict(nodes=nodes,memo_states=len(memo))

def criterion(P,h=3):
    if not P or not isinstance(P,str) or not set(P)<=set('RL'):
        raise ValueError('a nonempty literal P is required')
    if type(h) is not int or not 0<=h<4:raise ValueError('heading must be0..3')
    rr,dp,hp=trace(P,h)
    base=dict(word=P,heading=h,length=len(P),drift=dp,
              word_sha256=hashlib.sha256(P.encode()).hexdigest())
    if hp!=h or dp==(0,0):
        order=4//math.gcd((hp-h)%4,4)
        _,superd,_=trace(P*order,h)
        assert superd==(0,0)
        conflict=finite_conflict(P*(2*order),h)
        # A missing conflict would yield an exact finite-state cycle, contrary
        # to the retained strict integer clock. Do not silently accept it.
        if conflict is None:raise ArithmeticError('unexpected legal zero-drift recurrence')
        return dict(**base,status='FINITE_POWER_CONFLICT',copies_tested=2*order,
                    conflict=conflict,scope='Exact finite chronology obstruction; no bulk construction.')
    groups,_,_=orbit_histories(P,h)
    for rep,a in groups:
        if any(x[3]==y[3] for x,y in zip(a,a[1:])):
            width=max(x[2] for x in a)-min(x[2] for x in a)
            return dict(**base,status='INTERNAL_BULK_CONFLICT',representative=rep,
                        history=a,complete_history_loss=width,
                        impossible_when=f'n>{width}')
    blackgroups=[(rep,a) for rep,a in groups if a[0][3]=='L']
    if abs(dp[0])!=abs(dp[1]) or dp[0]==0:
        if not blackgroups:return dict(**base,status='MATCH_EMPTY_WHITE_PROFILE',parallel_standard_direction=False)
        rep,a=min(blackgroups,key=lambda z:max(x[2] for x in z[1])-min(x[2] for x in z[1]))
        width=max(x[2] for x in a)-min(x[2] for x in a)
        return dict(**base,status='INCOMPATIBLE',parallel_standard_direction=False,
                    reason='No standard direction is parallel; a required-L orbit cannot be supplied remotely.',
                    required_black_representative=rep,complete_history_loss=width,
                    lower_bound=f'|B|>=n-{width}-L-22*F')
    # Rotate the supplied geometry, without changing its R/L word, until its
    # drift is(-a,-a). This is an exact rotation of the physical ant.
    for rotation in range(4):
        hn=(h+rotation)%4;_,d,_=trace(P,hn)
        if d[0]==d[1] and d[0]<0:break
    else:raise AssertionError('diagonal normalization failed')
    a=-d[0];l=math.lcm(a,2);q=l//a;rh=l//2;Q=P*q
    qp=diagonal_profile(Q,hn,l)
    assert all(all(x[3]!=y[3] for x,y in zip(v,v[1:])) for v in qp.values())
    read=sorted(qp);black=sorted(s for s,v in qp.items() if v[0][3]=='L')
    white=set(read)-set(black);bindex={s:i for i,s in enumerate(black)}
    normal_lo=min(t for t,e in read);normal_hi=max(t for t,e in read)
    kk=[(p[0]-p[0]%l)//l for p,i,c in trace(Q,hn)[0]]
    wp=max(kk)-min(kk)
    wh=0
    for hw in (1,3):
        wr=trace(H*rh,hw)[0]
        for offset in range(l):
            vals=[(offset+p[0]-(offset+p[0])%l)//l for p,i,c in wr]
            wh=max(wh,max(vals)-min(vals))
    cpar=2*wh+104*(rh-1)
    cperp=22*l*(normal_hi-normal_lo+21)
    constants=dict(superperiod_copies=q,common_drift=[l,l],standard_superperiods=rh,
                   consumer_endpoint_loss=wp,standard_endpoint_width=wh,
                   parallel_flight_loss=cpar,nonparallel_flight_loss=cperp,
                   cap_loss_per_read=1,
                   lower_bound=f'|B|>=floor(n/{q})-{wp}-L-{cpar}*r_parallel-{cperp}*r_nonparallel')
    out=dict(**base,parallel_standard_direction=True,normalized_heading=hn,
             normalization_quarter_turns=rotation,diagonal_scale=a,
             read_classes=read,required_black_classes=black,
             constants=constants)
    if not black:return dict(**out,status='MATCH_EMPTY_WHITE_PROFILE',rails=[])
    candidates=[]
    for orientation,hw in [('NE',1),('SW',3)]:
        hp=diagonal_profile(H,hw,2)
        R=set(hp);B={s for s,v in hp.items() if v[-1][3]=='R'}
        assert all(v[0][3]=='R' for v in hp.values())
        lo=min(t for t,e in R);hi=max(t for t,e in R)
        assert R=={(t,e) for t in range(lo,hi+1) for e in (0,1)} and hi-lo==10
        assert all((t,e) in B for t in (lo,hi) for e in (0,1))
        placements={(tb-tw,(eb-ew)%2) for tb,eb in black for tw,ew in B
                    if (tb-tw)%2==(hn-1)%2}
        for t,p in sorted(placements):
            black_here={s for s in read if (s[0]-t,(s[1]-p)%2) in B}
            cover=black_here&set(black);polluted=sorted(black_here&white)
            mask=sum(1<<bindex[s] for s in cover)
            assert mask
            candidates.append(dict(orientation=orientation,normal=t,x_parity=p,
                                   band=[lo+t,hi+t],covered_black=sorted(cover),
                                   polluted_white=polluted,cover_mask=mask))
    clauses=[]
    for i,c in enumerate(candidates):
        if c['polluted_white']:clauses.append([-(i+1)])
    for b in range(len(black)):
        clauses.append([i+1 for i,c in enumerate(candidates) if c['cover_mask']>>b&1])
    for i,j in itertools.combinations(range(len(candidates)),2):
        a1,a2=candidates[i]['band'],candidates[j]['band']
        if not (a1[1]<a2[0] or a2[1]<a1[0]):clauses.append([-(i+1),-(j+1)])
    model,stats=solve_cover(candidates,len(black))
    status='INCOMPATIBLE' if model is None else 'MATCH_STANDARD_RAIL_BUNDLE'
    if model is not None:
        selected={i+1 for i in model}
        assert all(any((x>0)==(abs(x) in selected) for x in cc) for cc in clauses)
    return dict(**out,status=status,candidates=candidates,selector_variables=len(candidates),
                selector_clauses=len(clauses),selector_search=stats,
                matching_rail_indices=model,
                matching_rails=None if model is None else [candidates[i] for i in model],
                _clauses=clauses)

def certify_cnf(result,base):
    """Optional solver-independent RUP certificate using retained local tools."""
    if '_clauses' not in result:return None
    cnf=base.with_suffix('.cnf');rup=base.with_suffix('.rup')
    clauses=result['_clauses'];n=result['selector_variables']
    cnf.write_text(f'p cnf {n} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses))
    if result['status']!='INCOMPATIBLE':return dict(cnf=str(cnf),proof_required=False)
    binaries=ROOT/'causal_reduction/morphic_candidates'
    r=subprocess.run([str(binaries/'prove_cnf_rup'),str(cnf),str(rup),'100000'],capture_output=True,text=True,timeout=120)
    if r.returncode!=0:
        return dict(cnf=str(cnf),producer_returncode=r.returncode,producer=r.stdout,certificate='NOT_OBTAINED')
    s=subprocess.run([str(binaries/'check_drat'),str(cnf),str(rup)],capture_output=True,text=True,timeout=120)
    if s.returncode!=0:raise ArithmeticError('RUP checker rejected: '+s.stdout+s.stderr)
    report=json.loads(s.stdout)
    assert report['valid'] and report['RAT']==0 and report['deletions']==0
    return dict(cnf=str(cnf),proof=str(rup),checker=report,
                cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest(),
                proof_sha256=hashlib.sha256(rup.read_bytes()).hexdigest())

def public(r):return {k:v for k,v in r.items() if not k.startswith('_')}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('input',type=pathlib.Path,help='JSON object containing P and optional heading')
    ap.add_argument('--output',type=pathlib.Path)
    ap.add_argument('--cnf-base',type=pathlib.Path)
    args=ap.parse_args();x=json.loads(args.input.read_text());start=time.monotonic()
    r=criterion(x['P'],x.get('heading',3))
    if args.cnf_base:r['cnf_certificate']=certify_cnf(r,args.cnf_base)
    r['seconds']=time.monotonic()-start
    rendered=json.dumps(public(r),indent=2)+'\n'
    if args.output:args.output.write_text(rendered)
    else:print(rendered,end='')

if __name__=='__main__':main()
