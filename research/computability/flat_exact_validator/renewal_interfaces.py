"""Exact far-interface comparison of image-derived macro I/O relations.

Checks output -> next REQUIRED INPUT on its entire next read set, so garbage
outside that set is not incorrectly treated as an obstruction. A fixed finite
controller may repair any bounded mismatch union. Unbounded mismatch proves
that no bounded local repair can supply the missing remote interfaces.
"""
from macro_forced_seed import *


def affine_relation(A,variables,forms):
    """Pull a natural-coordinate automatic relation through integer affine maps.
    Negative source coordinates reject. All intermediate carries are retained,
    so no magnitude/encoding-length assumption is made.
    """
    variables=tuple(variables);coeff=tuple(tuple(forms[v][0].get(w,0) for w in variables) for v in A.vs)
    constant=tuple(forms[v][1] for v in A.vs);start=(A.start,constant);states=[start];index={start:0};tr=[];accept=set()
    def tail(q,carry):
        if any(c<0 for c in carry):return False
        while any(carry):
            q=A.tr[q][sum((c%2)<<i for i,c in enumerate(carry))];carry=tuple(c//2 for c in carry)
        return q in A.ac
    for i,(q,carry) in enumerate(states):
        if tail(q,carry):accept.add(i)
        row=[]
        for digit in range(1<<len(variables)):
            values=tuple(carry[h]+sum(coeff[h][j]*((digit>>j)&1) for j in range(len(variables))) for h in range(len(A.vs)))
            d=sum((v%2)<<h for h,v in enumerate(values));new=(A.tr[q][d],tuple(v//2 for v in values))
            if new not in index:index[new]=len(states);states.append(new)
            row.append(index[new])
        tr.append(row)
    return Rel(variables,tr,accept).minimal()


def complete_io(model):
    result,rels,bad,compiled,machines,shift=compile_macro(model,True)
    if bad.witness() is not None:raise ValueError('source family has bad depths')
    out={};(C,Dshift),(Bx,By)=shift
    for signs,(black,white) in rels.items():
        sx,sy=signs;guard=TRUE
        for coord,sign in zip(('x','y'),signs):
            if sign<0:guard=guard&linear({coord:1},1,'>=')
        Q=affine_pullback(machines[model.root],('r','x','y'),
                         ((1,0,0),(C,sx,0),(Dshift,0,sy)),(0,Bx,By))&guard
        out[signs]=dict(input=black,output=black.both(Q,lambda a,b:a!=b),read=black|white)
    return out


def compare(source,target,offset_sign):
    mismatch=FALSE
    forms={'r':({'r':1,'c':offset_sign},0),'x':({'x':1},0),'y':({'y':1},0)}
    vs=('r','x','y','c')
    for signs in source:
        outgoing=source[signs]['output']
        incoming=affine_relation(target[signs]['input'],vs,forms)
        footprint=affine_relation(target[signs]['read'],vs,forms)
        mismatch=mismatch|(outgoing.both(incoming,lambda a,b:a!=b)&footprint)
    # Spatial boundedness of the mismatch union over ALL r, for one constant c.
    # Omitting finitely many small r cannot change boundedness: each fiber is
    # finite. This therefore also allows an arbitrary finite initial exception.
    bound=linear({'m':1,'x':-1},0,'>=')&linear({'m':1,'y':-1},0,'>=')
    repaired=mismatch.implies(bound).forall('r','x','y').exists('m')
    witness=repaired.witness()
    return dict(offset_sign=offset_sign,mismatch_states=len(mismatch.tr),
                bounded_repair_parameter_states=len(repaired.tr),any_constant_parameter_offset_with_bounded_repair=witness is not None,
                witness=witness),mismatch,repaired


def compare_arbitrary_depths(source,target):
    """Every source depth r, every independent target depth s>=1.
    A mismatch is always in the explicit far three-cell candidate set.
    """
    outgoing=source[1,1]['output'];forms={'r':({'s':1},0),'x':({'x':1},0),'y':({'y':1},0)}
    vs=('r','s','x','y')
    incoming=affine_relation(target[1,1]['input'],vs,forms)
    footprint=affine_relation(target[1,1]['read'],vs,forms)
    mismatch=outgoing.both(incoming,lambda a,b:a!=b)&footprint
    # Candidate cells (2s,0),(2s,1),(2s+1,0) are all remote as s grows.
    at_far=linear({'x':1,'s':-2},0)&(linear({'y':1},0)|linear({'y':1},1))
    at_far=at_far|(linear({'x':1,'s':-2},1)&linear({'y':1},0))
    witnesses=(mismatch&at_far).exists('x','y')
    missing=~witnesses&linear({'s':1},1,'>=')
    assert missing.witness() is None
    return dict(mismatch_states=len(mismatch.tr),far_witness_relation_states=len(witnesses.tr),
                all_source_r_and_target_s_at_least_one_have_far_mismatch=True)


def main():
    start=time.monotonic();families={'G':complete_io(capped_rod('LLLR')),'H':complete_io(capped_rod('LRRRRLLR'))};records=[];arbitrary=[]
    for a,b in itertools.product(families,repeat=2):
        for sign in (-1,1):
            print('BEGIN',a,b,sign,flush=True);result,mismatch,good=compare(families[a],families[b],sign)
            assert not result['any_constant_parameter_offset_with_bounded_repair']
            result.update(source=a,target=b);records.append(result);print('RESULT',json.dumps(result),flush=True)
        result=compare_arbitrary_depths(families[a],families[b]);result.update(source=a,target=b);arbitrary.append(result)
        print('ARBITRARY',json.dumps(result),flush=True)
    out=dict(records=records,arbitrary_depth_checks=arbitrary,seconds=time.monotonic()-start,
        scope='Every G/H output at any source r>=0 mismatches every G/H target s>=1 on its required read set, at a listed cell x>=2s. Thus no direct renewal by any parameter update, even allowing repairs in one fixed finite controller as target s grows. Exact same physical pose, minimal prepared input families. Not a ban on other phases, moving controllers, new remote work, or arbitrary ambient backgrounds.')
    (HERE/'renewal_interfaces.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',out['seconds'],flush=True)
if __name__=='__main__':main()
