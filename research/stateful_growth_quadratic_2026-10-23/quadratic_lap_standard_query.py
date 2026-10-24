#!/usr/bin/env python3
"""Exact fixed104 event-successor query, separate from geometry/seed validation."""
from quadratic_lap_validator import *
from quadratic_lap_validator import _bind,_P,_val_str,_val_free,_libc

_maxval=_bind('isl_set_dim_max_val',[_P,C.c_int])
def max_n(s):
    v=_maxval(s.ptr,0)
    if not v:s.ctx.fail()
    z=_val_str(v)
    if not z:s.ctx.fail()
    try:return int(C.string_at(z).decode())
    finally:_libc.free(z);_val_free(v)

def successor(P,ctx):
    result=None
    def add_clause(domain,n,b,j,r):
        nonlocal result
        q=ctx.map('{[n,b,j,r]->[m,c,k,s]:'+domain+f' and m={n} and c={b} and k={j} and s={r}'+'}')
        result=q if result is None else result.union(q)
    def count(b,n='n'):
        w,a,v=P.blocks[b]
        return f'({a}*{n}+{v})'
    for f in P.families:
        w,a,v=P.blocks[f.block]
        if f.phase+1<len(w):
            add_clause(f.dom(),'n',f.block,'j',f.phase+1)
            continue
        add_clause(f.dom()+f' and j+1<{count(f.block)}','n',f.block,'j+1',0)
        last=f.dom()+f' and j+1={count(f.block)}'
        for c in range(f.block+1,len(P.blocks)):
            condition=last+f' and {count(c)}>0'
            condition+=''.join(f' and {count(b)}=0'for b in range(f.block+1,c))
            add_clause(condition,'n',c,0,0)
        last+=''.join(f' and {count(b)}=0'for b in range(f.block+1,len(P.blocks)))
        for c in range(len(P.blocks)):
            condition=last+f' and {count(c,"(n+1)")}>0'
            condition+=''.join(f' and {count(b,"(n+1)")}=0'for b in range(c))
            add_clause(condition,'n+1',c,0,0)
    return result.coalesce()

def power(S,n):
    assert n>0
    result=None
    while n:
        if n%2:result=S if result is None else result.apply_range(S).coalesce()
        n//=2
        if n:S=S.apply_range(S).coalesce()
    return result

def event_next(P,e):
    n,b,j,r=e;w,a,v=P.blocks[b]
    if r+1<len(w):return n,b,j,r+1
    if j+1<a*n+v:return n,b,j+1,0
    for c in range(b+1,len(P.blocks)):
        ww,aa,vv=P.blocks[c]
        if aa*n+vv:return n,c,0,0
    n+=1
    for c,(ww,aa,vv)in enumerate(P.blocks):
        if aa*n+vv:return n,c,0,0
    raise AssertionError('empty lap')

def first_event(P,n):
    for b,(w,a,v)in enumerate(P.blocks):
        if a*n+v:return n,b,0,0
    raise AssertionError('empty lap')

def query(P,ctx,canonical):
    S=successor(P,ctx);T=power(S,104)
    domain=ctx.set('{[n,b,j,r]:false}');L=domain
    for f in P.families:
        q=ctx.set('{[n,b,j,r]:'+f.dom()+'}')
        domain=domain.union(q)
        if f.turn=='L':L=L.union(q)
    domain=domain.coalesce();L=L.coalesce();R=domain.subtract(L).coalesce()
    mismatch=inter(inter(T,L,'domain'),R,'range').union(inter(inter(T,R,'domain'),L,'range')).domain().coalesce()
    finite=bounded(mismatch)
    result=dict(mismatch_relation=str(mismatch),mismatch_finite=finite)
    if not finite:return dict(result,standard104=False,reason='infinitely many104-successor mismatches')
    n=0 if mismatch.is_empty()else max_n(mismatch)+1
    e=first_event(P,n);turns=[]
    for k in range(104):
        turns.append(P._by[e[1],e[3]].turn)
        f=event_next(P,e)
        # Small exact-composition point check for this104-event inspection.
        point=ctx.map('{[n,b,j,r]->[m,c,k,s]:'+' and '.join(f'{v}={x}'for v,x in zip(('n','b','j','r','m','c','k','s'),e+f))+'}')
        assert not S.intersect(point).is_empty()
        e=f
    word=''.join(turns);phases=[i for i in range(104)if word==canonical[i:]+canonical[:i]]
    return dict(result,standard104=bool(phases),suffix_start=first_event(P,n),suffix_word=word,canonical_phases=phases)

def main():
    t=time.monotonic();ctx=Context(max_operations=200000000)
    standard=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
    programs=[Program([(standard['word'],1,1)],standard['heading'],'standard104_grouped'),
      Program([('LRRL',1,1)],1,'infinite_prepared_axial_rail'),
      Program([('LRRL',1,1),('RRRR',0,1)],1,'punctuated_prepared_rail')]
    records=[]
    for P in programs:
        ctx.reset_operations();q=query(P,ctx,standard['word']);records.append(dict(name=P.name,**q));print(P.name,q['standard104'],q['mismatch_finite'],flush=True)
    assert records[0]['standard104']
    assert not records[1]['standard104'] and records[1]['mismatch_finite']
    assert not records[2]['standard104'] and not records[2]['mismatch_finite']
    report=dict(status='EXACT STANDARD104 ORDERED-EVENT SUFFIX CONTROLS',records=records,seconds=time.monotonic()-t,
      source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      geometry_validator_sha256=hashlib.sha256(Path(__file__).with_name('quadratic_lap_validator.py').read_bytes()).hexdigest(),
      scope='Suffix query is applied to supplied geometric turn programs; it asserts an actual finite-seed orbit only after full geometry/chronology/finite-supply validation passes.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k!='records'},indent=2))
if __name__=='__main__':main()
