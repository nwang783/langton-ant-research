"""One next-foreign transfer of the genuine Q/B hook after three ordinary Cs.
No U-entry, simplicity, earlier-history or epoch-length premise.
All coordinates are in the SOURCE FOREIGN ENTRY frame (0,0,N).
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import importlib.util, json, hashlib
ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

lit = load('literal', ROOT / 'word_stabilization/check_foreign_return_interfaces.py')
owner = load('owner', ROOT / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
WORDS = owner.WORDS

def add(p, q): return p[0] + q[0], p[1] + q[1]
def sub(p, q): return p[0] - q[0], p[1] - q[1]
def after(word, pose=(0,0,0)):
    p, h = pose[:2], pose[2]
    for turn in word:
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, lit.DIRS[h])
    return (*p, h)
def local(cell, pose): return lit.rot(sub(cell, pose[:2]), (-pose[2]) % 4)
def active(pose): return (sum(pose[:2]) + pose[2]) % 2 == 0

def field_conflicts(packet, pose, field, forbid_true_inputs=False):
    trace = lit.trace(''.join(WORDS[a] for a in packet) + lit.M)
    result = []
    for cell in sorted(field):
        q = local(cell, pose)
        requirement = trace['first'].get(q)
        if q in lit.K or requirement and (requirement[0] == 'R' or forbid_true_inputs):
            result.append(dict(SAME_initial_cell=cell, local_cell=q,
                reason='ENTRY_CORE' if q in lit.K else 'first_WHITE' if requirement[0] == 'R' else 'forbidden_prior_CURRENT_loss',
                first_read=None if requirement is None else owner.describe(packet, requirement[1])))
    return result

NE = {(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)}
HOOK = {(-1,-1),(-2,-1),(-3,-1),(-3,-2)}
FIELD = NE | HOOK
assert len(FIELD) == 13
births = []
for source in 'QB':
    trace = lit.trace(WORDS[source])
    outputs = set(map(tuple, lit.literal_geometry(WORDS[source])['outputs']))
    assert FIELD | {(-4,1),(-4,-1)} <= outputs
    births.append(dict(source=source, actual_EXIT=after(WORDS[source]),
        tracked_originals=[dict(cell=q, own_last_R_tick0=trace['last'][q][1])
            for q in sorted(FIELD | {(-4,1),(-4,-1)})]))
    assert trace['last'][(-4,-1)] == ('R',55)

# All first ordinary losses of an unspent NE field during W3.
first_W = []
for cell in sorted(NE):
    for atom in 'DVU':
        for slot in map(tuple, lit.literal_geometry(WORDS[atom])['inputs']):
            pose = (*sub(cell, lit.rot(slot,3)), 3)
            row = dict(cell=cell, consumer=atom, true_input=slot, ENTRY=pose)
            if not active(pose):
                row['route'] = 'sector'
            else:
                conflicts = field_conflicts(atom, pose, FIELD)
                row['route'] = 'held_FIELD' if conflicts else 'only_possible_W3_first_NE_loss'
                row['conflicts'] = conflicts
            first_W.append(row)
assert len(first_W) == 80
assert Counter(r['route'] for r in first_W) == {
    'sector':40, 'held_FIELD':39, 'only_possible_W3_first_NE_loss':1}
sole = next(r for r in first_W if r['route'] == 'only_possible_W3_first_NE_loss')
assert (sole['consumer'], sole['ENTRY'], sole['cell'], sole['true_input']) == ('U',(2,3,3),(1,2),(-1,1))
assert after(WORDS['U'], (2,3,3)) == (-2,3,3)

# Exactly all next-foreign true-hook-loss poses with heading W.
goals = {}
for target in 'FQB':
    trace = lit.trace(WORDS[target] + lit.M)
    for cell in sorted(HOOK):
        for slot in map(tuple, lit.literal_geometry(WORDS[target])['inputs']):
            pose = (*sub(cell, lit.rot(slot,3)), 3)
            if active(pose):
                goals.setdefault((target,pose), []).append(dict(cell=cell, true_input=slot,
                    first_L=owner.describe(target,trace['first'][slot][1])))
assert len(goals) == 57
unspent = []
for (target, pose), witnesses in sorted(goals.items()):
    conflicts = field_conflicts(target, pose, FIELD)
    unspent.append(dict(target=target, ENTRY=pose, hook_input_witnesses=witnesses,
        route='held_FIELD' if conflicts else 'extra_source_output_guard', conflicts=conflicts))
assert Counter(r['route'] for r in unspent) == {'held_FIELD':53,'extra_source_output_guard':4}
remaining = {(r['target'],r['ENTRY']) for r in unspent if r['route'] == 'extra_source_output_guard'}
assert remaining == {(a,(-4,1,3)) for a in 'FQB'} | {('B',(-5,0,3))}

# If the earlier N2 first loss occurred, the signed paired gate exits (3,3,N).
# After C3, W starts (3,4,W). Every possible hook target has y<=4.
# Height equality forbids any further N base or W D/V; a first W U would be CU.
maximum_hook_y = max(pose[1] for _,pose in goals)
assert maximum_hook_y == 4
paired_targets = [(a,p) for a,p in goals if p[1] >= 4]
assert set(paired_targets) == {(a,(x,4,3)) for a in 'FQB' for x in (-1,1)}
assert after(WORDS['C'],(3,3,0)) == (3,4,3)
CU = lit.trace(WORDS['C'] + WORDS['U'])
assert not CU['feasible'] and (CU['previous_read'], CU['conflict_read'], CU['turn']) == (1,29,'L')
paired_route = dict(actual_N2_first_loss='U(3,-1,N)', actual_N2_gate_EXIT=(3,3,0),
    minimum_W3_ENTRY=(3,4,3), all_six_height_equality_hook_targets=paired_targets,
    argument='Every later N base raises y. W D/V also raise y; only W U preserves it, but the first such U would immediately follow C3 and is literally impossible. Thus equality y=4 permits no W base and leaves head (3,4), not x=-1 or x=1.')

# If first NE loss instead occurs at U(2,3,W), there are exactly four
# endpoint-compatible ordinary W continuations into any hook-loss target.
@lru_cache(None)
def W_paths(dx, dy):
    if dx < 0 or dy < 0: return ()
    if dx == dy == 0: return ('',)
    result = []
    for a,(x,y) in {'D':(1,1),'V':(3,1),'U':(4,0)}.items():
        if dx >= x and dy >= y:
            result.extend(s+a for s in W_paths(dx-x,dy-y))
    return tuple(result)
W_after_loss = []
for target, pose in sorted(goals):
    for suffix in W_paths(-2-pose[0],pose[1]-3):
        packet = 'U' + suffix + target
        trace = lit.trace(''.join(WORDS[a] for a in packet) + lit.M)
        conflicts = field_conflicts(packet,(2,3,3),FIELD)
        assert trace['feasible'] and conflicts
        W_after_loss.append(dict(packet=packet, suffix_after_first_U=suffix, target_ENTRY=pose,
            initial_GATE_ENTRY=(2,3,3), immutable_initial_FIELD_conflicts=conflicts))
assert len(W_after_loss) == 4
assert {r['packet'] for r in W_after_loss} == {'UF','UQ','UUQ','UB'}

# Genuine two extra source outputs close the four all-NE-unspent targets.
# S0/E1 cannot touch either tag: S input y<=source_EXIT_y-1 and E input
# y<=source_EXIT_y, whereas both source_EXIT_y<=-4 and tag_y>=-1.
ports = []
for atom in 'DVU':
    endpoint = after(WORDS[atom])
    complete = lit.trace(WORDS[atom] + lit.M)
    for slot in map(tuple, lit.literal_geometry(WORDS[atom])['inputs']):
        assert slot[1] >= 1 and -slot[0] <= 1
        dy = endpoint[1] - slot[1]
        assert dy >= 0
        if dy == 0: assert endpoint[0] - slot[0] == 1
        W_dy = endpoint[0] - slot[0]
        assert W_dy >= 0
        if W_dy == 0: assert lit.rot(sub(endpoint[:2],slot),3)[0] <= -1
        ports.append(dict(atom=atom, true_input=slot, actual_L=owner.describe(atom,complete['first'][slot][1]),
            N_RAW_EXIT_minus_tag=(endpoint[0]-slot[0],dy),
            W_RAW_EXIT_minus_tag=lit.rot(sub(endpoint[:2],slot),3)))
assert len(ports) == 8
upper_guard = []
for target in 'FQB':
    pose = (-4,1,3); tag=(-4,1)
    assert local(tag,pose) in lit.K
    upper_guard.append(dict(target=target,ENTRY=pose,SAME_tag=tag,local_entry_CORE=local(tag,pose),
        proof='A prior N2 first loss has EXIT_y>=1, then C3 forces W_y>=2, above target y=1. A W3 first loss has EXIT_y>=1; equality is V selected or U q/upper-d, and every such EXIT_x<=tag_x-1=-5, already left of target x=-4. All later W motion has nonincreasing x and nondecreasing y.'))
# The last target is blocked by R55=(-4,-1), using exact W suffix equations.
late_tag = (-4,-1); last_pose=(-5,0,3)
assert local(late_tag,last_pose) in lit.K
W_late_ports = []
for port in ports:
    atom,slot = port['atom'],port['true_input']
    pose = (*sub(late_tag,lit.rot(slot,3)),3)
    endpoint = after(WORDS[atom],pose)
    dx,dy = endpoint[0]-last_pose[0],last_pose[1]-endpoint[1]
    solutions = []
    for d in range(max(0,dy)+1):
        v = dy-d; residual = dx-d-3*v
        if v >= 0 and residual >= 0 and residual % 4 == 0:
            solutions.append((d,v,residual//4))
    assert not solutions
    W_late_ports.append(dict(consumer=atom,input=slot,actual_ENTRY=pose,actual_RAW_EXIT=endpoint,
        remaining_W_displacement_weights=(dx,dy),remaining_counts_D_V_U=solutions))
assert len(W_late_ports) == 8
last_guard = dict(target='B', ENTRY=last_pose, SAME_R55_tag=late_tag, local_entry_CORE=local(late_tag,last_pose),
    N2_loss_route='For target y=0, N first loss must EXIT exactly at y=-1; equality forces EXIT(-3,-1,N). C3 gives (-3,0,W). Any subsequent height-preserving W word is U^u and displaces x by -4u, never reaching target x=-5.',
    all8_W3_first_loss_exit_equations=W_late_ports)

# Genuine three-C prefixes remain possible. These are full finite fields,
# not successful next-foreign erosions or claims about their proxies.
def control(packet):
    raw=''.join(WORDS[a] for a in packet)
    trace=lit.trace(raw+lit.M)
    assert trace['feasible']
    seed={q for q,(turn,_) in trace['first'].items() if turn=='L'}
    black=set(seed); p=(0,0); h=0
    for tick,turn in enumerate(raw+lit.M):
        assert (p in black) == (turn=='L')
        black.symmetric_difference_update({p})
        h=(h+(1 if turn=='R' else -1))%4
        p=add(p,lit.DIRS[h])
    return dict(packet=packet, seed=sorted(seed), seed_mass=len(seed),actual_reads=len(raw+lit.M),
        RAW_EXIT=after(raw), after_actual_M_prefix=(p[0],p[1],h),final_mass=len(black),
        scope='Complete genuine U-entry finite prefix with three ordinary Cs after its first Q/B. No next foreign is asserted.')
controls=[control('UQUCCVC'),control('UBUCCVC')]

DEPS=[
 'foreign_two_C_pair_hole_transfer_2026-10-24/manifest.json',
 'audits/check_foreign_two_C_pair_hole_independent.json',
 'foreign_hook_four_C_maturity_2026-10-24/manifest.json',
 'audits/check_hook_four_C_maturity_independent.json',
 'Q_B_hook_next_foreign_low_clock_2026-10-24/manifest.json',
 'audits/check_QB_hook_low_clock_independent.json',
 'foreign_two_C_north_frontier_2026-10-24/manifest.json',
 'audits/check_foreign_two_C_frontier_independent.json',
 'word_stabilization/check_foreign_return_interfaces.py',
 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
result=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',
 scope='Any actual source Q/B ENTRY(0,0,N), then only ordinary RAW D/C/V/U with exactly three actual Cs, then one next complete F/Q/B RAW and actual M11. All four SAME source-hook IDs remain CURRENT at the next foreign RAW EXIT and through its actual M prefix. No U-entry, earlier-history, simple-proxy, global-first-contact, bounded-rail or language-coverage premise.',
 all2_source_birth_interfaces=births,all80_first_NE_loss_W3_roles=first_W,
 all57_next_foreign_hook_loss_poses_unspent_NE_branch=unspent,
 N2_first_loss_branch=paired_route,actual_CU_failure=CU,
 all4_endpoint_exhaustive_W_continuations_after_W3_first_NE_loss=W_after_loss,
 all8_true_input_exit_bounds=ports,all3_upper_source_tag_guards=upper_guard,
 final_B_R55_current_guard=last_guard,genuine_three_C_prefix_controls=controls,
 CURRENT_completion_argument='The genuine hook remains CURRENT through the ordinary prefix because its first ordinary loss needs four Cs. Any next-foreign first CURRENT loss, including exit-CORE capture, must be one of its complete-context true inputs, unless it already lies in entry CORE or first requires WHITE, which contradicts the preceding CURRENT field. All 57 true-input poses have now been excluded, in every possible NE first-loss branch. Therefore no hook identity dies or enters next-foreign exit CORE. Actual following M11 is supplied by the real next word, not treated as an extra completed packet.',
 one_transfer_only='Together with independently passed low-clock cases this gives zero-through-three Cs for ONE next foreign. It cannot be iterated across another foreign: the new exit head, core and auxiliary field are not a translated copy of the original source.',
 not_claimed=['No next-foreign transfer for four or more ordinary Cs.','No permanence through a third foreign.','No source-F hook theorem, arbitrary-tail simplicity, trajectory coverage, decreasing fuel or capture.','The source NE and auxiliary outputs need not all persist: the two genuine first-loss gates are retained as branches, not ruled out.'],
 dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS})
(HERE/'three_C_hook_transfer.json').write_text(json.dumps(result,indent=2)+'\n')
print('C3 hook transfer: W80=40 sector+39 field+1 U gate; nextFORE57=53 field+4 extra-tag guards; N2 spent branch and four finite W continuations excluded. Two genuine three-C U-entry controls replay.')
