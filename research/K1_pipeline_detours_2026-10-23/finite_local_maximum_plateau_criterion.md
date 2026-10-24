# Every finite local-maximum C plateau lies above the right exterior

23 October 2026, 15:49 UTC. Analytic extension submitted for later review.
This does not assert a new global speed bound or exclude K=1 fronts.

## 1. Exact hypotheses and conclusion

Use a complete WHITE cap-four translating front with actual full period
P, full nonzero drift d, and integer stream

    f(e)=h(C_right)-h(L_left), c_right-c_left=1.

Let Q be a corner-connected component of C faces of one height lambda.
Assume:

- Q has finitely many face classes modulo the actual full drift d;
- Q is locally maximal: every C face sharing a primal corner with a
  face of Q has height at most lambda.

Then

    lambda > c_right.

Neither lambda nor Q is assumed globally maximal. Higher peaks outside
Q, source L1/L3 visits, arbitrary detours and nonprimitive full periods
are retained. The finiteness assumption is essential: an exterior
plateau may have infinitely many classes in transverse width.

## 2. A zero boundary edge would flood the entire face lattice

For F in Q and an edge-neighboring L face J, nonnegative flow gives
h(J)<=lambda. Suppose equality held.

All four C neighbors of J have height at least lambda. The two C
neighbors perpendicular to F are corner-neighbors of F, so local
maximality forces them to lambda and places them in Q. The remaining
C neighbor of J is a corner-neighbor of either of those faces; it too
has height lambda. Thus all four boundary flows of J vanish.

At each corner of J, either geometrically possible R read uses at least
one of those zero-flow edges. A visited WHITE cell has a first R read.
Consequently none of J's four corners can be visited. All physical port
flows at each such corner vanish, forcing the opposite diagonal L face
also to have height lambda and the two opposite C faces to have height
lambda in Q.

Each newly reached L face already has two adjacent C neighbors in Q.
Its remaining two C neighbors are corner-neighbors of these and hence,
by local maximality and nonnegative flow, also have height lambda.
Therefore this new L face has four zero boundary flows as well. Repeat.
The diagonal L-face contact lattice is connected; this propagation
would make every C and L face have height lambda. It contradicts the
exterior jump c_right-c_left=1. Hence equality was impossible, and

    h(J)<=lambda-1 for every L neighbor of Q.

In particular all four physical boundary ports of every F in Q are
positive. This step does not invoke the global shifted-H maximum at a
submaximum height.

## 3. The canonical first-L predecessor stays in Q

For F in Q let B(F) be the earliest first traversal time of its four
positive directed boundary edges. At its minimizing corner v, the first
F output precedes the first F input.

The complete cap-four R-count rule implies every R at v chooses a
maximizing incident C face. Since F is locally maximizing, the only
possible negative first-port contact is flat: the opposite C face G
has height lambda, R0 chooses G, L1 uses the first F output, and R2
uses the first F input. Thus G belongs to Q. More explicitly,

    B(F)=T1(v), B(G)<=T0(v)-1, B(F)-B(G)>=5.

This is exactly the signed max-C birth argument, now with positivity
proved in Section 2 rather than borrowed from a global maximum.

The full-drift-equivariant functional predecessor F -> G closes in the
finite quotient of Q. Its simple embedded C-contact cycle cannot have
winding zero, because B decreases strictly. Reverse orientation gives
an embedded positive full-winding-one first-L curve Gamma inside Q.
The possible short quotient loops and multiple edges are retained;
no primitive-drift reduction is made.

## 4. Cursor sign determines the plateau height

At the selected flat contacts of Gamma, the signed local crossing table
and increasing selected L1 chronology apply unchanged: R0 crosses
LEFT to RIGHT, R2 crosses RIGHT to LEFT, and optional L3 stays on one
side. Every RIGHT excursion ends at an earlier selected L1 index.
The equivariant endpoint bijection therefore has a strictly positive
integer retreat K_Q. The actual RIGHT physical current has homology

    -K_Q < 0.

The disjoint physical side-current split uses only this embedded birth
curve and its selected occurrences; it does not require global
maximality of lambda. The piecewise stream of the same RIGHT current is
h-lambda on RIGHT, zero on LEFT, and zero at the cut C faces. With the
retained oriented exterior convention its homology is

    c_right-lambda.

Equating the two exact descriptions gives

    K_Q=lambda-c_right >=1,

which proves the criterion. No diagonal face edge was subtracted as a
physical edge, and no side current was added to an overlapping budget.

## 5. Supplier-connectivity consequence at K=1

Suppose the global C maximum is M=c_right+1. Consider a connected
component S of the C superlevel set {h>=c_right} which has finitely many
full-drift face classes. If S had no M face, all its faces would have
height c_right, and no corner-neighbor could be higher: any such face
would belong to S. Thus S would be a finite locally maximal plateau at
lambda=c_right, forbidden above. Therefore every such S contains an
M face.

This strengthens the pending locked-bent-rail conclusion in its exact
scope. A secondary face raised to at least c_right, separated from the
right exterior by the complete low C row at c_left, must connect to a
further M face by a C-contact path all of whose heights are at least
c_right. That further M component is distinct from the main rail,
because the intervening entire low row has height M-2. There is no
claim that the additional component repeats the locked architecture.

The criterion alone does not forbid right-exterior-connected plateaus,
produce a paid branch resource, imply K>=2, or exclude general K=1
fronts. The prepared W20 control remains outside its WHITE premise.

## Sources retained unchanged

The birth-cycle construction and local first-port rule are in
rank_two_plateau_2026-10-23/max_C_first_L_face_birth_backbone.md,
SHA c91710090256c728ae9876e7188a39fff3617fcb151a9fd3fc595c5bdbb7f6a5.
The disjoint cursor-current construction is in
face_birth_curve_cursor_counterflow.md, SHA
30b6aab03c07d0593c140af49f6262aeb427db7c8016ae672cf51b7399c40231;
its stream-sign clarification is in cursor_stream_height_and_K1_pipeline.md,
SHA 2e9400915fcc0a571b4effd209f04a8dfd4a0043b7f4c1a80e9f6e2ae5216c35.
This note's new work is the local-maximum zero-port propagation and the
explicit finite-superlevel supplier-connectivity consequence.
