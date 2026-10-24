# The first-L birth curve forces actual backward/right excursions

23 October 2026, 13:10 UTC. New analytic consequence of the independently
approved first-L max-face backbone. Independent review requested. No
front exclusion or finite-seed capture theorem.

## 1. An ordered essential geometric cut

Choose ONE positive essential first-L face-birth cycle Gamma inside a
maximum C plateau. Keep the actual full drift d and period P. Index its
selected primal contact vertices v_i in positive cyclic order, lifted to
all i in Z, so for its ell contacts

    v_(i+ell)=v_i+d.

Let T_r(v_i) denote that physical contact's complete rank-r read time.
The birth construction gives

    T_1(v_i)=B(F_(i+1)),
    T_1(v_(i+1))>T_1(v_i),
    T_1(v_(i+ell))=T_1(v_i)+P.

Thus its actual L1 times are STRICTLY ordered along Gamma, not merely
along an arbitrary local turn convention. This order is the crucial
rank-two chronology retained below.

Draw Gamma through the C-face centers and its selected contacts. The
embedded primitive essential cycle lifts to one proper separating line
in the plane, invariant under d. Its orientation defines LEFT and RIGHT
sides. At a selected contact, genuinely rotate so R0 arrives N and
turns E around parent max face G=SE. The child max face F=NW is entered
by L1(N->W), and R2 arrives S and turns W. The oriented Gamma arc goes
SE->NW. The complete local crossing table is:

    R0: LEFT -> RIGHT,
    L1: LEFT -> LEFT,
    R2: RIGHT -> LEFT,
    L3, if present: stays LEFT or stays RIGHT.

Indeed the left quadrants of the SE->NW diagonal are SW, while the right
quadrants are NE. Local smoothing of the turn arcs gives exactly these
crossings. At any other primal vertex Gamma is absent; inside faces
there is no physical grid edge crossing. Therefore these R0 and R2
occurrences are ALL actual crossings of Gamma.

## 2. Contiguous actual excursions, not a nonconsecutive backbone

The ant alternates actual crossings of the separating line. Each R0 at
v_i starts one contiguous RIGHT-side excursion and ends at some R2 at
v_j. Every R2 starts one contiguous LEFT-side excursion and ends at
some R0 at v_k. Ends exist because the complete periodic crossing set
continues in both time directions. Local noncrossing L3 reads may occur
inside either excursion; they are retained, not relabeled or discarded.

For the RIGHT excursion starting at T_0(v_i), the ant must already have
returned LEFT before its own later L1 at T_1(v_i). Its ending R2 therefore
satisfies

    T_2(v_j)<T_1(v_i).

But T_1(v_j)<T_2(v_j). Since selected L1 times strictly increase with
contact index, j<i. Every actual RIGHT-side excursion thus moves to an
EARLIER selected contact along the positive Gamma order.

For a LEFT excursion from R2(v_j) to R0(v_k), chronology gives

    T_1(v_j)<T_2(v_j)<T_0(v_k)<T_1(v_k),

hence k>j. Every actual LEFT-side excursion moves FORWARD in that same
contact order. No geometric simplicity of the excursion, absence of
self-intersections, or noncrossing matching assumption is used.

This is a continuous-cursor rank-two coupling around the essential
plateau: real right-side reverse passages and left-side forward passages
are forced by the intervening L1 times. Spatial index order is not
replaced by a Euclidean distance lower bound; Gamma may fold.

## 3. A canonical negative current on the right

Let E(i)=j be the end index of the RIGHT excursion starting at R0(v_i).
Every R2 is the end of exactly one such excursion, so E is a bijection
of the lifted contacts, commuting with i->i+ell. It satisfies E(i)<i.
The induced finite quotient permutation can have several cycles. Each
has strictly negative integer winding; its winding magnitude need not
be one because its actual excursion paths need not form an embedded
circle. Define

    K = sum_(i=0)^(ell-1) (i-E(i))/ell.

This is a positive INTEGER. Integrality follows because E permutes the
residue classes mod ell. In particular K>=1. One must retain K rather
than silently replacing each excursion cycle by a primitive circle.

Partition the actual physical edge occurrences into RIGHT and LEFT
according to the side of Gamma containing their interiors. Gamma meets
physical edges only at selected endpoints, so in fact the two currents
have disjoint physical EDGE SUPPORTS. At a selected contact, the RIGHT
current has one R0 outgoing occurrence and one R2 incoming occurrence;
they balance spatially. Any right-side L3 contributes an ordinary paired
arrival/departure. The LEFT current similarly balances its R0 arrival,
R2 departure, L1 passage and any left-side L3. At unselected vertices
each visit stays on its own side. Both currents are thus nonnegative,
integer and balanced at every physical cell.

Sum the RIGHT excursion displacements v_(E(i))-v_i over one full contact
period. The residue permutation cancels, leaving net displacement

    -K*d.

The complete flow has displacement d, so the LEFT current displaces
(1+K)*d. With D=||d||infinity, checker orientation equates horizontal
and vertical totals in each balanced physical current. Therefore

    length_RIGHT>=2D*K,
    length_LEFT>=2D*(1+K),
    P>=2D*(1+2K).

This is a side-separated ACTUAL current partition, not subtraction of
the diagonal face curve as if it were physical flow. Its coarse K>=1
constant is weaker than the existing all-cap P>=8D. The new information
is the canonical geometric separation and every individual excursion's
backward/forward index order. Do not add this bound to overlapping old
first-departure or A/B/C budgets.

## 4. The first-R physical walls can be chosen on the two sides

At selected contacts R0's incoming edge is LEFT and outgoing edge RIGHT.
A first-arrival dependency path starting at any selected contact stays
in the closed LEFT side: at another selected contact its R0 predecessor
is again on the left; at an unselected contact it cannot cross Gamma.
Its eventual signed A cycle is therefore a positive first-arrival
backbone lying on the LEFT.

A first-departure path starting at any selected contact stays in the
closed RIGHT side: its R0 output is right; upon reaching another selected
contact on a right edge, its next R0 output is still right. Its eventual
signed B cycle is a negative first-departure backbone on the RIGHT.
Both paths remain in the original max C component by the signed
cap-four maximum rule.

This yields a physically ordered corridor structure: a first-arrival
wall on the left, the essential first-L face-birth cut, and a first-
departure wall on the right. The actual ant must alternate backward
right excursions and forward left excursions. The structure is still
not a contradiction; unbounded side complexity and recurrent gate
forests remain unclassified.
