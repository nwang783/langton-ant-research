# Twelve remote black cells suffice for two-sided standard completion

23 October 2026. Author proof and exact implementation controls. Independent
review pending. This is a completion theorem and a limitation of finite-history
arguments, not universal finite-seed capture and not a noncapturing ant.

## 1. Statement

Let X=(B,p,h) be any complete finite black state. Let K be a finite protected
spatial set, and let T_minus,T_plus be any finite nonnegative integers. There
is an effective set E of at most twelve initially white cells, outside a square
containing B, K, and all reads/poses in the protected two-sided interval, such
that:

1. X_E=(B union E,p,h) has exactly the same head positions, headings and read
   colors as X throughout [-T_minus,T_plus]. On this protected interval its
   complete field is the original complete field XOR E; no claim of globally
   identical boards is made.
2. X_E eventually executes standard104 forward.
3. I(X_E) eventually executes standard104 forward, where
   I(B,p,h)=(B,p-d_h,h+2). Thus the actual negative-time tail of X_E is the
   corresponding exact reversed standard behavior. It is not asserted that
   the negative-time physical turn letters themselves equal forward W104.

Here headings N,E,S,W are 0,1,2,3, and d_h their unit vectors. The original
complete field is never erased or discarded. There is no bound on the mass
of its intermediate states. All twelve additions are specified before either
virtual forward evolution begins.

The retained one-sided four-cell completion does not already give this result:
a second reverse port could intersect the first infinite forward read set.
The new ingredient is an exact six-cell port into either chosen outward
quadrant, followed by disjoint-quadrant routing of the two opposite-sector
first exits.

## 2. Imported gate and its exact width-two bound

The retained four-cell port starts at (0,0),E with

    G={(0,-1),(1,1),(1,3),(2,2)}.

Its complete physical run stays in x>=0. After 182 reads it is at (5,1),E,
and executes the certified literal standard104 with full drift (2,2).
The full gate read set, AND its four initially black cells, satisfy

    x>=0, y>=-2.                                             (1)

To verify the extra y bound, inspect its 182 transient reads and one complete
104-read tail period. Their minimum y is -2. Later periods add (2,2), so their
y coordinates only increase. The four gate cells have y>=-1. This is an
all-future conclusion from the exact retained tail theorem, not a long-run
simulation assertion.

The fresh checker separately reconstructs the gate and validates its infinite
tail by exact phase-ray overlap thresholds without importing the author's
period oracle. It checks (1) directly on the finite transient and one period.

After rotation, if g is the gate's incoming unit heading and left(g) is the
counterclockwise unit tangent, all gate seeds and reads have coordinates

    a*g+b*left(g), with a>=0, b>=-2,                          (2)

relative to its launch point. Its eventual full drift is 2(g+left(g)).

Imported source: ../sources/kehao95-core/four_cell_port/PROOF.md, Theorem 2
and its complete-field infinite-tail certificate. Rotation here is a genuine
quarter rotation, never a reflection or a background color complement.

## 3. A six-black-cell port into either prescribed quadrant

At pose (e,g), choose either perpendicular unit tangent k. Let

    C(e;g,k)={e+a*g+b*k : a,b are nonnegative integers}.

There is a seed of exactly six black cells, contained in this quadrant, whose
entire forward READ/SEED set is contained in that quadrant, and whose eventual
standard drift is 2(g+k).

Case L: k=left(g). Prescribe the four-read word LRLR. Its successive reads are

    e, e+k, e+g+k, e+g+2k,

and its exit pose is (e+2g+2k,g). Initialize e and e+g+k black; the other two
reads are white. Attach the rotated four-cell gate at that exit pose. Every
strict-prefix read has g-coordinate at most 1, whereas the gate has
 g-coordinate at least 2, so its initial field is disjoint from every prefix
read. By (2), all gate read/seed k-coordinates relative to e are at least
2-2=0. Its g-coordinates are at least 2. Thus everything is inside C.

Case R: k=right(g). Prescribe the five-read word RLRLR. Its successive reads
are

    e, e+k, e+g+k, e+g+2k, e+2g+2k,

and its exit pose is (e+2g+3k,k). Initialize e+k and e+g+2k black. Attach the
rotated gate with heading k, for which left(k)=g. Every strict-prefix read
has k-coordinate at most 2, whereas the gate has k-coordinate at least 3.
Its g-coordinate is at least 2-2=0. Again the complete read/seed set stays in C.

Both prefixes are self-avoiding, the two prefix black cells and four gate
black cells are distinct, and all requested initial white cells are left
white. First-difference induction therefore proves the stated full paths;
there are no unrecorded changes or head relocations. Standard entry is after
186 or 187 reads, respectively, from the quadrant-port launch.

## 4. Two distinct square exits admit disjoint outward quadrants

Let Q=[a,b]x[c,d] be an axis-aligned lattice square. A first exit from Q is
one of

    east:  e=(b+1,y), c<=y<=d, incoming g=E;
    north: e=(x,d+1), a<=x<=b, incoming g=N;
    west:  e=(a-1,y), c<=y<=d, incoming g=W;
    south: e=(x,c-1), a<=x<=b, incoming g=S.

These four outside boundary sets are disjoint: the outside diagonal corner
cells cannot be first exits by a single unit step. Therefore a first-exit
CELL determines its unique outward incoming heading, including when the last
inside cell was a corner.

Given two distinct exits (e1,g1),(e2,g2), choose tangents k1,k2 as follows.

A. Opposite sides. Choose either tangent on each side, for example left(g_i).
   The two outward normal half-planes are already disjoint.

B. Same side. Their tangential coordinates differ. Choose k1 away from e2
   and k2 away from e1 along the side. Their closed tangential half-planes
   are separated by at least one lattice unit, so their quadrants are disjoint.

C. Adjacent sides. Choose k1=-g2 and k2=-g1. Each exit is directed away from
   their common square corner. The first quadrant lies strictly outside Q
   in the g1 direction. The second quadrant has its g1 coordinate bounded
   by the corresponding coordinate of e2, which still lies inside Q's
   g1 range. These coordinate intervals are disjoint by one lattice unit.
   The symmetric g2 argument also applies.

Explicit neighboring-side table, with the reverse ordering obtained by swapping
indices:

    east + north: east chooses south; north chooses west.
    north + west: north chooses east; west chooses south.
    west + south: west chooses north; south chooses east.
    south + east: south chooses west; east chooses north.

Every quadrant stays outside Q in its own exit's outward normal direction.
This is a full read-set separation, not merely separation of final tails or
of the twelve added seeds. The closest same-side separation of one cell
and every adjacent-side corner pair are covered by these exact inequalities.

## 5. Simultaneously forcing the positive and negative futures

Use the exact retained reversor

    I(B,p,h)=(B,p-d_h,h+2), I^2=id, I F I=F^(-1).            (3)

It changes the conserved pose sector. In the convention
sigma=chi(p) for vertical h and -chi(p) for horizontal h, translating p by
-d_h changes chi and h+2 preserves its axis, so sigma(I X)=-sigma(X).
The BOARD is unchanged by I. Thus adding one set E to B gives precisely the
same board additions in X_E and I(X_E), not a complemented or shifted set.

Choose Q containing B, K, both starting poses, and every read/pose needed to
preserve the requested finite positive and negative histories. One can simply
include a sufficiently large ball before running either first-exit search.
Compute the first exits (e1,g1) of X and (e2,g2) of I X. Both searches halt by
the retained finite-domain escape theorem, even on arbitrary exterior colors.
Their exit states have opposite sectors. If their exit cells were equal,
Section 4 would give equal incoming headings too, hence equal sectors. This
contradiction proves e1!=e2.

Select disjoint quadrants as in Section 4 and add the six-cell quadrant port
in each. These twelve cells are distinct, outside Q, initially white in X,
and not read by either protected pre-exit history. Up to each first exit,
first-difference coupling preserves the original path with complete field
XOR E. After its exit, each virtual ant follows its own staircase and gate.
Its complete infinite read set stays in its own quadrant, missing Q, the
other staircase, and the other gate's entire initial seed/read set. Thus no
original interior debris or other port bit can affect it. Both virtual
forward evolutions have the certified standard tail.

Equation (3) translates the second evolution into the actual negative-time
history of X_E. This proves all claims in Section 1. If Q has n cells per
side, both virtual standard-tail entries occur by E(n)+187, where E(n) is
the retained square first-exit bound. No optimality of twelve is asserted.

## 6. Strategic consequence and the exact remaining premise

Every finite positive AND negative observation of every finite seed, including
any hypothetical noncapturing one, occurs unchanged in a genuine finite-seed
orbit with standard asymptotes in both time directions. The extra hardware is
uniformly bounded in black count; only its remote location changes.

Therefore adding reversibility, finite past data, or standard-to-standard
scattering completion to a local macro argument cannot itself close the global
gap. The construction retains one continuous physical ant, full fields and
all-future chronology, so it is not one of the teleporting resource relaxations.

Here is a concrete alternative global sufficient target, with no local macro
alphabet. Let S be the finite seeds X for which both X and I X eventually
capture standard104. For each m define

    b(m)=sup { future adjacent-bad-ten count of X : X in S, |B_X|<=m }.

Use the true inverse history for boundary windows. Every element of this
supremum has a finite count. If b(m)<infinity for EVERY m, then universal
finite-seed capture follows. Indeed, a noncapturing seed of mass m has
infinitely many such events by the retained exact renewal equivalence. For
any q, preserve a prefix containing q events in the twelve-bit completion.
The resulting state belongs to S, has mass m+12 and at least q future events,
contradicting b(m+12)<infinity.

This is a uniform scattering-complexity target over ALREADY bi-standard
orbits, not a claim that b is finite or computably bounded. It is not asserted
equivalent to the conjecture: even universal capture alone need not supply a
fixed-mass uniform event bound by the retained compactness arguments. The
known fixed-mass long-delay examples do not refute this target because their
extra length lies inside standard episodes; the known quadratic defect family
requires increasing mass. A proof must bound actual defect count, not flight
time, local cycle rank, or relaxed genealogy.

The exact missing premise is finiteness of these bistandard scattering budgets.
The twelve-bit theorem explains precisely how that premise would control an
arbitrary noncapturing orbit. No present certificate supplies it. Conversely,
finite standard-to-standard scattering tests without such a uniformity/resource
argument cannot exclude an infinite defect sequence.

## 7. Provenance and status

Prior retained work already proved one-sided four-bit completion, the exact
reversor, bounded-mass compactness/scattered rank, dense capturing finite-prefix
completions and generic reversible computability separations. Those results
are dependencies, not relabeled new claims here. The two-sided disjoint-quadrant
assembly and its uniform twelve-bit count are the candidate new lemma in this
investigation. No claim of external literature priority is made.

The checker and JSON report are check_two_sided_quadrant_completion.py/json.
They are controls for this analytic all-square routing proof, not a replacement
for it. In particular no tested radius is extrapolated to all finite seeds.
