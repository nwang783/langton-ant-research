# Compact exact complete-white cylinder-clock encoding

23 October 2026, 05:57 UTC. New producer implementation, not independently
signed. Analytic framework: the previously signed full-period cylinder-clock
criterion and its real-clock equivalence. This is not a theorem excluding
an unbounded set of supplied drifts.

Producer: `synthesize_axis_compact_clock.py`.
Positive controls: `check_compact_clock_positive.py/json`.

## Finite discrete variables without exponential state tables

At cell class i, select a complete length n_i in{0,...,cap}. For each local
rank j<cap, one Boolean chooses between the two possible incoming headings
on that cell's fixed incoming axis. The turn is R at even j and L at odd j.
Thus every complete initially-white history is represented, and only such
histories are represented. Inactive heading bits may be fixed arbitrarily.

For each incoming and outgoing heading, define its integer prefix count
at rank j as the number of active lower ranks carrying that port. Total
counts on neighboring directed ports must agree. For every active source
rank j and active target rank k that carry the same physical directed edge,
equality of their prefix counts means exactly that their occurrence ordinals
match. Impose the clock equation precisely for these pairs. Equality of
full counts makes these matches bijective, so the resulting finite event
graph is a permutation.

Clocks are REAL. P is INTEGER and equals the total sum of active lengths.
Every matched edge from a representative u to v+z*d imposes

    t(v,k)+z*P=t(u,j)+1.

Adjacent active ranks at the same representative satisfy

    t(i,j+1)>=t(i,j)+4.

This is a valid strengthening of strict order: successive physical visits
to a cell need at least four moves. Inactive clocks are unrestricted.
One active clock is gauged to zero. P>0. The implemented even-horizontal
full-drift geometries also impose the necessary P divisible by four.

## Why real clocks remain exact

Sum the edge equations on any permutation cycle of length L and total
integer voltage z. One obtains L=z*P. Since L>0 and P>0, z is a positive
integer. The lengths of all cycles sum to P, so their positive voltages
sum to one. There is exactly one cycle, with voltage one and length P.
Starting at the gauged event and following its edges now shows every active
clock is integral. The cycle has one event in each temporal residue modulo
P; reconstructing the physical period from those residues gives an actual
walk with the supplied full drift. Ordered local ranks guarantee complete
white R,L alternation at every physical cell. Conversely every complete
white front in the supplied strip and cap supplies these exact variables.
Thus the compact representation is equivalent to the signed explicit-state
criterion, subject to faithful implementation.

## Geometry and current scopes

The core uses actual full drift d=(-2K,-dy), with representatives
(x,floor(dy*x/(2K))+v), x=0,...,2K-1, v=0,...,H-1. Reducing a physical
neighbor at x coordinate X gives seam voltage -floor(X/(2K)). Empty outside
neighbors are enforced by zero incoming/outgoing boundary-port counts.
The currently exposed searches use dy=0. Literal positive controls use
full diagonal drifts(-2,-2),(-4,-4),(-6,-6) without quotienting them.

`odd13` fixes a singleton bottom and specified length-four second-row
histories with odd marked ranks1 and3. `even02` is a second conditional
pattern. `singleton` fixes just the entire bottom to singleton. `free`
fixes no histories and only requires A0 active in the lowest row, a valid
horizontal choice of origin for an active boundary. Each run is still at
a FIXED height and multiplicity cap.

The existing reconstruction routine validates every SAT model by rebuilding
all P phases, checking unique phases, physical nearest-neighbor moves,
headings, turn rules, local white order and the final supplied displacement.
The standard104,208,312 complete-history controls pass. These controls do
not replace independent audit of every symbolic formula or solver proof
certificates. UNSAT outputs remain FIXED-STRIP SOLVER RESULTS; UNKNOWN is
retained unchanged. No SAT counterfront has been found at this checkpoint.
