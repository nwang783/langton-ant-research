# Equality in four-visit drift packing is not a white front

23 October 2026, 08:51 UTC. Analytic candidate; independent review pending.
The previous packing and four-unit-return factor lemmas remain separately
signed. This adds a WHITE-input argument specifically at multiplicity four.

Let a complete initially-white translating ant front have actual full
drift d with D=||d||infinity>=3, and let a quotient cell have exactly n=4
complete reads. It cannot attain packing equality

    P = 4(n-1)+2D = 2D+12.                       (1)

Consequently, together with the signed n>=5 factor refinement,

    P >= 4n+2D        whenever D>=3 and n>=4.     (2)

## Equality gives a literal loop cluster and an extremal passage

The reviewed packing proof shows equality forces exactly one nonzero
cyclic class gap, displacement d and length2D, and three zero-displacement
four-step gaps. Cut the cycle at the start of these three zero gaps, at
physical cell v=(0,0). All four reads of this physical v occur in this
single cluster; thus its first turn is R by the complete white premise.
Choose incoming W by a genuine quarter rotation.

The complete local enumeration in four_unit_returns.certificate.json has
exactly TWO legal three-loop words with this initial R. Their traces are:

A = RRRRLRRRRLLL. Its first two loops surround the NE and SW unit faces;
its third loop needs the cell SE=(1,-1) black on its first use within the
cluster. The loop cluster ends with incoming W. The following fourth
central read is L, so the winding passage starts S. Its final step is W
because the full period restores the initial incoming heading W.

B = RRRRLLLLRLLL. Its first two loops surround NE and SE. Its third loop
needs NW=(-1,1) black on its first use within the cluster. The cluster ends
with incoming E, so the fourth central L starts the winding passage N.
Again the winding passage ends W.

The winding passage has2D steps. In any coordinate attaining |d_i|=D,
all of that coordinate's D moves have the same sign. It is therefore
monotone in at least one dominant coordinate. All earlier passages have
the same property. Earlier loop clusters are centered at -j*d, j>=1;
in a dominant coordinate they are at least D-1>=2 away from v, so they
miss all near-v cells at coordinate±1 used below.

## A cannot acquire its necessary SE black cell

Dominant east is impossible because the passage ends W. Dominant north
is impossible because it starts S. Thus a dominant direction is west or
south (or both).

If dominant south, all earlier passages lie at y>=0 near v, and earlier
loop clusters have y>=D-1>=2. Neither of the first two current loops NE/SW
visits SE=(1,-1). Its third-loop required L would therefore be its first
physical read, violating white input.

If dominant west, every horizontal move in a passage is W. Earlier loop
clusters miss x=1, and only the immediately preceding passage can read
near-v x=1 cells. That passage ends with W from E=(1,0) to v. Its immediately
preceding step is vertical, at x=1; no other vertical move can occur in
that column. Therefore it can visit SE=(1,-1) only by stepping N from SE
to E immediately before the final W.

But then its first physical read at E arrives N and departs W, requiring
L. E has not been read before: older passages stay at x>=D, older loops
at x>=D-1, and the current loop cluster has not started. This contradicts
white input. If the preceding passage does not visit SE, SE instead has
the forbidden first L in the third current loop. A is impossible either way.

## B cannot acquire its necessary NW black cell

Dominant east is impossible by its final W; dominant south is impossible
by its first N. Thus a dominant direction is west or north.
For dominant west, every earlier passage is at x>=0 near v and earlier
loops have x>=D-1>=2, so none reads NW=(-1,1).
For dominant north, every earlier passage is at y<=0 and earlier loops
have y<=-D+1<=-2, again missing NW.
The first two current loops NE/SE also miss NW. Its third-loop required L
is therefore its first physical read, contradiction. B is impossible.

This excludes equality (1). Heading/axis parity makes P congruent to2D
modulo4, as is2D+12, so strict inequality improves by at least four and
proves (2). This is not reflection symmetry; all dominant-direction cases
are treated on the same fixed R/L rule.

## Universal period consequences, not standard104 minimality

The signed unrestricted cap3 exclusion gives some n>=4. Therefore every
white front with D>=3 satisfies P>=2D+16. For D2 the only remaining drift
family is(±2,±2), whose signed cap6 exclusion already givesP>=28.
For D1 the signed all-cap unit-diagonal exclusion leaves no front.

In particular EVERY nonzero white translating front has P>=26: D3 has
signed cap4 exclusions and thus n>=5, givingP>=26; D4 has signed cap4
exclusions everywhere (axis4 even through cap5), givingP>=28; D5 gives
P>=26 from (2); D>=6 givesP>=28. D2 andD1 were just handled. These are
all-cap lower period bounds. They do not classify all fronts, prove104
minimal, imply eventual periodicity, or settle finite-seed capture.
