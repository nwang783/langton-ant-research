"""Independent endpoint-turn and vertex-overlap composition controls.

No discovery implementation is imported. Complex coordinates encode compass
headings; all input inventories are regenerated from binary axis choices.
"""
from itertools import product
from pathlib import Path
import hashlib,json

def prefixes(word):
    p=0j;out=[p]
    for d in word:p+=d;out.append(p)
    return out
def turn(a,b):
    z=b/a
    assert z in (1j,-1j)
    return 1 if z==-1j else -1
def endpoint_info(word):
    p=prefixes(word);j=p.index(p[-1],1)
    return j,word[j-1],word[-1],sum(z==p[-1] for z in p[1:-1])

corrections=0;types={}
for k in [3,5,7,9,11]:
    for axis in [1,1j]:
        for bits in product([-1,1],repeat=k):
            word=tuple(axis*(1j if i%2 else 1)*s for i,s in enumerate(bits))
            p=prefixes(word);j,H,G,r=endpoint_info(word)
            assert j%2==1 and G/H in [-1,1]
            for boundary in [G*1j,G*-1j]:
                turns=[turn(word[t-1],word[t] if t<k else boundary)
                       for t in range(1,k+1) if p[t]==p[-1]]
                if any(a==b for a,b in zip(turns,turns[1:])):continue
                first=word[j] if j<k else boundary
                sigma=(-1)**r*(G/H)
                assert first==sigma*boundary
                corrections+=1
                key=f'r_parity={r%2},epsilon={int((G/H).real)}'
                types[key]=types.get(key,0)+1

A=((3,2),(2,5))
def apply(M,z):return complex(M[0][0]*z.real+M[0][1]*z.imag,M[1][0]*z.real+M[1][1]*z.imag)
def mul(M,N):return tuple(tuple(sum(M[i][k]*N[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def lattice(M,z):
    x,y=int(z.real),int(z.imag);det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return (M[1][1]*x-M[0][1]*y)%det==0 and(-M[1][0]*x+M[0][0]*y)%det==0
domains=[]
for axis in [1,1j]:
    words=[]
    for bits in product([-1,1],repeat=9):
        w=tuple(axis*(1j if i%2 else 1)*s for i,s in enumerate(bits))
        if sum(w)==apply(A,axis):
            assert all(not lattice(A,z) or z in (0,sum(w)) for z in prefixes(w)[1:-1])
            words.append(w)
    domains.append(words)
assert list(map(len,domains))==[20,4]
composition_checks=0
for E,N in product(*domains):
    phi={1:E,1j:N,-1:tuple(-x for x in E),-1j:tuple(-x for x in N)}
    H={d:endpoint_info(w)[1] for d,w in phi.items()};F={d:w[0] for d,w in phi.items()}
    assert len(set(H.values()))==len(set(F.values()))==4
    current={d:(d,) for d in phi};M=((1,0),(0,1));hp={d:d for d in phi};fp=hp.copy()
    for power in range(1,4):
        current={d:tuple(q for e in w for q in phi[e]) for d,w in current.items()};M=mul(A,M)
        hp={d:H[e] for d,e in hp.items()};fp={d:F[e] for d,e in fp.items()}
        for d,w in current.items():
            assert sum(w)==apply(M,d)
            assert endpoint_info(w)[1]==hp[d] and w[0]==fp[d]
            assert all(not lattice(M,z) or z in (0,sum(w)) for z in prefixes(w)[1:-1])
            composition_checks+=1

root=Path(__file__).resolve().parents[1]
note=root/'causal_reduction/matrix_candidates/vertex_only_overlap_obstruction.md'
result={'status':'PASS independent endpoint correction and vertex-only power controls',
        'endpoint_color_corrections':corrections,'correction_types':types,
        'mixing_matrix':A,'regenerated_domains':list(map(len,domains)),
        'halfturn_substitutions':80,'powers_checked':[1,2,3],
        'image_composition_checks':composition_checks,
        'theorem_note_sha256':hashlib.sha256(note.read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
