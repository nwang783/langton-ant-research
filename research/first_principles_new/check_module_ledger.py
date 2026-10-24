"""Exhaust the exact finite return interface used in face_module_return_lemma.md.

Child state 0: no G used; child state 1: G used; child state 2: B used.
A finite parent return can use only a G child return, which exists only from
state 0 and moves that child to state 1. A child B would force immediate
re-entry and prevent any finite parent return, by the induction hypothesis.
The parent sign is R=0. Exterior resets of the two boundary lamps do not
change these interior states.
"""
from itertools import product

def finish(s):
    x,y,c1,c2=s
    first=bool(x)
    if x:
        if c1:return None
        c1=1
    if y:
        if c2:return None
        c2=1
    return ('B' if first else 'G'), (0 if y else 1,1,c1,c2)

allowed={'','G','B','GB'}
traces=set()
for s0 in product(range(2),range(2),range(3),range(3)):
    s=s0;word=''
    for call in range(4):
        r=finish(s)
        if r is None:break
        outcome,s=r;word+=outcome
        assert word in allowed,(s0,word,s)
    else:raise AssertionError(('four returns',s0))
    traces.add(word)
print('PASS: all 36 initial interior/child-interface states; exact completed traces',sorted(traces))
