"""Exact geometric guards for the proposed mass-four exceptional chain.

This checker proves affine read-set bounds of the prescribed word template.
It does not itself prove that the template is the actual ant trajectory; that
is the independent full-field affine certificate's obligation. All extrema
are derived over every integer n >= N, with no sampling of large n.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ant_continuation"))
from ant_exact import W, plan, PHASES, canonical_source, certify_period


def value(q, normal):
    return q[0] * normal[0] + q[1] * normal[1]


def rotated(p, turns):
    for _ in range(turns % 4):
        p = p[1], -p[0]
    return p


def motion_extrema(template, minimum=200):
    # p = coefficient * n + constant; headings are parameter-independent.
    coefficient, constant, heading = (0, 0), (0, 0), 0
    # Each coordinate extremum of a finite arithmetic segment is at an end.
    affine_reads = []
    boundaries = []
    for number, segment in enumerate(template["segments"]):
        points, _, end, end_h = plan(segment["word"], (0, 0), heading)
        if segment["type"] == "finite":
            affine_reads.extend((coefficient,
                                 (constant[0] + q[0], constant[1] + q[1]))
                                for q in points)
            constant = constant[0] + end[0], constant[1] + end[1]
        else:
            assert end_h == heading
            a, b = segment["count"]
            assert a >= 0 and a * minimum + b >= 1
            for q in points:
                # First and last repetition. This is exact for every linear
                # functional, including when the repetition count is affine.
                affine_reads.append((coefficient,
                                     (constant[0] + q[0], constant[1] + q[1])))
                affine_reads.append(((coefficient[0] + a * end[0],
                                      coefficient[1] + a * end[1]),
                                     (constant[0] + q[0] + (b - 1) * end[0],
                                      constant[1] + q[1] + (b - 1) * end[1])))
            coefficient = coefficient[0] + a * end[0], coefficient[1] + a * end[1]
            constant = constant[0] + b * end[0], constant[1] + b * end[1]
        heading = end_h
        if number in (4, 8):
            extrema = {}
            for name, normal in (("u", (1, -1)), ("z", (1, 1))):
                terms = [(value(c, normal), value(k, normal)) for c, k in affine_reads]
                low = None if any(a < 0 for a, b in terms) else min(a * minimum + b for a, b in terms)
                high = None if any(a > 0 for a, b in terms) else max(a * minimum + b for a, b in terms)
                extrema[name] = {"minimum": low, "maximum": high}
            assert coefficient == (0, 0)
            tail_word = template["segments"][number + 1]["word"]
            phase = PHASES[tail_word]
            skip = (104 - phase) % 104
            _, _, core, core_heading = plan(tail_word[:skip], constant, heading)
            phase_points, phase_heads, end, end_heading = plan(W, core, core_heading)
            assert end_heading == core_heading
            drift = (end[0] - core[0], end[1] - core[1])
            phase72 = phase_points[72]
            first_period, _, _, _ = plan(tail_word, constant, heading)
            whole_future_bounds = {}
            for name, normal in (("u", (1, -1)), ("z", (1, 1))):
                low = extrema[name]["minimum"]
                high = extrema[name]["maximum"]
                change = value(drift, normal)
                whole_future_bounds[name] = {
                    "minimum": None if low is None or change < 0 else
                        min(low, min(value(q, normal) for q in first_period)),
                    "maximum": None if high is None or change > 0 else
                        max(high, max(value(q, normal) for q in first_period)),
                }
            clean, clean_p, clean_h = canonical_source(0, phase)
            turns = (heading - clean_h) % 4
            rp = rotated(clean_p, turns)
            shift = constant[0] - rp[0], constant[1] - rp[1]
            clean = {(rotated(q, turns)[0] + shift[0],
                      rotated(q, turns)[1] + shift[1]) for q in clean}
            cert = certify_period(clean, constant, heading, tail_word)
            assert cert and cert["drift"] == drift
            clean_u = [x - y for x, y in clean]
            first_u = [x - y for x, y in first_period]
            if number == 4:
                # Initial q has u=-19 and all reads have -82<=u<=58.
                archive_low = min(extrema["u"]["minimum"], -19, min(clean_u))
                archive_high = max(extrema["u"]["maximum"], -19, max(clean_u))
                guard_periods = max(0, (max(first_u) - archive_low) // 4 + 1)
                assert max(first_u) - 4 * guard_periods < archive_low
            else:
                # Initial q has u=-19, initial a has u=-74-4n.
                archive_low = None
                archive_high = max(extrema["u"]["maximum"], -19,
                                   -74 - 4 * minimum, max(clean_u))
                guard_periods = max(0, (archive_high - min(first_u)) // 4 + 1)
                assert min(first_u) + 4 * guard_periods > archive_high
            a, b = template["segments"][number + 1]["count"]
            assert a * minimum + b >= guard_periods
            guard_reads = [(q[0] + k * drift[0], q[1] + k * drift[1])
                           for q in first_period for k in range(guard_periods)]
            guard_radius = max(max(abs(x), abs(y)) for x, y in guard_reads)
            assert guard_radius < 2 * minimum - 33
            boundaries.append({
                "segment": number,
                "pose": [constant, heading],
                "all_n_prefix_read_bounds": extrema,
                "parent_complete_future_read_bounds": whole_future_bounds,
                "tail_word_phase": phase,
                "updates_to_W0": skip,
                "W0_pose": [core, core_heading],
                "tail_drift": drift,
                "phase72_ray_base": phase72,
                "phase72_z": sum(phase72),
                "phase72_u": phase72[0] - phase72[1],
                "phase72_heading": phase_heads[72],
                "placed_clean_field": sorted(clean),
                "clean_field_u_bounds": [min(clean_u), max(clean_u)],
                "clean_field_infinite_tail_certificate": cert,
                "residual_archive_u_bounds": [archive_low, archive_high],
                "fixed_periods_sufficient_to_guard_archive": guard_periods,
                "fixed_guard_read_radius": guard_radius,
            })
    return boundaries


def main():
    template_path = ROOT / "ant_continuation2/planar_structure/exceptional_rectangle_template.json"
    template = json.loads(template_path.read_text())
    boundaries = motion_extrema(template)
    ordinary = json.loads(Path(__file__).with_name("mass4_first_collision_audit.json").read_text())
    guards = ordinary["uniform_ordinary_guards"]
    assert guards == {"z_upper_offset": 58,
                      "horizontal_axis_max_abs_displacement": 31,
                      "vertical_axis_max_abs_displacement": 34}
    assert rotated((-2, -2), 1) == (-2, 2)
    assert rotated((-2, -2), 3) == (2, -2)
    # Algebraic covariance of the bounding normals and both coordinate axes.
    for q in [(1, 0), (0, 1)]:
        a, c = rotated(q, 1), rotated(q, 3)
        assert a[0] - a[1] == q[0] + q[1]
        assert c[0] - c[1] == -(q[0] + q[1])
    result = {
        "status": "PASS: exact all-parameter motion guards; actual color feasibility is a separate certificate",
        "minimum_parameter": 200,
        "prefixes": boundaries,
        "rotated_ordinary_guards": {
            "NW": {"normal": "u", "inequality": "u(read) <= u(impact) + 58",
                   "horizontal_axis_absolute_bound": 34, "vertical_axis_absolute_bound": 31},
            "SE": {"normal": "u", "inequality": "u(read) >= u(impact) - 58",
                   "horizontal_axis_absolute_bound": 34, "vertical_axis_absolute_bound": 31},
        },
    }
    Path(__file__).with_name("mass4_later_collision_guards_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
