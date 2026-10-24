# Conditional quantitative assembly for the canonical DCUV record weights

**This is not yet a DCUV exclusion theorem.** As of 2026-10-23 04:59 UTC,
eleven of the thirteen strict unfunded-record event types are independently
signed. V phase1 and U phase1 remain open. The following assembly applies only
after all thirteen are proved, possibly at different finite activation weights.

Take the maximum of those finitely many weights, denoted I, with I>=28. A record
unfunded at this larger weight is also unfunded at every smaller certificate
weight, so all per-case exclusions remain applicable. This is a logical
monotonicity statement, not an alteration of any frozen model.

At a marked boundary the board is the five-cell core, disjoint from a residual
identity set X. There are m-5 initial residual identities. Each is consumed at
most once. For each rotated diagonal L_r, record every core and newly created
output value immediately, and every first consumption of an initial identity
with value I+2L_r(q). Complete event coverage says that a created value can never
strictly increase this history without a previous or simultaneous activation.
A first-consumption activation exceeds the entering core by at most I+6, since
max over all packet input offsets and headings of 2L(input)-A_heading is6.
Thus each directional historical maximum is at most
A_r+(I+6)(m-5), relative to the initial head.

For every literal read offset u in any retained packet and heading h,
2L_h(u)-A_h<=14. This is the **shifted** prefix bound. The unshifted absolute
prefix diagonal radius is8, but subtracting the heading core offset is essential
and improves the combined bound. Since max A_r=22, every actual read satisfies
|x+y|,|x-y| <= 18+(I+6)(m-5)/2. In particular its two Cartesian coordinates
are bounded in absolute value by
R=ceil(18+(I+6)(m-5)/2).

Only cells in that square can change. The total black count is at most
m+(2R+1)^2. Every C macro increases mass by3, and each V or U macro by4;
D preserves mass. Hence the count t of non-D macros is at most
floor((2R+1)^2/3). Every maximal D run has at most2R packets, since D translates
the head by a fixed diagonal unit step without changing heading. The internal
macro boundaries are literal reads, and the final packet endpoint is bounded
by the core history, so terminal runs are covered as well. There are at most
t+1 D runs. The exact raw lengths are10,15,18,28 for D,C,V,U, respectively.
Therefore the raw duration is at most
20R(t+1)+28t.

This would be a mass-only cubic bound for finite complete recurrent-eight
factors, and would exclude an infinite finite-support DCUV tail after the signed
boundary restart. It would still not settle arbitrary seven-word tails or the
universal standard-highway conjecture.

The local arithmetic is replayed by `check_dcuv_record_conditional_constants.py`
and saved in `record_conditional_constants.json`. The hypothetical example I=48
gives R=18+27(m-5), but48 has not been established as sufficient for the two
remaining event types.
