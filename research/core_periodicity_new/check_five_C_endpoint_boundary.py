"""A noninitial D cannot begin a five-C nonproper first-contact D-to-C gate."""

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


# Use actual completed-full predecessor frames, not a fictitious atomic birth.
atomic_roles=roles
predecessor_roles=[]
for source in IDS:
    c=G[source]['name'].count('C')
    predecessor_roles.append({'atom':'D','source':source,'p':tuple(G[source]['endpoint'][:2]),'h':(-c)%4,'shift':c,'remaining':0})
roles=predecessor_roles
rows,opened=retire_options('D',(1,-1),'C',(0,-1))
assert len(rows)==1104 and len(opened)==68
assert rot(sub((1,-1),(0,-1)),1) in K

# Every final-clock incoming-bud clearer needs the D source's old common
# output(2,0) WHITE at its BASE entry. It cannot clear that output early.
roles=atomic_roles
helper_main_tables=[]
for atom,p in (('V',(3,-2)),('U',(4,-1))):
    local=rot(sub((2,0),p),1)
    assert contexts[atom].get(local) is False
    table,remaining=retire_options('D',(2,0),atom,p)
    assert len(table)==276 and len(remaining)==4
    for row in remaining:
        assert row['atomic_entry_C_gap']==3 and row['consumer'] in (4,5) and row['consumer_pose']==(0,1,1)
        # Atomic V exit bud is current through clock5, only2 post-exitCs.
        bud=(2,-1)
        local=rot(sub(bud,p),1)
        if atom=='V':
            assert contexts['V'].get(local) is False and local==(1,1)
        else:
            assert local==(0,2) and list(local) in G[7]['inputs']
            assert JO[7,0,2]>=4 # exact age2 cannot meet even the older minimum4.
        row['blocking_fresh_exit_bud']=bud
        row['helper_local_bud']=local
        row['reason']='FRESH_V_EXIT_BUD_STILL_CURRENT_WHITE_OR_TOO_YOUNG_AT_HELPER'
    helper_main_tables.append({'helper_atom':atom,'helper_pose':(*p,3),'main_output':(2,0),'rows':table})

# The remaining age3 U clearer creates output(0,1), current two Cs later.
# Its raw source can have any of the three attached-C tails.
u_output_queries=[]
for source in (7,8,9):
    for age in range(3):
        h=(-age)%4
        for consumer in IDS:
            for inp in G[consumer]['inputs']:
                p=sub((0,1),rot(inp,h))
                key=(NEW[source],NEW[consumer],*p,h,0,1,age)
                hb=(source,consumer,*p,h,0,1)
                if age<G[source]['name'].count('C'):
                    why='BEFORE_FULL_SOURCE_EXIT'
                elif (sum(p)+h)%2:
                    why='WRONG_SECTOR'
                elif hb in HB:
                    why='SIGNED_HB_EXCLUDED'
                else:
                    assert key in COUNTED
                    why='SIGNED_COUNT5_EXCLUDED'
                u_output_queries.append({'query':key,'HB_query':hb,'reason':why})
assert len(u_output_queries)==207

for row in opened:
    n,consumer,p=row['atomic_entry_C_gap'],row['consumer'],row['consumer_pose']
    if n==5:
        assert ((consumer in (4,5,6) and p==(3,-2,3)) or (consumer in (7,8,9) and p==(4,-1,3)))
        row['reason']='NEEDS_OLD_MAIN_WHITE_BUT_EVERY_PRIOR_MAIN_CLEARER_LEAVES_IMMATURE_BUD'
    else:
        assert n==3
        if G[consumer]['name'][0]=='V':
            assert p==(-2,-1,1)
            end=row['consuming_base_exit']
            assert twice_center(end[:2],end[2])==twice_center((0,-1),3)
            row['reason']='CLEARING_V_EXIT_CENTER_REPEATS_AT_FINAL_C_ENTRY'
        else:
            assert G[consumer]['name'][0]=='U' and row['full_source'] in (6,9)
            if p==(-3,-2,1):
                end=row['consuming_base_exit']
                assert twice_center(end[:2],end[2])==twice_center((0,-1),3)
                row['reason']='CLEARING_U_EXIT_CENTER_REPEATS_AT_FINAL_C_ENTRY'
            else:
                assert p==(-1,-2,1)
                q=add(p[:2],rot((0,1),1))
                assert q==(0,-2) and rot(sub(q,(0,-1)),1) in K
                row['new_U_output_global_cell']=q
                row['reason']='FRESH_U_OUTPUT_0_1_STILL_CURRENT_IN_FINAL_C_CORE'


def rational_json(value):
    if isinstance(value,F):return int(value) if value.denominator==1 else str(value)
    if isinstance(value,dict):return {k:rational_json(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [rational_json(v) for v in value]
    return value

result={'status':'AUTHOR_FIVE_C_NONPROPER_D_TO_C_FIRST_CONTACT_FORCES_D_FACTOR_FIRST',
 'scope':'Given the normalized D0N -> C(0,-1,W), exact5C first-contact gate, D must be the factor-first base. No arbitrary later5C transfer, generic first-contact or no-return theorem is claimed.',
 'all_eight_completed_predecessor_roles':predecessor_roles,
 'all_1104_incoming_bud_retirement_cases':rows,
 'last_clock_helper_main_retirement_tables':helper_main_tables,
 'all_207_fresh_U_output_0_1_age_zero_to_two_cases':u_output_queries,
 'dependency_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP,CP,HP,JP,ROOT/'atomic_exit_bud_frozen_20261023_1325/manifest.json',ROOT/'five_C_center_touch_frozen_20261023_1550/manifest.json',Path(__file__).resolve())}}
(ROOT/'chronology_dcuv/five_C_endpoint_boundary.json').write_text(json.dumps(rational_json(result),indent=2)+'\n')
print(json.dumps({'incoming_rows':len(rows),'initial_residual_options':len(opened),'residual_cut_counts':dict(Counter(r['reason'] for r in opened)),'helper_main_rows':sum(len(t['rows']) for t in helper_main_tables),'fresh_U_output_rows':len(u_output_queries)}))
