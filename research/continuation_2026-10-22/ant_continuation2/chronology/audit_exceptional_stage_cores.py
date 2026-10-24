"""Independent stage-core normalization and XOR-archive audit.

The all-parameter rectangle checker supplies the prescribed-prefix proof.
This checker independently reconstructs the exact XOR field after those
words, checks each omitted input is unread, and proves that the full residual
archive vanishes on EVERY clean incoming future ray. No finite simulation is
used to infer permanence, and no old black cell is silently discarded.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / 'ant_continuation'))
sys.path.insert(0, str(ROOT / 'ant_continuation' / 'wake_clock'))
sys.path.insert(0, str(ROOT / 'ant_continuation2' / 'planar_structure'))
from ant_exact import P, W, PHASES, plan, step, certify_period
import certify_four_scatterer_prefix as A
import certify_exceptional_rectangle as C


def rotate(p, j):
    x, y = p
    for _ in range(j % 4):
        x, y = y, -x
    return x, y


def concrete(p):
    assert p[0][0] == p[1][0] == 0
    return p[0][1], p[1][1]


def clone(field):
    other = A.Field(field.points)
    other.rays = list(field.rays)
    return other


def normalized_core(word, p, h):
    r = PHASES[word]
    black, cp, ch = set(P), (0, 0), 2
    for i in range(r):
        cp, ch, letter = step(black, cp, ch)
        assert letter == W[i]
    j = (h - ch) % 4
    shift = rotate(cp, j)
    origin = p[0] - shift[0], p[1] - shift[1]
    core = {(origin[0] + rotate(q, j)[0], origin[1] + rotate(q, j)[1])
            for q in black}
    cert = certify_period(core, p, h, word)
    assert cert is not None
    return core, r, j, origin, cert


def verify_archive(field, base, heading, word, omitted, reads, rays):
    # Removing an unread initial bit is exact first-difference coupling.
    for bit in omitted:
        for p in reads:
            assert p != bit and A.no_point_collision(p, bit)
        for b, drift, count in rays:
            assert not A.ray_membership(bit, b, drift, count)
    source = clone(field)
    source.add_points(omitted)
    p = concrete(base)
    core, phase, rotation, origin, clean_cert = normalized_core(word, p, heading)
    archive = clone(source)
    archive.add_points(A.point(*q) for q in core)
    data = A.word_data(word, heading)
    # In this check the required archive color is zero and it makes no flips.
    zero_data = ({q: False for q in data[0]}, set(), data[2], data[3])
    guarded = C.verify_infinite_period(archive, zero_data, base)
    source_tail = C.verify_infinite_period(source, data, base)
    bounds = C.affine_coordinate_bounds(archive, 'u')

    # Align to phase zero and use literally the supplied thirteen-cell P.
    offset = (-phase) % 104
    short = A.word_data(word[:offset], heading)
    source0 = clone(source)
    source0.add_points(A.translate_local(q, base, 0) for q in short[1])
    base0 = A.translate_local(short[2], base, 0)
    p0, h0 = concrete(base0), short[3]
    j0 = (h0 - 2) % 4
    core0 = {(p0[0] + rotate(q, j0)[0], p0[1] + rotate(q, j0)[1]) for q in P}
    assert len(core0) == 13
    assert certify_period(core0, p0, h0, W) is not None
    archive0 = clone(source0)
    archive0.add_points(A.point(*q) for q in core0)
    data0 = A.word_data(W, h0)
    zero0 = ({q: False for q in data0[0]}, set(), data0[2], data0[3])
    C.verify_infinite_period(archive0, zero0, base0)
    bounds0 = C.affine_coordinate_bounds(archive0, 'u')

    # Exact phase-72 fresh ray of this newly established standard tail.
    first72 = (72 - phase) % 104
    _, _, impact72, impact_heading = plan(word[:first72], p, heading)
    return {
        'stage_pose': [p, heading], 'word_phase': phase,
        'canonical_rotation_clockwise': rotation, 'canonical_origin': origin,
        'phase_core_cells': sorted(core), 'clean_core_certificate': clean_cert,
        'full_source_tail_certificate': source_tail,
        'archive_zero_on_all_clean_future_rays': guarded,
        'archive_u_bound': bounds,
        'updates_to_phase_zero': offset, 'phase_zero_pose': [p0, h0],
        'phase_zero_thirteen_cell_core': sorted(core0),
        'phase_zero_archive_u_bound': bounds0,
        'first_phase72_offset': first72, 'phase72_ray_origin': impact72,
        'phase72_heading': impact_heading,
        'phase72_ray_drift': data[2],
        'unread_input_count': len(omitted),
    }


def main():
    folder = ROOT / 'ant_continuation2' / 'planar_structure'
    template_path = folder / 'exceptional_rectangle_template.json'
    certificate_path = folder / 'exceptional_rectangle_affine_certificate.json'
    template = json.loads(template_path.read_text())
    certificate = json.loads(certificate_path.read_text())
    assert certificate['status'] == 'proved by exact affine-field read verification'
    assert certificate['parameter_minimum'] == template['base'] == 200
    A.LOW = 200
    A.no_point_collision = C.fast_no_point_collision
    for key in A.STATS:
        A.STATS[key] = 0
    q = ((-2, -33), (-2, -14))
    a = ((-2, -33), (2, 41))
    c = ((2, 8), (-2, -14))
    d = ((2, 8), (2, 41))
    field = A.Field({q, a, c, d})
    base, heading, elapsed = A.point(0, 0), 0, A.ZERO
    reads, rays = [], []
    output = []
    for i, segment in enumerate(template['segments'][:9]):
        data = A.word_data(segment['word'], heading)
        required, odd, drift, end_heading = data
        if segment['type'] == 'finite':
            reads.extend(A.translate_local(p, base, 0) for p in required)
            field.add_points(A.translate_local(p, base, 0) for p in odd)
            base = A.translate_local(drift, base, 0)
            elapsed = A.add(elapsed, (0, len(segment['word'])))
        else:
            count = tuple(segment['count'])
            assert A.nonneg(A.sub(count, A.ONE))
            assert end_heading == heading
            rays.extend((A.translate_local(p, base, 0), drift, count) for p in required)
            field.add_rays((A.translate_local(p, base, 0) for p in odd),
                           drift, count, 'independent-stage' + str(i))
            base = A.padd(base, (A.scale(count, drift[0]), A.scale(count, drift[1])))
            elapsed = A.add(elapsed, A.scale(count, 104))
        heading = end_heading
        rec = certificate['segments'][i]
        assert json.loads(json.dumps(base)) == rec['end']
        assert list(elapsed) == rec['time'] and heading == rec['heading']
        assert len(field.points) == rec['field_point_terms']
        assert len(field.rays) == rec['field_ray_terms']
        if i in (4, 8):
            omitted = (a, c, d) if i == 4 else (c, d)
            audit = verify_archive(field, base, heading,
                                   template['segments'][i + 1]['word'],
                                   omitted, reads, rays)
            audit.update({'segment': i, 'elapsed': elapsed})
            output.append(audit)
    assert output[0]['archive_u_bound']['lower'] == -82
    assert output[0]['archive_u_bound']['upper'] == 58
    assert output[1]['archive_u_bound']['upper'] <= 98
    assert output[0]['phase_zero_archive_u_bound']['lower'] == -82
    assert output[1]['phase_zero_archive_u_bound']['upper'] <= 98
    report = {
        'status': 'exact affine XOR-archive and clean-core checks passed',
        'parameter_minimum': 200,
        'scope': 'normalization audit conditional on the separate exact prescribed-prefix certificate',
        'template_sha256': hashlib.sha256(template_path.read_bytes()).hexdigest(),
        'prefix_certificate_sha256': hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
        'stages': output, 'statistics': dict(A.STATS),
    }
    (HERE / 'exceptional_stage_core_audit.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'stages'}, indent=2))
    for row in output:
        print(json.dumps({k: v for k, v in row.items()
                          if k not in ('phase_core_cells', 'phase_zero_thirteen_cell_core')}, indent=2))


if __name__ == '__main__':
    main()
