"""Literal whole-field controls for the analytic old-side fresh-cap embedding.
No imported ant simulator or return-map code. The all-parameter scope rests
on the stated set-separation and retained pristine-return theorem.
"""
from pathlib import Path
import collections,hashlib,json

P=Path(__file__).resolve().parent
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H']
vec=(1j,1,-1j,-1)
entry=-15+10j;ih=3;d=-2-2j;e=-d;o=-17+2j;a=52262

def trace_word(w,p,h):
    out=[]
    for c in w:
        out.append((p,h,c));h=(h+(1 if c=='R' else -1))%4;p+=vec[h]
    return out,p,h

def required(w,p,h):
    rows,p,h=trace_word(w,p,h);last={};B=set()
    for z,hh,c in rows:
        if z not in last:
            if c=='L':B.add(z)
        else:assert last[z]!=c
        last[z]=c
    return B,rows,p,h

def step(B,p,h):
    c='L' if p in B else 'R'
    if p in B:B.remove(p)
    else:B.add(p)
    h=(h+(1 if c=='R' else -1))%4
    return p+vec[h],h,c

S,inrows,end,eh=required(H,entry,ih)
assert len(S)==13 and end==entry+d and eh==ih
bb=set(S);pp=entry;hh=ih
for c in H:
    pp,hh,got=step(bb,pp,hh);assert got==c
W=bb^{z+d for z in S};assert len(W)==12
inverse=set();bb=set(S);pp=entry;hh=ih
for _ in range(10):
    z=pp-vec[hh];inverse.add(z)
    # Current color at old read z is the flipped old color.
    hh=(hh+(-1 if z in bb else 1))%4
    if z in bb:bb.remove(z)
    else:bb.add(z)
    pp=z

R=set(S)|{o+11*d};rp=entry;rh=ih;A=set()
for _ in range(a):A.add(rp);rp,rh,c=step(R,rp,rh)
assert len(R)==2216 and rp==-49j and rh==1
r=rp;rr=trace_word(H,r,rh)[0];Q={z for z,h,c in rr};M=set()
for z,h,c in rr:
    if z in M:M.remove(z)
    else:M.add(z)
assert len(M)==32
bb=set(R);pp=r;hh=rh
for c in H:
    pp,hh,got=step(bb,pp,hh);assert got==c
assert pp==r+e and hh==rh
assert bb==R^M
assert min(int(z.real-z.imag) for z in Q)==42
assert max(int(z.real-z.imag) for z in Q)==52

def copy_index(z,q):
    delta=z-q
    if delta.real!=delta.imag or int(delta.real)%2:return None
    return int(delta.real)//2

def past(z):return any((k:=copy_index(z,q)) is not None and k<0 for q in Q)
def causal(z):return sum((k:=copy_index(z,q)) is not None and k<0 for q in M)%2

firstfresh=[z for z,h,c in rr if not past(z)]
F={firstfresh[0],firstfresh[-1],entry,r+5}
assert len(F)==4 and not any(past(z) for z in F)
assert entry in F  # A cap spanning the original forbidden normal band.
minF=min(int(z.real) for z in F)
maxpast=max(int(z.real) for z in A|S|inverse|{z for z,h,c in inrows})
T0=max(1,(maxpast-minF)//2+1)

# The ideal finite response, used only as a literal comparison control.
changed=set();pp=r;hh=rh;ideal=[]
for i in range(600):
    bit=causal(pp)^(pp in F)^(pp in changed)
    c='L' if bit else 'R';ideal.append((pp,hh,c))
    if pp in changed:changed.remove(pp)
    else:changed.add(pp)
    hh=(hh+(1 if c=='R' else -1))%4;pp+=vec[hh]
minseen=min(int(z.real) for z,h,c in ideal)
maxmask=max(int(z.real) for z in R|W|M)
Tbase=max(T0,(maxmask-minseen)//2+1)
badn=[]
for z in inverse:
    delta=z-(o+11*d)
    if delta.real==delta.imag and int(delta.real)%2==0:
        n=-int(delta.real)//2
        if n>=0:badn.append(n)
n0=1+max(badn,default=-1)

controls=[]
for dn,dt in [(0,0),(1,3),(4,7)]:
    n=n0+dn;T=Tbase+dt;FT={z+T*e for z in F};obs=o+(11+n)*d
    assert not (FT&S) and obs not in FT|S and obs not in inverse
    assert min(int(z.real) for z in FT)>maxpast
    assert not any(past(z-T*e) for z in FT)
    B=set(S)|FT|{obs};p=entry;h=ih;elapsed=a+208*n+104*T
    assert len(B)==14+len(F)
    for _ in range(elapsed):p,h,c=step(B,p,h)
    assert p==r+T*e and h==rh
    field=FT^{z-n*e for z in R}
    for j in range(n):field^={z+j*d for z in W}
    for j in range(-n,T):field^={z+j*e for z in M}
    assert B==field
    assert all((z+T*e in B)==bool(causal(z)^(z in F)) for z,hh,c in ideal)
    for z,hh,c in ideal:
        assert p==z+T*e and h==hh
        p,h,got=step(B,p,h);assert got==c
    controls.append(dict(n=n,T=T,initial_mass=14+len(F),elapsed_to_section=elapsed,
        complete_section_mass=len(field),matched_response_reads=len(ideal)))

def encode(ss):return sorted([int(z.real),int(z.imag)] for z in ss)
out=dict(status='PASS literal all-field formula and causally fresh cap controls',scope=__doc__,
    canonical_seed=encode(S),entry=[-15,10,3],reverse_pose=[0,-49,1],
    stable_reads=len(A),stable_max_x=max(int(z.real) for z in A),
    reverse_read_normal_band=[42,52],old_wake_normal_band=[min(int(z.real-z.imag) for z in W),max(int(z.real-z.imag) for z in W)],
    cap=encode(F),cap_hits_original_entry=True,cap_misses_reverse_strict_past=True,
    effective_T0=T0,n0=n0,controls=controls,
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    note_sha256=hashlib.sha256((P/'old_side_fresh_cap_embedding.md').read_bytes()).hexdigest())
(P/'old_side_fresh_cap_embedding_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status']);print('T0',T0,'n0',n0,'controls',controls)
