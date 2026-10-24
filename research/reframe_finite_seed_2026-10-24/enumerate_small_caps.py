"""Exhaustive bounded-active no-import classification, author computation.
Every connected w edge set containing the fixed root, through chosen mass.
"""
from active_flight import *
from pathlib import Path
import json,sys,time
OUT=Path(__file__).parent

def levels(N):
    w=cursor((0,0),0);old={frozenset()};yield old
    for n in range(1,N+1):
        nxt=set()
        for C in old:
            vs=vertices(C,1)|{w}
            for x,y in vs:
                for dx,dy in((2,2),(2,-2),(-2,2),(-2,-2)):
                    assert (2*x+dx)%4==0 and(2*y+dy)%4==0
                    q=((2*x+dx)//4,(2*y+dy)//4)
                    if q not in C:nxt.add(C|{q})
        old=nxt;yield old

def main():
    N=int(sys.argv[1])if len(sys.argv)>1 else 5
    reports={M:{'cap':M,'states':0,'import':0,'cap_exit':0,'translator':0,'maximum_event':0,'max_witness':None}for M in range(N+1)}
    sizecounts=[];start=time.time()
    for n,L in enumerate(levels(N)):
        sizecounts.append(len(L));print('mass',n,'shapes',len(L),flush=True)
        for C in sorted(L,key=lambda z:sorted(z)):
            for M in range(n,N+1):
                a=plan(C,M=M);r=reports[M];r['states']+=1
                r[{'cap':'cap_exit','import':'import','translator':'translator'}[a.status]]+=1
                if a.status=='translator':raise AssertionError(('POSITIVE_CANDIDATE_REQUIRES_REVIEW',C,M,a))
                if a.event>=r['maximum_event']:
                    r['maximum_event']=a.event;r['max_witness']={'black_cells':sorted(C),'outcome':a.status,'predictor_period':a.period,'predictor_drift':a.drift,'first_import_or_cap':a.event,'contact':a.witness}
        print('elapsed',round(time.time()-start,3),'events',[(M,reports[M]['maximum_event'])for M in reports],flush=True)
    out={'status':'AUTHOR_EXHAUSTIVE_CONTROLS_PASS','scope':'Exact finite graph-shape enumeration only through supplied maximum cap. No extrapolation.','max_cap':N,'rooted_connected_shapes_by_mass':sizecounts,'caps':[reports[M]for M in range(N+1)]}
    (OUT/f'small_cap_{N}_classification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
