#!/usr/bin/env python3
"""Exact infinite periodic-word verifier for explicit finite ant states.

No finite-repeat heuristic. A returned mismatch is the literal first mismatch.
An absent mismatch certifies the entire prescribed infinite word by induction.
"""
from check_rigid_reachability import State, D, forward, transform
import json
from pathlib import Path

def multiplier(u,v):
    """Return integer k with u=k*v, or None; requires nonzero v."""
    if v[0]:
        if u[0]%v[0]:return None
        k=u[0]//v[0]
        return k if u[1]==k*v[1] else None
    if u[0] or u[1]%v[1]:return None
    return u[1]//v[1]

def plan(s,w):
    p=s.p;h=s.h;points=[]
    for ch in w:
        if ch not in 'LR':raise ValueError('Word must use L,R.')
        points.append(p);h=(h+(1 if ch=='R' else -1))%4
        dx,dy=D[h];p=(p[0]+dx,p[1]+dy)
    d=(p[0]-s.p[0],p[1]-s.p[1])
    if not w or h!=s.h or d==(0,0):
        raise ValueError('Need nonempty heading-restoring nonzero-drift period.')
    return points,d

def first_mismatch(s,w):
    qs,d=plan(s,w);P=len(w);answer=None
    for i,q in enumerate(qs):
        thresholds=[];tests={0}
        for j,qj in enumerate(qs):
            k=multiplier((qj[0]-q[0],qj[1]-q[1]),d)
            if k is not None and (k>0 or (k==0 and j<i)):
                thresholds.append(k);tests.add(k)
        for b in s.black:
            k=multiplier((b[0]-q[0],b[1]-q[1]),d)
            if k is not None and k>=0:tests.update((k,k+1))
        for k in sorted(tests):
            at=(q[0]+k*d[0],q[1]+k*d[1])
            bit=(at in s.black)^(sum(t<=k for t in thresholds)%2)
            if bit!=(w[i]=='L'):
                t=k*P+i
                if answer is None or t<answer:answer=t
                break
    return answer

def main():
    data=json.loads((Path(__file__).resolve().parents[1]/'recovered_bundle/ant_global/root/standard.json').read_text())
    word=data['word'];seed=State(frozenset(map(tuple,data['seed'])),(0,0),data['heading'])
    assert first_mismatch(seed,word) is None
    phases=0
    s=seed
    for i in range(len(word)):
        rotated=word[i:]+word[:i]
        for r in range(4):assert first_mismatch(transform(s,r,(123,-93)),rotated) is None;phases+=1
        s=forward(s)
    qs,d=plan(seed,word)
    # Locate a phase whose first visit in a late epoch is not an earlier phase.
    # Every marker is certified directly; compare all modest markers literally.
    near=[];far=[]
    for n in (3,7,10**30):
        point=(qs[0][0]+n*d[0],qs[0][1]+n*d[1])
        changed=State(seed.black.symmetric_difference((point,)),seed.p,seed.h)
        mismatch=first_mismatch(changed,word)
        assert mismatch is not None
        if n<100:
            s=changed
            for t in range(mismatch+1):
                bit=s.p in s.black
                if bit!=(word[t%len(word)]=='L'):
                    assert t==mismatch;break
                s=forward(s)
            near.append({'epoch':n,'first_mismatch':mismatch})
        else:far.append({'epoch':n,'first_mismatch':mismatch})
    print(json.dumps({'status':'exact arithmetic checker controls passed; analytic proof separate',
                      'phase_rotation_checks':phases,'near_markers':near,'huge_markers':far},indent=2))
if __name__=='__main__':main()
