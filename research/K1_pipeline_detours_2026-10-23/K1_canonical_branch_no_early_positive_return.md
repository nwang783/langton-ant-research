# A canonical LEFT branch cannot return positively to an early part of its own K1 curve

23 October 2026. Complete WHITE cap-four K = 1 front. This extracts the continuous-cursor argument from the specific half-turn square. It has no zero-output hypothesis and does not exclude cross-Gamma transfer.

## Precise hypotheses

Write the selected maximum curve as consecutive faces F_k in parent-to-child orientation, with selected contact v_k from F_k to F_(k+1). Fix D = F_i. Suppose an actual canonical branch

    D -> A_1 -> ... -> A_t

leaves Gamma into its LEFT component, with every A_s strictly off Gamma. Suppose A_t has a flat max/max contact with H = F_j, j <= i-2, and at that contact R0 chooses H while R2 chooses A_t. This is a POSITIVE return contact when the closing chord is oriented A_t -> H; it is not a canonical edge of that branch.

Use physical lifts. All branch faces and the positive return are distinct from the interior of Gamma, so the branch plus closing contact forms an embedded chord. Equivalently this disjoint embedded geometry may be included as an explicit hypothesis if applying the lemma to a separately constructed branch.

## Literal boundary inventory

The finite Gamma arc H -> D and chord D -> ... -> A_t -> H bound a physical ear on the LEFT of the oriented Gamma arc and LEFT of the oriented chord. Its interior is bounded. Each open cut segment and face-center join lies inside physical face interiors; only its specified primal contacts meet the lattice path.

At a canonical branch contact, R0 crosses LEFT -> RIGHT and exits the ear, while R2 crosses RIGHT -> LEFT and enters. L1 and optional L3 remain on one side. Every such R2 follows its actual child birth, and those births strictly increase from B(D). Hence every canonical-chord R2 entry occurs after B(D).

At the positive closing contact the roles reverse: R0 enters the ear and R2 exits. There is exactly one possible entry of this type. Optional L3 remains on one side. The same exhaustive R0/R2 crossing table holds on the Gamma arc. Complete flat histories are RLR or RLRL; no one-R corner or additional physical port is omitted.

## Chronological contradiction

Since j <= i-2, the first two contacts v_j and v_(j+1) on the Gamma arc are distinct physical occurrences. K = 1 gives

    T0(v_j) < T0(v_(j+1)) < T2(v_j).

The selected R2 times increase with the index, so no Gamma-arc R2 entry occurs before the second displayed R0 exit. Both exits precede B(D), because their target births are at most B(D). No canonical-chord R2 entry occurs by then either. Therefore, before these two exits, at most the single positive-return R0 has entered the bounded ear.

The actual cursor is outside the fixed bounded ear for all sufficiently negative times, by complete translated periodicity with nonzero drift. Two exits with at most one earlier entry are impossible. This proves the lemma.

## Exact scope

A positive return to the SAME selected curve cannot reach F_(i-2) or any earlier face. An immediate-predecessor return F_(i-1), a return to D itself, a later return, or a return to a DIFFERENT selected curve is not excluded here.

A useful application criterion is B(H) < B(F_(i+1)) together with physical distance forcing at least two Gamma edges from H to D. Selected birth monotonicity then puts H before D, and the distance rules out the immediate-predecessor escape. In the half-turn square H = (-4,0), D = (0,0) and B(H) <= B(F_(i+1))-13, so this criterion applies.

This is a rank-two actual-cursor obstruction along arbitrary-length canonical branches. It is not an output or fuel charge, a per-renewal current subtraction, or an assumption that the branch itself repeats. Cross-Gamma transfer and same-component off-cycle ancestry remain open.

Dependencies: canonical max-face birth and embedded graph c9171009; K = 1 physical cursor pipeline 2e940091; exhaustive flat crossing table 30b6aab0; bounded physical-ear cursor interface fe600cde. The specific application and its port deadline are frozen in half_turn_supplier_cannot_return_to_same_Gamma_v2.md, 7ef1fd92.
