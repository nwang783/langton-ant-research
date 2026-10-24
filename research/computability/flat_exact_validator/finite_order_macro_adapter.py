"""Verified finite-order powering for arbitrary finite physical macro bases."""
import math
from general_macro_decider import *
from finite_order_adapter import matpower,root_cycle,first_block_conflict


def prepare_macro(bases,images,A,order,root=0,max_powered_reads=None):
    if type(order) is not int or order<1:raise ValueError('positive spatial order required')
    validator=GeneralMacroModel(bases,[[s] for s in range(len(bases))],root)
    if not isinstance(A,(list,tuple)) or len(A)!=2 or any(not isinstance(row,(list,tuple)) or len(row)!=2 or any(type(a) is not int for a in row) for row in A):
        raise ValueError('integer two by two spatial matrix required')
    A=tuple(tuple(row) for row in A)
    if matpower(A,order)!=((1,0),(0,1)):raise ValueError('supplied macro spatial order is not valid')
    if not isinstance(images,(list,tuple)) or len(images)!=len(bases):raise ValueError('one image per base required')
    for s,row in enumerate(images):
        if not isinstance(row,(list,tuple)) or not row or any(type(t) is not int or not 0<=t<len(bases) for t in row):raise ValueError('finite nonempty integer-index macro images required')
        p=(0,0);h=validator.bases[s][0]
        for t in row:
            if validator.bases[t][0]!=h:raise ValueError('scaled macro image boundary-heading mismatch')
            p=add(p,validator.net[t]);h=validator.end[t]
        target=tuple(sum(A[i][j]*validator.net[s][j] for j in range(2)) for i in range(2))
        if p!=target or h!=validator.end[s]:raise ValueError('scaled macro full-pose mismatch')
    q=root_cycle(images,root);power=math.lcm(order,q);current=tuple((s,) for s in range(len(bases)))
    if max_powered_reads is not None and (type(max_powered_reads) is not int or max_powered_reads<1):raise ValueError('positive powered physical-read cap required')
    for r in range(power):
        size=sum(len(bases[t][1]) for row in current for s in row for t in images[s])
        if max_powered_reads is not None and size>max_powered_reads:raise ArithmeticError('explicit powered physical-read cap')
        current=tuple(tuple(t for s in row for t in images[s]) for row in current)
    model=GeneralMacroModel(bases,current,root)
    if model.images[root][0]!=root:raise AssertionError('cofinal macro root not fixed')
    return model,dict(verified_spatial_order=order,first_letter_root_cycle=q,common_power=power,
                      powered_macro_lengths=[len(row) for row in current],
                      powered_physical_lengths=[sum(len(bases[t][1]) for t in row) for row in current])


def solve_macro_finite_order(bases,images,A,order,root=0,max_powered_reads=None,**kwargs):
    try:
        model,certificate=prepare_macro(bases,images,A,order,root,max_powered_reads)
        conflict=first_block_conflict(model)
        if conflict is not None:return dict(status='decided',possible=False,reason='literal powered macro block internally inconsistent',conflict=conflict,adapter=certificate)
        result=solve_macro_generated(model,**kwargs);result['adapter']=certificate;return result
    except Unsupported as error:return dict(status='unsupported macro root convention',possible=None,error=str(error))
    except (ArithmeticError,MemoryError,RecursionError) as error:return dict(status='unknown: macro adapter resources',possible=None,error=str(error))


def main():
    A=((-1,0),(0,-1));records=[]
    cases=[('zero_displacement_multiread',[(1,'LLLRRRRL')],[[0]],True),
           ('two_cycle_multiread',[(1,'LLLRRRRL')]*2,[[1],[0]],True),
           ('branching_closed_macro',[(0,'RRRR')],[[0,0]],False)]
    bases=[(s//2,('RLLLLRRRR' if s%2==0 else 'LRRRRLLLL')) for s in range(8)]
    words=['RRRRLRLLL','LRRRLRLLL']*4;images=[word_states(w,s//2) for s,w in enumerate(words)]
    cases.append(('nonzero_multiread_halfturn',bases,images,False))
    for name,bases,images,expected in cases:
        print('BEGIN',name,flush=True);result=solve_macro_finite_order(bases,images,A,2,max_powered_reads=100000)
        assert result['possible']==expected
        if expected:assert result['candidate_seed']==[(-1,1),(0,0),(0,1)] and not result['given_seed_validation']['growing_root']
        result['name']=name;records.append(result);print('RESULT',json.dumps(result),flush=True)
    capped=solve_macro_finite_order(cases[-1][1],cases[-1][2],A,2,max_powered_reads=20)
    assert capped['possible'] is None
    invalid=0
    for matrix,order in [(((True,0),(0,1)),1),(((0,-1),(1,0)),2)]:
        try:prepare_macro([(1,'LLLRRRRL')],[[0]],matrix,order)
        except ValueError:invalid+=1
        else:raise AssertionError('invalid matrix/order accepted')
    out=dict(records=records,invalid_input_rejections=invalid,explicit_size_cap_result=capped,
        scope='Verified finite-order spatial/root-cycle adapter for exact-pose finite physical macro presentations, using the general A=I macro solver. Selected cofinal power-limits only; no singular finite-power or changing heading boundaries; no accepted growing model.')
    (HERE/'finite_order_macro_adapter.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
