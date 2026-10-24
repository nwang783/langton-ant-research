"""Exact ISL integer-set -> binary automatic relation conversion.

Local existential integers are lifted to explicit dimensions using the public
ISL API, then represented as differences of two naturals and projected by
ordinary existential quantification. No printed-formula parser is trusted.
Official API semantics: https://libisl.sourceforge.io/user.html (Lifting).
"""
import ctypes as C, pathlib,sys,itertools,json,time
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from presburger_read_set_solver import Context,relation
from isl_exact import _bind,_P,_libc
from flat_forced_seed import Rel,linear,TRUE,FALSE

_CB=C.CFUNCTYPE(C.c_int,_P,_P)
_foreach_basic=_bind('isl_set_foreach_basic_set',[_P,_CB,_P],C.c_int)
_setdim=_bind('isl_set_dim',[_P,C.c_int],C.c_int)
_lift=_bind('isl_basic_set_lift',[_P])
_flatten=_bind('isl_basic_set_flatten',[_P])
_dim=_bind('isl_basic_set_dim',[_P,C.c_int],C.c_int)
_free_basic=_bind('isl_basic_set_free',[_P])
_foreach_constraint=_bind('isl_basic_set_foreach_constraint',[_P,_CB,_P],C.c_int)
_const=_bind('isl_constraint_get_constant_val',[_P])
_coefficient=_bind('isl_constraint_get_coefficient_val',[_P,C.c_int,C.c_int])
_equality=_bind('isl_constraint_is_equality',[_P],C.c_int)
_free_constraint=_bind('isl_constraint_free',[_P])
_valstr=_bind('isl_val_to_str',[_P])
_valfree=_bind('isl_val_free',[_P])


def integer_value(ptr):
    if not ptr:raise ArithmeticError('ISL returned no coefficient')
    text=_valstr(ptr)
    try:
        if not text:raise ArithmeticError('ISL coefficient has no string')
        result=C.string_at(text).decode();return int(result)
    finally:
        if text:_libc.free(text)
        _valfree(ptr)


def convert(obj,variables,signs=None):
    """Visible original dimensions are sign_i * natural variable_i.
    Parameters are not silently interpreted; this entry point requires zero.
    """
    if obj.kind!='set':raise ValueError('ISL set required')
    variables=tuple(variables);signs=(1,)*len(variables) if signs is None else tuple(signs)
    if len(set(variables))!=len(variables) or any(not isinstance(v,str) or not v for v in variables):
        raise ValueError('distinct nonempty variable names required')
    if len(signs)!=len(variables) or any(type(s) is not int or s not in (-1,1) for s in signs):raise ValueError('sign vector mismatch')
    if _setdim(obj.ptr,1)!=0 or _setdim(obj.ptr,3)!=len(variables):raise ValueError('ISL visible dimension/parameter mismatch')
    union=FALSE;errors=[];stats=dict(basic_sets=0,constraints=0,lifted_integer_dimensions=0)
    @_CB
    def basic(ptr,user):
        nonlocal union
        lifted=None
        try:
            if _dim(ptr,1)!=0 or _dim(ptr,3)!=len(variables):raise ValueError('ISL visible dimension/parameter mismatch')
            lifted=_lift(ptr);ptr=None
            if not lifted:obj.ctx.fail()
            lifted=_flatten(lifted)
            if not lifted:obj.ctx.fail()
            if _dim(lifted,4)!=0:raise ArithmeticError('ISL lifting left local existential dimensions')
            n=_dim(lifted,3);extra=n-len(variables)
            if extra<0:raise ArithmeticError('lifting removed visible dimensions')
            hidden=tuple(v for j in range(extra) for v in (f'_h{j}p',f'_h{j}m'))
            if set(hidden)&set(variables):raise ValueError('reserved hidden variable collision')
            current=TRUE;stats['basic_sets']+=1;stats['lifted_integer_dimensions']+=extra
            @_CB
            def constraint(con,user):
                nonlocal current
                try:
                    const=integer_value(_const(con));coeff={}
                    for j,v in enumerate(variables):coeff[v]=signs[j]*integer_value(_coefficient(con,3,j))
                    for j in range(extra):
                        a=integer_value(_coefficient(con,3,len(variables)+j));coeff[f'_h{j}p']=a;coeff[f'_h{j}m']=-a
                    eq=_equality(con)
                    if eq<0:obj.ctx.fail()
                    current=current&linear(coeff,-const,'=' if eq else '>=');stats['constraints']+=1
                    return 0
                except BaseException as exc:errors.append(exc);return -1
                finally:_free_constraint(con)
            status=_foreach_constraint(lifted,constraint,None)
            if errors:raise errors[0]
            if status<0:obj.ctx.fail()
            current=current.exists(*hidden);union=union|current
            return 0
        except BaseException as exc:errors.append(exc);return -1
        finally:
            if lifted:_free_basic(lifted)
            elif ptr:_free_basic(ptr)
    result=_foreach_basic(obj.ptr,basic,None)
    if errors:raise errors[0]
    if result<0:obj.ctx.fail()
    return union.lift(variables),stats


def main():
    ctx=Context(max_operations=30000000);records=[];start=time.monotonic()
    for name,formula in [
        ('two_signed_rays','{ [r,x,y] : r>=0 and (x=2*r or x=-2*r) and y=0 }'),
        ('modulo_and_floor','{ [r,x,y] : r>=0 and (x+r)%3=0 and y=floor((2*x-r)/3) }'),
        ('integer_witnesses','{ [r,x,y] : exists (a,b : x=2*a+3*b and y=a-b and r>=a and r>=0) }'),
        ('two_local_divs','{ [r,x,y] : r>=0 and y=floor((2*x-r)/3)+floor((x+r)/5) }')]:
        obj=ctx.set(formula);checks=0;states=[];stats=[]
        for sx,sy in itertools.product((-1,1),repeat=2):
            A,st=convert(obj,('r','x','y'),(1,sx,sy));states.append(len(A.tr));stats.append(st)
            for r,x,y in itertools.product(range(9),range(10),range(10)):
                point=ctx.set(f'{{ [r,x,y] : r={r} and x={sx*x} and y={sy*y} }}')
                expected=not obj.intersect(point).is_empty();assert A.eval(r=r,x=x,y=y)==expected,(name,sx,sy,r,x,y)
                checks+=1
        records.append(dict(name=name,automaton_states=states,conversion=stats,exact_ISL_point_checks=checks))
    out=dict(records=records,seconds=time.monotonic()-start,scope='Exact ISL basic-set lifting and automatic conversion controls, including signed visible and signed existential integer dimensions. No ant trajectory claim.')
    (HERE/'isl_automatic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
