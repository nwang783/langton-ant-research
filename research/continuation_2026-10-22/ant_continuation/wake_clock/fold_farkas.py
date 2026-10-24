"""Exact Farkas audit of the ordinary nonnegative 3x3 fold-only rank ansatz.

Uses only the existing 34,941 explicit cuts; it does not generate new ant
trajectories or outside contexts. Floating LP chooses a support. The final
integer certificate is independently checked with integer arithmetic.
"""
from pathlib import Path
import sys,gzip,json,hashlib,math
from fractions import Fraction as Q
from functools import reduce
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,vstack

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'global_structure'))
from conditioned_rank import ContextProblem,CANON,energy_row

def exact_linear_solve(equations,targets):
    """Fraction-free Gaussian elimination, followed by rational backsolve."""
    original=[list(map(int,r))+[int(b)] for r,b in zip(equations,targets)]
    M=[r[:] for r in original]
    nr=len(M);nc=len(M[0])-1;rank=0;previous=1;pivots=[]
    for col in range(nc):
        candidates=[i for i in range(rank,nr) if M[i][col]]
        if not candidates:continue
        pivotrow=min(candidates,key=lambda i:abs(M[i][col]))
        M[rank],M[pivotrow]=M[pivotrow],M[rank]
        pivot=M[rank][col]
        for i in range(rank+1,nr):
            v=M[i][col]
            for k in range(col+1,nc+1):
                numerator=pivot*M[i][k]-v*M[rank][k]
                assert numerator%previous==0
                M[i][k]=numerator//previous
            M[i][col]=0
        pivots.append(col);rank+=1;previous=pivot
        if rank==nr:break
    assert rank==nc,('nonunique exact support',rank,nc)
    assert all(not any(r[:nc]) and r[nc]==0 for r in M[rank:])
    x=[Q(0)]*nc
    for i in range(rank-1,-1,-1):
        col=pivots[i]
        x[col]=(Q(M[i][nc])-sum(M[i][j]*x[j] for j in range(col+1,nc)))/M[i][col]
    assert all(sum(a*v for a,v in zip(r[:nc],x))==r[nc] for r in original)
    return x

def main():
    context_path=ROOT/'factor_language/conditioned_macro_contexts.json'
    cuts_path=ROOT/'global_structure/conditioned_rank_cuts.json.gz'
    data=json.loads(context_path.read_text())
    records=json.loads(gzip.decompress(cuts_path.read_bytes()))
    classes=sorted(set(CANON)-{0});index={c:i for i,c in enumerate(classes)}
    nw=len(classes);npot=len(data['ports'])
    problems=[ContextProblem(c) for c in data['contexts']]
    energy_cache={};seen={};rows=[];recids=[];costs=[]
    for rid,r in enumerate(records):
        e=data['edges'][r['edge']]
        key=(e['context'],tuple(map(tuple,r['outside_black'])))
        if key not in energy_cache:
            energy_cache[key]=energy_row(problems[e['context']],r['outside_black'],index)
        row=dict(energy_cache[key]);cost=int(e['macro'] in 'CQB')
        row[nw+e['target']]=row.get(nw+e['target'],0)+1
        row[nw+e['source']]=row.get(nw+e['source'],0)-1
        row={i:v for i,v in row.items() if v}
        rowkey=tuple(sorted(row.items())),cost
        if rowkey in seen:continue
        seen[rowkey]=len(rows);rows.append(row);recids.append(rid);costs.append(cost)
    rr=[];cc=[];vv=[]
    for j,row in enumerate(rows):
        for i,v in row.items():rr.append(j);cc.append(i);vv.append(v)
    A=coo_matrix((vv,(rr,cc)),shape=(len(rows),nw+npot),dtype=float).tocsr()
    C=np.array(costs,dtype=float)
    eq=vstack([A[:,nw:].T,coo_matrix(C[None,:])],format='csr')
    rhs=np.r_[np.zeros(npot),1.0]
    print(json.dumps({'input_cuts':len(records),'distinct_rows':len(rows),
                      'energy_variables':nw,'port_variables':npot,
                      'distinct_local_energy_rows':len(energy_cache)}),flush=True)
    result=linprog(np.ones(len(rows)),A_ub=-A[:,:nw].T,b_ub=np.zeros(nw),
                   A_eq=eq,b_eq=rhs,bounds=(0,None),method='highs-ds',
                   options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    assert result.success,result.message
    support=np.flatnonzero(result.x>1e-9)
    print(json.dumps({'floating_support':len(support),'objective':result.fun,
                      'maximum_balance_residual':float(np.max(np.abs(A[:,nw:].T@result.x))),
                      'minimum_energy_sum':float(np.min(A[:,:nw].T@result.x))}),flush=True)
    exact=None
    for bound in (100,1000,10000,100000,1000000,10000000,100000000,1000000000):
        candidate={int(i):Q(float(result.x[i])).limit_denominator(bound) for i in support}
        sums=[Q(0)]*(nw+npot)
        for i,v in candidate.items():
            for j,a in rows[i].items():sums[j]+=v*a
        if all(x==0 for x in sums[nw:]) and all(x>=0 for x in sums[:nw]):
            exact=candidate
            print(json.dumps({'rational_reconstruction_denominator_bound':bound}),flush=True)
            break
    if exact is None:
        # Reconstruct the floating basis as exact linear equations on its
        # support. A basic dual vertex has tight energy rows in addition
        # to graph balance and the cost normalization.
        active=np.flatnonzero(np.abs(A[:,:nw].T@result.x)<1e-8)
        cols=list(map(int,support));equations=[];targets=[]
        for j in list(range(nw,nw+npot))+list(map(int,active)):
            row=[rows[i].get(j,0) for i in cols]
            if any(row):equations.append(row);targets.append(0)
        equations.append([costs[i] for i in cols]);targets.append(1)
        solution=exact_linear_solve(equations,targets)
        exact={i:v for i,v in zip(cols,solution)}
        print(json.dumps({'exact_basis_reconstruction':True,'equations':len(equations)}),flush=True)
    assert all(v>0 for v in exact.values())
    denominator=math.lcm(*(v.denominator for v in exact.values()))
    integers={i:int(v*denominator) for i,v in exact.items()}
    divisor=reduce(math.gcd,integers.values())
    integers={i:v//divisor for i,v in integers.items()}
    # These are the decisive checks. No floating tolerances occur here.
    sums=[0]*(nw+npot);total_cost=0
    for i,v in integers.items():
        assert isinstance(v,int) and v>0
        for j,a in rows[i].items():sums[j]+=v*a
        total_cost+=v*costs[i]
    assert all(x==0 for x in sums[nw:])
    assert all(x>=0 for x in sums[:nw])
    assert total_cost>0
    terms=[]
    for i,v in sorted(integers.items()):
        r=records[recids[i]];e=data['edges'][r['edge']]
        terms.append({'cut_index':recids[i],'edge':r['edge'],'context':e['context'],
                      'source':e['source'],'target':e['target'],'macro':e['macro'],
                      'outside_black':r['outside_black'],'lambda_integer':v,
                      'energy_coefficients':{str(classes[j]):a for j,a in rows[i].items() if j<nw}})
    certificate={'status':'EXACT integer Farkas certificate','ansatz':'ordinary C4-invariant nonnegative 3x3 energy plus free port potential; fold-only cost',
                 'input_cut_count':len(records),'distinct_row_count':len(rows),'support_size':len(terms),
                 'energy_variable_count':nw,'port_variable_count':npot,
                 'total_fold_cost':total_cost,'multiplier_sum':sum(integers.values()),
                 'largest_multiplier':max(integers.values()),
                 'nonzero_aggregate_energy_coefficients':{str(classes[i]):v for i,v in enumerate(sums[:nw]) if v},
                 'potential_balance_identically_zero':True,
                 'source_sha256':{'contexts':hashlib.sha256(context_path.read_bytes()).hexdigest(),
                                  'compressed_cuts':hashlib.sha256(cuts_path.read_bytes()).hexdigest()},
                 'terms':terms}
    out=Path(__file__).with_name('fold_farkas_certificate.json')
    out.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({k:v for k,v in certificate.items() if k not in ('terms','nonzero_aggregate_energy_coefficients','source_sha256')},indent=2))

if __name__=='__main__':main()
