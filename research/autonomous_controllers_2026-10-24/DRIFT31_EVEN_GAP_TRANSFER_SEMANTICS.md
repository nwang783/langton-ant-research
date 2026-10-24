# Exact even-gap count transfer, and why its finite residue projection is not an exact controller state

24 October 2026. Author proof and exact OPEN countercontrol, submitted for
independent review. No complete front, finite board factor or controller is
constructed here. Reachability from the signed lower prefix remains open.

## 1. Scope and motivation

The signed middle-short mode has full odd inventory
{0,1,2,6,7,6c+1,6a+2,6a+4}, with 2 <= c <= a. Long intervals between these
classes therefore have even COMPLETE read multiplicity. This note derives a
transfer relation for such an interval without bounding its length, period or
visit multiplicities. It also identifies exactly what conservation does not
compress. The 3,109 previously enumerated partial interfaces are not extended.

Throughout, actual full drift is (3,1), normal coordinate T=3y-x, and incoming
headings are vertical on even T and horizontal on odd T. Every cell history
starts R and alternates R,L, as required of a complete WHITE front.

## 2. Exact local count laws on even-read cells

For an even-T cell let I be its known N-arrival count and J its known E-departure
count. Write its read length as 2m and let h be its number of N arrivals at L
ranks. Counting R and L positions gives

m = J-I+2h,
W departures = J-2I+4h,
S arrivals = 2J-3I+4h,
max(0, ceil((2I-J)/3), I-J) <= h <= I.

These inequalities are exactly the nonnegativity of all four incoming-heading
rank counts: N/R=I-h, N/L=h, S/R=J-2I+3h, S/L=J-I+h. Conversely, every integer
h in this interval supplies those valid counts and at least one binary heading
word. Chronological ordinal compatibility with other cells is a separate test.

For an odd-T cell let I be its known W-arrival count and J its known S-departure
count. If l is the number of W arrivals at L ranks, then

m = I+J-2l,
N departures = J+2I-4l,
E arrivals = 2J+I-4l,
0 <= l <= min(I,J,floor((I+J)/3)).

Again these are exact count-level possibilities: W/R=I-l, W/L=l,
E/R=J-l, E/L=I+J-3l. They do not assert a realizable chronological ordering.

Both laws derive the familiar finite local bound 2m <= 2(I+J), but I and J are
not uniformly bounded over an arbitrary long even gap.

## 3. The four-port spatial cut and its conserved current

At a cut immediately after an even level t, the four crossing physical edges
carry counts

w = W_t, n = N_(t-1), s = S_(t+1), u = S_(t+3).

Here subscripts label departure classes. The W edge jumps +1 in T, N jumps +3,
and S jumps -3. Counting all actual crossings gives the conserved normal
current J_cut = w+n-s-u. A complete finite read footprint has no crossings at
its distant ends, so J_cut=0 throughout. Hence u=w+n-s, leaving three counts
v=(w,n,s), with all four edge counts nonnegative.

This is a conservation law for TOTAL directed traffic, not merely odd-edge
parity, emitted black output, or an assumed finite input stock.

## 4. Two-level transfer and its finite residue projection

Process the next odd cell with parameter l from Section 2. It has incoming
I=w and outgoing J=s, and creates

e = 2s+w-4l, n_new = s+2w-4l.

Process the next even cell with I=n, J=e and parameter h. It creates
w_new=e-2n+4h and u_new=2e-3n+4h. The old u becomes the new s. Therefore

v_new = A v + 4(h-l, -l, 0),
A = [[1,-2,2], [2,0,1], [1,1,-1]].

The exact admissible parameter intervals are those in Section 2, first for
(w,s,l), then for (n,e,h). This is a finitely presented integer relation, not a
finite set of states. Direct multiplication gives A^3=-3I. Consequently

v_(t+6) = v_t modulo 4

through six even-read levels. Modulo 4, the 64 triples form four fixed points
and twenty three-cycles under the two-level map. These are cycles of the
RESIDUE PROJECTION ONLY. None is thereby an ant trajectory or regenerative
controller. The integer lift and all chronological data remain essential.

There are count-level fixed points of arbitrary size: w=n=s=u=2k, h=l=k.
Thus conservation alone cannot provide a strict resource loss on every count
cycle. A valid exclusion must use more chronology or a proved reachability
restriction, not declare those cycles impossible by assertion.

## 5. What an exact chronological transfer must retain

For a finite spatial prefix, the literal ordinal successor graph decomposes
into open directed chains unless it already has a forbidden closed component.
A completion-equivalent symbolic boundary description must retain at least:

- every crossing port's total multiplicity and ordered occurrence labels;
- the pairing of incoming and outgoing boundary occurrences through each
  internal chain, together with that chain's length and full-drift voltage;
- all consecutive-read clock inequalities, with their integer constants and
  coefficients of the unknown full period, between chain anchors;
- the full odd-class ownership already fixed, and the conditions for eventual
  closure into ONE actual event cycle of winding +1, not several disjoint cycles.

The chain description can compile older internal events into their exact
relations; it cannot replace an unbounded ordinal list by its parity. At final
closure, every class must have its complete WHITE order and the complete event
cycle must use all events once. Any reconstructed word still needs the retained
exact finite-support checker and finite-overlap realization before it is called
a controller. No unread field or residual archive is silently removed.

These are finite objects for each fixed prefix, but their state space is not
shown finite. Open-chain lengths, crossing multiplicities, occurrence matchings
and clock coefficients can all grow. A proposed finite abstraction must prove
that identifying two such states preserves admissible completions. Merely
observing the six-level residue period does not prove that.

## 6. An explicit unbounded OPEN clock family

For every k>=1, give three consecutive classes T=0,1,2 the COMPLETE histories

H0=(NNSS)^k, H1=(EEWW)^k, H2=(NNSS)^k.

All three have 4k reads, zero odd output, and 2k uses on each incident physical
port. All other classes are UNKNOWN. This is a local even-band interface, not
an actual read-minimum prefix and not claimed reachable from the signed g8
lower boundary.

For block b=0,...,k-1, assign the following read clocks at representatives
(0,0),(-1,0),(-2,0), respectively:

H0: 128b + (60,64,96,100),
H1: 128b + (1,33,65,97),
H2: 128b + (0,4,8,32).

Take the full-period PARAMETER P=128k+2. The four internal physical ordinal
matches per block are exactly

H0_(4b+1) -> H1_(4b+2), H0_(4b+2) -> H1_(4b+3),
H2_(4b) -> H1_(4b), H2_(4b+3) -> H1_(4b+1).

Each target clock is source+1. Every same-cell consecutive read gap is a
positive multiple of four. All 12k named phases are distinct modulo P and
satisfy the actual spatial phase sector, including under every full-drift lift.
There are 8k open chains and no internal event cycle. The remaining 116k+2
phases are NOT filled. No routing outside the three named classes is supplied.

The displayed formulas prove these facts for every k; finite controls in the
checker are replay checks, not extrapolation evidence. This family shows that
zero odd output plus literal local port, rank, phase and clock constraints do
not uniformly bound even-band traffic. Its arbitrary port demands also show
why an exact ordinal interface cannot simply identify every k by a residue.
It does NOT prove that global g8 prefixes reach all k, that a whole infinite
front exists, or that no more sophisticated finite quotient can be proved.

## 7. Precise next proof obligation

The unresolved question is reachability and chronological closure, not the
count residue period. One may now seek either:

(a) a symbolic invariant restricting integer lifts and chain permutations
reachable from the signed lower prefix, strong enough to exclude long even
gaps or force an upper-boundary contradiction; or
(b) an explicit whole event-cycle completion of one allowed lifted transfer,
then exact supplied-word/finite-support replay.

No such invariant or completion is claimed in this note. The explicit
integer map, admissible parameters, normal current and open countercontrol
are auditable inputs for that next step.

Artifacts: `check_drift31_even_gap_transfer.py` and
`drift31_even_gap_transfer_certificate.json`. The checker also reconstructs
all 64 residue states, exact local count controls, and six literal members of
the unbounded open family. No solver or external software is needed.
