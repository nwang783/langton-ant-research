# Exact three-read exit-coset blocks in the five-macro language

Status: analytic proof plus finite literal checker; independent audit requested. This refines the symbolic exit freshness proved by the global analysis in `../word_stabilization/check_exit_coset_fresh_global.py`. It is not physical freshness or finite fuel.

## Statement

In any concatenation of C,V,U,Q,B, let E be the coset of a non-C macro's first L read at its terminal exit cell. Within that concatenation, E is read exactly twice in that macro, with symbols L,R. If another macro follows, its phase3 reads E once more, with symbol L. No subsequent macro reads E. Thus the within-concatenation coset block is LR or LRL, and after the third read the physical exit cell is white.

All assertions are relative to the concatenation's initial group state. A finite earlier history outside the interval is not silently assumed absent. Arbitrary later behavior outside the five-macro interval is not covered by the last-read claim.

## Symbolic conventions and finite identities

Use G=<R,L | R^4=L^4=1>, right cosets of H=<R L^3>, with minimum-syllable canonical representatives. A reduced alternating word whose exponents all lie in {1,2} is canonical. Call such a word an S word.

Let F_A be the reduced full word of macro A. Each F_A is an S word beginning R and ending L; |F_A|>=2, where bars denote syllable length. Therefore all concatenated endpoint words are already reduced canonical S words, with no cancellation at seams.

The literal finite checker `certify_exit_coset_blocks.py` verifies these additional identities:

- For every macro, local read cosets at phases0,4 are the identity; phases1,2,3 are L,L^2,L^3; every other local read coset is an S word beginning R.
- For every non-C A, its exit representative E_A ends R^2 and F_A=E_A L.
- Within A, only its exit-first-L phase and its final-R phase have coset E_A.
- For each possible immediately following macro, phase3 is its only read of E_A after left multiplication by F_A.

The canonicalization algorithm repeatedly shortens a final exponent3 by multiplying by the appropriate generator of H. The exceptional singleton R^3/L^3 tie is represented by L^3. This is the already established exact canonicalization, not an empirical hash.

## Uniform loss bound

Let P be any nonempty concatenated endpoint prefix, hence an S word ending L. For any read coset c of the next macro, canonicalizing Pc loses at most TWO syllables from P.

If c is the identity there is no loss. If c begins R and has exponents1/2, Pc is already canonical. The remaining cases are c=L^j, j=1,2,3. Write P=P' R^a L^b with a,b in {1,2}. Multiplication can merge or cancel the final L syllable. If it creates a final L^3, the coset shortening removes that L syllable and reduces the preceding R exponent by one. At worst the R syllable also disappears. The earlier prefix P' is empty or ends in an exponent1/2, so there is no further shortening cascade. At most two syllables disappear.

This two-syllable bound is sharp for the suffix R L^2 followed by L. A one-syllable bound would be false.

## No later exit-coset read

Rebase at the selected non-C macro A. Its exit E_A has length |F_A|-1. The immediate-next-macro claim was checked literally above.

At the beginning of any macro after that immediate successor, the endpoint prefix includes F_A and at least one full F_B. Its length is at least |F_A|+2. The uniform loss bound makes every read there have canonical length at least |F_A|, strictly greater than |E_A|. Hence none can be E_A. This is an all-length argument, not a search cutoff.

Combined with the global analysis's symbolic freshness of E_A relative to earlier macros, the complete within-interval visit sequence is exactly LR or LRL.

## Causal meaning and remaining obstacle

The independently audited square-to-coset/no-A-B-A theorem now applies. A later physical reuse of this exit cell, if it occurs inside the concatenation, is necessarily in a different coset. The first such reuse after the LRL block must read R because the physical cell is white. A still later non-C terminal first-L at the same physical cell would therefore require an intervening different-coset R-producing block.

This exposes an inter-coset color-transfer requirement. It does not exclude it. The assigned autonomous coset coloring may have infinite black support, even for a finite or blank square seed, so symbolic freshness cannot be charged injectively to initial physical black cells without a further argument.
