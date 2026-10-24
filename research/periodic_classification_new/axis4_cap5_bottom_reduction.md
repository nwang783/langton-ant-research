# Lowest-row singleton reduction at full positive-axis-four and cap five

23 October 2026, 07:40 UTC. Independently replayed local certificate (audit KO).
This is a LOCAL BOUNDARY NECESSITY, not a complete cap-five exclusion.

Assume a complete white front of actual full drift (+4,0), with at most
five reads per physical cell. In the lowest active row choose the signed
sector A_i=(2i,0) vertical-departing, B_i=(2i+1,0) horizontal-departing.
Then, up to shifting the two A/B pairs, its complete read-count profile is

    (0,0,1,1) or (1,1,1,1).

Thus every lowest-row read class is singleton. Empty classes may remain.
No primitive quotient, period cutoff or upper strip-width bound is used.
Quarter rotations carry the correspondingly rotated boundary statement.
This note does not silently turn a lowest-row result into a highest-row
result under a drift reversal.

## Finite local reduction with an unbounded physical period

The independently signed axis_four_extreme_row_counts.md gives the ten
cap-five possibilities. The eight excluded profiles are uniform m=2,3,4,5,
(2,2,3,3), (4,4,5,5), (1,2,2,1), and (3,4,4,3), up to pair shift.
Their fixed complete bottom words are A arrivals W,E,W,E,... and B arrivals
S,S,S,.... Enumerate ALL complete upper words through five reads that
match the internal horizontal edges and these bottom-to-upper ports.
There are exactly 6,200 such upper-row assignments across the eight cases.
No condition on the open upper exterior is imposed.

Each assignment fails by one of the following necessary conditions:

1. A sealed proper successor cycle cannot occur in a single complete front.
   The only whole-window cycle that is retained is its sole voltage-one
   cycle; it is not silently discarded.
2. On a proper successor segment from a class rank j to another rank k at
   that class, cumulative seam w must satisfy w<=0 if k>j, and w>=1 if k<j.
   This is t_k-t_j = length - wP with segment length strictly below P.
3. The FIRST literal return to the exact same physical cell (same class,
   cumulative seam zero) must hit its consecutive complete rank j+1.
4. Explicit affine-in-P negative cycles in exact local read clocks.

For (4), each real arc u->v of physical seam k has

    t_v-t_u = 1-kP.

Consecutive ranks at a physical cell differ by at least four steps, so

    t_j-t_(j+1) <= -4.

These are ordinary difference constraints with affine bounds aP+b. A
certificate cycle has summed bound aP+b with a<=0 and 16a+b<0. It is
therefore negative for EVERY P>=16. The lower bound P>=16 follows the
signed white-front g>=8 plus signed paired-left kinematic bound at full
axis-four. The proof does not set P equal to sixteen.

Only seventeen upper assignments survive the literal proper-path tests:
fifteen for bottom2222 and two for bottom1221. Every one has such a
negative cycle. The two1221 survivors are explicitly stored in the
certificate. No external solver UNSAT verdict is needed.

Producer certify_axis4_cap5_bottom.py and frozen artifact
axis4_cap5_bottom_reduction.certificate.json record every upper history,
its proper-path rejection reason or its literal affine negative cycle.
The independent checker regenerates every upper assignment directly from
vertical demands and physical horizontal port counts, then verifies every
proper-path failure and every affine negative cycle. See audit KO.
The general cap-five frontier, all-cap axis-four, and finite-seed standard
capture conjecture remain open.
