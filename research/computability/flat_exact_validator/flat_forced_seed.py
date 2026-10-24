"""Exact all-depth input-board requirements for flat additive-I typed refinements.

A flat occurrence graph has at most one internal child occurrence per state in
any recurrent SCC. Every occurrence WALK (not just its Parikh image) is covered
by a finite family of simple-cycle schemes. Both colors required at each
spatial position are compiled as automatic relations. This is a restricted
integrated arbitrary-mass/radius decision procedure, not a highway proof.
"""
from __future__ import annotations
import collections, dataclasses, functools, itertools, json, pathlib, sys, time
import sympy as S
from sympy.polys.matrices import DomainMatrix
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent))
sys.path.insert(0,str(HERE.parent/'finite_power_exact_validator'))
from automatic_relations import Rel, linear, TRUE, FALSE
from cartier_controls import machine, evaluate
from automatic_selected_ray_control import affine_pullback, parity_bounded

D=((0,1),(1,0),(0,-1),(-1,0))
Z,X,Y=S.symbols('z x y'); VARIABLES=(Z,X,Y)

@dataclasses.dataclass(frozen=True)
class Edge:
    source:int
    index:int
    target:int
    offset:tuple[int,int]

class Unsupported(Exception): pass

class Model:
    def __init__(self,physical,images,root=0):
        if not isinstance(physical,(list,tuple)) or not physical or not isinstance(images,(list,tuple)):
            raise ValueError('finite nonempty physical alphabet and finite image sequence required')
        if len(physical)!=len(images) or type(root) is not int or not 0<=root<len(images):
            raise ValueError('invalid alphabet/root')
        for pair in physical:
            if not isinstance(pair,(list,tuple)) or len(pair)!=2 or any(type(a) is not int for a in pair):
                raise ValueError('each physical type must be an integer heading/turn pair')
            if pair[0] not in range(4) or pair[1] not in (-1,1):
                raise ValueError('invalid physical heading/turn')
        for word in images:
            if not isinstance(word,(list,tuple)) or not word or any(type(t) is not int or not 0<=t<len(images) for t in word):
                raise ValueError('each image must be a nonempty finite sequence of integer state indices')
        self.physical=tuple(tuple(s) for s in physical)
        self.images=tuple(tuple(w) for w in images)
        self.root=root
        self.phi=[]
        for s,word in enumerate(self.images):
            if not word:raise ValueError('images must be nonerasing')
            h,turn=self.physical[s]
            if h not in range(4) or turn not in (-1,1):raise ValueError('invalid physical type')
            p=(0,0);row=[]
            for j,t in enumerate(word):
                if not 0<=t<len(images):raise ValueError('invalid child')
                ih,tr=self.physical[t]
                if h!=ih:raise ValueError(('heading mismatch',s,j,h,ih))
                row.append(Edge(s,j,t,p))
                h=(h+tr)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
            out=(self.physical[s][0]+turn)%4
            if h!=out or p!=D[out]:raise ValueError(('not exact unit pose',s,p,h,D[out],out))
            self.phi.append(tuple(row))
        reach={root};todo=[root]
        for s in todo:
            for e in self.phi[s]:
                if e.target not in reach:reach.add(e.target);todo.append(e.target)
        self.reach=tuple(sorted(reach))
        # Exact SCCs by mutual reachability. Alphabet sizes here are deliberately
        # small; no graph-library dependency or potentially ambiguous edge merge.
        follows={s:{s} for s in reach}
        for s in reach:
            queue=list(follows[s])
            for t in queue:
                for e in self.phi[t]:
                    if e.target not in follows[s]:follows[s].add(e.target);queue.append(e.target)
        remaining=set(reach);scc=[]
        while remaining:
            s=min(remaining);c=frozenset(t for t in remaining if t in follows[s] and s in follows[t])
            remaining-=c;scc.append(c)
        self.components=tuple(scc);self.comp={s:c for c in scc for s in c}
        self.internal={}
        for s in reach:
            internal=tuple(e for e in self.phi[s] if e.target in self.comp[s])
            if len(internal)>1:raise Unsupported('branching occurrence SCC; this compiler is flat-only')
            if len(self.comp[s])>1 and len(internal)!=1:raise AssertionError('bad SCC')
            self.internal[s]=internal[0] if internal else None

    def schemes(self):
        """Each scheme is (chunks,terminal); chunk=(is_cycle,edge_tuple).
        Every natural exponent tuple is a genuine path. The schemes cover all
        finite root paths exactly once, because complete laps precede the
        unique residual partial lap at each SCC.
        """
        def go(s):
            if self.internal[s] is None:
                yield (),s
                for e in self.phi[s]:
                    for chunks,t in go(e.target):yield ((False,(e,)),)+chunks,t
                return
            cycle=[];v=s
            while True:
                e=self.internal[v];assert e is not None
                cycle.append(e);v=e.target
                if v==s:break
            cchunk=(True,tuple(cycle));prefix=[];v=s
            for j in range(len(cycle)):
                head=(cchunk,)+(((False,tuple(prefix)),) if prefix else ())
                yield head,v
                for e in self.phi[v]:
                    if e!=self.internal[v]:
                        for chunks,t in go(e.target):yield head+((False,(e,)),)+chunks,t
                prefix.append(cycle[j]);v=cycle[j].target
        return list(go(self.root))

    def parity_machines(self):
        """Exact rational parity extraction, independent of flat schemes."""
        shift=(max(0,-min(e.offset[0] for s in self.reach for e in self.phi[s])),
               max(0,-min(e.offset[1] for s in self.reach for e in self.phi[s])))
        ids={s:j for j,s in enumerate(self.reach)};n=len(ids);T=S.zeros(n)
        for s in self.reach:
            for e in self.phi[s]:T[ids[s],ids[e.target]]+=X**(e.offset[0]+shift[0])*Y**(e.offset[1]+shift[1])
        A=DomainMatrix.from_Matrix(S.eye(n)-Z*T)
        rhs=DomainMatrix.from_Matrix(S.ones(n,1)).convert_to(A.domain)
        numerator,denominator=A.solve_den(rhs);N=numerator.to_Matrix();den=A.domain.to_sympy(denominator)
        out={};certificate={}
        for s,j in ids.items():
            P,H=S.fraction(S.cancel(N[j]/den));p=S.Poly(P,*VARIABLES,modulus=2);h=S.Poly(H,*VARIABLES,modulus=2)
            if h.coeff_monomial((0,0,0))!=1:raise ValueError('parity denominator not a unit')
            g=S.gcd(p,h);p=p.exquo(g);h=h.exquo(g)
            out[s]=machine(p.monoms() if not p.is_zero else [],h.monoms())
            certificate[s]=dict(numerator=str(p.as_expr()),denominator=str(h.as_expr()),states=len(out[s]['states']))
        return shift,out,certificate

    def literal(self,depth):
        word=[self.root]
        for _ in range(depth):word=[t for s in word for t in self.images[s]]
        p=(0,0);h=self.physical[self.root][0];reads=[]
        for s in word:
            assert self.physical[s][0]==h
            reads.append((p,int(self.physical[s][1]==-1),s))
            h=(h+self.physical[s][1])%4;p=(p[0]+D[h][0],p[1]+D[h][1])
        return reads


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(k,a):return tuple(k*x for x in a)
def affine(coeff,constant):return (tuple(coeff),constant)
def edge_sum(edges):return (len(edges),sum(e.offset[0] for e in edges),sum(e.offset[1] for e in edges))

def compile_scheme(model,scheme,shift,machines):
    chunks,terminal=scheme;k=sum(c for c,es in chunks);variables=tuple('n'+str(i) for i in range(k));zero=(0,)*k
    total_c=[0,0,0];total_v=[list(zero) for _ in range(3)];counter=0
    for cyc,es in chunks:
        v=edge_sum(es)
        if cyc:
            for h in range(3):total_v[h][counter]+=v[h]
            counter+=1
        else:
            for h in range(3):total_c[h]+=v[h]
    prefix_c=[0,0,0];prefix_v=[list(zero) for _ in range(3)];counter=0;prior=FALSE;terms=0
    for cyc,es in chunks:
        cycleweight=edge_sum(es);local=[0,0,0]
        for e in es:
            for sibling in model.phi[e.source][:e.index]:
                # Q(depth remaining, selected position-prefix-sibling offset).
                coeff=[tuple(total_v[h][i]-prefix_v[h][i] for i in range(k)) for h in range(3)]
                const=[total_c[0]-prefix_c[0]-local[0]-1,
                       total_c[1]-prefix_c[1]-local[1]-sibling.offset[0],
                       total_c[2]-prefix_c[2]-local[2]-sibling.offset[1]]
                # Remaining depth subtracts exactly ONE chosen edge, not its
                # spatial offset. Current prefix includes all earlier edges.
                if cyc:
                    coeff=[coeff[h]+(-cycleweight[h],) for h in range(3)]
                    vs=variables+('q',)
                else:vs=variables
                # Cartier machine uses Q(r,x+C*r,y+D*r).
                cf=(coeff[0],tuple(a+shift[0]*b for a,b in zip(coeff[1],coeff[0])),
                    tuple(a+shift[1]*b for a,b in zip(coeff[2],coeff[0])))
                cc=(const[0],const[1]+shift[0]*const[0],const[2]+shift[1]*const[0])
                term=affine_pullback(machines[sibling.target],vs,cf,cc)
                if cyc:term=parity_bounded(term,'q',variables[counter])
                prior=prior.both(term,lambda a,b:a!=b);terms+=1
            local[0]+=1;local[1]+=e.offset[0];local[2]+=e.offset[1]
        if cyc:
            for h in range(3):prefix_v[h][counter]+=cycleweight[h]
            counter+=1
        else:
            for h in range(3):prefix_c[h]+=local[h]
    assert counter==k and prefix_c==total_c and prefix_v==total_v
    # Last letter needs black iff L, before its preceding reads are toggled.
    need_black=~prior if model.physical[terminal][1]==-1 else prior
    return dict(variables=variables,prior=prior,black=need_black,terminal=terminal,
                length=(tuple(total_v[0]),total_c[0]),
                x=(tuple(total_v[1]),total_c[1]),y=(tuple(total_v[2]),total_c[2]),terms=terms)


def locate(compiled,sx,sy):
    vs=compiled['variables'];out=TRUE
    for coord,sign in [('x',sx),('y',sy)]:
        coeff,const=compiled[coord];c={v:a for v,a in zip(vs,coeff)};c[coord]=-sign
        out=out&linear(c,-const)
    return out


def compile_requirements(model,verbose=False):
    start=time.monotonic();shift,machines,rat=model.parity_machines();schemes=model.schemes()
    compiled=[];relations={sign:(FALSE,FALSE) for sign in itertools.product((-1,1),repeat=2)}
    for j,scheme in enumerate(schemes):
        c=compile_scheme(model,scheme,shift,machines);compiled.append(c)
        for signs,(black,white) in list(relations.items()):
            spatial=locate(c,*signs);vs=c['variables']
            b=(spatial&c['black']).exists(*vs);w=(spatial&~c['black']).exists(*vs)
            relations[signs]=(black|b,white|w)
        if verbose:print('scheme',j+1,'/',len(schemes),'cycles',len(c['variables']),'prior states',len(c['prior'].tr),flush=True)
    conflicts={};finite=True
    for signs,(black,white) in relations.items():
        witness=(black&white).witness()
        if witness is not None:conflicts[str(signs)]={v:signs[('x','y').index(v)]*n for v,n in witness.items()}
        finite=finite and black.bounded()
    possible=not conflicts and finite
    seed=None
    if possible:
        points=set()
        for signs,(black,white) in relations.items():
            if black.witness() is None:continue
            # Derive a radius from the exact automatic bound sentence, never
            # impose one as a decision cutoff.
            m='_bound';guard=linear({m:1,'x':-1},0,'>=')&linear({m:1,'y':-1},0,'>=')
            radius=black.implies(guard).forall('x','y').witness()[m]
            for x in range(radius+1):
                for y in range(radius+1):
                    if black.eval(x=x,y=y):points.add((signs[0]*x,signs[1]*y))
        seed=sorted(points)
    nested=model.images[model.root][0]==model.root
    growing=nested and len(model.images[model.root])>1
    return dict(status='decided',possible=possible,nested_root=nested,growing_root=growing,
                accepted_growing_model=possible and growing,finite_black_requirement=finite,
                conflict_cells=conflicts,seed=seed,schemes=len(schemes),
                rational_parity=rat,requirement_state_counts={str(s):[len(b.tr),len(w.tr)] for s,(b,w) in relations.items()},
                seconds=time.monotonic()-start),compiled,relations,machines,shift


def standard_physical():return [(h,turn) for h in range(4) for turn in (1,-1)]
def word_states(word,heading=0):
    states=[];h=heading
    for ch in word:
        turn=1 if ch=='R' else -1;states.append(2*h+int(turn==-1));h=(h+turn)%4
    return states

def identity(root=0):return Model(standard_physical(),[[s] for s in range(8)],root)
def right_five_flat():
    # a is a decorated R@N; the four extra R states are fixed letters.
    return Model(standard_physical()+[(0,1)],[[s] for s in range(8)]+[[8]+word_states('RRRR',1)],8)
def hairpin(U,V):
    physical=standard_physical()+[(0,1)];images=[[s] for s in range(8)]
    states=word_states(U);h=(sum(1 if c=='R' else -1 for c in U))%4
    assert h==0
    images.append(states+[8]+word_states(V,1))
    return Model(physical,images,8)


def run_controls():
    records=[]
    for name,model in [('identity_R',identity(0)),('identity_L',identity(1)),('right_five_flat',right_five_flat()),
                       ('oblique_hairpin',hairpin('LRLLLLRRRRLRRL','RLRRLL')),
                       ('axial_hairpin',hairpin('RRLRRRRL','LLRLLRLL'))]:
        print('BEGIN',name,flush=True);result,compiled,relations,machines,shift=compile_requirements(model,True)
        result['name']=name
        assert result['possible']==name.startswith('identity')
        if name=='identity_R':assert result['seed']==[]
        if name=='identity_L':assert result['seed']==[(0,0)]
        # Independent literal prefix parity at selected leaves through depth5.
        checks=0;position_checks=0
        for depth in range(6):
            reads=model.literal(depth);previous=set()
            for p,turn,s in reads:
                required=turn^int(p in previous);signs=tuple(1 if a>=0 else -1 for a in p);b,w=relations[signs]
                vals=dict(x=abs(p[0]),y=abs(p[1]));assert (b if required else w).eval(**vals)
                position_checks+=1
                previous.symmetric_difference_update({p})
            for s,M in machines.items():
                # Re-root without redoing geometry and compare complete local
                # parity by direct refinement rather than transfer arithmetic.
                word=[s]
                for _ in range(depth):word=[t for a in word for t in model.images[a]]
                pos=(0,0);h=model.physical[s][0];odd=set()
                for a in word:
                    odd.symmetric_difference_update({pos});h=(h+model.physical[a][1])%4
                    pos=(pos[0]+D[h][0],pos[1]+D[h][1])
                lo_x=min([0]+[p[0] for p in odd]);hi_x=max([0]+[p[0] for p in odd]);lo_y=min([0]+[p[1] for p in odd]);hi_y=max([0]+[p[1] for p in odd])
                for x in range(lo_x-1,hi_x+2):
                    for y in range(lo_y-1,hi_y+2):
                        shifted=(depth,x+shift[0]*depth,y+shift[1]*depth)
                        actual=evaluate(M,shifted) if min(shifted)>=0 else 0
                        assert actual==int((x,y) in odd);checks+=1
        result['literal_requirement_memberships']=position_checks;result['literal_parity_checks']=checks
        records.append(result);print('RESULT',json.dumps(result),flush=True)
    out=dict(records=records,scope='Integrated exact all-depth realization decision for flat decorated additive-I typed refinement families, arbitrary finite seed mass/radius. Root-growing legality is a special case. No accepted growing model or global highway theorem.')
    (HERE/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
    return out
if __name__=='__main__':run_controls()
