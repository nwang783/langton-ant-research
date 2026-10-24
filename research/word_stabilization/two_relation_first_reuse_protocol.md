# Proposed two-relation first-reuse protocol

Status: logical proposal awaiting independent review; no new invariant asserted.

Fix a finite macro language with inherited actual right-marker contexts. Every macro has a raw read footprint and endpoint; target first-read templates may include its required next marker. Fix a candidate family F assigning selected RAW first-L cells to macro types. An interval is F-valid when every selected cell at each macro has not been read in any earlier raw macro of that interval.

We seek simultaneous proofs that all physically feasible intervals in the language are F-valid. The following uses two separate forbidden spatial-pair relations, not an assumption that the goal itself is fresh.

## Ordinary relation N

N is forbidden only in F-valid intervals. Its short-gap bases retain precisely the physically feasible gap1/gap2 words that are F-valid, including their target. In addition to the usual strict-gap neighbor and equal-read clauses, N may have a direct clause: an F-mark of the target lies in the raw footprint of the source. This directly contradicts F-validity. Every proper subfactor of an F-valid interval remains F-valid, so the usual minimum-gap argument proves N under its stated conditional premise.

## Goal relation G

G is forbidden in intervals whose every macro EXCEPT THE FINAL TARGET is F-valid. The final target need not satisfy any mark in F. Its short-gap bases retain all physically feasible gap1 words and the gap2 words for which the middle macro's F marks avoid the source raw footprint. Source marks are automatically fresh relative to that interval's own initial cut.

For a source A and target B at index gap at least3, with source successor C and target predecessor D, a neighbor clause requires, for every admissible C,D option, at least one of:
- (A,D) belongs to N;
- (C,B) belongs to G;
- (C,D) belongs to N.
The first and third pairs lie wholly before the exceptional target, and therefore have the ordinary premise. The second has the same exceptional final target and a strictly smaller gap.

For an equal-letter last-A/first-B witness q, every possible raw intermediate reader C must satisfy either (A,C) in N or (C,B) in G. The first pair is wholly before the goal and the second has smaller gap. The target's complete prefix through a first read in its right marker is included literally, exactly as in the audited asymmetric convention. G has NO direct freshness clause at B.

A minimum-gap induction proves all stable G clauses, assuming the separately proved conditional N relation. No circular same-goal freshness is used.

## Closing the first-reuse induction

If every possible earlier-read alignment of every F-mark is excluded by G, suppose an actual interval violated F and take the earliest violating macro B. Its earlier prefix is F-valid. Any earlier macro A reading the violated cell would give one of the excluded G pairs, contradiction. This proves F for every actual interval, with the ordinary right-context convention.

For discovery, start with a candidate F. Compute N and G, remove every mark whose old-read alignments are not all excluded by G, and repeat. Only a SAME-family stable set F may be promoted. If the family empties or a resource cap is reached, the attempt is inconclusive. Certificates must include normal short-word F checks, goal short-word prefix-F checks, all ordinary clauses, all goal clauses, and every final marked-site alignment.

Raw marked sites avoid lookahead charge multiplicity and ambiguity in which macro is the earliest violation. No finite-support premise is needed until distinct first-L cells are charged to the entry black set.
