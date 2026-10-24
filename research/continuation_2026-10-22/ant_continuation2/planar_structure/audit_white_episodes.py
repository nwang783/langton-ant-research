"""Audit the finite-white-component episode theorem with integer geometry.

The physical ant simulation and white-dual graph reconstruction are independent.
Exhaustive tests use every internal bond coloring of several small rectangles;
all their boundary bonds start black, so all rectangle vertices are finite.
"""
from __future__ import annotations

from collections import deque
from itertools import product
from pathlib import Path
import json
import random

DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))
HERE = Path(__file__).resolve().parent


def edge(p):
    x, y = p
    if (x + y) % 2 == 0:
        return ((x+y)//2-1, (x-y)//2), ((x+y)//2, (x-y)//2)
    return ((x+y-1)//2, (x-y-1)//2), ((x+y-1)//2, (x-y+1)//2)


def cell(a, b):
    (u, v), (r, s) = sorted((a, b))
    assert abs(u-r)+abs(v-s) == 1
    if u != r:
        return (u+v+1, u-v+1)
    return (u+v+1, u-v)


def active(p, h):
    x, y = p
    assert (x+y+h) % 2 == 0
    a, b = ((x-1,y-1),(x-1,y),(x,y),(x,y-1))[h]
    assert (a+b) % 2 == 0
    return ((a+b)//2, (a-b)//2)


def pose(a, b):
    p = cell(a, b)
    hs = [h for h in range(4) if (p[0]+p[1]+h) % 2 == 0 and active(p, h) == a]
    assert len(hs) == 1
    return p, hs[0]


def step(B, p, h):
    old_p = p
    h = (h + (-1 if p in B else 1)) % 4
    B.symmetric_difference_update({old_p})
    dx, dy = DIR[h]
    return (p[0]+dx,p[1]+dy), h


def adjacent(v):
    x, y = v
    return ((x+1,y),(x-1,y),(x,y+1),(x,y-1))


def finite_vertices(B):
    if not B:
        return set()
    removed = {frozenset(edge(p)) for p in B}
    vertices = set().union(*removed)
    xs, ys = zip(*vertices)
    lo, hi, bot, top = min(xs)-1, max(xs)+1, min(ys)-1, max(ys)+1
    box = set(product(range(lo,hi+1),range(bot,top+1)))
    reached = {(lo,bot)}
    q = deque(reached)
    while q:
        v = q.popleft()
        for w in adjacent(v):
            if w in box and w not in reached and frozenset((v,w)) not in removed:
                reached.add(w)
                q.append(w)
    return box-reached


def component(v, S, B=None):
    assert v in S
    found = {v}
    q = deque(found)
    while q:
        a = q.popleft()
        for b in adjacent(a):
            if b in S and b not in found and (B is None or cell(a,b) not in B):
                found.add(b)
                q.append(b)
    return found


def geometry(K):
    internal, boundary = set(), set()
    for v in K:
        for w in adjacent(v):
            (internal if w in K else boundary).add(cell(v,w))
    xs, ys = zip(*K)
    a, b = max(xs)-min(xs)+1, max(ys)-min(ys)+1
    r = min(a,b)
    clock_bound = len(internal)*(3**(r-1)-1)+2*(3**r-1)+1
    return internal, boundary, a, b, clock_bound


def check_episode(B, p, h, S=None):
    B = set(B)
    initial = set(B)
    S = finite_vertices(B) if S is None else set(S)
    av = active(p,h)
    assert av in S
    K = component(av,S)
    internal,boundary,a,b,bound = geometry(K)
    assert boundary <= B
    assert 16*len(S) <= len(B)**2
    assert 2*(a+b) <= len(boundary) <= len(B)
    seen = set()
    for t in range(bound):
        av = active(p,h)
        assert av in K
        state = (frozenset(B & internal),p,h)
        assert state not in seen
        seen.add(state)
        ends = edge(p)
        assert av in ends
        other = next(v for v in ends if v != av)
        old_W = component(av,S,B)
        black = p in B
        exit_now = black and other not in S
        old_p = p
        p,h = step(B,p,h)
        new_av = active(p,h)
        assert new_av == (av if black else other)
        if exit_now:
            assert old_p in boundary
            new_S = finite_vertices(B)
            assert new_S == S-old_W
            assert new_av not in new_S
            return t+1, len(K), len(internal), a, b, bound
        assert old_p in internal
        assert B-boundary-internal == initial-boundary-internal
        assert boundary <= B
    raise AssertionError('Clock exit bound violated')


def local_audit():
    checks = 0
    for x,y,h,black in product(range(-4,5),range(-4,5),range(4),range(2)):
        if (x+y+h) % 2:
            continue
        p = (x,y)
        av = active(p,h)
        a,b = edge(p)
        assert av in (a,b)
        assert cell(a,b) == p
        other = b if av == a else a
        B = {p} if black else set()
        q,k = step(B,p,h)
        assert active(q,k) == (av if black else other)
        checks += 1
    return checks


def rectangle_audit():
    summaries = []
    for a,b in ((1,1),(1,2),(1,4),(2,2),(2,3),(3,3)):
        K = set(product(range(a),range(b)))
        internal,boundary,aa,bb,bound = geometry(K)
        edges = sorted(internal)
        poses = [pose(v,w) for v in sorted(K) for w in adjacent(v)]
        cases, maximum = 0, 0
        example = None
        for mask in range(1 << len(edges)):
            B = boundary | {p for j,p in enumerate(edges) if (mask >> j)&1}
            for p,h in poses:
                result = check_episode(B,p,h,K)
                cases += 1
                if result[0] > maximum:
                    maximum = result[0]
                    example = {'black_internal_mask':mask,'pose':[p,h]}
        summaries.append({'rectangle':[a,b],'mutable_bonds':len(edges),
                          'cases':cases,'maximum_exit_steps':maximum,
                          'uniform_clock_bound':bound,'maximizer':example})
        print(summaries[-1],flush=True)
    return summaries


def sampled_orbits():
    rng = random.Random(20261022)
    seeds = [set()]
    cells = list(product(range(-3,4),repeat=2))
    seeds.extend({p for p in cells if rng.randrange(3)==0} for _ in range(12))
    checks, entries, maximum = 0, 0, 0
    for index,seed in enumerate(seeds):
        B,p,h = set(seed),(0,0),0
        for t in range(900 if index else 11000):
            S = finite_vertices(B)
            av = active(p,h)
            old_B = set(B)
            old_p,old_h = p,h
            black = p in B
            a,b = edge(p)
            other = b if av==a else a
            p,h = step(B,p,h)
            if av in S:
                old_W = component(av,S,old_B)
                expected = S-old_W if black and other not in S else S
                assert finite_vertices(B) == expected
                checks += 1
                if t % 19 == 0:
                    result = check_episode(old_B,old_p,old_h,S)
                    entries += 1
                    maximum = max(maximum,result[0])
    return {'orbits':len(seeds),'internal_transition_checks':checks,
            'full_episode_checks':entries,'maximum_sampled_exit':maximum}


def main():
    results = {'status':'PASS','local_coordinate_cases':local_audit()}
    results['exhaustive_rectangles'] = rectangle_audit()
    results['sampled_orbits'] = sampled_orbits()
    (HERE/'white_episode_audit.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2),flush=True)


if __name__ == '__main__':
    main()
