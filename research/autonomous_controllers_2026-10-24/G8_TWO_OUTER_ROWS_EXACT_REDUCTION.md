# Seven paired boundary modes excluded with all higher ports open

24 October 2026. Author finite proof certificate, submitted for independent
review. This is an ALL-PERIOD, ALL-WIDTH local reduction within the signed
cyclic-E growth-eight branch, not a whole-front classification.

## Hypotheses and exhaustive domain

Use the signed canonical boundary and G8_CYCLE_THREE_OUTER_MODES.md
(fe06a08d). The full drift is d=(2,-2), and the four boundary classes have
W singleton histories at t=-1 and SSN triples at t=0. The next C row t=1
has modes X=EEWW, Y=EEWWW, Z=WEWWE. Both full-drift classes are included.
The following Q row t=2 has even histories because all remaining odd
outputs must be on positive odd levels. No global visit cap is assumed.

For each Q class, let I be its number of N arrivals from the lower row
and J its number of W departures into that row. Exact matching gives
I,J in{2,3}, determined by the adjacent X versus Y/Z counts. A Q history
of even length n has X_N R-rank N arrivals and I-X_N L-rank N arrivals,
with

    n = 2(J-I+2X_N),  0<=X_N<=I,
    n<=2(I+J)<=12.

Every such choice is explicitly enumerated by choosing the N positions
at even and odd ranks; all remaining headings are S. Thus the lists are
COMPLETE, not an assumed bounded-visit experiment. Their sizes are10 for
(I,J)=(2,2),19 for either mixed pair, and46 for(3,3).

The nine paired C modes therefore give

    100 + 4*361 + 4*2116 = 10,008

exact local histories on the eight named cell classes. All complete
letters alternate WHITE R,L,R,L,... . Every outgoing/incoming occurrence
on a physical directed edge internal to these rows is matched by ordinal,
with the FULL d voltage retained. Every higher incoming/outgoing port is
left open and explicitly retained.

## Two elementary rejection witnesses, independent of P

1. CLOSED INTERNAL EVENT COMPONENT. If the matched internal successor
   graph contains a cycle, those phase events already have all successors
   and predecessors fixed. They cannot join any additional event. Every
   complete growth-eight front must have at least two further odd classes
   outside these eight cells: the lower circle accounts for4 and row1 at
   most2, while row2 is even. Its whole actual event permutation must be
   one cycle. Hence any internal closed component is impossible, at any
   winding and any full period. The outside odd-output obligation is kept
   explicitly; no missing exterior is treated as empty.

2. SKIPPED PHYSICAL READ RANK. Follow a contiguous internally matched
   successor chain and lift its cells using the exact edge voltages. If
   consecutive occurrences of one PHYSICAL cell on that chain have ranks
   r and s with s!=r+1, the proposed history is impossible. There is no
   external event between those chain events in the actual trajectory.
   Matching only turn parity would be insufficient; the complete ranks
   must be consecutive. The certificate supplies the entire intervening
   chain segment, same lifted cell, and incompatible endpoint ranks.

Neither witness is an SMT status, a simulation cutoff, or a lower bound
on a proposed finite period. Both are exact local contradictions with
arbitrary higher fields and ports still open.

## Exhaustion result and exact surviving interfaces

The supplied certificate lists all10,006 rejected cases, indexed by their
two C modes and two complete Q words:

    1,494 contain a closed internal event component;
    8,512 contain a skipped physical rank.

Exactly TWO local history assignments remain:

    (Y,Y), with BOTH Q words SSSNNSNS;
    (Z,Z), with BOTH Q words SSSNNSNS.

Consequently every complete cyclic-E g8 front must have equal odd modes
Y/Y or Z/Z at t=1, and exactly eight reads with incoming SSSNNSNS in each
t=2 class. Modes XX,XY,XZ,YX,ZX,YZ,ZY are excluded locally, without a
period or higher-width bound. The previously signed seventeen-event Y/X
interface remains a correct OPEN first-row control, but this stronger
next-row proof shows that it cannot extend with the required even Q row.

Each remaining interface has34 events, ten open incoming and ten open
outgoing ports. Their complete internal event chains are supplied in the
JSON report. They have no closed internal event component or skipped rank.
Relaxed chain clock potentials are supplied at P=140 only as a positive
necessary-condition control. They have one phase collision and are NOT
claimed as whole trajectories, geometric completions, or finite seeds.
The surviving histories, not those particular clock values, are the
remaining exact possibilities.

## Output budget and next obligation

The lower circle has four odd classes, row1 now has two, and row2 has
none. Exactly TWO further odd C classes remain, one in each lane. Row2's
upper ports are nonempty: it has five incoming S and five outgoing E
occurrences per class. Therefore the support cannot terminate here, and
the next C row has five lower-side E arrivals and five S departures at
each class. No repetitive row pattern or uniform higher multiplicity
bound is inferred from this first forced eight-read row.

## Reproducibility

* enumerate_g8_cycle_two_outer_rows.py generates every case and witness.
* g8_two_outer_rows_rejection_certificate.json contains all10,006 local
  contradictions as explicit closed cycles or lifted chain segments.
* enumerate_g8_cycle_two_outer_rows.json retains both surviving complete
  interfaces, all open ports, mode counts, and clearly scoped clock data.

The small difference-constraint routine is used only to exhibit relaxed
clocks for the two survivors; NO rejected case depends on it. The complete
exclusion premise is precisely the two explicit witness types above.
