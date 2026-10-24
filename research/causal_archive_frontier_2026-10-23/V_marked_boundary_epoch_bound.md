# Marked V boundaries force a uniform epoch bound

23 October2026,20:48 UTC. Author theorem submitted for independent review.
NEW local dependency: V_C_same_heading_exclusion_frozen_20261023_2043.
No assertion about arbitrary finite-seed capture is made.

## 1. Scope and the exact local ingredients

Work in an actual complete recurrent-eight factor beginning with U, UC or UCC.
Its corrected atomic-center path is simple. Packet names and distinguished
inputs are the signed conventions. Let N_j,d_j,v_j,u_j count packet starts
and D/V/U bases at full-source ENTRY C clock j. Skipped clocks have0 counts.

Use these signed interfaces:

1. Produced distinguished input source age is at most294, and no produced
   input from the same C clock can be spent. Parallel heading sources have
   even age2,4,...,294, at most147 cohorts.
2. At most4851 packets in a consumer epoch have ANY perpendicular-source input.
3. At most3 odd extra C-tail identities are born per SOURCE EPOCH. There is
   at most one positive-C full packet per source clock. Parallel distinguished
   slots have odd coordinate sum, so D-base outputs contribute none.
4. U-base outputs cannot selected-feed any parallel V/U-family packet.
5. A V base can selected-feed parallel V/U only through original C=(2,1),
   once. Its A output has no parallel selected consumer; B feeds only D/DC
   at age4. The U arm selected-feeds only plain D at age6.
6. Original V-base C cannot selected-feed same-heading V or VC. Such a V/VC
   child must be opposite-heading at source-relative(3,3,S). Two consecutive
   C-to-V/VC child edges therefore return to the first source's exact full
   entry pose and center, impossible by simplicity. VCC child edges are NOT
   excluded or ignored.

The first five ingredients already give A=4851+3*147=5292 and the
coefficient-one actual spending inequalities

    v_j+u_j <=A+sum_even2..294 v_(j-e),                       (1)
    N_j <=A+sum_even2..294 v_(j-e)+v_(j-4)+u_(j-6),            (2)

after entry funding expires. With entry funding present add at most r0, the
number of original residual identities, to each inequality. The parent
birth clocks never reset at internal C tails.

## 2. Actual parallel genealogy and marked nodes

Construct the graph on actual V-family producers only. Give Q a parent P iff
Q's distinguished input is P's genuine original BASE-V C output and their
full-entry headings are parallel or antiparallel. Every node has indegree at
most1 and outdegree at most1: the selected input is unique and C is spent only
once. Clocks strictly increase on parent edges. No physical connector between
parent and child is assumed.

Call a node an EXTERNAL ROOT if it has no such parent. Its selected input is:

- an untouched entry identity; there are at most r0 such roots in the ENTIRE
  factor, by once-only entry spending;
- or a perpendicular-source identity, at most4851 such root packets per clock;
- or a parallel extra C-tail identity, at most3*147=441 per consumer clock.

There is no missing parallel-base case: D has no odd base output, U has no
parallel reproductive selected port, and V-base A/B are excluded by the causal
r-lock. V-base C would give a parent by definition. Thus at most A produced-
input external roots occur per clock. This is not an assumption that total
external roots are bounded globally.

MARK every external root and every POSITIVE-C V-FAMILY boundary node (VC or
VCC). There is at most one such positive-C boundary node at any clock, even
if an epoch contains arbitrarily many plain D,V,U packets. Hence marks per
clock are bounded by A+1, apart from the globally at-most r0 entry-input roots.
A root that is also a boundary is counted only once; double-counting in this
upper bound is harmless.

## 3. Every V node is at most one edge after a mark

A marked V node needs no ancestor. Any unmarked node Q is a PLAIN V with a
parallel C parent P. If P is marked, done. If P is unmarked, P is also plain V
and has some parallel C parent G. Then G->P->Q are two consecutive edges with
V/VC children, contradicting ingredient6. Therefore P MUST be marked.

This handles VC explicitly: it is marked as a positive-C boundary, never
silently discarded. VCC is also marked. No chain-length estimate from a
coefficient-one scalar recurrence is being substituted for this exact local
parent decomposition.

At a fixed consumer clock j, map each V node to itself if marked, otherwise
to its marked parent. Different V nodes at that clock map to DIFFERENT actual
marks: a mark's C can have only one child, and the mark itself cannot be at
the same clock as a child because edge age is positive. Every assigned mark
lies at one of the148 clock labels

    j, j-2, j-4, ..., j-294.

Consequently, for EVERY actual epoch,

    v_j <=r0+148*(A+1) =r0+783364.                           (3)

The r0 term counts entry-input marks across all148 labels jointly, not r0
per label. Negative source clocks contribute0.

## 4. Eventual seed-independent constants

Let H=20R+211 be the signed untouched-entry INPUT horizon, with R the initial
entry residual radius about the first head. For j>H+294 every candidate
assigned mark is born after entry funding expires. Equation(3) sharpens to

    v_j <=M=783364.                                         (4)

For j>H+594, both the direct source clocks in(2) and the source clocks needed
to bound u_(j-6) via(1) are after H+294. Their maximal combined age is300.
Equations(1)-(2) then give

    N_j <=2A+295M =231102964.                               (5)

Only eventual uniformity matters; this deliberately conservative constant is
not claimed optimal. A global bound with the entry exception retained is also
available, but unnecessary for the infinite-factor argument. No bound on
active-token count, recent spatial width, original root genealogy depth, or
current archive component count was assumed in deriving(3)-(5).

For a phase refinement, an unmarked plain-V child has opposite heading, so its
positive parent ages lie in{2,6,10,...,294},74 labels rather than147. Self
marks add one label, giving75*(A+1)=396975 in place of783364 after startup,
and117118209 in place of(5). The proof does NOT need this refinement; the
148-label conservative bound is the main stated interface.

## 5. Consequence and exact stopping boundary

The already independently signed infinite-factor theorem says that an infinite
actual U-entry retained-eight factor cannot have eventually uniformly bounded
epoch lengths. Its proof uses the TRANSITION-COMPLETE330 relevance induction
on the original real exterior, a finite normalized parser under an epoch
bound, and exclusion of both zero-drift and nonzero-drift periodic reduced
cycles by actual center injectivity/tangent winding. Thin-chord linear distance
alone is NOT used to exclude a translating period.

Assume an infinite U-entry retained-eight factor. Finite-C duration implies
its C clock tends to infinity, so its finite entry horizon and the startup
margins in section4 eventually expire. Equation(5) provides precisely the
uniform epoch bound excluded by that signed theorem. Contradiction.

THERE IS NO INFINITE ACTUAL COMPLETE-EIGHT FACTOR BEGINNING WITH U/UC/UCC.

Equivalently, within the complete-eight language, every actual U-family entry
has a finite remaining retained factor before language exit. This says nothing
by itself about arbitrary fine-ant behavior AFTER that language exit. It does
not prove eventual entrance into the retained-eight language from arbitrary
finite seeds, make original strict V1/U1 funding true, or establish global
standard104 capture. Those broader interfaces must remain separate.

## Independent dependencies and reproducibility

The checker reconstructs the external-root partition, finite marking/depth
argument,148 and75 allowed labels, and every integer startup/epoch constant.
It uses the immutable local certificates rather than guessing a spatial box
or searching a finite support word. The graph argument is quantified over all
actual finite factors, not inferred from finite controls.
