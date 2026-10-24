"""Check the finite geometric premises of isolated_event_spiral.md.

The note contains the all-parameter rectangle separation proof. Longer finite
controls below audit formulas and exact fuel accounting, not replace that proof.
"""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[2]
PRIOR=ROOT/'ant_continuation/factor_language'
sys.path.insert(0,str(PRIOR))
from analyze_language import highway_word,cyclic_factors

D=json.loads((PRIOR/'five_macro_footprints.json').read_text())
DIRS=((0,1),(1,0),(0,-1),(-1,0))
M='LLLLRLRRRRLR'

def trace(seq):
    x=y=h=0;last={};firstL=set();points=[];fresh=[]
    for name in seq:
        before=len(firstL)
        for c in D[name]['word']:
            p=x,y;points.append(p)
            assert last.get(p)!=c,(name,p,c)
            if p not in last and c=='L':firstL.add(p)
            last[p]=c;h=(h+(1 if c=='R' else -1))%4
            dx,dy=DIRS[h];x+=dx;y+=dy
        fresh.append(len(firstL)-before)
    box=[min(p[i] for p in points) for i in (0,1)]+[max(p[i] for p in points) for i in (0,1)]
    return {'end':[x,y,h],'box':box,'firstL':len(firstL),'fresh':fresh}

def formulas(i):
    k,r=divmod(i,4);S=16**k
    starts=[(8*S-8,-4*S+4),(8*S-11,16*S+6),(-32*S-13,16*S+3),(-32*S-10,-64*S+1)]
    boxes=[(8*S-11,-4*S+3,8*S-6,16*S+7),(-32*S-14,16*S+3,8*S-10,16*S+8),
           (-32*S-15,-64*S,-32*S-10,16*S+4),(-32*S-11,-64*S-1,128*S-7,-64*S+4)]
    return starts[r],(-i)%4,boxes[r]

def main():
    assert trace('U')['end']==[0,4,0]
    cv=trace('CV');assert cv['end']==[-3,2,3] and cv['box']==[-3,-1,2,3]
    interface=trace('UCVU');assert interface['fresh']==[9,1,1,5]
    F=cyclic_factors(highway_word(),10)
    counts={}
    for k in 'UCV':
        w=D[k]['word'];assert w.startswith(M)
        after=w[len(M):]+M;z=M+after
        hits=[i for i in range(len(z)-len(M)+1) if z[i:i+len(M)]==M]
        assert hits==[0,len(w)]
        bad=[j-len(M) for j in range(len(M),len(z)) if z[j-9:j+1] not in F]
        assert bad==([1] if k=='V' else [])
        counts[k]=bad
    controls=[]
    for K in range(1,11):
        seq=''.join('U'*(5*2**i)+'CV' for i in range(K))
        r=trace(seq);expected=4+25*(2**K-1)+2*K
        assert r['firstL']==expected
        p,h,_=formulas(K);assert r['end']==[*p,h]
        controls.append({'legs':K,'steps':sum(D[k]['length'] for k in seq),'firstL':expected})
    # Exact integer comparisons at representative complete groups; the note
    # gives the symbolic inequalities valid for every S=16^k.
    for i in range(40):
        _,_,b=formulas(i)
        for j in range(i-1):
            _,_,a=formulas(j)
            assert b[2]<a[0] or a[2]<b[0] or b[3]<a[1] or a[3]<b[1]
    out={'local_CV':cv,'local_UCVU':interface,'bad_appended_indices':counts,
         'finite_controls':controls,'status':'Finite premises pass; all-parameter proof is isolated_event_spiral.md.'}
    Path(__file__).with_name('spiral_geometry_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
