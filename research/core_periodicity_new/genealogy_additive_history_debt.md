# Additive ancestry transport debt from the joint history exclusion

23 October 2026 09:09 UTC. Analytic consequence of signed JO/KV/KP and LH;
independent analytic scope confirmation PASSED at09:10UTC. No new finite search is involved.

Consider an auxiliary selected-input ancestry path whose initial node is a
produced residual identity, so every edge's parent is produced. For each edge,
let a be its child packet, n its source-included/consumer-excluded C-birth gap,
and v its actual parent-to-child displacement. The chosen-input table gives

packet a          D  DC  V  VC  VCC U  UC UCC
minimum age A_a   3   3  3   3   5  5   5   5
max Linf D_a      2   3  2   3   3  3   3   4
A_a - D_a         1   0  1   0   2  2   2   1.

These are per-edge necessary inequalities; no physical attainment of an equality
case is asserted.

Let p count occurrences along this path of the exact producer-role triple

VCC output(0,0), heading h;
D output(2,0), heading h+1;
VC output(2,5), heading h+2,

with the intermediate inputs being the selected ones. The identity alignments
uniquely fix their relative poses to the LH configuration. Each of its two
birth gaps is congruent3 modulo4 and at least3. LH forbids the pair(3,3), so the
sum is at least10 instead of its separate-minimum sum6. Such triples cannot
overlap in edges along one path, because their packet-type word VCC,D,VC has no
nonempty proper prefix equal to a suffix. Therefore their four-C surcharges add:

Delta C >= sum_edges A_a +4p.

Triangle inequality and the literal distance table then give

Delta C - ||Delta position||_infinity
 >= N_D +N_V +2(N_VCC+N_U+N_UC)+N_UCC +4p.

Counts here refer to CHILD packet types along this ONE auxiliary ancestry path.
They are not global packet frequencies or elapsed-time counts. In particular
DC/VC generations receive no charge in this coarse norm inequality. The separate
heading-sensitive speed bounds retain more directional information.

Initial entry identities are exempt from produced-input age rules. Do not apply
the displayed age sum to an initial-entry edge. A safe root-to-leaf version bounds
the first output's distance from its entry root by4, and applies the displayed
debt only after that first output. Thus a leaf at C clock b lies within distance
b+4 minus the subsequent path's weighted generation/history debt from its entry
root. This is a conditional support bound, not an upper C count.

No finite number of roots bounds total descendants; no dormant branch, hidden U,
or restored-token ancestry is omitted. The inequalities remain compatible with
unbounded C and do not supply global capture or a V1/U1 funding-record closure.
