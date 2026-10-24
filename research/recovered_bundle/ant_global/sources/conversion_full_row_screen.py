"""Independent full output inventory, without root's clocks or lane filters.

The two immutable guardrails consume four black classes. Negative mass change
is divisible by four, leaving mass 4 and 8, hence 1+binom(18,4) inventories.
Exact row-port bounds and proved cap charges provide finite enumeration.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PORTS_ONLY = '--ports-only' in sys.argv[1:]
PREFIX = 'conversion_ports' if PORTS_ONLY else 'conversion_full'
standard = json.loads((BASE / 'root/standard.json').read_text())
U = {(c['key'][0] // 2, c['key'][1]) for c in standard['classes']
     if len(c['stable_visits']) % 2}
us = collections.Counter(s for s, r in U)
guardrails = {(s, r) for s in (-3, 7) for r in range(2)}
active = [(s, r) for s in range(-2, 7) for r in range(2)]
profiles, summary = [], []
outputs = [guardrails] + [guardrails | set(c) for c in itertools.combinations(active, 4)]

for case_id, V in enumerate(outputs):
    vs = collections.Counter(s for s, r in V)
    delta = {s: vs[s] - us[s] for s in range(-2, 7)}
    m_bot, m_top = 1 - vs[-2], 1 - vs[6]
    sols = []
    if min(m_bot, m_top) >= 0:
        # Backward inequality: I_(s-1) <= 3 I_s - (-1)^s Delta_s.
        upper = {6: 0}
        for s in range(6, -3, -1):
            eps = 1 if s % 2 == 0 else -1
            upper[s - 1] = 3 * upper[s] - eps * delta[s]

        def visit(s, prev, edges, has_started=False, has_finished=False):
            if s == 6:
                if prev != m_top:
                    return
                crossing = {-3: 0, **dict(zip(range(-2, 6), edges)), 6: 0}
                period = 2 * sum(edges)
                if period <= 0 or period % 4:
                    return
                ns = {s: crossing[s - 1] + crossing[s] for s in range(-2, 7)}
                if not PORTS_ONLY and ns[-1] != 4 * m_bot - 1 + vs[-1]:
                    return
                if not PORTS_ONLY and ns[5] != 4 * m_top - 1 + vs[5]:
                    return
                db_num = 8 * m_bot - 3 + 4 * vs[-1] - vs[0] - ns[0]
                dt_num = 8 * m_top - 4 + 4 * vs[5] - vs[4] - ns[4]
                if not PORTS_ONLY and (db_num % 4 or dt_num % 4):
                    return
                db, dt = db_num // 4, dt_num // 4
                if not PORTS_ONLY and min(db, dt) < 0:
                    return
                if not PORTS_ONLY and ns[1] > 12 * m_bot - 5 + 8 * vs[-1] - 4 * vs[0] + vs[1] - 8 * db:
                    return
                if not PORTS_ONLY and ns[3] > 12 * m_top - 9 + 8 * vs[5] - 4 * vs[4] + vs[3] - 8 * dt:
                    return
                row_counts = [ns[s] for s in range(-2, 7)]
                profile = {'id': len(profiles), 'case': case_id,
                           'bottom': -2, 'top': 6, 'U': sorted(U), 'V': sorted(V),
                           'period': period, 'crossings': edges,
                           'D': [db, dt], 'M': [m_bot, m_top],
                           'row_counts': row_counts}
                profiles.append(profile)
                sols.append(profile['id'])
                return
            eps = 1 if s % 2 == 0 else -1
            ceiling = min(3 * prev - eps * delta[s], upper[s])
            for nxt in range(ceiling + 1):
                if has_finished and nxt:
                    continue
                cu = 3 * nxt - prev - eps * delta[s]
                cl = 3 * prev - nxt - eps * delta[s]
                if min(cu, cl) < 0 or cu % 4 or cl % 4:
                    continue
                if s == -2 and nxt != m_bot:
                    continue
                if s == 5 and nxt != m_top:
                    continue
                visit(s + 1, nxt, edges + [nxt], has_started or nxt > 0,
                      has_finished or (has_started and nxt == 0))

        if min(upper.values()) >= 0:
            visit(-2, 0, [])
    summary.append({'case': case_id, 'mass': len(V), 'V': sorted(V), 'profiles': sols})

(BASE / f'sources/{PREFIX}_row_profiles.json').write_text(json.dumps(profiles, indent=2) + '\n')
(BASE / f'sources/{PREFIX}_row_screen.json').write_text(json.dumps(summary, indent=2) + '\n')
with (BASE / f'sources/{PREFIX}_chronology_inputs.txt').open('w') as f:
    for case in profiles:
        u, v = set(map(tuple, case['U'])), set(map(tuple, case['V']))
        f.write(f"{case['id']} {case['bottom']} {case['top']} {case['period']}\n")
        for s, n in zip(range(case['bottom'], case['top'] + 1), case['row_counts']):
            f.write(' '.join(map(str, [int((s, 0) in u), int((s, 1) in u),
                                      int((s, 0) in v), int((s, 1) in v), n])) + '\n')
print(json.dumps({'candidates': len(outputs),
                  'survivors': sum(bool(s['profiles']) for s in summary),
                  'profiles': len(profiles),
                  'max_period': max((p['period'] for p in profiles), default=0),
                  'mass_counts': dict(collections.Counter(s['mass'] for s in summary if s['profiles']))}))
