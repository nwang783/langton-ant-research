"""Independent adversarial controls for the exact symbolic proof kernels.

These are implementation controls, not substitutes for the kernel's analytic
soundness argument or for the all-parameter rectangle proof.
"""
from pathlib import Path
import json
import random
import sys

ROOT = Path(__file__).resolve().parent / "certificate_replay"
sys.path[:0] = [str(ROOT / "ant_continuation"),
               str(ROOT / "ant_continuation" / "wake_clock"),
               str(ROOT / "ant_continuation2" / "planar_structure")]
import ant_exact as E
import certify_four_scatterer_prefix as A
import certify_exceptional_rectangle as C

A.LOW = 200
A.no_point_collision = C.fast_no_point_collision
passed = []

def rejected(label, operation):
    try:
        operation()
    except (AssertionError, ValueError):
        passed.append(label)
        return
    raise AssertionError(("damaged input was accepted", label))

def field(cells):
    return A.Field({A.point(*p) for p in cells})

data = A.word_data(E.W, 2)
base = A.point(0, 0)
C.verify_infinite_period(field(E.P), data, base)
passed.append("canonical exact infinite tail accepted")
A.apply_periods(field(E.P), data, base, 0, (1, 0), "all n periods")
passed.append("all n >= 200 canonical finite repetitions accepted")

rejected("wrong current bit rejected", lambda:
    C.verify_infinite_period(field(E.P ^ {(0, 0)}), data, base))
far = 10**60
rejected("blocker 10^60 periods ahead rejected", lambda:
    C.verify_infinite_period(field(E.P ^ {(2*far, -2*far)}), data, base))
C.verify_infinite_period(field(E.P | {(far, 0)}), data, base)
passed.append("off-ray remote marker accepted")

# A point touching a tested point only at n = 10^60 must abort, not be
# accepted merely because it is absent at n = LOW.
rejected("isolated affine point collision at 10^60 rejected", lambda:
    A.no_point_collision(A.point(0, 0), ((1, -far), (0, 0))))
rejected("isolated affine ray incidence at 10^60 rejected", lambda:
    A.line_coordinate(((1, -far), (0, 0)), (2, -2)))
rejected("range membership crossing at 10^60 rejected", lambda:
    A.in_range((1, -far), (1, 1)))
rejected("nonintegral parameter residue rejected", lambda:
    A.integer_affine((1, 0), 2))

def concrete(p, n):
    return tuple(a*n+b for a, b in p)

def ray_points(base, drift, count, n):
    b = concrete(base, n)
    length = count[0]*n+count[1]
    assert length >= 1
    return {(b[0]+k*drift[0], b[1]+k*drift[1]) for k in range(length)}

# Compare accepted ray-intersection intervals with a literal set calculation.
# Small random coefficients sometimes cause the conservative symbolic checker
# to refuse an instance. Refusal is safe; only accepted instances are compared.
rng = random.Random(743029)
accepted = rejected_cases = comparisons = 0
drifts = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
for _ in range(1000):
    q = tuple((rng.randrange(-2,3), rng.randrange(-12,13)) for _ in range(2))
    b = tuple((rng.randrange(-2,3), rng.randrange(-12,13)) for _ in range(2))
    drift, old_drift = rng.choice(drifts), rng.choice(drifts)
    M = rng.randrange(0,2), rng.randrange(1,8)
    N = rng.randrange(0,2), rng.randrange(1,8)
    try:
        interval = A.previous_ray_interval(q, drift, b, old_drift, M, N)
    except AssertionError:
        rejected_cases += 1
        continue
    accepted += 1
    for n in (200,201,231,400):
        points = ray_points(b, old_drift, M, n)
        qn = concrete(q,n)
        expected = {k for k in range(N[0]*n+N[1])
                    if (qn[0]+k*drift[0],qn[1]+k*drift[1]) in points}
        if interval is None:
            actual = set()
        else:
            lo, hi = interval
            actual = set(range(lo[0]*n+lo[1],hi[0]*n+hi[1]+1))
        assert actual == expected, (q,b,drift,old_drift,M,N,n,interval)
        comparisons += 1

result = {"status":"PASS", "negative_and_positive_controls":passed,
          "ray_interval_random_cases_accepted":accepted,
          "conservative_refusals":rejected_cases,
          "literal_interval_comparisons":comparisons,
          "scope":"Implementation controls only; all-parameter proof uses the audited exact algebra."}
Path(__file__).with_name("auditor_negative_controls.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
