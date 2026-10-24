# Exact interval coverage deficiency and the strengthened preparation coefficient

23 October2026. Analytic lemma and focused helper submitted for independent
review. The signed generic criterion/lift remain unchanged. No word search.

## 1. Supplied bulk profile

Use one complete diagonal supplied-consumer instance from the independently
signed generic criterion. In its common physical period Q=P^q let b be the
number of required-black full-drift classes. Every class has one integer
normal coordinate. The finite anchored standard-rail list is complete for
rails contributing at least one required-black class.

Delete all candidates that paint a consumer-required-white class black.
For every remaining candidate i, let I_i be its CLOSED standard read band and
C_i its set of required-black classes painted black. Every class in C_i has
normal coordinate in I_i.

Compatible mature white-input writer bands are disjoint, including endpoints.
Consequently compatible candidates have DISJOINT cover sets C_i: one physical
normal cannot lie in two disjoint intervals. Therefore maximum possible
required-black coverage is exactly

    W=max sum_i |C_i| over pairwise disjoint selected I_i.

This is ordinary weighted interval scheduling, not arbitrary interval set
cover. Sort by right endpoint; if p(i) is the last previous band ending strictly
before I_i starts, the exact recurrence is

    best(i)=max(best(i-1), |C_i|+best(p(i))).

Set delta=b-W. The empty bundle is included. Full bulk compatibility is
EQUIVALENT to delta=0. For delta>0 every compatible white-clean bundle leaves
at least delta required-black classes unpainted.

The deficit is exact for this stated relaxed coverage optimization. It is not
asserted to equal minimal realizable initial fuel: an unpainted required-black
class might lie in a writer band whose output is white, making that partial
bundle outright illegal rather than repairable with initial black. Such cases
only strengthen the NECESSARY fuel inequality below; no attainability is claimed.

## 2. Quantitative physical lift

Keep the already signed common-period boundary constants:

    G=floor(n/q)-W_Q-L-c_parallel*F_parallel-c_perp*F_perp.

There are at least G good common PHYSICAL levels before a supplied P^n consumer.
At each good level, every active parallel writer band is complete or absent,
all cap/nonparallel repair witnesses are protected, and first-R black
persistence makes active writer bands compatible. Consumer legality excludes
white-polluting candidates. Thus their required-black coverage is at most W.

At least delta required-black classes remain. If any were written white by an
active standard band the actual consumer would already be illegal. Otherwise
their cells were untouched and must be distinct initially black cells. Distinct
classes at one level and distinct common levels represent distinct physical
cells; no multiplicity factor is hidden. Hence every legal preparation obeys

    |B| >= delta*G.

Negative right sides are simply vacuous. The loss constants are deliberately
multiplied as whole discarded levels; sharper per-class boundary counting is
not asserted. Arbitrary cyclic standard phases retain the signed extra104 cap
reads per flight reduction.

For prepared108, delta=11. For the separate forward108 fresh origin/E instance,
delta=3. Both have q=1,W_Q=2,c_parallel=6,c_perp=1408, giving respectively

    |B| >= 11*(n-2-L-6F_parallel-1408F_perp),
    |B| >=  3*(n-2-L-6F_parallel-1408F_perp).

These strengthen only the same supplied architecture; they do not imply a
uniform global scattering budget or exclude general nonstandard preparation.

## 3. Executed helper and controls

`bulk_black_deficiency.py` does NOT modify the signed generic source. It accepts
that source's finite profile data, validates that each covered black class is
physically inside its band, computes the interval optimum and emits the
selected-band witness plus all dynamic-programming values. It verifies that
delta=0 agrees with the independently signed selector decision.

The geometric mask condition is ESSENTIAL. An arbitrary abstract cover bit
cannot be repeated in two disjoint bands and then counted twice. The helper
rejects such unphysical input rather than misusing interval scheduling as a
general set-cover algorithm.

`check_bulk_black_deficiency.py` compares36 retained supplied profile/rotation
instances and500 separate physical point/interval instances against exhaustive
subset UNION maximization. It includes empty and positive-coverage cases,
endpoint clashes, repeated normal coordinates, white pollution and explicit
unphysical-mask rejection. These are author controls; independent implementation
audit is separate. No new consumers, periods or caps were enumerated.
