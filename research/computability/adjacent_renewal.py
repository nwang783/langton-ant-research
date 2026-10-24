#!/usr/bin/env python3
"""Exact total next-adjacent-defect renewal, never a finite-repeat heuristic.
Termination uses the audited no-K theorem; an independent elementary running
bound is proved in elementary_adjacent_renewal_bound.md. True inverse history
preserves overlapping events across renewed checkpoints.
"""
from dataclasses import dataclass
from collections import deque
from pathlib import Path
import json,random
from check_rigid_reachability import State,D,forward,backward,transform
from periodic_tail_checker import first_mismatch

STANDARD=json.loads((Path(__file__).resolve().parents[1]/'recovered_bundle/ant_global/root/standard.json').read_text())
WORD=STANDARD['word'];PHASES={WORD[i:]+WORD[:i] for i in range(104)}
FACTORS={''.join(WORD[(i+j)%104] for j in range(10)) for i in range(104)}
assert len(WORD)==104 and len(FACTORS)==84

def history(s,n=104):
    out=[]
    for _ in range(n):
        s=backward(s);out.append('L' if s.p in s.black else 'R')
    return ''.join(reversed(out))

def pair(w):
    return len(w)>=11 and w[-11:-1] not in FACTORS and w[-10:] not in FACTORS

@dataclass
class Result:
    kind:str
    steps:int
    state:State
    tail_word:str|None=None


def renew(s):
    hist=deque(history(s),maxlen=104);black=set(s.black);p=s.p;h=s.h;t=0
    while True:
        recent=''.join(hist)
        if recent in PHASES:
            current=State(frozenset(black),p,h)
            if first_mismatch(current,recent) is None:
                # The last104 true past turns also match this phase. Hence
                # all boundary windows, not just wholly future ones, are good.
                return Result('terminal',t,current,recent)
        c='L' if p in black else 'R';hist.append(c)
        h=(h+(-1 if c=='L' else 1))%4;black.symmetric_difference_update((p,))
        dx,dy=D[h];p=p[0]+dx,p[1]+dy;t+=1
        if pair(''.join(hist)):
            return Result('event',t,State(frozenset(black),p,h))


def controls():
    rng=random.Random(2026102219);checked=0
    pts=[(x,y) for x in range(-3,4) for y in range(-3,4)]
    for _ in range(80):
        s=State(frozenset(rng.sample(pts,rng.randrange(10))),(0,0),0)
        z=s;w=history(s,10);first=None
        for t in range(200):
            w+=('L' if z.p in z.black else 'R');z=forward(z)
            if pair(w):first=(t+1,z);break
        if first:
            ans=renew(s);assert ans.kind=='event' and (ans.steps,ans.state)==first;checked+=1
    seed=State(frozenset(map(tuple,STANDARD['seed'])),(0,0),STANDARD['heading'])
    for _ in range(104):seed=forward(seed)
    phases=0
    for j in range(104):
        for r in range(4):
            ans=renew(transform(seed,r,(117,-231)))
            assert ans.kind=='terminal' and ans.steps==0;phases+=1
        seed=forward(seed)
    # Repeated next-event calls must preserve adjacent and overlapping events.
    blank=State(frozenset(),(0,0),0);z=blank;w=history(z,10);positions=[]
    for t in range(500):
        w+=('L' if z.p in z.black else 'R');z=forward(z)
        if pair(w):positions.append(t+1)
    z=blank;elapsed=0
    for target in positions[:30]:
        ans=renew(z);assert ans.kind=='event';elapsed+=ans.steps;z=ans.state
        assert elapsed==target
    return {'random_first_event_controls':checked,'terminal_phase_rotation_controls':phases,
            'overlapping_event_controls':min(30,len(positions)),
            'status':'PASS finite implementation controls; totality and elementary bound are separate analytic theorems'}

if __name__=='__main__':
    result=controls();Path(__file__.replace('.py','_controls.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
