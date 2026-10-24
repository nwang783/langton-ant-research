#!/usr/bin/env python3
"""Independent literal tests for the arbitrary-color cap charge.

Tests check a written proof. They do not prove an infinite statement.
"""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

V = ((0,1),(1,0),(0,-1),(-1,0))


def audit(events):
    # An event is (x,y,incoming_heading,outgoing_heading,black_before).
    rows = defaultdict(list)
    rank = {}
    visits = Counter()
    for j, (x,y,h,hp,b) in enumerate(events):
        rows[x+y].append(j)
        rank[j] = visits[(x,y)]
        visits[(x,y)] += 1
    m = len(rows[0])
    hset = {j for j in rows[-1] if events[j][2:] == (2,1,True)}
    qset = {j for j in rows[-1] if events[j][2:] == (0,3,True)}
    eb = {j for j in rows[-2] if events[j][2:] == (3,0,False)}
    kc = {j for j in rows[-3] if events[j][2:] == (2,1,True)}
    h = len(hset)
    assert all(rank[j] == 0 and visits[events[j][:2]] == 1 for j in hset)

    roofs = []
    charged = set()
    positive_endpoints = set()
    for j in rows[0]:
        assert not events[j][4] and visits[events[j][:2]] == 1
        if events[j-1][4]:
            continue  # Not the first top event in this roof.
        k = 0
        end_top = j
        while events[end_top+1][4]:
            assert end_top+1 in hset
            k += 1
            end_top += 2
            assert end_top in rows[0]
        start_b, end_b = j-2, end_top+2
        assert sum(events[start_b][:2]) == -2
        assert sum(events[end_b][:2]) == -2
        roofs.append(k)
        if k == 0:
            assert events[start_b][:2] == events[end_b][:2]
            white = [a for a in (start_b,end_b) if a in eb]
            assert len(white) == 1 and white[0] not in charged
            charged.add(white[0])
        else:
            positive_endpoints.add(events[end_top+1][:2])
    assert m == len(roofs)+h and h == sum(roofs)
    j0 = roofs.count(0)
    jp = len(roofs)-j0
    rho = h-jp
    d0 = len(eb)-j0
    d = len(eb)-m+2*h
    assert d == d0+rho and min(d,d0,rho) >= 0

    assigned = defaultdict(list)
    unmarked = []
    c_events = rows[-3]
    for a in qset:
        if a-1 in eb-charged or a+1 in eb-charged:
            continue
        unmarked.append(a)
        left = max(j for j in c_events if j<a)
        right = min(j for j in c_events if j>a)
        x,y = events[a][:2]
        assert events[left][:2] == (x-1,y-1) == events[right][:2]
        assert not any(j in qset for j in range(left+1,right) if j!=a)
        choices = [j for j in (left,right) if j in kc]
        assert len(choices) == 1
        assigned[choices[0]].append(a)
    assert len(unmarked) >= len(qset)-2*d0
    collisions = 0
    for key, aa in assigned.items():
        assert len(aa) == 1, "The strengthened charge map must be injective."
    assert collisions <= jp
    q = len(qset)
    z = len(kc)+2*d+h-q
    assert len(kc) >= q-2*d0 and z >= h+2*rho
    delta = {t:sum(1-2*events[j][4] for j in rows[t]) for t in (-1,-2,-3)}
    assert q == 2*m-delta[-1]-3*h
    assert len(rows[-1]) == 4*m-delta[-1]-4*h
    assert len(rows[-2]) == 8*m-4*delta[-1]+delta[-2]-8*h-4*d
    assert len(rows[-3]) == 12*m-8*delta[-1]+4*delta[-2]-delta[-3]-8*d-4*z
    return {"M":m,"H":h,"D0":d0,"D":d,"rho":rho,"Jplus":jp,
            "Q":q,"KC":len(kc),"Z":z,"collisions":collisions}


def main():
    rng = random.Random(0xCA73A)
    counts = Counter()
    examples = {}
    for case in range(30000):
        p = (0.12,0.3,0.5,0.75)[case%4]
        black = {(x,t-x) for t in range(-6,1) for x in range(-10,11)
                 if rng.random()<p}
        black.discard((0,-4))
        initial = sorted(black)
        x,y,h = 0,-4,3
        events = []
        for step in range(180):
            b = (x,y) in black
            hp = (h+(-1 if b else 1))%4
            if b: black.remove((x,y))
            else: black.add((x,y))
            events.append((x,y,h,hp,b))
            dx,dy = V[hp]
            x += dx; y += dy; h=hp
            if x+y>0:
                break
            if x+y<=-4 and step>=5 and (step<30 or step%17==0):
                r = audit(events)
                counts["completed_segments"] += 1
                if r["M"]: counts["with_top"] += 1
                if r["H"]: counts["with_initial_black_bridges"] += 1
                if r["rho"]: counts["with_long_roofs"] += 1
                if r["collisions"]: counts["with_charge_collision"] += 1
                for label in ("H","rho","collisions"):
                    if r[label] and label not in examples:
                        examples[label]={"initial_black":initial,"steps":step+1,
                                         "result":r,"events":events.copy()}
        counts["initial_fields"] += 1
    output={"status":"finite_checks_passed_not_universal_proof",
            "counts":dict(counts),"examples":examples,
            "seed":0xCA73A,"max_updates":180}
    Path(__file__).with_name("arbitrary_cap_independent_checks.json").write_text(
        json.dumps(output,indent=2)+"\n")
    print(json.dumps({"status":output["status"],"counts":dict(counts),
                      "witness_types":list(examples)}))


if __name__ == "__main__": main()
