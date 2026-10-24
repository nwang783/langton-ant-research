"""All n3 canonical nonproper contacts reduce to a V-family -> plain D gate.

Use exact old-core/retired-input age cuts, existing clauses and two literal controls.
No path generation or higher counted threshold.
"""

from collections import Counter
from fractions import Fraction as F
from math import ceil, floor
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GP = ROOT / "chronology_dcuv/literal_residual_geometry.json"
CP = ROOT / "chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv"
HP = ROOT / "chronology_dcuv/protected_patch2.tsv"
AP = ROOT / "atomic_common_4C_frozen_20261023_1344/manifest.json"
JP = ROOT / "chronology_dcuv/counted_input_age_rules_complete.json"
DATA = json.loads(GP.read_text())
G = DATA["geometry"]
K = set(map(tuple, DATA["core"]))
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
NEW = {a: i for i, a in enumerate(IDS)}
COUNTED = {tuple(map(int, line.split()[:8])) for line in CP.read_text().splitlines()}
HB = {tuple(map(int, line.split()[:7])) for line in HP.read_text().splitlines()}
VECTORS = {"D": (1, 1), "C": (1, 1), "V": (1, 3), "U": (0, 4)}
CENTER = (F(-1, 2), F(-1, 2))
HEAD_STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def base(a):
    return 0 if G[a]["name"][0] == "D" else 4 if G[a]["name"][0] == "V" else 7




def literal_control(word):
    raw = "".join(G[a]["word"] for a in word)
    colors, initial = {}, {}
    p, h = (0, 0), 0
    for tick, turn in enumerate(raw + G[0]["marker"]):
        black = turn == "L"
        assert p not in colors or colors[p] == black
        if p not in colors:
            initial[p] = black
        colors[p] = not black
        h = (h + (-1 if black else 1)) % 4
        p = add(p, HEAD_STEPS[h])
    seed = {p for p, black in initial.items() if black}
    assert K <= seed
    board, p, h, clock = set(seed), (0, 0), 0, 0
    identities = {q: {"kind": "entry", "cell": q} for q in seed - K}
    boundaries, edges = [], []
    for packet_index, source in enumerate(word):
        old_pose, old_clock = [*p, h], clock
        core = {add(p, rot(q, h)) for q in K}
        assert core <= board and set(identities) == board - core
        consumed = []
        for inp in G[source]["inputs"]:
            cell = add(p, rot(inp, h))
            assert cell in identities
            consumed.append({"cell": cell, "input": inp, "identity": identities.pop(cell)})
        outputs = [add(p, rot(q, h)) for q in G[source]["outputs"]]
        for output, local in zip(outputs, G[source]["outputs"]):
            assert output not in identities
            identities[output] = {"kind": "produced", "packet_index": packet_index, "source": source, "output": local, "birth_C_clock": clock}
        for turn in G[source]["word"]:
            black = p in board
            assert black == (turn == "L")
            board.symmetric_difference_update({p})
            h = (h + (-1 if black else 1)) % 4
            p = add(p, HEAD_STEPS[h])
        expected = add(tuple(old_pose[:2]), rot(tuple(G[source]["endpoint"][:2]), old_pose[2]))
        assert p == expected and h == (old_pose[2] + G[source]["endpoint"][2]) % 4
        clock += G[source]["name"].count("C")
        core = {add(p, rot(q, h)) for q in K}
        assert core <= board and set(identities) == board - core
        boundaries.append({"packet_index": packet_index, "source": source, "entry_pose": old_pose, "entry_C_clock": old_clock, "consumed": consumed, "exit_pose": [*p, h], "exit_C_clock": clock, "live_residual_identities": [{"cell": cell, "identity": identity} for cell, identity in sorted(identities.items())]})
    raw_pose = [*p, h]
    for turn in G[0]["marker"]:
        black = p in board
        assert black == (turn == "L")
        board.symmetric_difference_update({p})
        h = (h + (-1 if black else 1)) % 4
        p = add(p, HEAD_STEPS[h])
    p, h, clock = (0, 0), 0, 0
    for packet_index, source in enumerate(word):
        for atom in [G[source]["name"][0]] + ["C"] * G[source]["name"].count("C"):
            start = add((2 * p[0], 2 * p[1]), rot((-1, -1), h))
            old_pose, old_clock = [*p, h], clock
            step = (0, 1) if atom == "C" else VECTORS[atom]
            p = add(p, rot(step, h))
            h = (h - int(atom == "C")) % 4
            clock += int(atom == "C")
            end = add((2 * p[0], 2 * p[1]), rot((-1, -1), h))
            edges.append({"atom": atom, "packet_index": packet_index, "entry_pose": old_pose, "entry_C_clock": old_clock, "start_twice": start, "end_twice": end})
    contacts = []
    for bi, later in enumerate(edges):
        for ai in range(bi - 1):
            earlier = edges[ai]
            u, v = sub(earlier["end_twice"], earlier["start_twice"]), sub(later["end_twice"], later["start_twice"])
            w = sub(later["start_twice"], earlier["start_twice"])
            denominator = det(u, v)
            if denominator:
                s, t = F(det(w, v), denominator), F(det(w, u), denominator)
                if not (0 <= s <= 1 and 0 <= t <= 1):
                    continue
            else:
                if det(w, u):
                    continue
                k = 0 if v[0] else 1
                t0, t1 = F(-w[k], v[k]), F(u[k] - w[k], v[k])
                low, high = max(F(0), min(t0, t1)), min(F(1), max(t0, t1))
                if low > high:
                    continue
                t = low
                point = add(later["start_twice"], (t * v[0], t * v[1]))
                k = 0 if u[0] else 1
                s = F(point[k] - earlier["start_twice"][k], u[k])
            contacts.append({"earlier_edge": ai, "later_edge": bi, "earlier_parameter": s, "later_parameter": t, "earlier_path_parameter": ai + s, "later_path_parameter": bi + t})
    assert contacts == []
    first_time, ai, bi, s, t = None, None, None, None, None
    return {"word": word, "names": [G[a]["name"] for a in word], "seed": sorted(seed), "entry_mass": len(seed), "raw_length": len(raw), "raw_plus_marker_length": len(raw) + len(G[0]["marker"]), "raw_exit_pose": raw_pose, "all_full_packet_identity_boundaries": boundaries, "atomic_chords": edges, "all_nonadjacent_contacts": contacts, "first_contact_path_time": first_time, "canonical_first_contact": {"earlier_edge": ai, "later_edge": bi, "earlier_parameter": s, "later_parameter": t}}

control=literal_control((7,1,0,9,5))
assert control['entry_mass']==18 and control['raw_length']==154
raw=''.join(G[a]['word'] for a in control['word'])
p,h=(0,0),0;reads=[]
for tick,turn in enumerate(raw+G[0]['marker']):
    if p==(0,4):reads.append({'tick':tick,'turn':turn,'incoming_heading':h,'in_raw':tick<len(raw)})
    h=(h+(-1 if turn=='L' else 1))%4;p=add(p,HEAD_STEPS[h])
assert reads==[{'tick':t,'turn':turn,'incoming_heading':h,'in_raw':True} for t,turn,h in [(24,'R',0),(28,'L',0),(32,'R',0),(40,'L',2),(152,'R',2)]]
control['five_read_cell']=(0,4);control['all_reads_of_that_cell']=reads
result={'status':'AUTHOR_ACTUAL_SIMPLE_CENTER_FIVE_PHYSICAL_READ_CONTROL',
 'scope':'Actual18-cell U,DC,D,UCC,VC factor has simple corrected-center path but5raw reads of one initially-white cell. This refutes cap4 in that scope; no renewal, capture or upper-bound optimality claim.',
 'control':control,'dependency_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP,Path(__file__).resolve())}}
def encode(v):
    if isinstance(v,F):return int(v) if v.denominator==1 else str(v)
    if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v
(ROOT/'chronology_dcuv/simple_center_five_read_control.json').write_text(json.dumps(encode(result),indent=2)+'\n')
print(json.dumps({'word':control['names'],'mass':control['entry_mass'],'raw_length':control['raw_length'],'atomic_chords':len(control['atomic_chords']),'center_contacts':len(control['all_nonadjacent_contacts']),'five_read_cell':[0,4],'reads':reads}))
