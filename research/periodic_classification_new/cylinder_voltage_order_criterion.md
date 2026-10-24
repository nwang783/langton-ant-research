# Exact cylinder criterion using only local states and integer voltages

23 October 2026. Independently analytically reviewed, including both lazy clause types.
Implementation and solver UNSAT derivations require separate audit.
It applies with any finite visit cap, and uses the FULL candidate drift.
Fixed-strip searches remain finite searches, never unrestricted exclusions.

Fix d=(a,b), a>0, with a+b even, and finitely many full-drift representative
cells. At each representative choose a complete white history R,L,R,L,...
with allowed incoming-axis headings. Match the kth traversal at either end
of every directed physical edge. Edge counts must agree, and all boundary
ports must vanish. This gives a successor permutation of the chosen events.
Each successor edge e->f carries the integer k for which the physical target
of its representative source is representative(f)+k*d. Write P for the
total number of chosen events. Require the sum of all edge voltages to be 1.

**Criterion.** The assignment is a complete white translating front exactly
when the following two conditions hold:

1. Every event-permutation cycle has strictly positive total voltage.
2. For each pair of consecutive chronological visits j,j+1 at one
   representative, the forward successor segment from j to j+1 has
   nonpositive voltage.

Condition 1 plus total voltage 1 forces exactly one cycle, of voltage one.
Every event cycle has integer voltage and the cycles partition the edges.
Conversely a full-period front has precisely that single winding-one cycle.

For the single cycle, choose one event's time zero. Traversing r edges
with cumulative voltage k gives its representative event time

    t = r - k P.

After the complete cycle this is consistent, because r=P and k=1. For
consecutive local visits, let L be the number of successor edges from j to
j+1, and w their voltage. These are distinct events, so 1<=L<P. Their
representative time difference is L-wP, strictly positive exactly when
w<=0. Thus Condition 2 is precisely all local white-history order, with
no clock variables or large integer bounds needed. These times satisfy
every edge-clock equality and give the signed exact cylinder criterion.

## Sound lazy exclusions

A nonpositive-voltage event cycle can never occur in a complete front.
Fixing every cell state on that cycle preserves all its matched edges,
so the conjunction of those literal states can be forbidden.

If Condition 1 holds but a local j->j+1 segment has positive voltage,
fixing every cell state on the segment preserves its edges and the local
chronological-order requirement. Any completed event cycle would have
P>=L+1, hence L-wP<0. Therefore that state conjunction can also be forbidden,
independently of how all other cells are assigned.

There are finitely many local-state assignments on a supplied strip.
Repeated SAT proposals and these sound exclusions therefore form a complete
finite decision method if run to exhaustion. An iteration limit or solver
timeout is UNKNOWN, never UNSAT. A reported solver UNSAT is not itself an
independently checked formal proof certificate.

## Implementation and controls

`synthesize_white_cylinder_lazy.py` implements the criterion with every
complete white history through the selected cap. It records the literal
bad cycle or bad-order segment for each learned clause. Any accepted state
assignment is converted to exact event clocks and a period word, then to
a finite black seed by past-read parity on histories straddling time zero.
The ordinary ant is replayed for 100 full periods before SAT is reported.

`check_lazy_cylinder_standard_control.py/json` supplies positive controls
from the standard word at periods104,208,312 and full drifts(2,2),(4,4),(6,6).
They use22,44,66 classes respectively and preserve maximum multiplicity10.
Each reconstructed phase supplies a15-cell finite seed and passes100-period
literal replay. These are author controls, not independent audit.

## Signed rank-preserving clause generalization

Independent analytic review also accepts replacing each fixed cell state
by all states preserving the witness's named local event indices. For
each witness arc, keep the source event's outgoing heading and its ordinal
among that port's outgoing events, and the target event's incoming heading
and matching incoming-port ordinal. Intersect these conditions per cell.
Static total edge-count matching remains imposed. Hence the same endpoint
events are paired, with the same seam voltage, for every allowed combination.
The entire bad cycle/segment and its local-order violation are preserved.
Extra events can change P but still leave P>L for a proper wrong-order
segment. These broader conjunctions may therefore be forbidden soundly.
The generalized implementation records the per-arc index/heading/ordinal/
voltage obligations together with its allowed-state sets. This signoff
does not certify the implementation or terminal solver UNSAT derivations.
