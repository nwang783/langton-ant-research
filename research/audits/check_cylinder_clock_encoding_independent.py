#!/usr/bin/env python3
"""No author imports. Reconstruct literal local states and all clock assertions.
This checks the encoding, not the SMT solver's UNSAT derivation.
"""
from pathlib import Path
import json,re,hashlib,itertools,collections
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(__file__).with_suffix('.json')
# Headings are represented as actual complex lattice vectors, clockwise order.
HEAD=(1j,1,-1j,-1)

def parse(s):
    toks=re.findall(r'\(|\)|[^\s()]+',s)
    stack=[[]]
    for t in toks:
        if t=='(': stack.append([])
        elif t==')':
            a=stack.pop();stack[-1].append(a)
        else: stack[-1].append(t)
    assert len(stack)==1
    return stack[0]

def canon(a):
    if isinstance(a,str): return a
    if len(a)==1: return canon(a[0])
    op=a[0];args=[canon(x) for x in a[1:]]
    if op in ('and','or','+','='):
        args.sort(key=repr)
    return (op,*args)

def disj(a): return 'false' if not a else a[0] if len(a)==1 else ['or',*a]
def conj(a): return 'true' if not a else a[0] if len(a)==1 else ['and',*a]

def independent_states(p):
    # Independently enumerate first R; two visits RL have all heading choices;
    # triple RLR has opposite first/third headings (signed same-type exclusion).
    axis=(1-(p[0]+p[1])%2)
    hs=(axis,(axis+2)%4)
    universe=[()]
    for m in (1,2,3):
        for h in itertools.product(hs,repeat=m):
            if m==3 and h[0]==h[2]: continue
            universe.append(tuple((1 if j%2==0 else -1,hj) for j,hj in enumerate(h)))
    assert len(universe)==11
    # Index assignment is the declared literal interface, not discovered rules.
    indexed=[()]
    for h in hs:
        o=(h+2)%4
        indexed += [((1,h),),((1,h),(-1,h)),((1,h),(-1,o)),
                    ((1,h),(-1,h),(1,o)),((1,h),(-1,o),(1,o))]
    assert set(indexed)==set(universe)
    return indexed

def check_file(path):
    m=re.fullmatch(r'cap3_cylinder_d(\d+)_w(\d+)\.smt2',path.name);n,w=map(int,m.groups())
    # Fundamental representatives use x in [0,n); transverse coordinate y-x.
    points=[(r,r+z) for z in range(-w,w+1) for r in range(n)]
    idx={p:i for i,p in enumerate(points)};loc=[independent_states(p) for p in points]
    def reduce(q):
        k=-(q[0]//n);base=(q[0]+k*n,q[1]+k*n)
        assert 0<=base[0]<n and (base[0]-k*n,base[1]-k*n)==q
        return base,k
    expected=[]
    sizes=[];growth=[]
    for i,states in enumerate(loc):
        expected += [['and',['<=','0',f's{i}'],['<',f's{i}','11']],['<',f't{i}_0',f't{i}_1'],['<',f't{i}_1',f't{i}_2']]
        sizes.append(['+',*(['ite',['=',f's{i}',str(a)],str(len(h)),'0'] for a,h in enumerate(states) if h)])
        growth.append(['+',*(['ite',['=',f's{i}',str(a)],'1','0'] for a,h in enumerate(states) if len(h)%2)])
    expected += [['=','P',['+',*sizes]],['>','P','0'],['>=',['+',*growth],'8']]
    branches=0;equations=0;boundary=0
    for i,p in enumerate(points):
        for h,v in enumerate(HEAD):
            # Every source's outgoing direction is perpendicular to its allowed
            # incoming axis, i.e. this parity test is independently derived.
            if h%2!=(p[0]+p[1])%2: continue
            dst,k=reduce((p[0]+int(v.real),p[1]+int(v.imag)))
            out=[[j for j,(c,ih) in enumerate(st) if HEAD[ih]*(-1j if c==1 else 1j)==v] for st in loc[i]]
            if dst not in idx:
                expected.append(disj([['=',f's{i}',str(a)] for a,o in enumerate(out) if not o]));boundary+=1;continue
            z=idx[dst]
            inc=[[j for j,(c,ih) in enumerate(st) if HEAD[ih]==v] for st in loc[z]]
            opts=[]
            for a,o in enumerate(out):
                for b,ins in enumerate(inc):
                    if len(o)!=len(ins):continue
                    eq=[['=',['+',f't{z}_{j}',['*',str(k),'P']],['+',f't{i}_{u}','1']] for u,j in zip(o,ins)]
                    opts.append(conj([['=',f's{i}',str(a)],['=',f's{z}',str(b)],*eq]));branches+=1;equations+=len(eq)
            expected.append(disj(opts))
        for h,v in enumerate(HEAD):
            if h%2==(p[0]+p[1])%2:continue
            src,k=reduce((p[0]-int(v.real),p[1]-int(v.imag)))
            if src not in idx:
                expected.append(disj([['=',f's{i}',str(a)] for a,st in enumerate(loc[i]) if not any(HEAD[ih]==v for c,ih in st)]));boundary+=1
    actual=[s[1] for s in parse(path.read_text()) if s[0]=='assert']
    A=collections.Counter(map(canon,actual));E=collections.Counter(map(canon,expected))
    assert A==E,(path,A-E,E-A)
    decl=[s for s in parse(path.read_text()) if s[0]=='declare-fun']
    assert set(s[1] for s in decl)=={'P'}|{f's{i}' for i in range(len(points))}|{f't{i}_{j}' for i in range(len(points)) for j in range(3)}
    assert all(s[2]==[] and s[3]=='Int' for s in decl)
    prior=json.loads(path.with_suffix('.json').read_text())
    return dict(file=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),drift=[-n,-n],width=w,classes=len(points),assertions=len(actual),state_pair_branches=branches,clock_equalities=equations,boundary_guards=boundary,encoding='PASS',recorded_solver_status=prior['status'])

def standard_control():
    word=(ROOT/'word_stabilization/standard_word.txt').read_text().strip()
    p=complex(1,0);h=-1j;events=[];N=len(word);d=complex(-2,-2)
    for t,c in enumerate(word):
        events.append((t,p,h,c));h*=(-1j if c=='R' else 1j);p+=h
    assert (p,h)==(complex(-1,-2),-1j)
    hist=collections.defaultdict(list)
    for t,p,h,c in events:
        k=-(int(p.real)//2)
        b=p-k*d
        assert int(b.real) in (0,1)
        hist[b].append((t-k*N,h,c))
    for b,vis in hist.items():
        vis.sort()
        assert ''.join(c for t,h,c in vis)==''.join('R' if j%2==0 else 'L' for j in range(len(vis)))
    total=0
    for b,vis in hist.items():
        for v in HEAD:
            outgoing=[t+1 for t,h,c in vis if h*(-1j if c=='R' else 1j)==v]
            q=b+v;k=-(int(q.real)//2);qb=q-k*d
            incoming=[t+k*N for t,h,c in hist.get(qb,[]) if h==v]
            assert outgoing==incoming
            total+=len(outgoing)
    assert total==N
    # Literal finite input construction: the current color at a given cell is
    # parity of its past reads; only classes straddling time zero can require it.
    seed=set()
    for b,vis in hist.items():
        lo=min(t for t,h,c in vis);hi=max(t for t,h,c in vis)
        for k in range(-hi//N-2,-lo//N+3):
            times=[t+k*N for t,h,c in vis]
            future=[j for j,t in enumerate(times) if t>=0]
            if future and future[0]%2:seed.add(b+k*d)
    p=events[0][1];h=events[0][2];board=set(seed)
    for t in range(100*N):
        c='L' if p in board else 'R';assert c==word[t%N]
        board.symmetric_difference_update({p});h*=(-1j if c=='R' else 1j);p+=h
    return dict(period=N,drift=[-2,-2],classes=len(hist),max_multiplicity=max(map(len,hist.values())),edge_clocks=total,finite_seed_mass=len(seed),literal_replayed_periods=100,result='PASS',scope='General clock/sign control above cap three; not a cap-three positive example.')

if __name__=='__main__':
    fs=sorted((ROOT/'periodic_classification_new').glob('cap3_cylinder_d*_w*.smt2'))
    result=dict(formulas=[check_file(p) for p in fs],standard_control=standard_control(),scope='Independent encoding equivalence and literal positive control. Recorded UNSAT/UNKNOWN values are not independently certified solver proofs.')
    OUT.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
