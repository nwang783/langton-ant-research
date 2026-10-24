"""Reconstruct the finite geometry behind the atomic turning-number lemma.

This is a finite identity checker, not a path search or a no-return checker.
The mathematical note supplies the elementary simple-polygon argument.
"""

from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GEOMETRY_PATH = ROOT / "chronology_dcuv/literal_residual_geometry.json"
NONRETURN_PATH = ROOT / "atomic_common_4C_frozen_20261023_1344/manifest.json"
GEOMETRY = json.loads(GEOMETRY_PATH.read_text())["geometry"]
HEAD_STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))
IDS = (0, 1, 4, 5, 6, 7, 8, 9)


def rot(point, heading):
    x, y = point
    return ((x, y), (y, -x), (-x, -y), (-y, x))[heading % 4]


def raw_endpoint(word):
    x = y = heading = 0
    for turn in word:
        heading = (heading + (-1 if turn == "L" else 1)) % 4
        dx, dy = HEAD_STEPS[heading]
        x += dx
        y += dy
    return x, y, heading


def center_step(endpoint):
    x, y, heading = endpoint
    # Twice the center correction is (-1, -1), so all checks stay integral.
    cx, cy = rot((-1, -1), heading)
    twice_step = (2 * x + cx + 1, 2 * y + cy + 1)
    assert all(v % 2 == 0 for v in twice_step)
    return tuple(v // 2 for v in twice_step)


c_word = GEOMETRY[1]["word"][len(GEOMETRY[0]["word"]):]
words = {
    "D": GEOMETRY[0]["word"],
    "V": GEOMETRY[4]["word"],
    "U": GEOMETRY[7]["word"],
    "C": c_word,
}
expected = {"D": (1, 1), "V": (1, 3), "U": (0, 4), "C": (1, 1)}
atoms = {}
for name, word in words.items():
    endpoint = raw_endpoint(word)
    step = center_step(endpoint)
    assert step == expected[name]
    assert endpoint[2] == (3 if name == "C" else 0)
    atoms[name] = {
        "raw_word": word,
        "raw_endpoint": endpoint,
        "center_step": step,
        "C_increment": int(name == "C"),
    }

for packet_id in IDS:
    item = GEOMETRY[packet_id]
    base = "D" if packet_id in (0, 1) else "V" if packet_id in (4, 5, 6) else "U"
    c_count = item["name"].count("C")
    assert item["word"] == words[base] + c_word * c_count
    assert raw_endpoint(item["word"]) == tuple(item["endpoint"])

transitions = []
for before, before_data in atoms.items():
    for after, after_data in atoms.items():
        v = before_data["center_step"]
        w = rot(after_data["center_step"], 3 if before == "C" else 0)
        cross = v[0] * w[1] - v[1] * w[0]
        dot = v[0] * w[0] + v[1] * w[1]
        if before == "C":
            assert cross > 0 and dot <= 0
            turn_interval = "[pi/2, 3*pi/4]"
            turn_formula = "3*pi/4 - alpha(after)"
        else:
            assert dot > 0
            # The algebraic alpha values lie in [0, pi/4].
            assert abs(cross) <= dot
            turn_interval = "[-pi/4, pi/4]"
            turn_formula = "alpha(before) - alpha(after)"
        transitions.append({
            "before": before,
            "after": after,
            "before_vector": v,
            "after_vector_in_before_frame": w,
            "cross_product": cross,
            "dot_product": dot,
            "principal_turn_interval": turn_interval,
            "principal_turn_formula": turn_formula,
        })

assert len(transitions) == 16
result = {
    "status": "AUTHOR_ATOMIC_CENTER_TURNING_IDENTITY_PASS",
    "scope": (
        "Actual atomic cuts inside a complete recurrent-eight factor. "
        "For a closed full-pose excursion, center-polygon turning number is C_count/4. "
        "A simple center polygon would force C_count=4, excluded by the signed atomic "
        "nonreturn theorem. Auxiliary chord crossings are not literal ant collisions."
    ),
    "center_correction": ["-1/2", "-1/2"],
    "angle_offsets": {"D": "pi/4", "V": "atan(1/3)", "U": "0", "C": "pi/4"},
    "atoms": atoms,
    "all_16_adjacent_atom_transitions": transitions,
    "dependency_hashes": {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (GEOMETRY_PATH, NONRETURN_PATH, Path(__file__).resolve())
    },
}
output = ROOT / "chronology_dcuv/atomic_center_turning.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"atomic_steps": expected, "adjacent_transitions": len(transitions), "status": result["status"]}))
