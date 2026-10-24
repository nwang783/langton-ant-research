#!/usr/bin/env python3
"""Independent no-residue read relations and lexicographic consecutive reads."""
from pathlib import Path
import sys,json,hashlib,random,itertools,time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'global_architecture_2026-10-23'))
import flat_collinear_validator as candidate
from isl_exact import Context,Object,_FUN

def raw(w,h):
    x=y=0;out=[]; dirs=((0,1),(1,0),(0,-1),(-1,0))
    for t,c in enumerate(w):
        out.append((x,y,t,c));h=(h+(1 if c=='R' else 3))%4
        dx,dy=dirs[h];x+=dx;y+=dy
    return out,(x,y),h

def independent(U,C,V,h,n0,ctx):
    a,du,hu=raw(U,h); b,dc,hc=raw(C,h); c,dv,hv=raw(V,hc)
    atoms=[]
    for kind,rows in enumerate((a,b,c)):
        for x,y,i,turn in rows:
            if kind==0:dom=f'exists j: 0<=j<n and x={x}+{du[0]}*j and y={y}+{du[1]}*j and TIME={len(U)}*j+{i}'
            elif kind==1:dom=f'x={x}+{du[0]}*n and y={y}+{du[1]}*n and TIME={len(U)}*n+{i}'
            else:dom=f'exists j: 0<=j<n and x={x+dc[0]}+{du[0]}*n+{dv[0]}*j and y={y+dc[1]}+{du[1]}*n+{dv[1]}*j and TIME={len(U)}*n+{len(C)+i}+{len(V)}*j'
            atoms.append((dom,turn))
    read={c:ctx.map('{[n,x,y]->[t]:false}') for c in 'RL'}
    future={c:ctx.map('{[n,x,y,t]->[u]:false}') for c in 'RL'}
    current={c:ctx.set('{[n,x,y,t]:false}') for c in 'RL'}
    for dom,c in atoms:
        clause=f'n>={n0} and ({dom.replace("TIME","t")})'
        read[c]=read[c].union(ctx.map('{[n,x,y]->[t]:'+clause+'}'))
        current[c]=current[c].union(ctx.set('{[n,x,y,t]:'+clause+'}'))
        clause=f'n>={n0} and t<u and ({dom.replace("TIME","u")})'
        future[c]=future[c].union(ctx.map('{[n,x,y,t]->[u]:'+clause+'}'))
    first=read['R'].union(read['L']).lexmin().intersect(read['L']).domain()
    successor=future['R'].union(future['L']).lexmin()
    bad=ctx.set('{[n,x,y]:false}')
    for c in 'RL':
        same=successor.intersect(future[c]);same=Object(ctx,'map',_FUN['map','intersect_domain'](same._copy(),current[c]._copy())).domain()
        bad=bad.union(Object(ctx,'set',_FUN['set','project_out'](same._copy(),3,3,1)))
    return first,bad

H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
cases=[('standard',H,'',H,3,1),('rail','RLLR','','RLLR',3,1),('unequal','RLLR','','RLLR'*3,0,2),('reverse','RLLR','RR','RLLR',2,1),('cap_multi','RLLR','RLRLRL','RLLR',1,3)]
short=[]
for n in (4,8):
    for w in map(''.join,itertools.product('RL',repeat=n)):
        _,d,h=raw(w,0)
        if h==0 and d!=(0,0):short.append(w)
rng=random.Random(20261023)
while len(cases)<24:
    U,V=rng.choice(short),rng.choice(short);C=rng.choice(('','RR','RRRR','LRLR'));h=rng.randrange(4)
    _,a,_=raw(U,h);_,_,hc=raw(C,h);_,b,_=raw(V,hc)
    if a[0]*b[1]==a[1]*b[0]:cases.append(('generic'+str(len(cases)),U,C,V,h,rng.choice((1,2,5))))
records=[]
for name,U,C,V,h,n0 in cases:
    start=time.monotonic(); r=candidate.certify(U,C,V,h,n0)
    ctx=r['_ctx'];ctx.reset_operations();f,b=independent(U,C,V,h,n0,ctx)
    assert f.is_equal(r['_first']),(name,'first');assert b.is_equal(r['_bad']),(name,'bad')
    # Direct raw dictionary controls, no candidate trace or literal helper.
    for n in (n0,n0+1,n0+4):
        rr,_,_=raw(U*n+C+V*n,h);seen={};ff=set();bb=set()
        for x,y,t,c in rr:
            p=(x,y)
            if p not in seen and c=='L':ff.add(p)
            if seen.get(p)==c:bb.add(p)
            seen[p]=c
        def pts(S):return ctx.set('{[n,x,y]:'+(' or '.join(f'(n={n} and x={x} and y={y})' for x,y in S) or 'false')+'}')
        slab=ctx.set('{[n,x,y]:n='+str(n)+'}')
        assert f.intersect(slab).is_equal(pts(ff));assert b.intersect(slab).is_equal(pts(bb))
    rec={'name':name,'all_n_legal':r['all_n_legal'],'fuel':r['fuel_status'],'uniform_bound':r['uniform_fuel_bound'],'seconds':time.monotonic()-start};records.append(rec);print(json.dumps(rec),flush=True)
# Independent interval bound sanity: tracks must remain separate; negative/nonprimitive cases included above.
ctx=Context(); fiber=[]
for text,status,bound in [('{[N,Z]:N>=7 and (Z=3*N-8 or Z=-2*N+5)}','BOUNDED',2),('{[N,Z]:N>=0 and 5*N-2<=Z<=5*N+8}','BOUNDED',11),('{[N,Z]:N>=0 and -N<=Z<=2*N}','UNBOUNDED',None),('{[N,Z]:N>=0 and Z mod 3=1 and 0<=Z<=N}','UNKNOWN',None)]:
    r=candidate.interval_fiber_certificate(ctx.set(text));assert r['status']==status
    if bound is not None:assert r['uniform_bound']==bound
    fiber.append(r)
out={'status':'PASS','source_sha256':hashlib.sha256((ROOT/'global_architecture_2026-10-23/flat_collinear_validator.py').read_bytes()).hexdigest(),'exact_all_n_lexmin_reconstructions':len(records),'literal_controls':3*len(records),'records':records,'fiber_controls':fiber,'scope':'Supplied nonzero-collinear words only; exact same-cell first and consecutive read relations independently rebuilt without residue splitting. Fuel proof uses convex div-free basic fibers; no cap synthesis.'}
(ROOT/'audits/check_flat_collinear_independent.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',flush=True)
