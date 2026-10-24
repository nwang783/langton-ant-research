# Cap-four first-read backbones climb the stream height

23 October 2026, 09:43 UTC. Analytic candidate; independent review pending.
This couples GLOBAL stream height to actual physical FIRST-read chronology;
it is not a drift-radius or local-factor search. Only complete bi-infinite
WHITE fronts of read cap four are considered. No initial-head exception is
allowed. The full drift quotient is retained throughout.

Use the signed stream function h with f(e)=h(C_right)-h(L_left), where C
faces have clockwise directed boundaries and L faces counterclockwise
boundaries. At an active vertex v let

    m(v)=max{h(F): F is one of the two incident C faces}.

## Local first-R maximum rule

The counts of R corners around the two C faces have difference equal to
the difference of those two face heights, by the signed local stream table.
For example at an even vertex, the signed stream-table normalization gives
h(NE)=k+r_W and h(SW)=k+r_E for one common additive k; odd vertices
are genuine rotations. Their sum r_W+r_E is the total number of R reads,
at most TWO under cap four.
If the two R-corner counts differ, the smaller must be zero: the only
possibilities are(1,0),(2,0) and their reversals. If they agree, both incident
C heights agree. Therefore the FIRST read, an R, always turns around a
C face attaining m(v).

Let a(v) be the physical predecessor cell of v's first read. It is active,
is incident to this same maximizing C face, and satisfies

    m(a(v))>=m(v),       first_time(a(v))<first_time(v).     (1)

The second inequality uses the actual earlier read at a(v), not a phase.
Both the predecessor map and m are equivariant under the ACTUAL full drift.

## Global essential backbones

There are finitely many active cell classes in the full-drift cylinder.
Every orbit of the quotient functional map a therefore reaches a directed
cycle. Heights m are nondecreasing under a, hence constant on the cycle.
Lift a cycle to the physical plane; its net displacement is k*d. Summing
(1) gives k*P<0, so k<0. The cycle is simple in the embedded full-drift
cylinder (distinct vertex classes and consistently directed checker edges),
hence its winding is0,+1 or-1. Therefore k=-1.

Reversing this dependency cycle gives an ACTUAL-EDGE directed simple
essential cycle of winding+1. It is not asserted to be one uninterrupted
ant time interval. Every edge's clockwise face has the same height m.
In particular a cell with m=M_C=max_C h reaches a backbone whose every
clockwise incident face has height M_C.

For any threshold lambda, form corner-connected components of C faces
with h>=lambda. At a vertex incident to such a component, its first-R face
also lies in that component. The predecessor stays incident to it. Thus
every component containing an active vertex contains an essential backbone
in its full-drift quotient and has an unbounded physical lift. Finite
active C-superlevel islands are impossible. This is stronger than a purely
local maximum restriction, but does not forbid essential high strips.

## Candidate global period consequence

Use the separately signed global-maximum defect criterion for shifted
height H(C)=h(C), H(L)=h(L)+1. Its global maximum M is attained uniquely
among a vertex's four incident corners somewhere, necessarily at a C face.
Consequently M_C=M and a maximal-C backbone exists.

Let its reversed actual-edge cycle have length ell. At a right corner only
one clockwise face is incident to its two edges, so its vertex needs at
least one read. At a LEFT corner, the two edges have the TWO opposite
clockwise faces on their right, both at height M_C. Equality of their
heights forces their R-corner counts to agree; positivity of the first R
then forces at least one R around each. Such a vertex has at least THREE
reads. A simple essential rectilinear cylinder circle has zero total
turning, hence equally many right and left corners. Thus the complete
multiplicities of its DISTINCT cell classes sum to at least2*ell.

The signed global-maximum defect vertex has at least three reads and
UNEQUAL incident C heights. If it lies on this backbone, it cannot be a
left corner, so it contributes at least two beyond that corner's minimum
one. If it lies off the backbone, its at least three reads are additional.
In either case

    P>=2*ell+2.

The checker sector makes the cycle alternate horizontal/vertical edges,
and its full winding+1 displacement is d, so ell>=2*norm_infinity(d)=2D.
Therefore a cap-four WHITE front would satisfy

    P>=4D+2,

rounded upward to its compulsory residue P=2D modulo4: explicitly
P>=4D+4 for even D, and P>=4D+2 for odd D. This is a necessary all-drift
cap-four period relation, not a global cap-four exclusion, a proof that
any backbone is a single time interval, or an all-cap statement.

The zero-turning fact above can be obtained by the elementary turning/Euler
formula on the annulus between the embedded essential circle and a distant
parallel geodesic; their total signed curvature is zero. Independent review
should check this topology and the extra-two defect argument separately.
