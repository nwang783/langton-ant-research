# Ordered port pairing in a hypothetical multiplicity-three periodic front

22 October 2026. Analytic proof independently reviewed by the proof-certificate auditor on 22 October 2026. This does not classify all periodic fronts, and no nonstandard finite-seed front is constructed.

## Setting

Let a finite-seed translating periodic ant word have full nonzero displacement d. Assume every displacement class has at most three read phases. The exact stable chronology criterion implies that sufficiently far-forward representatives have complete histories R, RL, or RLR. They are outside the initial support and have no time-zero exception. Work with these literal physical histories, then count translation classes.

Let n1 be the number of singleton classes. Split the three-read classes into n_s and n_o according as the incoming headings at their first and third R reads are the same or opposite. Let R1, R4, L1, L4 count cyclic maximal constant-letter runs of the indicated lengths. Runs have lengths 1, 2, or 4: length 5 and interior length 3 violate consecutive same-cell alternation.

## 1. Same-heading triples pair along triply traversed edges

At a fixed physical cell the incoming headings have one fixed axis, hence take only two opposite values. For a three-read cell with first and third heading A, its heading list is either AAA or A(-A)A. In the first case its three incoming edges coincide. In the second case its three outgoing edges coincide, because the middle turn is L and the other two are R.

An edge used three times has both endpoints visited at least three times. Under the cap they are visited exactly three times, and the three crossings match first-to-first, second-to-second, third-to-third. Thus the source has heading type A(-A)A and the target has constant heading. Their crossing turn pairs are RR, LL, RR.

Consequently the same-heading three-read classes partition into disjoint adjacent pairs, each joined by one triply used directed edge. Translation preserves the complete chronological heading type. Each pair contains one constant-heading endpoint and one alternating-heading endpoint, so no pair identifies with itself in the translation quotient. In particular n_s is even. On the third passage, each pair contributes two consecutive R reads.

This is an exact port-graph statement, not a conclusion that the intervening paths are disjoint or erasable.

## 2. Four-run markers are opposite-heading triples

The fourth R of each cyclic R4 run is at the cell read immediately before that run, where the turn was L. That L is the cell's second read, and the fourth R is its third. The two incoming headings are opposite. If the first and third R headings were equal, this would be an alternating-heading triple with all three outgoing edges equal. Its successor would then receive three visits, but its two displayed visits (the first R of the R4 block and the L immediately after it) are R then L and must be its first two visits. The additional earlier visit is impossible. Therefore this marker belongs to n_o. Its heading pattern is A,A,-A, with the last heading used as the negative reference.

The R immediately following each L4 run is the third read of the L4 run's initial cell. Its second and third incoming headings coincide. If its first heading also coincided, all three incoming edges would coincide. Its predecessor would then be visited three times, but the displayed predecessor reads just before and at the end of the L4 run are R then L, necessarily its first two visits. Again the additional earlier crossing is impossible. This marker also belongs to n_o, with heading pattern A,-A,-A.

The R4 and L4 marker events are all distinct. Hence

    R4 + L4 <= n_o.                                      (1)

## 3. Singleton-L charge capacity

Every L is the second read of an initially white cell. For a singleton L at v, compare its incoming heading to the preceding R at v.

- Equal headings: the two predecessor cells coincide. The R immediately before the singleton L is a non-first R, hence a third R. Charge it.
- Opposite headings: the two successor cells coincide. The R immediately after the singleton L is a non-first R, hence a third R. Charge it.

There are no initial-head or endpoint exceptions in sufficiently far-forward complete periodic histories. This is the inherited merge/fork charge, now with its capacity evaluated using the three-read port types.

### Opposite-heading triples receive at most one charge

Let v's first and third R incoming headings be opposite, and call its third heading h. To receive a charge from the singleton L immediately before v, the earlier R at that predecessor must also move into v with incoming heading h. Since v's first heading is not h, this earlier arrival is v's middle L; its heading must be h.

To receive a charge from the singleton L immediately after v, v must have an earlier outgoing edge equal to its current R outgoing edge. Its first R has the opposite outgoing direction, so the earlier traversal is its middle L. The middle incoming heading must then be opposite h. The two requirements are incompatible.

An L4 marker can receive no charge: its middle heading equals its third heading, so only a preceding singleton L could charge it, whereas its preceding L belongs to a run of four.

### Each same-heading pair receives at most one charge in total

Write u -> v for the triply used edge, whose third passage is RR. Only a singleton L immediately before this pair or immediately after it could charge its two R events.

Suppose both neighboring turns were L, even without assuming singleton status. Call their cells w before u and z after v. Both are second reads. The first R at u has the same incoming heading as its third R, so its predecessor is w, whose read there must be its first R. Similarly, the first R at v is followed by the first R at z. Therefore the first passage contains the four consecutive R reads w,u,v,z. Geometrically the predecessor of w in this R4 block is z. This is an earlier read of z, contradicting the assertion that its read after v is its first. Thus at most one neighboring L, and hence at most one charge, is possible.

Summing capacities gives the sharpened exact inequality

    L1 <= n_o - L4 + n_s/2.                              (2)

## 4. Consequence for run counts and growth

The signed turn excess of a cyclic word is

    g = -R1 + 2R4 + L1 - 2L4,

because the numbers of R and L runs agree. The white-input chronology also gives g=n1+n_o+n_s. Combining (1) and (2) yields

    n1 + R1 + 5 L4 + n_s/2 <= 2 n_o.                    (3)

If n_o=0, (3) forces n1=n_s=0, hence g=0. A nonzero finite-seed translating front has positive growth by the established mass/displacement inequality. Therefore there is no such front with n_o=0. Thus any hypothetical multiplicity-three finite-seed front must include a cell whose first and last R reads arrive in opposite directions. The global two-visit theorem alone does not distinguish these port types.

The inequality does not rule out n_o>0. For example, the bare nonnegative numbers n1=4,n_o=4,n_s=R1=L4=0 satisfy it and have admissible growth g=8. These are only numerical counts, not an asserted ant trajectory or complete combinatorial realization.

## 5. Scope and next target

The useful remaining cap-three question is whether opposite-heading triples can reproduce indefinitely on a white-input periodic front. Each is one of two mixed heading patterns, A,A,-A or A,-A,-A. The pairing proof does not say their doubled-edge interaction graph is a forest, does not bound its winding, and does not justify deleting simple pose loops. A proof of one of those stronger claims, or an exact obstruction to it, is still needed.
