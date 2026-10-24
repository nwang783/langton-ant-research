# A genuine four-step return cannot skip two middle reads

24 October 2026. Author analytic proof, submitted for independent review.
This removes two interfaces from the signed complete diagonal minimum
cover77fde6d4. It is independent of any bounded SMT UNSAT result.

## Complete histories and all-cap scope

Use the complete WHITE front, full d=(2,-2), actual minimum-read-row
normalization of DIAGONAL_READ_MINIMUM_COMPLETE_INTERFACE.md, independently
signed report9d8ef1d3. Consider its one-singleton minimum case

    T0=(0,-1): W;             T1=(1,-2): empty;
    B0=(0,0):  NS;            B1=(1,-1): SS;
    A0=(0,1):  WEWW;          A1=(1,0): WWEE or WWEEW.

The histories listed are COMPLETE, not cropped factors. All higher cells
and the full period remain unrestricted. We prove BOTH A1 options
impossible in any such front, at every growth and visit count elsewhere.

Let Q1=(1,1). It has exactly three outgoing W occurrences, because A0
has three incoming W reads. It has I=2 or3 incoming N occurrences,
because those are exactly A1's outgoing N reads.

## The forced local first return

The THIRD W departure of Q1 must, by physical ordinal matching, enter
A0 at its third W arrival, which is rank3/L. From there the actual path is

    Q1.thirdW -> A0.L3 -> B0.L1 -> A1.L3 -> Q1.secondN.

All four moves and intermediate ranks are forced by the supplied complete
histories. A0 has just one S departure, B0 just one S arrival and two E
departures, and A1's second E arrival is rank3. The last step is A1's
SECOND N departure. The three intervening positions are distinct and
none is Q1. Thus Q1's second N arrival is the very next read after its
third W departure, exactly four time steps later.

## WHITE alternation forces Q1's first N to be rank3/L

The second N read cannot be L, because N/L turns W and would produce a
FOURTH W departure after the already third W departure. It is therefore R.
The previous rank is L; to depart W it must itself arrive N. It is Q1's
FIRST N occurrence. All earlier headings were S.

If the second N rank is k, then k is even. The initial k-1 S reads have
k/2 R turns, each departing W, and the preceding first N/L adds one more.
Exactly three W departures have then occurred, so k/2+1=3 and k=4.
Therefore the complete heading prefix is S,S,S,N,N; in particular the
FIRST N read is rank3/L. No visit cap or upper-region assumption entered.
For reference the full allowed Q1 words are SSSNN/SSSNNS if I=2, and
SSSNNSN/SSSNNSNS if I=3, but the contradiction needs only this prefix.

## The impossible middle-rank jump

A1's FIRST read is W/R and departs N. This is the first N arrival at Q1,
now known to be Q1.L3. The actual next four moves are consequently

    A1.R0 -> Q1.L3 -> A0.L3 -> B0.L1 -> A1.L3.

These positions form the unit square

    (1,0) -> (1,1) -> (0,1) -> (0,0) -> (1,0).

There is no intermediate read at A1. The path therefore asserts its next
read after rank0 is rank3. This skips its required complete ranks1 and2.
Equivalently, the four edge equalities force t(A1,3)-t(A1,0)=4, whereas
three consecutive same-cell return gaps force this difference at least12.
There are no seam voltages in this literal physical square, and no choice
of period, distant support, initial board, or reverse BLACK root repairs it.

## Exact consequence and controls

The signed 227-interface all-growth diagonal cover now loses these two
cases, leaving225 necessary open interfaces. At g=8 the independently
signed cyclic-E exclusion separately removes its nine cases, giving216
necessary open interfaces. In the one-singleton category only FOUR of the
previous six remain. No remaining interface is certified completable or
excluded here, and there is no conclusion g>=12.

The author checker check_one_singleton_skipped_middle.py/JSON rebuilds the
four possible Q1 complete words and verifies every physical occurrence
ordinal in both four-step paths. It is a control for the short analytic
proof, not a substitute for a full controller checker.

The height13/cap12/g8 constructive search happened to return bounded UNSAT
for these two cases. That output is neither a premise nor a proof of this
all-period result. The literal skipped-rank contradiction above is the
independently checkable reason that no higher completion can exist.
