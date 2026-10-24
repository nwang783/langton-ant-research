"""Check finite premises of the all-parameter double-C fold proof."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'ant_continuation/factor_language/five_macro_footprints.json').read_text())
DIR=((0,1),(1,0),(0,-1),(-1,0));F=D['C']['word']*2;V=D['V']['word'];M='LLLLRLRRRRLR'

def trace(w,require=True):
    x=y=h=0;visits={};firstL=[];conflict=None
    for t,c in enumerate(w):
        p=x,y;old=visits.get(p,[])
        if old and old[-1][1]==c and conflict is None:conflict=[list(p),old[-1][0],t,c]
        if require:assert conflict is None,(t,p,c)
        if not old and c=='L':firstL.append(p)
        visits.setdefault(p,[]).append((t,c))
        h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
    return visits,(x,y,h),firstL,conflict

def main():
    fv,fe,_,_=trace(F);vv,ve,_,_=trace(V)
    assert fe==(-1,1,2) and ve==(1,3,0)
    assert fv[2,1]==[(7,'R')] and fv[0,-1]==[(3,'L')] and fv[0,3]==[(23,'R')]
    assert (-2,-1) not in fv and (-1,2) not in vv
    assert {(x,y):z for (x,y),z in vv.items() if y==3*x+1}=={(0,1):[(11,'R')]}
    assert vv[1,2]==[(13,'L'),(17,'R')]
    assert F[:12]==V[:12]==M
    cases=[]
    for n in range(31):
        for m in range(31):
            w=F+V*n+F+V*m+F
            v,_,_,_=trace(w,False)
            if n==0:q,a,b,c=(2,1),7,67,'R'
            elif m>=n:q,a,b,c=(0,-1),3,36*n+55,'L'
            else:r=n-m;q,a,b,c=(-r,3-3*r),18*r+23,60+18*(n+m)+23,'R'
            assert [(t,l) for t,l in v[q] if a<=t<=b]==[(a,c),(b,c)]
            cases.append([n,m])
    mixed=F+V*4+D['U']['word']*2+F+V*3+F+M
    _,end,seed,_=trace(mixed)
    out={'finite_premises_pass':True,'controls':len(cases),'control_parameter_range':[0,30],
         'mixed_rail_counterexample':{'word':'CC V^4 U^2 CC V^3 CC M','length':len(mixed),
                                      'end_pose':end,'initial_black':sorted(seed),'mass':len(seed)},
         'status':'All-parameter proof is double_c_fold_lemma.md; controls are supplementary.'}
    Path(__file__).with_name('double_c_fold_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
