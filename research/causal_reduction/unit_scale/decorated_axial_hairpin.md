# An axial decorated hairpin and a full-row transfer

23 October 2026, 06:10 UTC. Independently signed all-r history proof and separate
Presburger verification. This is a prepared local component,
not a finite-seed root, a renewable device, or a counterexample.

Put U=RRLRRRRL, V=LLRLLRLL, q=(2,0), with incoming north and central turn R.
U preserves N and moves q. V preserves E and moves -q. For r>=1 put

    W_r=U^r R V^r.

It starts at(0,0,N), ends at(1,0,E), and has length16r+1. The recursive label
b of physical type N-R has image U b V, with all other read labels identities.
The recursive label is interior, at offset q, so this is not a growing root.

## Complete chronological read histories

The following table lists every read cell and its full turn string. Ranges
with their lower endpoint above the upper endpoint are empty.

    y=-2: x=1,...,2r                         R
    y=-1: odd x=1,3,...,2r-1                 LR
           even x=2,4,...,2r                 RL
    y= 0: x=0                               RL
           x=1                               R
           x=2,...,2r-1                     RL
           x=2r                              R   (central read)
           x=2r+1                            L
    y= 1: x=0                                L
           x=1                               R
           even x=2,4,...,2r-2               LR
           odd x=3,5,...,2r-1                RL
           x=2r                              R
           x=2r+1                            L
    y= 2: x=1,...,2r                         L

To verify the table directly, the eight U reads relative to its start are
(0,0)R,(1,0)R,(1,-1)L,(2,-1)R,(2,-2)R,(1,-2)R,
(1,-1)R,(2,-1)L. Copy i adds(2i,0).

Index a V copy by m=r,r-1,...,1. Its eight reads are
(2m+1,0)L,(2m+1,1)L,(2m,1)R,(2m,2)L,
(2m-1,2)L,(2m-1,1)R,(2m-2,1)L,(2m-2,0)L.
All U reads precede the central R, and V copies occur in descending m.
These lists give exactly the table, including the overlapping row-one LR/RL
histories. Every history alternates, proving internal legality for ALL r.

## Exact minimum input and complete output

The minimum black input is

    I_r = {(x,-1): x odd, 1<=x<=2r-1}
        union {(2r+1,0)}
        union {(x,1): x even, 0<=x<=2r-2}
        union {(2r+1,1)}
        union {(x,2): 1<=x<=2r}.

The complete black output on this minimum board is

    O_r = {(x,-2): 1<=x<=2r}
        union {(x,-1): x odd, 1<=x<=2r-1}
        union {(1,0),(2r,0),(1,1)}
        union {(x,1): x even, 2<=x<=2r}.

Thus |I_r|=4r+2, |O_r|=4r+3, the complete XOR has4r+7 cells, and the read
support has10r+4 cells. These counts follow from the complete histories and
are not finite-depth extrapolations. At r=0 the separate degenerate word R
has empty input and output {(0,0)}.

In the stable bulk, the alternating rails y=-1 (odd x black) and y=1 (even x
black) remain unchanged. The fully black upper row y=2 is erased and the
fully white lower row y=-2 is filled. Only fixed-size end effects accompany
this entire-row transfer. This is a genuinely axial component, outside the
oblique-strip root obstruction, but its required entry fuel still grows
linearly and its label is not prolongable.

## How this concrete target was selected

U is the previously signed A sweep. A shortest length-eight return preserving
incoming E and moving(-2,0) has final move E, its other three horizontal moves
W, and two N/two S moves. There are exactly six choices of vertical signs.
Five already conflict in U R V; the displayed V is the sole internally legal
case and is now proved for all repetitions. This is not an increasing-bound
search for arbitrary controllers.

The immediate two-decoration root wrapper a->a U_tail b V, b->U b V does NOT
work: its second image repeats R at(1,0), at read17 after the R at read1.
More generally, the separately proved canonical-occurrence fuel bound prevents
this component from appearing in a finite-seed fixed exact-charge-preserving
controller. A charge-changing preparation mechanism or a materially different
assembly is still needed.

## A sharp same-strip inverse-interface caution

In the stable bulk, a half-turn rotated copy can exchange the upper/lower full
rows only after an ODD horizontal phase shift: its two alternating input rails
otherwise have the opposite parity to O_r. The same strip fixes the vertical
shift to zero. But a half-turn leaves the incoming-heading parity unchanged,
so an odd horizontal shift changes the invariant x+y+h modulo2. Therefore
these directly matched same-strip inverse interfaces cannot be connected by
an actual ant cap. This is a specific bulk-phase obstruction, not a general
exclusion of offset strips, different operators, or two-dimensional assembly.

## Independent certificates

The bridge's exact all-r result is
`computability/finite_power_exact_validator/axial_hairpin_presburger.json`.
Independent coordinate-equation Presburger chronology and complete-board checks
are `audits/check_axial_hairpin_presburger_independent.py/json` and
`audits/check_axial_hairpin_fields_independent.py/json`. Their symbolic bad-depth
set is empty; separate literal controls through r257 match all field counts.
The specific same-strip phase obstruction is also independently reviewed.
