"""Verified finite-order spatial adapter to the generated additive-I decider.

Strict exact-heading unit-read presentations only. The common spatial-order /
first-letter-root-cycle power is composed literally and revalidated at I.
The selected original root power-limit is unchanged by this cofinal power.
"""
import math
from generated_cover_decider import *


def matmul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def matpower(A,n):
    out=((1,0),(0,1))
    while n:
        if n%2:out=matmul(out,A)
        A=matmul(A,A);n//=2
    return out


def scaled_images(physical,images,A,root):
    # Reuse the signed strict input validator with identity images first;
    # then validate every supplied scaled physical word before composition.
    validator=Model(physical,[[s] for s in range(len(physical))],root)
    if not isinstance(A,(list,tuple)) or len(A)!=2 or any(not isinstance(row,(list,tuple)) or len(row)!=2 or any(type(a) is not int for a in row) for row in A):
        raise ValueError('two by two integer spatial matrix required')
    A=tuple(tuple(row) for row in A)
    if not isinstance(images,(list,tuple)) or len(images)!=len(physical):raise ValueError('one finite image per state required')
    for s,word in enumerate(images):
        if not isinstance(word,(list,tuple)) or not word or any(type(t) is not int or not 0<=t<len(physical) for t in word):
            raise ValueError('nonempty finite integer-index images required')
        h,turn=validator.physical[s];p=(0,0)
        for t in word:
            if validator.physical[t][0]!=h:raise ValueError('scaled image heading mismatch')
            h=(h+validator.physical[t][1])%4;p=add(p,D[h])
        out=(validator.physical[s][0]+turn)%4;v=D[out];target=tuple(sum(A[i][j]*v[j] for j in range(2)) for i in range(2))
        if h!=out or p!=target:raise ValueError('scaled image does not preserve the exact supplied full pose')
    return validator.physical,tuple(tuple(w) for w in images),A


def root_cycle(images,root):
    path=[];seen={};s=root
    while s not in seen:seen[s]=len(path);path.append(s);s=images[s][0]
    if s!=root:raise Unsupported('root is not on a first-letter cycle; supply the actual power-limit root')
    return len(path)


def prepare(physical,images,A,order,root=0,max_powered_reads=None):
    if type(order) is not int or order<1:raise ValueError('positive verified spatial order required')
    physical,images,A=scaled_images(physical,images,A,root)
    if matpower(A,order)!=((1,0),(0,1)):raise ValueError('supplied order does not make the spatial matrix identity')
    q=root_cycle(images,root);power=math.lcm(order,q);current=tuple((s,) for s in range(len(physical)))
    if max_powered_reads is not None and (type(max_powered_reads) is not int or max_powered_reads<1):raise ValueError('positive powered-size cap required')
    for r in range(power):
        next_lengths=[sum(len(images[t]) for t in row) for row in current]
        if max_powered_reads is not None and sum(next_lengths)>max_powered_reads:raise ArithmeticError('explicit powered-image size cap')
        current=tuple(tuple(t for s in row for t in images[s]) for row in current)
    model=GeneralUnitModel(physical,current,root)
    if model.images[root][0]!=root:raise AssertionError('common root power not prolongable')
    return model,dict(verified_spatial_order=order,first_letter_root_cycle=q,common_power=power,
                      powered_image_lengths=[len(row) for row in current])


def first_block_conflict(model):
    requirements={};previous=set()
    for i,(p,turn,s) in enumerate(model.literal(1)):
        initial=turn^int(p in previous)
        if p in requirements and requirements[p][0]!=initial:
            return dict(cell=p,first_read=requirements[p][1],conflicting_read=i,required_initial_bits=[requirements[p][0],initial])
        requirements[p]=(initial,i);previous.symmetric_difference_update({p})
    return None


def solve_finite_order(physical,images,A,order,root=0,max_powered_reads=None,**kwargs):
    try:
        model,certificate=prepare(physical,images,A,order,root,max_powered_reads)
        conflict=first_block_conflict(model)
        if conflict is not None:return dict(status='decided',possible=False,reason='literal powered block internally inconsistent',conflict=conflict,adapter=certificate)
        result=solve_generated(model,**kwargs);result['adapter']=certificate;return result
    except Unsupported as error:return dict(status='unsupported root convention',possible=None,error=str(error))
    except (ArithmeticError,MemoryError,RecursionError) as error:return dict(status='unknown: adapter resources',possible=None,error=str(error))


def main():
    records=[]
    controls=[('halfturn',((-1,0),(0,-1)),2,['RRRRLRLLL','LRRRLRLLL']*4),
              ('quarterturn',((0,-1),(1,0)),4,['RRRRLRR','LRRRLRR']*4),
              ('nonorthogonal_order2',((1,2),(0,-1)),2,['R','L','RRRRLLRLL','LRRRLLRLL','R','L','RRRRLLRLL','LRRRLLRLL'])]
    for name,A,order,words in controls:
        print('BEGIN',name,flush=True);images=[word_states(w,s//2) for s,w in enumerate(words)]
        result=solve_finite_order(standard_physical(),images,A,order,max_powered_reads=100000)
        if name=='nonorthogonal_order2':assert result['possible'] and not result['given_seed_validation']['growing_root']
        else:assert result['possible'] is False
        result['name']=name;records.append(result);print('RESULT',json.dumps(result),flush=True)
    # Actual root first-letter cycle of length2, identity spatial geometry.
    model=GeneralUnitModel([(0,1)]*2,[[1],[0]],0)
    result=solve_finite_order(model.physical,model.images,((1,0),(0,1)),1)
    assert result['possible'] and result['adapter']['common_power']==2
    result['name']='two_state_root_cycle';records.append(result)
    # Invalid order and invalid geometric transmission must not become NO.
    errors=0
    quarter_images=[word_states(w,s//2) for s,w in enumerate(controls[1][3])]
    for A,order,images in [(((0,-1),(1,0)),2,quarter_images),(((True,0),(0,1)),1,[[s] for s in range(8)]),
                           (((-1,0),(0,-1)),2,[[s] for s in range(8)])]:
        try:prepare(standard_physical(),images,A,order)
        except ValueError:errors+=1
        else:raise AssertionError('bad adapter input accepted')
    transient=solve_finite_order([(0,1)]*2,[[1],[1]],((1,0),(0,1)),1)
    assert transient['possible'] is None and transient['status']=='unsupported root convention'
    capped=solve_finite_order(standard_physical(),quarter_images,((0,-1),(1,0)),4,max_powered_reads=100)
    assert capped['possible'] is None and capped['status']=='unknown: adapter resources'
    out=dict(records=records,strict_invalid_input_rejections=errors,
        transient_root_result=transient,explicit_size_cap_result=capped,
        scope='Verified finite-order spatial/root-cycle powering adapter for exact heading-compatible unit presentations. Calls the generated A=I solver. No singular finite-power matrices, nonperiodic boundary headings, macro bases or accepted growing models.')
    (HERE/'finite_order_adapter.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
