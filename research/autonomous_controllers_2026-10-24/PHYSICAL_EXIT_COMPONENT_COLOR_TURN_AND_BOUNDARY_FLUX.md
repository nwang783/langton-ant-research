# Physical exit components: exact color/turn accounting and signed WHITE boundary flux

24 October 2026. Author proof and literal controls, submitted for independent
review. No per-component output lower bound or controller classification is
proved. This is a new accounting formulation, not a claim of literature novelty.

## 1. The partition and the clocks it actually controls

Take any supplied legal translating orbit with complete stable read histories,
actual full period P and nonzero full drift d. Both complete WHITE and genuinely
prepared BLACK-first histories are allowed in this identity. Quotient physical
cells by Zd, NOT by a primitive sublattice chosen to simplify coordinates.

For each read class v choose a physical representative. Its last read has
canonical time lambda(v). Its ACTUAL last departure goes to s(v)+nu(v)d.
The arrival occurs one update after that last source read, whereas the target's
last read can be later. Exactly

    lambda(s(v)) + nu(v)P - lambda(v) >= 1.

The selected arrival is not silently identified with the target's last arrival.
Cycle sums are positive. The separately signed primitive-spine theorem of the
global-attraction analysis additionally gives shift+1 and effective turning0 for
each embedded unit-grid quotient cycle. Thus each quotient basin corresponds
to one physical forward component, with all its translated spine copies joined.
That theorem is a dependency here, not re-proved from this accounting identity.

Let C be one such physical last-departure component, represented by its full
set of quotient read classes. Membership concerns the CELL, not the event's
active C face, first-entry basin, last-L reverse graph, BLACK support component
or lifetime-boundary circuit. Those other graphs must not be conflated with it.

Every selected last edge preserves C by definition. Earlier actual steps can
cross its boundary. Every crossing departure is therefore strictly BEFORE its
source cell's last read. It has a required NEXT same-cell read at a positive
four-divisible age, at least4, on the same component. If the crossing read is R,
that next L consumes its actual BLACK lifetime. If it is L, a next R restores
that cell. These intervals may overlap; no disjoint-time packing is inferred.

## 2. Exact color charge and boundary-heading identity

Let O_C be the number of permanent last-R classes in C and I_C the number of
BLACK-first classes in C. The complete alternating history of each physical
cell gives, without any time or visit cap,

    g_C := number of R reads in C - number of L reads in C = O_C - I_C.

All actual R-to-next-L ownership stays in the same component, because it stays
at the same physical cell. This does NOT remove movement-boundary terms.
Passive unread prepared BLACK strands are retained in the supplied backgrounds;
they have no read vertex in this partition and contribute no turn charge.

Use headings N=0,E=1,S=2,W=3. Count every actual crossing update, including the
full-period seam. Define b_h(C) as outgoing crossings in direction h minus
incoming crossings in that SAME direction. Arrival and departure use the same
physical step heading. Then sum_h b_h(C)=0. Put

    Phi_C = sum_h h b_h(C),
    Q_C = #(R with incoming W in C) - #(L with incoming N in C).

The exact identity is

    O_C - I_C = 4 Q_C + Phi_C.                         (1)

Proof: for each actual update, its signed turn epsilon=+1 for R, -1 for L
satisfies epsilon = h_out-h_in+4kappa, with kappa=+1 for R,W->N, -1 for
L,N->W, and0 otherwise. Sum over all C events in the actual full period.
The outgoing heading of an internal step cancels the next event's incoming
heading. Precisely the actual crossing headings remain. No selected forest
edge can replace this full-event cancellation. This proves(1).

The branch-cut terms Q and Phi depend on where headings0..3 are cut. Their
sum does not. In particular Q alone is not an intrinsic geometric winding.

## 3. A rotation-invariant block form

For more geometric accounting, split the actual cyclic event order into its
maximal contiguous C blocks. For a block j, record its true first incoming
heading a_j, its heading after its last update b_j, and its complete signed
turn sum T_j. Let delta_j be the representative of b_j-a_j modulo4 in
{-1,0,1,2}. The tie for opposite headings is explicitly +2. Define

    W_C = sum_j (T_j-delta_j)/4,
    Psi_C = sum_j delta_j.

Then, exactly,

    O_C - I_C = 4 W_C + Psi_C.                         (2)

If C is the entire event orbit, use the whole P interval as one block, with
delta=0. Otherwise the blocks really end at earlier cross-component steps,
not at selected last departures. Formula(2) is a sum of actual turn identities,
not a claim that the open blocks are embedded closed curves.

Psi is invariant under proper rigid rotations and phase cuts. No geometric
interpretation of W as a positive count of bounded regions is asserted. The
opposite-heading tie convention matters in general; the WHITE countercontrol
below has no opposite-heading block, so its sign does not depend on that tie.
Under a full period power q, all component charges, crossing vectors, Psi and
W multiply by q. The number of physical components is unchanged. This exact
full-drift covering behavior is verified, not replaced by primitive labels.

## 4. Standard104 is a literal WHITE countercontrol to boundary-flux positivity

The two physical exit components of the standard word contain16 and6 read
classes and have respectively8 and4 permanent outputs, no input classes.
Each has four maximal movement blocks per primitive period.

For the8-output component, all four blocks enter with S and exit with E.
Their exact phase intervals, signed turns and residual full turns are:

    [18,18]:  T=-1, delta=-1, W=0;
    [20,22]:  T= 3, delta=-1, W=1;
    [32,38]:  T=-1, delta=-1, W=0;
    [40,114]: T= 7, delta=-1, W=2.

The last interval crosses the actual period seam. Therefore

    g=8 = 4*3 + (-4),       Psi=-4.

For the4-output component, the blocks are[11,17],[19,19],[23,31],[39,39].
All enter with E, exit with S, and have T=delta=1. Therefore

    g=4 = 4*0 + 4,          Psi=+4.

Thus an actual complete WHITE controller has BOTH boundary-flux signs, in a
rotation-invariant formulation. WHITE implies neither Psi>=0 for every exit
component nor vanishing boundary flux. The4-output component has zero residual
block full-turn sum W: its entire charge is the boundary term. This blocks
inferring its four outputs from a strictly positive internal winding count.
It does not refute a possible different four-output theorem.

The heading-cut version has b=(0,4,-4,0), Phi=-4, Q=3 for the8-output
component, and the opposite vector, Phi=4, Q=0 for the4-output component.
Rotating the actual standard control by180 degrees gives Phi=12,Q=-1 in the
8-output component. Hence even the branch-cut wrap count can be negative in
WHITE; treating it as a nonnegative topological count would be an error.

### Earlier crossings, with every future source obligation retained

The exact standard crossing source phases are10,17,18,19,22,31,38,39.
The certificate records every physical step, full-period voltage, complete
source/target ordinal, and the source's next actual same-cell read and age.
No crossing is a last departure. Each crossing R's L owner remains internal
to its source component; the movement itself does not.

Even FIRST departures need not preserve exit components: actual R38 at
(-3,3) moves east to R39 at(-2,3), from the8-output component to the4-output
component. R38 is the complete first R of class(1,-1); R39 is rank2 of
class(0,1). Thus closing a component under all first departures is false.
The selected-spine incoming heading and actual last incoming heading are also
stored separately; they differ at some actual standard spine vertices.

### Whole finite field positive, not merely a stable word

A fresh empty-board simulation provides complete fields at9977,10289,10393,
with715,751,763 BLACK cells. The exact all-future checker certifies the standard
word at capture and at10289. Every104 actual read and actual L owner is stored,
along with the eight literal crossings and their next same-cell reads. The
first-crossing R38 is independently checked to be the actual first visit of
that physical cell in the blank trajectory. Normalized and literal coordinates
are kept distinct.

## 5. Supplied prepared controls

The four supplied prepared words each have one physical exit component, so
there is no intercomponent crossing flux at all. Their exact data are:

    prepared10:   I=1,   O=1,   g=0,   Psi=0, W=0,  spine length2;
    prepared80:   I=2,   O=14,  g=12,  Psi=0, W=3,  spine length12;
    prepared1564: I=197, O=301, g=104, Psi=0, W=26, spine length176;
    prepared4352: I=406, O=590, g=184, Psi=0, W=46, spine length108.

All spine shifts are+1. The P/Q complete prepared input/output profiles,
223/62 passive unread BLACK classes, and finite XOR caps2/68 are retained.
Prepared10/80's exact caps and future input rays are retained as well. These
are not autonomous finite-seed WHITE controls; zero boundary flux is not an
input-free certificate. Standard has nonzero flux despite being WHITE.

The checker rebuilds100 rotation/full-period-power/phase controls and all
component histories rather than normalizing away a winding or an input class.

## 6. Exact live middle-short target, and the remaining gap

All six signed middle-short T0..T10 interfaces have a common lower exit basin.
Their last arrows include

    0->1->4->3->6->7->10,     2->3,     5->8->7.

In four interfaces the continuation is10->9->12; in the other two it is
10->11 and9->6. Thus ALL eleven named classes feed one unknown upper class,
and all five low permanent outputs0,1,2,6,7 belong to one exit component.
Only the three upper permanent outputs remain outside this named set.
The actual-component conclusion retains the separately signed unit-shift
spine theorem; it does not discard voltage to identify different physical ends.

A theorem requiring at least four outputs per WHITE exit component, together
with a separate theorem requiring two components, would exclude this branch.
Neither statement follows from(1) or(2), and neither is asserted here. The
actual signed standard flux prevents a simple positivity shortcut. Any useful
componentwise lower bound must control the coupled boundary movement and
residual turn terms, with the actual future same-cell obligations retained.
No new numerical conjecture is inferred from the five examples.

Artifacts: certify_exit_component_turn_flux.py and
exit_component_turn_flux_certificate.json. Exact dependency hashes are bound
in the certificate. No period/visit cap, unknown-field deletion, or opaque
solver status is part of this proof.
