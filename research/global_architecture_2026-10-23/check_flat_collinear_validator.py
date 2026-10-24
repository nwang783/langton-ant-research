#!/usr/bin/env python3
"""Literal and geometric controls for the focused exact supplied-word checker."""
import hashlib, itertools, json, pathlib, time
from flat_collinear_validator import *

HERE=pathlib.Path(__file__).resolve().parent
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
V=''.join('L' if c=='R' else 'R' for c in H[::-1])
P108=V[:31]+'LRRRR'+V[32:]

def expected(ctx,n,cells):
    out=ctx.set('{[n,x,y]:false}')
    for x,y in cells:
        out=out.union(ctx.set('{[n,x,y]:'+f'n={n} and x={x} and y={y}'+'}'))
    return out

def replay(w,heading,B):
    B=set(B);p=(0,0);h=heading
    for i,c in enumerate(w):
        actual='L' if p in B else 'R'
        assert actual==c,(i,p,actual,c)
        B.symmetric_difference_update({p});h=(h+(1 if c=='R' else -1))%4
        p=add(p,D[h])

def check(name,U,C,P,h=3,n0=1,ns=(1,2,3,5,10),want=None):
    start=time.monotonic();r=certify(U,C,P,h,n0)
    ctx=r['_ctx'];controls=[]
    for n in ns:
        if n<n0: continue
        first,bad=literal(U,C,P,h,n)
        sl=ctx.set('{[n,x,y]:n='+str(n)+'}')
        assert r['_first'].intersect(sl).is_equal(expected(ctx,n,first)),(name,n,'first')
        assert r['_bad'].intersect(sl).is_equal(expected(ctx,n,bad)),(name,n,'bad')
        if not bad: replay(U*n+C+P*n,h,first)
        controls.append(dict(n=n,first_L=len(first),bad_cells=len(bad)))
    if want is not None:
        assert (r['all_n_legal'],r['fuel_status'])==want,(name,r['all_n_legal'],r['fuel_status'])
    rec=dict(name=name,all_n_legal=r['all_n_legal'],fuel_status=r['fuel_status'],
             uniform_fuel_bound=r['uniform_fuel_bound'],illegal_depths=r['illegal_depths'],
             scalar_drifts=r['scalar_drifts'],residue_modulus=r['residue_modulus'],
             literal_controls=controls,seconds=time.monotonic()-start)
    return rec,r

def main():
    start=time.monotonic();records=[]
    maincases=[('standard_positive',H,'',H,3,1,(True,'BOUNDED')),
               ('prepared_rail_positive','RLLR','','RLLR',3,1,(True,'UNBOUNDED')),
               ('prepared108_positive',P108,'',P108,3,1,(True,'UNBOUNDED')),
               ('standard_reverse_return',H,'RR',V,3,1,(False,'UNBOUNDED')),
               ('low_fuel_but_illegal_D10_return',H,'R','LLLLRLRRRR',3,1,(False,'BOUNDED')),
               ('unequal_copy_rates','RLLR','','RLLR'*2,3,2,(True,'UNBOUNDED'))]
    for name,U,C,P,h,n0,want in maincases:
        rec,r=check(name,U,C,P,h,n0,want=want);records.append(rec)
        (HERE/(name+'_exact_flat.json')).write_text(json.dumps(serializable(r),indent=2)+'\n')
        print(name,rec['all_n_legal'],rec['fuel_status'],flush=True)
    # Small, deterministic geometry controls. They do not search for a pump.
    short=[]
    for size in (4,8):
        for tup in itertools.product('RL',repeat=size):
            w=''.join(tup);_,d,hh=trace(w,3)
            if hh==3 and d!=(0,0): short.append(w)
    small=[]
    for U in short[:6]:
        for P in short[::max(1,len(short)//6)][:6]:
            for C in ('','R','RR','LRLR'):
                _,dh,hh=trace(U,3);_,dc,hc=trace(C,3);_,dp,hp=trace(P,hc)
                if dh[0]*dp[1]!=dh[1]*dp[0]: continue
                small.append((U,C,P))
    for i,(U,C,P) in enumerate(small):
        rec,r=check('small_geometry_'+str(i),U,C,P,ns=(1,2,3,4,7));records.append(rec)
    # Cardinality is NOT global diameter: two far-separated tracks stay bounded.
    ctx=Context();fiber_controls=[]
    for name,text,want,bound in [
      ('separated_two_tracks','{[N,Z]:N>=0 and (Z=0 or Z=N)}','BOUNDED',2),
      ('growing_integer_interval','{[N,Z]:N>=0 and 0<=Z<=N}','UNBOUNDED',None),
      ('three_point_interval','{[N,Z]:N>=0 and N<=Z<=N+2}','BOUNDED',3),
      ('div_structure_not_assumed_convex','{[N,Z]:N>=0 and 0<=Z<=N and Z mod 2=0}','UNKNOWN',None)]:
        c=interval_fiber_certificate(ctx.set(text));assert c['status']==want,(name,c)
        if bound is not None: assert c['uniform_bound']==bound,(name,c)
        fiber_controls.append(dict(name=name,**c))
    invalid=0
    for args in [('R','','R'),('RRRR','','RRRR'),('RLLR','','RLLR',-1),('RLLR','','RLLR',3,0)]:
        try: certify(*args)
        except ValueError: invalid+=1
        else: raise AssertionError('malformed geometry accepted')
    out=dict(status='PASS focused all-n validator with independent literal controls',
             scope='Nonzero-collinear supplied words only; no cap synthesis, arbitrary-period classification, or general semilinear extraction.',
             records=records,fiber_controls=fiber_controls,invalid_inputs_rejected=invalid,
             exact_cases=len(records),literal_parameter_controls=sum(len(r['literal_controls']) for r in records),
             seconds=time.monotonic()-start,isl_version=ctx.version,
             source_sha256={q.name:hashlib.sha256(q.read_bytes()).hexdigest() for q in
                            (HERE/'flat_collinear_validator.py',HERE/'check_flat_collinear_validator.py')})
    (HERE/'flat_collinear_validator_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','fiber_controls')},indent=2))

if __name__=='__main__': main()
