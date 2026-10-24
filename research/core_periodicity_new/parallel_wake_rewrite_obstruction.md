# Reciprocal wake energy excludes clean parallel rewriting

Status: Sections1–4 passed independent analytic audit on 2026-10-22 at 23:30 UTC, including the same-full-drift lift and normalized finite-family corollary. This is a consequence of the already audited signed two-boundary clock inequalities, not a proof of global stabilization.

## 1. Exact scope and moments

Fix a nonzero non-axis full drift d with even checker parity and one ant sector sigma. All incoming and outgoing profiles in this note are finite sets of classes in the SAME quotient Z^2 / <d>. In particular, if d is k times a basic wake period, each basic profile class contributes k distinct full-drift classes.

Choose the primitive integral normal eta to d and r=4, after a quarter rotation putting both components of eta positive. Write chi(q)=(-1)^(q_x+q_y) and

    E_+(A) = -sigma sum_[q] in A chi(q) r^(eta dot q),
    E_-(A) = -sigma sum_[q] in A chi(q) r^(-eta dot q).

The moments are independent of class representatives. They are signed quantities; positivity must not be assumed for an arbitrary installed profile.

A translating periodic front on incoming profile I with outgoing profile O is understood exactly as in two_boundary_front_synthesis.md: it is realized on the bilateral input background with a finite cap modification, has nonzero full displacement d, restores its heading, and changes the stable incoming profile to O on the region it passes. Arbitrary unread background behind the front need not be erased.

The strict one-sided clock inequalities give

    E_+(O) - E_+(I) > 0,
    E_-(O) - E_-(I) > 0.

These inequalities hold for every possible raw word and period. They do not depend on a particular consumer word. Finite moving caps cancel from the per-period stable-class calculation.

Assume E_+(I)>0 and E_-(I)>0. This is automatic if I is itself a same-sector completed wake of a nonzero translating white-input front, when its profile is counted in this full-drift quotient. For a longer compatible full drift, both moments are multiplied by the same positive integer.

Consequently every such consumer must satisfy

    E_+(O) E_-(O) > E_+(I) E_-(I).

The output moments are positive because each is strictly larger than the corresponding positive input moment.

## 2. Translation and half-turn invariance of the product

For a lattice translation s, put epsilon=chi(s) and z=eta dot s. Then

    E_+(A+s) = epsilon r^z E_+(A),
    E_-(A+s) = epsilon r^(-z) E_-(A).

Hence the product is unchanged. For a half-turn followed by translation,

    E_+(s-A) = epsilon r^z E_-(A),
    E_-(s-A) = epsilon r^(-z) E_+(A),

so again the product is unchanged. These are algebraic profile identities in the fixed sector. If epsilon=-1, both transformed moments are negative, which already contradicts the necessary output positivity.

THEOREM. If I has two positive reciprocal moments, no finite-cap translating periodic front with nonzero non-axis drift can have outgoing profile O equal to a translate or translated half-turn of I, provided both are profiles in the same full-drift quotient.

Proof. Such an O has the same reciprocal-moment product as I. A feasible consumer would have a strictly larger product by Section1. Contradiction.

The theorem includes longitudinal translates (which may leave I unchanged) as well as transverse shifts. It does not require the candidate period to equal the producer's period. It also does not assume that the consumer itself has positive net black-mass growth.

## 3. Application to the standard104 wake

Use the canonical twelve-class completed standard wake T pinned in two_boundary_front_synthesis.md and standard_block_union_history.md. Its basic translation is (2,2), up to rotation and sign. For every full drift d=plus or minus k(2,2), k>=1, lift T to its 12k full-drift classes. Its same-sector moments are both positive because it is the wake of the ordinary white-input standard front.

No exact periodic finite-cap consumer can transform that incoming bilateral standard wake into a shifted or half-turned copy of one standard wake, with any parallel nonzero drift and any raw period. This is an ALL-PERIOD clean single-wake rewrite exclusion.

The earlier pure-erasure exclusion is complementary: O=empty has both output moments zero and is also impossible. The new theorem additionally excludes retaining exactly one congruent parallel standard wake as output.

Important limits:

- A consumer emitting a different profile is not excluded.
- Multiple outgoing rails or distributed extra wake classes can increase the product.
- Opposite-sector time reversal is not covered by the same-sector positivity assumption.
- An arbitrary nonperiodic finite-seed trajectory need not admit the stipulated incoming/outgoing front decomposition.
- This is not a classification of arbitrary finite caps on a standard wake.

## 4. Finite profile families cannot form a clean rewrite cycle

For any finite family of same-sector positive-moment profiles with a common basic non-axis period, take products normalized to that basic quotient. Allow arbitrary translations and half-turns of family members and arbitrary compatible full-period multiples. Every exact finite-cap periodic rewrite strictly increases the normalized product. Therefore there is no cycle of such rewrites, and no infinite chain staying in that finite profile family.

This finite-family statement is only about the stipulated sequence of exact periodic profile-to-profile transformations. It gives no bound when profile shape or transverse extent is unbounded, and it must not be substituted for a decomposition theorem for arbitrary ant dynamics.

## 5. Nonperiodic finite rewrites with bounded signed endcap error

This strengthening passed independent analytic audit on2026-10-22 at23:34 UTC. It removes periodicity of the rewriting schedule, but replaces it with an explicit complete endpoint-field hypothesis.

Fix profiles I,O and full drift d as above, and assume that at least one reciprocal moment difference is nonpositive. For instance this holds when I has two positive moments and O is a translate or translated half-turn of I. Choose representatives for the profile classes and define finite segments

    I_N = {q+j*d : [q] in I, 0<=j<N},
    O_N = {q+j*d : [q] in O, 0<=j<N}.

The representatives may incorporate fixed longitudinal offsets. Suppose one ACTUAL uninterrupted trajectory interval, of duration t, has the exact signed endpoint-board change

    1_(B_t) - 1_(B_0) = 1_(O_N) - 1_(I_N) + e,              (12)

where e is a finitely supported integer-valued error with sum_q |e(q)|<=K. Suppose all cells in I_N, O_N, supp(e), and both endpoint head positions lie in one fixed transverse strip

    L <= eta dot q <= U.                                    (13)

The initial board may otherwise be arbitrary, even infinite. It is only the COMPLETE signed endpoint change that is prescribed. Unchanged archival working memory cancels exactly; any other surviving change must be included in e.

Then, with r=4 and kappa as in the source clock,

    t <= (K+4) r^(U-L) / kappa.                             (14)

This bound is independent of N and of the longitudinal separation of the endpoint caps.

Proof. First take the positive reciprocal if E_+(O)-E_+(I)<=0. By(12), the board part of the one-sided clock increment is

    N[E_+(O)-E_+(I)] - sigma sum_q chi(q)e(q)r^(eta dot q)
       <= K r^U.

The source head coefficients are

    gamma_N=2/(b+1), gamma_E=2/(a+1),
    gamma_S=-2b/(b+1), gamma_W=-2a/(a+1),

with a=r^eta_x and b=r^eta_y. Each has absolute value less than2, so the endpoint head correction is less than4r^U.

The support of the complete XOR is contained in the union of the three supports in(12). The audited open-interval hull identity

    conv({p_0,...,p_t})
      = conv((B_0 symmetric_difference B_t) union {p_0,p_t})

therefore confines every read to the strip(13). Every literal update increases the chosen clock by at least kappa*r^L. Summing gives(14). If instead the negative reciprocal difference is nonpositive, apply the same argument to the normal coordinate -eta dot q, whose strip is[-U,-L]. The ratio of maximum to minimum weight is again r^(U-L).

For infinite backgrounds, copy the entry colors on the finite read set into a finite board. The physical interval and complete signed board change remain identical, so the same proof applies.

Consequences and limits. There is no family of arbitrarily long actual clean single-wake rewrites with uniformly bounded signed endcap error K and fixed transverse strip, even if their internal schedules and cap states change nonperiodically. This applies in particular to rewriting a same-sector standard wake into a fixed shifted or half-turned parallel copy. It does not cover transverse shifts growing with N, unbounded distributed output corrections, or different output profiles with both moments increasing. The conclusion is a DURATION bound: N alone need not measure work when the formal input/output segments cancel.
