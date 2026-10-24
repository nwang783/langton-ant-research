# The leftmost branch-free K=1 curve has one LEFT middle contour

23 October 2026, 17:30 UTC. New conditional geometric specialization,
submitted for independent review. This does not exclude K=1 or eliminate
lower-sheet essential pairs or positive cycle excess.

## 1. Exact hypotheses

Use a complete WHITE cap-four translating front with its actual full
period P and full drift d, and K=1. Write

    M=c_right+1, b=M-2=c_left, j_middle=M-1.

Let Gamma be the canonical first-L birth circle in the LEFTMOST maximum
C component. Assume Gamma has no LEFT maximum branch: every C-contact
neighbor of a Gamma face lying strictly LEFT of Gamma has height <M.
No restriction is made on the RIGHT, on deeper detours, on other sheets,
on graph cycle excess, or on the full period being primitive.

The signed branch-or-rank3 theorem implies that every selected contact
has LEFT L3. In the local SE-to-NW normalization its complete incoming
history is N,N,S,N, with turns R,L,R,L. The strict straight and strict
right tables consequently apply to every straight or right face.

## 2. The entire unused LEFT C collar is at b

For a straight face its unused LEFT corner has both R reads around the
maximum face, so its other C face has height M-2=b. For a right face
both unused LEFT corners are two-R helpers in the signed all-LEFT-L3
rows 2, 4 or 5, again with other C height b. A left face has a one-edge
LEFT boundary arc and no unused LEFT C-contact neighbor. Thus EVERY
C-contact step from a Gamma face into its strict LEFT has endpoint b.

This assertion is about the complete C-contact lattice, not just a
visual narrow strip. A step from a Gamma C center to another C center
can cross the embedded Gamma only along one of its own contact edges.
Every remaining step into LEFT is one of the unused corners above.
Possible folds, short full-drift quotients and distinct lifted contacts
are retained. A helper cannot simultaneously touch two Gamma maximum
faces: that would be the expressly excluded LEFT maximum branch.

Suppose a strict-LEFT C face had height >=M-1. Its C-contact component
S in {h>=M-1} cannot meet Gamma, since its last step would have to use
the b collar. It also cannot cross Gamma into RIGHT. There are finitely
many face classes in S modulo the actual full drift: far in the LEFT
exterior the height is b, and the front has finite transverse support.
The signed finite-superlevel criterion forces an M face in S.

That M component is distinct from Gamma's component, because no maximum
C-contact path can cross the same b collar. It lies LEFT, contradicting
leftmostness. Therefore

    every C face strictly LEFT of Gamma has height <=M-2.       (1)

The collar argument also rules out a same-component maximum returning
from RIGHT into LEFT: such a C-contact path must first leave Gamma
through an unused LEFT corner. No half-plane or straightness assumption
has entered this argument.

## 3. TOP and MIDDLE have the same LEFT physical support

Restrict the indicator sheet flows g_M and g_(M-1) to physical edges
strictly on the LEFT side of Gamma, with the selected-corner boundary
port convention of the signed side-current construction. By (1), an
active edge of either restriction must have its right C face on Gamma
at height M. Conversely the complete left arcs of Gamma faces carry
both indicators.

Here are the only local boundary configurations.

- At a selected contact N,N,S,N, the LEFT ports are incoming N and
  outgoing W. Their first occurrences are TOP; their second occurrences
  are MIDDLE; their third occurrences are LOWER b. The RIGHT ports have
  only TOP occurrences. Thus TOP and MIDDLE both use precisely the same
  LEFT N/W pair.
- At an unused LEFT helper the incident C heights are M and M-2. The
  TOP occurrence is the ordinary first R0 corner around the M face. The
  MIDDLE canonical repaired corner is the same physical R corner.

All other strict-LEFT edges are inactive on these two sheets by (1).
In particular the two restricted indicator flows have IDENTICAL
physical edge support and IDENTICAL rounded corner geometry.

For TOP this is a side-boundary pairing, NOT the global canonical TOP
pairing into four-edge max-face circles. At each selected contact it
pairs incoming R0 with outgoing L1 on the LEFT. Its actual lifted time
increment is

    1+T1(v)-T0(v) >=5.

At helpers it is the unchanged R0 transition, with increment one. Its
oriented path joins the left boundary arc of one Gamma face to that of
the next, through every selected contact in cyclic order. Each face
contributes its one-, two- or three-edge left arc according as the
face is a left bend, straight, or right bend. There are no other active
LEFT arcs and no extra helper identifications. Hence this pairing is
ONE embedded essential circle, with full winding +1. Positivity of all
its actual clocks independently fixes the positive orientation.

The canonical MIDDLE pairing has exactly the same geometric arcs.
At the selected contacts it is incoming L1 -> outgoing R2, again the
same N/W LEFT turn; at helpers it is the R corner already described.
Consequently

    there is exactly ONE canonical MIDDLE node on LEFT;
    it is essential with winding +1.                           (2)

There is no contractible MIDDLE hole on LEFT under these hypotheses.
Other MIDDLE nodes may exist on RIGHT; no statement about their count
or winding is made. The TOP side-boundary circle above is not itself
a canonical cycle-graph node and is not added to an occurrence budget.

For reference, if ell is the selected-contact count, the left arcs have
2*ell physical edges: equal total left and right face bends follow from
embedded essentiality. The positive TOP side clock gives the exact
identity

    P=2*ell+sum_selected(T1(v)-T0(v)).                           (3)

This is a conditional identity, not an extra disjoint time payment.

## 4. The lower-sheet side separator and row-5 consequence

Every canonical cycle at level <=M-1 stays on one geometric side of
Gamma. At MIDDLE the selected pairing is wholly LEFT; at level b the
only selected occurrence is unchanged LEFT L3; below b there is no
selected occurrence. The physical face arcs of Gamma have no primal
edge crossing in their interiors. Therefore a lower-level canonical
cycle cannot cross Gamma. An exchange edge between two such levels is
also confined to the side of its physical cell.

Consider the conditional same-Gamma row-5 return in the signed note,
with its downward exchange e at E of history S,N,S,S. The outgoing-L1
MIDDLE endpoint A lies LEFT, so by (2) it is the unique LEFT MIDDLE
node. The outgoing-R2 endpoint is a LOWER b node on LEFT.

If e is a bridge, its outgoing-R2 component cannot reach another
MIDDLE node. Indeed, until its first MIDDLE node, every adjacent-level
path stays on LEFT by the preceding separator. That first MIDDLE node
would have to be A, which is in the opposite bridge component. Reaching
TOP or any higher level also first requires this same forbidden step.
Thus the entire outgoing-R2 component lies on LEFT at levels <=b.

The signed bridge orientation then gives this component total winding
1+m>=1. Some canonical LEFT lower-sheet cycle has winding +1. Since
each entire sheet at j<=b has total winding zero, the SAME sheet has
a distinct negative essential cycle. Its compensation is also LEFT:
the selected ports do not transmit that sheet and the LEFT restricted
sheet has exterior jump zero (both exterior indicators at height b
are one, including every still lower threshold).

We obtain the sharper exhaustive necessary alternative:

- e is nonbridge, hence the full cycle graph has even excess >=2; or
- a LEFT lower sheet j<=b has both a positive and a negative essential
  canonical circle.

The earlier additional-MIDDLE-node alternative is absent in this
leftmost branch-free specialization. This does not rule out either
remaining alternative, does not charge a fresh root, and does not count
one resource per renewal. A single handle or essential pair may support
many local returns. It is not asserted that the conditional row-5
connector has a complete WHITE realization.

## Dependencies preserved unchanged

K1_branch_or_rank3_gate.md, SHA
b85bbad1c675f2604d355db955ddbc08e16771f7c077b1ede1cbb07202e8afe4;
strict_left_K1_right_turn_table.md, SHA
63c41e1359c39e52f2f864d9ec8d66c9f52172af9c4969a5a350134a8a87c511;
finite_local_maximum_plateau_criterion.md, SHA
fb1c92ce019043bd59408c60183076aa9b78dfdfbbc2184a66a0e5be34c9e4d1;
chronological_stream_sheet_exchange.md, SHA
fd20e425b8a6bbc3aefd5eca06b4d443c1d2bdfde5f1d2d69c25d5c4d62af484;
stream_sheet_clocks_and_bridge_sign.md, SHA
552d5aa8cc604cb3899291d688f016652fcd00ab6108e24eb44efa86ea9efe84;
K1_secondary_return_strand_row5.md, SHA
a46d61d8a2b88f9f8ba8525bf8c1d4d58a1a122c04e443be3e7c968721909e46.
