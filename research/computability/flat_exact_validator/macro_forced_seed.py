"""Flat exact-pose refinement with finite physical BASE WORDS per state.

Unlike the signed single-read compiler, a state can carry a multi-read base
word, including zero net displacement. No unit-letter subdivision is assumed.
All image poses, terminal physical reads and their complete prior parity are
checked explicitly. The original JX source is not modified.
"""
from flat_forced_seed import *
from depth_requirements import count_representation,combine,equivalent_zero,linear_representation


def physical_trace(word,heading):
    p=(0,0);h=heading;reads=[]
    for ch in word:
        turn=1 if ch=='R' else -1;reads.append((p,int(turn==-1),h))
        h=(h+turn)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
    return tuple(reads),p,h


class MacroModel:
    schemes=Model.schemes
    def __init__(self,bases,images,root=0):
        if not isinstance(bases,(list,tuple)) or not bases or not isinstance(images,(list,tuple)) or len(bases)!=len(images):
            raise ValueError('finite nonempty base alphabet and matching image sequence required')
        if type(root) is not int or not 0<=root<len(bases):raise ValueError('integer root index required')
        for base in bases:
            if not isinstance(base,(list,tuple)) or len(base)!=2 or type(base[0]) is not int or base[0] not in range(4):
                raise ValueError('base must be (integer heading, nonempty R/L string)')
            if not isinstance(base[1],str) or not base[1] or not set(base[1])<=set('RL'):
                raise ValueError('nonempty finite R/L base word required')
        for row in images:
            if not isinstance(row,(tuple,list)) or not row or any(type(t) is not int or not 0<=t<len(bases) for t in row):
                raise ValueError('nonempty finite integer-index images required')
        self.bases=tuple(tuple(b) for b in bases);self.images=tuple(tuple(w) for w in images);self.root=root
        self.traces=[];self.net=[];self.end=[]
        for h,w in self.bases:
            trace,net,end=physical_trace(w,h);self.traces.append(trace);self.net.append(net);self.end.append(end)
        self.phi=[]
        for s,row in enumerate(self.images):
            p=(0,0);h=self.bases[s][0];edges=[]
            for j,t in enumerate(row):
                if self.bases[t][0]!=h:raise ValueError(('macro heading mismatch',s,j,h,self.bases[t][0]))
                edges.append(Edge(s,j,t,p));p=add(p,self.net[t]);h=self.end[t]
            if p!=self.net[s] or h!=self.end[s]:raise ValueError(('macro pose mismatch',s,p,h,self.net[s],self.end[s]))
            self.phi.append(tuple(edges))
        reach={root};queue=[root]
        for s in queue:
            for e in self.phi[s]:
                if e.target not in reach:reach.add(e.target);queue.append(e.target)
        self.reach=tuple(sorted(reach));follows={s:{s} for s in reach}
        for s in reach:
            queue=[s]
            for t in queue:
                for e in self.phi[t]:
                    if e.target not in follows[s]:follows[s].add(e.target);queue.append(e.target)
        remain=set(reach);components=[]
        while remain:
            s=min(remain);c=frozenset(t for t in remain if t in follows[s] and s in follows[t]);remain-=c;components.append(c)
        self.components=tuple(components);self.comp={s:c for c in components for s in c};self.internal={}
        for s in self.reach:
            internal=[e for e in self.phi[s] if e.target in self.comp[s]]
            if len(internal)>1:raise Unsupported('branching occurrence SCC; flat macro compiler only')
            self.internal[s]=internal[0] if internal else None

    def parity_machines(self):
        C=max(0,-min(e.offset[0] for s in self.reach for e in self.phi[s]));Dshift=max(0,-min(e.offset[1] for s in self.reach for e in self.phi[s]))
        Bx=max(0,-min(p[0] for s in self.reach for p,t,h in self.traces[s]));By=max(0,-min(p[1] for s in self.reach for p,t,h in self.traces[s]))
        ids={s:i for i,s in enumerate(self.reach)};n=len(ids);T=S.zeros(n);base=S.zeros(n,1)
        for s in self.reach:
            for e in self.phi[s]:T[ids[s],ids[e.target]]+=X**(e.offset[0]+C)*Y**(e.offset[1]+Dshift)
            for p,t,h in self.traces[s]:base[ids[s]]+=X**(p[0]+Bx)*Y**(p[1]+By)
        A=DomainMatrix.from_Matrix(S.eye(n)-Z*T)
        # Identity macro images can leave x,y absent from the transfer matrix
        # while their multi-read base polynomial still needs those variables.
        # Unify BOTH domains rather than coercing the base into ZZ[z].
        A,rhs=A.unify(DomainMatrix.from_Matrix(base))
        N,den=A.solve_den(rhs);N=N.to_Matrix();den=A.domain.to_sympy(den);machines={};cert={}
        for s,i in ids.items():
            P,H=S.fraction(S.cancel(N[i]/den));p=S.Poly(P,*VARIABLES,modulus=2);h=S.Poly(H,*VARIABLES,modulus=2)
            if h.coeff_monomial((0,0,0))!=1:raise ValueError('macro parity denominator must be a unit')
            gcd=S.gcd(p,h);p=p.exquo(gcd);h=h.exquo(gcd)
            machines[s]=machine([] if p.is_zero else p.monoms(),h.monoms())
            cert[s]=dict(numerator=str(p.as_expr()),denominator=str(h.as_expr()),states=len(machines[s]['states']))
        return ((C,Dshift),(Bx,By)),machines,cert

    def literal(self,depth):
        word=[self.root]
        for _ in range(depth):word=[t for s in word for t in self.images[s]]
        p=(0,0);h=self.bases[self.root][0];out=[]
        for s in word:
            assert self.bases[s][0]==h
            for q,turn,ih in self.traces[s]:out.append((add(p,q),turn,s))
            p=add(p,self.net[s]);h=self.end[s]
        return out


def compile_terminal(model,scheme,read_index,shift,machines):
    chunks,terminal=scheme;tau,turn,heading=model.traces[terminal][read_index]
    base_prior=sum(p==tau for p,t,h in model.traces[terminal][:read_index])%2
    k=sum(cyc for cyc,es in chunks);vs=tuple('n'+str(i) for i in range(k));zero=(0,)*k
    total_c=[0,tau[0],tau[1]];total_v=[list(zero) for _ in range(3)];counter=0
    for cyc,es in chunks:
        weight=edge_sum(es)
        if cyc:
            for h in range(3):total_v[h][counter]+=weight[h]
            counter+=1
        else:
            for h in range(3):total_c[h]+=weight[h]
    prefix_c=[0,0,0];prefix_v=[list(zero) for _ in range(3)];counter=0;prior=TRUE if base_prior else FALSE;terms=0
    for cyc,es in chunks:
        cycleweight=edge_sum(es);local=[0,0,0]
        for e in es:
            for sibling in model.phi[e.source][:e.index]:
                cf=[tuple(total_v[h][i]-prefix_v[h][i] for i in range(k)) for h in range(3)]
                cc=[total_c[0]-prefix_c[0]-local[0]-1,
                    total_c[1]-prefix_c[1]-local[1]-sibling.offset[0],
                    total_c[2]-prefix_c[2]-local[2]-sibling.offset[1]]
                if cyc:cf=[cf[h]+(-cycleweight[h],) for h in range(3)]
                variables=vs+('q',) if cyc else vs
                (C,Dshift),(Bx,By)=shift
                coeff=(cf[0],tuple(a+C*b for a,b in zip(cf[1],cf[0])),tuple(a+Dshift*b for a,b in zip(cf[2],cf[0])))
                const=(cc[0],cc[1]+C*cc[0]+Bx,cc[2]+Dshift*cc[0]+By)
                term=affine_pullback(machines[sibling.target],variables,coeff,const)
                if cyc:term=parity_bounded(term,'q',vs[counter])
                prior=prior.both(term,lambda a,b:a!=b);terms+=1
            local[0]+=1;local[1]+=e.offset[0];local[2]+=e.offset[1]
        if cyc:
            for h in range(3):prefix_v[h][counter]+=cycleweight[h]
            counter+=1
        else:
            for h in range(3):prefix_c[h]+=local[h]
    assert prefix_c==[total_c[0],total_c[1]-tau[0],total_c[2]-tau[1]] and prefix_v==total_v
    black=~prior if turn else prior
    return dict(variables=vs,prior=prior,black=black,terminal=terminal,base_read=read_index,
                length=(tuple(total_v[0]),total_c[0]),x=(tuple(total_v[1]),total_c[1]),y=(tuple(total_v[2]),total_c[2]),terms=terms)


def compile_macro(model,keep_depth=True,verbose=False):
    start=time.monotonic();shift,machines,rat=model.parity_machines();schemes=model.schemes()
    rels={sign:(FALSE,FALSE) for sign in itertools.product((-1,1),repeat=2)};compiled=[]
    for i,scheme in enumerate(schemes):
        for j in range(len(model.traces[scheme[1]])):
            c=compile_terminal(model,scheme,j,shift,machines);compiled.append((scheme,c));vs=c['variables']
            if keep_depth:
                coeff,constant=c['length'];eq=linear(dict(zip(vs,coeff))|{'r':-1},-constant)
            else:eq=TRUE
            for signs,(black,white) in list(rels.items()):
                guard=locate(c,*signs)&eq
                for coord,sign in zip(('x','y'),signs):
                    if sign<0:guard=guard&linear({coord:1},1,'>=')
                b=(guard&c['black']).exists(*vs);w=(guard&~c['black']).exists(*vs)
                rels[signs]=(black|b,white|w)
        if verbose:print('scheme',i+1,'/',len(schemes),flush=True)
    bad=FALSE
    for b,w in rels.values():bad=bad|(b&w).exists('x','y')
    result=dict(schemes=len(schemes),terminal_scheme_reads=len(compiled),parity=rat,
                black_states={str(s):len(b.tr) for s,(b,w) in rels.items()},bad_states=len(bad.tr),
                keep_depth=keep_depth,seconds=time.monotonic()-start)
    if keep_depth:result['all_depths_internally_legal']=bad.witness() is None
    else:
        finite=all(b.bounded() for b,w in rels.values());conflict=bad.truth()
        possible=not conflict and finite;seed=None
        if possible:
            points=set()
            for signs,(black,white) in rels.items():
                if black.witness() is None:continue
                m='_bound';guard=linear({m:1,'x':-1},0,'>=')&linear({m:1,'y':-1},0,'>=')
                bound=black.implies(guard).forall('x','y').witness()[m]
                for x in range(bound+1):
                    for y in range(bound+1):
                        if black.eval(x=x,y=y):points.add((signs[0]*x,signs[1]*y))
            seed=sorted(points)
        nested=model.images[model.root][0]==model.root
        growing=nested and len(model.images[model.root])>1
        result.update(same_board_consistent=not conflict,finite_black_requirement=finite,possible=possible,seed=seed,
                      nested_root=nested,growing_root=growing,accepted_growing_model=possible and growing)
    return result,rels,bad,compiled,machines,shift


def prove_macro_fuel(model,relations,alpha,beta=0,zero_correction=0):
    maxedge=max(abs(a) for s in model.reach for e in model.phi[s] for a in e.offset)
    maxbase=max(abs(a) for s in model.reach for p,t,h in model.traces[s] for a in p)
    extra=(maxedge+maxbase+1).bit_length()+1
    reps=[count_representation(b,extra) for b,w in relations.values()]
    reps.append(linear_representation(-alpha,-beta,-zero_correction))
    okay,certificate=equivalent_zero(combine(reps));assert okay
    return dict(alpha=alpha,beta=beta,zero_correction=zero_correction,padding_bits=extra,
                weighted_states=sum(M[0].rows for a,M,b in reps),**certificate)


def capped_rod(central='LLLR'):
    bases=[(h,('R' if turn==1 else 'L')) for h in range(4) for turn in (1,-1)]
    images=[[s] for s in range(8)]
    A='LRRL';B='RLLR';cap='RRRL';heading=1
    b=len(bases);bases.append((heading,central));images.append([])
    root=len(bases);bases.append((heading,central+cap));images.append([])
    left=word_states(A,heading);afterA=(heading+sum(1 if c=='R' else -1 for c in A))%4
    _,_,afterC=physical_trace(central,afterA)
    right=word_states(B,afterC);_,_,afterB=physical_trace(B,afterC)
    tail=word_states(cap,afterB)
    images[b]=left+[b]+right;images[root]=left+[b]+right+tail
    return MacroModel(bases,images,root)


def verify_capped_tables(model,relations,machines,shift,growth=False):
    """Exact automatic equality with complete input/output/XOR/support tables."""
    eq=lambda name,n:linear({name:1},n)
    row=(eq('y',0)&linear({'r':2,'x':-1},0,'>='))
    right=eq('y',1)&linear({'x':1,'r':-2},1 if growth else 0)
    left=(eq('x',2)&(eq('y',0)|eq('y',1)))
    results=[]
    for signs,(black,white) in relations.items():
        sx,sy=signs;guard=TRUE
        for coord,sign in zip(('x','y'),signs):
            if sign<0:guard=guard&linear({coord:1},1,'>=')
        incoming=FALSE;xor=FALSE;support=FALSE
        if sy==1:
            if sx==1:
                incoming=row if growth else row|(eq('y',1)&linear({'x':1,'r':-2},0))
                xor=right if growth else (linear({'x':1,'r':-2},0)&(eq('y',0)|eq('y',1)))
                if growth:xor=linear({'x':1,'r':-2},1)&(eq('y',0)|eq('y',1))
                support=(eq('y',0)|eq('y',1))&linear({'r':2,'x':-1},-int(growth),'>=')
            else:
                incoming=eq('x',1)&eq('y',1);xor=left
                support=(eq('y',0)|eq('y',1))&linear({'x':-1},-2,'>=')
        incoming=incoming&guard;xor=xor&guard;support=support&guard
        assert black.both(incoming,lambda a,b:a!=b).witness() is None
        assert (black|white).both(support,lambda a,b:a!=b).witness() is None
        (C,Dshift),(Bx,By)=shift
        parity=affine_pullback(machines[model.root],('r','x','y'),
            ((1,0,0),(C,sx,0),(Dshift,0,sy)),(0,Bx,By))&guard
        assert parity.both(xor,lambda a,b:a!=b).witness() is None
        output=black.both(parity,lambda a,b:a!=b)
        expected=incoming.both(xor,lambda a,b:a!=b)
        assert output.both(expected,lambda a,b:a!=b).witness() is None
        results.append(dict(signs=signs,input_states=len(black.tr),output_states=len(output.tr),
                            xor_states=len(parity.tr),support_states=len((black|white).tr)))
    return dict(all_binary_input_output_xor_support_equalities=16,orthants=results)


def main():
    records=[]
    for name,central,fuel in [('domino_transport','LLLR',(2,3,0)),('domino_growth','LRRRRLLR',(2,2,0))]:
        print('BEGIN',name,flush=True);model=capped_rod(central)
        result,rels,bad,compiled,machines,shift=compile_macro(model,True,True)
        assert result['all_depths_internally_legal']
        result['fuel_proof']=prove_macro_fuel(model,rels,*fuel)
        result['exact_board_tables']=verify_capped_tables(model,rels,machines,shift,central!='LLLR')
        checks=0
        for r in range(33):
            reads=model.literal(r);initial={};odd=set()
            for p,turn,s in reads:
                need=turn^int(p in odd)
                if p in initial:assert initial[p]==need
                initial[p]=need;odd.symmetric_difference_update({p})
            assert sum(initial.values())==fuel[0]*r+fuel[1]
            C=max(abs(a) for p,turn,s in reads for a in p)
            for x in range(-C-1,C+2):
                for y in range(-3,4):
                    signs=tuple(1 if a>=0 else -1 for a in (x,y));b,w=rels[signs];vals=dict(r=r,x=abs(x),y=abs(y))
                    assert b.eval(**vals)==bool(initial.get((x,y),0));checks+=1
        result['literal_complete_input_cells']=checks;result['name']=name
        fixed,_,_,_,_,_=compile_macro(model,False)
        assert not fixed['possible'] and not fixed['finite_black_requirement']
        result['same_board_decision']=fixed
        records.append(result);print('RESULT',json.dumps(result),flush=True)
    generic=[]
    for name,model,expected in [
        ('identity_multiread',MacroModel([(1,'LLLRRRRL')],[[0]]),True),
        ('two_cycle_multiread',MacroModel([(1,'LLLRRRRL')]*2,[[1],[0]]),True),
        ('identity_zero_parity_illegal',MacroModel([(0,'RRRRRRRR')],[[0]]),False)]:
        result,rels,bad,compiled,machines,shift=compile_macro(model,False)
        assert result['possible']==expected
        if expected:assert result['seed']==[(-1,1),(0,0),(0,1)]
        generic.append(dict(name=name,**result));print('GENERIC',name,result['possible'],flush=True)
    out=dict(records=records,scope='Exact flat finite-base macro refinement. Both capped families internally legal at every depth, with different prepared input boards and infinite union fuel. No renewable device or finite-seed growing trajectory.')
    out['generic_controls']=generic
    (HERE/'macro_controls.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
