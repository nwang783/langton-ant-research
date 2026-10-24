# No finite-seed pure inflation at temporal scales up to six

Status: independently audited analytic reduction and complete image enumeration,
22 October2026; see audits/check_pure_small_inflation_independent.py and JSON.
No finite-state assumption is made.

Let a legal finite-black-seed ant trace be normalized to p(0)=0, h(0)=N.
There are no Gaussian a with |a|>1 and integers2<=k<=6 such that, for EVERY
n>=0,

    p(k*n)=a*p(n),   h(k*n)=h(n).

Here multiplication uses ordinary complex coordinates with east1 and north i.
This does not exclude affine corrections depending on state, eventual rather
than from-origin inflation, larger k, or arbitrary sublinear ant behavior.

Proof. The k-letter block beginning at time k*n must have the same total
quarter-turn as the coarse turn c(n), so k is odd. In its own incoming frame,
it has displacement a for coarse R and -a for coarse L. Both types occur in
any infinite legal ant word: four consecutive equal turns return to the same
cell, so a fifth equal turn would violate alternation.

A macro with an internal consecutive-equal-read failure is impossible on any
background. Enumerate all internally valid binary words of length3 or5 and
pair their opposite-quarter-turn endpoint geometries. This leaves exactly:

 k3: a=2-i, 2+i.
 k5: a=-1-2i, -1+2i, 1-2i, 1+2i, 3-2i, 3, 3+2i.

Except for the two explicitly handled scales below, EVERY eligible R-image
has signed excess at most1 and EVERY eligible L-image at most-1. This holds
even when the image choice changes arbitrarily at every occurrence, with
unbounded memory. Therefore signed turn excess satisfies E(k*N)<=E(N) for
all N. In particular E(k^j)<=E(1)<=1. The black mass at these times is at most
|B_0|+1, while p(k^j)=a^j*p(1) escapes to infinity. The audited midpoint
inequality gives a contradiction.

For k5,a=-1+2i, the only R-image is LRLRR, beginning L, and the only L-image
is RRLRR, beginning R. Neither can be the first macro: its first fine turn
must equal its own coarse type c(0). Thus this scale fails immediately.

For k5,a=1+2i, the complete image sets are

 R: A=RLLRR or B=LRRLR;
 L: C=RRRLR or D=LLLRR.

The first macro must A or D, by its first-letter consistency. In either case
the coarse turn at time1 is L, so the second macro must C or D. All four
possibilities AC,AD,DC,DD have an equal consecutive reread. The literal
checker records the two times and cell for each, at no later than time8.
There is no choice of initial coloring that realizes even these two macros.

These cases exhaust k3 and k5, and the parity argument covers k2,k4,k6. QED.

The statement is broader than a two-letter substitution exclusion: the macro
at an occurrence of R/L need not equal the macro at any other occurrence.
Only the pure position and heading scaling identities are assumed.

Certificates: `free_inflations_k3.json`, `free_inflations_k5.json`, generated
by `search_free_inflations.py`; `free_five_inflation_any.json` records all four
exceptional two-macro contradictions. The separate k7/k9 searches have capped
branches and are NOT part of this theorem.
