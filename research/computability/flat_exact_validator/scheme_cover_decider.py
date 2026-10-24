"""Selector-free arbitrary-seed decision from a genuine POSITION scheme cover.

Schemes need not cover all occurrence words or preserve the earliest visit.
Their complete selected requirements force a candidate; exact position coverage
plus the general given-seed frame validator supplies sufficiency. A partial
cover may already certify NO by conflicting bits or infinite black demand.
"""
from general_given_seed import *


def validate_scheme(model,scheme):
    chunks,terminal=scheme;s=model.root
    if type(terminal) is not int or terminal not in model.reach:raise ValueError('invalid terminal state')
    for cycle,edges in chunks:
        if type(cycle) is not bool or not isinstance(edges,(list,tuple)) or not edges:raise ValueError('nonempty finite chunks required')
        before=s
        for e in edges:
            if not isinstance(e,Edge) or e.source!=s or type(e.index) is not int or not 0<=e.index<len(model.phi[s]) or model.phi[s][e.index]!=e:
                raise ValueError('scheme is not a genuine occurrence walk')
            s=e.target
        if cycle and s!=before:raise ValueError('starred chunk is not a closed graph walk')
    if s!=terminal:raise ValueError('wrong terminal state')


def selected_requirements(model,schemes,verbose=False):
    if not isinstance(schemes,(list,tuple)) or not schemes:raise ValueError('finite nonempty scheme list required')
    for scheme in schemes:validate_scheme(model,scheme)
    shift,machines,rat=model.parity_machines();relations={s:(FALSE,FALSE) for s in itertools.product((-1,1),repeat=2)}
    for j,scheme in enumerate(schemes):
        c=compile_scheme(model,scheme,shift,machines);vs=c['variables']
        for signs,(black,white) in list(relations.items()):
            spatial=locate(c,*signs)
            for coord,sign in zip(('x','y'),signs):
                if sign<0:spatial=spatial&linear({coord:1},1,'>=')
            b=(spatial&c['black']).exists(*vs);w=(spatial&~c['black']).exists(*vs)
            relations[signs]=(black|b,white|w)
        if verbose:print('SELECTED',j+1,'/',len(schemes),flush=True)
    return relations,rat


def extract_seed(relations):
    points=set()
    for signs,(black,white) in relations.items():
        if black.witness() is None:continue
        guard=linear({'m':1,'x':-1},0,'>=')&linear({'m':1,'y':-1},0,'>=')
        bound=black.implies(guard).forall('x','y').witness()['m']
        for x in range(bound+1):
            for y in range(bound+1):
                if black.eval(x=x,y=y):points.add((signs[0]*x,signs[1]*y))
    return sorted(points)


def solve(model,schemes,verbose=False,max_operations=30000000):
    start=time.monotonic();relations,rat=selected_requirements(model,schemes,verbose);conflicts={};finite=True
    for signs,(black,white) in relations.items():
        witness=(black&white).witness()
        if witness is not None:conflicts[str(signs)]=witness
        finite=finite and black.bounded()
    result=dict(schemes=len(schemes),selected_requirements={str(s):[len(b.tr),len(w.tr)] for s,(b,w) in relations.items()},
                selected_conflicts=conflicts,selected_black_finite=finite)
    if conflicts or not finite:
        result.update(status='decided',possible=False,reason='inconsistent or infinite genuine selected requirements',
                      coverage_required_for_this_negative=False,seconds=time.monotonic()-start)
        return result
    # A complete all-depth read relation is needed only if a finite candidate
    # survives. Its spatial projection is the EXACT visited set.
    ctx=Context(max_operations=max_operations);edges=[(s,e.target,e.offset) for s in model.reach for e in model.phi[s]]
    R,formula=relation(ctx,model.reach,edges,model.root);uncovered={}
    for signs,(black,white) in relations.items():
        visited,stats=convert(R,('r','x','y'),(1,*signs));visited=visited.exists('r')
        for coord,sign in zip(('x','y'),signs):
            if sign<0:visited=visited&linear({coord:1},1,'>=')
        witness=(visited&~(black|white)).witness()
        if witness is not None:uncovered[str(signs)]=witness
        # Genuineness proves the other inclusion; checking it independently
        # also catches an implementation/input mismatch rather than trusting it.
        if ((black|white)&~visited).witness() is not None:raise AssertionError('genuine scheme outside exact read set')
    if uncovered:
        result.update(status='incomplete cover',possible=None,uncovered=uncovered,seconds=time.monotonic()-start)
        return result
    seed=extract_seed(relations);validator=GivenSeedValidator(model,seed,verbose,max_operations);frames=validator.solve()
    result.update(status='decided',possible=frames['possible'],position_coverage_exact=True,candidate_seed=seed,
                  given_seed_validation=frames,seconds=time.monotonic()-start)
    return result


def fixed_path(model,indices):
    s=model.root;edges=[]
    for index in indices:
        e=model.phi[s][index];edges.append(e);s=e.target
    return (((False,tuple(edges)),) if edges else ()),s


def main():
    start=time.monotonic();records=[]
    for root in (0,1):
        model=identity(root);schemes=[fixed_path(model,())];result=solve(model,schemes)
        assert result['possible'] and result['candidate_seed']==([] if root==0 else [(0,0)])
        result['name']='identity_'+str(root);records.append(result);print('RESULT',json.dumps(result),flush=True)
    model=from_strings(['RRRRR','LLLLL']*4)
    result=solve(model,[fixed_path(model,())]);assert result['status']=='incomplete cover'
    result['name']='R5_incomplete';records.append(result);print('RESULT',json.dumps(result),flush=True)
    # Only four literal occurrences are supplied, not all R5 occurrence words.
    # They cover all four visited positions; the candidate empty seed MUST
    # then pass through general frames, where it correctly fails.
    schemes=[fixed_path(model,())]+[fixed_path(model,(j,)) for j in (1,2,3)]
    result=solve(model,schemes,True);assert result['position_coverage_exact'] and not result['possible']
    assert result['given_seed_validation']['reason']=='all-depth frame disagreement'
    result['name']='R5_complete_position_cover';records.append(result);print('RESULT',json.dumps(result),flush=True)
    model=from_strings(['RLLLLRRRR','LRRRRLLLL']*4)
    e=model.phi[0][1];f=model.phi[e.target][1];assert f.target==0
    scheme=(((True,(e,f)),),0)
    result=solve(model,[scheme],True);assert not result['possible'] and not result['selected_black_finite']
    result['name']='nine_partial_infinite_black';records.append(result);print('RESULT',json.dumps(result),flush=True)
    out=dict(records=records,seconds=time.monotonic()-start,
        scope='Integrated unknown-mass/radius decision from supplied exact genuine position covers for arbitrary branching additive-I unit presentations; incomplete covers never imply NO. Partial genuine schemes can independently certify infinite forced fuel. General cover generation not yet integrated.')
    (HERE/'scheme_cover_decider.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',out['seconds'],flush=True)
if __name__=='__main__':main()
