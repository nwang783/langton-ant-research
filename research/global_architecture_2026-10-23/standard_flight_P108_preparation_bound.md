# Standard-flight preparation cannot fund arbitrarily long P108 runs

23 October 2026. The finite bulk-profile premise is independently signed;
the new finite-flight boundary/ownership lift is submitted for separate review.
No multi-flight solver was added because the proposed two-rail input has no
bulk match.

## Quantitative theorem

H is the literal standard104 word. P is the fixed108-letter prepared word
obtained from complement(reverse(H)) by replacing zero-based letter31 L with
LRRRR. Normalize a rotation so that P begins heading W and drifts(-2,-2).

Consider ANY finite legal ant prefix, on its entire original finite black
board B, of the form

    C0 H^N1 C1 H^N2 ... H^NF CF P^n.

Each H flight may begin at any heading, hence use any of the four diagonal
directions. Each Nj is any nonnegative integer; zero-length flights can be
omitted. The Cj are arbitrary literal words. Write L for their TOTAL number of
turns, r_parallel for the number of flights parallel to P's drift, and
r_nonparallel for the other two diagonal directions. Then

    |B| >= n - 2 - 6*r_parallel - L - 1408*r_nonparallel.

Equivalently, with F=r_parallel+r_nonparallel,

    |B| + L + 1408*F + 2 >= n.

No restriction on flight lengths or parameter-dependent placements is needed.
Consequently fixed initial mass, fixed flight count and bounded cap length
cannot produce unbounded P repetition counts. In particular neither two
opposite standard rails nor any other fixed-count standard-flight itinerary
gives a bounded-fuel flat-pump counterexample through this P.

The numerical bound above uses canonical literal H powers. An arbitrary cyclic
cut H=UV satisfies (VU)^N=V H^(N-1) U for N>=1. Charging these two fixed end
pieces to the caps adds exactly104 reads per nonempty flight, so the same
fixed-complexity conclusion holds for all cyclic standard phases. A uniform
coarser numerical statement in that convention is

    |B| + L + 1512*F + 2 >= n.

The whole initial black field is retained. Cj are actual read steps of one ant;
there is no seed replacement or teleportation. This does not bound arbitrary
interactions, different periodic consumers, or nonstandard prepared rewrites.

## 1. Finite profile obstruction

Label full-drift classes modulo d=(2,2) by (t,e)=(x-y,x mod2). Both NE and SW
standard writers have22 read classes: both parities at eleven consecutive
normals. All complete histories start R and alternate. Their mature output
has12 black classes, including BOTH parity classes at BOTH extreme normals.

P uses23 classes, needs11 black input classes, and its required-black normals
span eleven consecutive normal positions (range width10). Its full read
normal range, at its literal origin heading W, is [-7,4].

At a remote common level, two complete white-input standard writer bands
cannot overlap: any overlapping eleven-normal band contains a black endpoint
of the earlier band. A later complete standard history starts R there, which
cannot read that black cell.

At most two disjoint eleven-normal bands can contribute to P's eleven-normal
required-black span. Any noncontributing rail cannot supply a missing black
input, and can only pollute a white input. Every contributing rail has a black
class meeting a required-black class, giving a finite exact translation anchor.
Sector conservation permits precisely even normal translations and either x
parity relative to P's origin.

`check_standard_flight_P108_obstruction.py` separately reconstructs all such
placements with P fixed at its origin:39 single-rail placements and148
compatible unordered two-rail placements. Every one has a missing required
black or a polluted required white. The table is in
`standard_flight_P108_obstruction_certificate.json`. Rotation by180 degrees
covers the opposite consumer orientation. This is a finite all-placement
certificate, not a radius, word-length or period scan.

The construction analysis's separate anchored normalization has59 pair cases;
the larger table here is deliberately less reduced. The two counts describe
different finite enumerations, not different claims of matching interfaces.
The59-case table and its geometric reduction have now been independently
reconstructed in `../audits/check_reverse108_rail_bundle_independent.py/json`.

## 2. One shared physical orbit gauge

Let q be the actual starting cell of P. Every physical cell has a UNIQUE
representation

    q + (e,e-t) + k*d,  e in {0,1}, k in Z.

Thus k is a common physical longitudinal level, defined even for cells outside
P's read support. Cells selected at different k are necessarily distinct.
This avoids a hidden multiplicity factor when the mismatching class varies
from one level to another.

For a P phase position u_i, write u_i=(e_i,e_i-t_i)+k_i*d. In copy j its level
is k_i-j. Every phase is present at every level in

    [max_i k_i - n + 1, min_i k_i].

The checker obtains max k_i-min k_i=2. Hence there are at least n-2 complete
consumer levels, with the inequality still valid when n<2.

## 3. Standard-flight endpoint windows

At each parallel writer's literal phase, the common level has form

    a_i + sigma*j, 0<=j<N, sigma in {+1,-1}.

All a_i are integers. Let a_min,a_max be their extrema and W=a_max-a_min.
For sigma=+1, every level outside the two windows

    [a_min,a_max-1], [a_min+N,a_max+N-1]

has either ALL phase visits or NONE. For sigma=-1, use

    [a_min-N+1,a_max-N], [a_min+1,a_max].

Each window has W levels; overlap only improves the bound. These statements
also handle flights shorter than a fringe width. The only origin dependence
of W is the relative x parity. Direct literal phase reconstruction for both
parallel headings and both parities gives W<=3. Discarding at most six levels
per parallel flight therefore makes every such flight complete or absent.

This partition uses actual longitudinal endpoints, not an assumption that all
rails coexist on a common infinite interval. Different flights may cover
different portions of the consumer, and the lengths Nj need not be affine in
any parameter.

## 4. Fixed nonparallel intersections: a linear, not quadratic, loss

A parallel writer is relevant if its read band meets P's full read-normal
range [-7,4]. Such a band lies entirely in the enlarged normal interval

    U=[-17,14].

U contains64 full-drift classes, both parities at32 normals. A nonparallel
standard read strip consists of22 affine lattice lines in the other diagonal
direction. Each meets each of U's lines in at most one physical cell.
Consequently one nonparallel flight reads at most22*64=1408 cells in U,
independent of its length, offset, or the number of parallel writers. Discard
their common levels. This covers not only direct intersections with P, but
also every possible relevant writer–writer black-endpoint clash witness.

There is no missing quadratic flight-pair term. An irrelevant parallel writer
cannot erase an earlier black clash cell in U: after endpoint fringes have
been discarded, its first read there would itself be R and therefore illegal.
The only possible repairs are nonparallel reads or cap reads, both explicitly
discarded. This local black-persistence observation prevents a distant chain
of intermediate parallel writers from repairing a relevant overlap.

Finally discard every level containing any cap read, at most L levels. This
retains all actual debris and all possible cap interventions.

## 5. Each remaining level costs one distinct initial black cell

At any remaining complete consumer level:

* Every parallel writer is complete or absent.
* No cap or nonparallel flight reads any cell in U at this level.
* All relevant active parallel writer bands are disjoint, by the complete
  first-R black-persistence argument above.
* Their exact mature outputs therefore form one of the excluded compatible
  rail bundles.

The bundle mismatch cannot be a required white polluted by a writer black:
that would contradict the consumer's first read. Nor can it be a required
black at a cell any active writer has read and left white. Both are impossible
in the assumed legal prefix. Therefore some required-black P cell lies
outside every active writer read band and must be black in the INITIAL B.
Absent writers never read any cell at this level, and all other interventions
were discarded. Different retained levels give distinct physical B cells by
the common gauge.

The number of remaining levels is at least

    n-2-6*r_parallel-L-1408*r_nonparallel,

proving the theorem. The statement remains true when the right side is negative.

## Scope

The fixed-count conclusion follows from this explicit linear inequality, not
from a general principle that finitely many components have bounded collisions.
One can escape this PARTICULAR obstruction only by changing the consumer,
introducing nonstandard repeated preparation, or letting flight/cap complexity
grow. Nothing here excludes such routes or establishes a global defect budget.
The supplied two-block exact validator remains separately frozen and audited;
there was no reason to extend it to a multi-flight candidate with no input match.
