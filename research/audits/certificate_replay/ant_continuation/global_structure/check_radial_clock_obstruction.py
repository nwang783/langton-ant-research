"""Exact implementation audit of an endpoint-only obstruction, not a path search."""
from fractions import Fraction as Q
import json
from pathlib import Path

def pow3(k):return Q(3)**k

def radial(B,p,h,zsign,c):
    sig=(1 if (p[0]+p[1])%2==0 else -1)*(1 if h%2==0 else -1)
    if zsign==-1:sig=-sig
    e=(1 if h in (0,1) else -1) if zsign==1 else (1 if h in (1,2) else -1)
    z=lambda q:q[0]+zsign*q[1]-c
    f=lambda s:pow3(abs(s))-1
    return -sig*sum((1 if (x+y)%2==0 else -1)*f(z((x,y))) for x,y in B)+Q(1 if e*z(p)>=0 else -3,2)*f(z(p))

def formula(n,c,sign):
    a=pow3(2*n);U=pow3(-c)
    if sign==1:
        if c<=-2*n:return (3*a*a-a-Q(3,2)/a-Q(1,2))*U+2
        if c<=0:return (3*a*a-a-Q(1,2))*U+a/(2*U)
        if c<=2*n:return (3*a*a-a)*U+(a/2+Q(3,2))/U-2
        if c<=4*n+1:return 3*a*a*U+(a/2+Q(3,2)-1/a)/U-2
        return (1/(3*a*a)-1/a+a/2+Q(3,2))/U-2
    H=6*n+2;A=pow3(H)
    if c<=-2*n:return (A/2-Q(3,2)+1/a)*U-2
    if c<=0:return a/U+(A/2-Q(3,2))*U-2
    if c<=1:return (a-Q(1,2))/U+(A/2-3)*U
    if c<=H:return (a-Q(5,6))/U+A*U/2
    return (a-Q(5,6)-Q(3,2)/A)/U+2

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def main():
    cases=0;previous=None
    for n in range(1,13):
        B={(0,2*n),(2*n+1,2*n)};p=(2*n+1,-4*n-1)
        # Corrected rows empty; corrected columns {0}, heading-mass invariant.
        rows=set();cols=set()
        for x,y in B:rows.symmetric_difference_update({y});cols.symmetric_difference_update({x})
        cols.symmetric_difference_update({p[0]})
        assert rows==set() and cols=={0} and (2-len(B))%4==0
        # Counterclockwise hull: origin, lower-right head, upper-right, upper-left.
        hull=[(0,0),p,(2*n+1,2*n),(0,2*n)]
        if previous:
            for q in previous:
                assert all(cross(hull[i],hull[(i+1)%4],q)>=0 for i in range(4))
        previous=hull
        for c in range(-12*n-6,12*n+7):
            for sign in (-1,1):
                direct=radial(B,p,2,sign,c)-radial(set(),(0,0),0,sign,c)
                assert direct==formula(n,c,sign)
                assert direct>=pow3(2*n)
                cases+=1
    out={'exact_formula_cases':cases,'n_range':[1,12],'clock_budget_lower_bound':'3^(2n)',
         'status':'analytic endpoint obstruction; reachability not asserted'}
    Path(__file__).with_name('radial_clock_obstruction_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
