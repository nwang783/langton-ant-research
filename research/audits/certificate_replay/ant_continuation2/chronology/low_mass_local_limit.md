# Local limits at bounded-mass recurrence lose at least four black cells

Date: 22 October 2026.

Status: analytic corollary of the axial separator theorem and the four-clock
forcing theorem in this continuation. It does not prove eventual highway
formation and does not assert that eventual capture is continuous under
local convergence of fields.

## 1. Quantifiers and statement

Fix one ordinary Langton-ant orbit from a finite black seed. Write its state
as X_t=(B_t,p_t,h_t). Fix an integer K, and suppose there is an infinite
sequence t_j tending to infinity with |B_(t_j)|<=K.

**Local-limit theorem.** There is a subsequence of these checkpoints, a fixed
pose (p_*,h_*), and a finite set B_* such that:

1. every selected checkpoint has pose (p_*,h_*);
2. |B_*|<=K-4;
3. for each finite set F of lattice cells, eventually
   B_(t_j) intersect F = B_* intersect F;
4. for every fixed nonnegative integer T, the trajectories started from
   X_(t_j) and from (B_*,p_*,h_*) have exactly the same positions, headings
   and read colors for their first T updates, once j is sufficiently large.

The hypothesis is impossible when K<4. The stronger joint result excluding
mass four, when invoked, also makes K=4 vacuous. The statement above uses
only the earlier clock and separator theorems.

## 2. At least four cells must escape every fixed box

The axial separator theorem bounds all checkpoint heads in a fixed finite
box. Hence their head terms in the four critical clocks are uniformly
bounded. The forcing theorem says that all four clocks tend to positive
infinity along the checkpoint sequence. Both facts depend on the checkpoints
belonging to **one actual orbit**.

Fix any finite set F. Contributions of cells in F to all four clocks are
uniformly bounded, because F is fixed. Suppose that at infinitely many
checkpoints at most three black cells lie outside F.

Use the two coefficient classes b(q)=-sigma*chi(q) in {+1,-1}. The b=+1
class supplies positive terms to both z=x+y clock components; the b=-1
class supplies positive terms to both u=x-y components. Among at most three
outside cells, one of these classes has at most one cell.

If the outside positive z-class contains at most one cell q, at least one
of 3^(z(q)) and 3^(-z(q)) is at most 1. All other outside contributions to
that chosen z-clock are nonpositive. If the outside positive u-class has
at most one cell, the same argument applies to a u-clock. Thus at each of
these checkpoints at least one clock is bounded above by a constant depending
only on F and the bounded checkpoint-head box. All four clocks cannot tend
to infinity while their minimum obeys this fixed upper bound infinitely
often.

Therefore, for every fixed finite F,

    |B_(t_j) outside F| >= 4

at all sufficiently late checkpoints. The threshold can depend on F. This
does not claim that four individually labeled cells follow permanent
trajectories to infinity; cell labels are unnecessary.

## 3. Extracting the local limit

There are finitely many checkpoint poses, so pass to an infinite subsequence
on which the pose is fixed. Enumerate the countable lattice. Successively
pass to subsequences on which the occupancy bit at the first cell, second
cell, and so on is fixed, and take a diagonal subsequence. Every finite set
then has eventually constant occupancy. Let B_* be the set of cells whose
limiting occupancy is black.

Since every checkpoint has at most K black cells, B_* has at most K cells
and is finite. Apply Section 2 to the finite set F=B_*. Eventually every
cell of B_* is present and at least four additional black cells lie outside
B_*. Consequently

    |B_*|+4 <= |B_(t_j)| <= K,

which proves |B_*|<=K-4.

For any fixed T, the limit trajectory reads a finite set of cells in its
first T updates. At sufficiently late checkpoints the initial colors agree
on that set, and the initial poses agree. Deterministic induction on the
updates gives identical positions, headings and read colors throughout the
T-step prefix. This is finite-time continuity, proved by first-difference
coupling.

## 4. Consequence for K<=6

If K<=6, the limit field has at most two black cells. The all-position
two-black theorem inspected in
`../planar_structure/two_black_corridor_assessment.md` therefore applies
to this **limit state**. It eventually has period-104 translating position,
heading and read-color observations. The one-black subcase is also covered
by Hao Ke's earlier exact one-black result. The relevant primary source for
the two-black claim is
<https://github.com/imfinn/langton-two-black/blob/main/paper/TWO_BLACK_CELLS_REVISED.md>;
the current workspace inspected the source and formal statement but did not
rebuild that Lean project.

Fix a tail-entry time T_* for the limit trajectory. For every finite length
L, sufficiently late selected checkpoints reproduce the limit trajectory
through T_*+L updates. Hence the original orbit contains arbitrarily long
copies of one fixed translating period-104 tail, preceded by the same fixed
finite prefix. This is a conclusion about finite intervals of the original
orbit, with a checkpoint threshold that depends on L.

## 5. The missing step

The preceding quantifiers are

    for every finite L, there is a checkpoint threshold J(L).

They do not give a single J for all L. A remote initial black cell can agree
with the white limit on every fixed finite region, yet interrupt the apparent
highway at a later time depending on its distance. The exceptional one-black
shuttle is a concrete mechanism for a very late reversal after a long blank
highway prefix; it does not contradict the eventual capture of those
particular one-black examples.

An infinite-half-plane capture certificate for the limit field does not
automatically transfer to the checkpoint fields. Their additional remote
black cells may lie inside that half-plane, so the required board equality
can fail arbitrarily far away.

To deduce capture of the original orbit one still needs a theorem controlling
all encounters with the escaping bits, including returns to old wake and
debris. For K=4 the local limit is uniquely blank, and the joint four-black
analysis resolves the specific forced chain of exceptional returns. For
K=5 or K=6 the limit may already contain a nonblank finite seed. Its later
remote collision returns to a different core, and the existing two-black
result does not automatically control every subsequent third or fourth
collision. No continuity assertion about eventual capture, and no general
interaction-closure theorem, is supplied by compactness alone.

