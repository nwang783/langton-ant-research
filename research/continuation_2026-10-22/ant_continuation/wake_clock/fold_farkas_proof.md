# Exact infeasibility of the ordinary 3-by-3 context-wise energy rank

Date: 21 October 2026.

Status: exact integer Farkas certificate, independently verified. This is
a restriction on the specified rank ansatz, not on all possible proof
methods and not a physical counterexample to the highway conjecture.

## 1 The ansatz being tested

Give every nonzero 3-by-3 binary pattern a nonnegative weight, invariant
under quarter-turn rotation. There are 139 such pattern classes. The
all-white pattern has weight zero. For a finite black field B, sum these
weights over all translated 3-by-3 windows to obtain E_w(B).

Add an arbitrary real potential phi on the 995 ports in
`factor_language/conditioned_macro_contexts.json`. For every listed
history-conditioned edge e from s to t, require

    E_w(after)-E_w(before)+phi(t)-phi(s) <= -c_e

for every exterior assignment allowed by that edge's local context.

The weakest target initially audited here is fold-only cost:
c_e=1 for macros C,Q,B and c_e=0 for U,V. A second target, requested during
the audit, is J-only cost: c_e=1 for V,Q and zero for the other macros.

The existing cut collection contains 34,941 explicit inequalities. No new
contexts, outside assignments, trajectories, or seeds were generated in
this audit.

## 2 Exact certificate

Write one inequality as

    a_e dot w + phi(t_e)-phi(s_e) <= -c_e.

The saved certificate assigns positive integer multipliers lambda_e to
159 of the existing cuts and zero to every other cut. These supported
cuts involve 109 graph edges, 71 local contexts, and 86 ports. Direct
integer verification establishes:

1. Every multiplier is nonnegative.
2. Every one of the 995 potential columns sums to zero.
3. Every one of the 139 aggregate energy coefficients
   A_j=sum_e lambda_e*a_(e,j) is nonnegative; 66 are strictly positive.
4. The weighted fold cost is the positive integer

       C_fold=4180793699792737832807650877360807723851.

Multiplying the asserted inequalities by lambda_e and adding them gives

    A dot w <= -C_fold.

The left side is nonnegative because both A and w are componentwise
nonnegative. The right side is negative. This is a contradiction.

Therefore no real nonnegative ordinary C4-invariant 3-by-3 pattern weights
and no real port potential satisfy the fold-only constraints. The result
does not depend on floating numerical tolerances, a bound on the weights,
or a chosen gauge for the potential.

## 3 The same witness also excludes J-only and all-macro costs

The same integer multipliers have positive total weight on every one of
the five macro types U,V,B,C,Q. In particular,

    C_J=4507001484264218697569420166724368040022 > 0

for the J-only target. All-macro cost gives the positive multiplier sum

    C_all=11039569244127093338379771101052963592565.

The potential cancellation and energy coefficients do not depend on the
chosen costs. The same contradiction therefore excludes both targets.
More generally, it excludes any nonzero nonnegative cost vector assigned
by macro type, while requiring the other macro types to be nonincreasing.

This extension required no additional dual optimization. The independent
verifier computes the five exact macro totals directly from the witness.

## 4 Construction and independent verification

The discovery program reconstructed the supplied inequalities and solved
a dual LP with nonnegative multipliers, exact target form, and a fold-cost
normalization. The floating solution selected 159 supported cuts. Simple
bounded-denominator rounding was insufficient, so its active basis was
reconstructed using fraction-free integer Gaussian elimination on 160
equations. The resulting rational solution was scaled to primitive positive
integers and checked exactly.

The independent verifier imports neither the optimizer nor the context
energy-row routine. For every supported cut it:

- checks the original cut index, edge identity, and source-file hashes;
- verifies that the chosen exterior black cells lie in the permitted free
  cells and do not contradict the fixed black/white context;
- reconstructs all affected 3-by-3 windows directly from cell sets;
- computes each rotation class and exact before/after pattern count;
- checks the supplied row coefficients and all weighted sums using
  arbitrary-precision integers.

The verifier uses only Python's standard library. Its output records
exact zero potential balance, nonnegative energy coefficients, positive
fold and J costs, and the certificate hash. The largest multiplier has
40 decimal digits; none is rounded.

## 5 Scope

The certificate excludes the ordinary translation-invariant, quarter-turn
invariant, nonnegative 3-by-3 energy plus the specified port potential when
the inequality must hold for every permitted outside assignment at each
listed context.

It does not exclude a sector-dependent energy, a larger pattern radius,
a nonlocal functional, a richer history state, or a proof that restricts
which listed contexts can actually occur in one global orbit. The witness
combines different local outside assignments; it is not asserted to be a
single physical trajectory or a counterexample to the highway conjecture.

A targeted reuse check evaluates the same 159 multipliers on the 271
sector-dependent pattern columns. It gives 104 negative columns, 162
positive columns, and five zero columns. Therefore this particular witness
does not extend to the sector-dependent ansatz. That result is saved in
`fold_farkas_sector_reuse_check.json`; it is not an exact sector-infeasibility
certificate and did not require a new dual search.

## 6 Files and reproduction

- `fold_farkas.py`: discovery and exact rational basis reconstruction.
- `fold_farkas_certificate.json`: all 159 integer multipliers, exact cuts,
  local row coefficients, aggregate energy coefficients, and source hashes.
- `verify_fold_farkas.py`: independent integer-only verification.
- `fold_farkas_verification.json`: compact exact verification outcome.

The source context and cut files are

    ../factor_language/conditioned_macro_contexts.json
    ../global_structure/conditioned_rank_cuts.json.gz

To verify the mathematical certificate, run

    python3 verify_fold_farkas.py

Re-running the floating discovery program is unnecessary for verification.
