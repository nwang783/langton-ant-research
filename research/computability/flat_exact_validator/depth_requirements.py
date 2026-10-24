"""All-depth internal legality and exact input-fuel weighted-automaton controls.
Preserving refinement depth lets different depths have different entry boards.
This is distinct from flat_forced_seed's ONE fixed input board question.
"""
import itertools,json,math,pathlib,time,sys
import sympy as S
from flat_forced_seed import *


def compile_depth(model):
    shift,machines,rat=model.parity_machines();schemes=model.schemes()
    relations={sign:(FALSE,FALSE) for sign in itertools.product((-1,1),repeat=2)}
    for scheme in schemes:
        c=compile_scheme(model,scheme,shift,machines);vs=c['variables']
        coeff,constant=c['length'];eq=linear(dict(zip(vs,coeff))|{'r':-1},-constant)
        for signs,(black,white) in list(relations.items()):
            spatial=locate(c,*signs)&eq
            # Disjoint orthants: zero belongs only to the positive sign.
            for coord,sign in zip(('x','y'),signs):
                if sign<0:spatial=spatial&linear({coord:1},1,'>=')
            b=(spatial&c['black']).exists(*vs);w=(spatial&~c['black']).exists(*vs)
            relations[signs]=(black|b,white|w)
    bad=FALSE
    for b,w in relations.values():bad=bad|(b&w).exists('x','y')
    return relations,bad,rat


def count_representation(A,extra):
    """Count x,y choices for fixed r bits, plus enough forced-zero r padding.
    Since all actual positions satisfy |coordinate|<=max_edge_offset*r,
    this fixed extra bit count covers every spatial witness exactly once.
    """
    assert set(A.vs)=={'r','x','y'};n=len(A.tr);ri=A.vs.index('r');xi=A.vs.index('x');yi=A.vs.index('y')
    matrices=[]
    for rb in (0,1):
        M=S.zeros(n)
        for q,row in enumerate(A.tr):
            for xb,yb in itertools.product((0,1),repeat=2):M[q,row[(rb<<ri)|(xb<<xi)|(yb<<yi)]]+=1
        matrices.append(M)
    begin=S.zeros(1,n);begin[A.start]=1
    end=S.Matrix([int(q in A.ac) for q in range(n)])
    end=matrices[0]**extra*end
    return begin,matrices,end


def combine(reps):
    initial=S.Matrix.hstack(*(a for a,m,b in reps));final=S.Matrix.vstack(*(b for a,m,b in reps))
    matrices=[S.diag(*(m[d] for a,m,b in reps)) for d in (0,1)]
    return initial,matrices,final


def linear_representation(alpha,beta,zero_correction=0):
    a=S.Matrix([[0,1,1]]);M=[S.Matrix([[1,0,0],[d,2,0],[0,0,1]]) for d in (0,1)];b=S.Matrix([alpha,0,beta])
    reps=[(a,M,b)]
    if zero_correction:reps.append((S.Matrix([[1]]),[S.Matrix([[1]]),S.Matrix([[0]])],S.Matrix([zero_correction])))
    return combine(reps)


def equivalent_zero(rep):
    """Exact Q-linear reachable-row-space equality for EVERY binary word."""
    start,M,end=rep;basis={};queue=[start];steps=0
    for row in queue:
        values=list(row)
        for pivot,old in sorted(basis.items()):
            if values[pivot]:
                factor=values[pivot];values=[a-factor*b for a,b in zip(values,old)]
        pivot=next((i for i,v in enumerate(values) if v),None)
        if pivot is None:continue
        factor=values[pivot];values=[v/factor for v in values];basis[pivot]=values
        vector=S.Matrix([values]);steps+=1
        if (vector*end)[0]!=0:return False,dict(rank=len(basis),checks=steps)
        for matrix in M:queue.append(vector*matrix)
    return True,dict(rank=len(basis),checks=steps)


def prove_fuel(model,relations,alpha,beta=0,zero_correction=0):
    maxoffset=max(abs(a) for s in model.reach for e in model.phi[s] for a in e.offset)
    extra=maxoffset.bit_length()+1
    reps=[count_representation(b,extra) for b,w in relations.values()]
    expected=linear_representation(-alpha,-beta,-zero_correction);reps.append(expected)
    okay,certificate=equivalent_zero(combine(reps));assert okay
    return dict(alpha=alpha,beta=beta,zero_correction=zero_correction,extra_spatial_bits=extra,
                weighted_states=sum(m[0].rows for a,m,b in reps),**certificate)


def main():
    start=time.monotonic();records=[]
    for name,model,bad_expected,fuel in [
        ('identity_R',identity(0),FALSE,(0,0,0)),
        ('identity_L',identity(1),FALSE,(0,1,0)),
        ('rooted_R5',right_five_flat(),linear({'r':1},1,'>='),None),
        ('oblique_hairpin',hairpin('LRLLLLRRRRLRRL','RLRRLL'),FALSE,(6,0,0)),
        ('axial_hairpin',hairpin('RRLRRRRL','LLRLLRLL'),FALSE,(4,2,-2))]:
        print('BEGIN',name,flush=True);rels,bad,rat=compile_depth(model)
        assert bad.both(bad_expected,lambda a,b:a!=b).witness() is None
        record=dict(name=name,bad_depth_states=len(bad.tr),all_depths_internally_legal=bad.witness() is None,
                    black_relation_states={str(s):len(b.tr) for s,(b,w) in rels.items()})
        if fuel:record['all_binary_input_fuel_proof']=prove_fuel(model,rels,*fuel)
        literal=0
        for r in range(25):
            initial={};conflict=False;odd=set()
            for p,turn,s in model.literal(r):
                value=turn^int(p in odd)
                if p in initial and initial[p]!=value:conflict=True
                initial[p]=value;odd.symmetric_difference_update({p})
            assert bad.eval(r=r)==conflict
            if not conflict:
                wanted=sum(initial.values());actual=0
                for signs,(b,w) in rels.items():
                    c=max(abs(a) for s in model.reach for e in model.phi[s] for a in e.offset)*r
                    for x in range(c+1):
                        for y in range(c+1):
                            if b.eval(r=r,x=x,y=y):actual+=1
                assert actual==wanted
                if fuel:assert wanted==fuel[0]*r+fuel[1]+fuel[2]*(r==0)
            literal+=1
        record['literal_complete_depth_checks']=literal;records.append(record);print('RESULT',json.dumps(record),flush=True)
    out=dict(records=records,seconds=time.monotonic()-start,
        scope='Exact all-depth internal-legality automata and all-binary fuel equalities for flat typed families. Distinct entry boards are allowed at different depths. No growing finite-seed model or wrapper exclusion.')
    (HERE/'depth_requirements.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',out['seconds'],flush=True)
if __name__=='__main__':main()
