#!/usr/bin/env python3
"""Literal controls for the analytic causal-front identity; no author's oracle."""
from pathlib import Path
import hashlib,json
source=Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json')
raw=source.read_bytes();data=json.loads(raw)
word=data['word'];P=len(word);seed={tuple(q) for q in data['seed']};h0=data['heading']
vec=((0,1),(1,0),(0,-1),(-1,0))
def step(B,p,h):
    turn='L' if p in B else 'R'
    B.symmetric_difference_update({p});h=(h+(-1 if turn=='L' else 1))%4
    a,b=vec[h];return (p[0]+a,p[1]+b),h,turn
B=set(seed);p=(0,0);h=h0;offsets=[];heads=[]
for ch in word:
    offsets.append(p);heads.append(h);p,h,got=step(B,p,h);assert got==ch
assert h==h0;d=p;assert d!=(0,0)
def copy_index(z,s):
    diff=(z[0]-s[0],z[1]-s[1]);ks=[]
    for v,w in zip(diff,d):
        if w==0:
            if v: return None
        else:
            if v%w: return None
            ks.append(v//w)
    return ks[0] if ks and len(set(ks))==1 else None

def past_hits(z,phi):
    sphi=offsets[phi];found=[]
    for i,s in enumerate(offsets):
        a=copy_index(z,(s[0]-sphi[0],s[1]-sphi[1]))
        if a is not None and a*P+i<phi: found.append((a,i))
    return found

def color(z,phi):return len(past_hits(z,phi))%2==1
fresh=[i for i in range(P) if not past_hits((0,0),i)]
assert len(fresh)==22
checks=0;local_equalities=0;insertion_runs=0
for phi in range(P):
    for n in [0,1,2,8,20]:
        board=set(seed);p=(0,0);h=h0
        for t in range(n*P+phi):
            p,h,ch=step(board,p,h);assert ch==word[t%P]
        q=p;assert q==(n*d[0]+offsets[phi][0],n*d[1]+offsets[phi][1])
        for z in [(x,y) for x in range(-8,9) for y in range(-8,9)]+[(-n*d[0]+x,-n*d[1]+y) for x,y in seed]:
            absz=(q[0]+z[0],q[1]+z[1])
            predicted_difference=(absz in seed)^(sum(a < -n for a,_ in past_hits(z,phi))%2==1)
            assert ((absz in board)^color(z,phi))==predicted_difference
            checks+=1
            if n==20:
                assert (absz in board)==color(z,phi) if max(map(abs,z))<=8 else True
                local_equalities+=max(map(abs,z))<=8
for phi in fresh:
    # A three-cell causally fresh cluster, not arbitrary flips on a white board.
    candidates=[(x,y) for x in range(-2,3) for y in range(-2,3) if (x,y)!=(0,0) and not past_hits((x,y),phi)]
    F={(0,0),*candidates[:2]};assert len(F)==3
    for n in [12,23]:
        q=(n*d[0]+offsets[phi][0],n*d[1]+offsets[phi][1]);extra={(q[0]+x,q[1]+y) for x,y in F}
        assert not seed&extra
        board=set(seed)|extra;p=(0,0);h=h0
        for t in range(n*P+phi):
            p,h,ch=step(board,p,h);assert ch==word[t%P]
        assert p==q and h==heads[phi]
        flips=set();r=(0,0);hh=h
        for t in range(50):
            initial=color(r,phi)^(r in F)
            expected='L' if initial^(r in flips) else 'R'
            flips.symmetric_difference_update({r});hh=(hh+(-1 if expected=='L' else 1))%4
            a,b=vec[hh];r=(r[0]+a,r[1]+b)
            p,h,ch=step(board,p,h)
            assert ch==expected and p==(q[0]+r[0],q[1]+r[1]) and h==hh
        insertion_runs+=1
out={'status':'PASS','source_sha256':hashlib.sha256(raw).hexdigest(),'P':P,'drift':d,
     'all_phase_discrepancy_identity_cells':checks,'deep_local_limit_cells':local_equalities,
     'causally_fresh_phases':len(fresh),'actual_initial_three_cell_cluster_runs':insertion_runs,
     'scope':'Finite literal identity and initial-insertion controls only; the compactification and all-depth cone claims are analytic.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
