"""Independent literal audit of the parametric exceptional rectangle certificate.

The affine proof covers all n >= 200. This separate complex-coordinate checker
audits that proof's conventions and complete fields at three selected n. It also
checks each supplied infinite tail by exact parity boundaries, without calling
the affine engine or its ant simulator.
"""
from pathlib import Path
from collections import Counter
import hashlib
import gzip
import json
from independent_audit import update, coords

HERE = Path(__file__).resolve().parent


def integer_multiple(v, d):
    vx, vy = coords(v)
    dx, dy = coords(d)
    a, b = (vx, dx) if dx else (vy, dy)
    if a % b:
        return None
    k = a // b
    return k if (vx, vy) == (k*dx, k*dy) else None


def permanent_word(B, p, d, word):
    start, old_d = p, d
    required, odd = {}, set()
    for letter in word:
        bit = (letter == 'L') ^ (p in odd)
        assert p not in required or required[p] == bit
        required[p] = bit
        odd.symmetric_difference_update({p})
        d *= 1j if letter == 'L' else -1j
        p += d
    drift = p - start
    assert d == old_d and drift
    comparisons = 0
    for q, initial_bit in required.items():
        boundaries = {0} if initial_bit else set()
        for cell in B:
            k = integer_multiple(cell-q, drift)
            if k is not None and k >= 0:
                boundaries.symmetric_difference_update({k, k+1})
        for cell in odd:
            k = integer_multiple(cell-q, drift)
            if k is not None and k > 0:
                boundaries.symmetric_difference_update({k})
        assert not boundaries, (coords(q), boundaries)
        comparisons += 1
    return {'drift': coords(drift), 'distinct_start_color_constraints': comparisons,
            'net_odd_cells_per_period': len(odd)}


def main():
    data = json.loads((HERE/'planar_structure/exceptional_rectangle_template.json').read_text())
    snapshots = json.loads(gzip.decompress((HERE/'planar_structure/exceptional_affine_fields.json.gz').read_bytes()))
    symbolic_fields = {row['segment']: row for row in snapshots['snapshots']}
    B, p, d = set(), 0j, 1j
    for _ in range(9977):
        p, d = update(B, p, d)
    standard = ''
    for _ in range(104):
        standard += 'L' if p in B else 'R'
        p, d = update(B, p, d)
    rotations = {standard[k:]+standard[:k] for k in range(104)}
    for segment in data['segments']:
        if segment['type'] == 'periods':
            assert len(segment['word']) == 104 and segment['word'] in rotations
    assert len(data['infinite_tail_word']) == 104 and data['infinite_tail_word'] in rotations
    results = []
    for n in (200, 201, 500):
        q = complex(-33-2*n, -14-2*n)
        a = complex(-33-2*n, 41+2*n)
        c = complex(8+2*n, -14-2*n)
        remote = complex(8+2*n, 41+2*n)
        B = {q, a, c, remote}
        p, d, time = 0j, 1j, 0
        contacts = {}
        stages = []
        for index, segment in enumerate(data['segments']):
            repeats = 1 if segment['type'] == 'finite' else segment['count'][0]*n+segment['count'][1]
            assert repeats > 0
            for _ in range(repeats):
                for expected in segment['word']:
                    assert p != remote
                    if p in (q, a, c) and p not in contacts:
                        contacts[p] = time
                    assert ('L' if p in B else 'R') == expected, (n, time, coords(p))
                    p, d = update(B, p, d)
                    time += 1
            stages.append({'segment': index, 'time': time, 'position': coords(p),
                           'heading_vector': coords(d), 'mass': len(B)})
            if index in symbolic_fields:
                state = symbolic_fields[index]
                evaluate_point = lambda point: complex(point[0][0]*n+point[0][1], point[1][0]*n+point[1][1])
                expanded = set()
                for point in state['point_terms']:
                    expanded.symmetric_difference_update({evaluate_point(point)})
                for base, drift, count, label in state['ray_terms']:
                    first = evaluate_point(base)
                    direction = complex(*drift)
                    length = count[0]*n+count[1]
                    assert length > 0
                    for k in range(length):
                        expanded.symmetric_difference_update({first+k*direction})
                assert expanded == B, (n, index, len(expanded ^ B))
                stages[-1]['complete_symbolic_field_matches_literal_field'] = True
        assert time == 728*n+200304
        assert p == complex(-2*n-58, 2*n+98) and d == 1j
        cert = permanent_word(B, p, d, data['infinite_tail_word'])
        assert cert['drift'] == (-2, 2)
        # The future tail's translated read set must also miss the fourth bit.
        tail_p, tail_d = p, d
        for letter in data['infinite_tail_word']:
            k = integer_multiple(remote-tail_p, complex(-2, 2))
            assert k is None or k < 0
            tail_d *= 1j if letter == 'L' else -1j
            tail_p += tail_d
        canonical = json.dumps(sorted(coords(cell) for cell in B), separators=(',', ':')).encode()
        row = {'n': n, 'time': time, 'position': coords(p), 'heading': 'N',
               'mass': len(B), 'field_sha256': hashlib.sha256(canonical).hexdigest(),
               'first_contacts': [{'point': coords(cell), 'time': t} for cell, t in contacts.items()],
               'fourth_corner_untouched': True, 'infinite_tail': cert, 'stages': stages}
        results.append(row)
        print(json.dumps({k: v for k, v in row.items() if k != 'stages'}), flush=True)
    out = {'status': 'PASS', 'scope': 'Independent finite-parameter audit plus exact supplied-tail proof',
           'all_parameter_proof': 'planar_structure/certify_exceptional_rectangle.py',
           'literal_updates': sum(row['time'] for row in results),
           'complete_symbolic_field_comparisons': 3*len(results), 'cases': results}
    (HERE/'independent_rectangle_audit.json').write_text(json.dumps(out, indent=2)+'\n')


if __name__ == '__main__':
    main()
