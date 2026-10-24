"""Independent inventory count, strict input parser, completion and hash audit.

The independent row-profile DP uses universal symmetric bounds instead of
the generating script's output-dependent backward bounds. It checks exact
set coverage by necessary membership, uniqueness, and equal cardinality.
"""
import collections
import argparse
import hashlib
import itertools
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / 'sources'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--results', nargs='+',
                    default=['conversion_ports_chronology_results.txt',
                             'conversion_ports_resume_results.txt'],
                    help='Result filenames under sources, or absolute paths. All IDs must occur exactly once.')
args = parser.parse_args()
std = json.loads((BASE / 'root/standard.json').read_text())
x = y = 0
h = std['heading']
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
odd = set()
for c in std['word']:
    odd.symmetric_difference_update([(x-y, x % 2)])
    h = (h + (1 if c == 'R' else 3)) % 4
    x, y = x + dx[h], y + dy[h]
assert (x, y, h) == (-2, -2, std['heading'])
U = {(c['key'][0] // 2, c['key'][1]) for c in std['classes']
     if len(c['stable_visits']) % 2}
assert U == odd and len(U) == 12
us = collections.Counter(s for s, r in U)
guard = {(s, r) for s in (-3, 7) for r in range(2)}
active = [(s, r) for s in range(-2, 7) for r in range(2)]
expected_outputs = {frozenset(guard)} | {
    frozenset(guard | set(c)) for c in itertools.combinations(active, 4)}
inventory = json.loads((SRC / 'conversion_ports_row_screen.json').read_text())
assert len(inventory) == 3061
assert {frozenset(map(tuple, c['V'])) for c in inventory} == expected_outputs
assert [c['case'] for c in inventory] == list(range(len(inventory)))
profiles = json.loads((SRC / 'conversion_ports_row_profiles.json').read_text())
assert [p['id'] for p in profiles] == list(range(len(profiles)))
by_case = collections.defaultdict(list)
for p in profiles:
    by_case[p['case']].append(p)
    assert set(map(tuple, p['U'])) == U
    assert p['V'] == inventory[p['case']]['V']
    assert p['bottom'] == -2 and p['top'] == 6
    es = p['crossings']
    assert len(es) == 8 and min(es) >= 0
    all_edges = [0] + es + [0]
    assert p['row_counts'] == [a+b for a, b in zip(all_edges, all_edges[1:])]
    assert p['period'] == 2*sum(es) > 0 and p['period'] % 4 == 0
    nonzero = [i for i, n in enumerate(es) if n]
    assert nonzero == list(range(min(nonzero), max(nonzero)+1))
    vs = collections.Counter(s for s, r in p['V'])
    assert es[0] == 1-vs[-2] and es[-1] == 1-vs[6]
    for s, a, b in zip(range(-2, 7), all_edges, all_edges[1:]):
        sign = 1 if s % 2 == 0 else -1
        d = vs[s] - us[s]
        corners = (3*b-a-sign*d, 3*a-b-sign*d)
        assert min(corners) >= 0 and all(c % 4 == 0 for c in corners)

# Independent DP: I at both extreme edges is at most one, |Delta_s|<=2,
# so I_next<=3*I_prev+2 in either direction gives these universal bounds.
universal = (1, 5, 17, 53, 53, 17, 5, 1)
dp_profiles = dp_max_period = 0
for item in inventory:
    case = item['case']
    rows = by_case[case]
    assert item['profiles'] == [p['id'] for p in rows]
    assert len({tuple(p['crossings']) for p in rows}) == len(rows)
    vs = collections.Counter(s for s, r in item['V'])
    mb, mt = 1-vs[-2], 1-vs[6]
    states = {(0, 0, False, False): 1} if min(mb, mt) >= 0 else {}
    for s, ub in zip(range(-2, 6), universal):
        d = vs[s]-us[s]
        sign = 1 if s % 2 == 0 else -1
        nxt_states = collections.defaultdict(int)
        for (a, total, began, ended), multiplicity in states.items():
            first = (3*(a+sign*d)) % 4
            for b in range(first, ub+1, 4):
                if ended and b:
                    continue
                if s == -2 and b != mb or s == 5 and b != mt:
                    continue
                cu, cl = 3*b-a-sign*d, 3*a-b-sign*d
                if min(cu, cl) < 0 or cu % 4 or cl % 4:
                    continue
                nxt_states[b, total+b, began or b > 0, ended or (began and b == 0)] += multiplicity
        states = nxt_states
    counts = collections.Counter()
    for (a, total, began, ended), n in states.items():
        d = vs[6]-us[6]
        if min(-a-d, 3*a-d) < 0 or (-a-d) % 4 or (3*a-d) % 4:
            continue
        if total > 0 and total % 2 == 0:
            counts[2*total] += n
    assert counts == collections.Counter(p['period'] for p in rows), (case, counts, rows)
    dp_profiles += sum(counts.values())
    dp_max_period = max(dp_max_period, max(counts, default=0))
assert dp_profiles == len(profiles)

# Parse all records strictly and compare every field against the enumerated input.
tokens = list(map(int, (SRC / 'conversion_ports_chronology_inputs.txt').read_text().split()))
at = 0
for p in profiles:
    assert tokens[at:at+4] == [p['id'], -2, 6, p['period']]
    at += 4
    V = set(map(tuple, p['V']))
    for s, n in zip(range(-2, 7), p['row_counts']):
        expected = [int((s, 0) in U), int((s, 1) in U),
                    int((s, 0) in V), int((s, 1) in V), n]
        assert tokens[at:at+5] == expected
        at += 5
assert at == len(tokens)

result_files = args.results
accepted = {}
trials = 0
elapsed = 0.0
for name in result_files:
    for line in (SRC / name).read_text().splitlines():
        fields = line.split()
        assert fields[0] == 'RESULT' and len(fields) == 10, line
        uid, state, period = int(fields[1]), fields[2], int(fields[3])
        assert uid not in accepted, ('duplicate', uid)
        assert state == 'complete', (uid, state)
        assert period == profiles[uid]['period']
        assert int(fields[8]) == 0
        accepted[uid] = name
        trials += int(fields[4])
        elapsed += float(fields[9])
assert set(accepted) == set(range(len(profiles)))
controls = json.loads((SRC / 'conversion_controls_audit.json').read_text())
assert {c['id'] for c in controls} == {-1, -2, -3}

files = ['conversion_chronology.cpp', 'conversion_chronology',
         'conversion_full_row_screen.py', 'conversion_ports_row_screen.json',
         'conversion_ports_row_profiles.json', 'conversion_ports_chronology_inputs.txt',
         'conversion_controls_and_verifier.py', 'conversion_controls_audit.json',
         'conversion_controls_results.txt', 'audit_negative_converter_coverage.py'] + result_files
hashes = {name: hashlib.sha256((SRC/name).read_bytes()).hexdigest() for name in files}
report = {'theorem': 'No same-sector (2,2) negative-mass converter of the standard wake confined to -3<=x-y<=7',
          'input_black_classes': sorted(U), 'labelled_outputs': len(inventory),
          'mass_4_outputs': 1, 'mass_8_outputs': 3060,
          'row_surviving_outputs': sum(bool(c['profiles']) for c in inventory),
          'row_profiles': len(profiles), 'independent_dp_profiles': dp_profiles,
          'max_period': dp_max_period, 'complete_chronology_records': len(accepted),
          'accepted_result_files': result_files,
          'timeouts_accepted': 0, 'solutions': 0, 'partial_checks': trials,
          'sum_reported_seconds': elapsed, 'controls': controls, 'sha256': hashes,
          'status': 'internally audited computer-assisted result; no external or formal review'}
(SRC / 'negative_converter_coverage_audit.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k: v for k, v in report.items() if k not in {'sha256', 'input_black_classes', 'controls'}}))
