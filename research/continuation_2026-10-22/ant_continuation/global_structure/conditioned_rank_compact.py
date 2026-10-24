#!/usr/bin/env python3
"""Equivalent compact LP: one upper-bound variable per local context.

Context cuts are a.w <= z_context; graph inequalities are
z_context+phi(target)-phi(source) <= -cost. This avoids duplicating a local
energy cut for every graph edge carrying that same local context.
"""
from pathlib import Path
import gzip,json,sys,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from conditioned_rank import (BASE,OTHER,ContextProblem,SectorContextProblem,
                              CANON,SECTOR_CANON,energy_row,load_records)
from exact_local_energy import HeadContextProblem


def main(mode='all',sector=True,max_rounds=100,solver='highs',radius=None):
    assert mode in ('all','fold','event')
    data=json.loads((OTHER/'conditioned_macro_contexts.json').read_text())
    pc=SectorContextProblem if sector else ContextProblem
    problems=[pc(c) if radius is None else HeadContextProblem(c,radius,sector) for c in data['contexts']]
    classes=sorted(set(SECTOR_CANON if sector else CANON)-{0})
    indices={c:i for i,c in enumerate(classes)}
    nw=len(classes);npot=len(data['ports']);nz=len(problems)
    sites=[] if radius is None else problems[0].head_sites
    nh=len(sites);po=nw+nh;zo=po+npot;nv=zo+nz
    edges=data['edges'];costs=[int(mode=='all' or e['macro'] in ('CQB' if mode=='fold' else 'VQ')) for e in edges]
    prefix=('sector_' if sector else '')+'compact_'+mode
    if radius is not None:prefix=f'head{radius}_'+prefix
    cuts=[];record=[];seen=set()
    def add(cid,outside):
        key=cid,tuple(map(tuple,sorted(outside)))
        if key in seen:return False
        seen.add(key)
        row=energy_row(problems[cid],outside,indices,sector)
        if radius is not None:
            hr=problems[cid].head_row(outside)
            row.update({nw+j:hr[p] for j,p in enumerate(sites) if hr[p]})
        row[zo+cid]=-1
        cuts.append(row);record.append({'context':cid,'outside_black':sorted(outside)})
        return True
    for cid in range(nz):add(cid,[])
    old=BASE/'conditioned_rank_result.json'
    if old.exists():
        for r in load_records(old):add(edges[r['edge']]['context'],r['outside_black'])
    if mode!='all' and sector and (BASE/'sector_compact_all_cuts.json.gz').exists():
        for r in json.loads(gzip.decompress((BASE/'sector_compact_all_cuts.json.gz').read_bytes())):
            add(r['context'],r['outside_black'])
    if (BASE/f'{prefix}_cuts.json.gz').exists():
        for r in json.loads(gzip.decompress((BASE/f'{prefix}_cuts.json.gz').read_bytes())):
            add(r['context'],r['outside_black'])
    if radius is not None and (BASE/'sector_compact_event_cuts.json.gz').exists():
        for r in json.loads(gzip.decompress((BASE/'sector_compact_event_cuts.json.gz').read_bytes())):
            add(r['context'],r['outside_black'])
    edge_rows=[]
    for e in edges:
        row={zo+e['context']:1}
        row[po+e['target']]=row.get(po+e['target'],0)+1
        row[po+e['source']]=row.get(po+e['source'],0)-1
        edge_rows.append({k:v for k,v in row.items() if v})
    bounds=[(0,None)]*nw+[(None,None)]*(nh+npot+nz);bounds[po]=(0,0)
    objective=np.r_[np.ones(nw),np.zeros(nh+npot+nz)]
    out={'status':'unfinished','mode':mode,'sector_dependent':sector,'solver':solver,
         'head_radius':radius,'head_sites':sites,'iterations':[]}
    start=time.monotonic()
    for it in range(max_rounds):
        rr=[];cc=[];vv=[]
        allrows=edge_rows+cuts
        for j,row in enumerate(allrows):
            for i,v in row.items():rr.append(j);cc.append(i);vv.append(v)
        a=coo_matrix((vv,(rr,cc)),shape=(len(allrows),nv)).tocsr()
        rhs=np.r_[-np.array(costs,dtype=float),np.zeros(len(cuts))]
        res=linprog(objective,A_ub=a,b_ub=rhs,bounds=bounds,method=solver,options={'time_limit':30})
        if not res.success:
            out['status']=('numerical LP infeasibility on explicit contexts' if res.status==2
                           else 'LP stopped without a feasibility decision')
            out['solver_status']=int(res.status)
            out['message']=res.message
            print('STOPPED',it,'context cuts',len(cuts),res.message,flush=True);break
        weights={c:float(w) for c,w in zip(classes,res.x[:nw])}
        head={p:float(a) for p,a in zip(sites,res.x[nw:po])}
        phi=res.x[po:zo]
        worst=[p.maximize(weights) if radius is None else p.maximize(weights,head) for p in problems]
        maximum=-float('inf');badcontexts=set();violations=0
        for eid,e in enumerate(edges):
            excess=worst[e['context']]['maximum_energy_change']+phi[e['target']]-phi[e['source']]+costs[eid]
            maximum=max(maximum,excess)
            if excess>1e-7:
                violations+=1;badcontexts.add(e['context'])
        added=sum(add(c,worst[c]['outside_black']) for c in sorted(badcontexts))
        rec={'iteration':it,'context_cuts':len(cuts),'weight_sum':float(res.fun),
             'maximum_excess':float(maximum),'violating_edges':violations,
             'added':added,'seconds':round(time.monotonic()-start,2)}
        print(rec,flush=True);out['iterations'].append(rec)
        out['energy']={str(c):w for c,w in weights.items() if w>1e-10}
        out['head_weights']=[head[p] for p in sites]
        out['potential']=list(map(float,phi))
        if not added:
            assert not violations,'Duplicate violated floating cut'
            out['status']='floating feasible certificate; rounding check pending'
            for scale in [100,1000,10000,100000,1000000]:
                iw={c:int(round(w*scale)) for c,w in weights.items()}
                ih={p:int(round(a*scale)) for p,a in head.items()}
                ip=[int(round(p*scale)) for p in phi]
                exact=[p.maximize(iw) if radius is None else p.maximize(iw,ih) for p in problems]
                excess=max(exact[e['context']]['maximum_energy_change']+ip[e['target']]-ip[e['source']]+cost
                           for e,cost in zip(edges,costs))
                print('INTEGER',scale,'excess',excess,flush=True)
                if excess<=0:
                    out['status']='CERTIFIED integer local energy plus port rank'
                    out['integer_energy']={str(c):w for c,w in iw.items() if w}
                    out['integer_potential']=ip;out['integer_scale']=scale
                    out['integer_head_weights']=[ih[p] for p in sites]
                    out['integer_maximum_excess']=int(excess);out['exact_context_results']=exact
                    break
            break
        (BASE/f'{prefix}_progress.json').write_text(json.dumps(out,indent=2))
    out['constraints_file']=f'{prefix}_cuts.json.gz'
    (BASE/out['constraints_file']).write_bytes(gzip.compress(json.dumps(record,separators=(',',':')).encode()))
    (BASE/f'{prefix}_result.json').write_text(json.dumps(out,indent=2))


if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else 'all',
         len(sys.argv)<=2 or sys.argv[2]=='sector',
         int(sys.argv[3]) if len(sys.argv)>3 else 100,
         sys.argv[4] if len(sys.argv)>4 else 'highs',
         int(sys.argv[5]) if len(sys.argv)>5 else None)
