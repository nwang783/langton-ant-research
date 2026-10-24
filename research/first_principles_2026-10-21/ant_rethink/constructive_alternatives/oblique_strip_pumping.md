# Bounded complete crossing histories force a translating tail

21 October 2026. Research note. The full highway conjecture remains open in
this investigation. The arguments below are conditional. They do not identify
the resulting word with the standard period-104 word.

The rule is white/right, black/left, toggle, then move. The initial black field
is finite. Positions are integer pairs. A trajectory can be restarted at any
finite time, because its black field is still finite.

## 1. A general crossing-history theorem

**Theorem.** Suppose the ant's x coordinate tends to positive infinity. Suppose
there are constants K and D such that every sufficiently far vertical cut
`x=k+1/2` has at most K crossings, and the y coordinates of all its crossings
have diameter at most D. Then the turn stream is eventually periodic. Its
positions have a nonzero integer translation per period.

The bounds concern COMPLETE crossing histories, including every later return.
No effective method for finding their final crossings is assumed.

### Finite types

Choose cuts beyond the initial head and all initial black cells. Their crossing
lists are finite because x tends to infinity. Each list starts with E, alternates
E,W,...,E, and ends with E. Record each crossing heading and its y coordinate
minus the y coordinate of the first crossing. These offsets lie in [-D,D].
Thus at most

    S = sum_(j=1)^K [2(2D+1)]^j

types are possible. In fact the alternation and first-zero constraints give a
smaller number, but this loose bound suffices.

Take two cuts k1<k2 with identical types. Let y1,y2 be the heights of their
first crossings, and put u=(k2-k1,y2-y1).

### Splice complete histories

Keep every portion of the original trajectory in x<=k1. Keep every portion in
x>=k2+1, translated by -u. Discard the intervening columns. Interleave the two
kept histories by their crossing indices.

Each interface pose matches. An E crossing of the first cut enters at exactly
the translated position and heading of the corresponding E crossing of the
second cut. The same holds for W crossings. Within each retained half-plane,
keep that half-plane's own chronological order. Its cells therefore have the
same colors as in its source history at every processed event.

The initial complete state is unchanged. Every initial black cell and the
initial head are in the retained left half-plane. Both the deleted band and
the retained right half-plane are initially white. Translation of the right
half-plane changes no initial bit. Unvisited initial black cells on the left
remain present.

The lists have the same finite odd length. The left and right finite pieces
therefore alternate until the last E crossing. After it, the spliced run uses
the translated infinite suffix to the right of the second cut. Every step is
a valid ant update from the original complete initial state. Determinism makes
the spliced trajectory identical to the original one.

Let T1 and T2 be the times immediately after the original final E crossings
of the first and second cuts. The final seam crossing in the splice occurs at
T1. The original ant must cross the second cut after T1, so T2>T1. The suffix
identity gives, for every n>=0,

    p_(T2+n)=p_(T1+n)+u,
    h_(T2+n)=h_(T1+n),
    turn_(T2+n)=turn_(T1+n).

This proves a translating periodic tail with period T2-T1 and nonzero drift
u. The x component of u is positive.

This proof does not require the translated right-hand path to lie in a
previously specified strip. It only needs exact lattice translation, matching
crossing poses, preserved within-side history, and initially white right
half-planes. A restriction on an arbitrary geometric enclosure is not part of
the ant's transition rule.

## 2. Every fixed non-axis strip forces a translating tail

**Corollary.** Suppose that on a tail

    c <= a*x+b*y <= c+W,

where a,b are nonzero real numbers and W is finite. Then the turn stream is
eventually periodic with nonzero integer drift u=(u_x,u_y), and

    a*u_x+b*u_y=0.

In particular, confinement in an irrational-slope strip is impossible.

### Uniform visit bounds

Put delta=min(|a|,|b|)>0 and ell(x,y)=a*x+b*y. At each cell, the incoming axis
is fixed: position parity and heading axis both alternate at every update.

Choose the two adjacent neighbors that increase ell. They are one horizontal
and one vertical neighbor. One of the two turn colors, determined by the
incoming axis and the signs of a,b, always uses at least one of these upper
neighbors. Turns at a given physical cell alternate in color.

If N(q) counts visits on the confined tail, every other event at q can therefore
be assigned to a visit of an upper neighbor. One initial pseudo-arrival can be
excepted. A visit at one neighbor cannot receive two assignments from q: that
would require an immediate reversal q -> neighbor -> q, which the 90-degree
turn rule forbids. Consequently

    N(q) <= 2 N(q+e1) + 2 N(q+e2) + 3.

This also proves finiteness inductively. Any infinite number of q events would
force infinitely many upper-neighbor events.

An upper step raises ell by at least delta. Set

    r(q)=floor((c+W-ell(q))/delta)+1.

Upper neighbors in the strip have rank at most r(q)-1; those above it have no
visits. Induction on r gives

    N(q) <= 4^r(q)-1 <= L:=4^(floor(W/delta)+1)-1.

### One longitudinal end

Each vertical column intersects the strip in at most

    H=floor(W/|b|)+1

lattice cells. Each has finitely many visits. Thus each column has finitely
many visits. An infinite path cannot remain in finitely many columns. It also
cannot reach arbitrarily large positive and negative x values repeatedly,
because that would cross a fixed column infinitely often. Therefore x tends
to one infinity. A half turn makes that infinity positive.

### Apply the crossing-history theorem

Each cut has at most K=2HL crossings. Both of its adjacent columns have y
coordinates in an interval of length at most (W+|a|)/|b|. Thus the crossing
heights have diameter at most

    D=ceil((W+|a|)/|b|).

The first theorem applies. A periodic tail with drift u remains in the strip
only if ell(u)=0: otherwise ell(p+n*u) is unbounded. Since u_x is nonzero,
the strip's direction must have rational slope.

### Period bound

Choose the matching cuts among S+1 consecutive cuts, with S as in Section 1.
Their separation d is at most S. The time removed by the splice is exactly
the total number of departures from their d intervening columns. Each column
has at most H visited cells, each with at most L visits. Hence a period exists
with

    P <= S*H*L.

This is a finite theoretical bound. It is too large to be a useful enumeration
limit in general.

## 3. Extension to finitely many non-axis strips

Suppose a tail is contained in a finite union of fixed-width strips, all with
non-axis directions. Merge parallel strips into one wider strip whenever
needed. Any two remaining center lines are nonparallel. Their strips have
bounded intersection.

The following elementary peeling argument gives a uniform cell-visit bound
for the union.

For each constituent strip, let r_i be the maximum rank used in Section 2.
Let r=max_i r_i. Outside a sufficiently large finite square, every radius-r
lattice neighborhood in the union meets at most one strip. Such a neighborhood
therefore has the same corner-removal argument as that single strip.

Start with the union's lattice cells. In each round remove every cell with two
adjacent neighbors already absent. Outside that finite square, every cell is
removed within r rounds, because the argument depends only on its radius-r
neighborhood. After r rounds, only a finite set remains.

Every nonempty finite lattice set has a cell with two adjacent missing
neighbors: choose its highest row, then the rightmost cell in that row.
Thus the remaining finite set disappears after finitely many further rounds.
There is a finite global peeling depth R.

The same event assignment as above, using the adjacent missing neighbors at
the round when a cell is removed, gives

    N(q) <= 4^R-1

for every cell. The two chosen neighbors need not be the same pair at different
cells; their fixed incoming-axis cases still select one alternating color.

The finite central square is visited only finitely many times. Outside a large
enough square, the constituent strip arms are pairwise disjoint and separated
by more than one lattice step. After the last central visit, the ant therefore
stays in one strip arm. Section 2 supplies the translating periodic tail.

Hence a nonperiodic finite-seed trajectory cannot eventually lie in any finite
union of fixed-width non-axis strips. Axis directions are essential exceptions
to this proof, because an axis boundary has only one outward neighbor at an
ordinary boundary cell.

## 4. Scope and prior work

The earlier investigation already supplied the diagonal-strip theorem and its
complete-history splicing proof. This note retains that method and broadens
its sufficient geometric conditions. It must not be reported as an independent
proof of the global highway conjecture or of period-104 uniqueness.

Current primary factor-language notes refer to oblique-strip and diagonal-cross
visit arguments, so no novelty claim is made for the geometric extension. This
note makes the arbitrary integer splice translation and irrational-slope
consequence explicit.

An asymptotic direction does not imply fixed-width strip confinement. A path
can have transverse displacement that is unbounded but sublinear. The proof
also supplies no uniform crossing-history bounds for an arbitrary finite seed.

Relevant primary source status was checked on 21 October 2026:

- https://github.com/Atharva12456/langtons-ant-highway
- https://github.com/kehao95/langtons-ant-core
- https://github.com/kehao95/langtons-ant-core/blob/main/factor_language/proof/silent-axis-return.md

Both repositories still distinguish their conditional results from general
finite-support convergence.
