"""Exact primary-theorem hypothesis test, not a rotor theorem for the ant."""
from pathlib import Path
from collections import Counter, defaultdict
from itertools import product
import json, hashlib
from check_return_permanent_output_debt import DXY, future

P = Path(__file__).parent
B = {}; p = (0, 0); h = 1
events = []; snapshots = {}; visits = defaultdict(list)
cutset = {0, 5, 8, 9, 13, 14, 16, 17, 52, 9977, 10081}
for t in range(10081):
    if t in cutset:
        snapshots[t] = (dict(B), p, h)
    old = B.pop(p, None)
    ch = 'R' if old is None else 'L'
    if old is None:
        B[p] = t
    out = (h + (1 if ch == 'R' else -1)) % 4
    q = (p[0] + DXY[out][0], p[1] + DXY[out][1])
    # Exact square mirror/rotator gauge: slash (+1) sends (dx,dy) to (dy,dx).
    # At an even site in this sector, the mirror sign is the negative rotator sign.
    r = 1 if ch == 'R' else -1
    mu = (-1 if sum(p) % 2 == 0 else 1) * r
    vx, vy = DXY[h]
    mirror_out = (mu * vy, mu * vx)
    assert mirror_out == DXY[out]
    assert h % 2 == (1 - sum(p) % 2)
    row = dict(tick=t, cell=p, incoming=h, turn=ch, outgoing=out, next=q,
               old_lifetime=old, mirror_sign=mu)
    visits[p].append(row); events.append(row)
    p, h = q, out
snapshots[10081] = (dict(B), p, h)

bb, pp, hh = snapshots[9977]
W, drift, deaths, parity = future(bb, pp, hh)
assert W == ''.join(e['turn'] for e in events[9977:])
assert drift == (-2, 2) and len(bb) == 715

def interval(s, t):
    rows = events[s:t]
    cnt = Counter(tuple(z['cell']) for z in rows)
    return dict(start=s, end=t, reads=t-s, word=''.join(z['turn'] for z in rows),
                read_counts=[dict(cell=q, count=n) for q,n in sorted(cnt.items())],
                read_set=sorted(cnt), max_reads=max(cnt.values()))

# Return-cut convention: two subsequent returns to the origin per packet.
returns = [z['tick'] for z in events[:53] if z['cell'] == (0, 0)]
assert returns == [0, 4, 8, 16, 52]
A1 = set(tuple(z['cell']) for z in events[0:8])
A2 = set(tuple(z['cell']) for z in events[8:52])
missing = sorted(A1 - A2)
assert missing
assert (1, 0) in missing and (1, 1) in missing
assert max(Counter(z['cell'] for z in events[8:52]).values()) > 2

# The first repeated directed edge after a fully retained actual reset is not at its origin.
seen = {}; repeat = None
for z in events[8:53]:
    edge = (z['cell'], z['next'])
    if edge in seen:
        repeat = dict(first=seen[edge], second=z['tick'], edge=edge)
        break
    seen[edge] = z['tick']
assert repeat == dict(first=9, second=13, edge=((0,1),(-1,1)))
assert next(z['tick'] for z in events[9:] if z['cell'] == (0,0)) == 16
assert set(snapshots[8][0]) == {(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)}

# Local exact algebra, every initial color / incoming axis / sign word up to length 8.
algebra_count = 0
for axis in (0, 1):
    e = DXY[axis]; f = DXY[(axis+1)%4]
    for r0 in (-1, 1):
        for n in range(1, 9):
            for aa in product((-1,1), repeat=n):
                zz = []
                for j,a in enumerate(aa):
                    ih = axis if a == 1 else (axis+2)%4
                    r = r0 * (-1)**j
                    oh = (ih + r) % 4
                    z = r0 * (-1)**j * a
                    assert DXY[oh] == (z*f[0], z*f[1])
                    zz.append(z)
                paired = sum(aa[j] != aa[j+1] for j in range(0,n-1,2))
                assert sum(zz) == r0 * sum((-1)**j*a for j,a in enumerate(aa))
                assert abs(sum(zz)) <= 2*paired + n%2
                assert all((zz[j] == zz[j+1]) == (aa[j] != aa[j+1]) for j in range(n-1))
                algebra_count += 1

# A nonabelian two-input local processor witness. These are port inputs, not an exterior route.
def local(seq):
    r = 1; outs = []
    for ih in seq:
        outs.append((ih+r)%4); r = -r
    return dict(incoming=seq, outgoing=outs, final_rotator=r)
ab, ba = local([0,2]), local([2,0])
assert ab['outgoing'] == [1,1] and ba['outgoing'] == [3,3]
assert ab['final_rotator'] == ba['final_rotator'] == 1

# This obstruction is not a finite transient error: one pair recurs in every certified period.
u, v = events[9980], events[9984]
assert u['cell'] == v['cell'] == (8,16)
assert (u['incoming'],v['incoming'],u['turn'],v['turn'],u['outgoing'],v['outgoing']) == (3,1,'L','R',2,2)
assert all(z['cell'] != (8,16) for z in events[9981:9984])
stable = dict(first=9980, second=9984, cell=(8,16), drift=drift, period=104,
              incoming=[3,1], turns='LR', outgoing=[2,2],
              assertion='For every k>=0 these two consecutive visits occur at ticks +104k and cell +(-2k,2k).')

# Also retain the literal visit-count threshold cuts printed in the primary paper.
# The source prose describes return-cut packets. Neither convention repairs this ant transfer.
threshold = [interval(0,5), interval(5,17)]
threshold_missing = sorted(set(tuple(z['cell']) for z in events[:5]) - set(tuple(z['cell']) for z in events[5:17]))
assert threshold_missing

deps = ['check_return_permanent_output_debt.py','ORDERED_SQUARE_CIRCULATION_MANIFEST.json',
        '../audits/check_ordered_square_circulation_independent.json',
        'EXPLICIT_RECORD_CLOCK_MANIFEST.json']
for f in deps:
    assert (P/f).exists(), f
out = dict(status='AUTHOR: exact rotor transfer obstruction; independent audit pending',
 initial_black=[], initial_pose=[[0,0],1], fine_reads=len(events), full_word=''.join(z['turn'] for z in events),
 first_53_events=events[:53], complete_snapshots=[dict(cut=t,pose=[q,head],black=[dict(cell=z,lifetime=i) for z,i in sorted(b.items())]) for t,(b,q,head) in sorted(snapshots.items())],
 return_cuts=returns, return_packets=[interval(0,8),interval(8,52)], lost_previous_packet_cells=missing,
 literal_printed_threshold_packets=threshold, literal_printed_threshold_missing=threshold_missing,
 first_repeated_edge=repeat, next_origin_return=16,
 local_algebra_cases=algebra_count, nonabelian_port_orders=[ab,ba],
 stable_repeated_exit_pair=stable, tail_word=W, tail_drift=drift, infinite_parity_tests=parity,
 dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in deps},
 scope='Exact classical ant. Graph and mirror equivalence hypotheses pass, rotor exit order fails. No growth, record occurrence, universal finite perturbation invariance, or capture theorem follows.')
(P/'ROTOR_EXCURSION_TRANSFER_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(fine_reads=len(events),algebra_cases=algebra_count,missing=missing,
                    max_second_packet=out['return_packets'][1]['max_reads'],parity_tests=parity,
                    first_repeated_edge=repeat,stable_pair=stable),indent=2))
