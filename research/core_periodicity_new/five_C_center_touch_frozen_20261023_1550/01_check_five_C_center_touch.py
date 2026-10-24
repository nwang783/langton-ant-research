"""Exact reduction of every five-C nonproper first center contact.

Existing clauses, one-cohort retirement, old-core origins and exact cones only.
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
HEAD_STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))
JO = {tuple(row[:3]):row[3] for row in json.loads(JP.read_text())}
assert all(JO[a,0,1]>=3 for a in (0,1))
assert all(JO[a,-1,1]>=3 for a in (7,8,9))
C_WORD = G[1]["word"][len(G[0]["word"]):]


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


def requirements(raw):
    colors, initial = {}, {}
    p, h = (0, 0), 0
    for tick, turn in enumerate(raw + G[0]["marker"]):
        black = turn == "L"
        if p in colors:
            if colors[p] != black:
                return initial, {"tick": tick, "cell": p, "prescribed": turn, "actual": "L" if colors[p] else "R"}
        else:
            initial[p] = black
        colors[p] = not black
        h = (h + (-1 if black else 1)) % 4
        p = add(p, HEAD_STEPS[h])
    return initial, None


contexts = {name: {tuple(v[:2]): v[2] for v in G[a]["requirements"]} for name, a in (("D", 0), ("V", 4), ("U", 7))}
contexts["C"], conflict = requirements(C_WORD)
assert conflict is None
outputs = {"D": G[0]["outputs"], "V": G[4]["outputs"], "U": G[7]["outputs"], "C": [(1, 2), (2, 0), (2, 1)]}


def closed_contact(source_atom, consumer, p, h):
    u = tuple(2 * v for v in VECTORS[source_atom])
    v = rot(tuple(2 * z for z in VECTORS[G[consumer]["name"][0]]), h)
    c = (-1, -1)
    w = sub(add((2 * p[0], 2 * p[1]), rot(c, h)), c)
    denominator = det(u, v)
    if denominator:
        s, t = F(det(w, v), denominator), F(det(w, u), denominator)
        return 0 <= s <= 1 and 0 <= t <= 1
    if det(w, u):
        return False
    return all(max(min(c[k], c[k] + u[k]), min(c[k] + w[k], c[k] + w[k] + v[k])) <= min(max(c[k], c[k] + u[k]), max(c[k] + w[k], c[k] + w[k] + v[k])) for k in (0, 1))


def zero_reach(p, target, h):
    x, y = rot(sub(target, p), -h)
    return x >= 0 and y >= 0 and any(y - x - 2 * v >= 0 and (y - x - 2 * v) % 4 == 0 for v in range(x + 1))




def one_reach(p,target,h):
    X,Y=rot(sub(target,p),-h)
    if Y<1:return None
    for y in range(Y):
        for x in range(y+1):
            if zero_reach((0,0),(x,y),0) and zero_reach((x,y+1),(X,Y),3):
                return (x,y)
    return None

roles=[]
for source in IDS:
    count=G[source]['name'].count('C');atom=G[source]['name'][0]
    roles.append({'atom':atom,'source':source,'p':(0,0),'h':0,'shift':0,'remaining':count})
    p,h=tuple(G[base(source)]['endpoint'][:2]),0
    for j in range(count):
        roles.append({'atom':'C','source':source,'p':p,'h':h,'shift':j,'remaining':count-j})
        p,h=add(p,rot((0,1),h)),(h-1)%4

geo=[]
center=(F(-1,2),F(-1,2))
for a,u in VECTORS.items():
 for b,bb in VECTORS.items():
    v=rot(bb,3);correction=sub(center,rot(center,3));corners=[add(correction,(s*u[0]-t*v[0],s*u[1]-t*v[1])) for s in (0,1) for t in (0,1)]
    for x in range(int(min(z[0] for z in corners)),int(max(z[0] for z in corners))+1):
     for y in range(int(min(z[1] for z in corners)),int(max(z[1] for z in corners))+1):
      if (x+y+3)%2:continue
      w=sub(add((x,y),rot(center,3)),center);den=det(u,v);s,t=F(det(w,v),den),F(det(w,u),den)
      if 0<=s<1 and 0<t<=1 and not(0<s<1 and 0<t<1):geo.append({'a':a,'b':b,'p':(x,y),'h':3,'s':s,'t':t})
assert len(geo)==24


# All output-source identities are actual births. This helper enumerates only
# strict consumers before the target atom; target C may cut a consuming tail.
def retire_options(a, output, target_atom, target_pose, chosen_roles=None):
    rows, opened = [], []
    for ri, r in enumerate(roles):
        if r['atom'] != a or (chosen_roles is not None and ri not in chosen_roles):
            continue
        source = r['source']
        full_output = add(r['p'], rot(output, r['h']))
        assert list(full_output) in G[source]['outputs']
        for n in range(6):
            h = (-n) % 4
            for consumer in IDS:
                for inp in G[consumer]['inputs']:
                    cp = sub(output, rot(inp, h))
                    fp = add(r['p'], rot(cp, r['h']))
                    fh, age = (r['h'] + h) % 4, n + r['shift']
                    key = (NEW[source], NEW[consumer], *fp, fh, *full_output, min(age, 5))
                    hb = (source, consumer, *fp, fh, *full_output)
                    row = {'source_role_index':ri, 'full_source':source, 'atomic_output':output,
                           'full_source_output':full_output, 'atomic_entry_C_gap':n,
                           'full_source_age':age, 'consumer':consumer, 'consumer_input':inp,
                           'consumer_pose':(*cp,h), 'counted_query':key, 'HB_query':hb}
                    if n < r['remaining']:
                        why = 'BEFORE_FULL_SOURCE_EXIT'
                    elif (sum(fp) + fh) % 2:
                        why = 'WRONG_SECTOR'
                    elif hb in HB:
                        why = 'SIGNED_HB_EXCLUDED'
                    elif key in COUNTED:
                        why = 'SIGNED_COUNT5_EXCLUDED'
                    elif closed_contact(a, consumer, cp, h):
                        assert n >= 2
                        why = 'EARLIER_NONADJACENT_CLOSED_CONTACT'
                    elif target_atom != 'C' and n + G[consumer]['name'].count('C') > 5:
                        why = 'FULL_CONSUMER_CANNOT_FINISH_BEFORE_TARGET_BASE'
                    else:
                        bs = 0 if G[consumer]['name'][0] == 'D' else 4 if G[consumer]['name'][0] == 'V' else 7
                        end = add(cp, rot(G[bs]['endpoint'][:2], h))
                        left = 5 - n
                        row['consuming_base_exit'] = (*end,h)
                        if left == 0 and not (h == 3 and zero_reach(end,target_pose,3)):
                            why = 'EXACT_ZERO_C_CONE_CANNOT_REACH_TARGET'
                        elif left == 1 and not ((h-1)%4 == 3 and one_reach(end,target_pose,h) is not None):
                            why = 'EXACT_ONE_C_CONE_CANNOT_REACH_TARGET'
                        else:
                            why = 'RESIDUAL_OPTION'
                            opened.append(row)
                    row['reason'] = why
                    rows.append(row)
    return rows, opened


def twice_center(p,h):
    return add((2*p[0],2*p[1]),rot((-1,-1),h))

reductions, retirement_tables = [], []
for gi, geometry in enumerate(geo):
    a,b,p = geometry['a'],geometry['b'],geometry['p']
    forced = []
    for output in outputs[a]:
        local = rot(sub(output,p),1)
        if local in K or contexts[b].get(local) is False:
            forced.append(tuple(output))
    # Fixed finite slot choice, not an unbounded search.
    candidate_tables = []
    for output in forced:
        rows, opened = retire_options(a,output,b,p)
        candidate_tables.append((output,rows,opened))
    hard = next(((output,rows) for output,rows,opened in candidate_tables if not opened),None)
    if hard is not None:
        output, rows = hard
        retirement_tables.append({'geometry_index':gi,'hard_source_output':output,'rows':rows})
        reason = 'MANDATORY_SOURCE_OUTPUT_HAS_NO_TIMELY_NONCONTACT_RETIREMENT'
    elif a == 'D' and b in ('V','U'):
        assert (b,p) in (('V',(2,-1)),('U',(1,0)),('U',(3,0)))
        rows, opened = retire_options(a,(2,0),b,p)
        survivors = []
        for row in opened:
            n, consumer, cp = row['atomic_entry_C_gap'],row['consumer'],row['consumer_pose']
            if n == 3:
                assert consumer in (4,5) and cp == (0,1,1)
                # The V base's exit bud is global(2,-1), current two Cs later.
                bud, local = (2,-1),rot(sub((2,-1),p),1)
                assert (local in K) or (b=='U' and local==(-1,1))
                row['second_generation_bud'] = bud
                row['target_local_bud'] = local
                row['reason'] = 'FRESH_V_EXIT_BUD_STILL_CURRENT_IN_TARGET_CORE_OR_TOO_YOUNG_U_LOWER'
            else:
                assert b=='U' and p==(1,0) and n==5
                assert (consumer,cp) in ((4,(4,-1,3)),(7,(5,0,3)))
                assert row['consuming_base_exit'] == (1,0,3)
                # Nonempty zero-C words cannot have zero displacement.
                row['reason'] = 'OPEN_IMMEDIATE_V_OR_U_PREDECESSOR_OF_TARGET_U'
                survivors.append(row)
        retirement_tables.append({'geometry_index':gi,'hard_source_output':(2,0),'rows':rows})
        if survivors:
            assert len(survivors)==4 # two actual D/DC source roles, two helpers.
            reason = 'OPEN_D_TO_U_WITH_IMMEDIATE_V_OR_U_OLD_MAIN_CLEARER'
        else:
            reason = 'SECOND_GENERATION_FRESH_BUD_EXCLUDES_ALL_RESIDUAL_CLEARERS'
    elif a in ('D','C') and b=='D' and p==(0,-1):
        reason = 'OLD_CORE_D_INPUT_ORIGIN_FORCES_AN_EARLIER_ENTRY_CENTER_REPEAT'
    else:
        assert a in ('D','C') and b=='C' and p==(0,-1)
        reason = 'C_SOURCE_INCOMING_BUD_FORCES_EARLIER_CONTACT' if a=='C' else 'OPEN_D_TO_C_ENDPOINT_GATE'
    reductions.append({'geometry_index':gi,'forced_source_outputs':forced,'reason':reason})
assert len(reductions)==24
assert Counter(r['reason'] for r in reductions)=={
 'MANDATORY_SOURCE_OUTPUT_HAS_NO_TIMELY_NONCONTACT_RETIREMENT':17,
 'SECOND_GENERATION_FRESH_BUD_EXCLUDES_ALL_RESIDUAL_CLEARERS':2,
 'OPEN_D_TO_U_WITH_IMMEDIATE_V_OR_U_OLD_MAIN_CLEARER':1,
 'OLD_CORE_D_INPUT_ORIGIN_FORCES_AN_EARLIER_ENTRY_CENTER_REPEAT':2,
 'C_SOURCE_INCOMING_BUD_FORCES_EARLIER_CONTACT':1,
 'OPEN_D_TO_C_ENDPOINT_GATE':1}

# Old core(-1,-1) cannot be an entry residual at the later D. The containing
# full packet never outputs it; every later actual birth has clock at least 1.
# Clock-zero N full producers cannot output behind their already-positive exit.
old_core_role_cases=[]
for ri,r in enumerate(roles):
    if r['atom'] not in ('D','C'):continue
    full_q=add(r['p'],rot((-1,-1),r['h']))
    assert list(full_q) not in G[r['source']]['outputs']
    if not r['remaining']:
        assert r['atom']=='D' and r['source']==0 and G[0]['endpoint'][1]>-1
    old_core_role_cases.append({'role_index':ri,'old_atomic_core_cell':(-1,-1),'full_frame_cell':full_q,'same_full_output':False})
assert len(old_core_role_cases)==9

# A fresh D input can never have exact age four, across ALL output origins.
d_age4=[]
for source in IDS:
 for output in G[source]['outputs']:
  for target in (0,1):
   h=0;p=sub(output,(0,1));key=(NEW[source],NEW[target],*p,h,*output,4);hb=(source,target,*p,h,*output)
   if sum(p)%2:why='WRONG_SECTOR'
   elif hb in HB:why='SIGNED_HB_EXCLUDED'
   else:
    assert key in COUNTED;why='SIGNED_COUNT5_EXCLUDED'
   d_age4.append({'query':key,'HB_query':hb,'reason':why})
assert len(d_age4)==136

# At birth clock2 a prospective producer is S. All age-three D-input origins
# either contact the old source chord already, or plain D's earlier exit
# center equals the final target D ENTRY center.
core_producers=[]
for a in ('D','C'):
 for source in IDS:
  for output in G[source]['outputs']:
   p=sub((-1,-1),rot(output,2))
   for target in (0,1):
    target_p=rot(sub((0,-1),p),-2);target_h=1
    key=(NEW[source],NEW[target],*target_p,target_h,*output,3);hb=(source,target,*target_p,target_h,*output)
    row={'earlier_atom':a,'producer':source,'output':output,'producer_pose':(*p,2),'target':target,'query':key,'HB_query':hb}
    if (sum(p)+2)%2:why='WRONG_SECTOR'
    elif hb in HB:why='SIGNED_HB_EXCLUDED'
    elif key in COUNTED:why='SIGNED_COUNT5_EXCLUDED'
    elif closed_contact(a,source,p,2):why='EARLIER_CLOSED_CONTACT'
    else:
     assert source==0 and target in (0,1) and output==[2,0] and p==(1,-1)
     end=add(p,rot(G[0]['endpoint'][:2],2))
     assert twice_center(end,2)==twice_center((0,-1),3)
     row['producer_base_exit']=(*end,2)
     why='PRODUCER_EXIT_CENTER_REPEATS_AT_TARGET_ENTRY_BEFORE_ENDPOINT_CONTACT'
    row['reason']=why;core_producers.append(row)
assert len(core_producers)==272

# An earlier actual C ALWAYS has the preceding atom's fresh exit bud(1,-1).
# This remains in the containing full output set, with the explicit shift.
# The target C requires it in its entry core, hence it must retire strictly.
assert rot(sub((1,-1),(0,-1)),1) in K
incoming_rows,incoming_open=retire_options('C',(1,-1),'C',(0,-1))
late_helper_common_tables=[]
for helper,p in (('V',(3,-2)),('U',(4,-1))):
 local=rot(sub((2,0),p),1)
 assert contexts[helper].get(local) is False
 rows,opened=retire_options('C',(2,0),helper,p)
 assert not opened
 late_helper_common_tables.append({'helper_atom':helper,'helper_pose':(*p,3),'hard_source_output':(2,0),'rows':rows})
for row in incoming_open:
 n,consumer,p=row['atomic_entry_C_gap'],row['consumer'],row['consumer_pose']
 if n==3:
  assert row['full_source']==1 and consumer in (4,5) and p==(-2,-1,1)
  assert twice_center(row['consuming_base_exit'][:2],1)==twice_center((0,-1),3)
  row['reason']='CLEARING_BASE_EXIT_CENTER_REPEATS_AT_TARGET_ENTRY'
 else:
  assert n==5 and ((consumer in (4,5,6) and p==(3,-2,3)) or (consumer in (7,8,9) and p==(4,-1,3)))
  row['reason']='CLEARING_HELPER_NEEDS_UNRETIRABLE_OLD_C_COMMON_OUTPUT_WHITE'
assert len(incoming_rows)==966 and len(incoming_open)==44


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
    first_time = min(row["later_path_parameter"] for row in contacts)
    first_contacts = [row for row in contacts if row["later_path_parameter"] == first_time]
    canonical = set()
    for row in first_contacts:
        ai, bi, s, t = row["earlier_edge"], row["later_edge"], row["earlier_parameter"], row["later_parameter"]
        if s == 1:
            ai, s = ai + 1, F(0)
        if t == 0:
            bi, t = bi - 1, F(1)
        canonical.add((ai, bi, s, t))
    assert len(canonical) == 1
    ai, bi, s, t = next(iter(canonical))
    assert edges[ai]["atom"] == "D" and edges[bi]["atom"] == "C" and s == 0 and t == 1
    assert edges[bi]["entry_C_clock"] - edges[ai]["entry_C_clock"] == 5
    assert rot(sub(tuple(edges[bi]["entry_pose"][:2]), tuple(edges[ai]["entry_pose"][:2])), -edges[ai]["entry_pose"][2]) == (0, -1)
    assert (edges[bi]["entry_pose"][2] - edges[ai]["entry_pose"][2]) % 4 == 3
    return {"word": word, "names": [G[a]["name"] for a in word], "seed": sorted(seed), "entry_mass": len(seed), "raw_length": len(raw), "raw_plus_marker_length": len(raw) + len(G[0]["marker"]), "raw_exit_pose": raw_pose, "all_full_packet_identity_boundaries": boundaries, "atomic_chords": edges, "all_nonadjacent_contacts": contacts, "first_contact_path_time": first_time, "canonical_first_contact": {"earlier_edge": ai, "later_edge": bi, "earlier_parameter": s, "later_parameter": t}}

positive=literal_control((1,5,4,5,5,6))
assert positive['entry_mass']==16 and positive['raw_length']==190
assert positive['first_contact_path_time']==12
assert positive['canonical_first_contact']=={'earlier_edge':0,'later_edge':11,'earlier_parameter':F(0),'later_parameter':F(1)}
# This fixed control is left-isolated; that is NOT a generic boundary theorem.
prepend_controls=[]
for source in IDS:
    _,conflict=requirements(G[source]['word']+''.join(G[a]['word'] for a in positive['word']))
    assert conflict is not None
    prepend_controls.append({'prepend':source,'conflict':conflict})


def rational_json(value):
    if isinstance(value,F):return int(value) if value.denominator==1 else str(value)
    if isinstance(value,dict):return {k:rational_json(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [rational_json(v) for v in value]
    return value

result={'status':'AUTHOR_FIVE_C_NONPROPER_CONTACT_REDUCED_TO_TWO_D_GATES_WITH_ACTUAL_ENDPOINT_CONTROL',
 'scope':'Every canonical n5 nonproper first contact reduces to D -> C(0,-1,W), or D -> U(1,0,W) with immediate V/U old-main clearer. No general boundary-only claim; the D->C gate is actually attained from16cells.',
 'all_24_geometries':geo,'all_15_source_roles':roles,'geometry_reductions':reductions,
 'hard_retirement_tables':retirement_tables,'old_core_role_cases':old_core_role_cases,
 'all_136_D_input_exact_age_four_queries':d_age4,'all_272_old_core_clock_two_producer_cases':core_producers,
 'all_966_C_incoming_bud_retirement_cases':incoming_rows,
 'late_helper_common_output_tables':late_helper_common_tables,
 'actual_sixteen_cell_control':positive,'fixed_control_eight_prepended_packet_conflicts':prepend_controls,
 'dependency_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP,CP,HP,AP,JP,ROOT/'atomic_exit_bud_frozen_20261023_1325/manifest.json',Path(__file__).resolve())}}
(ROOT/'chronology_dcuv/five_C_center_touch.json').write_text(json.dumps(rational_json(result),indent=2)+'\n')
print(json.dumps({'geometries':len(geo),'reduction_counts':dict(Counter(r['reason'] for r in reductions)),'retirement_rows':sum(len(t['rows']) for t in retirement_tables),'old_core_producer_rows':len(core_producers),'incoming_bud_rows':len(incoming_rows),'late_helper_common_rows':sum(len(t['rows']) for t in late_helper_common_tables),'actual_control_mass':positive['entry_mass']}))
