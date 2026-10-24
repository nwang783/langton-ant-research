# Standard capture in the seven-word single-defect grammar

Status: independently audited exact finite certificate. The theorem below is standalone and does not assume correctness of the larger exploratory graph.

## Literal language

Use these seven raw before-marker words:

- 0: `RRRLLRLLR`; next marker `RRRLLRLLRRRR`.
- 2: `LLLLRLRRRRLRRRR`; next marker `LLLLRLRRRRLR`.
- 3: `RRRLLRLLRRRRLLR`; next marker `RRRLLRLLRRRR`.
- 26: `RRRLLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR`; next marker `LLLLRLRRRRLR`.
- 37: `RRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR`; next marker `LLLLRLRRRRLR`.
- 39: `LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLR`; next marker `RRRLLRLLRRRR`.
- 57: `LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRLRLLR`; next marker `RRRLLRLLRRRR`.

The only allowed adjacent macro pairs are:
(0,3),(0,37),(2,39),(2,57),(3,0),(3,26),(26,2),(37,2),(39,37),(57,3),(57,37).
Every macro endpoint has its stated actual twelve-turn next marker. This premise is automatic in an infinite concatenation obeying these pairs, including the short9-turn word0, whose next three turns complete its marker.

## Theorem

Every physically feasible infinite word in this language, started from a finite black board, is eventually the standard104-turn highway word.

In any finite factor with the specified actual right context, the local phase7 L site(2,-3) is unread earlier in the factor at every macro0 or26; the local site(-3,-3) is unread earlier at every macro57. These cells are inside the raw words. Consequently the total number of occurrences of0,26,57 is at most the black mass at the factor entry.

After their last occurrence, type3 cannot persist because its only successors are0 and26. The remaining graph is exactly the directed cycle2 ->39 ->37 ->2. Its literal concatenation has length104 and is a cyclic rotation of the standard word.

## Finite certificate and induction

spatial_single_bad57_kernel.py/json enumerates8,501 overlapping relative source/target types with all four headings and the exact necessary pose parity. There are23 short feasible types at macro-index gaps1 or2. The stable forbidden family has8,028 types. Every row has either a successor/predecessor strict-gap certificate or an equal-read certificate quantifying all literal intermediate reader poses. The seventeen short triples are exactly all triples admitted by the eleven adjacent pairs; no hidden long-graph condition is needed.

Sources use only RAW last reads and footprints. Targets use FIRST reads of RAW + their stated next marker. Endpoints remain RAW. Every proper subfactor inherits that required marker. Equal-read barriers inside the marker include the full target prefix up to the barrier and hence omit no possible read. This is the same asymmetric, strict minimum-gap argument as the independently checked six-word N theorem.

Querying the stable family excludes every old-read alignment for the three selected marked sites. The certificate in fact proves three fresh first-L sites inside raw26, so a stronger weighted count n0+3*n26+n57 <= entry mass is available. The single-site count suffices for capture.

## Relation to the larger experiment

The unreviewed1682-state spaced-K quotient, after deleting every K-bearing label except57, has a33-state cyclic component whose labels and pair grammar are exactly those above. It also has the previously handled five-macro H component. This observation is only a bridge awaiting a separate graph audit. The standalone literal-language theorem and its certificate do not depend on that bridge.

The earlier zero-new-fuel example for macro57 uses an old U writer before entry into this seven-word grammar. It therefore does not contradict this factor-relative freshness theorem.

Independent reconstruction: audits/check_single_bad57_independent.py and its JSON result. This verifies the standalone literal language, not the larger graph bridge.
