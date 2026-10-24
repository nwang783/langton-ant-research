"""Third independent C/V freshness checker: four fully colored cells.

Sensitive macro centers are solved by exact inverse lattice equations, never
by a bounded search. Every omitted center is therefore patch-invisible.
"""
import json
from pathlib import Path
from collections import deque

ROOT = Path('/workspace/shared/langton')
WORDS = {'C': 'LLLLRLRRRRLRRRR', 'V': 'LLLLRLRRRRLRRLRRRR'}
source = json.loads((ROOT/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text())
assert all(source[k]['word'] == word for k,word in WORDS.items())
DIRS = ((0,1),(1,0),(0,-1),(-1,0))
PATCH = ((1,1),(1,2),(2,1),(2,2))
INDEX = {p:i for i,p in enumerate(PATCH)}
NOSE = (1,2)
QBIT = 1 << INDEX[NOSE]
OUT = None

def trace(p, h, word):
    visits = []
    for c in word:
        assert c in 'RL'
        visits.append((p, c == 'L'))
        h = (h + (1 if c == 'R' else -1)) % 4
        p = (p[0]+DIRS[h][0], p[1]+DIRS[h][1])
    return visits, (p,h)

def inverse(p, h):
    f,r = DIRS[h], DIRS[(h+1)%4]
    X,Y = 2*p[0]+f[0]-r[0]+1, 2*p[1]+f[1]-r[1]-1
    an,bn = X+3*Y, -3*X+Y
    if an % 20 or bn % 20:
        return None
    return an//20, bn//20, h

def pose(a,b,h):
    f,r = DIRS[h], DIRS[(h+1)%4]
    x,y = -1+2*a-6*b-f[0]+r[0], 1+6*a+2*b-f[1]+r[1]
    assert x % 2 == y % 2 == 0
    return (x//2,y//2),h

centers = set()
for q in PATCH:
    for h in range(4):
        for word in WORDS.values():
            relative,_ = trace((0,0),h,word)
            for displacement,_ in relative:
                p = (q[0]-displacement[0], q[1]-displacement[1])
                st = inverse(p,h)
                if st is not None:
                    centers.add(st[:2])

heads = {(a,b,h) for a,b in centers for h in range(4)}
transitions = {}
initial = set()
sources = []
for head in heads:
    p,h = pose(*head)
    assert inverse(p,h) == head
    for name,word in WORDS.items():
        visits,(end,eh) = trace(p,h,word)
        dest = inverse(end,eh)
        assert dest is not None
        a,b,h = head
        da,db = ((1,0),(0,-1),(-1,0),(0,1))[h]
        expected = (a,b,(h-1)%4) if name == 'C' else (a+da,b+db,h)
        assert dest == expected
        dest = dest if dest in heads else OUT
        local = [(1 << INDEX[q],black) for q,black in visits if q in INDEX]
        transitions[head,name] = dest,local
        nose_colors = [black for q,black in visits if q == NOSE]
        if nose_colors and not nose_colors[-1]:
            # Store the forced post-macro colors; leave every other bit free.
            known = blackmask = 0
            for bit,black in local:
                known |= bit
                if black: blackmask &= ~bit
                else: blackmask |= bit
            sources.append((head,name))
            for mask in range(1 << len(PATCH)):
                if mask & known == blackmask:
                    initial.add((dest,mask))

target_visits,_ = trace(*pose(0,0,0),WORDS['V'])
assert [black for q,black in target_visits if q == NOSE] == [True,False]
boundary = set()
for head in heads:
    a,b,h = head
    da,db = ((1,0),(0,-1),(-1,0),(0,1))[h]
    if (a-da,b-db) not in centers:
        boundary.add(head)

def successors(state):
    head,mask = state
    assert mask & QBIT
    if head is OUT:
        return {(q,mask) for q in boundary}
    result = set()
    for name in WORDS:
        dest,reads = transitions[head,name]
        target = head == (0,0,0) and name == 'V'
        if not target and any(bit == QBIT for bit,_ in reads):
            continue
        current = mask
        for bit,black in reads:
            if bool(current & bit) != black:
                break
            current ^= bit
        else:
            assert not target, ('ABSTRACT REUSE',state)
            result.add((dest,current))
    return result

closure = set(initial)
queue = deque(initial)
while queue:
    state = queue.popleft()
    for child in successors(state):
        if child not in closure:
            closure.add(child)
            queue.append(child)
assert initial <= closure
for state in closure:
    assert successors(state) <= closure

# Four consecutive C's cannot be followed by either allowed macro.
conflicts = {}
for following in WORDS:
    seen = {}
    conflict = None
    visits,_ = trace((0,0),0,WORDS['C']*4+WORDS[following])
    for t,(q,black) in enumerate(visits):
        if q in seen and seen[q][1] == black:
            conflict = (q,seen[q][0],t,'L' if black else 'R')
            break
        seen[q] = (t,black)
    assert conflict == ((2,1),7,67,'R')
    conflicts['CCCC'+following] = conflict

out = dict(status='PASS: no prior-read V nose in any feasible C/V concatenation',
           patch=PATCH, sensitive_centers=sorted(centers),
           head_states=len(heads)+1, last_R_source_macros=sorted(sources),
           initial_full_color_states=len(initial), reachable_full_color_states=len(closure),
           outside_states=sum(h is OUT for h,m in closure),
           consecutive_C_conflicts=conflicts,
           finite_support_macro_bound='4*m+4 for entry-time black mass m',
           semantics='Freshness is relative to the chosen C/V concatenation, including tails begun mid-history.',
           closure=sorted(closure,key=repr))
(ROOT/'audits/cv_patch_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='closure'},indent=2))
