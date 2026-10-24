"""All-parameter guard for 16-cell corner-block families.

Family: union of 2x2 blocks with lower-left corners
(a + sx*2*n, a-u + sy*2*n), sx,sy in {-1,+1}.
Start (0,0),N. Parameters a=0,1; u=-29,-27,...,-17; n>=34.
"""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ant_exact import step,plan,certify_period,multiple,PHASES,W
from single_blocks import REFERENCE,block

N=34;d=(-2,-2)
def shift(S,v):return {(x+v[0],y+v[1]) for x,y in S}

def first_hit_formula(a,u):
    B,p,h,prefix=REFERENCE
    qs,hs,end,eh=plan(W,p,h)
    candidates=[]
    for b in block((a,a-u)):
        for i,q in enumerate(qs):
            j=multiple((b[0]-q[0],b[1]-q[1]),d)
            if j is not None:candidates.append((104*j+i,j,i,b))
    c,j,i,b=min(candidates)
    assert N+j>=0
    # All first differences are among this finite list of rays.
    assert all(N+v[1]>=0 for v in candidates)
    return c,i,candidates

def incoming_at(a,u,n,hit):
    B0,p,h,_=REFERENCE
    B=set(B0)
    for j in range(hit):
        p,h,c=step(B,p,h)
        assert c==W[j%104]
    return shift(B,(2*n,2*n))|block((a,a-u)),(p[0]+2*n,p[1]+2*n),h

def certificate(a,u,result):
    base,p0,h0,prefix=REFERENCE
    c,phase,candidates=first_hit_formula(a,u)
    hit=104*N+c
    assert hit==result['first_hit_offset']+104*(N-result['n'])
    # All four initial blocks miss the blank prefix, uniformly in n>=N.
    xmin=min(x for x,y in prefix);xmax=max(x for x,y in prefix)
    ymin=min(y for x,y in prefix);ymax=max(y for x,y in prefix)
    assert a-2*N+1<xmin and a+2*N>xmax
    # So every block misses by x alone; this remains strict as n grows.
    # Before the SW hit, NW and SE blocks miss the whole standard band.
    qs,_,_,_=plan(W,p0,h0)
    umin=min(x-y for x,y in qs);umax=max(x-y for x,y in qs)
    assert u-4*N+1<umin and u+4*N-1>umax
    # The NE block is above every x coordinate on the forward SW ray.
    assert a+2*N>max(x for x,y in qs)

    B,p,h=incoming_at(a,u,N,hit)
    B1,p1,h1=incoming_at(a,u,N+1,hit+104)
    assert (p,h)==(p1,h1)
    E=B^B1
    recovery=result['recovery_bound']
    reads=[];word=''
    for _ in range(recovery):
        reads.append(p);p,h,c0=step(B,p,h);word=(word+c0)[-104:]
    assert PHASES[word]==result['word_phase']
    cert=certify_period(B,p,h,word)
    assert cert
    tail,_,end,eh=plan(word,p,h)
    out_d=(end[0]-p[0],end[1]-p[1])
    assert sum(out_d)<=0
    H=max(x+y for x,y in reads+tail+[p])
    E_min=min(x+y for x,y in E)
    assert E_min>H
    # Every extra old-state difference E translates by (2,2) as n grows.
    # Every non-SW corner block has normalized coordinate sum at least
    # 4*n+2*a-u, hence misses the same guard for every n>=N.
    other_min=4*N+2*a-u
    assert other_min>H
    return {'a':a,'u':u,'n_min':N,'hit_offset_formula':{'n_coefficient':104,'constant':c},
            'first_hit_pose_normalized':p1,'first_hit_heading':h1,
            'recovery_updates':recovery,'protected_halfplane_sum_max':H,
            'remote_source_difference_min_sum':E_min,'remote_source_difference_size':len(E),
            'other_corner_min_sum_at_n_min':other_min,
            'tail_drift':out_d,'tail_phase':PHASES[word],
            'tail_certificate':cert,
            'standard_time_bound':{'n_coefficient':104,'constant':9977+c+recovery},
            'source_change_E':sorted(E),
            'first_hit_ray_candidates':[list(z[:3])+[list(z[3])] for z in candidates]}

def main():
    data=json.loads(Path(__file__).with_name('single_blocks_results.json').read_text())
    rows=[]
    for r in data:
        if r['n']!=64:continue
        rec=certificate(r['a'],r['u'],r)
        rows.append(rec)
        print(json.dumps({k:v for k,v in rec.items() if k not in ('source_change_E','first_hit_ray_candidates')}),flush=True)
    assert len(rows)==14
    Path(__file__).with_name('corner_blocks_guard_certificate.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':main()
