"""Exact frontier and full-field one-bit audits for mass-four recurrence.

Reuses the already reconstructed canonical one-bit certificate. Nine ordinary
horizontal-arrival channels get complete post-impact half-plane/axis guards.
The exceptional phase 72 is recorded, not declared harmless.
"""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'ant_continuation'))
from ant_exact import (
    P, W, step, plan, multiple, canonical_source, certify_period, avoids_old_tail,
)


def cw(p):
    return p[1], -p[0]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def audit_frontier():
    B, p, h = set(), (0, 0), 0
    prefix_reads = set()
    for _ in range(9977):
        prefix_reads.add(p)
        p, h, _ = step(B, p, h)
    assert p == (-15, 10) and h == 3
    blank_cert = certify_period(B, p, h, W)
    assert blank_cert and tuple(blank_cert['drift']) == (-2, -2)
    core = {(p[0] + cw(q)[0], p[1] + cw(q)[1]) for q in P}
    assert core <= B and len(core) == 13
    history = B - core
    assert len(history) == 702
    phase_reads, phase_heads, end, end_h = plan(W, p, h)
    drift = sub(end, p)
    assert drift == (-2, -2) and end_h == h

    # For n >= depth_threshold, the first-read status of every phase is exact:
    # all possible earlier periodic occurrences and all prefix hits are covered.
    frontier = []
    depth_threshold = 0
    for i, q in enumerate(phase_reads):
        prior = []
        for j, r in enumerate(phase_reads):
            k = multiple(sub(r, q), drift)
            if k is not None and (k > 0 or k == 0 and j < i):
                prior.append(k)
        for r in prefix_reads:
            k = multiple(sub(r, q), drift)
            if k is not None and k >= 0:
                depth_threshold = max(depth_threshold, k + 1)
        if prior:
            depth_threshold = max(depth_threshold, min(prior))
        else:
            frontier.append({
                'phase': i, 'offset': sub(q, p), 'heading': phase_heads[i],
                'checkerboard': 1 if sum(q) % 2 == 0 else -1,
            })
    assert len(frontier) == 22
    horizontal = [a['phase'] for a in frontier if a['heading'] % 2]
    assert horizontal == [14, 28, 32, 38, 46, 56, 60, 62, 70, 72]
    return {
        'entry_time': 9977, 'entry_head': p, 'entry_heading': h,
        'blank_tail_certificate': blank_cert,
        'prefix_history_black_count': len(history),
        'prefix_history_z_range': [min(x + y for x, y in history),
                                   max(x + y for x, y in history)],
        'prefix_history_sha256': hashlib.sha256(repr(sorted(history)).encode()).hexdigest(),
        'stable_first_read_depth': depth_threshold,
        'frontier': frontier, 'horizontal_phases': horizontal,
    }


def audit_channel(r, source):
    N = source['thresholds'][r]
    rec = next(a for a in source['cases'] if a['n'] == N and a['r'] == r)
    B, p, h = canonical_source(N, r)
    impact = p
    B.symmetric_difference_update({impact})
    reads = set()
    for _ in range(rec['steps']):
        reads.add(p)
        p, h, _ = step(B, p, h)
    assert list(p) == rec['position'] and h == rec['heading']
    assert hashlib.sha256(repr(sorted(B)).encode()).hexdigest() == rec['field_sha256']
    word = W[rec['phase']:] + W[:rec['phase']]
    tail = certify_period(B, p, h, word)
    assert tail == {**rec['tail'], 'drift': tuple(rec['tail']['drift'])}
    assert avoids_old_tail(reads, p, h, word, N)
    phase_points, _, end, _ = plan(word, p, h)
    drift = cw(sub(end, p))
    offsets = [cw(sub(q, impact)) for q in phase_points]
    finite = [cw(sub(q, impact)) for q in reads]
    horizontal_hits = {x for x, y in finite if y == 0}
    vertical_hits = {y for x, y in finite if x == 0}
    for x, y in offsets:
        # Full exact rays, not a finite-period truncation.
        if (-y) % drift[1] == 0:
            k = (-y) // drift[1]
            if k >= 0:
                horizontal_hits.add(x + k * drift[0])
        if (-x) % drift[0] == 0:
            k = (-x) // drift[0]
            if k >= 0:
                vertical_hits.add(y + k * drift[1])
    z_upper = None
    if sum(drift) <= 0:
        z_upper = max(x + y for x, y in finite + offsets)
    return {
        'phase': r, 'canonical_age_threshold': N,
        'recovery_updates': rec['steps'],
        'recovery_radius': max(max(abs(x), abs(y)) for x, y in finite),
        'end_offset_from_impact': cw(sub(p, impact)),
        'end_heading': (h + 1) % 4, 'tail_phase': rec['phase'],
        'outgoing_drift': drift,
        'complete_field_tail_certificate': tail,
        'all_age_old_tail_guard': True,
        'postimpact_z_upper_offset': z_upper,
        'horizontal_axis_max_abs_displacement': max(map(abs, horizontal_hits), default=0),
        'vertical_axis_max_abs_displacement': max(map(abs, vertical_hits), default=0),
        'status': 'ordinary_guarded_exclusion' if r != 72 else 'exceptional_origin_return',
    }


def main():
    frontier = audit_frontier()
    source_path = ROOT / 'ant_continuation/one_bit_certificate_restored.json'
    source = json.loads(source_path.read_text())
    rows = [audit_channel(r, source) for r in frontier['horizontal_phases']]
    ordinary = [r for r in rows if r['phase'] != 72]
    assert len(ordinary) == 9
    assert all(sum(r['outgoing_drift']) <= 0 for r in ordinary)
    result = {
        'status': 'PASS', 'scope': 'Nine ordinary channels excluded by exact all-future guards; phase72 remains.',
        'source_certificate_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
        'frontier': frontier, 'channels': rows,
        'uniform_ordinary_guards': {
            'z_upper_offset': max(r['postimpact_z_upper_offset'] for r in ordinary),
            'horizontal_axis_max_abs_displacement':
                max(r['horizontal_axis_max_abs_displacement'] for r in ordinary),
            'vertical_axis_max_abs_displacement':
                max(r['vertical_axis_max_abs_displacement'] for r in ordinary),
        },
    }
    Path(__file__).with_name('mass4_first_collision_audit.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps({
        'status': result['status'],
        'stable_first_read_depth': frontier['stable_first_read_depth'],
        'prefix_history_z_range': frontier['prefix_history_z_range'],
        'horizontal_phases': frontier['horizontal_phases'],
        'uniform_ordinary_guards': result['uniform_ordinary_guards'],
        'channels': [
            {k: r[k] for k in ('phase', 'canonical_age_threshold', 'recovery_updates',
                               'outgoing_drift', 'postimpact_z_upper_offset')}
            for r in rows],
    }, indent=2))


if __name__ == '__main__':
    main()
