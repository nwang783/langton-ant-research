# Classification checkpoint, 23 October 2026 05:50 UTC

New signed conditional result:
`axis_multicolumn_singleton_local_branches.md` proves the exact two local
branches above a fully singleton bottom at actual (-2K,0), K>=2. Odd q
forces p=q; even q forces p=q+2. The q marks cannot all be equal around
the cylinder. This does not force the bottom to be singleton or exclude
axis-four fronts. 

The earlier singleton symbolic probe had assumed all marks odd. This was
not a proven necessary premise for multiple columns. Do NOT use its
UNSAT outputs for classification. Its SAT outcomes were already explicitly
only partial-clock relaxations. The corrected signed note preserves the
real even branch, and fresh literal open-strip clock controls admit distinct
even q values, so no all-odd claim remains.

A compact exact fixed-strip cylinder-clock implementation is being tested:
`synthesize_axis_compact_clock.py` uses one binary heading per local rank,
port-prefix counts, rank-matched clock equations and real clocks. It avoids
exponential explicit state enumeration. SAT must reconstruct the entire
physical period through the retained independent-format checker. The
implementation itself is not independently audited. Its first conditional
cap6/H4 odd13 control agrees with the old producer's solver-UNSAT result,
in0.25 seconds versus1.55 seconds. A cap8/H6 odd13 real-clock run is active
Existing signed real-clock
equivalence supplies the analytic framework, not implementation validation.
