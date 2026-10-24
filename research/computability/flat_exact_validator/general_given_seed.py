"""Integrated IJ given-seed frame validator for arbitrary additive-I unit images.

No flatness hypothesis: branching occurrence SCCs are allowed. Read footprints
are compiled exactly by Euler-count Presburger construction, converted through
public ISL lifting APIs, then checked with exact automatic relations. Resource
errors raise UNKNOWN rather than being interpreted as negative realization.
"""
from flat_forced_seed import *
from renewal_interfaces import affine_relation
from isl_automatic import Context,relation,convert


class GeneralUnitModel(Model):
    def __init__(self,*args,**kwargs):
        try:super().__init__(*args,**kwargs)
        except Unsupported as error:
            # Core Model has already completed strict finite input/geometry,
            # reachability and SCC checks. Only its explicit flat architecture
            # filter is skipped. No geometry/ISL/runtime exception is swallowed.
            if str(error)!='branching occurrence SCC; this compiler is flat-only':raise
            self.internal=None


def from_strings(images,root=0):
    if not isinstance(images,(list,tuple)) or len(images)!=8 or any(not isinstance(w,str) or not w or not set(w)<=set('RL') for w in images):
        raise ValueError('eight nonempty physical R/L image strings required')
    return GeneralUnitModel(standard_physical(),[word_states(w,s//2) for s,w in enumerate(images)],root)


def plus(a,b):
    coeff=dict(a[0])
    for v,c in b[0].items():coeff[v]=coeff.get(v,0)+c
    return coeff,a[1]+b[1]
def times(c,a):return {v:c*x for v,x in a[0].items()},c*a[1]
def constant(c):return {},c


def canonical_prefixes(model):
    refs={model.root:()};word=[model.root]
    for depth in range(len(model.reach)+1):
        for i,s in enumerate(word):
            if s not in refs:refs[s]=tuple(word[:i])
        if set(refs)==set(model.reach):break
        word=[t for s in word for t in model.images[s]]
    else:raise AssertionError('reachable state not found by its shortest graph-path depth')
    positions={};tables={}
    for s,w in refs.items():
        p=(0,0);heading=model.physical[model.root][0];trace=[]
        for t in w:
            assert model.physical[t][0]==heading
            trace.append((t,p));heading=(heading+model.physical[t][1])%4;p=add(p,D[heading])
        positions[s]=p;tables[s]=trace
    return refs,positions,tables


class GivenSeedValidator:
    def __init__(self,model,seed,verbose=False,max_operations=30000000):
        self.model=model;self.verbose=verbose
        if not isinstance(seed,(list,tuple,set,frozenset)) or any(not isinstance(p,(tuple,list)) or len(p)!=2 or any(type(a) is not int for a in p) for p in seed):
            raise ValueError('finite integer-coordinate seed list required')
        self.seed=frozenset(tuple(p) for p in seed)
        if verbose:print('PARITY BEGIN',flush=True)
        self.shift,self.machines,self.rational=model.parity_machines()
        if verbose:print('PARITY COMPLETE',flush=True)
        self.refs,self.positions,self.prefix=canonical_prefixes(model)
        ctx=Context(max_operations=max_operations);self.read={};self.read_stats={}
        # Every reachable state starts a finite subgraph; use only its actual
        # descendants so disconnected vertices do not inflate Euler formulas.
        for s in model.reach:
            reach={s};queue=[s]
            for t in queue:
                for e in model.phi[t]:
                    if e.target not in reach:reach.add(e.target);queue.append(e.target)
            edges=[(t,e.target,e.offset) for t in reach for e in model.phi[t]]
            ctx.reset_operations();R,formula=relation(ctx,sorted(reach),edges,s);self.read[s]={};states=[]
            for signs in itertools.product((-1,1),repeat=2):
                A,stats=convert(R,('r','x','y'),(1,*signs));self.read[s][signs]=A;states.append(len(A.tr))
            self.read_stats[s]=dict(isl_relation=str(R),automaton_states=states,edge_types=len(set(edges)))
            if verbose:print('READ',s,states,str(R),flush=True)

    def Q(self,s,r,x,y,variables):
        C,Dshift=self.shift
        args=(r,plus(x,times(C,r)),plus(y,times(Dshift,r)))
        coeff=tuple(tuple(a[0].get(v,0) for v in variables) for a in args);const=tuple(a[1] for a in args)
        return affine_pullback(self.machines[s],variables,coeff,const)

    def B(self,x,y):
        out=FALSE
        for a,b in self.seed:out=out|(linear(x[0],a-x[1])&linear(y[0],b-y[1]))
        return out

    def I(self,s,r,x,y,variables):
        z=self.positions[s];x=plus(x,constant(z[0]));y=plus(y,constant(z[1]));out=self.B(x,y)
        for t,p in self.prefix[s]:
            out=out.both(self.Q(t,r,plus(x,constant(-p[0])),plus(y,constant(-p[1])),variables),lambda a,b:a!=b)
        return out

    def R(self,s,r,x,y,variables):
        out=FALSE
        for signs,A in self.read[s].items():
            forms={'r':r,'x':times(signs[0],x),'y':times(signs[1],y)}
            out=out|affine_relation(A,variables,forms)
        return out

    def solve(self):
        model=self.model;checks=0
        for s in model.reach:
            z=self.positions[s];initial=int(z in self.seed)^sum(p==z for t,p in self.prefix[s])%2
            required=int(model.physical[s][1]==-1)
            if initial!=required:return dict(possible=False,reason='canonical zero-depth turn',state=s,frame_checks=0)
        variables=('r','x','y');r=({'r':1},0)
        for s in model.reach:
            for signs in itertools.product((-1,1),repeat=2):
                x=({'x':signs[0]},0);y=({'y':signs[1]},0)
                current=self.I(s,plus(r,constant(1)),x,y,variables)
                for e in model.phi[s]:
                    cx=plus(x,constant(-e.offset[0]));cy=plus(y,constant(-e.offset[1]))
                    wanted=self.I(e.target,r,cx,cy,variables);guard=self.R(e.target,r,cx,cy,variables)
                    bad=current.both(wanted,lambda a,b:a!=b)&guard;checks+=1;witness=bad.witness()
                    if witness is not None:
                        witness['x']*=signs[0];witness['y']*=signs[1]
                        return dict(possible=False,reason='all-depth frame disagreement',state=s,child_index=e.index,witness=witness,frame_checks=checks)
                    current=current.both(self.Q(e.target,r,cx,cy,variables),lambda a,b:a!=b)
            if self.verbose:print('FRAME',s,checks,flush=True)
        nested=model.images[model.root][0]==model.root;growing=nested and len(model.images[model.root])>1
        return dict(possible=True,frame_checks=checks,nested_root=nested,growing_root=growing,accepted_growing_model=growing,
                    seed=sorted(self.seed))


def minimal_seed_for_word(model,depth):
    odd=set();initial={}
    for p,turn,s in model.literal(depth):
        need=turn^int(p in odd)
        if p in initial and initial[p]!=need:return None
        initial[p]=need;odd.symmetric_difference_update({p})
    return sorted(p for p,b in initial.items() if b)


def main():
    start=time.monotonic();records=[]
    transient_nine=GeneralUnitModel(standard_physical()+[(0,1)],[[s] for s in range(8)]+[word_states('RLLLLRRRR')],8)
    controls=[('identity_R_empty',identity(0),[],True),('identity_L_empty',identity(1),[],False),
              ('identity_L_origin',identity(1),[(0,0)],True),
              ('branching_R5',from_strings(['RRRRR','LLLLL']*4),[],False),
              ('two_cycle_single_read',GeneralUnitModel([(0,1)]*2,[[1],[0]],0),[],True),
              ('transient_nine_positive',transient_nine,None,True)]
    for name,model,seed,expected in controls:
        if seed is None:seed=minimal_seed_for_word(model,1);assert seed is not None
        print('BEGIN',name,'seed',seed,flush=True);validator=GivenSeedValidator(model,seed,True)
        result=validator.solve();assert result['possible']==expected
        result.update(name=name,seed=seed,read_set_certificates=validator.read_stats)
        records.append(result);print('RESULT',json.dumps(result),flush=True)
    out=dict(records=records,seconds=time.monotonic()-start,
             scope='Integrated arbitrary branching additive-I physically typed GIVEN-SEED all-depth frame decision. Exact ISL read sets plus rational Cartier parity, no supplied templates. Not an unknown-seed decision or global highway theorem.')
    (HERE/'general_given_seed.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',out['seconds'],flush=True)
if __name__=='__main__':main()
