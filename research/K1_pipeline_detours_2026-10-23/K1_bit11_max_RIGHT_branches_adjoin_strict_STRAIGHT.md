# Bit-11 maximum RIGHT branches adjoin a strict STRAIGHT gate

23 October 2026, 20:20 UTC. Exact necessary local geometry. Submitted for
independent review. Complete WHITE cap-four translating front, actual full
P,d, canonical maximum-face first-L curve Gamma and K=1 throughout.
Neither leftmostness nor absence of other branches is assumed.

## 1. A branched bit-11 RIGHT face has two flat helpers

Normalize a RIGHT face F with lower-left (0,0), entry A=(1,0), exit
B=(1,1), helpers Z=(0,0),Y=(0,1). Suppose both selected LEFT-L3 bits
are1 and at least one unused LEFT C neighbor is maximum. The complete
bit-11 RIGHT inventory forces BOTH neighbors G=(-1,-1),H=(-1,1) to
have height M and leaves exactly these complete incoming histories:

    A=NNSN, B=EEWE;
    Z=WWEW, Y=NSSS; or Z=EWWW, Y=SSNS.             (1)

The mixed strict/equal cases are excluded by the complete ordinal port
inventory, not by dropping rank-three or older L suppliers. This is the
bit-11 portion of the independently reconstructed RIGHT inventory used
before the locked-predecessor condition in the signed RR stock gate.
In particular all occurrences of Z and Y, including their actual L3
reads, remain in (1).

## 2. Neither neighboring face can be LEFT

If the preceding face were LEFT, the signed complete LEFT/RIGHT input1,
output1 theorem would force F to strict locked row4: Z=WWWE,Y=NNNS,
with both other heights M-2. This contradicts (1). No LEFT predecessor
is possible.

Suppose instead that the successor G1=(1,1) is LEFT. Its entry is B and
its exit D=(1,2). The one-edge LEFT arc preserves the LEFT-L3 bit, so
D=NNSN. Its next face F2 has lower-left (0,2). All three types fail:

- LEFT is forbidden by the signed all-K no-consecutive-LEFT theorem.
- RIGHT would make G1,F2 a LEFT/RIGHT pair with input bit1. The signed
  complete pair inventory forces its lower helper q' to be NNNS. In
  these exact physical coordinates q'=(0,1)=Y, whereas (1) gives Y=NSSS
  or SSNS. The same physical cell cannot have both complete histories.
- STRAIGHT would have first unused LEFT C neighbor H=(-1,1), already
  maximum in (1). An equal-M straight requires input LEFT-L3 bit0,
  while D has bit1.

Thus no LEFT successor is possible either. The argument retains physical
lifts and whole cell histories, including in short translation quotients.

## 3. At least one adjacent face is strict STRAIGHT

The two neighbors can now only be RIGHT or STRAIGHT. They cannot both
be RIGHT: three consecutive RIGHT faces close the physical elementary
four-edge contact-lattice square, including the face immediately before
the block, contradicting Gamma's embedded essential lift. This is a
geometric physical closure, not a primitive-quotient assumption.

Consequently F has at least one STRAIGHT neighbor. Its shared selected
contact has LEFT-L3 bit1, so the straight neighbor cannot be equal-M,
which permits only0->0. It is a strict STRAIGHT face, with its genuine
rank-three helper/supplier inventory still required.

We have proved, without a global constant-state premise:

    Every bit-11 RIGHT face with a maximum LEFT branch is directly
    adjacent to at least one strict STRAIGHT face.

This statement does not say which side contains the gate, nor that the
branch or the adjacent gate is realized by a complete exterior front.

## 4. Safe constant-one localization and incidence count

If the whole Gamma has LEFT-L3 state constantly1, an equal-M STRAIGHT
branch is impossible and a LEFT face has no unused LEFT corner. Thus
EVERY unused LEFT maximum branch on Gamma is incident at a bit-11 RIGHT
face of section1. Such a face has both maximum neighbors by (1), and
it is immediately adjacent to a strict straight gate by section3.

Let n_B be the number of these RIGHT face classes in the actual full
quotient and n_S the number of STRAIGHT face classes. Count adjacency
incidences on the cyclic face sequence, with lifted contacts retained for
small quotients. Each branched RIGHT contributes at least one adjacent
STRAIGHT incidence and each STRAIGHT has at most two neighboring face
slots. Hence

    n_B <= 2 n_S.

There are exactly two unused LEFT maximum incidences per such RIGHT
face, so that incidence total is at most4 n_S. This is not a count of
distinct maximum supplier faces or new components: physical faces can
supply more than one incidence. It is not a charge to original roots,
permanent fuel, time budgets or independent cycle excess.

Variable-state curves are not silently replaced by constant-one curves.
The local result in sections1-3 applies only to bit-11 branched RIGHT
faces; rises0->1, falls1->0, optional RIGHT L3 and all other branch
modes remain outside that local count unless separately controlled.

## Dependencies

K1_locked_RIGHT_to_max_branched_RIGHT_stock_gate.md, SHA
b9f4b64f05d7680c431086a6d0deb3cbfea3c149681c4db127f0b05d694965b0
(the complete bit-11 flat profiles BEFORE adding the locked predecessor);
K1_LRLR_forces_locked_row4_and_straight.md, SHA
4f9db2ac3df183a0d8fb549fa2efce0ac27f6a0ee94dc2dccd605ff523aee165;
max_face_birth_curve_no_two_LEFT_turns.md, SHA
a93dabfc34aecede83ef23fb81cb7899e3b2c774fbdb489a018bab5768fef20d;
K1_left_L3_state_gates.md, SHA
ac025ac64acb980d7ace6b757f5c6d9902b4084529ff2d38e449f5f6a771130f.

No new bounded period, drift, radius or multiplicity scan is used.
