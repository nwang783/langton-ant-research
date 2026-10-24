# Critical flow-two departure circles have same-contact LEFT returns

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Author proof pending independent audit. Let gamma be an embedded
first-R departure b-cycle of constant TOTAL physical edge flow two and
selected C height c. Write c_right=c_left+1 for the retained exterior
stream convention. No global maximum, cap-free generalization, bounded
wait, or complete-front existence claim is made.

The local side table is the one frozen in b019b6d3: both RIGHT profiles
preserve actual side; LEFT V preserves side; LEFT O/U has exactly L1
RIGHT->LEFT and R2 LEFT->RIGHT. The all-V wall theorem implies there is
at least one O/U contact. Until that theorem's independent audit closes,
this note is conditional on its stated complete local table and proof.

## 1. Two physical side currents, with all contacts retained

Along each cycle edge assign ordinal first to RIGHT and ordinal second
to LEFT. Off gamma assign every physical edge occurrence to its geometric
component. At a RIGHT contact the exterior ports are LEFT; at a LEFT
contact they are RIGHT. Chords between gamma vertices lie on a single
side, exactly as in the wall argument. These account for every physical
edge occurrence, including all L3 supply and arbitrarily deep exterior
history.

At O/U repair ONLY the two crossing turns:

    RIGHT: incoming L1 -> outgoing R2;
    LEFT:  incoming R2 -> outgoing L1.

All other reads retain their ACTUAL incoming/outgoing pairing. Each side
is balanced and nonnegative. This is a finite edge-occurrence permutation
on the full drift quotient, not a claim that the actual cursor keeps one
side before the repairs. Any other sheet exchanges in the exterior stay
actual, unrepaired.

For clarity, a RIGHT contact has one RIGHT incoming/outgoing port and
three LEFT incoming/outgoing ports. A LEFT V/U has three RIGHT and one
LEFT; a LEFT O has two RIGHT and one LEFT. The pairs above restore this
same count at the two crossing ranks. Thus no positive residual or
unaccounted port is hidden in the cut.

## 2. Exact stream and temporal winding

Use the signed unshifted h convention: every cycle edge has C height c
on its oriented right and L height c-2 on its oriented left. The cut is
therefore at c-1. The RIGHT current has piecewise stream

    h_R = h-(c-1) on geometric RIGHT, and 0 on geometric LEFT.

Across a gamma edge its jump is exactly one, agreeing with its assigned
first ordinal; interior-side edges keep their full original flow.
The LEFT current is the complementary stream/current. Because gamma has
winding -1, its geometric RIGHT contains the global LEFT exterior. The
RIGHT/LEFT oriented homologies are consequently

    W_R = (c-1)-c_left = c-c_right = K_c,
    W_L = c_right-(c-1) = 1-K_c.

This uses the retained exterior jump convention, not an inference from
local tangent direction alone. The currents are physical, edge-disjoint
occurrence partitions, not extra additive budgets over overlapping old
backbones.

Every repaired RIGHT circuit has exact clock

    w P = physical_edge_length + sum_at_its_O/U_contacts (T2-T1) > 0.

Every displayed wait is positive, at least four. No RIGHT circuit can
avoid all O/U contacts: such a circuit would be an unchanged closed
subcycle of the actual one-P-cycle successor, despite the nonempty cuts.
This also makes explicit why an arbitrary disconnected exterior actual
orbit cannot be supplied as a completion. No circuit is assumed embedded
or primitive. Its temporal winding w is a positive integer by the exact
physical-time telescoping identity.

Summing w gives K_c. Thus c>=c_right+1, and the number of RIGHT circuits
is at most K_c. These are consequences of the positive chronology, not
of nonnegative flow alone.

## 3. Critical level forces exact same-contact excursions

Now suppose c=c_right+1, equivalently K_c=1. Then the RIGHT permutation
has exactly one circuit, with winding +1, containing ALL O/U cuts.
Enumerate its contacts by consecutive outgoing R2 events, choosing their
physical lifts along this circuit. If contact i is followed by i+1, the
intervening RIGHT path is an ACTUAL factor from R2_i to L1_(i+1), of
positive length l_i. It follows that

    T2_i < T1_(i+1) < T2_(i+1),
    T1_(i+1) = T2_i + l_i.

After all n contacts, the same lifted contact has moved by +d and time
+P. In particular

    P = sum_i l_i + sum_i (T2_i-T1_i),

so every individual T2_i-T1_i<P follows from the identity. It is not an
extra premise. Winding +1 guarantees that the lifted list contains every
full-drift translate of every cut occurrence; no extra crossing can hide
inside one of these intervals.

Thus the ACTUAL crossing order alternates

    ... L1_i, R2_i, L1_(i+1), R2_(i+1), ... .

Immediately after L1_i the cursor is LEFT, and its next possible crossing
is R2_i. These events are at the SAME physical cell, not merely the same
quotient class: the displayed physical T1_i/T2_i were chosen before any
period reduction. Hence each actual LEFT excursion starts at O/U.L1 and
returns to that same O/U.R2, with no intervening cut crossing.

It may touch any other gamma vertex at a LEFT-preserving rank, including
late L3 ranks at RIGHT/V contacts; those passive/current contacts are
not excluded. It may self-intersect and use arbitrary old stock. Nothing
asserts a simple Jordan loop, elementary face shape, fresh root, or
permanent fuel consumption. The resulting closed physical walk has
zero winding because it returns to its identical physical endpoint.

## 4. Partial repair graph and limits

Repairing only these n O/U contacts gives one RIGHT circuit and n LEFT
circuits, the latter one per actual same-contact excursion. Its associated
cut graph is a star with n edges, n+1 vertices and cycle rank zero.
This is ONLY the partial cut graph. Other canonical sheet exchanges were
not repaired, so its vertices are not necessarily canonical sheet nodes
and its rank is not an upper bound for the full exchange graph. In
particular the signed elementary-C-loop classification cannot simply
be applied to these mixed-sheet actual excursions.

At K_c>=2 there may be several positive RIGHT circuits or nonprimitive
positive windings, and this same-contact conclusion does not follow.
The theorem gives an exact critical reset pipeline, not a whole-front
exclusion. Whether its old-stock LEFT excursions can be supplied by a
complete WHITE cap-four exterior remains open.
