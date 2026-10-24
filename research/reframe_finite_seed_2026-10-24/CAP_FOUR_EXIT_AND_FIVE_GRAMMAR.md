# Cap-four exit and the exact cap-five first-return grammar

24 October 2026. Author continuation, pending independent audit. This is about
small active w components, not standard-highway capture.

## Exact graph certificate

The finite local kernels in component_kernel_M4.json and component_kernel_M5.json
contain respectively 550/432 and 2774/2292 states/transitions. Their coverage is
as in CAP_THREE_AND_RANK_OBSTRUCTION.md: every physical step preserving the cap
appears, including complete imported components and complete L emissions.

kernel_scc_analysis.py provides integer-only graph checks. Deleting empty-active
state 0 leaves a DAG at BOTH caps. The output files list a complete topological
ordering, checked on every remaining edge. Forward and reverse reachability of
state 0 identify the only possible recurrent strongly connected component.
At cap four it has exactly five states and five edges, the RRRRL reset loop.
At cap five it has 153 states and 262 edges.

## Cap-four exit on any background

Every physical orbit with active w mass at most four leaves this cap within
558 updates, regardless of finite or infinite initial support.

Proof. A cap-preserving state path can visit each vertex outside the unique
five-state cyclic component at most once: a repeated outside vertex would
belong to another cyclic component. Thus it has at most 545 cuts outside that
component. Its visits to the cyclic component form one contiguous interval,
since leaving and returning would put the intervening vertices in the same
strongly connected component.

Within this interval the transition is uniquely the RRRRL cycle, with no
imports. From any phase, the empty state is reached in at most four updates.
But from the empty state, following this cycle for nine updates is physically
impossible: the first RRRRL block emits a complete three-edge star, and update
8 (zero-based) reconnects it to the new three-edge active star. The active mass
at cut 9 is seven, not at most four. Extra passive components either force an
earlier import (already departing this SCC) or leave that forced collision
unchanged. All emitted archives remain physically present. This is precisely
the signed active-flight zero-drift regression, also separately proved by the
physical-lift analysis.

Consequently the cyclic interval contains at most 4+8+1=13 cuts. A complete
cap-four interval contains at most 545+13=558 cuts. Starting at a cap-four cut,
the next 558 updates therefore include an exit. This bound is deliberately
conservative; no optimality is asserted. For finite seeds it implies infinitely
many cuts with active mass at least five. It does not imply eventually staying
above that value.

## Cap-five first-return grammar

Every local-kernel path from empty state back to empty state with no intermediate
empty state is among exactly 110 paths, all explicitly listed with ordered
transitions in kernel_M5_scc.json. Completeness follows because the nonempty
subgraph is a DAG, and the enumeration traverses every possible outgoing edge
from 0 until first return. In a sustained cap-five physical orbit, the empty
state must recur: an arbitrarily long path avoiding it contradicts the DAG.

The 110 paths have only four turn words, with pose normalized to start at
(0,0), north:

- RRRRL: 10 local paths, endpoint (-1,0), west.
- RRRRLL: 1 local path, endpoint (-1,-1), south.
- RRRRLRL: 62 local paths, endpoint (-2,1), west.
- RRRRLRRL: 37 local paths, endpoint (0,2), north.

There are 109 import-containing paths. The sole no-import path is the familiar
RRRRL reset. These are NECESSARY local path options, not 110 physically
composable gadgets. Some may already fail full-field consistency within one
block. The output retains every imported and emitted component and exact pose.

## A non-reset resource obstruction

Path index 11 in kernel_M5_scc.json is RRRRLRL. Its complete transitions consume
one singleton module and emit one singleton module plus one three-edge star.
Thus its net component-type vector is exactly +star. In particular, even after
assigning the reset star weight zero, no nonnegative additive type-weight rank
can strictly decrease on every import-containing first return. This is an
integer resource-vector identity, not an inference from LP infeasibility.

This local macro has westward net heading rotation. Repeating its normalized
path is not asserted to be physically possible; that is a separate full-field
chronology and geometry question. Mixed first-return words, module positions,
and overlaps with emitted stars remain unbounded information absent from a
pure component-type resource vector.

## Status and files

The original cap-three rank and kernel coverage through cap four independently
passed in audit report e2ec84625e48dbb5ec5598b10598ebe05c1c7227b0d2a8e23a7c53d1d34fa91c.
The auditor independently observed the same unique cap-four SCC. The 558-update
composition and cap-five coverage/grammar are author results submitted next.
The exact active-flight theorem remains signed with its lifetime-metadata
clarification; this continuation does not change it.
