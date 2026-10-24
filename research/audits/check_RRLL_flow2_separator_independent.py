import itertools,json,hashlib
from pathlib import Path
R=Path('/workspace/shared/langton');P=R/'first_departure_multiplicity_2026-10-24'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=P/'RRLL_flow2_departure_circles_force_disconnected_actual_events.md'
assert sha(proof)=='9276befb71360ea9507f0a1532de8505ddd611c1435cd1c3aa7e4ba57494b996'
J=json.loads((P/'check_RRLL_flow2_event_separator.json').read_text())
vec={'N':1j,'E':1,'S':-1j,'W':-1}; rev={v:k for k,v in vec.items()}
def outs(w):return [rev[vec[h]*(-1j if i%2==0 else 1j)]for i,h in enumerate(w)]
def idx(w,d,out=False):return [i for i,h in enumerate(outs(w)if out else w)if h==d]
alph={}
for role,first,arrival,departure,left in [('Z','N','S','E',1),('A','E','E','S',0),('B','S','S','W',0),('Y','E','W','S',1)]:
    a=[]
    for n in range(1,5):
        for tail in itertools.product([first,rev[-vec[first]]],repeat=n-1):
            w=first+''.join(tail)
            if left and(n<3 or w[2]!=arrival):continue
            if len(idx(w,arrival))==len(idx(w,departure,True))==2:a.append(w)
    alph[role]=sorted(a)
assert {k:sorted(v)for k,v in J['complete_constant_flow2_alphabets'].items()}==alph

def square(words,edges,k):
    arrivals={};deps={}
    for u,v,d in edges:
        a=idx(words[u],d,True);b=idx(words[v],d)
        if len(a)!=len(b)or len(a)<=k:return None
        deps[u]=a[k];arrivals[v]=b[k]
    return {v:[arrivals[v],deps[v]]for v in words}
F=[('Z','A','E'),('A','B','S'),('B','Y','W'),('Y','Z','N')]
rows=[];surv=[]
for values in itertools.product(*(alph[k]for k in 'ZABY')):
    w=dict(zip('ZABY',values));pairs=square(w,F,0)
    if pairs is None:continue
    nz={k:v for k,v in pairs.items()if v[0]!=v[1]}
    assert nz==({'Y':[2,1]}if w['Y']=='EEWW'else{'Y':[1,2]})
    # Closed four-edge time sum 4+Tout-Tin=0 requires the negative jump.
    if w['Y']=='EEWW':
        assert idx(w['Y'],'N',True)==[1,2]
        if w['Z']=='NSSN':assert idx(w['Z'],'N')==[0,3] # gap>=12, vs forced4
        else:assert w['Z']=='NNSS';surv.append(w)
    rows.append((w,pairs))
assert len(rows)==20 and len(surv)==4
canon=lambda x:json.dumps(x,sort_keys=True)
assert set(canon([a,b])for a,b in rows)==set(canon([r['histories'],r['first_ordinal_pairs']])for r in J['F_first_ordinal_rows'])
Q=[('Z','A','E'),('A','B','N'),('B','Y','W'),('Y','Z','S')];qs=[]
for w in surv:
    pairs=square(w,Q,1);nz={k:v for k,v in pairs.items()if v[0]!=v[1]}
    assert nz==({**({'A':[1,2]}if w['A']=='EEWW'else{}),**({'B':[2,1]}if w['B']=='SNNS'else{})})
    if w['B']!='SNNS':continue # no negative jump: 4+nonnegative impossible
    if w['A']=='EEWW':
        assert idx(w['A'],'N',True)==idx(w['B'],'N')==[1,2] # equal gaps ⇒4=0
    else:qs.append(w)
assert qs==[dict(Z='NNSS',A='EWWE',B='SNNS',Y='EEWW')]
w=qs[0]
pos=lambda u,k:{'Z':0,'A':1,'B':1+1j,'Y':1j}[u]+2j*k
def decode(p):
    if p.real not in(0,1):return None
    k=int(p.imag)//2;odd=int(p.imag)%2
    return ('Z'if p.real==0 and not odd else 'Y'if p.real==0 else 'A'if not odd else 'B',k)
lab=lambda u,r:('W'if r<3 else'E')if u in'ZY'else('W'if r==0 else'E')
internal=[];incoming=[];outgoing=[]
for u in 'ZABY':
    for r,d in enumerate(outs(w[u])):
        q=pos(u,0)+vec[d];target=decode(q)
        if target:
            v,k=target;rr=idx(w[v],d)[idx(w[u],d,True).index(r)]
            assert lab(u,r)==lab(v,rr)
            internal.append([u,0,r,v,k,rr,d])
        else:
            assert lab(u,r)==('W'if q.real<0 else'E');outgoing.append([u,r,d,int(q.real),int(q.imag)])
    for r,d in enumerate(w[u]):
        q=pos(u,0)-vec[d]
        if decode(q)is None:
            assert lab(u,r)==('W'if q.real<0 else'E');incoming.append([u,r,d,int(q.real),int(q.imag)])
assert len(internal)==12 and len(incoming)==len(outgoing)==4
assert set(map(tuple,internal))==set(tuple(r['source']+r['target']+[r['heading']])for r in J['all_internal_symbolic_ordinal_edges'])
# Verify physical lift and short quotient as an extra control, not as a length scan premise.
for a in range(1,9):
    states={(u,k,r)for u in'ZABY'for k in range(a)for r in range(4)}
    assert len(states)==16*a
    for u,k,r in states:
        d=outs(w[u])[r];target=decode(pos(u,k)+vec[d])
        if target:
            v,l=target;rr=idx(w[v],d)[idx(w[u],d,True).index(r)]
            assert lab(u,r)==lab(v,rr) and(v,l%a,rr)in states
report={'status':'PASS: actual complete WHITE cap4 b-cycle, constant physical flow2 and cyclic RRLL geometry only','proof_sha256':sha(proof),'script_sha256':sha(Path(__file__)),'full_alphabets':alph,'F_rows':len(rows),'F_survivors':len(surv),'Q_survivor':w,'internal_edges':internal,'open_ingress':incoming,'open_egress':outgoing,'analytic_closure':['Actual first-departure winding -1 makes full drift (0,2a), not a guessed primitive shift','All physical cells in the two infinite columns have complete four-read histories; no hidden strip rank','Every internal successor and every open port preserves WEST/EAST; exterior unit paths cannot cross either complete column without an accounted strip event','Full vertical quotient preserves the two nonempty sets, contradicting the one actual P-event successor cycle'],'not_claimed':['finite RRLL segment exclusion','general one-use theorem','global maximum premise','complete cap4 front exclusion']}
out=R/'audits/RRLL_flow2_separator_independent.json';out.write_text(json.dumps(report,indent=2)+'\n');print(sha(out));print(report['status'])
