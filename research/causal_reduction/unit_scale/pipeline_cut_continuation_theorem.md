# The exact disconnected pipeline cut follows H forever

23 October 2026, 14:48 UTC. Author exact proof and literal controls, independent review requested. This strengthens the former finite discovery trace without extending its scope. The entry field is a semi-infinite prepared field, not a finite seed. Earlier physical connectors or additional changes are not included.

Use the signed literal H/LR/Q words and headings N,E,S,W. For integers l>=-1 and 1<=t<=l+2, schedule in each integer period n the disconnected pieces

    H at (2l,10+2l,E)+n(2,2),
    LR at (-1+2t,6+2t,S)+n(2,2),
    Q at (0,0,E)+n(2,2),

in that order. This is the signed white-starting orbit-history relaxation, not a continuous ant path. Define its H-end cut at period0 by toggling the initially white field at all H reads with n<=0 and all LR/Q reads with n<0. Every individual cell receives finitely many such reads, so this defines a genuine infinite binary field without an infinite parity sum at a cell.

Starting at the period0 H endpoint (2l+2,2l+12,E), the actual ant follows H forever, with drift(2,2) per104 reads.

## Exact comparison with the standard H past

For a cell p set its full-drift orbit a=(p_x-p_y,p_x mod2) and longitudinal level k=floor(p_x/2). Let H0 denote H translated to (0,10,E), Q0 the stated Q at the origin, and R0 the two-read repair at(-1,6,S). A slot of level q in a piece placed at longitudinal offset z has a past copy with n<0 at p precisely when k<z+q. Its contribution to the cut field is therefore the indicator of that inequality, modulo2.

Compare the full cut with the simpler white field toggled only by H copies n<=0. Future H copies n>=1 visit, on any orbit a of H0, exactly the ray

    k >= l+1+min(levels of H0 on a).

Only three H0 orbits occur in Q0 or R0. The literal inventories are:

    a=(-8,1): H levels[1,1,1]; Q levels[0]; no repair slot.
    a=(-7,0): H levels[2]; Q levels[0,1]; no repair slot.
    a=(-7,1): H levels[1]; Q levels[0,0]; repair level[-1].

Thus the EXTRA past LR/Q field is, on these respective orbits:

    1 if k<=-1;
    1 if k=0;
    1 if k<=t-2.

All other H orbits have zero extra field. The three future H rays begin at l+2, l+3 and l+2, respectively. Since l>=-1 and t<=l+2, each extra field lies strictly behind its future H ray. Therefore the two cut fields agree on EVERY future H read, not merely a finite prefix. The literal standard H orbit histories start R and alternate; the H-only cut consequently realizes every future H copy. Equality on that complete support proves the result by deterministic induction.

The cancellation of the two Q slots on orbit(-7,1) is essential: this is comparison of COMPLETE fields, not an assertion that all earlier reads miss the future geometrically. No infinite-field finiteness is inferred.

## A stronger universal endpoint-memory corollary

Independently of the prepared cut, ANY single completed literal H fixes the current colors at every cell it read. Starting at its endpoint, these alone force exactly the next13 turns

    LRLLRRRRLLRLL.

Their movements are N,E,N,W,N,E,S,W,S,E,S,E,N. They end at endpoint+(2,1), incoming N. That next cell was not read by H or by the forced13 reads, so its color is genuinely unconstrained if the outside board is free. This is a maximal forced prefix from the last H read set alone, not an assumed standard continuation.

For the pipeline connector target endpoint+(2u-3,2u-6), incoming S, u=t-l<=2, any connector length has form n=4k+3. The forced prefix contains four north moves. To achieve vertical displacement2u-6 therefore requires at least10-2u south moves and14-2u vertical moves total. Consequently

    n >= 27-4u = (11-4u)+16.

This replaces the earlier eight-read surcharge by a sixteen-read surcharge. Equality is kinematically possible after the fixed13 reads: use7-2u remaining south moves, one remaining east move and6-2u remaining west moves, alternating horizontal/vertical and ending south. No color realizability is asserted at equality.

The exact-cut theorem says no spontaneous connector exists on that ONE complete inherited field, at any length or compatible phase. A putative continuous assembly may have extra field changes from its earlier connectors, so it is NOT excluded. In particular neither this result nor the surcharge is a general obstruction to all H/LR/Q splicing or to nonstandard prepared fronts.
