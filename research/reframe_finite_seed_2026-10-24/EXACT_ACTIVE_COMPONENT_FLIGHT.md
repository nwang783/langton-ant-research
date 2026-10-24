# Exact active-component flights and dormant-module contact

24 October 2026. New author theorem and executable reduction, submitted for
independent audit. This is NOT a proof of capture, an undecidability result,
or a universal-machine construction. No literature priority is claimed.

## 1. The target is an actual graph event, not a turn defect

Use the actual complete finite black field B and physical pre-update pose
(p,h). Fix the w diagonal BLACK graph. The edge at a black physical cell has
that cell as midpoint. The active component C is the entire black-edge
component at the actual w cursor. A nonempty dormant import is an actual R
whose insertion connects the cursor's old component to a DIFFERENT component
containing at least one edge. An edge joining an isolated vertex is not an
import; a cycle-closing edge inside C is not an import.

The input includes an integer cap M>=0. Define the first stopping event as
follows: at every pre-update cut, first test |C|>M; if false, test whether the
next update is a nonempty dormant import. Stop at the first applicable event.
If that import would itself make the post-update component exceed M, report
IMPORT, with its exact pre-update state, rather than silently taking the R.

**Theorem.** There is a total exact algorithm that, from every supplied finite
(B,p,h,M), returns exactly one of:

1. The first cap-failure cut, if it precedes every import.
2. The first nonempty dormant-import update, if no earlier cap failure occurs.
3. An exact certificate that neither event ever occurs, together with an
   eventual heading-restoring nonzero translating periodic turn plan.

The complete field at the reported cut is retained, including unread original
archives and every subsequently detached component. It can be given as a finite
union of finite translation runs, rather than expanding a huge remote flight.
Outcome 3 is not automatically the standard104 word. No claim is made that it
occurs for any supplied example in this note.

## 2. Exact isolated-component predictor

The following established physical gates are the starting point:

- At R, w is stationary and the new edge is incident to w. Existing active
  edges stay active. If its other endpoint v is in another nonempty component,
  the ENTIRE component at v is imported.
- At L, w crosses the deleted edge. The next active component is its arrival
  component in C minus that edge. All other surviving components are dormant.
  No old dormant component is activated by a deletion.

These gates are independently signed in
../active_w_archive_itinerary_2026-10-23/ACTIVE_EPISODES.md, Lemma 3. The predictor
uses the same literal update, but on C alone. After an L it retains the complete
arrival component and records every lost edge as a time-tagged emitted archive.
It never treats those emitted edges as erased physical cells.

For an R whose other endpoint is already a vertex of C, no archive lookup is
needed. For an R to an endpoint outside C, record v as a QUERY. Before any import,
that query is an import exactly when v is incident to any current dormant edge.

**First-collision induction.** Until the first query that meets a dormant
vertex, the predictor's active component, pose, and turns equal the real ones.
The dormant field is exactly the union of the initial dormant field and every
previously emitted component, each still black and unmoved.

Proof: initially active and dormant components have disjoint vertex sets. An
L removes only an active edge, and its retained and emitted components have
disjoint occupied vertices. An R inside the active vertex set touches no
archive. An R to a new endpoint either misses every archive and updates exactly
as predicted, or is the claimed first import. This proves the induction.

In particular an emitted fragment cannot first attach to an older emitted
fragment silently. It was active immediately before emission. Any contact with
an old dormant vertex would already have entered the active graph at an earlier
R QUERY. Thus query-versus-earlier-emission tests cover emitted/emitted as well
as active/old-passive collisions. Hypothetical emissions after the first
collision are not asserted physical and cannot change which collision is first.

## 3. Why a cap gives finitely many isolated shapes

If e is an active black edge and |C|<=M, its midpoint lies within infinity
distance M of the physical head. This is the signed metric lemma in
ACTIVE_EPISODES.md, Lemma 1: a shortest active graph path to an endpoint uses
at most M-1 diagonal edges, and the endpoint and cursor head corrections total
one more unit. It also covers R-only motion.

Consequently a normalized predictor state is completely determined by h and
the set of active edge midpoints relative to p in [-M,M]^2. A sufficient state
bound is

    S(M) = 4 * sum_{j=0}^M binomial((2M+1)^2,j).

For M=0 take S(0)=4. Not every bit mask counted here is a connected realizable
state; overcounting is harmless. Absolute p is stored separately. The fixed
pose sector means a repeated heading/relative component can only have an
even-checkerboard displacement, preserving the same diagonal lattice.

Run the isolated predictor, NOT the physical ant beyond a detected collision,
until either its active cap fails or a normalized state repeats. This happens
after finitely many transitions, at most S(M)+1 state inspections. A repeated
shape gives a preperiod a and period P with a+P<=S(M). There are literal finite
phase records (pose, heading, complete C, R query if any, and emitted edges).
If d is the physical displacement over the period, every later predictor
period is exactly the same record translated by d.

This is a finite local predictor, not a cropped physical evolution. Its entire
old and newly emitted field is checked in the next section before any predicted
infinite motion is accepted.

## 4. Exact all-time query/emission arithmetic

First inspect all finite preperiod queries against the initial dormant vertices
and strictly earlier preperiod emissions. If the predictor hits its cap before
repeating, do this over its complete finite prefix and return the earliest
import or the terminal cap cut. There is no infinite quantifier in this case.

For a repeated predictor, let A be the occupied vertices of the initial archive
plus all preperiod emissions. At cycle phase i, let q_i be the R query (if any).
Let E_j be the occupied vertices emitted at cycle phase j. Graph vertex
coordinates are doubled in the implementation, so put D=2d. Emissions are
created AFTER their update; the next query at a later phase sees them.

At time a+kP+i a query meets an old/preperiod archive exactly when

    q_i + kD = v,        v in A, k>=0.                       (1)

It meets a periodic emission from an EARLIER update exactly when

    q_i + kD = v + ell D,  v in E_j, ell>=0,
    ell P + j < kP + i.                                   (2)

When D!=0, (1) is an exact integer-ray test, with at most one k per vertex.
For (2), put n=k-ell. Solve v-q_i=nD in integers. The chronology test is

    n>0, or n=0 and j<i.                                  (3)

If admissible, its earliest occurrence is k=n, ell=0. If n<0 or the n=0
phase order fails, it never occurs. Take the least physical update over all
finite vertex/phase pairs and all preperiod candidates. This includes arbitrary
differences of periodic indices, not merely adjacent copies or active read rays.

When D=0, equality is just q_i=v. For a periodic emission the first eligible
query is in cycle zero if j<i, and cycle one otherwise. Static archive equality
is eligible in cycle zero. Thus zero displacement is explicitly checked too.

If no finite candidate exists, the first-collision induction proves that the
entire infinite predictor is the physical ant and that the cap never fails.
A zero-drift predictor would then remain in one finite set of cells forever,
contradicting the established no-bounded-orbit theorem. Thus the no-collision
outcome necessarily has d!=0 and certifies an actual translator. In particular
repeating a normalized state with d=0 is NOT accepted as a physical cycle.

## 5. Complete field and lifetime ownership at a distant event

Suppose the first event has t=a+kP+i. At that PRE-UPDATE cut the full black
field is exactly the union of:

- the active phase-i component translated by kd;
- the original dormant field;
- all preperiod emitted edges;
- every emitted edge set E_j (in physical midpoint coordinates) translated
  by ell*d, for 0<=ell<k and 0<=j<P;
- phase-j emissions in the current period translated by kd, for j<i.

Use edges, not just occupied vertices, for this output. It is a finite union of
finite translation runs. Before the first import these edge sets are distinct
current lifetimes: no archived edge has been read, erased, or reborn. Keeping
its birth/detachment phase and period index preserves literal chronological
ownership. At the event an actual R adds its current edge and imports ALL
components incident to the queried endpoint (in a graph these form one complete
old component); it is not merely a one-edge marker consumption.

The implementation returns the exact pre-import field and does not execute the
import or erase unselected archives. `archive_terms(t)` provides the full finite
run representation at every cut up to the event. `state_at(t)` optionally
materializes it and checks the real full board in the finite controls.

## 6. A useful quantitative corollary, not a global return budget

Let R be the maximum infinity distance from the cycle-start head to any occupied
vertex in the STATIC archive A, using physical coordinates. A query vertex lies
within P+1/2 of that head. A vertex of an emitted component lies within P+M+1/2.
Therefore, if d!=0, a static collision's epoch is at most ceil(R)+P+1 and a
periodic-emission collision's epoch gap is at most 2P+M+1. These follow by taking
an integer coordinate with |d_coordinate|>=1 in (1) or (2). The constants are
safe overestimates. Thus any future collision, if present, occurs by an explicit
finite time bounded by the input archive radius and the finite predictor size.

This does NOT bound the number of successive imports, the lifetime of a
particular frozen component, or return times solely by original seed mass. Long
standard flights can themselves have frequent imports of newly emitted modules.
The signed fixed-count remote-scatterer families and pending bounded-component
long-dormancy family do not contradict this theorem.

## 7. Concrete computational reduction and its missing obligation

Under a sustained active cap M, the actual infinite evolution can be reorganized
at nonempty R imports. Every between-import motion is decided by one of the
finite isolated shape plans and exact intersections with the COMPLETE spatial
archive. If there are only finitely many imports, the theorem certifies eventual
nonzero translating periodicity. Thus every non-eventually-translating capped
orbit must make infinitely many nonempty component imports.

This produces a specific finite-control, spatially distributed memory model:
finite active shapes, finite lists of phase-query and fragment-emission templates,
and a finite but potentially growing archive of embedded components. Positions,
component contents, and chronological ownership are NOT finite-state data and
must not be omitted. When the cap also holds after an import, its imported
nonempty component has at most M-1 edges. The exact new edge pays the extra one.

A finite-support universality construction in this model still needs a finite
initial archive and a renewable sequence of actual module interactions. The
present operator is a forward exact reduction FROM ant dynamics, not a compiler
FROM a hard machine problem into the ant. It gives no undecidability conclusion.
It also does not classify the no-further-import translator as standard104.

This differs from the retained total next-K or stale-memory target algorithms.
Their event is a turn-language defect or an old consumed lifetime. Here the event
is a whole-component attachment at a WHITE read, and the certificate retains
old-passive and emitted/emitted attachment geometry. No turn defect, consumed
age cap, directional strip, or finite macro language is assumed. The abandoned
column/tape analogy is not being promoted as a substantive result.

## 8. Artifact and exact verification scope

- active_flight.py: self-contained literal update, diagonal graph, capped
  isolated predictor, all-time affine contact test, exact complete-field output.
- check_active_flight.py: author comparison to a separate whole-board first-event
  simulation, all small-board fields/poses/caps, standard104 phase controls,
  and synthetic periodic ray arithmetic tests.
- active_flight_controls.json: executed control results.

The synthetic nonzero-drift/huge-distance arithmetic controls are NOT ant
trajectories. No actual no-import translator was found or is claimed. The blank
board control has a zero-drift 20-step isolated predictor cycle but the actual
first import is update 8, from the fragment emitted at update 4. This is a direct
adversarial check against treating the pruned cycle as physical recurrence.

The implementation's finite memory/time limits are not mathematical negative
certificates. The totality claim is the finite-state and ray-arithmetic proof
above, conditional only on the established exact gates, metric lemma, and
no-bounded-orbit theorem. Independent audit has been requested, not assumed.
