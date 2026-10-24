"""Targeted source-collision corrections after two phase-72 reversals.

Candidate corrections are single initially white cells whose first read is
in the bounded source region after both canonical reversal responses.  Thus
the earlier two responses are unchanged. All physical writes are retained.
A repeated word is only a locator; tail() certifies any reported capture.
This script does not count a finite delayed capture as regenerative feedback.
"""
import json
from pathlib import Path
from double_reversal import *


def probe(N=50,n=100,cap=400000,radius=45):
    q1,q2=markers(N,n)
    b=set(SEED)|{q1,q2};p=(0,0);h=REF['heading']
    seen=set();letters=[];hits={};jobs=[];t2=None;first_bad=None;last_bad=None
    for t in range(126000):
        if p==q2 and t2 is None:t2=t
        if p not in seen:
            if (t2 is not None and t>=t2+RECOVERY and
                max(abs(p[0]),abs(p[1]))<=radius and p not in b):
                jobs.append((t,p,h,set(b),''.join(letters[-9:])))
            seen.add(p)
        p,h,c=step(b,p,h);letters.append(c)
        if (t2 is not None and t>=t2+RECOVERY+208 and
            ''.join(letters[-10:]) not in FACT):
            if first_bad is None:first_bad=t+1
            last_bad=t+1
        if t>=125000 and (t+1)%104==0:
            nt=tail(b,p,h)
            if nt:break
    jobs=[j for j in jobs if first_bad-10<=j[0]<=last_bad]
    print(json.dumps({'kind':'inventory','N':N,'n':n,'q1':q1,'q2':q2,
          't2':t2,'first_baseline_capture':t+1,'collision_window':[first_bad-10,last_bad],
          'candidates':len(jobs)}),flush=True)
    for ti,qi,hi,bi,suffix in jobs:
        p=qi;h=hi;b=bi;flip(b,qi);last=0;bad=0;letters=list(suffix)
        visits_q1=visits_q2=0;nearest_q1=10**9;nearest_q2=10**9;nt=None
        for elapsed in range(1,cap+1):
            visits_q1+=p==q1;visits_q2+=p==q2
            nearest_q1=min(nearest_q1,max(abs(p[0]-q1[0]),abs(p[1]-q1[1])))
            nearest_q2=min(nearest_q2,max(abs(p[0]-q2[0]),abs(p[1]-q2[1])))
            p,h,c=step(b,p,h);letters.append(c)
            if len(letters)>=10 and ''.join(letters[-10:]) not in FACT:
                last=elapsed;bad+=1
            if elapsed%104==0 and elapsed-last>=208:
                nt=tail(b,p,h)
                if nt:break
        print(json.dumps({'kind':'case','correction':qi,'first_read':ti,
              'elapsed':elapsed,'bad10_after_correction':bad,'captured':nt is not None,
              'drift':None if nt is None else nt['drift'],'end':p,'heading':h,
              'q1_visits':visits_q1,'q2_visits':visits_q2,
              'nearest_q1':nearest_q1,'nearest_q2':nearest_q2}),flush=True)


if __name__=='__main__':probe()
