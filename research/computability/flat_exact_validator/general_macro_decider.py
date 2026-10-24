"""Generated-cover arbitrary-branching finite-base MACRO realization at A=I.

Keeps every physical terminal base read, not an assumed single-unit subdivision.
Canonical input templates, exact terminal-offset read sets and finite base-word
legality replace the corresponding unit-only checks. Caps/errors are UNKNOWN.
"""
from macro_forced_seed import *
from generated_cover_decider import bounded_schemes,support_scheme
from general_given_seed import GivenSeedValidator,plus,times,constant
from scheme_cover_decider import extract_seed
from isl_automatic import Context,convert
from presburger_read_set_solver import lin


class GeneralMacroModel(MacroModel):
    def __init__(self,*args,**kwargs):
        try:super().__init__(*args,**kwargs)
        except Unsupported as error:
            if str(error)!='branching occurrence SCC; flat macro compiler only':raise
            self.internal=None


def macro_relation(ctx,model,start):
    reach={start};queue=[start]
    for s in queue:
        for e in model.phi[s]:
            if e.target not in reach:reach.add(e.target);queue.append(e.target)
    vertices=tuple(sorted(reach));edges=sorted(set((s,e.target,e.offset) for s in vertices for e in model.phi[s]));m=len(edges)
    incident={v:[j for j,e in enumerate(edges) if v in e[:2]] for v in vertices}
    balance={v:lin([(j,int(u==v)-int(w==v)) for j,(u,w,p) in enumerate(edges)]) for v in vertices}
    rank={v:'h'+str(j) for j,v in enumerate(vertices)}
    common=[f'n{j}>=0' for j in range(m)]+[f'0<={rank[v]}<={len(vertices)}' for v in vertices]+[f'{rank[start]}=0']
    common.append('r='+lin([(j,1) for j in range(m)]));wx=lin([(j,e[2][0]) for j,e in enumerate(edges)]);wy=lin([(j,e[2][1]) for j,e in enumerate(edges)])
    endings=[]
    for end in vertices:
        degree=' and '.join(f'{balance[v]}={int(v==start)-int(v==end)}' for v in vertices)
        offsets=sorted({p for p,turn,h in model.traces[end]})
        cells=' or '.join(f'(x=({wx}){p[0]:+d} and y=({wy}){p[1]:+d})' for p in offsets)
        endings.append('('+degree+' and ('+cells+'))')
    common.append('('+' or '.join(endings)+')')
    for v in vertices:
        if v==start:continue
        pieces=[lin([(j,1) for j in incident[v]])+'=0']
        for j in incident[v]:
            u,w,p=edges[j];other=w if u==v else u
            if other!=v:pieces.append(f'(n{j}>0 and {rank[other]}<{rank[v]})')
        common.append('('+' or '.join(pieces)+')')
    names=[f'n{j}' for j in range(m)]+list(rank.values())
    formula='{ [r,x,y] : exists ('+','.join(names)+' : '+' and '.join(common)+') }'
    return ctx.set(formula).coalesce(),formula


def macro_prefixes(model):
    refs={model.root:()};word=[model.root]
    for depth in range(len(model.reach)+1):
        for j,s in enumerate(word):
            if s not in refs:refs[s]=tuple(word[:j])
        if set(refs)==set(model.reach):break
        word=[t for s in word for t in model.images[s]]
    else:raise AssertionError('macro reachable state missing')
    positions={};prefix={}
    for s,word in refs.items():
        p=(0,0);h=model.bases[model.root][0];trace=[]
        for t in word:
            assert model.bases[t][0]==h;trace.append((t,p));p=add(p,model.net[t]);h=model.end[t]
        positions[s]=p;prefix[s]=trace
    return refs,positions,prefix


class MacroGivenSeedValidator(GivenSeedValidator):
    def __init__(self,model,seed,verbose=False,max_operations=30000000):
        self.model=model;self.verbose=verbose
        if not isinstance(seed,(list,tuple,set,frozenset)) or any(not isinstance(p,(tuple,list)) or len(p)!=2 or any(type(a) is not int for a in p) for p in seed):
            raise ValueError('finite integer-coordinate seed required')
        self.seed=frozenset(tuple(p) for p in seed);self.shift,self.machines,self.rational=model.parity_machines()
        self.refs,self.positions,self.prefix=macro_prefixes(model);self.read={};self.read_stats={};ctx=Context(max_operations=max_operations)
        for s in model.reach:
            ctx.reset_operations();R,formula=macro_relation(ctx,model,s);self.read[s]={};states=[]
            for signs in itertools.product((-1,1),repeat=2):
                A,stats=convert(R,('r','x','y'),(1,*signs));self.read[s][signs]=A;states.append(len(A.tr))
            self.read_stats[s]=dict(isl_relation=str(R),automaton_states=states)
            if verbose:print('MACRO READ',s,states,flush=True)

    def Q(self,s,r,x,y,variables):
        (C,Dshift),(Bx,By)=self.shift
        args=(r,plus(plus(x,times(C,r)),constant(Bx)),plus(plus(y,times(Dshift,r)),constant(By)))
        coeff=tuple(tuple(a[0].get(v,0) for v in variables) for a in args);const=tuple(a[1] for a in args)
        return affine_pullback(self.machines[s],variables,coeff,const)

    def solve(self):
        model=self.model;checks=0;base_reads=0
        for s in model.reach:
            z=self.positions[s];before=set()
            for t,p in self.prefix[s]:
                # Toggle each physical read separately. Passing a whole base's
                # iterable to set.symmetric_difference_update would discard
                # duplicate positions BEFORE parity and is not equivalent.
                for q,turn,h in model.traces[t]:before.symmetric_difference_update({add(p,q)})
            within=set()
            for j,(q,turn,h) in enumerate(model.traces[s]):
                p=add(z,q);bit=int(p in self.seed)^int(p in before)^int(q in within);base_reads+=1
                if bit!=turn:return dict(possible=False,reason='canonical literal base-word turn',state=s,base_read=j,frame_checks=0,base_reads=base_reads)
                within.symmetric_difference_update({q})
        variables=('r','x','y');r=({'r':1},0)
        for s in model.reach:
            for signs in itertools.product((-1,1),repeat=2):
                x=({'x':signs[0]},0);y=({'y':signs[1]},0);current=self.I(s,plus(r,constant(1)),x,y,variables)
                for e in model.phi[s]:
                    cx=plus(x,constant(-e.offset[0]));cy=plus(y,constant(-e.offset[1]));wanted=self.I(e.target,r,cx,cy,variables)
                    bad=current.both(wanted,lambda a,b:a!=b)&self.R(e.target,r,cx,cy,variables);checks+=1;witness=bad.witness()
                    if witness is not None:
                        witness['x']*=signs[0];witness['y']*=signs[1]
                        return dict(possible=False,reason='all-depth macro frame disagreement',state=s,child_index=e.index,witness=witness,frame_checks=checks,base_reads=base_reads)
                    current=current.both(self.Q(e.target,r,cx,cy,variables),lambda a,b:a!=b)
            if self.verbose:print('MACRO FRAME',s,checks,flush=True)
        nested=model.images[model.root][0]==model.root;growing=nested and len(model.images[model.root])>1
        return dict(possible=True,frame_checks=checks,base_reads=base_reads,nested_root=nested,growing_root=growing,
                    accepted_growing_model=growing,seed=sorted(self.seed))


def _solve_macro_generated(model,max_length=None,max_schemes=None,max_operations=30000000,verbose=False):
    if max_length is not None and (type(max_length) is not int or max_length<0):raise ValueError('nonnegative base-length cap required')
    if max_schemes is not None and (type(max_schemes) is not int or max_schemes<1):raise ValueError('positive scheme-count cap required')
    start=time.monotonic();shift,machines,rat=model.parity_machines();rels={s:(FALSE,FALSE) for s in itertools.product((-1,1),repeat=2)}
    bound=len(model.reach)*(sum(len(model.phi[s]) for s in model.reach)+1)-1;count=0;last=-1;terminals=0;early=None
    for depth,scheme,expected in bounded_schemes(model,max_length,max_schemes):
        assert expected==bound;count+=1;last=depth
        for j in range(len(model.traces[scheme[1]])):
            terminals+=1;c=compile_terminal(model,scheme,j,shift,machines);vs=c['variables']
            for signs,(black,white) in list(rels.items()):
                guard=locate(c,*signs)
                for coord,sign in zip(('x','y'),signs):
                    if sign<0:guard=guard&linear({coord:1},1,'>=')
                b=black|(guard&c['black']).exists(*vs);w=white|(guard&~c['black']).exists(*vs);rels[signs]=(b,w)
                conflict=(b&w).witness()
                if conflict is not None:early=dict(reason='conflicting genuine macro requirements',signs=signs,witness=conflict);break
                if not b.bounded():early=dict(reason='infinite genuine macro required-black set',signs=signs);break
            if early:break
        if verbose and (count<12 or count%100==0):print('MACRO BASE',count,depth,'/',bound,flush=True)
        if early:break
    out=dict(processed_schemes=count,terminal_read_schemes=terminals,last_base_length=last,theoretical_base_bound=bound)
    if early:
        out.update(status='decided',possible=False,early_certificate=early,seconds=time.monotonic()-start);return out
    capped=(max_length is not None and max_length<bound) or (max_schemes is not None and count>=max_schemes)
    if capped:
        out.update(status='unknown: explicit macro cover cap',possible=None,seconds=time.monotonic()-start);return out
    assert last==bound;seed=extract_seed(rels);validator=MacroGivenSeedValidator(model,seed,verbose,max_operations);frames=validator.solve()
    out.update(status='decided',possible=frames['possible'],complete_generated_cover=True,candidate_seed=seed,
               given_seed_validation=frames,seconds=time.monotonic()-start);return out


def solve_macro_generated(model,**kwargs):
    try:return _solve_macro_generated(model,**kwargs)
    except (ArithmeticError,MemoryError,RecursionError) as error:
        return dict(status='unknown: exact macro computation resources/error',possible=None,error_type=type(error).__name__,error=str(error))


def main():
    records=[]
    revisit_bases=[(h,'R' if turn==1 else 'L') for h in range(4) for turn in (1,-1)]
    revisit_bases += [(1,'LLLRRRRL'),(0,'R'),(1,'LLLRRRRLRRRR')]
    revisit_images=[[s] for s in range(10)]+[[8]+word_states('RRR',1)+[9]]
    revisit=GeneralMacroModel(revisit_bases,revisit_images,10)
    controls=[('identity_multiread',GeneralMacroModel([(1,'LLLRRRRL')],[[0]]),True),
              ('two_state_multiread_cycle',GeneralMacroModel([(1,'LLLRRRRL')]*2,[[1],[0]]),True),
              ('branching_zero_displacement',GeneralMacroModel([(0,'RRRR')],[[0,0]]),False),
              ('zero_parity_illegal',GeneralMacroModel([(0,'RRRRRRRR')],[[0]]),False),
              ('transient_macro_positive',GeneralMacroModel([(1,'LLLR'),(3,'RRRL'),(1,'LLLRRRRL')],[[0],[1],[0,1]],2),True),
              ('canonical_revisited_prefix_positive',revisit,True),
              ('capped_G',capped_rod('LLLR'),False),('capped_H',capped_rod('LRRRRLLR'),False)]
    for name,model,expected in controls:
        print('BEGIN',name,flush=True);result=solve_macro_generated(model,verbose=True);assert result['possible']==expected
        if expected:assert result['candidate_seed']==[(-1,1),(0,0),(0,1)]
        result['name']=name;records.append(result);print('RESULT',json.dumps(result),flush=True)
    # Exercise GENERAL macro frames directly, rather than only early cover NO.
    model=GeneralMacroModel([(0,'RRRR')],[[0,0]])
    validator=MacroGivenSeedValidator(model,[]);negative=validator.solve()
    assert not negative['possible'] and negative['reason']=='all-depth macro frame disagreement'
    capped=solve_macro_generated(controls[4][1],max_length=0);assert capped['possible'] is None
    out=dict(records=records,branching_direct_frame_control=negative,explicit_cap_control=capped,
        scope='Integrated generated-cover arbitrary-mass/radius realization for general branching additive-I finite physical macro bases. No unit subdivision, no finite-order/singular matrix adapter, and no accepted growing model.')
    (HERE/'general_macro_decider.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
