# Second-R gate-or-corridor coupling on maximal C plateaus

23 October 2026, 12:41 UTC. New analytic structural result and exact finite
controls, submitted for independent reconstruction. No front exclusion,
standard104 uniqueness, or finite-seed capture conclusion is asserted.
The full actual drift and event period are retained throughout.

## 1. Scope and corrected stream normalization

Work with a COMPLETE bi-infinite WHITE translating Langton front, actual
period P and nonzero actual displacement d. Assume at most four reads per
physical cell. Its complete histories are R, RL, RLR, RLRL. Number reads
from zero. Use the signed stream normalization

    f(e) = h(C_right) - h(L_left),
    H(C) = h(C),  H(L) = h(L)+1.

The signed global-maximum defect theorem gives max_C h = max_all H = M.
Consequently H(L)<=M, equivalently UNSHIFTED h(L)<=M-1. It does NOT give
H(L)<=M-1. Thus a max-C face has positive flow on every boundary edge,
and a contact between two max-C faces is active. Shifted L equality at M
is retained, including every L supplier described below.

The signed cap-four local table gives: every R at a cell incident to a
max-C face turns around a max-C face. Indeed the two C heights differ as
their R counts do; with at most two total R reads their count pairs are
(1,0), (1,1), (2,0), or reversals. The first pair has no second R; the
balanced pair sends its two R reads around different max faces; the last
pair sends both around the same higher max face.

## 2. Exact paired-R predecessor, without deleting source L events

For EACH actual R read at v, let j be the complete rank of the actual
source event immediately preceding it, at neighbor u. Retain that exact
supplier event and its exact physical port ordinal. Replace its source
rank j by its preceding paired R rank

    p(j) = j-j mod 2.

Thus an R0 or L1 supplier is paired with source R0; an R2 or L3 supplier
is paired with source R2. This defines an outdegree-one DEPENDENCY map
from target R nodes (v,0)/(v,2) to source paired-R nodes. It is not an
R2-only functional graph. In actual-edge orientation the selected arc is
u->v, but its source departure remains rank j, not the earlier paired R.

Let T_r(v) be the actual time of R rank r. If the supplier is paired with
source R_s, exact chronology gives

    T_r(v) = T_s(u)+1+4q,
    q=0 for a source R supplier,
    q>=1 for a source L supplier.

The multiple-of-four statement is the signed physical zero-displacement
return fact. In particular paired-R time strictly DECREASES under the
dependency map. The construction is equivariant under the actual full d.

If v touches a fixed max-C corner-connected component K, the R at v uses
a face F in K. The supplying edge u->v is a boundary edge of F, so u is
also incident to K. BOTH R reads at u, when present, select maximizing C
faces, which belong to K because all max faces at u corner-connect.
Therefore the entire paired-R dependency remains in this SAME K. The
same localization works for any active C-superlevel component, with its
original threshold, by the same cap-four maximum rule.

This is an actual rank-two chronological coupling retaining all source-L
suppliers. It does not assert that each second R has a second-R supplier.

## 3. Restricting to R2: explicit gates or positive essential corridors

Retain only target nodes (v,2). Stop a dependency path when its next node
is R0. Call that final arc a GATE. Its actual supplier is R0 or L1. All
other arcs have source paired rank R2 and actual supplier R2 or L3.
There are finitely many R2 classes on the full-drift cylinder. Therefore
every R2 component either reaches a gate or contains a directed R2 cycle.

An R2 cycle has distinct physical cell classes: there is only one R2 node
per physical class. Its physical unit edges are therefore a simple
embedded cylinder circle. If its dependency orientation winds k, strict
time descent gives kP<0. Embedded simplicity gives k in {0,+1,-1}, so
k=-1. Reversing it, its selected actual-edge occurrences form a winding
PLUS ONE essential cycle. It need not be a consecutive ant time interval.

Every such cycle stays in the same max-C component K. However an
essential max-C plateau DOES NOT, by this argument, force an R2 cycle:
its R2 forest may instead terminate at R0 gates. This is the precise
remaining branch of the dichotomy, not an ignorable exception.

For a homogeneous R2 cycle of length ell, with source-L3 delays q_i,
exact summation gives

    P = ell+4 sum q_i.

No term may be added to a separately proved chronological bound unless
the payments are separately proved disjoint.

## 4. The second-R ordinal switch law and exact gate classification

For any two-R white cell, let i2,o2 be the incoming/outgoing port ordinals
of its R2 event (counted chronologically from one at each physical port).
Only ranks0,1 can precede that event at those ports. If R0 and R2 use
opposite incoming headings (flat max-C contact), then

    {i2,o2} = {1,2}.

If R0 and R2 use the SAME incoming heading (height-two boundary defect),
then

    {i2,o2} = {2,3}.

These are exact, not just bounds. In the flat case R0 contributes zero
to either R2 port; L1 contributes to exactly ONE of them. In the same-
face case R0 contributes to BOTH R2 ports and L1 again contributes to
exactly one. This proves both identities for length3 and length4 alike;
rank3 cannot change earlier ordinals.

A source R0 has output ordinal1. A source L1 has output ordinal1 if it
uses the opposite output port from source R0, and ordinal2 if it uses the
same output port. Exact edge matching gives the following gate cases:

- Flat target, i2=1: supplier R0, or L1 whose output differs from source
  R0. In the latter case the source is itself flat at the selected max
  face: its first R selects the other max face and its later R2 the face
  used by the gate edge.
- Flat target, i2=2: supplier L1, with the SAME output as source R0.
- Same-face defect target: only i2=2 can be a gate, and supplier MUST be
  L1 with the same output as source R0. If i2=3, source paired rank must
  be R2, so no gate is possible there.

The 78 local max-C edge-compatible pairs in paired_r_controls.json retain
all source ranks0,1,2,3. In particular flat targets can receive L3 from a
flat source; defect targets can receive L3 from flat or defect sources.
No general R-to-R matching is substituted for these suppliers.

## 5. A same-face gate is a synchronized two-cell first-return bracket

Consider the final gate case above. Write u for source, v for target,
S0/S1 for source R0/L1 times and T0/T1/T2 for target R0/L1/R2 times.
The gate uses edge ordinal2. Its source's ordinal1 departure is R0;
its target's ordinal1 arrival is R0. Exact edge matching forces

    T0=S0+1,  T2=S1+1,  S1-S0=T2-T0.

Source R0 and L1 incoming headings are opposite, since they have the same
output despite opposite turns. Target R0/R2 have one heading h, while
its L1 has heading -h, since i2=2 rather than3. Thus the source's ONE
first-return interval brackets the target's TWO consecutive returns.
In the paired-R graph this creates a genuine coalescing fork: target R0
and target R2 both depend on source R0, via different actual supplier
occurrences (source R0 and L1). It does not create a new root.

There is a sharp local lower bound, allowing arbitrary colors away from
these two specified initially-white cells:

    S1-S0 = T2-T0 >=16,
    T2-S0 >=17,  equivalently q_gate>=4.

Here is a complete short-return check of the inequality, with a separate
literal six-black-cell positive control in gate_word_enumeration.json.
Genuinely rotate/translate to u=(0,0), incoming N, its R0 at time0, and
v=(1,0), its R0 incoming E at time1. The first return to u must arrive S.
The root-return span is a positive multiple of4. All color-consistent
first-return words of length4/8/12 with initial RR and final incoming S
are:

    length4: none,
    length8: none,
    length12: RRRLRRLRRLRR, RRLLRLLRLLRL.

Neither length12 word reads v after its first read at time1. Hence neither
can supply the required target L1 before the source returns. Length16
is achievable: the unique normalized gate word is

    RRLLLLRLRRLRRLRR

followed by source L at16 and target R at17. Initial black cells are
(-1,-1),(-1,0),(0,-1),(1,-1),(2,-1),(2,0); all others are white and the
ant starts at u facing N. The complete two-cell histories through time17
are source R@0(N),L@16(S), and target R@1(E),L@5(W),R@17(E). This is an
exact finite factor, NOT a complete white translating front. The small
return table is exact exhaustion over at most2^14 turn suffixes, not a
period/drift scan or extrapolation. The 16 bound is local sharpness under
the stated arbitrary-other-color scope, not claimed sharp for translating
fronts. The exact finite table is independently reproducible.

Within any complete paired-R dependency cycle, the exact clock identity
may use this stronger q>=4 at each same-face gate, because its edge
increments telescope. It does NOT make gate costs globally additive over
unrelated paths, and does not bound the number of gates.

## 6. Conditional third-family integral subtraction

Let A be any selected first-arrival backbone cycles (actual winding+1),
B any selected first-departure cycles (actual winding-1), and C any
selected homogeneous R2 cycles from Section3 (actual winding+1). Let
a,b,c be their counts and L_A,L_B,L_C their total edge lengths.

The previously signed theorem makes the A/B families edge-disjoint.
The C family may share PHYSICAL edges with either family, but cannot
share their selected edge OCCURRENCES:

- Every A occurrence arrives at target R0; every C occurrence arrives
  at target R2. They are different actual event occurrences.
- Every B occurrence departs from source R0; every C occurrence departs
  from source R2 or L3. Again they are different actual occurrences.
- Different C cycles have disjoint R2 node sets, hence distinct suppliers
  and target events, so they do not reuse an occurrence.

Subtract these selected occurrences from the complete nonnegative integer
physical flow. The result is balanced, nonnegative, and has full homology
1-a+b-c. Its horizontal and vertical edge totals are equal (checker
orientation), and its displacement is (1-a+b-c)d. With D=||d||infinity,

    P >= L_A+L_B+L_C+2D*abs(1-a+b-c).

No physical-edge-disjointness between C and A/B is assumed or needed;
occurrence disjointness is enough. This supplies a safe additive register
for ACTUAL completed R2 cycles. It supplies nothing from a gated R2 tree
until an additional independent resource bound is proved.

## 7. Exact controls and remaining obstruction

paired_r_controls.py checks every length<=4 local history (24 two-R rows
in one parity, with all headings), the ordinal switch law, all78 max-C
edge-compatible source/target pairs, and actual complete standard fronts
at full drifts(2,2),(4,4),(6,6) with periods104,208,312. For the cap-free
all-R paired graph on the standard104 front, all58 R nodes feed TWO R0-
only cycles of length4 and winding+1; each has two L suppliers and q-sum25.
All later-R nodes drain into those old cycles. This is not a cap-four
positive control (standard104 has max multiplicity10), but it is an exact
warning that introducing all-R paired nodes need not create a new cycle.

A separate all-white blank-ant control is especially direct: at time50,
source(1,-1) has history R@2(S),L@50(N), both departures W; its L1 supplies
target(0,-1)'s R2 at51. The target history is R@3(W),L@15(E),R@51(W), a
same-face defect. Thus the dangerous defect-gate coupling occurs in an
actual finite-seed ant, not merely a free local routing table. No max-C
plateau or eventual cap-four claim is made about that prefix.

The new exact stopping point is therefore: second-R behavior on a max-C
plateau is a gate forest or positive essential corridor; same-face gates
are synchronized, cost at least16 actual steps, and coalesce into first-R
structure. The open missing advance is a nonstandard-only bound or a
contradiction for those potentially recurring gate forests. Positivity,
first-R roots, and a bare second-R cycle assertion do not supply it.

## Source and artifact integrity

Inherited signed sources are unchanged:
../periodic_classification_new/cap_four_first_read_stream_backbone.md
../periodic_classification_new/cap_four_bidirectional_stream_corridors.md
../periodic_classification_new/white_front_stream_defect_criterion.md
../periodic_classification_new/dual_first_backbone_edge_separation.md
../periodic_classification_new/white_front_first_read_speed_bound.md

All new source/JSON/note hashes are frozen in manifest.sha256. No original
proof document, paid resource, or independent cap-six
replay was changed or duplicated.
