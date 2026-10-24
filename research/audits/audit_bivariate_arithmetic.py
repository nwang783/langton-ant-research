"""Independent Bezout-interval oracle, not bounded parameter sampling."""
import json,random,sys
from pathlib import Path
ROOT=Path('/workspace/shared/langton')
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
import bivariate as b

def egcd(a,b):
    r0,r1=a,b;x0,x1=1,0;y0,y1=0,1
    while r1:
        q,r=r0//r1,r0%r1
        r0,r1=r1,r;x0,x1=x1,x0-q*x1;y0,y1=y1,y0-q*y1
    assert a*x0+b*y0==r0
    return r0,x0,y0

def family(f):
    a,c,z=f
    if a==c==0:return 'all' if z==0 else None
    g,x,y=egcd(abs(a),abs(c))
    if (-z)%g:return None
    x*=(-z)//g*(1 if a>=0 else -1)
    y*=(-z)//g*(1 if c>=0 else -1)
    dx,dy=c//g,-a//g
    lower=upper=None
    for origin,step in ((x,dx),(y,dy)):
        if step==0:
            if origin<0:return None
        elif step>0:
            bound=-((-(-origin))//step)  # ceil(-origin/step)
            lower=bound if lower is None else max(lower,bound)
        else:
            bound=(-origin)//step
            upper=bound if upper is None else min(upper,bound)
    if lower is not None and upper is not None and lower>upper:return None
    return x,y,dx,dy,lower,upper

def point_collision(f,g):
    sol=family(f)
    if sol is None:return False
    if sol=='all':return family(g) is not None
    x,y,dx,dy,lo,hi=sol
    a,c,z=g;constant=a*x+c*y+z;step=a*dx+c*dy
    if step==0:return constant==0
    if (-constant)%step:return False
    k=(-constant)//step
    return (lo is None or k>=lo) and (hi is None or k<=hi)

def implementation_collision(f,g):
    try:return not b.no_point_collision((f,g),(b.ZERO,b.ZERO))
    except AssertionError as exc:
        assert exc.args[0][0]=='bivariate point incidence'
        return True

rng=random.Random(20261022)
scalar_count=point_count=0
for i in range(12000):
    scale=10**(i%61)
    f=tuple(rng.randrange(-20,21)*scale+rng.randrange(-3,4) for _ in range(3))
    if i%5==0:
        u,v=rng.randrange(5)*scale,rng.randrange(5)*scale
        f=f[:2]+(-f[0]*u-f[1]*v,)
    assert b.has_nonnegative_zero(f)==(family(f) is not None),f
    scalar_count+=1
    g=tuple(rng.randrange(-20,21)*scale+rng.randrange(-3,4) for _ in range(3))
    if i%7==0:g=tuple(3*q for q in f)
    elif i%5==0:g=g[:2]+(-g[0]*u-g[1]*v,)
    assert implementation_collision(f,g)==point_collision(f,g),(f,g)
    point_count+=1
for f in ((0,0,0),(0,0,1),(0,1,0),(0,-1,1),(1,0,-10**100),(-1,1,10**100)):
    assert b.has_nonnegative_zero(f)==(family(f) is not None)
    for g in ((0,0,0),(0,0,1),(1,-1,0)):
        assert implementation_collision(f,g)==point_collision(f,g)
out=dict(status='PASS: independent exact Bezout interval oracle agrees',
         scalar_cases=scalar_count,point_cases=point_count,
         maximum_generated_scale='10^60',extra_exact_controls='10^100',
         scope='Implementation controls; theorem quantifiers follow from audited arithmetic derivation.')
(ROOT/'audits/bivariate_arithmetic_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
