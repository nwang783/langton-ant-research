# A four-black-cell static chain survives all exponential clock tests

Status: independently approved algebraic negative control (2026-10-22 at23:27 UTC) extending an already archived four-corner example to the full non-axis exponential-clock cone. The bare mass-four architecture is DYNAMICALLY EXCLUDED by the audited eventual-mass-at-least-five theorem. These states are NOT asserted to lie on one ant orbit. In particular this is not a nonstandard finite-seed construction.

Prior sources: ../continuation_2026-10-22/ant_continuation2/chronology/eventual_mass_five.md and mass_bound_extension_limits.md. The latter already gives a fixed-cap-plus-four-corners countermodel for the diagonal clocks and charges. The product calculation here merely makes the full exponential-cone compatibility explicit.

Keep the physical pose fixed at(0,0,N), hence sector sigma=+1. For n>=1 let B_n consist of the four corners of the rectangle

    [-n,n+1] x [-n-1,n].

Its side lengths2n+1 are odd and its lower-left checker parity is odd. Every B_n has exactly four black cells.

## Conserved cut charges agree

Each occupied physical row has two corners with opposite checker parity, so its alternating black sum is zero. The same holds in each occupied column. Thus all alternating row/column sums vanish as integer arrays, not merely modulo4. With the identical pose, all conserved mod4 cut-charge arrays agree for every n.

## Every non-axis exponential field clock increases

For a,b>1, the signed board term of the northeast clock is

    F_n(a,b)=-sum_(x,y in B_n) (-1)^(x+y) a^x b^y
            =(a^(n+1)-a^-n)(b^n-b^(-n-1)).

Both factors are positive and strictly increase with n. For any other open quadrant, rotate the clock and use its rotated sector. The corresponding board term is again a product of two positive increasing factors of the forms

    a^(n+1)-a^-n,     a^n-a^(-n-1),

and the analogous b factors. Consequently the board part of EVERY one-sided exponential clock in the four non-axis quadrants strictly increases along this sequence, whenever that clock's parameter condition gives nonnegative physical increments.

The head correction is unchanged because the pose is fixed. Positive sums of these clocks also increase. Subtracting a constant multiple of black mass changes nothing, since mass is always four. In particular all four critical diagonal clocks, their translated integer combinations, and the inherited strict non-axis exponential clocks are compatible with B_n -> B_(n+1).

## Other elementary endpoint tests do not reject the chain

The complete difference B_n XOR B_(n+1) consists of eight rectangle corners. Its convex hull contains the fixed head and expands. Hence the closed-pose hull condition is satisfied. Its diameter grows, so the compact-export bound does not make return durations uniformly bounded. The one-sided-controller obstruction does not apply because the difference surrounds the head.

This explicitly shows why bounded BLACK MASS ONLY AT CHECKPOINTS, conserved cut charges, and the entire exponential-clock cone do not by themselves exclude distributed growing hardware. Bounded mass along the full physical orbit is a different hypothesis and is already excluded. The four-cell version itself has no infinite real implementation, by the stronger dynamical theorem just cited. Adding a fixed finite cap preserves every moment difference and every equality of charge arrays across n; that higher-mass distributed version is not excluded by the mass-four theorem. Any real implementation would have to create and erase all intervening working material; none is known.
