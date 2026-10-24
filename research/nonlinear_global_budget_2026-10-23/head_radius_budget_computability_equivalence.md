# Head-radius budgets: exact equivalence and where totality is missing

23 October2026. An effective reformulation, NOT a new proof of universal capture.
The radius here is explicitly anchored at the INITIAL HEAD.

## 1. Effective state class and recognizable capture

Normalize the initial head to(0,0), retain its four possible headings, and let

    C(r,m)={ (B,0,h): B subset [-r,r]^2, |B|<=m, h in{0,1,2,3} }.

This is a computably enumerable FINITE set for every pair of natural numbers.
Its size is4 times the sum of binomial((2r+1)^2,j) for0<=j<=min(m,(2r+1)^2).
Black-set diameter alone is not the same radius: if head-to-board distance is
unbounded it does NOT give this finite normalized state class.

An exact standard104 tail from a complete finite state is decidable. For each
of the finitely many cyclic phases and proper rotations, group its104 read
slots modulo the nonzero drift. Check complete-list alternation, every finite
eligibility fringe, and every existing black cell on every future required-
white ray. A black cell outside those rays is retained, not discarded.
The arithmetic is finite because the current board is finite. If it passes,
it certifies the ENTIRE infinite standard tail, not a long sampled period.

Therefore eventual standard capture is semidecidable for each finite input:
simulate it, testing for this whole-board certificate at successive times.
A failed test does not certify noncapture. A run that never finds a certificate
might simply be slow; no finite timeout establishes noncapture.

At time zero compute the actual inverse ten turns by reversibility. Maintain
that history while simulating. Once a true standard-tail certificate is found,
advance ten further standard turns. Every later11-window is cyclic standard,
so every future K event has now been counted exactly. Thus total future K is
computable on the semidecidable domain of captured inputs.

## 2. One explicit partial maximum algorithm

For each C(r,m), run all its finitely many capture searches in parallel. When
ALL have returned a certified tail, finish their ten-turn seams and output:

* the maximum exact total future K over the class;
* the maximum certified standard-entry time (a capture-time upper bound).

Call this partial computable procedure Q(r,m). It halts if and only if EVERY
state in that finite class captures. No claimed global theorem makes Q total
at present. Enumerating the states or writing Q does not solve its totality.

## 3. Equivalent universal assertions

Using the independently retained renewal equivalence on finite inputs

    finite future K if and only if eventual standard104 capture,

the following assertions are equivalent:

A. Every finite input eventually captures.
B. Q(r,m) halts for every r,m.
C. For every r,m there exists SOME finite uniform K bound on C(r,m), with no
   computability initially required.
D. There exists a TOTAL COMPUTABLE function G(r,m) bounding total future K
   on every state in C(r,m).
E. There exists a TOTAL COMPUTABLE uniform capture-time bound T(r,m) on C(r,m).

Proof:
A implies B by finite parallel termination. B implies D and E by the actual
outputs of the partial computable Q, now proved total. D implies C trivially.
C implies A because every finite input belongs to one such finite class and
finite K implies capture. E implies A directly. These implications account
for every assertion, so all are equivalent.

In fact r alone suffices because m<=(2r+1)^2. Retaining m may improve numerical
bounds but does not weaken the logical universal assertion. A true bound can
always be monotonized by taking the maximum over all smaller r,m.

A proved explicit computable G would of course be substantive: it would prove
A. The vacuous statement that one could enumerate configurations if A were
already known is not such a proof. Likewise a program that appears to return
for many small radii is a collection of finite controls, not a totality proof.

## 4. What the mass-only counterexample changes

The original184-cell family has radius70n+295 and unbounded K. Hence replacing
r by mass alone is strictly stronger and is now FALSE. Even restricting the
supremum to already bistandard inputs does not rescue it. The original family
has independently certified forward and backward standard tails, so b(184)
is infinite; the older12-completion corollary b(196)=infinity remains valid
but is no longer sharp.

A head-radius budget has no such contradiction: the same family forces at
least linear growth in r at mass184. It also shows why first-root count,
transverse width, and drift-phase projections cannot replace the missing
longitudinal distance in a spatial rank.

## 5. Precise mathematical work still required

The equivalence provides neither an explicit upper formula nor an invariant,
confinement theorem, amortization inequality, or well-founded order proving Q
total. A useful geometric proof must supply one of those independently of
assuming capture. For instance it might bound the total repeatedly reusable
longitudinal archive capacity by initial geometry, while retaining dormant
branches and every finite cap edit. The accompanying interval note identifies
one locally valid no-refill rule and the exact unresolved funding/renewal
obligations; it does not claim to close them.

## 6. A crucial different question: bounds only on POSITIVE inputs

Define instead

    P(r,m)=max({N(X):X in C(r,m) AND X captures} union{0}).

This maximum is finite UNCONDITIONALLY because the class is finite and each
capturing member has finite N. It is not an all-input bound: it ignores every
hypothetical noncapturing member. Merely asserting existence of this finite
function says nothing about universal capture.

The retained unconditional next-K map R_K is TOTAL computable. It returns the
first future event's complete after-state, or a terminal symbol if no further
event exists. Its totality uses the no-event language theorem and exact tail
certificates, not universal termination of its iteration. Therefore for any
finite q, 'at least q future K events occur' is decidable by q applications,
always retaining/reconstructing the true inverse ten letters at renewed cuts.

It follows that these two assertions, distinct from universal capture, are
equivalent:

This is the head-radius/mass reformulation of the already audited positive-
instance encoding-size metatheorem in
`../computability/adjacent_renewal_normal_form.md`, Section5; it is not a new
undecidability or termination theorem.

F. The capture predicate on finite inputs is decidable.
G. There exists a total computable majorant g(r,m) of P(r,m).

G implies F: compute r,m for X and run the finite-threshold decider for
q=g(r,m)+1. If YES, X cannot be a capturing positive instance, by the majorant.
If  X has at most g(r,m) events and hence captures by renewal equivalence.
Both branches terminate unconditionally.

F implies G: enumerate the finite C(r,m), use the decider to discard negative
instances, and compute exact total K for each retained positive instance by
its terminating certified capture search. Taking the maximum computes P
itself, not just a majorant.

Universal capture implies decidability trivially, but a decidable mixture of
capturing and noncapturing inputs would also satisfy F/G. Thus a positive-only
computable radius majorant must NOT be called equivalent to universal capture.
A computable majorant does not automatically come with a proof that all inputs
are positive. The ALL-input and POSITIVE-only formulations must stay separate.

## 7. Already retained quantitative count-to-clock transfer

The independent earlier theorem
`../computability/elementary_adjacent_renewal_bound.md` gives an explicit total
next-event-or-terminal clock. With

    A0=69426531, C0=543959, Lambda=138853063,
    w=m+r+1+C0,

a capturing input with exactly k true-history future K events reaches a genuine
certified standard checkpoint within

    w*(Lambda^(k+1)-1)/2

physical reads. This is a retained quantitative result, not newly proved here.
It shows directly that an ALL-input count bound G supplies an explicit
capture-time bound by substitution. It also bounds positive-instance capture
times using a positive-only majorant, without claiming negative instances halt.

The unresolved global mathematics is the number of event renewals or the
termination of their iteration, not whether one next renewal can be computed.
The184-cell example shows that no bound ignoring longitudinal input geometry
can control that iteration even on known bistandard positive inputs.

References: the finite-K/capture equivalence and unconditional finite-threshold
decider are in `../computability/adjacent_defect_quantitative_compactness.md`,
Sections4--4.1; their language dependency is
`../word_stabilization/adjacent_defect_highway_theorem.md`.
