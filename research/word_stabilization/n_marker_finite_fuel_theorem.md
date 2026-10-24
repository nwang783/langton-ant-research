# Fuel theorem for the six N-return words

Status: independently audited exact finite certificate.
This is a new restricted-language theorem, not the highway conjecture.

Let N=RRRLLRLLRRRR. The six literal before-marker words are:

- 0: `RRRLLRLLR` (9 turns).
- 3: `RRRLLRLLRRRRLLR` (15 turns).
- 8: `RRRLLRLLRRRRLLRLLRLRLLR` (23 turns).
- 10: `RRRLLRLLRRRRLLRLRRRRLRLLR` (25 turns).
- 45: `RRRLLRLLRRRRLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR` (50 turns).
- 71: `RRRLLRLLRRRRLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLR` (77 turns).

Let E={8,10,45,71}. Consider a finite word of these macros, followed by the literal12-turn right context N. Assume the whole turn string is physically feasible under right-on-white/left-on-black/flip/move, and contains no macro factor a,3,b with a,b in E. The entry board may otherwise be arbitrary. Freshness below is only relative to the beginning of this macro factor.

## Statement

Every macro of type0,8,10,45,71 reads the cell with local coordinate(2,-3) for the first time in the factor, with letter L at phase7 (zero-based). Type3 need not have that freshness property.

Literal two-macro feasibility forces type3 to alternate with the other five types. Consequently, if the board at the factor entry has m black cells, the number of non3 macros is at most m, the total number of macros is at most2m+1, and their raw turn length is at most92m+15. In particular, no infinite finite-support stream satisfying these hypotheses exists.

## Exact certificate

The generator spatial_n_marker_separated_kernel.py uses source footprints and last reads from the RAW macro, but target footprints and first reads from RAW MACRO + N. Endpoints remain those of the raw macro. It enumerates7221 overlapping relative types (source ID,target ID,dx,dy,heading), with all four headings and the necessary parity dx+dy=heading mod2. Twenty types occur at physically feasible index gaps1 or2 under the stated short forbidden-factor premise. They are removed before iteration.

The stable forbidden family has6562 types. Every member is justified either by universal successor/predecessor descent or by an equal-letter last-source/first-target read whose every possible intermediate reader is excluded by a proper subpair. All reader poses are generated from every literal raw footprint coordinate and every heading, with no spatial cutoff. No independently assumed fresh marker is used.

The minimum macro-index-gap proof is the same strict descent as in the earlier C-free certificate. For gaps at least3, the source successor and target predecessor are distinct. Every proper subfactor inherits both the forbidden-factor premise and its actual next N marker. Although a target first read may lie in its twelve-turn right context, that full prefix is included in the target template, so there is no omitted read between the target cut and the selected first occurrence. Only raw intervening macros are enumerated as readers. An actual previous read of the claimed phase7 cell would yield one of the explicitly excluded overlap types.

The five marked first-L cells are therefore distinct physical cells that were black at factor entry. The two-macro feasibility list is exactly (0,3),(3,0),(3,8),(3,10),(3,45),(3,71),(8,3),(10,3),(45,3),(71,3). Each non3 word has length at most77 and each3 has length15, giving92m+15.

## Bridge to spaced adjacent defects

Use J(t) for the bad standard-ten window ending at t and K(t)=J(t-1)J(t). The four exceptional words have their designated K endings at local offsets19,27,51,48, respectively, including the required next marker when the ending is beyond the raw macro. In a,b separated by type3, the two designated K endings differ by |a|+15+k_b-k_a. The sixteen values lie between32 and95. Thus spacing of distinct K events by at least96, and in particular by at least140, forbids every a,3,b factor.

The exploratory150-history graph for K spacing140 has a two-marker return decomposition into88 words. Its N-to-N words are exactly these six. Removing BOTH markers leaves an acyclic graph. Therefore, once that graph decomposition is independently certified, the present theorem implies that every infinite finite-support path in that language visits the original marker M=LLLLRLRRRRLR infinitely often. This does not exclude the main component, which contains the standard highway and additional K-bearing excursions.

Independent reconstruction: audits/check_n_marker_kernel_independent.py and audits/check_n_marker_kernel_independent.json. The checker verified all6,562 clauses and1,310 charged-site alignments using separately reconstructed literal geometry.

## Files and failed weaker attempt

- spatial_n_marker_separated_kernel.py/json: direct short-grammar certificate.
- spatial_n_marker_spacing_kernel.py/json: directly checks K spacing140 in the short bases; produces exactly the same certificate.
- spatial_n_marker_kernel.py/json: without the separation premise the candidate family shrinks to EMPTY. This is an inconclusive proof-method result, not a physical counterexample.
