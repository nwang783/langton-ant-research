"""Generated genuine bounded covers -> general additive-I finite-seed decision.

Implements JE's support-preserving bounded base/cycle cover, but avoids its
canonical selector by retaining both selected color requirements and applying
exact general given-seed frames to the unique surviving finite candidate.
All optional experiment caps return UNKNOWN, never an inferred NO/YES.
"""
from scheme_cover_decider import *


def edge_key(e):return (e.source,e.index)


def simple_cycles(support):
    support=frozenset(support);vertices={v for e in support for v in (e.source,e.target)}
    outgoing={v:sorted((e for e in support if e.source==v),key=edge_key) for v in vertices};found={}
    def visit(start,v,path,seen):
        for e in outgoing[v]:
            if e.target==start:
                cycle=tuple(path+[e]);rotations=[cycle[j:]+cycle[:j] for j in range(len(cycle))]
                cycle=min(rotations,key=lambda row:tuple(map(edge_key,row)))
                found[tuple(map(edge_key,cycle))]=cycle
            elif e.target not in seen:visit(start,e.target,path+[e],seen|{e.target})
    for v in sorted(vertices):visit(v,v,[],{v})
    return [found[k] for k in sorted(found)]


def support_scheme(model,base):
    """Fixed canonical simple cycles inserted at first visited basepoints."""
    support=set(base);cycles=simple_cycles(support);at={}
    for cycle in cycles:at.setdefault(cycle[0].source,[]).append(cycle)
    chunks=[];done=set();s=model.root
    def fixed(e):
        if chunks and not chunks[-1][0]:chunks[-1]=(False,chunks[-1][1]+(e,))
        else:chunks.append((False,(e,)))
    for i in range(len(base)+1):
        if s not in done:
            for cycle in at.get(s,[]):chunks.append((True,cycle))
            done.add(s)
        if i<len(base):
            e=base[i];assert e.source==s;fixed(e);s=e.target
    scheme=tuple(chunks),s;validate_scheme(model,scheme);return scheme


def bounded_schemes(model,max_length=None,max_schemes=None):
    vertices=len(model.reach);edges=sum(len(model.phi[s]) for s in model.reach);bound=vertices*(edges+1)-1
    stop=bound if max_length is None else min(max_length,bound)
    queue=[()];count=0
    for depth in range(stop+1):
        for path in queue:
            if max_schemes is not None and count>=max_schemes:return
            yield depth,support_scheme(model,path),bound
            count+=1
        if depth<stop:queue=[path+(e,) for path in queue for e in model.phi[path[-1].target if path else model.root]]


def _solve_generated(model,max_length=None,max_schemes=None,max_operations=30000000,verbose=False):
    if max_length is not None and (type(max_length) is not int or max_length<0):raise ValueError('nonnegative length cap required')
    if max_schemes is not None and (type(max_schemes) is not int or max_schemes<1):raise ValueError('positive scheme cap required')
    start=time.monotonic();shift,machines,rat=model.parity_machines()
    rels={sign:(FALSE,FALSE) for sign in itertools.product((-1,1),repeat=2)}
    bound=len(model.reach)*(sum(len(model.phi[s]) for s in model.reach)+1)-1
    count=0;last=-1;early=None
    for depth,scheme,expected_bound in bounded_schemes(model,max_length,max_schemes):
        assert expected_bound==bound;count+=1;last=depth
        c=compile_scheme(model,scheme,shift,machines);vs=c['variables']
        for signs,(black,white) in list(rels.items()):
            guard=locate(c,*signs)
            for coord,sign in zip(('x','y'),signs):
                if sign<0:guard=guard&linear({coord:1},1,'>=')
            b=(guard&c['black']).exists(*vs);w=(guard&~c['black']).exists(*vs)
            b=black|b;w=white|w;rels[signs]=(b,w)
            conflict=(b&w).witness()
            if conflict is not None:early=dict(reason='conflicting genuine requirements',signs=signs,witness=conflict);break
            if not b.bounded():early=dict(reason='infinite genuine required-black set',signs=signs);break
        if verbose and (count<12 or count%100==0):print('BASE',count,'depth',depth,'bound',bound,flush=True)
        if early is not None:break
    out=dict(processed_schemes=count,last_base_length=last,theoretical_base_bound=bound,
             requirement_states={str(s):[len(b.tr),len(w.tr)] for s,(b,w) in rels.items()})
    if early is not None:
        out.update(status='decided',possible=False,early_certificate=early,coverage_exhaustion_needed=False,seconds=time.monotonic()-start);return out
    # If the caller cut enumeration, a finite partial requirement is NOT a yes.
    # In a nonerasing graph, each level has at least one path, so a length cap
    # below the proved bound is always incomplete. A count cap can stop exactly
    # at the last scheme; conservatively calling that UNKNOWN is safe.
    capped=(max_length is not None and max_length<bound) or (max_schemes is not None and count>=max_schemes)
    if capped:
        out.update(status='unknown: explicit cover-enumeration cap',possible=None,seconds=time.monotonic()-start);return out
    assert last==bound
    seed=extract_seed(rels)
    validator=GivenSeedValidator(model,seed,verbose,max_operations);frames=validator.solve()
    out.update(status='decided',possible=frames['possible'],complete_generated_cover=True,candidate_seed=seed,
               given_seed_validation=frames,seconds=time.monotonic()-start);return out


def solve_generated(model,max_length=None,max_schemes=None,max_operations=30000000,verbose=False):
    try:return _solve_generated(model,max_length,max_schemes,max_operations,verbose)
    except (ArithmeticError,MemoryError,RecursionError) as error:
        return dict(status='unknown: exact computation resource/error',possible=None,error_type=type(error).__name__,error=str(error))


def main():
    records=[];start=time.monotonic()
    transient=GeneralUnitModel(standard_physical()+[(0,1)],[[s] for s in range(8)]+[word_states('RLLLLRRRR')],8)
    controls=[('identity_R',identity(0),True),('identity_L',identity(1),True),
              ('two_state_cycle',GeneralUnitModel([(0,1)]*2,[[1],[0]],0),True),
              ('branching_R5',from_strings(['RRRRR','LLLLL']*4),False),
              ('branching_nine',from_strings(['RLLLLRRRR','LRRRRLLLL']*4),False),
              ('transient_nine_positive',transient,True)]
    for name,model,expected in controls:
        print('BEGIN',name,flush=True);result=solve_generated(model,verbose=True);assert result['possible']==expected
        result['name']=name;records.append(result);print('RESULT',json.dumps(result),flush=True)
    capped=solve_generated(transient,max_length=0);assert capped['possible'] is None
    capped['name']='explicit_cap_unknown';records.append(capped)
    out=dict(records=records,seconds=time.monotonic()-start,
        scope='Integrated generated-cover arbitrary-mass/radius same-board realization decision for arbitrary branching additive-I physical unit presentations, subject to explicit computation resources. Full finite-power matrices and finite macro bases are not in this implementation. No accepted growing model or general finite-seed capture theorem.')
    (HERE/'generated_cover_decider.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',out['seconds'],flush=True)
if __name__=='__main__':main()
