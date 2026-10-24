# Exact passage permutation and physical side currents of every G3 circle

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Every C level and required positive output are retained. No K1 or
homogeneous-sign premise in sections1-4. Pending independent review.

Let gamma be a physical G3(c) cycle, length ell in the actual full
quotient. Signed5036e7c2 gives essentiality; its embedded winding is
w=+1 or-1. Index its physical lift v_i by the actual edge orientation,
so v_(i+ell)=v_i+w*d. Middle edge ordinal2 is one canonical circle at
sheet c-1. Each vertex is positive (incoming L1 -> outgoing R2) or
negative (incoming R2 -> outgoing L1).

## 1. All eight local ports have one consistent physical side cut

At every vertex, R0 stays RIGHT and L3 stays LEFT of oriented gamma.
The other two reads connect its middle track to one off-circle side:
LEFT at a physical RIGHT turn, RIGHT at a physical LEFT turn. For a
positive corner L1 leaves gamma and R2 returns; for a negative corner
R2 leaves and L1 returns. First and third triple-edge occurrences are
pushed RIGHT and LEFT, consistently across both physical endpoints.

This is the complete eight-profile table, including both same-R and
opposite-R cases. Other physical edges cannot cross gamma away from a
vertex. Hence an actual excursion with no middle-track visit stays
on one fixed side, even if it touches gamma at R0 or L3.

Define A_i to be the middle ARRIVAL/off-circle EXIT event and D_i the
off-circle ENTRY/middle DEPARTURE event. Thus

    positive: A_i=T1(v_i), D_i=T2(v_i);
    negative: A_i=T2(v_i), D_i=T1(v_i).

Physical ordinal matching is exactly A_(i+1)=D_i+1.

## 2. An exact equivariant passage permutation, not a static path guess

Let H(i) be the index of the next D event in ACTUAL time after D_i.
Let F(i) be the next D event after A_i, closing that off-circle excursion.
These are bijections of lifted indices and commute with translation
by ell. They are defined in both time directions: all gamma event
classes recur with period P on the same essential physical lift.
There is no assumption that a local Delta=T2-T1 is less than P.

The actual one-step middle edge gives

    H(i)=F(i+1),
    side(F(i))=side(i).

The quotient H is one ell-cycle and H^ell(i)=i+w*ell. Therefore the
lifted displacement identity is

    sum_(i mod ell)(F(i)-i)=(w-1)*ell.

F is an even quotient permutation. Its restriction preserves LEFT and
RIGHT turn-side classes. This is an exact all-sign chronological
interface; arbitrary static port matchings need not satisfy it.

## 3. Repairing only gamma: one middle circle plus the F cycles

Perform ONLY the L1/R2 transpositions at the ell gamma vertices, leaving
all other actual transitions unrepaired. The resulting permutation has
one gamma cycle and exactly one additional cycle for each quotient
cycle of F. A side excursion ends at D_(F(i)); the repair redirects it
into A_(F(i)), the next excursion. Every nonmiddle component must meet
gamma, because otherwise it would already be a proper invariant cycle
of the original single actual P-cycle.

These side cycles are genuine permutation cycles and balanced integer
flows. They need NOT be embedded circles, primitive, contractible, or
legal ant trajectories. An F cycle lifting by q*ell has oriented physical
homology w*q. Do not replace q by its sign or a quotient phase.

The partial cycle excess is exactly

    beta_gamma=ell-number_of_quotient_cycles(F).

It is nonnegative even. Adding any remaining disjoint repair
transposition changes beta by0 or2, never decreases it. Thus

    beta_full >= beta_gamma.

This is a single partial-graph reservation, not an additive claim over
overlapping circles or resources, and it supplies no beta upper bound.

## 4. Exact physical stream split on the two sides

Keep h(C)-h(L) as the original physical current and c_right-c_left=1.
Define stream functions on original faces by

    h_LEFT = h-(c-2) on physical LEFT, zero on RIGHT;
    h_RIGHT= h-(c-1) on physical RIGHT, zero on LEFT.

Their nonnegative balanced currents, plus ONE use of every gamma edge,
partition the entire actual integer flow. On each triple edge the
pieces are respectively third, first and middle occurrences. Elsewhere
all physical uses lie on the appropriate side. The all-eight-corner
inventory checks both local balance and the exact stream constants.
The F cycles are precisely the partial-repair decomposition of these
side currents.

With homology measured in the original +d direction, exterior jumps give

    w=+1: LEFT=c-2-c_left, RIGHT=c_right-c+1;
    w=-1: LEFT=c_right-c+2, RIGHT=c-1-c_left.

Their sum is1-w, as required by the middle circle's winding w. This
uses the retained oriented exterior convention, not local tangent
agreement alone.

## 5. Homogeneous positive and negative normal forms

If every vertex is positive, A_i<D_i<A_(i+1), so F(i)=i. The partial
repair is a STAR TREE: one positive middle circle and ell zero-homology
side cycles, each the actual L1-to-R2 closed excursion at one cell.
The same side split forces c=c_right+1. These closed excursions may
intersect physically or reuse cells at different ranks, and need not
return the same heading. They are not removable physical leaves or
independent fresh stock.

If every vertex is negative, signed2bcd69ed gives winding-1, alternating
turns and F(i)=i-2. Ell is even. Thus F has exactly TWO quotient cycles,
one on each physical side. Each lifts by -ell and has physical homology
+1. The partial repair has EXACTLY three cycles: the negative middle
circle and these two positive side cycles. Hence

    beta_full >= ell-2.

Equating their side homologies+1 with section4 also forces

    c=c_right+1.

Therefore BOTH homogeneous types can occur only at this critical C
height, at any global K. In K1 this is c=M. Mixed-sign circles may lie
at other levels and are not classified by either normal form.

All-positive W20-type stars require explicit supply analysis; the
prepared W20 control is not a WHITE-front realization. The all-negative
diagonal necessary profile is not a realized front either. Positive
output defects, free-patch rank shifts and mixed-sign assembly remain.

Companion triple_circle_side_stream_inventory.py/json independently
checks all eight geometric corners and the physical stream split. No
front, period, width, drift or seed search is performed.
