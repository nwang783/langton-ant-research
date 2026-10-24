"""Two preinstalled phase-72 markers, complete physical board retained.

Positive capture uses an exact infinite-tail test. A step cutoff gives only
an unresolved experiment, never a negative conclusion.
"""
import json,sys
from pathlib import Path
from first_marker_scattering import *

def phases():
    b=set(SEED);p=(0,0);h=REF['heading'];out=[]
    for _ in range(104):out.append((p,h));p,h,c=step(b,p,h)
    return out

PH=phases()

def reference_reversal():
    age=50;b=set(SEED);p=(0,0);h=REF['heading']
    for _ in range(104*age+72):p,h,c=step(b,p,h)
    base=p;flip(b,p);letters=[];last=0
    for t in range(1,100000):
        p,h,c=step(b,p,h);letters.append(c)
        if t>=10 and ''.join(letters[-10:]) not in FACT:last=t
        if t%104==0 and t-last>=208:
            nt=tail(b,p,h)
            if nt:break
    assert nt['drift']==(2,2)
    a=next(a for a in range(104) if W[a:]+W[:a]==nt['word'])
    assert h==(PH[a][1]+2)%4
    return sub(p,base),a,t

V,A,RECOVERY=reference_reversal()

def markers(N,n):
    q1=add(PH[72][0],DR,N)
    v=add(q1,V)
    dq=sub(PH[72][0],PH[A][0]);dq=(-dq[0],-dq[1])
    q2=add(add(v,(2,2),n+(72<A)),dq)
    return q1,q2

def run(N,n,cap):
    q1,q2=markers(N,n);b=set(SEED)|{q1,q2};p=(0,0);h=REF['heading'];letters=[];bad=0;last=0;hits={};segments=[];streak=0
    for t in range(1,cap+1):
        if p in (q1,q2) and p not in hits:hits[p]=t-1
        p,h,c=step(b,p,h);letters.append(c)
        if t>=10 and ''.join(letters[-10:]) not in FACT:bad+=1;last=t;streak=0
        else:streak+=1
        if t%104==0 and t-last>=208:
            nt=tail(b,p,h)
            if nt:
                return {'N':N,'gap':n,'markers':[q1,q2],'steps':t,'bad10':bad,'last_bad_end':last,'mass':len(b),'end':p,'heading':h,'drift':nt['drift'],'captured':True,'first_hits':[(q,hits.get(q)) for q in (q1,q2)]}
    return {'N':N,'gap':n,'markers':[q1,q2],'steps':cap,'bad10':bad,'last_bad_end':last,'mass':len(b),'end':p,'heading':h,'captured':False,'first_hits':[(q,hits.get(q)) for q in (q1,q2)]}

if __name__=='__main__':
    if len(sys.argv)>=4:
        jobs=[(int(sys.argv[1]),int(sys.argv[2]))]; cap=int(sys.argv[3])
    else:
        jobs=sorted(set([(50,n) for n in (50,100,200,400)]+[(n,n) for n in (50,100,200,400)]+[(2*n,n) for n in (50,100,200,400)]+[(n,2*n) for n in (50,100,200,400)]));cap=2000000
    for N,n in jobs: print(json.dumps(run(N,n,cap)),flush=True)
