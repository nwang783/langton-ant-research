# A leftmost K=1 maximum component needs a left branch or a straight gate

23 October 2026, 16:09 UTC. Conditional synthesis of the current analytic
extensions, pending independent review. This is not a K=1 exclusion.

## Statement

Take a complete WHITE cap-four K=1 front and the canonical first-L birth
curve Gamma in its LEFTMOST global-max C component. Then either

- Gamma has a LEFT max branch; or
- Gamma has a STRAIGHT face, hence a genuine rank3-to-rank1 gate under
  the branch-free all-LEFT-L3 state theorem.

In particular the leftmost component cannot be both branch-free and an
all-bend curve. Other maximum components, their birth trees and arbitrary
straight-gate detours are retained.

## Exact dependency chain

Assume Gamma has no LEFT max branch and no straight face. The signed
branch-or-rank3 theorem gives a LEFT L3 at every selected contact. All
faces of Gamma are now RIGHT or LEFT bends.

The pending RIGHT/LEFT theorem gives two facts: every adjacent RIGHT,
LEFT pair uses strict-right row 4, and RIGHT,LEFT,LEFT is impossible.
An embedded essential circle in the flat drift cylinder has total signed
turn zero. One elementary justification is to take the annular region
between the circle and a distant parallel straight circle: it has Euler
characteristic zero, the metric has zero interior curvature, and the
straight boundary contributes zero turn. Thus the polygonal boundary
has equally many LEFT and RIGHT quarter turns.

If a cyclic all-bend word had two adjacent LEFT turns, its maximal LEFT
run would be preceded by RIGHT, producing the forbidden R,L,L triple.
(The all-LEFT word is already excluded by the zero total turn.) So LEFT
turns are isolated. Equal LEFT/RIGHT counts then force every separating
RIGHT run to have length exactly one. The turn word alternates R,L.

Alternating diagonal contact-lattice steps have fixed direction on every
other edge. After one genuine quarter rotation and translation, Gamma's
contacts are A_k=(1,2k), B_k=(1,2k+1), with full drift d=(0,2a), a>=1.
Every RIGHT face is followed by LEFT and hence is row 4. The complete
main histories are therefore exactly

    Z_k=(0,2k):   W,W,W,E;
    Y_k=(0,2k+1): N,N,N,S;
    A_k=(1,2k):   N,N,S,N;
    B_k=(1,2k+1): E,E,W,E,

all with turns RLRL. No primitive-period replacement occurred. These
are the locked bent main histories, not the prepared fuel histories.

The pending secondary-rail chronology theorem forces a deeper C face
at height at least c_right=M-1. The complete separating C row has height
M-2=c_left. The pending finite local-maximum plateau criterion then
forces a further M face to the LEFT, connected to that raised face
through {h>=c_right}. This maximum component is distinct from Gamma's
because the entire intervening low row separates them in the C-contact
lattice. It contradicts the chosen LEFTMOST maximum component.

Hence some STRAIGHT face or LEFT max branch is necessary. If branch-free,
a strict straight face has all selected LEFT L3 and its actual path
A.L3 -> Z.R2 -> B.L1 is the signed rank-lowering gate. It is not assigned
a paid budget here.

## Status and open supplier geometry

The all-bend subcase is reduced to the already documented locked rail.
The new conclusion still permits LEFT max birth trees and arbitrary
strict straight-gate arrangements at the leftmost component. Neither
straight gates nor branches have a proved fresh or permanent resource
charge. No standard104 uniqueness or finite-seed capture follows.

Dependencies awaiting review:
K1_right_left_forces_row4_gate.md, SHA
04953c96737e932323f29e343dfd07096401c4fa74f710bec07a3c76a8fcc3ed;
bent_secondary_rail_height_obligation.md, SHA
f8a56ac667b3475e3328b86a6420d411c5fe4f03e735d0db02d5615e308185ce;
finite_local_maximum_plateau_criterion.md, SHA
fb1c92ce019043bd59408c60183076aa9b78dfdfbbc2184a66a0e5be34c9e4d1.
The signed branch-or-rank3 theorem and strict straight gate are retained
unchanged. This synthesis is not represented as independently signed.
