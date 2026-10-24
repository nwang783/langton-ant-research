#!/usr/bin/env python3
"""Search and exactly certify a nonnegative 3x3 energy plus port rank.

For each history-conditioned transition e=(s,t,c), impose
    E(after)-E(before)+phi(t)-phi(s) <= -1
for all unknown outside bits in context c. Counterexample generation uses
the complete finite variable-elimination oracle, not random testing.
"""
from pathlib import Path
import json
import gzip
import sys
import time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

BASE=Path(__file__).resolve().parent
OTHER=BASE.parent/'factor_language'
sys.path.insert(0,str(OTHER))
from exact_local_energy import ContextProblem,SectorContextProblem,CANON,SECTOR_CANON


def energy_row(problem,outside,indices,sector=False):
    before=problem.initial|set(map(tuple,outside))
    after=before^problem.toggled
    row={}
    for x,y in problem.origins:
        p=sum(((x+dx,y+dy) in before)<<(dx+3*dy) for dy in range(3) for dx in range(3))
        q=sum(((x+dx,y+dy) in after)<<(dx+3*dy) for dy in range(3) for dx in range(3))
        phase=((x+y)&1)<<9
        cp=SECTOR_CANON[phase|p] if sector else CANON[p]
        cq=SECTOR_CANON[phase|q] if sector else CANON[q]
        if cp:
            i=indices[cp];row[i]=row.get(i,0)-1
        if cq:
            i=indices[cq];row[i]=row.get(i,0)+1
    return {i:v for i,v in row.items() if v}


def load_records(path):
    raw=json.loads(path.read_text())
    if 'constraints' in raw:return raw['constraints']
    return json.loads(gzip.decompress((BASE/raw['constraints_file']).read_bytes()))


def main(max_rounds=100,mode='all',sector=False):
    assert mode in ('all','fold')
    prefix='conditioned_rank' if mode=='all' else 'conditioned_fold_rank'
    if sector:prefix='sector_'+prefix
    data=json.loads((OTHER/'conditioned_macro_contexts.json').read_text())
    problem_class=SectorContextProblem if sector else ContextProblem
    problems=[problem_class(c) for c in data['contexts']]
    classes=sorted(set(SECTOR_CANON if sector else CANON)-{0});indices={c:i for i,c in enumerate(classes)}
    nw=len(classes);npot=len(data['ports']);nv=nw+npot
    edges=data['edges'];rows=[];seen=set();record=[]
    costs=[int(mode=='all' or e['macro'] in 'CQB') for e in edges]
    def add(edge_id,outside):
        e=edges[edge_id];key=(edge_id,tuple(map(tuple,sorted(outside))))
        if key in seen:return False
        seen.add(key)
        row=energy_row(problems[e['context']],outside,indices,sector)
        row[nw+e['target']]=row.get(nw+e['target'],0)+1
        row[nw+e['source']]=row.get(nw+e['source'],0)-1
        row={i:v for i,v in row.items() if v}
        rows.append(row);record.append({'edge':edge_id,'outside_black':sorted(outside)})
        return True
    for eid in range(len(edges)):add(eid,[])
    if (mode=='fold' or sector) and (BASE/'conditioned_rank_result.json').exists():
        for r in load_records(BASE/'conditioned_rank_result.json'):add(r['edge'],r['outside_black'])
    if mode=='fold' and sector and (BASE/'sector_conditioned_rank_result.json').exists():
        for r in load_records(BASE/'sector_conditioned_rank_result.json'):add(r['edge'],r['outside_black'])
    bounds=[(0,None)]*nw+[(None,None)]*npot
    bounds[nw]=(0,0)
    objective=np.r_[np.ones(nw),np.zeros(npot)]
    started=time.monotonic();output={'status':'unfinished','mode':mode,'sector_dependent':sector,'iterations':[]}
    for iteration in range(max_rounds):
        rr=[];cc=[];vv=[]
        for j,row in enumerate(rows):
            for i,v in row.items():rr.append(j);cc.append(i);vv.append(v)
        matrix=coo_matrix((vv,(rr,cc)),shape=(len(rows),nv)).tocsr()
        rhs=-np.array([costs[r['edge']] for r in record],dtype=float)
        result=linprog(objective,A_ub=matrix,b_ub=rhs,bounds=bounds,method='highs')
        if not result.success:
            output['status']='LP infeasible on explicit contexts'
            output['message']=result.message
            print('INFEASIBLE',iteration,len(rows),result.message,flush=True)
            break
        weights={c:float(w) for c,w in zip(classes,result.x[:nw])}
        phi=result.x[nw:]
        worst=[p.maximize(weights) for p in problems]
        added=0;maximum=-float('inf');violations=0
        for eid,e in enumerate(edges):
            r=worst[e['context']]
            lhs=r['maximum_energy_change']+phi[e['target']]-phi[e['source']]
            maximum=max(maximum,lhs+costs[eid])
            if lhs>-costs[eid]+1e-7:
                violations+=1;added+=add(eid,r['outside_black'])
        rec={'iteration':iteration,'cuts':len(rows),'weight_sum':float(result.fun),
             'potential_range':float(np.max(phi)-np.min(phi)),
             'maximum_excess':float(maximum),'violations':violations,'added':added,
             'seconds':round(time.monotonic()-started,2)}
        print(rec,flush=True);output['iterations'].append(rec)
        output['energy']={str(c):w for c,w in weights.items() if w>1e-10}
        output['potential']=list(map(float,phi))
        if added==0:
            assert violations==0,'Repeated violated floating cut'
            output['status']='floating certificate; checking rounded integer certificate'
            for scale in [100,1000,10000,100000,1000000]:
                iw={c:int(round(w*scale)) for c,w in weights.items() if w>1e-10}
                ip=[int(round(p*scale)) for p in phi]
                exact=[p.maximize(iw) for p in problems]
                values=[r['maximum_energy_change']+ip[e['target']]-ip[e['source']]
                        for e in edges for r in [exact[e['context']]]]
                upper=max(v+c for v,c in zip(values,costs))
                print('INTEGER',scale,'maximum excess relative unit target',upper,flush=True)
                if upper<=0:
                    output['status']='CERTIFIED integer local energy plus port rank'
                    output['integer_energy']={str(c):w for c,w in iw.items() if w}
                    output['integer_potential']=ip
                    output['integer_maximum_excess']=int(upper)
                    output['integer_scale']=scale
                    output['exact_context_results']=exact
                    break
            break
        (BASE/f'{prefix}_progress.json').write_text(json.dumps(output,indent=2))
    output['constraints_file']=f'{prefix}_cuts.json.gz'
    (BASE/output['constraints_file']).write_bytes(gzip.compress(json.dumps(record,separators=(',',':')).encode()))
    output['source_contexts']='../factor_language/conditioned_macro_contexts.json'
    (BASE/f'{prefix}_result.json').write_text(json.dumps(output,indent=2))


if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 100,sys.argv[2] if len(sys.argv)>2 else 'all',len(sys.argv)>3 and sys.argv[3]=='sector')
