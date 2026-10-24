#!/usr/bin/env python3
"""Exact supplied H^n C P^n chronology and uniform first-L fuel.

Scope: H and P restore heading and have nonzero collinear integral drifts.
The initial board may depend on n.  No cap synthesis or pump discovery occurs.
All quantification over n is exact libisl integer-set algebra, not sampling.
"""
from __future__ import annotations
import argparse, ctypes as CT, hashlib, json, math, pathlib, sys, time
from fractions import Fraction as Q

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
BRIDGE = ROOT/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'
sys.path.insert(0, str(BRIDGE))
from isl_exact import Context, Object, _bind, _FUN, _P, _libc

_list = _bind('isl_set_get_basic_set_list', [_P])
_list_n = _bind('isl_basic_set_list_n_basic_set', [_P], CT.c_int)
_list_get = _bind('isl_basic_set_list_get_basic_set', [_P, CT.c_int])
_list_free = _bind('isl_basic_set_list_free', [_P], None)
_from_basic = _bind('isl_set_from_basic_set', [_P])
_basic_dim = _bind('isl_basic_set_dim', [_P, CT.c_int], CT.c_int)
_deltas = _bind('isl_map_deltas', [_P])
_maxval = _bind('isl_set_dim_max_val', [_P, CT.c_int])
_val_inf = _bind('isl_val_is_infty', [_P], CT.c_int)
_val_int = _bind('isl_val_is_int', [_P], CT.c_int)
_val_str = _bind('isl_val_to_str', [_P])
_val_free = _bind('isl_val_free', [_P], None)

D = ((0, 1), (1, 0), (0, -1), (-1, 0))

def trace(word, h):
    if not isinstance(word, str) or not set(word) <= set('RL'):
        raise ValueError('literal words must contain only R and L')
    x = y = 0
    rows = []
    for i, c in enumerate(word):
        rows.append(((x, y), i, c))
        h = (h + (1 if c == 'R' else -1)) % 4
        dx, dy = D[h]
        x += dx; y += dy
    return rows, (x, y), h

def add(a, b): return (a[0]+b[0], a[1]+b[1])

def multiple(p, v):
    a = 0 if v[0] else 1
    if p[a] % v[a]: return None
    k = p[a] // v[a]
    return k if p == (k*v[0], k*v[1]) else None

def linear(coeffs, names=('N', 'Z')):
    """Integer affine expression, accepting rational input by denominator clearing."""
    out = str(coeffs[-1])
    for a, x in zip(coeffs[:-1], names):
        out += f'+{a}*{x}'
    return out

def compare(a, b):
    """Strict comparison of rational affine times, exact over integer N,Z."""
    d = [Q(x)-Q(y) for x, y in zip(a, b)]
    m = math.lcm(*(x.denominator for x in d))
    return '('+linear([int(x*m) for x in d])+') < 0'

def basic_sets(s):
    ll = _list(s.ptr)
    if not ll: s.ctx.fail()
    try:
        count = _list_n(ll)
        if count < 0: s.ctx.fail()
        for i in range(count):
            bs = _list_get(ll, i)
            if not bs: s.ctx.fail()
            divs = _basic_dim(bs, 4)  # isl_dim_div
            if divs < 0: s.ctx.fail()
            yield Object(s.ctx, 'set', _from_basic(bs)), divs
    finally:
        _list_free(ll)

def interval_fiber_certificate(s):
    """Exact uniform fiber test for union of div-free planar basic sets.

    Each basic set's fixed-N Z-fiber is an integer interval.  An unbounded
    diameter therefore gives unbounded cardinality, not merely distant points.
    Finite diameters give explicit upper bounds.  Div-bearing unbounded pieces
    are reported UNKNOWN, never silently treated as intervals.
    """
    result = []; bound = 0; unknown = False; growing = False
    for b, divs in basic_sets(s):
        if b.is_empty(): continue
        rendered = str(b)
        to_n = b.ctx.map('{ [N,Z] -> [n] : n=N }')
        to_z = b.ctx.map('{ [N,Z] -> [z] : z=Z }')
        restricted = Object(b.ctx, 'map', _FUN['map','intersect_domain'](to_n._copy(), b._copy()))
        r = restricted.reverse().apply_range(to_z)
        same_n = r.reverse().apply_range(r)
        differences = Object(b.ctx, 'set', _deltas(same_n._copy()))
        value = _maxval(differences._copy(), 0)
        if not value: b.ctx.fail()
        try:
            infinite = _val_inf(value)
            if infinite < 0: b.ctx.fail()
            if infinite:
                status = 'UNBOUNDED_INTERVALS' if divs == 0 else 'UNKNOWN_DIVS'
                growing |= divs == 0; unknown |= divs != 0
                width = None
            else:
                integral = _val_int(value)
                if integral < 0: b.ctx.fail()
                if not integral:
                    raise ArithmeticError('nonintegral integer-set diameter')
                text = _val_str(value)
                if not text: b.ctx.fail()
                try: width = int(CT.string_at(text).decode())
                finally: _libc.free(text)
                assert width >= 0
                bound += width+1; status = 'BOUNDED'
        finally: _val_free(value)
        result.append(dict(piece=rendered, local_divisions=divs,
                           status=status, max_fiber_diameter=width))
    status = 'UNBOUNDED' if growing else ('UNKNOWN' if unknown else 'BOUNDED')
    return dict(status=status, uniform_bound=bound if status == 'BOUNDED' else None,
                pieces=result)

def certify(H, C, P, heading=3, n0=1, max_operations=100_000_000):
    if type(heading) is not int or not 0 <= heading < 4:
        raise ValueError('heading must be an integer 0..3')
    if type(n0) is not int or n0 < 1: raise ValueError('n0 must be positive')
    hr, dh, hh = trace(H, heading)
    cr, dc, hc = trace(C, heading)
    pr, dp, hp = trace(P, hc)
    if not H or not P or hh != heading or hp != hc:
        raise ValueError('nonempty H,P must restore their incoming headings')
    if dh == (0, 0) or dp == (0, 0):
        raise ValueError('this focused adapter requires nonzero H,P drift')
    g = math.gcd(*dh); v = (dh[0]//g, dh[1]//g)
    a = multiple(dh, v); b = multiple(dp, v)
    if b is None: raise ValueError('this focused adapter requires collinear drifts')
    modulus = math.lcm(abs(a), abs(b))
    groups = []
    for kind, rows in (('H', hr), ('C', cr), ('P', pr)):
        for p, phase, turn in rows:
            if kind == 'P': p = add(dc, p)
            for rep, gg in groups:
                k = multiple((p[0]-rep[0], p[1]-rep[1]), v)
                if k is not None: break
            else:
                rep = p; gg = []; groups.append((rep, gg)); k = 0
            gg.append(dict(kind=kind, phase=phase, turn=turn, k=k))
    ctx = Context(max_operations=max_operations)
    empty = lambda: ctx.set('{ [N,Z] : 0=1 }')
    all_bad = ctx.set('{ [n,x,y] : 0=1 }')
    all_first = ctx.set('{ [n,x,y] : 0=1 }')
    records = []; fuel_bounds_by_nres = [0]*modulus; growing_pieces = []
    for gi, (rep, gg) in enumerate(groups):
        for nr in range(modulus):
            for zr in range(modulus):
                ctx.reset_operations()
                rows = []
                n = f'({modulus}*N+{nr})'; z = f'({modulus}*Z+{zr})'
                for row in gg:
                    kind, j, turn, k = (row[t] for t in ('kind', 'phase', 'turn', 'k'))
                    if kind == 'H':
                        if (zr-k) % abs(a): continue
                        # 0 <= (z-k)/a < n, with signs handled explicitly.
                        lo = f'0 <= {z}-{k}' if a > 0 else f'{z}-{k} <= 0'
                        hi = f'{z}-{k} <= {a}*({n}-1)' if a > 0 else f'{a}*({n}-1) <= {z}-{k}'
                        t = (Q(0), Q(len(H)*modulus, a), Q(len(H)*(zr-k), a)+j)
                    elif kind == 'P':
                        if (zr-a*nr-k) % abs(b): continue
                        expr = f'{z}-{a}*{n}-{k}'
                        lo = f'0 <= {expr}' if b > 0 else f'{expr} <= 0'
                        hi = f'{expr} <= {b}*({n}-1)' if b > 0 else f'{b}*({n}-1) <= {expr}'
                        t = (Q(modulus*len(H))-Q(len(P)*a*modulus, b),
                             Q(len(P)*modulus, b),
                             Q(nr*len(H)+len(C)+j)+Q(len(P)*(zr-a*nr-k), b))
                    else:
                        lo = f'{z}={a}*{n}+{k}'; hi = '1=1'
                        t = (Q(len(H)*modulus), Q(0), Q(len(H)*nr+j))
                    domain = ctx.set('{ [N,Z] : '+f'{n}>={n0} and {lo} and {hi}'+' }')
                    if not domain.is_empty(): rows.append((domain, t, turn))
                if not rows: continue
                first = empty(); bad = empty()
                for f, (df, tf, cf) in enumerate(rows):
                    if cf == 'L':
                        ff = df
                        for dhh, th, ch in rows:
                            ff = ff.subtract(dhh.intersect(ctx.set('{[N,Z]:'+compare(th, tf)+'}')))
                        first = first.union(ff)
                    for g, (dg, tg, cg) in enumerate(rows):
                        if f == g or cf != cg: continue
                        candidate = df.intersect(dg).intersect(ctx.set('{[N,Z]:'+compare(tf, tg)+'}'))
                        if candidate.is_empty(): continue
                        for dhh, th, ch in rows:
                            middle = dhh.intersect(ctx.set('{[N,Z]:'+compare(tf, th)+' and '+compare(th, tg)+'}'))
                            candidate = candidate.subtract(middle)
                        bad = bad.union(candidate)
                cert = interval_fiber_certificate(first)
                if cert['status'] == 'BOUNDED': fuel_bounds_by_nres[nr] += cert['uniform_bound']
                elif cert['status'] == 'UNBOUNDED': growing_pieces.append(dict(group=gi, n_residue=nr, z_residue=zr, **cert))
                transform = ctx.map('{ [N,Z] -> [n,x,y] : '+f'n={modulus}*N+{nr} and x={rep[0]}+{v[0]}*({modulus}*Z+{zr}) and y={rep[1]}+{v[1]}*({modulus}*Z+{zr})'+' }')
                def image(s):
                    return Object(ctx, 'map', _FUN['map', 'intersect_domain'](transform._copy(), s._copy())).range()
                all_first = all_first.union(image(first)); all_bad = all_bad.union(image(bad))
                records.append(dict(group=gi, representative=rep, n_residue=nr, z_residue=zr,
                                    phase_rows=len(rows), first_L=str(first),
                                    bad_cells=str(bad), fuel=cert))
    bad_n = Object(ctx, 'set', _FUN['set','project_out'](all_bad._copy(),3,1,2))
    statuses = {r['fuel']['status'] for r in records}
    fuel_status = 'UNBOUNDED' if growing_pieces else ('UNKNOWN' if 'UNKNOWN' in statuses else 'BOUNDED')
    return dict(scope='Supplied nonzero-collinear H^n C P^n; finite seeds may differ with n; no synthesis.',
                heading=heading, n0=n0, lengths=dict(H=len(H), C=len(C), P=len(P)),
                sha256={k:hashlib.sha256(w.encode()).hexdigest() for k,w in (('H',H),('C',C),('P',P))},
                H_drift=dh, P_drift=dp, cap_displacement=dc, cap_out_heading=hc,
                primitive=v, scalar_drifts=[a,b], residue_modulus=modulus,
                all_n_legal=all_bad.is_empty(), illegal_depths=str(bad_n.coalesce()),
                forced_first_L_relation=str(all_first.coalesce()),
                fuel_status=fuel_status,
                uniform_fuel_bound=max(fuel_bounds_by_nres) if fuel_status == 'BOUNDED' else None,
                unbounded_pieces=growing_pieces, records=records,
                _ctx=ctx, _first=all_first, _bad=all_bad)

def literal(H,C,P,heading,n):
    rows, dp, hh = trace(H*n+C+P*n, heading)
    seen = {}; first = set(); bad = set()
    for p,t,c in rows:
        if p in seen and seen[p] == c: bad.add(p)
        if p not in seen and c == 'L': first.add(p)
        seen[p] = c
    return first,bad

def serializable(r): return {k:v for k,v in r.items() if not k.startswith('_')}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('input', type=pathlib.Path, help='JSON with H,C,P, optional heading,n0')
    ap.add_argument('--output', type=pathlib.Path)
    args = ap.parse_args(); x = json.loads(args.input.read_text()); start = time.monotonic()
    r = certify(x['H'], x['C'], x['P'], x.get('heading',3), x.get('n0',1))
    out = serializable(r); out['seconds'] = time.monotonic()-start; out['isl_version'] = r['_ctx'].version
    rendered = json.dumps(out, indent=2)+'\n'
    if args.output: args.output.write_text(rendered)
    else: print(rendered, end='')

if __name__ == '__main__': main()
