# All-cap first/last-read coupling for autonomous translating fronts

24 October 2026. Author proof and executable controls, awaiting independent audit.
This is a necessary structural theorem, not standard104 classification, a proof
of eventual periodicity, or a nonstandard regenerative construction. No literature
priority claim is made.

## 1. Exact hypotheses and the two boundary graphs

Use the standard white-R/black-L/flip/move rule. Let a COMPLETE bi-infinite WHITE
front have full event period P, full nonzero drift d, finitely many read-cell
classes modulo Z*d, and a finite complete history at every physical read cell.
Every such history starts R and alternates. The retained finite-seed periodic-tail
bridge supplies these hypotheses for a finite-seed periodic suffix after moving
to stable representatives. Conversely its finite-overlap construction realizes
any such complete front with a finite seed; no infinite supplied rail is used.

Write F(v), H(v) for the first and last read times of physical cell v; write
I(v), J(v) for their incoming headings. Let O be the odd-history classes, so their
last read is R and their permanent output is BLACK. Write g=|O|. The retained
stronger output theorem g>=max(8,2||d||infinity)>0 remains in force.

The first-departure map b(v) is the neighbor entered immediately after F(v).
It gives an outdegree-one graph on all read classes. Its complete physical
cycles have winding -1 relative to d, by the retained all-cap first-departure
counterflow theorem. Multiple cycles and all attached trees are allowed.

Define a SECOND graph k as follows. For an EVEN-history cell v, k(v) is the
physical predecessor cell read immediately before H(v). For odd v, give k no
outgoing edge and keep v as an explicit terminal. This is the first-departure
graph of the exactly time-reversed physical trajectory on its WHITE-input
cells. Its BLACK-input terminals are exactly O, not absent cells or free fuel.
The reversing involution changes the invariant checkerboard sector; it is not
an authorized physical return transport.

**Reverse output-root/counterflow dichotomy.** Every quotient k component has
exactly one odd-output terminal, or exactly one simple essential cycle with
winding +1 relative to original d. In particular the number of components is
exactly g+k_L, where k_L is the number of those cycles. An assertion that all
components reach output would need an additional proof excluding k_L>0.
Standard104 has k_L=0, but that observation is not promoted to a general theorem.

Here is a cap-free proof covering the prepared BLACK exterior. On a k cycle,
all reverse first colors are WHITE. Reverse first times along a right corner
increase by exactly 1; along a left corner they increase by 1-4q with q>=1.
These statements use the first use of the SAME physical incoming port, so
arbitrary colors off the cycle do not affect them. A quotient cycle is simple
on the cylinder. For an essential cycle, equal R/L corner counts and summation
force negative winding relative to reverse drift -d, hence winding +1 relative
to d. For a contractible CCW polygon, summation gives ell=4Q>=2ell+8, impossible.
For a clockwise polygon it gives ell>=2ell-8, hence ell<=8. A four-edge cycle is
all R and has positive summed first-time increment, impossible without an initial
head. A simple eight-edge quarter-turn polygon does not exist: its 6R/2L word
would have to be (RRRL)^2, since four successive R already close a proper unit
face; that eight-step word repeats a vertex before closing. Thus there is no
contractible cycle. The finite functional-graph statement proves the dichotomy.
Notice that this argument does NOT turn odd-output BLACK terminals into WHITE.

## 2. An exact first-to-last coincidence capacity

Mark a directed physical edge u->v when the read at u is u's FIRST R and the
immediately following read at v is v's LAST read of either color. Denote this
translation-invariant graph by E. Each vertex has outdegree at most one and
indegree at most one: first departure and last arrival are individually unique.

**Extremal coupling theorem.** If v has both an incoming and an outgoing E edge,
then either:

1. v is a singleton R history; or
2. v is an ODD history with at least three reads and J(v)=-I(v).

In particular, if E_L keeps only E edges whose TARGET's last read is L, then
E_L is a vertex-disjoint MATCHING, not a collection of chains. There is no
multiplicity, drift, width, duration, or seed-size cutoff.

Proof. Suppose u->v->w are E edges. Then the actual read times on u->v are
F(u),H(v)=F(u)+1, while those on v->w are F(v),H(w)=F(v)+1.
If v is nonsingleton, F(v)<H(v). Incoming headings at one physical cell have
one fixed axis and therefore are equal or opposite. If J(v)=I(v), v's earlier
first arrival came from the SAME predecessor u. That required an earlier read
at u, contradicting that the departure into v at H(v) was u's first. Hence
J(v)=-I(v).

If v's last turn were L, its last departure direction would be L(-I(v))=R(I(v)),
exactly the first-R departure direction toward w. The later read at H(v) would
therefore enter w after its claimed last read H(w)=F(v)+1. Contradiction.
Thus v's last turn is R, hence its history is odd. A singleton is necessarily R
by WHITE input and is separately allowed. This proves the theorem. Applied to
two adjacent E_L edges, the middle vertex would be both an even-history target
and one of the permitted odd internal types, which is impossible. Unique
in/out degree then makes E_L a matching. Translation identifies no exception.

Let n_1 be singleton classes; n_o be nonsingleton odd classes with opposite
first/last incoming headings; n_s be nonsingleton odd classes with equal such
headings; and n_e be even classes. Put A=n_1+n_o and B=n_s+n_e. Degree counting
at the COMPLETE quotient vertices gives the all-cap capacity

    2|E| <= 2A+B,       |E| <= A+floor(B/2).

Every E cycle is a first-departure cycle, so has winding -1, and by the theorem
all its vertices belong to O. It contains an opposite-heading nonsingleton:
a cycle made solely of singletons would have every first-time increment +1,
contradicting its negative winding. If c_E is the number of E cycles, then

    n_o >= c_E,       g >= sum(lengths of E cycles) >= 2||d||infinity*c_E.

On EACH such cycle C, exact chronology further gives

    P = sum over v in C (H(v)-F(v)) - |C|.

These are live positive-output constraints. They do not present the already
impossible g=0 case as a new exclusion.

## 3. The correct joint counterflow bound, including overlap

Select any k_F distinct b cycles and any k_L distinct k cycles. Reverse the
latter edges to orient them as ACTUAL original steps. Both selected families
then have winding -1. Let L_F,L_L be their summed lengths, and k=k_F+k_L.
A b edge selects the actual traversal at the source's first R. A reversed k
edge selects the actual traversal into the target's last L. Geometrically
coincident edges might be DIFFERENT traversals and must not be collapsed.

Let C count only coincident SELECTED EVENT CLASSES, i.e. an actual traversal
selected by both families. These coincidences are precisely E_L edges within
the selected cycles, so the theorem proves

    2C <= min(L_F,L_L,n_e).

Let C_H,C_V be their horizontal/vertical counts, delta=C_H-C_V, and let
(e_x,e_y) be the sum of their actual directed unit movement vectors. Then

    P >= L_F+L_L-C
         +max(2*|(1+k)*d_x+e_x|-delta,
              2*|(1+k)*d_y+e_y|+delta).

Proof. Each family selects at most one occurrence of an actual event, since
its cycles are vertex-disjoint. Remove each DISTINCT selected occurrence from
the full P-event inventory, retaining every other occurrence. The remaining
inventory is NONNEGATIVE, with size P-L_F-L_L+C and total displacement
(1+k)*d+(e_x,e_y). It need not be a balanced graph, one path, or a legal new
ant trace. Each individual selected cycle has equal horizontal and vertical
counts. The residual horizontal-minus-vertical count is therefore delta.
If its size is r, its horizontal/vertical counts are (r+delta)/2 and
(r-delta)/2; each must dominate the absolute corresponding displacement.
This proves the bound WITHOUT treating the residual as an autonomous front.

If C=0, this reduces to the additive bound

    P>=L_F+L_L+2(1+k)||d||infinity>=2||d||infinity*(1+2k).

Adding the two old counterflow bounds without an overlap correction would be
unjustified. The matching theorem supplies exact information about that
obstruction, not permission to ignore it.

## 4. Executable author controls and concrete failed connector

check_extremal_read_coupling.py reconstructs the exact complete stable histories
of standard104,208,312 in four rotations, computes all three graphs and checks
the capacities, windings, cycle-age identities and corrected joint bound. It
also checks 120 actual finite factors of 3000 reads each, with finite initial
BLACK support, and retains the eight encountered initial/final-boundary
exceptions rather than importing the boundary-free theorem into a finite factor.
A literal initially blank factor has an isolated marked E_L edge at ticks
1723->1724; LAST here means within those 3000 reads, not the whole future.
This demonstrates that the local mechanism is not simply an absent pattern.

A separate one-candidate diagnostic tests the supplied actual D102 connector
and its exact read-event inverse, not a period scan. Each has EIGHT full-drift
classes whose stable turn histories contain consecutive equal letters. Thus
neither infinite repetition is a physical ant word even on an arbitrary
prelaid infinite board. The inverse has positive growth8 but still fails this
stronger exact alternation test; mass/output arithmetic does not repair it.
The finite17-cell prepared D102 witness remains valid. No finite-factor result
is being converted into recurrence or a global cap-four exclusion.

## 5. Remaining classification obligation

No theorem here rules out k_L>0, bounds total visits or the full width, forces
standard104, or decides that arbitrary finite seeds become periodic. The
actual remaining autonomous-controller question is whether all ordered local
histories, both boundary graphs, all paired lifetimes, one connected event
orbit, and positive output can close into a nonstandard translating controller.
The counterflow dichotomy and extremal matching are necessary constraints on
that question, not a replacement for complete spatial and chronological closure.
