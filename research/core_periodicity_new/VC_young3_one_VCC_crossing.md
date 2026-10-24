# An all-word two-C input-crossing obstruction in the VC-young3 branch

23 October 2026 12:02 UTC. Author finite induction certificate passes;
independent analytic/literal reconstruction requested. No length, mass, seed,
excursion, or parameter bound is assumed.

## Exact statement and remaining scope

Normalize the source to VC at(0,0,N). There is NO actual complete recurrent-eight
factor whose strict middle is A,VCC,B, where A and B are arbitrary finite words
over zero-C D,V, and whose target U starts at(0,-1,E). These are exactly the
one-VCC/no-U members of the young lower-pair age3 VC-source branch. This is a
conditional grammar/pose exclusion, not all VC-young3 or U1. In particular two
separate one-C packets, any zero-C U, and a middle UCC remain outside the claim.
The statement does not need the stronger funding-record or target-survival
premises; it follows from endpoint geometry and the signed produced-D age3 law.

## Parallel row paths and ordered identity reuse

Source VC exits at(1,4,W), at C clock tau+1 if its outputs' birth clock is tau.
Outgoing D and V endpoints are(-1,1),(-3,1): each rises EXACTLY one horizontal row.
The one VCC then moves(-4,0), turns to E and adds exactly2 C. Returning D and V
endpoints are(1,-1),(3,-1): each descends exactly one row. All outgoing packet
inputs, including VCC's, are removed at clock tau+1. All returning packet inputs
are consumed at clock tau+3. The removed ordered identity cannot revive through
black-to-black recycling; every replacement born after its removal is at most2
C old at return, too young for a produced D input, whose signed minimum is3.

At a row common to both head paths, write Delta=incoming_head_x-outgoing_head_x.
Let the CURRENT outgoing type be the D or V packet starting at that row; at the
top row the current type is the far VCC. If Delta=-4 and that outgoing type is
V or VCC, its lower input is(outgoing_x-3,row). A returning D's input is
(incoming_x+1,row), EXACTLY the same cell. Thus this transition is impossible
by the preceding ordered-age reuse argument, even if helpers replace its color.
This is about residual retirement, not the timing of a literal L read.

## A finite invariant for arbitrarily long outgoing/returning words

At the top row Delta=-4 and current outgoing type=VCC. We claim inductively:

  Delta>=-4; if Delta=-4, the current outgoing type is V (or top VCC), not D.

All gaps are even. To descend one row, let b in{1,3} be the incoming D/V width,
and a in{1,3} the width of the outgoing packet at the NEXT LOWER row. Then
Delta'=Delta+b-a, and the new outgoing type is D if a=1, V if a=3.

- At Delta=-4, the returning D case b=1 is forbidden by identity reuse. For
  b=3, a=1 gives Delta'=-2,typeD; a=3 gives Delta'=-4,typeV.
- At even Delta>=-2, the successor is at least-4. Equality can occur only from
  Delta=-2,b=1,a=3, whose new outgoing type is V.

That proves the invariant for every number and ordering of packets. The finite
checker explicitly verifies the only boundary gaps and the affine positive ray;
it does not extrapolate a finite packet/coordinate search.

## Contradiction at the bottom row

Let N=|A|. The outgoing head rises from row4 to row4+N. The far VCC has no y
motion. To reach U at row-1, the incoming path has N+5 packets. After its first
N descents it is at bottom row4, where FIVE further packets remain. Each moves
right by at least1, so its x at bottom is at most-5 in order to end at x0.
The outgoing bottom head is(1,4). Thus Delta<=-6, contradicting Delta>=-4.
This also covers N=0 directly. No core can be freely transported across this gap.

One displayed subfamily is VC,V^r,VCC,V^(r-1),D^6,U for r>=1. Its first return D
reuses(-5,5), retired by VCC when r=1 or by the second outgoing V when r>=2.
The full row argument above covers all D/V interleavings, not just this subfamily.

Files: check_VC_young3_one_VCC_crossing.py and
chronology_dcuv/VC_young3_one_VCC_crossing.json. This is the structural obstruction
extracted after the one-shot arbitrary-middle discovery probe capped100k states
UNKNOWN; that cap is not part of the proof and is not increased.
