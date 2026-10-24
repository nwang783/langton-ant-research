# An upper-boundary lifetime obstruction for the paid201 factor

24 October 2026. Author all-period proof for independent review. This closes
one of the two a=5 inventory choices for the supplied factor, not the general
middle-short family and not all c=a fronts.

## Concrete conclusion

The independently signed paid201 finite factor cannot occur inside a complete
WHITE full-drift (3,1) front whose FULL odd inventory is

    {0,1,2,6,7,31,32,34}.

This is the live middle-short choice a=c=5. The a=5,c=3 inventory
{0,1,2,6,7,19,32,34} is not excluded by this argument.

The contradiction concerns two actual BLACK input lifetimes of the factor,
not a blanket rejection of prepared BLACK cells. At physical points

    q=(-3,5),    q+d=(0,6),    d=(3,1),

the factor has these exact reads:

    q+d: time87, W/L;
    q:   times93,105,109,117, respectively W/L,W/R,W/L,E/R.

The four reads at q are consecutive PHYSICAL reads of q. Full drift translates
the first observation back to a read of q at time87-P, strictly before93 for
every positive period P. Thus the complete T29 history needs an earlier W/L
read before that consecutive four-read block. The exact upper boundary makes
that impossible.

## General local rank lemma

Let M be the maximum of the COMPLETE read footprint of a complete WHITE
full-drift (3,1) front, with the vertical incoming sector on even normal
levels T=3y-x. Suppose the parity pattern at M through M-5 is

    odd, even, odd, odd, even, even.

Then any consecutive read block W/L,W/R,W/L,E/R at level M-5 must begin
at COMPLETE rank1. Consequently there can be no earlier L read at that
full-drift class before the block. Exterior histories below M-5 are entirely
unrestricted and not assumed empty.

For the concrete full odd inventory above, the signed complete-read extreme
lemma gives M=34 and complete history N at M. The maximum is of the read
footprint, not of the BLACK field or merely of a cropped emitted wake.
The required parity pattern is exactly present, so the general rank lemma
applies at T29.

## Complete finite upper cover, with derived bounds

Start with T34=N and T35,T36,T37 empty. The upper classes are COMPLETE. At
an even new level, match its S incoming count I and W outgoing count J to
the already complete upper neighbors. At an odd new level, match E incoming
count I and N outgoing count J instead.

The bound n <= 2(I+J)+1 is derived, not imposed. For the even case, if a/b
count S arrivals on R/L ranks, then I=a+b and J=a+floor(n/2)-b; hence
floor(n/2)=I+J-2a <= I+J. For the odd case, writing a/b for E arrivals gives
ceil(n/2)=I+J-2b <= I+J. Enumerating the corresponding R- and L-position
subsets therefore gives every complete word at every multiplicity compatible
with these exact upper ports. The required odd/even total is then enforced.

Exact physical first-return chains through the already named upper cells
require consecutive endpoint ranks. Every rejected word has its explicit
violated ordinal equation, skipped-read path or positive clock-cycle witness
stored in the certificate. No solver status is used.

The cover is:

- T33 has the sole word EW.
- T32 has the sole word NNN.
- T31 has the three five-read words EWEWW, EWWWE, WWEWE.
- T30 has57 complete port-compatible words across those branches. Their
  actual upper first returns reject54. The only surviving T30/T31 pairs are
  NNNNSS/EWWWE, NNSSNN/WWEWE and NNSNNS/WWEWE.
- In each of those three branches, T29 has I=3,J=3, even length and derived
  bound13. There are46 complete words per branch,138 in total. Exact upper
  returns reject121. Five further words have explicit skipped ranks and
  four have explicit positive clock cycles. The remaining eight complete
  upper interfaces are listed below.

    T30     T31     T29
    NNNNSS  EWWWE   EEWE
    NNNNSS  EWWWE   EWEWWWWE
    NNNNSS  EWWWE   EWWWEWWE
    NNNNSS  EWWWE   WWEWEWWE
    NNSNNS  WWEWE   EEWE
    NNSNNS  WWEWE   EWEWWWWE
    NNSNNS  WWEWE   EWWEEWWW
    NNSNNS  WWEWE   EWWWEWWE

These are necessary OPEN upper interfaces, not full front realizations.
Every omitted level at or below28 remains UNKNOWN.

## The exact ownership/rank contradiction

In a complete WHITE cell history, even ranks turn R and odd ranks turn L.
Check the eight words without adding any visit cap. The block W/L,W/R,W/L,E/R
has no placement except in EWWWEWWE, where it occupies ranks1,2,3,4.
There is no earlier L rank: the only earlier rank0 is R.

In the supplied factor, the translated W/L at87-P is an ACTUAL earlier read
of the same physical q as the block at93 onward. It therefore must have a
strictly smaller ordinal than the block's first rank, while still being an
L. Rank0 cannot supply it. This is the contradiction. In particular, an
unspecified preceding R does not solve the issue: it would still have to
be followed by this distinct earlier L within the same complete history.
No WHITE-first assumption was applied to the finite factor itself; it is
applied only to the hypothesized complete front's full class history.

## Scope

This excludes the paid201 factor in the exact a=c=5 full inventory at every
period and at arbitrary exterior multiplicity. It neither retracts the
literal 28-to-41 finite-factor replay nor excludes the general c=a branch.
The a=5,c=3 upper ownership test still has surviving interfaces; they are
necessary partial models, not candidates with complete fields or clocks.
No larger a, arbitrary controller, or eventual attraction claim follows.
