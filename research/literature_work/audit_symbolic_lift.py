"""Exact finite audit of a proposed use of Gajardo's 2003 hyperbolic bound.

Own code; no upstream checker imported. SymPy is used only for exact algebraic
number arithmetic. This does NOT prove or disprove the highway conjecture.
"""
from pathlib import Path
import json
import sympy as s

W = "RRLLLLRLLLLRLLLLRRRRLRRLLLLRRLRRRRLLL"

def normal_form(word):
    out = []
    for c in word:
        out.append(c)
        if out[-4:] == [c] * 4:
            del out[-4:]
    return "".join(out)

def square_audit(word):
    p, h = (0, 0), 0
    first, last, rows = {}, {}, []
    for t, c in enumerate(word):
        first.setdefault(p, c)
        assert p not in last or last[p] != c, (t, p)
        last[p] = c
        rows.append(dict(t=t, p=p, h=h, turn=c, nf=normal_form(word[:t])))
        h = (h + (1 if c == "R" else -1)) % 4
        dx, dy = [(0, 1), (1, 0), (0, -1), (-1, 0)][h]
        p = p[0] + dx, p[1] + dy
    return dict(initial_black=sorted(p for p,c in first.items() if c == "L"), rows=rows)

def hyperbolic_audit(word):
    # Poincare disk: vertex rotation S(z)=exp(2pi*i/5) z;
    # edge half-turn A(z)=(r-z)/(1-r*z), r^2=cos(2pi/5).
    # R=A*S and L=A*S^{-1}; current directed edge is g(0)->g(r).
    # Matrices are projective; no floating-point equality is used.
    sq5 = s.sqrt(5)
    K = s.QQ.algebraic_field(s.I, sq5, s.sqrt(10-2*sq5), s.sqrt(sq5-1))
    cv = K.from_sympy
    zero, one = K.zero, K.one
    r = cv(s.sqrt(sq5-1)/2)
    z = cv((1+sq5+s.I*s.sqrt(10-2*sq5))/4)
    zi = one/z
    def mul(a,b):
        return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])
    A = (-one,r,-r,one)
    R = mul(A,(z,zero,zero,zi))
    L = mul(A,(zi,zero,zero,z))
    I = (one,zero,zero,one)
    for name,M,n in [("A",A,2),("S",(z,zero,zero,zi),5),("R",R,4),("L",L,4)]:
        power=I
        for _ in range(n): power=mul(power,M)
        assert power[1]==zero and power[2]==zero and power[0]==power[3] and power[0]!=zero,name
    sites, first, last, ids, g = [], {}, {}, [], I
    for t,c in enumerate(word):
        point=(g[0]*r+g[1],g[2]*r+g[3])
        assert point[1] != zero
        matches=[j for j,q in enumerate(sites) if point[0]*q[1] == q[0]*point[1]]
        if matches: j=matches[0]
        else: j=len(sites); sites.append(point)
        first.setdefault(j,c)
        assert j not in last or last[j]!=c,("hyperbolic alternation conflict",t,j)
        last[j]=c;ids.append(j)
        g=mul(g,R if c=="R" else L)
    return dict(site_ids=ids, initial_black_site_ids=sorted(j for j,c in first.items() if c=="L"),
                root_visits=[dict(t=t,turn=word[t]) for t,j in enumerate(ids) if j==ids[0]],
                distinct_sites=len(sites), exact_field_degree=K.ext.minpoly.degree())

if __name__ == "__main__":
    out = dict(word=W, square=square_audit(W), hyperbolic=hyperbolic_audit(W))
    path=Path(__file__).with_name("symbolic_lift_witness.json")
    path.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(dict(word=W, hyperbolic=out["hyperbolic"]),indent=2))
