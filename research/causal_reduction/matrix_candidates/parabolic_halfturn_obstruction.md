# Polynomially growing shear matrices: an even-prefix obstruction

23 October 2026, 03:07 UTC. Independently signed analytic review at 03:11 UTC.
This is a new extension beyond expansive spatial matrices, not a universal
ant theorem or an image-length enumeration.

## Statement

Let phi be a uniform substitution of length k>=2 on absolute movement letters
E,N,W,S, with

    phi(-d)=-phi(d),       net(phi(d))=A d,

where A is an integer two-by-two matrix of the form

    A=epsilon I+N,   epsilon in{1,-1},   N!=0,   N^2=0.

No growing rooted power-limit of phi can be an actual ant trajectory from
finite black support. There is no image-length bound and no restriction on
internal visits to coarse vertices. In particular this excludes all nonzero
integer shears [[1,b],[0,1]] whenever the local geometric/parity conditions
permit them, and their negative, conjugate and transposed versions.

The conclusion concerns one fixed half-turn-symmetric four-direction
substitution and its rooted power-limits. It does not cover arbitrary
nonperiodic directives, independent opposite images, or finite-state context
refinements. Power-bounded spatial matrices remain outside this theorem.

## 1. Reduce a rooted cycle to a fixed point

Take a power psi=phi^m for which the rooted infinite movement word P is an
actual fixed point. Its length K=k^m, half-turn symmetry and endpoint matrix
B=A^m are inherited. Here

    B=epsilon^m I + m epsilon^(m-1) N,

so B is again a nontrivial signed unipotent matrix with the same bounded-
orbit subspace ker N. Work with psi below and rename its matrix B as A.

The actual movement word alternates horizontal and vertical directions.
Both axis classes therefore occur. Half-turn symmetry makes the starting
axis of an image depend only on its source axis. If K is odd, legal image
seams force the two source axes to map to opposite starting axes; if K is
even, they force a common starting axis. Thus the ordinary two-axis
curvature recurrence applies. Missing signs of an axis cause no problem:
the opposite image is the half-turn of an occurring image.

## 2. Polynomial area kills the mean curvature mode

Let U_r be the internal signed right-minus-left turn excess of the refined
E image psi^r(E); the W image has the same excess. Let V_r be the common
N/S excess. Every internal turn in an occurring refined image is a legal
quarter turn. Half-turn symmetry preserves its sign.

Put S_r=(U_r+V_r)/2 and D_r=(U_r-V_r)/2. Splitting a refined image into
its K refined child images gives

    S_r=K S_(r-1)+beta_r,       |beta_r|<=K-1,
    D_r=eta D_(r-1)+gamma_r,    |gamma_r|<=K-1,

where eta is1 or-1 for odd K and0 for even K. The bounded terms are exactly
the at most K-1 child seams. Consequently

    S_r=C K^r+O(1),       D_r=O(r).

No periodicity of the seam corrections is needed.

Because ||A^j||=O(j+1), every position in a depth-r image is a sum of r
bounded local offsets acted on by powers of A. Its radius is O(r^2), so
it reads at most O(r^4) distinct lattice cells. In an ant-legal word on
ANY coloring, each cell contributes at most1 in absolute signed excess.
The actual rooted refined prefix therefore has polynomial excess. Its
internal excess is S_r plus or minus D_r, with only one bounded initial
turn correction. This forces C=0 and hence

    U_r+V_r=O(1),

uniformly in r. The difference U_r-V_r may still grow linearly; discarding
that difference without explanation would be an error.

## 3. Even prefixes cancel the remaining mode exactly

Take any FIXED even prefix w of the actual fixed point P, of length2n.
It has exactly n horizontal and n vertical movement letters. The refined
word psi^r(w) is again an actual prefix of P. Its internal child excess is

    n U_r+n V_r = n(U_r+V_r)=O_n(1).

There are only2n-1 seams between these child blocks and one initial turn,
so its complete signed turn excess is bounded independently of r. For a
finite initial black set, black mass at these checkpoints is bounded.
The endpoint is A^r p(2n). The previously signed axial midpoint inequality
therefore implies that A^r p(2n) is bounded in r.

For A=epsilon I+N,

    A^r z=epsilon^r z+r epsilon^(r-1)N z,

so boundedness is equivalent to N z=0. We conclude

    p(2n) belongs to ker N for every n>=0.                 (*)

Already p(2) is one of(1,1),(1,-1),(-1,1),(-1,-1). Thus unless ker N is a
grid diagonal, (*) is impossible. The diagonal cases are excluded by the
next elementary finite-fuel lemma.

## 4. No finite-seed ant has all even positions on one grid diagonal

Normalize the initial position to0 and its incoming heading to north.
At every even time the incoming heading is vertical, so the next move is
horizontal; at odd times the next move is vertical. Suppose every p(2n)
lies on one fixed grid diagonal. Then the even positions form a nearest-
neighbor walk on that diagonal, identified with Z. Each directed coarse
edge has its own odd intermediate cell, and opposite directions along the
same coarse edge use different intermediate cells.

If the diagonal has slope+1, its allowed two-move pairs are EN or WS.
Their second turn is ALWAYS L. A repeated odd intermediate cell would thus
repeat L without an intervening opposite read, which is impossible: the
spatial parity prevents that cell from being read at an even time. Hence
all infinitely many odd reads are distinct first-L cells, requiring an
infinite initial black set.

If the diagonal has slope-1, its pairs are ES or WN, and every odd turn
is R. Again no directed coarse edge can be used twice. An infinite nearest-
neighbor walk on Z without a repeated directed edge is eventually monotone.
For example, after traversing an edge in one direction and then reversing
across it, crossing that edge again in the original direction is forbidden;
an infinite walk cannot keep reversing in a bounded interval, nor alternate
between the two unbounded ends. Its eventual motion must therefore continue
forever toward one end without reversal.

Along either eventual monotone pair sequence ES,ES,... or WN,WN,...,
every late EVEN turn is L: S->E or N->W. The even positions are then distinct,
so infinitely many of these are first-L cells. This also requires an infinite
initial black set. Both diagonals are impossible, proving the lemma and the
theorem.

## 5. Scope and conceptual gain

The earlier expansive-matrix proof used mass O(r) versus an exponentially
escaping endpoint. That argument does not apply to a shear, whose endpoint
can escape only linearly. Here the equal axis counts of EVEN prefixes remove
the entire O(r) curvature mode, leaving bounded checkpoint mass. This is
why the polynomially growing, nonexpansive case is excluded without a
stronger global mass-divergence theorem.

In dimension two, an integer matrix with spectral radius at most1 and
unbounded powers must have a nontrivial Jordan block at eigenvalue1 or-1,
so it has the displayed form. Thus within this half-turn rooted-power class,
all genuinely nonexpansive spatial matrices left open by this result have
bounded powers. No claim is made that the unit Gaussian matrices exhaust
all such power-bounded integer matrices.
