"""Direct ten-cell literal control: a proper center crossing need not raise beta.

No corpus generation, search, numerical cap, or claimed minimality occurs here.
"""

from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GEOMETRY_PATH = ROOT / "chronology_dcuv/literal_residual_geometry.json"
DATA = json.loads(GEOMETRY_PATH.read_text())
G = DATA["geometry"]
K = set(map(tuple, DATA["core"]))
WORD = (1, 1, 1, 0, 4)
SEED = {
    (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -1),
    (0, 0), (0, 1), (0, 2), (1, -1), (1, 0),
}
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


raw = "".join(G[a]["word"] for a in WORD)
program = raw + G[0]["marker"]
board = set(SEED)
head = (0, 0)
heading = 0
states = {0: (set(board), head, heading)}
required_initial = {}
seen = set()
for tick, turn in enumerate(program):
    black = head in board
    assert black == (turn == "L")
    if head not in seen:
        required_initial[head] = black
        seen.add(head)
    if black:
        board.remove(head)
    else:
        board.add(head)
    heading = (heading + (-1 if black else 1)) % 4
    head = add(head, DIRECTIONS[heading])
    states[tick + 1] = (set(board), head, heading)
assert {p for p, black in required_initial.items() if black} == SEED
assert len(raw) == 103 and states[len(raw)][1:] == ((2, -1), 1)

roots = sorted(SEED - K)
parents = list(range(len(roots)))
tokens = {p: {"root": i, "birth_packet": None, "birth_clock": None} for i, p in enumerate(roots)}


def find(i):
    while parents[i] != i:
        i = parents[i]
    return i


history = []
head = (0, 0)
heading = tick = clock = beta = mergers = 0
atomic_edges = []
for packet_index, a in enumerate(WORD):
    real_board, real_head, real_heading = states[tick]
    core = {add(head, rot(p, heading)) for p in K}
    assert (head, heading) == (real_head, real_heading)
    assert real_board == core | set(tokens)
    inputs = [add(head, rot(p, heading)) for p in G[a]["inputs"]]
    identities = [tokens.pop(p) for p in inputs]
    components = {find(t["root"]) for t in identities}
    increment = len(inputs) - len(components)
    merged = len(components) - 1
    beta += increment
    mergers += merged
    representative = min(components)
    for component in components:
        parents[component] = representative
    for slot in G[a]["outputs"]:
        p = add(head, rot(slot, heading))
        assert p not in tokens
        tokens[p] = {"root": representative, "birth_packet": packet_index, "birth_clock": clock}
    history.append({
        "packet_index": packet_index,
        "name": G[a]["name"],
        "entry_pose": [*head, heading],
        "entry_C_clock": clock,
        "input_cells": inputs,
        "input_identities": identities,
        "input_component_count": len(components),
        "beta_increment": increment,
        "component_mergers": merged,
    })
    base = G[a]["name"][0]
    for atom in [base] + ["C"] * G[a]["name"].count("C"):
        center_before = add(tuple(Fraction(v) for v in head), rot((Fraction(-1, 2), Fraction(-1, 2)), heading))
        step = {"D": (1, 1), "V": (1, 3), "U": (0, 4), "C": (0, 1)}[atom]
        head = add(head, rot(step, heading))
        heading = (heading - int(atom == "C")) % 4
        clock += int(atom == "C")
        center_after = add(tuple(Fraction(v) for v in head), rot((Fraction(-1, 2), Fraction(-1, 2)), heading))
        atomic_edges.append({"packet_index": packet_index, "atom": atom, "start": center_before, "end": center_after})
    tick += len(G[a]["word"])
    real_board, real_head, real_heading = states[tick]
    core = {add(head, rot(p, heading)) for p in K}
    assert (head, heading) == (real_head, real_heading)
    assert real_board == core | set(tokens)

assert beta == 0 and mergers == 1
assert all(row["beta_increment"] == 0 for row in history)
assert history[-1]["input_component_count"] == 2
assert history[-1]["input_cells"] == [(2, 0), (1, -1)]
assert history[-1]["input_identities"][0]["birth_packet"] == 0
assert history[-1]["input_identities"][1]["birth_packet"] is None

first = atomic_edges[0]
last = atomic_edges[-1]
assert first["atom"] == "D" and last["atom"] == "V"
assert first["start"] == (Fraction(-1, 2), Fraction(-1, 2))
assert first["end"] == (Fraction(1, 2), Fraction(1, 2))
assert last["start"] == (Fraction(-3, 2), Fraction(1, 2))
assert last["end"] == (Fraction(3, 2), Fraction(-1, 2))
intersection = tuple((a + b) / 2 for a, b in zip(first["start"], first["end"]))
assert intersection == tuple((a + b) / 2 for a, b in zip(last["start"], last["end"])) == (0, 0)
u = tuple(b - a for a, b in zip(first["start"], first["end"]))
v = tuple(b - a for a, b in zip(last["start"], last["end"]))
assert u[0] * v[1] - u[1] * v[0] == -4


def rational_json(value):
    if isinstance(value, Fraction):
        return int(value) if value.denominator == 1 else str(value)
    if isinstance(value, dict):
        return {k: rational_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [rational_json(v) for v in value]
    return value


result = {
    "status": "AUTHOR_ACTUAL_CENTER_CROSSING_WITH_BETA_ZERO_PASS",
    "scope": "A finite actual complete-eight factor, not a closed excursion or an unfunded record control.",
    "word": WORD,
    "names": [G[a]["name"] for a in WORD],
    "seed": sorted(SEED),
    "entry_mass": len(SEED),
    "raw_length": len(raw),
    "raw_plus_actual_marker_length": len(program),
    "raw_exit_pose": [*head, heading],
    "C_count": clock,
    "all_input_beta": beta,
    "all_input_component_mergers": mergers,
    "history": history,
    "atomic_center_chords": atomic_edges,
    "proper_crossing": {"first_edge_index": 0, "second_edge_index": len(atomic_edges) - 1, "point": intersection, "both_segment_parameters": "1/2", "cross_product": -4},
    "limitation": "The final V uses one descendant of the first DC and one different entry component. Thus a proper crossing need not raise beta, but this control does use a component merger. No theorem says all crossings require one.",
    "dependency_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GEOMETRY_PATH, Path(__file__).resolve())},
}
(ROOT / "chronology_dcuv/center_crossing_beta_zero_control.json").write_text(json.dumps(rational_json(result), indent=2) + "\n")
print(json.dumps({"names": result["names"], "mass": len(SEED), "beta": beta, "mergers": mergers, "crossing": [0, 0], "raw_length": len(raw)}))
