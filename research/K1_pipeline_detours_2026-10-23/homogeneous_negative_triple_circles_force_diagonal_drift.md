# A homogeneous negative G3 circle forces alternating turns and diagonal drift

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. All C levels and positive odd output are allowed. No K1, global
maximum, root-free or zero-output premise. Pending independent review.

Let gamma be a cycle of the signed physical triple-use graph G3(c).
Its middle chronological edge occurrences form one canonical node on
sheet c-1. Assume EVERY one of its vertices is NEGATIVE at that node:
the repaired corner is incoming R2 -> outgoing L1. This is an explicit
homogeneity assumption; mixed-sign G3 cycles remain open.

THEOREM: gamma has winding -1. Its physical turns alternate LEFT/RIGHT.
Consequently actual full drift is diagonal:

    |d_x|=|d_y|=length(gamma)/2 >0.

In particular, axis fronts contain no homogeneous negative G3 circle.
The proof uses actual continuous-cursor side balance, not a static
terrain shortcut or an odd-output-to-initial-fuel assumption.

## 1. Complete local crossing inventory

Normalize incoming axis E/W. Exactly four negative middle profiles are

    EWEE, WEWW: RIGHT turn;
    WEEE, EWWW: LEFT turn.

Rotations give eight distinct complete compass histories. At every
such corner:

- R0 stays on the RIGHT of the oriented physical gamma;
- L3 stays on its LEFT;
- L1 arrives from an off-circle side and DEPARTS along the middle edge;
- R2 ARRIVES along the middle edge and leaves to the SAME off-circle side.

That off-circle side s(v) is LEFT at a RIGHT turn, RIGHT at a LEFT turn.
The first and third uses of every triple edge can be pushed slightly
RIGHT and LEFT respectively; its middle use stays on gamma. R0/L3
therefore do not cross this cut, including visits tangent to gamma.
Unused ports at the corner obey the same side table. There is no
omitted physical crossing or chord crossing away from a gamma vertex,
since gamma is an embedded physical-edge circle.

## 2. Lifted exact event order

Index a physical lift in its edge orientation by ...v_(i-1),v_i,v_(i+1)...
and put tau_i=T1(v_i), eta_i=T2(v_i), Delta_i=eta_i-tau_i>=4.
Middle-edge ordinal matching is exactly

    eta_(i+1)=tau_i+1,
    tau_(i-1)-tau_i=Delta_i-1 >=3.

All tau events are consequently strictly ordered in REVERSE physical
index. Their order is bi-infinite: physical full-drift equivariance
shifts them by the nonzero P. The canonical clock identity gives

    kP=ell-sum Delta_i <0,

where ell is the number of full-quotient gamma cells. Embedded simplicity
on the full cylinder gives k=-1 (rather than0 or a nonprimitive winding).
Thus the lift contains every physical translate of this circle.

The exact actual order is

    L1(v_i), R2(v_(i+1)), L1(v_(i-1)), R2(v_i), ... .

There is NO other gamma L1 or R2 event between R2(v_(i+1)) and
L1(v_(i-1)). Every other gamma contact in this interval, if any, is R0
or L3 and stays on one side by section1. Hence this genuine actual
excursion cannot cross gamma. Its departure and arrival off-circle
sides must agree:

    s(v_(i+1))=s(v_(i-1)) for every i.

This is the essential chronological coupling. It keeps the actual R0
and L3 suppliers instead of replacing the three-port flow by one
uninterrupted hypothetical cursor path.

## 3. From side period two to geometric rigidity

The side sequence has period two, so the physical LEFT/RIGHT turn
sequence does too. An essential embedded physical-edge circle has
zero signed total turning in a full drift period. A constant turn
sequence is impossible (it would close an elementary square); the
only remaining period-two sequence is strict alternation.

Each vertex turns90 degrees because the Manhattan incoming and outgoing
axes are perpendicular. Alternation fixes two perpendicular compass
travel directions for the entire lifted circle. Every pair of edges
therefore has displacement (epsilon_x,epsilon_y), epsilon_x,epsilon_y
in {+1,-1}. There are ell/2 pairs, and the circle displacement is -d
by winding -1. This proves the stated full diagonal drift, without
replacing P,d by a primitive pair or assuming a long quotient.

For example a physical NE staircase has alternating complete profiles
NSNN (incoming N -> outgoing E, RIGHT) and WEEE (incoming E -> outgoing N,
LEFT). These are necessary complete port histories, not a constructed
translating front.

## 4. Structural consequences and retained escapes

The signed root-free M-3 reverse rail2ca8c002 forces original full drift
AXIS, and aa7dadc2 identifies its positive all-R2 G3(M) sink. Thus a
front with that root-free shallow minimum cannot ALSO contain any
homogeneous negative G3 circle at ANY level. Mixed-sign G3 circles,
odd-rooted shallow minima and deeper reverse-retreat geometry remain.

In particular, if a homogeneous negative top G3(M) circle is incident
to an L plateau Q at M-3, then Q cannot simultaneously be locally minimal
and have no odd incident corner: those hypotheses would force axis
and diagonal drift at once. Therefore Q has an odd incident corner or
has a lower adjacent L face. This is an alternative, not a distinct-root
payment per circuit, and not a general G3 or K1 exclusion.

The companion negative_triple_circle_crossing_inventory.py/json exhausts
only the30 local WHITE cap-four histories and their compass rotations.
It does not scan fronts, periods, drifts, widths or seeds.
