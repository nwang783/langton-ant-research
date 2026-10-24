# The endpoint-only positive cancellation-height relaxation is vacuous

The construction was independently reviewed by the auditor on 2026-10-22 at 18:28 UTC; the explicit proof is given below. This is a limitation theorem for a relaxation, not a theorem about realizable ant histories.

Let epsilon(x,y)=(-1)^(x+y+1). A valid signed binary field is rho(x,y)=epsilon(x,y) B(x,y), with B in {0,1} of finite support. Write

    (Delta K)(x,y)=K(x,y)-K(x-1,y)-K(x,y-1)+K(x-1,y-1).

## Theorem

For EVERY finitely supported integer field D on Z^2, there exist a finitely supported, pointwise nonnegative integer K and a finite signed binary field rho such that

    rho = D + Delta K.

Moreover, rho can be chosen with at most 17 ||D||_1 black cells. The analogous statement holds after reversing the checkerboard convention.

Consequently, the exact ant identity rho_t=rho_0+D(r_t)+Delta K_t, considered only at its final endpoint, with rho_0=0 and K_t>=0, imposes NO restriction on the possible finite integer deposit field D(r_t). It cannot by itself distinguish even arbitrary reduced words from realizable histories. Temporal compatibility, including all intermediate binary fields and legal ant motions, is indispensable.

## Proof: first match row and column sums

Write D as a sum of n=||D||_1 signed unit atoms s delta_(x0,y0), where s is +1 or -1. We will replace each atom by either three or five distinct allowed-sign cells. Every new row and column is chosen fresh globally and outside the finite sets of original D rows and columns. Thus cells used by different atom replacements never overlap.

If s is OPPOSITE epsilon(x0,y0), choose a fresh column c with parity opposite x0 and a fresh row r with parity opposite y0. Put the following three signed entries into rho:

    (c,y0): s,  (c,r): -s,  (x0,r): s.

All signs equal epsilon at their cells. The intermediate row r and column c each have sum0. The only nonzero row/column contributions are s in original row y0 and original column x0, exactly those of the atom.

If s EQUALS epsilon(x0,y0), choose fresh columns c1,c2 with parity respectively x0 and x0+1, and fresh rows r1,r2 with parity respectively y0+1 and y0. Put:

    (c1,y0): s,
    (c1,r1): -s,
    (c2,r1): s,
    (c2,r2): -s,
    (x0,r2): s.

Again every sign equals epsilon. Each intermediate row/column sums to0, and the original row and column each receive s.

Summing these disjoint replacements gives a signed binary field rho with the same sum as D on EVERY individual row and column. It uses at most5n cells.

## Proof: integrate the zero-margin difference

Set F=rho-D and define

    K0(x,y) = sum_{i<=x, j<=y} F(i,j).

All row and column sums of F are0, so K0 has finite support. It is integer-valued and Delta K0=F. It may take negative values.

Let N=max(0,-min K0). Since F has total sum0 and ||F||_1 <=6n, every partial sum has absolute value at most3n. Hence N<=3n.

## Proof: raise the height without violating binary colors

Choose N distinct, sufficiently large integers M. For each, add the unit plateau

    P_M(x,y)=1 on [-M,M] x [-M-1,M+1], and0 elsewhere.

Choose every rectangle to contain supp K0 and supp rho strictly inside, and choose distinct increasing M so their four corner cells below are all different.

Its mixed difference Delta P_M is supported at four cells:

    (-M,-M-1): +1,
    (M+1,-M-1): -1,
    (-M,M+2): -1,
    (M+1,M+2): +1.

Each displayed sign equals epsilon at that cell. The corners lie outside supp rho, and corners from distinct plateaus do not overlap. Thus

    K = K0 + sum_M P_M,
    rho_new = rho + sum_M Delta P_M

satisfy rho_new=D+Delta K. On supp K0, every plateau contributes1, so K>=0; outside it, all contributions are nonnegative. The new field remains signed binary. Its black mass is at most5n+4N<=17n. This proves the theorem.

## Small exact control

For start (0,0,N), r=RRRLRRR has c(r)=5. Its ordinary per-cell deposit v counts R as+1 and L as-1, and D=epsilon v. With B0 empty, take K=1 on the five plaquettes with lower-left corners

    (0,-1),(0,0),(0,1),(1,-1),(2,-1),

and0 elsewhere. Odd-parity plaquettes add1 to their four ordinary black bits, even-parity plaquettes subtract1. The resulting formal black set is

    {(-1,-2),(-1,-1),(0,-2),(0,0),(0,2),
     (1,-1),(1,2),(3,-1),(3,0)}.

All other formal black bits are0. The auditor independently verified this arithmetic in ../audits/static_curvature_relaxation_counterexample.json. No actual blank-ant history with this reduced word is asserted.

## Important limitation of the conclusion

The theorem does not discard the all-history height representation. Its monotone chronology and exact coupling to the live ant can carry decisive information. It only shows that projecting away chronology and retaining one final nonnegative K and binary rho loses all finite-deposit discrimination. The explicitly constructed plateaus are algebraic scaffolding, not certified sequences of legal ant cancellations.

## Monotonicity alone also does not repair the relaxation

For any sequence of finite integer deposits D_t, one can inductively maintain finite binary rho_t and pointwise nondecreasing K_t satisfying rho_t=D_t+Delta K_t. Given rho_(t-1), apply the theorem to E_t=rho_(t-1)+D_t-D_(t-1), obtaining rho_t=E_t+Delta J_t with J_t>=0; then set K_t=K_(t-1)+J_t. This works over every finite horizon and, inductively, over a countable sequence, with each time slice finitely supported.

This corollary allows arbitrary multi-plaquette jumps. It does NOT respect the exact single-cancellation increment rate, its prescribed physical location, or ant trajectory causality. Those are the indispensable constraints. The adjective “monotone” alone therefore does not make the endpoint relaxation informative.
