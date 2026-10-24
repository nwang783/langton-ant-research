"""Exact open atomic-chord/physical-edge contacts, with no guessed box.

This is a current ordered-identity barrier, not a historical embedding.
"""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, math

ROOT = Path(__file__).resolve().parent
GP = ROOT/'chronology_dcuv/literal_residual_geometry.json'
AP = ROOT/'active_center_edge_walk_frozen_20261023_1739/manifest.json'
G = json.loads(GP.read_text())['geometry']
K = {(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
STEPS = ((0,1),(1,0),(0,-1),(-1,0))

def sub(a,b): return a[0]-b[0],a[1]-b[1]
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def edge(q):
    x,y = q
    a,b = (1,1) if (x+y)%2 == 0 else (1,-1)
    return ((2*x-a,2*y-b),(2*x+a,2*y+b))

def open_contact(a,b,c,d):
    u,v,w = sub(b,a),sub(d,c),sub(c,a)
    den = det(u,v)
    if den:
        s,t = F(det(w,v),den),F(det(w,u),den)
        return dict(kind='point',chord_parameter=s,edge_parameter=t) if 0<s<1 and 0<=t<=1 else None
    if det(w,u): return None
    k = 0 if u[0] else 1
    lo,hi = sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])))
    lo,hi = max(F(0),lo),min(F(1),hi)
    if hi>0 and lo<1 and lo<=hi:
        return dict(kind='collinear_overlap',chord_parameter_closure=(lo,hi))
    return None

def reconstruct(word):
    p,h,parity,req = (0,0),0,set(),{}
    for ch in word+G[0]['marker']:
        before = (ch=='L') ^ (p in parity)
        assert p not in req or req[p] == before
        req[p] = before
        parity.symmetric_difference_update({p})
        h = (h+(-1 if ch=='L' else 1))%4
        p = p[0]+STEPS[h][0],p[1]+STEPS[h][1]
    return req

C = G[1]['word'][len(G[0]['word']):]
sources = [('D',G[0]['word'],(2,2),set(map(tuple,G[0]['inputs']))),
           ('V',G[4]['word'],(2,6),set(map(tuple,G[4]['inputs']))),
           ('U',G[7]['word'],(0,8),set(map(tuple,G[7]['inputs']))),
           ('C',C,(2,2),set())]
rows=[]
for name,word,step,I in sources:
    req=reconstruct(word)
    assert {q for q,b in req.items() if b} == K|I
    a=(-1,-1);b=(a[0]+step[0],a[1]+step[1])
    # If an edge meets the chord, its midpoint is coordinatewise at most
    # one doubled unit outside the chord rectangle. This is complete.
    bounds=[(math.ceil((min(a[k],b[k])-1)/2),math.floor((max(a[k],b[k])+1)/2)) for k in (0,1)]
    hits=[];tested=[]
    for x in range(bounds[0][0],bounds[0][1]+1):
        for y in range(bounds[1][0],bounds[1][1]+1):
            q=x,y;e=edge(q);hit=open_contact(a,b,*e)
            tested.append(q)
            if hit:
                role='core' if q in K else 'true_input' if q in I else 'before_white' if req.get(q) is False else 'unclassified'
                assert role!='unclassified'
                hits.append(dict(cell=q,edge_twice=e,role=role,contact=hit))
    expected = {(0,0):'core'} if name in ('D','C') else {(0,1):'before_white'} if name=='V' else {(-1,1):'true_input',(-1,2):'true_input',(0,1):'before_white',(0,2):'true_input'}
    assert {tuple(r['cell']):r['role'] for r in hits}==expected
    star={edge(q) for q in K-{(1,0)}}
    assert star=={tuple(sorted((a,(a[0]+dx,a[1]+dy)))) for dx,dy in ((-2,-2),(-2,2),(2,-2),(2,2))}
    rows.append(dict(atom=name,center_chord_twice=(a,b),complete_candidate_cell_bounds=bounds,tested_cells=tested,open_chord_contacts=hits,black_input_mask=sorted(I)))

out=dict(status='AUTHOR_EXACT_CURRENT_RESIDUAL_EDGE_BARRIER',
         scope='Actual D/V/U/C atomic cuts inside a complete-eight factor. Current ordered residual edges only; not a historical connector or component embedding.',
         theorem='An ordered residual identity that is current at an actual atomic cut has an edge disjoint from every later atomic-center subarc strictly before its retirement. A U consuming base may first meet it at the midpoint or exit, and a D/V consuming base may first meet it at its exit. Fresh recycled identities are distinct.',
         rows=rows,
         dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP,AP,Path(__file__).resolve())})
def enc(x):
    if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x
(ROOT/'chronology_dcuv/current_residual_edge_barrier.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print(json.dumps([dict(atom=r['atom'],tested=len(r['tested_cells']),contacts=[dict(cell=h['cell'],role=h['role']) for h in r['open_chord_contacts']]) for r in rows],indent=2))
