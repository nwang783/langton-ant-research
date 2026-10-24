# Exact positive foreign-cycle clock in the inherited return graph

23 October 2026, 21:23 UTC. Finite GRAPH-ONLY certificate submitted for independent replay. No physical prefix or continuation search.

## Scope and clock

Use the immutable 214-state/993-edge coalesced quotient, with labels0D,1C,2V,3U,4F,5Q,6B. Retain its marker and state restrictions; this is NOT a universal presentation of all physically feasible seven-word factors.

Lift a state q to (q,b), where b records whether the preceding raw label was C. On an original edge (q,a,q'), set

    w = 1[a=C] + 2*1[a in F/Q/B] - 4*b*1[a in F/Q/B],
    b' = 1[a=C].

There are428 lifted states and1,986 lifted edges. This is exactly the integer clock proposed for the separately checked canonical foreign-piece tangent joins. The present result is algebraic on this fixed graph even without a geometric interpretation. Do not omit the C→foreign boundary-wrap term. In particular C−2*foreign is only the special case when every foreign word follows C, not a universal identity.

## Exact no-negative-cycle certificate

The artifact supplies an integer potential d on all428 states, taking values0,-1,-2 with multiplicities222,70,136. Every lifted edge u→v satisfies

    w + d(u) - d(v) >= 0.

Hence every directed cycle has nonnegative total clock. No reachability assumption is needed; all lifted states are included.

The zero-reduced-cost subgraph has746 edges. Its complete strongly connected decomposition is stored. NONE of its foreign-labelled edges has both endpoints in one strongly connected component. Therefore there is NO directed cycle of zero clock containing F/Q/B.

Proof of the second assertion: a cycle of zero total w has zero total reduced cost; all reduced costs are nonnegative, so each edge is tight. A foreign edge on that cycle would belong to a tight strongly connected component, contrary to the finite certificate. Thus every cycle containing a foreign edge has strictly positive integer clock. Negative cycles and foreign zero cycles are excluded, not merely absent from a bounded cycle listing.

## A coarse path resource, not merely a cycle sign

A second exact integer potential e satisfies every edge inequality

    428*w - 1[foreign] + e(u) - e(v) >= 0.

Its oscillation is857. Summing over ANY finite inherited-graph walk gives

    T_foreign <= 428*W + e(start)-e(end) <= 428*W+857.

Consequently infinitely many foreign edges on such a graph path force W to tend to positive infinity. This is a genuine graph/path consequence rather than an assumption that recurrence produces a periodic orbit. The constants are deliberately coarse and are not claimed sharp.

## Explicit positive restored-heading graph cycle

Original edge IDs21,232,866 form q9 --D--> --V--> --F--> q9, with preceding-C bit0 throughout. It has clock2 and one foreign edge. Repeating it twice gives q9/bit0/restored-heading0 again, clock4 and two foreign edges. The exact q/bit/heading state sequence is recorded.

This is a GRAPH witness, not a claim that the raw word DVFDVF or its repetition is physically realizable. A finite physical DVFD return exists in a separate signed control, but that does not license repeating its class path or board.

## Exact stopping point

The conditional inherited graph has no zero/negative foreign-clock renewal. Bare formal words such as CCF have zero C−2F clock but are not cycles of this graph. On the BROADER literal seven-word language, QF/BF physical controls already show that this graph cannot be imposed without its original coverage premise.

Even within the inherited graph, unbounded positive clock is not by itself a physical termination theorem. The complete-eight argument also required a simple corrected-center path, positive-clock relevance horizons, and exact frontier recognition. Foreign word pieces do not automatically inherit those hypotheses. A protected current-edge barrier is not path injectivity. No foreign return budget, new K-label union, arbitrary eventual-entry theorem or universal capture is concluded here.

## Replay

The checker builds the lifted graph directly from the original993 transitions, computes and verifies both integer potentials, reconstructs the entire tight SCC decomposition and checks the explicit positive cycle including restored heading. It enumerates no physical prefixes, assumes no cap and supplies exact edge inequalities as the certificate.
