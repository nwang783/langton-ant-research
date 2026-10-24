# A C-first five-C W crossing cannot be the first center self-contact

23 October 2026, 14:24 UTC. This is a bounded-clock but all-word chronological
necessity, using existing signed counted clauses and exact zero/one-C cones.
Independent reconstruction is requested. No path search or guessed box is used.

## Exact conditional geometry

Normalize an actual C atom's entry to (0, 0, N), and use corrected centers
p + rot_h(-1/2, -1/2). The proper W-oriented crossing of its chord occurs at
a later V base with head (1, 0, W). Suppose their atomic ENTRY C clocks differ
by five, and suppose the contact in this V chord is the first self-contact of
the center path under consideration.

The C atom freshly installs q = (1, 2). At the later V pose, q is local
(2, 0), which is before-white at marker read 8, not an input. Thus its old
identity must have been retired by a STRICT earlier residual-consuming base.
The C atom also installs (2, 0), which lies in the later V core, but q alone
suffices for this proof. Replacements do not revive the retired old identity.

The conclusion is that these hypotheses are inconsistent. This does not ban
the same geometric crossing after an earlier center contact has already
occurred, and it does not assert any five-C full-pose nonreturn theorem.

## Full-producer and atomic clock alignment

An actual C atom has seven possible full-producer roles: the first C of DC,
VC, VCC, UC or UCC, and the second C of VCC or UCC. At a first C, its entry
clock equals the full producer's entry clock. At a second C it is one later.
All seven exact producer-relative positions of q are reconstructed by the
checker, and each is an output of that actual full producer.

If a first consuming full packet starts at atomic gap delta, its full-source
included age is delta for a first C, and delta plus one for a second C. The
query inventory keeps that shift explicit. Source tails cannot consume any
residual identity, so the consuming packet must begin after the full source
finishes. Since the target is a later V BASE, rather than a cut inside a tail,
the consuming full packet must also finish before the target. Its attached C
count plus delta is therefore at most five.

The finite table accounts for all 966 choices of seven source roles, gaps
zero through five, and all 23 input slots of the eight possible consumers.
Options are excluded only by those timing facts, sector, or existing signed
KV clauses, before the following geometric cases are considered. Count value
five is the signed overflow class for full-source ages at least five; the
shifted age-six queries is not silently treated as exact age five.

## The only options left by the signed relation

For each of the five first-C roles, the only remaining consumers of q are
zero-C U packets at atomic gap five, with heads (2, 3, W) or (3, 2, W). Their
base exits are (-2, 3, W) or (-1, 2, W). No C remains. Every W zero-C base
moves strictly left and never down, so neither exit can reach (1, 0, W).

For either second-C role, no consumer before atomic gap four survives. At
gap four, six eligible consumer placements per role already have a CLOSED
center-chord contact with the source C chord. They therefore contradict the
first-contact premise. Endpoints and collinear contact count; only checking
proper transverse intersections here would be insufficient.

The other six gap-four placements per second-C role finish a N-oriented base
with y at least two. Exactly one C remains, rotating N to W and adding one to
head y. All intervening N and W zero-C bases have nonnegative y increment.
The later head would have y at least three, not zero.

The gap-five options are the same two zero-C U placements already excluded
by the final W cone. Thus every possible strict retirement is impossible or
already creates an earlier center self-contact. This proves the conditional
statement without bounding the number of zero-C packets.

## Scope and reproducibility

Working checker: check_C_first_W_crossing.py.
Finite table: chronology_dcuv/C_first_W_crossing.json.

The checker keeps every full-source query, atomic shift, consuming tail count,
closed-segment contact and endpoint inequality. It uses the literal complete
recurrent-eight geometry and the signed cap-five relation, not an enlarged
standalone-C language. The first-contact two-through-six-C theorem and the
proper-crossing catalogue explain why this is the relevant C-first W branch;
they are not needed to prove the explicit conditional five-C statement above.

The C-first E crossing at gap three can consume the common output at the
crossing itself and is not excluded here. Other source atoms, degenerate
first contacts, larger returns, V1, U1 and global capture remain open.
