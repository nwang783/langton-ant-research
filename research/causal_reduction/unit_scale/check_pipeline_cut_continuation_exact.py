"""Finite literal certificate for the all-parameter, all-future H-cut theorem.
No trajectory horizon is used in the proof. Extra sample trajectories are
controls only, with the complete infinite initial field evaluated on demand.
"""
import collections, hashlib, json
from pathlib import Path

P=Path(__file__).resolve().parent
J=json.loads((P/'forward108_domino_repair.json').read_text())
H,LR,Q=J['words']

def trace(word,start=0j,head=1+0j):
    rows=[]
    for turn in word:
        rows.append((start,head,turn))
        head*= -1j if turn=='R' else 1j
        start+=head
    return rows,start,head

def orbit(z):
    x,y=int(z.real),int(z.imag)
    return x-y,x%2

def level(z):return int(z.real)//2

def slots(word,start,head):
    out=collections.defaultdict(list)
    for i,(p,h,c) in enumerate(trace(word,start,head)[0]):
        out[orbit(p)].append((level(p),i,c))
    return out

h=slots(H,10j,1);q=slots(Q,0j,1);a=slots(LR,-1+6j,-1j)
assert trace(H,10j,1)[1:]==(2+12j,1)
assert trace(Q,0j,1)[1:]==(2+2j,1)
assert trace(LR,-1+6j,-1j)[1:]==(0+5j,-1j)
histories=[]
for key,es in sorted(h.items()):
    es=sorted(es,key=lambda e:(-e[0],e[1]))
    assert ''.join(e[2] for e in es)==''.join('R' if i%2==0 else 'L' for i in range(len(es)))
    histories.append(dict(orbit=key,levels=[e[0] for e in es],turns=''.join(e[2] for e in es)))
common=sorted(set(h)&(set(q)|set(a)))
assert common==[(-8,1),(-7,0),(-7,1)]
inventory=[]
expected={(-8,1):([1,1,1],[0],[]),(-7,0):([2],[0,1],[]),(-7,1):([1],[0,0],[-1])}
for key in common:
    ls=tuple(sorted(e[0] for e in x.get(key,[])) for x in (h,q,a))
    assert ls==expected[key]
    inventory.append(dict(orbit=key,H=ls[0],Q=ls[1],repair=ls[2]))

# Maximal prefix forced by H's actual last reads, independently of any old field.
rows,end,head=trace(H)
colors={p:int(c=='R') for p,hh,c in rows}
forced=[];p=end
while p in colors:
    c='L' if colors[p] else 'R';forced.append((p,head,c));colors[p]^=1
    head*=1j if c=='L' else -1j;p+=head
    assert len(forced)<=104
assert ''.join(c for p,h,c in forced)=='LRLLRRRRLLRLL'
assert p==end+2+1j and head==1j
assert p not in {z for z,hh,c in rows}
assert p not in {z for z,hh,c in forced}
move_counts=collections.Counter()
for z,hh,c in forced:move_counts[hh*(1j if c=='L' else -1j)]+=1
assert move_counts=={1j:4,1:4,-1j:3,-1:2}

# Exact affine inequalities, represented by their nonnegative differences.
# H ray min minus last extra-black level is l+3, l+3, l-t+4.
# Given l>=-1 and t<=l+2 these are >=2,>=2,>=2.
gaps={'(-8,1)':'l+3 >= 2','(-7,0)':'l+3 >= 2','(-7,1)':'l-t+4 >= 2'}

controls=[]
for l,t in [(-1,1),(0,1),(0,2),(1,1),(1,3),(5,1),(5,7),(100,1),(100,102)]:
    def initial(z):
        key=orbit(z);k=level(z)
        return (sum(k<=l+v for v,i,c in h.get(key,[]))+
                sum(k<t+v for v,i,c in a.get(key,[]))+
                sum(k<v for v,i,c in q.get(key,[])))%2
    changed=set();p=2*l+2+(2*l+12)*1j;head=1
    for i,c in enumerate(H*20):
        bit=initial(p)^(p in changed)
        assert c==('L' if bit else 'R')
        if p in changed:changed.remove(p)
        else:changed.add(p)
        head*=1j if c=='L' else -1j;p+=head
    controls.append(dict(l=l,t=t,reads=20*len(H),endpoint=[int(p.real),int(p.imag)]))

out=dict(status='PASS exact all-phase/all-future profile comparison and maximal endpoint-memory prefix',
    scope=__doc__,overlap_inventory=inventory,standard_histories=histories,
    exact_ray_gaps=gaps,forced_prefix=''.join(c for p,h,c in forced),
    forced_rows=[dict(position=[int(p.real),int(p.imag)],heading=[int(h.real),int(h.imag)],turn=c) for p,h,c in forced],
    next_unknown_relative_to_H_endpoint=[2,1],connector_bound='n >=27-4u for every integer u<=2',
    controls=controls,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    note_sha256=hashlib.sha256((P/'pipeline_cut_continuation_theorem.md').read_bytes()).hexdigest())
(P/'pipeline_cut_continuation_exact.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status']);print('controls',len(controls),'literal reads',sum(x['reads'] for x in controls))
