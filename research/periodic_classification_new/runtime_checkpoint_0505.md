# Classification continuation, 23 October 2026, 05:05 UTC

## Signed result and delivery

The all-cap full unit-axis exclusion is independently signed, audit JC:
`axis_negative_drift_extreme_exclusion.md`. It excludes actual full
(±2,0),(0,±2) at all widths/periods/growth, by directly proving the negative
lowest-row case and then rotating. 04:49. The finite-seed
periodic-suffix bridge is appended; the auditor is reviewing that routine
stable-order corollary and `minimal_full_drift_corollary.md`.
The latter combines checker parity and the retained all-cap unit-diagonal
exclusion: Manhattan norm>=4, squared Euclidean norm>=8; the only surviving
vectors inside the max-coordinate-two box are (±2,±2). No period uniqueness
or universal eventual104 conclusion is claimed.

The earlier third-row notes are independently signed but superseded as
necessary proof machinery: zero offset for both rank-zero branches, and
(a,b)=(0,4),(0,6),(2,6) for the rank-two branch.

## New scope: larger axis drift, not a primitive quotient

At full (-4,0), upper E and W edges enter DIFFERENT neighboring D classes.
The two-word reversed ballot is therefore unavailable. We must not identify
this with the full (-2,0) cylinder. A genuinely multi-column invariant is
missing; no larger-axis theorem is claimed.

`probe_axis_multicolumn_singleton.py` supplies a necessary unbounded-rank
clock relaxation above an all-singleton lowest row for full (-2k,0).
For k=2 it has a SAT relaxation with four upper histories of length16,
(p0,q0,p1,q1)=(11,15,3,7), P=128, after finite-neighborhood exact clocks,
static edge counts and necessary phase disequalities for offsets -2..2.
This is NOT a full front and is not independently audited. It only warns
that the two-column proof is not a trivial local contradiction for k=2.
The original no-phase relaxation and the phase2 files are retained.

A literal three-row completion of that candidate has 15 event cycles,
including many zero-voltage four-cycles, so it is NOT a front. The exact
control is `probe_axis_three_row_candidate.py` and
`axis_negative_three_row_n16_control.json`. In fact a top row immediately
above the singleton-bottom/odd-mark upper row forces a first-read four-R
square, so that naive three-row completion cannot work. No all-width
conclusion follows. No new long-running process remains.

## Remaining work

Seek a coupled-column boundary invariant for full axis four, or return to
cap-four essential-height-component structure. The full conjecture, larger
axis drift and classification at full (2,2) remain open. All exploratory
solver outcomes retain their SAT-relaxation/UNSAT-solver-only/UNKNOWN status.
