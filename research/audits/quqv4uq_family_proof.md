# Exact unbalanced mixed-fold family

Status: exact all-parameter certificate by the independent-audit analysis,
independently reviewed by the word-stabilization analysis. It is a negative
control for proposed mixed-fold obstructions, not a highway counterexample.

For the established before-marker macros Q,U,V, the finite word

    Q U^n Q V^4 U^n Q

is physically feasible exactly for integer n>=3. Its minimal finite entry
black set has10n+57 cells; its length is56n+264 updates and its endpoint is
(0,8,S), starting at(0,0,N).

## Exact chronology proof

Literal Q,U,V words are read from the already used macro source, whose
SHA256 is02646581d58b0072a245ca3f57edab2a69174dc670ce616ce2466dc10a0a0557.
The verifier recomputes all turn geometry rather than using saved traces.
There are six chronological segments: Q, U^n, Q, V^4, U^n, Q.
Both U repetitions have zero horizontal displacement and vertical drift
of magnitude4, with opposite signs. Every read family therefore has a
constant physical x coordinate, a fixed y residue r modulo4, and an integer
rank l=(y-r)/4 ranging over an affine interval [a*n+b,c*n+d).
Fixed-word read occurrences are singleton intervals of length1.

For each (x,r), collect every interval endpoint. An integer strictly above
every crossing of two distinct affine endpoint functions is computable by
integer division. Here n>=4 suffices. The verifier sorts endpoints at n=4
and checks that each adjacent difference has nonnegative slope and strictly
positive value there. Their order is therefore proved constant for ALL
n>=4. Every adjacent endpoint slab has a fixed set of active read families.

Chronology between different segments is fixed. Within either U segment,
the repetition index of a read at rank l is +/- (l-a*n-b). Differences
between two indices lose both l and n; the verifier asserts this and sorts
by that exact difference, then by literal phase. Within a fixed segment,
literal phases suffice. Thus each of182 slabs has a complete, parameter-
independent chronological list of R/L reads for every physical cell in it.
Every such list alternates. Assign initial black exactly when its first
letter is L. This realizes the whole word by induction on its reads, and
is minimal because every first-L cell must initially be black.

The number of cells in each first-L slab is the difference of its two
endpoint functions. Summing these disjoint intervals gives10n+57 exactly.
The checker also derives the constant endpoint and update count. Literal
first-read checks at n=0,1,2 fail respectively by R/R at times46/122 at(-1,-1),
L/L at3/175 at(0,-1), and R/R at8/232 at(2,0). At n=3 the complete literal
chronology is feasible with87 initial black cells. These four cases finish
the theorem; they are not used to extrapolate the infinite parameter range.

## Scope

The outward run has U-count n and V-count0; the return run has U-count n
and V-count4. Therefore even strict componentwise domination of return
Parikh counts does not force a three-fold conflict. The balanced-return
obstruction remains valid and is not contradicted. Entry fuel grows with n,
and nothing here constructs an infinite trajectory from one finite seed.

Artifacts: certify_quqv4uq_family.py and quqv4uq_family_certificate.json.
