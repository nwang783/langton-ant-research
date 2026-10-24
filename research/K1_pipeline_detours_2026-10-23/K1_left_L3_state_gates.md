# The selected LEFT-L3 bit can renew only at a branched right turn

23 October 2026, 14:50 UTC. Exact necessary local state consequence of the
signed straight and bend tables. Submitted for independent review.
This is NOT a charged budget, no renewal existence is asserted, and no
front exclusion follows.

## Definition

For the signed K=1 first-L curve with contacts v_i and parent faces F_i,
put s_i=1 if v_i has a complete L3 read on LEFT, and s_i=0 otherwise.
Thus0 retains both no-L3 and optional RIGHT-L3 possibilities. At F_i,
read the transition s_(i-1)->s_i. Keep actual full P,d and ell.

## Exact necessary transition rules

1. LEFT turn: s_i=s_(i-1). The LEFT parent-face arc is one physical edge.
   Its complete outputs at v_(i-1) are L1,R2 and LEFT L3 if present;
   its complete inputs at v_i are R0,L1 and LEFT L3 if present. Counts
   2+s_(i-1)=2+s_i give equality. If both bits are1, the two actual L3
   reads are consecutive physical events, increasing time by1.

2. STRAIGHT, strict LEFT other-C neighbor: s_(i-1)=1, while s_i may be0
   or1. This is the signed strict-corner ordinal result. More precisely,
   if s_i=0 the nearcorner has RLR headings W,W,W; if s_i=1 it has RLRL
   headings W,W,W,E. Selected RIGHT L3 is retained in state0.

3. STRAIGHT, equal-M LEFT other-C neighbor:0->0 only, from the signed
   unique RLRL nearcorner W,W,E,E. Moreover the NEXT face must bend.

4. RIGHT turn, BOTH intermediate LEFT other-C neighbors strict: the
   six signed local port families allow only0->0,1->0,1->1. They do NOT
   permit0->1. In the0->0 rows both helper corners have one R and other
   C heights M-1. In the1->0 or1->1 rows both have two Rs and other C
   heights M-2. This remains merely a necessary exterior-relaxed table.

All possible face geometries are straight, left turn or right turn;
a simple embedded first-L cycle has no immediate backtrack. Therefore

    Any rise 0->1 requires a RIGHT turn AND at least one equal-M
    other-C neighbor on its LEFT.

This is a necessary rank3 renewal-GATE classification, not a supply
construction. The helper E/W histories, real previous outputs and both
side-current boundaries must still connect.

## Safe whole-curve consequences and exact open cases

Since s_(i+ell)=s_i, the number of0->1 rises equals the number of1->0
falls. Thus any face where the selected LEFT-L3 bit is lost requires
some branched-right-turn renewal gate elsewhere on the actual full
curve. No payment per gate, age bound or additive time claim is made.
If no such gates occur, the bit is constant:

- Constant0: no strict-left straight face; every straight face has a
  LEFT max branch and is immediately followed by a bend. At strict-left
  right turns the one-R helpers and optional paired RIGHT L3 remain.
- Constant1: no straight equal-M LEFT branch. Left turns transmit an
  actual L3 event directly. Strict-left right turns retain the three
  two-R1->1 families from the signed six-row table.

These alternatives do not exclude any whole front. They isolate where
source-L3 chronology can really renew, rather than charging every max
branch or silently discarding the constant0 one-R bend mode.
