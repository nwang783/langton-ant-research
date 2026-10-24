"""Independent orchestration of the stable all-(m,n) complete-field claim."""
import json,hashlib
from pathlib import Path
from bivariate import A,infinite_tail
HERE=Path(__file__).resolve().parent
M=(1,0,100);N=(1,1,200)

def main():
    T=json.loads((HERE/'template.json').read_text())
    for key in A.STATS:A.STATS[key]=0
    A.READ_POINTS.clear();A.READ_RAYS.clear()
    def lin(variable,a,b):return A.add(A.scale(variable,a),(0,0,b))
    s=(lin(M,-2,-23),lin(M,2,31))
    q=(lin(N,-2,-33),lin(N,-2,-14))
    a=(lin(N,-2,-33),lin(N,2,41))
    c=(lin(N,2,8),lin(N,-2,-14))
    d=(lin(N,2,8),lin(N,2,41))
    inputs=[s,q,a,c,d]
    for i,x in enumerate(inputs):
        for y in inputs[i+1:]:assert A.no_point_collision(x,y)
    counts={1:lin(N,1,8),3:lin(N,1,7),5:M,7:lin(M,1,2),9:lin(N,1,-20),11:A.add(A.add(N,M),(0,0,10))}
    standard={A.W[i:]+A.W[:i] for i in range(104)}
    field=A.Field(inputs);p=A.point(0,0);h=0;t=A.ZERO
    for i,segment in enumerate(T['segments']):
        word=segment['word'];assert word and set(word)<={'R','L'}
        data=A.word_data(word,h)
        if segment['type']=='finite':
            p=A.apply_finite(field,data,p,0,str(i));t=A.add(t,(0,0,len(word)))
        else:
            assert segment['type']=='periods' and word in standard and len(word)==104
            assert data[3]==h and A.nonneg(A.sub(counts[i],A.ONE))
            p=A.apply_periods(field,data,p,0,counts[i],str(i));t=A.add(t,A.scale(counts[i],104))
        h=data[3]
        print('checked segment',i,'time',t,'pose',p,h,flush=True)
    assert t==A.add(A.add(A.scale(N,416),A.scale(M,312)),(0,0,197704))
    assert p==(lin(M,-2,-28),lin(M,2,68)) and h==0
    word=T['infinite_tail_word'];assert word in standard
    tail=A.word_data(word,h);assert tail[2]==(-2,2) and tail[3]==h
    proof=infinite_tail(field,tail,p)
    for target in (a,d):
        assert all(A.no_point_collision(target,x) for x in A.READ_POINTS)
        assert all(not A.ray_membership(target,b,e,count) for b,e,count in A.READ_RAYS)
        for x in tail[0]:
            k=A.line_coordinate(A.psub(target,A.translate_local(x,p,0)),tail[2])
            assert k is None or A.negative(k)
    stats=dict(A.STATS)
    # An otherwise identical capture field with one future toggle must fail.
    marker=A.padd(A.translate_local(sorted(tail[0])[0],p,0),tuple(A.scale((0,0,10**60),x) for x in tail[2]))
    field.add_points([marker])
    try:infinite_tail(field,tail,p)
    except AssertionError as exc:
        assert exc.args[0][0]=='bivariate infinite-tail mismatch'
    else:raise AssertionError('10^60-period blocker incorrectly accepted')
    field.add_points([marker])
    out=dict(status='PASS: independent all-parameter complete-field replay',domain='m>=100, n>=m+100',
             capture_time=t,capture_pose=[p,h],tail=proof,never_read=['a','d'],statistics=stats,
             negative_control='10^60-period future blocker rejected',
             template_sha256=hashlib.sha256((HERE/'template.json').read_bytes()).hexdigest())
    (HERE/'independent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
