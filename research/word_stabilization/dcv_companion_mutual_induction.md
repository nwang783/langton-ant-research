# Companion source-output flags and simultaneous protected-transfer induction

This is an analytic protocol. A candidate family becomes a theorem only after every required no-hit model and inductive invariant has been independently verified against the same frozen family. Discovery stages are not forbidden relations.

## Scope and finite family

Use the recurrent marked packets D, DC, V, VC, VCC and their actual complete RAW+M11 contexts. A row is `(A,B,x,y,h,qx,qy)`, with source at the north origin, q a residual black output of RAW A, and that same physical cell a residual input of the target B at `(x,y,h)`. Its protected premise says that every strict intermediate packet's COMPLETE context avoids q. The exact residual ledger and original ordinary/protected relation are already signed.

Let S be a finite independently signed family and H a finite candidate family containing S. Each row in H minus S must receive its own no-hit patch certificate generated against exactly H. Rows outside H are never implicitly forbidden. Observed feasible controls are explicitly excluded from the candidate universe.

## State and exact updates

Retain a finite color patch containing q and EVERY source residual output. Use the anchored-patch head states and conservative OUT abstraction. For each source output q' other than q, append an initially-one Boolean flag. Its meaning is that every earlier strict intermediate COMPLETE context has avoided q'.

A strict intermediate packet whose complete context touches q' clears that flag permanently. The flag is cleared even if the actual RAW portion did not touch q'; this conservative early retirement cannot remove a physical history. Because every flagged cell belongs to the patch, a wholly OUT packet cannot touch a flagged cell. OUT reentry retains all colors and flags.

Before executing a candidate strict intermediate packet C, if the normalized source-to-C tuple for a still-live q' lies in H, reject that transition. This rejection is encoded by requiring its flag to be zero. Independently signed S rows may also filter the outer target goal. Unproved H-minus-S rows MUST NOT filter the outer target goal, even for a different source companion output: that pair has the same outer temporal gap, not a smaller one.

Packet color updates are exact guarded XOR followed by forced-zero flag clearing. Initial unknown color bits form the entire Boolean cube. No one chosen completion may stand in for that cube.

## Why mutual induction is sound

Assume some row in H minus S has a physical counterexample, and choose one with the least actual packet-index gap. This minimization is across the whole finite family, not separately within each row. Map its colors, head poses and flag meanings into that row's finite graph.

Every ordinary or already signed protected guard is valid. Suppose a hypothetical H guard would reject one of the actual strict intermediate packets C. The corresponding q' is black immediately after RAW A, because it is a source residual output. Its live flag says that every earlier strict intermediate complete context avoided q'. Hence A to C is a physical protected pair in H, with strictly smaller gap than A to B. It cannot belong to S, whose rows are already proved, or to H minus S by minimality. Therefore no actual transition is rejected.

The outer target is not rejected by an unproved H guard. Its colors must satisfy the accepting condition, contradicting the certified no-hit invariant. Thus no counterexample exists to any row of H minus S. This proves the family simultaneously.

Spatial returns to the same source pose/type do not change this argument: the induction parameter is temporal index gap. Arbitrarily long far excursions are already represented by OUT. A capped search, an abstract witness, an unverifiable BDD, or a missing family member cannot establish the theorem.

## Discovery versus proof

`run_dcv_mutual_family.py` begins with 221 exact residual-transfer candidates minus 19 explicit physically realized controls. It fixes the earlier 38 signed clauses (37 on-list plus the separate original DC upper-output test). A stage exhausts candidate graphs under its current H, removes every witness/cap result, and repeats. If it stabilizes, only its final H and final-stage invariants may be submitted as a mutually inductive proof. Earlier-stage no-hit invariants used stronger assumptions and are not independently promotable without checking them against the weaker final graph.

The separate `check_dcv_direct_source_flags40.py` tests whether an earlier invariant already remains inductive after replacing all candidate assumptions by the independently signed40 relation. A successful replay is a direct signed-dependency proof, not mutual induction, but still requires independent literal-model and invariant audit.

Positive controls with explicit finite seeds, maximal-C boundaries and full protected-context checks are in `dcv_observed19_witnesses.json`. They are not merely BDD witnesses. The known false universal V-freshness claim remains false, including the DCVCCVV control.
