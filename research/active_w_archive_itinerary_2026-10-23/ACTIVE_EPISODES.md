# Active w episodes separate local motion from dormant-archive renewal

23 October2026. Author global structural lemma and CONDITIONAL sufficient
criterion, frozen for independent review. This applies to arbitrary actual
finite-board trajectories, without a marker language or presumed periodicity.
It does NOT prove that its additional sustained hypotheses hold.

## 1. Definitions at every physical cut

States are pre-update, with the COMPLETE actual finite black field retained.
Use the paired-cursor convention. The active w vertex, in physical coordinates,
is

    w_t = p_t + r_h(1/2,-1/2).

Let C_t be the COMPLETE black-edge component of w_t in its fixed diagonal
lattice, with C_t empty if w_t is isolated. Its mass is its number of edges.
A black lifetime is born at an actual R and ends at the NEXT read of that
cell, an L. Deletion and later rebirth create distinct lifetimes.

For a fixed current lifetime e, call a cut ACTIVE if e belongs to C_t and
DORMANT otherwise. An active or dormant episode is a maximal consecutive
interval of integer cuts of that type DURING that lifetime. Episodes include
ALL fine cuts, including every intermediate R of a four-R reset. They are not
compressed-block lengths or a stack order on archives.

Use the established no-bounded-orbit theorem for the classical finite-support
ant. For definiteness, an elementary uniform escape deadline for an n by n
cell square is

    Q(n)=4n^2 2^(n^2).

Indeed, before first exit all exterior cells are unchanged, and there are at
most4n^2 2^(n^2) possible interior-field/head/heading states. Staying inside at
Q(n)+1 consecutive cuts repeats a COMPLETE state and would produce a bounded
periodic orbit. This is impossible. A sharper retained strict square clock
may replace Q; no improved clock is claimed here. Put

    H(M)=Q(2M+1),     M>=1.

## 2. Exact metric lemma, including R-only motion

**Lemma1.** If a fixed physical black edge e has midpoint x and belongs to C_t
with |C_t|<=M, then

    ||p_t-x||_infinity <= M.

**Proof.** Choose the closer endpoint of e by a shortest w-graph path from w_t.
Such a path uses at most M-1 edges: it never needs e itself, since it stops at
its first endpoint. Each diagonal edge changes each physical coordinate by
at most1. That endpoint is at infinity-distance1/2 from x, and p_t is at
infinity-distance1/2 from w_t. The triangle inequality gives
(M-1)+1/2+1/2=M. If the cursor is an endpoint, the path has length zero. No
claim about the geometry of an inactive component is used. QED.

This holds at EVERY physical cut. R keeps w fixed but moves p among its
adjacent corners; the half-unit head correction already covers this. During
an RRRR reset, a fixed active e still pins the physical head in the same box.
An isolated w cursor cannot contain an active black edge at all.

**Lemma2 (uniform active-episode bound).** If |C_t|<=M at every cut of one
continuous active episode of e, that episode has at most H(M) integer cuts.

**Proof.** Lemma1 confines every one of those head positions to the FIXED
square x+[-M,M]^2, which contains(2M+1)^2 cells. An episode of H(M)+1 cuts would
contradict the uniform square escape deadline. All exterior fields remain on
the board and are allowed to be arbitrary; the clock only uses that no
exterior cell has been read before exit. QED.

The contrapositive is useful without any global bound: a lifetime that remains
continuously active for more than H(M) cuts must encounter an active component
with MORE than M edges during that episode. Long active ancestry cannot hide
inside one uniformly small continuously active component indefinitely.

## 3. Exact gates into and out of dormancy

**Lemma3.** A surviving active lifetime can become dormant only at an L that
deletes a w bridge and leaves its side behind. A surviving dormant lifetime
can become active only at an R importing the FULL component at the new
edge's other endpoint.

**Proof.** At L, the w cursor crosses the deleted edge. The new active component
is exactly its arrival-side component in the old C_t minus that edge; no old
inactive component becomes connected by a deletion. If the deleted edge is
nonbridge, every surviving edge in C_t remains active. At R, the new edge is
incident to the unchanged w cursor. All old active edges stay active. If its
other endpoint lies outside the old active component, insertion joins in
exactly that endpoint's whole old component, possibly empty. If it lies
inside, no dormant component is imported. These statements use the entire
embedded field, not an interface summary. QED.

Thus every completed dormant interval of an R-born lifetime records a real
bridge-cut archival departure followed by a real R reconnection. Its duration
is not an abstract profile wait; its reactivation count is not a LIFO depth.
This is compatible with the signed serial-chain/archive-splice calculus,
including non-LIFO archives and temporary R-arm imports left behind at the
following bridge L.

## 4. A sustained itinerary criterion implies eventual translation

**Conditional theorem.** Suppose there are integers T>=0, M>=1, A>=0, J>=0
such that:

1. The ENTIRE active w component has at most M edges at EVERY cut t>=T.
2. Every R-born lifetime born at or after T that is eventually consumed has
   at most J completed dormant episodes.
3. Each such dormant episode contains at most A integer cuts.

Then every such consumed lifetime has age at most

    D=(J+1)H(M)+JA,

and the actual trajectory is eventually a nonzero translating periodic
TRACE. The translator is not asserted to be standard104.

**Proof.** A lifetime born at update b is active at cut b+1, since its new
edge is incident to the stationary w cursor. It is active at its consuming
cut d, because the current black read edge is incident to that cursor. Its
cuts b+1,...,d alternate active and dormant episodes, beginning and ending
active. If j dormant episodes occur, there are j+1 active episodes. Their
cut counts sum EXACTLY to d-b, the consumed lifetime's age. Lemma2 bounds
the active contribution by(j+1)H(M), and the hypothesis bounds the dormant
contribution by jA. Since j<=J, the claimed age bound follows.

There are only finitely many black lifetimes present at cut T. Each can be
consumed only once. After the last future consumption from this finite set,
every L consumes a lifetime born at or after T, with age<=D. Lifetimes from
that set never consumed in the future are irrelevant to this argument and
remain on the actual board.

Now apply the RETAINED bounded-consumed-lifetime/stale-memory theorem,
`../sources/kehao95-core/memory_feedback/proof/stale-memory.md`, Sections1--4.
Once every L has a previous R within D updates, its stale predicate S_D never
occurs. The exact D-letter suffix predictor is autonomous, with at most2^D
states; the retained theorem gives eventual nonzero translating periodicity.
This finite-memory implication is attributed, NOT a new result here. It does
not classify all possible finite-seed translating words as104. QED.

## 5. Exact decomposition of the unresolved attraction condition

Equivalently, any R-born consumed lifetime of age L>(J+1)H(M)+JA MUST exhibit
at least one of the following concrete mechanisms during its life:

- an active cut containing it with more than M active-component edges;
- more than J complete bridge-departure/R-reimport dormant episodes;
- a completed dormant episode longer than A cuts.

For a finite trajectory that is NOT eventually a translating periodic trace,
the retained stale-memory theorem supplies unbounded consumed ages in every
tail. Removing the finitely many lifetimes present at a chosen cut T leaves
arbitrarily old consumed lifetimes born by R after T. Therefore for EVERY
M,A,J,T, an R-born lifetime born after T exhibits one of these three mechanisms.
The conclusion concerns ACTUALLY CONSUMED lifetimes, not never-read old cycle
support. The24-cell cap's permanent original z support is not counted.

This is a structural trilemma, NOT evidence that any branch is impossible.
Finite support by itself does not currently give the sustained bounds M,A,J.
The isolated identical59-edge controls do not supply a global M. The finite
184-cell waves already show that uniform original-mass bounds on consumed
ages are false, and the archive calculus permits temporary imports and
non-LIFO reactivation. A new proof must constrain those ACTUAL bridge-cut/
R-import itineraries or active-component growth, not substitute an
instantaneous component picture or passive cycle-support age.

## 6. What the serial-chain theorem does and does not add

During an ordinary old-bridge zipper, every new R arm is left on the departed
side when the old bridge L is consumed. The old arrival-side component is
inherited EXACTLY. Hence a dormant component temporarily imported by an R
cannot ride along across that bridge unless it was already part of the old
far-side field; an actual outside import is discarded with the departure
side. This locates repeated temporary activations in the trail, not in the
retained far-side component. At a later genuine w-exceptional renewal the
exposed serial bridge chain and proper r0/1/2/4 import constraints still
apply, preserving whole blocks and attachment ports.

These exact restrictions are inherited from the signed
`../global_renewal_archive_2026-10-23/serial_bridge_release_and_archive_splice_v2.md`
and old-bridge inheritance notes. They do NOT bound the number of later
returns to that trail, completed dormant gaps, or reimports. Establishing
such a sustained restriction, or a real finite-seed countermechanism, is the
next unresolved target. No global capture conclusion is drawn.
