"""Finite premises for the all-horizon fixed-candidate obstruction.

The all-parameter proof is in arbitrary_lookahead_obstruction.md.  The long
controls audit its explicit formulas and do not substitute for that proof.
"""
from pathlib import Path
import json

from verify_maxplus_sft import DATA,DIRS,context_data,rot,value

HERE=Path(__file__).resolve().parent


def trace(word):
    x=y=h=0;first={};last={};points=[]
    for c in word:
        p=x,y;assert last.get(p)!=c
        first.setdefault(p,c);last[p]=c;points.append(p)
        h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
    return first,last,(x,y,h),points


def main():
    witness=json.loads((HERE/'counterfield_lookahead_verification.json').read_text())['examples']['two_successors']
    raw=json.loads((HERE/'last_port_candidate_weights.json').read_text());w=raw['weights']
    graph=json.loads((HERE/'full_history_macro_contexts.json').read_text())
    d=context_data(HERE/'full_history_macro_contexts.json',True)
    base=set(map(tuple,witness['initial_black']))
    assert witness['edge_path']==[3,1882,749] and witness['heading']==3 and witness['start_y']==-3
    assert min(x for x,y in base)==-9
    known=[rot(p,3) for key in ('first_L','first_R') for p in d['edge_3'][key]]
    assert min(x for x,y in known)==-5
    U=d['edge_623']['word'];V=d['edge_3']['word']
    first,last,end,points=trace(U)
    assert end==(0,4,0)
    assert min(x for x,y in points)==-1 and max(x for x,y in points)==2
    assert min(y for x,y in points)==-1 and max(y for x,y in points)==3
    ff,ll,ee,pp=trace(U+U)
    F={(0,0),(-1,0),(-1,-1),(0,1),(-1,2)}
    fresh={p for p,c in ff.items() if c=='L'}-{p for p,c in first.items() if c=='L'}
    assert fresh=={(x,y+4) for x,y in F}
    G={rot(p,3) for p in F}
    assert G=={(0,0),(0,-1),(1,-1),(-1,0),(-2,-1)}
    # The recurrent graph path is exact, including its eventual U self-loop.
    ports=[3,721,282,633,690,749,212,212]
    edges=[3,1882,749,1704,1836,1956,623]
    for i,eid in enumerate(edges):
        e=graph['edges'][eid]
        assert (e['source'],e['target'])==(ports[i],ports[i+1])
        assert e['macro']==('V' if i==0 else 'U')
    controls=[]
    for n in (0,1,2,3,4,10,100):
        extra={(x-11-4*j,y-2) for j in range(n) for x,y in G}
        assert len(extra)==5*n and not extra&base
        initial=base|extra;actual=set(initial);x=0;y=-3;h=3
        before=value(actual,(x,y,h),w,3);after=None
        for j,word in enumerate([V]+[U]*(n+2)):
            for c in word:
                assert ((x,y) in actual)==(c=='L'),(n,j,c,(x,y))
                actual.symmetric_difference_update({(x,y)})
                h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
            if j==0:
                after=value(actual,(x,y,h),w,721)
                def mask(field):
                    return sum(1<<((dy+1)*3+dx+1) for dx in (-1,0,1) for dy in (-1,0,1)
                               if (dx,1+dy) in field)
                assert mask(initial)==390 and mask(actual)==391
        assert before==0 and after==1 and (x,y,h)==(-11-4*n,-2,3)
        controls.append({'extra_U':n,'initial_black_count':len(initial),'steps':len(V)+(n+2)*len(U),
                         'pre_potential':before,'after_V_potential':after,'end_pose':[x,y,h]})
    assert w[390]==-1 and w[391]==0
    report={'status':'Finite premises verified; all-parameter proof in arbitrary_lookahead_obstruction.md',
            'base_initial_black':sorted(base),'base_mass':len(base),'added_cells_per_U':sorted(G),
            'additional_head_positions':'(-11-4j,-2), j=0,...,n-1','edge_path_to_U_loop':edges,
            'port_path_to_U_loop':ports,'mask_change':{'center':[0,1],'before':390,'after':391,
            'before_weight':-1,'after_weight':0,'toggled_cell':[-1,0]},'controls':controls}
    (HERE/'arbitrary_lookahead_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k not in ('base_initial_black','controls')})


if __name__=='__main__':main()
