"""Independent complex-coordinate audit of the 14 unbounded-family leaves.

This file does not import ant_exact or either family simulator. It uses a
different tail checker: scan all epochs through the last possible change,
then use stabilization for every remaining epoch.
"""
import json
from pathlib import Path

W='LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR'
ROT={ 'R':-1j, 'L':1j }

def step(B,p,v):
    c='L' if p in B else 'R'
    if p in B:B.remove(p)
    else:B.add(p)
    v*=ROT[c]
    return p+v,v,c

def plan(w,p,v):
    qs=[]
    for c in w:
        qs.append(p);v*=ROT[c];p+=v
    return qs,p,v

def quotient(z,d):
    # Complex division is exact for this audit's small integer coordinates;
    # the equality below verifies the candidate in integer coordinates.
    r=z/d
    k=round(r.real)
    return k if k*d==z else None

def certify(B,p,v,w):
    qs,end,ev=plan(w,p,v);d=end-p
    assert ev==v and d!=0
    checks=0
    for i,q in enumerate(qs):
        initial={k for b in B if (k:=quotient(b-q,d)) is not None and k>=0}
        earlier=[]
        for j,r in enumerate(qs):
            m=quotient(r-q,d)
            if m is not None and (m>0 or m==0 and j<i):earlier.append(m)
        last=max([0,*initial,*earlier])+1
        for k in range(last+1):
            black=(k in initial)^bool(sum(m<=k for m in earlier)%2)
            assert black==(w[i]=='L')
            checks+=1
        # No initial hit or newly available earlier phase exists above last.
    return d,checks

def main():
    root=Path(__file__).parent
    rows=json.loads((root/'corner_blocks_guard_certificate.json').read_text())
    blank=set();bp=0j;bv=1j;prefix=set()
    for _ in range(9977):
        prefix.add(bp);bp,bv,c=step(blank,bp,bv)
    assert bp==-15+10j and bv==-1 and len(blank)==715
    bd,blank_checks=certify(blank,bp,bv,W)
    assert bd==-2-2j
    blank_reads,_,_=plan(W,bp,bv)
    prefix_x_bounds=(min(q.real for q in prefix),max(q.real for q in prefix))
    normal_bounds=(min(q.real-q.imag for q in blank_reads),max(q.real-q.imag for q in blank_reads))
    assert normal_bounds==(-28,-18)
    out=[];total_steps=0
    for row in rows:
        a,u,n=row['a'],row['u'],34
        seed={complex(a+2*s*n+i,a-u+2*t*n+j)
              for s in (-1,1) for t in (-1,1) for i in (0,1) for j in (0,1)}
        assert len(seed)==16
        B=set(seed);p=0j;v=1j;first=None;guard_max=-10**9
        tau=104*n+row['standard_time_bound']['constant']
        expected_hit=9977+104*n+row['hit_offset_formula']['constant']
        for t in range(tau):
            if first is None and p in seed:first=t
            if first is not None:guard_max=max(guard_max,int(p.real+p.imag)+4*n)
            p,v,c=step(B,p,v)
        total_steps+=tau
        assert first==expected_hit
        phase=row['tail_phase'];word=W[phase:]+W[:phase]
        d,checks=certify(B,p,v,word)
        assert (int(d.real),int(d.imag))==tuple(row['tail_drift'])
        qs,end,ev=plan(word,p,v)
        tail_max=max(int(q.real+q.imag)+4*n for q in qs)
        H=row['protected_halfplane_sum_max']
        assert max(guard_max,tail_max)<=H
        assert d.real+d.imag<=0
        E={complex(*q) for q in row['source_change_E']}
        # Recompute BOTH complete source fields with this independent simulator.
        source_fields=[]
        for m in (n,n+1):
            incoming=set(blank);ip=bp;iv=bv
            steps=104*m+row['hit_offset_formula']['constant']
            for t in range(steps):
                ip,iv,c=step(incoming,ip,iv)
                assert c==W[t%104]
            source_fields.append({q+2*m+2*m*1j for q in incoming})
        assert E==source_fields[0]^source_fields[1]
        assert len(E)==796
        assert min(int(q.real+q.imag) for q in E)==115>H
        assert 4*n+2*a-u>H
        # Affine exclusion of the blank prefix and other forward ray blocks.
        assert a-2*n+1<prefix_x_bounds[0] and a+2*n>prefix_x_bounds[1]
        assert u-4*n+1<normal_bounds[0] and u+4*n-1>normal_bounds[1]
        assert a+2*n>max(q.real for q in blank_reads)
        out.append({'a':a,'u':u,'first_hit':first,'certified_time':tau,
                    'all_future_epoch_checks':checks,'max_guard_sum':max(guard_max,tail_max),
                    'source_margin':115-H,'other_block_margin':4*n+2*a-u-H})
    result={'cases':len(out),'literal_steps':total_steps,'all_future_epoch_checks':sum(r['all_future_epoch_checks'] for r in out),
            'blank_reference_epoch_checks':blank_checks,
            'blank_prefix_x_bounds':prefix_x_bounds,'blank_forward_normal_bounds':normal_bounds,
            'minimum_source_margin':min(r['source_margin'] for r in out),
            'minimum_other_block_margin':min(r['other_block_margin'] for r in out),
            'rows':out}
    (root/'corner_blocks_independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))

if __name__=='__main__':main()
