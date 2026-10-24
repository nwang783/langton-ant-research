# Exact local clocks automatically enforce one translating event circuit

22 October 2026. Submitted for independent analytic review.
This is a fixed-support synthesis criterion, not a bound on all front supports.

Fix a nonzero full drift d preserving checker parity, a checker/heading-axis
sector, and a finite set K of vertices of the cylinder Z^2/<d>. Choose a
lattice representative b_v for every v in K. Vertices outside K are empty.
At each v choose one of the locally allowed complete white histories of
length m_v<=3. For the cap-three front problem the independently proved
same-type exclusion leaves 11 possibilities: empty, and R, equal-heading
RL, opposite-heading RL, AAB, ABB with either possible first heading.

Let

    P = sum_v m_v > 0.

For each chosen read j at v introduce an unbounded integer T_(v,j), ordered
strictly by j. For every directed physical edge, list its traversals at
both ends in chronological rank. Require the counts to agree. If the edge
from representative b_u reaches b_v+k d, and its r-th traversal uses read
j at u and read l at v, impose

    T_(v,l) + k P = T_(u,j) + 1.

Edges reaching outside K have zero traversal count. Incoming directions
and outgoing directions are those of the chosen heading/turn histories.
All constraints are integer-linear for fixed K,d. The visit count defining
P is an integer expression in the finitely many local state choices.

## Proposition

These local clocks and ordered histories are equivalent to a complete
white-input cap-three translating front supported in K, in the selected
sector and with full drift d, after allowing a global time shift.

The nontrivial direction does NOT require an additional connectivity test,
a pairwise phase-distinctness constraint, or a bound on the T variables.
Every read slot has exactly one successor and predecessor, by edge-count
matching. Thus the finite set of read slots is a disjoint union of directed
cycles. On a cycle C of length L, sum the clock equations. The T terms cancel,
yielding

    L = k_C P,

where k_C is the integer sum of representative-crossing voltages. Since
L>0 and P>0, k_C is a positive integer and L>=P. But the sum of all cycle
lengths is exactly P. Therefore there is exactly one cycle, of length P
and voltage one. Along it the clocks increase by one modulo P, so all
phases are distinct and it translates by exactly d.

The strictly ordered clocks at each representative give the required
stable physical R,L,R chronology, not just a quotient cyclic order. The
previously established white-input realizability criterion then supplies
a finite black seed realizing the translating tail.

Conversely any such front supplies these states, clocks and edge equations
by taking the actual read times at the chosen physical representatives.

## Computational scope

`synthesize_cap_three_cylinder.py` implements this criterion for d=(-n,-n)
and the explicitly supplied strip |y-x|<=w. It uses the preinstalled libz3,
installs nothing, and leaves integer clock variables unbounded. P is
computed from the states rather than enumerated. Any returned model is
replayed independently at every phase before being marked SAT.

An UNSAT result concerns ONLY that drift, sector, and finite strip. It does
not bound the period or support of arbitrary translating fronts, and it
is not a general cap-three classification. The files retain UNKNOWN for
timeouts. The absence of a presently known cap-three positive control is
not a substitute for an independent encoding audit.
