# Actual read extrema remove one whole interleaving family

24 October 2026. Author all-cap proof, submitted for independent review.
This concerns the live two-quadruple SINGLE-USED F-circle branch, not an E cycle.
It is not a complete exclusion of that branch or of drift(3,1).

## Exact maximum lemma for the COMPLETE read footprint

For full drift(3,1), let T=3y-x and normalize the minimum READ level to0.
The signed minimum lemma92b5092a makes that class a vertical S/R singleton.
Since incoming axis flips with checker parity and T=x+y modulo2, even T classes
have vertical incoming headings and odd T classes horizontal incoming headings.

The COMPLETE read footprint has a finite maximum M. Any read there can arrive
only N or W: the other headings would require a predecessor above M. If M were
horizontal, its first WHITE W/R would exit N, above M, impossible. Thus M is
vertical and even, and every arrival is N. A subsequent N/L would exit W, also
above M. Its complete history is therefore exactly one N/R.

In particular M is an odd-output class. Every odd-output class is read, so

    max{T of ALL odd-output classes}=M, and M is even.     (1)

The analogous minimum is also the minimum of the full odd set. This is a
statement about the complete READ footprint, not a black-field maximum, an
emitted-field cutoff, or a contour extremum. Unread black data above/below the
footprint is allowed and never cleared. No multiplicity or width cap is used.

## The negative-pair full-wake family is impossible at every scale

The two-quadruple F-circle branch and its middle-read reduction92380db9 give
candidate FULL odd inventories

    {0,1,2,5,6,6a+1,6b+s,6c+s},
    a>=2, 1<=b<c, s=2 or5.

The exact quadratic theorem b5f64068 requires b<a<=c. With s=5, the largest odd
level is then6c+5, which is ODD. This contradicts(1). Thus the ENTIRE s=5
interleaving family is excluded, with unbounded a,b,c, period, and upper traffic.
The application requires the independent status of its family/character
premises; it does not elevate a partial output subset to a full wake.

The remaining family is s=2, b<a<=c. Its maximum6c+2 is even and is not excluded
by the maximum lemma alone. No contrary chronological ordering has been proved.

## The smallest positive interleaving inventory cannot extend this prefix

At c=2 the parameter inequalities force a2,b1. Its full odd set is

    {0,1,2,5,6,8,13,14}.                                (2)

It passes the retained signed-residue, winding and quadratic parity screens.
Nevertheless it CANNOT extend the present forced complete circle/middle prefix,
which includes T5=EEW, T6=NNN, T7=EEEW. The short contradiction is:

1. By(1), the full read maximum is14, with T14=N singleton.
2. T13 has no N exit to unread16, so every read exits S. It receives exactly
   one E input from T14. Hence its complete history is E or EW; odd status in
   (2) forces E.
3. T12 has no S arrival from unread15, so all arrivals are N. Its W exits feed
   the zero W inputs of T13. It is empty or N singleton; even status in(2)
   forces it EMPTY.
4. T9 has no N exit to empty T12, and no S exit to T6, whose complete history
   NNN has zero S arrivals. Thus T9 is EMPTY too.
5. T8 therefore has no W exit and all its reads exit E. It receives exactly
   two N inputs from the complete EEW at T5, so WHITE alternation makes its
   history NSN or NSNS (odd status selects NSN, but is not needed below).
6. There is an uninterrupted physical four-step return from T8's FIRST E
   departure to its SECOND N arrival through T7.R0, T4.R0, T5.R2. In either
   all-E history this goes from rank0 to rank2, skipping rank1. Contradiction.

With representative T8=(-8,0), that return visits(-7,0),(-7,-1),(-8,-1), then
(-8,0), so no hidden read at the start or quotient-only seam is involved.
The full-drift lifts of T4 and T5 are -1; the return closes in physical space.
All other histories and unread fields remain unknown. This excludes (2) ONLY
as an extension of the specified live circle branch, not automatically every
possible front sharing its odd inventory.

Consequently the remaining two-quadruple branch satisfies

    s=2, c>=3, 1<=b<a<=c.                               (3)

The candidate full odd set{0,1,2,5,6,8,13,20} (a2,b1,c3) passes the same retained
parity screens and is not excluded by this particular top-zero-port argument.
No complete chronology, finite seed, or alternative controller is supplied.

## Audit boundary

This is an analytic proof from literal firstness, complete-history port totals,
and one exact return. The accompanying `check_drift31_extreme_read_controls.py`
records all boundary turn checks, the mandatory small histories, the geometric
four-return and both concrete screen results. The controls are not a replacement
for the complete-read maximum proof or independent review. Exact dependencies
are in `DRIFT31_EXTREME_READ_SHA256SUMS`. The full positive interleaving family,
all-quadruple circle branch, multiply-used F cycles, and finite-seed conjecture
remain open.
