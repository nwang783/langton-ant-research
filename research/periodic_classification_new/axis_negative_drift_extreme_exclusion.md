# No complete white translating front has full drift (-2,0)

23 October 2026, 04:49 UTC. Independently signed all-cap analytic exclusion.
This is a fresh calculation at NEGATIVE actual drift. It does not reflect
an ant or assume that the previous positive-drift lowest-row theorem also
holds at its other transverse extreme.

Let a complete white-input translating front have period P and actual full
drift d=(-2,0). Every class is read finitely often, with alternating R,L
turns starting R. Choose its lowest active row as y=0. Its two classes are
A=(0,0), with vertical departures, and B=(1,0), with horizontal departures.
The checker sector can be chosen by an integer horizontal translation.
No move goes below this row. Thus B has incoming history S^m; A has
incoming history W,E,W,E,... of the same positive length m.

Above them take C=(0,1), D=(1,1), with common complete history length n.
C has vertical arrivals and D vertical departures. Let p_j, q_j be the
ordered C incoming-N and D outgoing-S ranks, respectively. Both lists
have m elements. All other C arrivals are S and D departures N.
Clocks c_i,d_i are the actual read times at these fixed representatives.

## Clock equations, reversed ballot and properness

The lower paths, by exact edge ordinal matching, are

    D_(q_j) -> B_j -> A_j -> C_(p_j),

with compass S,W,N for even j and S,E,N for odd j. Since d=(-2,0),

    c_(p_j) = d_(q_j) + 3 + (j mod2)*P.             (1)

C-to-D E edges have zero seam and give d=c+1. W edges reach D+d and give

    d=c+1-P.                                      (2)

At rank r, the E-port indicator on either C or D is “marked XOR odd r”.
The E count before r is floor(r/2) plus the signed sum of earlier marks,
where an even mark contributes +1 and an odd mark -1. E and W occurrences
match by their own ordinal.

If a W source precedes an E source at C, its target must precede the E
target at D: (2) makes the target time difference even smaller. Therefore
an equal-length D prefix cannot contain more E occurrences than the C
prefix. Otherwise the earliest unmatched W source and E target give
exactly such a reversed pair. In mark notation,

    sum_(q_j<=r) (-1)^q_j - sum_(p_j<=r) (-1)^p_j <= 0.       (3)

The period P is divisible by four, since horizontal and vertical moves
alternate and the signed horizontal displacement is -2. P=4 would visit
four distinct full-drift classes once each, so all four turns would be R;
that closes a unit square instead of translating. Hence P>=8. Every
four-step return below is proper. Once m>=2, the eight-step path below is
also proper: q0 is odd, the forced q1=q0+1 gives n>=3, and hence
P>=2m+2n>=10; divisibility by four gives P>=12.

A first physical return to a cell along a proper actual path ends at the
next local rank, not merely at an arbitrary later rank. We use this only
on the explicitly traced four- and eight-step paths below.

## 1. The first downward mark is odd

Suppose q0 is even. Its incoming E has a C source C_k. The source edge
followed by the first lower path is E,S,W,N, a four-step first physical
return to C. Thus p0=k+1. Since k precedes the first mark p0, it is
unmarked; an unmarked E source has odd rank k. Matching E ordinals gives

    (k-1)/2=q0/2, hence p0=q0+2.

The first D mark is even and precedes every C mark. This violates (3).
Thus q0 is odd.

Its W source C_k and (1),(2) give

    c_(p0)=c_k+4-P<c_k, hence p0<k.                 (4)

If p0 were odd, (3) would force q0<=p0: an odd C mark appearing before
all D marks would make its left side positive. The W ordinal at q0 is
(q0+1)/2, while that at p0 is (p0+1)/2. Consequently the W source of q0
would be at or before p0, contrary to (4). Therefore p0 is even.

## 2. The first two bounces force opposite marked parities

C_(p0) now outputs E. The first lower bounce followed by this edge has
compass S,W,N,E, a four-step first return to D. Its endpoint is q0+1,
an even E arrival, which turns downward. Thus q1=q0+1. If m=1, this is
already a contradiction.

The E ordinal at C_(p0) is p0/2. At D_(q1), the earlier odd mark q0
subtracts one, so it is q1/2-1. Therefore

    p0=q0-1.                                      (5)

Starting from the W source C_k of D_(q0), follow the first two bounces:

    C_k -> D_(q0) -> B_0 -> A_0 -> C_(p0)
        -> D_(q1) -> B_1 -> A_1 -> C_(p1).

Its compass word is W,S,W,N,E,S,E,N. At physical starting C=(0,1), its
intermediate C is (-2,1) and its endpoint is (0,1); no earlier intermediate
vertex is the starting cell. Thus it first-returns physically and

    p1=k+1.

Together with p0<k, this makes k unmarked. Its W output makes k even;
p1 is odd. The W ordinal at C_k is k/2-1, since p0 is the only earlier
mark and is even. Matching D_(q0)'s W ordinal (q0+1)/2 gives

    k=q0+3,               p1=q0+4.                 (6)

## 3. The third bounce reverses local chronology

The second lower bounce followed by C_(p1)'s W edge has compass S,E,N,W,
a four-step first physical return to D. Its endpoint is q1+1=q0+2, an
odd W arrival turning downward. Thus q2=q0+2. If m=2 this is impossible.

At C_(p1), the W ordinal is (p1+1)/2-1=(q0+3)/2. At D_(q2), its two
earlier marks q0,q1 have cancelling signs, so the W ordinal is
(q2+1)/2=(q0+3)/2. Hence C_(p1) is exactly D_(q2)'s W source.

The third lower bounce has even index and zero voltage. Equation (2)
for its preceding W edge gives

    c_(p2)=c_(p1)+4-P<c_(p1),

contradicting p2>p1. All positive m are excluded.

Therefore no complete white-input translating front has actual full drift
(-2,0). A half turn of the entire plane preserves handed turns and sends
(+2,0) to (-2,0), so this excludes actual full drift (+2,0) as well.
Quarter rotations give (0,+2) and (0,-2). This says nothing about larger
axis drift such as (4,0), other drift vectors, nonperiodic behavior, or the
finite-black-on-white eventual-standard104 conjecture.

## Consequence for finite-black initial configurations

The exclusion also applies to every eventually periodic turn stream from
an arbitrary finite black seed, whenever its repeated word restores the
heading and has one of these actual full displacements. To see the needed
white-front premise directly, fix any full-drift class and write its finitely
many period-phase read positions as c+k_i*d. At c+n*d the corresponding
read times are n*P+i-k_i*P. For all sufficiently large n the cell is outside
the finite seed and all these visits occur after the prelude. Thus their
stable chronological order must alternate R,L starting R. Translating the
periodic walk through all integer periods then supplies exactly the complete
white histories used above. Stationary seed debris does not affect them.
This rules out these periodic endpoint drifts, not eventual periodicity or
universal capture by standard104.

## Method provenance and priority scope

Stable white chronological histories and first-to-first directed-edge
matching are established ingredients in the retained Jillhewar/Ke periodic
front framework. The consecutive-return rule also appears explicitly in
Hao Ke's retained analytic unit-diagonal proof,
`../sources/kehao95-core/wake_synthesis/verification/unit_diagonal_analytic/PROOF.md`,
Sections1-5. Those general tools are not claimed as new here. The present
calculation applies them to the negative two-cell axis with its reversed
horizontal ballot. The inspected axis baseline gave arithmetic restrictions
and left growth eight and larger permitted multiples open. This is a stronger
conclusion than that inspected statement, not an exhaustive literature-priority
claim or a claim of formal proof-assistant verification.
