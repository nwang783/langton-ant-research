# Necessary repeated-right directional defect, without a multiplicity cap

23 October 2026. Independently analytically reviewed, all sections.
This uses the signed stream-function and cut/barrier argument in
`cap_three_shifted_stream_height.md`, not its cap-three local exclusion.

## Statement

In every complete initially white nonzero translating Langton front,
there is a physical-cell history in which the counts of R reads with the
two possible incoming headings differ, and the larger count is at least
two. No bound on history length, period, width or drift is assumed.

## Local formula

At an even vertex, write r_E,r_W and l_E,l_W for R and L incoming-heading
counts. Complete white alternation gives r=l or r=l+1, where r=r_E+r_W
and l=l_E+l_W. The shifted stream heights around this vertex are, up to
an additive constant,

    (H_NW,H_NE,H_SE,H_SW) = (1-l_E,r_W,1-l_W,r_E).

The odd cases are rotations. If max(r_E,r_W)>=2, the two L-face entries
are <=1, so the maximum is unique exactly when r_E!=r_W. If both R counts
are <=1, there is never a unique maximum: for r=2 the two C entries tie
at one; for r=1 the bound l<=1 leaves at least one L entry at one; and
for r=0 both L entries are one. Thus the stated defect is exactly a
unique local maximum of the shifted stream height.

## Global necessity

Suppose no defect exists. Then no local maximum is unique. The non-axis
part of the signed proof applies verbatim: the maximum on every monotone
full-drift dual cut is independent of its position, contradicting the
exterior stream jump one.

For axis drift, the signed row-maximum propagation also applies verbatim.
It forces some adjacent pair of dual rows to have values M everywhere on
one row and values strictly below M on the other. At each intervening
vertex, precisely two adjacent corners are maxima. Here is a cap-free
replacement for the old short local table. One maximizing corner is C and
one is L, so the local maximum in the displayed normalization is <=1.
Since all r counts are nonnegative and the other L entry is not larger,
the maximum is one (a maximum zero would force r=0 and l=0, inconsistent
with the L entries). If r=2, both C entries are one and opposite, so the
maxima cannot be precisely two adjacent corners. If r=0 the two L entries
are opposite maxima. Hence r=1. If l=0 there are three maximizing corners;
therefore l=1. The complete history is exactly RL.

With a horizontal pair of maxima, the two vertical ports each have count
one and exactly one horizontal port has count two. The same double-domino
barrier therefore follows. Its two nonempty successor-invariant side sets
contradict the single full event cycle. Thus absence of a defect is also
impossible for axis drift.

## Cap-four reduction

For maximum multiplicity four, the necessary defect has length three or
four and its first and third incoming headings agree. Up to an
orientation-preserving rotation, choose that heading W; the six possible
complete histories are

    (W,E,W), (W,W,W),
    (W,E,W,E), (W,E,W,W), (W,W,W,E), (W,W,W,W).

These are incoming-heading lists; their turn lists are RLR or RLRL.
Unlike the signed cap-three theorem, the criterion does not exclude these
six cap-four possibilities. It isolates the exact local family that any
cap-four front must contain.

## Stronger global-maximum form

Independently analytically reviewed, 23 October 2026, 01:17 UTC.

At least one vertex has exactly one incident corner attaining the GLOBAL
maximum M of H. This is an existence assertion for at least one defect,
not a statement that every defect is globally maximal.

First, M exists and is finite. H is periodic under the full drift, the
active strip has finitely many face classes on the cylinder, and both
exteriors have constant unshifted heights. Write their constants as
c_low and c_high=c_low+1. Since exterior shifted heights include c_high+1,
we have M>=c_low+2. Every face sufficiently far on the lower exterior side
has H<=c_low+1<M.

Suppose no vertex has exactly one M-corner. The binary face function
B=1[H=M] has no unique maximum on any dual square: a square with no M-corner
has four zeroes, and any other square has at least two ones. Therefore
replacing the middle corner of a dual three-face path preserves its maximum.
For non-axis drift, the signed EN/NE and cyclic-shift argument makes the
maximum of B on a monotone full-drift cut independent of the cut's position.
Some such cut contains a face attaining M, while a cut far on the lower
exterior side has B=0 throughout. Contradiction.

For axis drift, some horizontal dual row contains an M-face and a far
lower-exterior row contains none. At an adjacent transition, the no-unique-
M-corner property propagates M along the entire row containing it. Each
intervening dual square has two adjacent corners equal to M and two strictly
below M. The cap-free adjacent-max argument above forces every intervening
cell to be exactly RL. Its double-domino row is again a successor-invariant
separator, impossible for one event cycle.

Hence the global maximum is unique among the four corners at some vertex.
That vertex satisfies the already signed unequal-R-count criterion. Under
cap four it belongs to the same six normalized families, with the additional
necessary condition H(F)<=H(peak) for every face F in the plane. Restricting
that inequality to any finite neighborhood is a valid necessary relaxation.
