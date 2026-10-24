"""Reconstruct the 739-case certificate missing from Ke's release package.

The input family and the thresholds are prior results, not new claims.
All finite sources and every infinite suffix are checked from complete fields.
"""
import hashlib
import json
import time
from pathlib import Path
from ant_exact import *

THRESHOLDS = [
8,7,9,2,1,5,1,3,5,15,7,2,2,1,2,6,1,2,5,2,3,11,21,3,4,3,
2,1,13,17,1,17,3,7,1,3,18,10,7,0,14,8,3,5,9,9,4,4,9,4,
5,25,9,13,2,12,7,2,0,16,9,14,12,14,0,3,2,4,14,3,4,8,11,
6,12,5,12,4,4,15,14,0,0,15,1,15,0,8,0,1,0,3,1,4,2,5,8,
1,3,0,3,2,1,1]

def one_case(n,r):
    B,p,h=canonical_source(n,r)
    q=p
    B.symmetric_difference_update({p})
    invB=set(B);ip=p;ih=h;old=[];invreads=[]
    for _ in range(9):
        ip,ih,c=inverse_step(invB,ip,ih)
        old.append(c);invreads.append(ip)
    history=''.join(reversed(old))
    reads=set(invreads)
    forward=[]
    defects=0;last_defect=None;max_radius=0
    for L in range(1,104001):
        reads.add(p)
        max_radius=max(max_radius,abs(p[0]-q[0]),abs(p[1]-q[1]))
        p,h,c=step(B,p,h)
        forward.append(c)
        history=(history+c)[-10:]
        if history not in LEGAL10:
            defects+=1;last_defect=L-1
        if L%104:
            continue
        word=''.join(forward[-104:])
        if word not in PHASES:
            continue
        cert=certify_period(B,p,h,word)
        if cert is None:
            continue
        guarded = avoids_old_tail(reads,p,h,word,n)
        if n==THRESHOLDS[r] and not guarded:
            raise AssertionError(('failed old-tail guard',n,r,L))
        return dict(n=n,r=r,steps=L,position=p,heading=h,phase=PHASES[word],
                    field_count=len(B),field_sha256=hashlib.sha256(repr(sorted(B)).encode()).hexdigest(),
                    defect_count=defects,last_defect=last_defect,radius=max_radius,
                    tail=cert,old_tail_guard=guarded)
    raise AssertionError(('no certificate found within construction budget',n,r))

def main():
    assert len(THRESHOLDS)==104
    assert sum(n+1 for n in THRESHOLDS)==739
    rows=[];start=time.time()
    for r,N in enumerate(THRESHOLDS):
        for n in range(N+1):
            rows.append(one_case(n,r))
        if r%10==0:
            print(json.dumps({'completed_phases':r+1,'cases':len(rows),'seconds':round(time.time()-start,2)}),flush=True)
    result=dict(status='all cases and infinite guards proved by exact finite checks',
                thresholds=THRESHOLDS,cases=rows,
                totals=dict(cases=len(rows),literal_steps=sum(x['steps'] for x in rows),
                    breakpoints=sum(x['tail']['breakpoints'] for x in rows),
                    maximum_steps=max(x['steps'] for x in rows),
                    maximum_radius=max(x['radius'] for x in rows),
                    maximum_defects=max(x['defect_count'] for x in rows),
                    infinite_guard_bases=sum(x['n']==THRESHOLDS[x['r']] for x in rows)))
    out=Path(__file__).with_name('one_bit_certificate_restored.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['totals']),flush=True)

if __name__=='__main__':
    main()
