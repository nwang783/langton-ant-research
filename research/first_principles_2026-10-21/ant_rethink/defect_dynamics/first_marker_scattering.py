"""Exact one-marker scattering on every first-visit standard phase.

Finite simulations locate candidate suffixes. Finite-ray parity then verifies
the complete infinite suffix and guards all additional older input wake.
This program does not prove closure after multiple markers.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REF = json.loads((ROOT / 'ant_global/root/standard.json').read_text())
W = REF['word']
DR = tuple(REF['drift'])
SEED = {tuple(p) for p in REF['seed']}
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))
ROT = {W[i:] + W[:i] for i in range(104)}
FACT = {(W + W)[i:i+10] for i in range(104)}

def add(p, d, k=1): return p[0] + k*d[0], p[1] + k*d[1]
def sub(p, q): return p[0]-q[0], p[1]-q[1]
def flip(b, p):
    if p in b: b.remove(p)
    else: b.add(p)
def step(b, p, h):
    c = 'L' if p in b else 'R'
    flip(b, p)
    h = (h + (3 if c == 'L' else 1)) % 4
    return add(p, DIR[h]), h, c
def multiple(p, d):
    axis = 0 if d[0] else 1
    if p[axis] % d[axis]: return None
    k = p[axis] // d[axis]
    return k if p == (k*d[0], k*d[1]) else None
def orbit(p, d):
    # Every drift used below has two even nonzero coordinates.
    return (d[0]*p[1]-d[1]*p[0], p[0] % abs(d[0])), p[0] // d[0]

def tail(b, p, h):
    bb=set(b); reads=[]; word=''; hh=h; pp=p
    for _ in range(104):
        reads.append(pp); pp,hh,c=step(bb,pp,hh); word+=c
    d=sub(pp,p)
    if hh != h or abs(d[0]) != 2 or abs(d[1]) != 2 or word not in ROT: return None
    write=b ^ bb
    delta = b ^ write ^ {add(q,d) for q in b}
    lower={}
    for q in reads:
        cl,k=orbit(q,d); lower[cl]=min(lower.get(cl,k+1),k+1)
    if any((cl:=orbit(q,d)[0]) in lower and orbit(q,d)[1] >= lower[cl] for q in delta): return None
    return {'drift': d, 'reads': reads, 'word': word}

def old_guard(p, deposit, age):
    return not any((k:=multiple(sub(q,p),DR)) is not None and k >= age+1 for q in deposit)

def rays_avoid_old(reads, d, deposit, age):
    for p in reads:
        for q in deposit:
            # p+j*d=q-k*DR, j>=0, k>=age+1.
            z=sub(q,p); det=d[0]*DR[1]-d[1]*DR[0]
            if det:
                jnum=z[0]*DR[1]-z[1]*DR[0]
                knum=d[0]*z[1]-d[1]*z[0]
                if jnum % det == 0 and knum % det == 0 and jnum//det >= 0 and knum//det >= age+1: return False
            else:
                a=multiple(z,DR)
                if a is None: continue
                if d == DR and a >= age+1: return False
                if d == (-DR[0],-DR[1]): return False
    return True

def main():
    age=50
    baseline=tail(SEED,(0,0),REF['heading'])
    assert baseline is not None and baseline['word']==W and baseline['drift']==DR
    b=set(SEED); p=(0,0); h=REF['heading']; phase=[]
    for _ in range(104): phase.append((p,h)); p,h,_=step(b,p,h)
    assert p==DR and h==REF['heading']
    deposit=b ^ {add(q,DR) for q in SEED}
    assert len(deposit)==12
    assert not (deposit & {add(q,DR) for q in SEED})
    assert len({orbit(q,DR)[0] for q in deposit})==12
    assert all((k:=multiple(sub(q,v),DR)) is None or k<1 for q in deposit for v in SEED)
    b=set(SEED)
    for k in range(1,age+1): b |= {add(q,DR,-k) for q in deposit}
    frontier=[]
    for i,(q,hh) in enumerate(phase):
        earlier=False
        for j,(v,_) in enumerate(phase):
            k=multiple(sub(q,v),DR)
            if k is not None and j+104*k < i: earlier=True; break
        if not earlier: frontier.append(i)
    assert len(frontier)==22
    reports=[]
    for i,(q,hh) in enumerate(phase):
        if i in frontier:
            assert q not in b
            bb=set(b); flip(bb,q); pp=q; hhh=hh; reads=[]; letters=[]; last_bad=0; nt=None
            for t in range(1,200001):
                reads.append(pp); pp,hhh,c=step(bb,pp,hhh);letters.append(c)
                if t>=10 and ''.join(letters[-10:]) not in FACT: last_bad=t
                if t%104==0 and t-last_bad>=208:
                    nt=tail(bb,pp,hhh)
                    if nt: break
            assert nt is not None, (i,t)
            guard=all(old_guard(v,deposit,age) for v in reads) and rays_avoid_old(nt['reads'],nt['drift'],deposit,age)
            assert guard, i
            report={'phase':i,'impact':q,'heading':hh,'recovery_steps':t,'end':pp,'end_heading':hhh,'drift':nt['drift'],
                    'end_relative':sub(pp,q),'suffix_rows_x_minus_y':sorted({x-y for x,y in nt['reads']}),
                    'suffix_rows_x_plus_y':sorted({x+y for x,y in nt['reads']}),
                    'finite_radius':max(max(abs(v[0]-q[0]),abs(v[1]-q[1])) for v in reads),
                    'prefix_bad10':sum(''.join(letters[j:j+10]) not in FACT for j in range(len(letters)-9)),
                    'all_older_ages_guard':guard}
            reports.append(report)
        p2,h2,c=step(b,q,hh)
        assert c==W[i]
    out={'status':'all_first_marker_phases_certified','age':age,'input_drift':DR,'deposit':sorted(deposit),'frontier_phases':frontier,'cases':reports}
    path=Path(__file__).with_name('first_marker_scattering.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
