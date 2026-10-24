# The minimal affine-particle stationary target has rectangular velocities

23 October 2026, 04:14 UTC. Analytic construction-target reduction
independently signed after review of the near-axis dominance, fixed-strip,
and row/column residue arguments. This is NOT an actual ant mechanism or an exclusion
of the rectangular residual. The inherited four-corner clock example already
shows that the endpoint conditions can be mutually compatible.

## Conditional statement

Suppose one actual finite-seed ant has increasing checkpoints t_r with:

1. One fixed physical position and incoming heading at every checkpoint.
2. B_(t_r)=C union {r v_i+b_i : 1<=i<=4}, where C is a fixed finite black set,
   each v_i is a nonzero rational vector, and the four displayed lattice cells
   are distinct and outside C for all sufficiently large r.
3. t_r >= c lambda^r eventually, for constants c>0 and lambda>1.

Passing to a residue class clears all rational denominators and fixes every
particle's checkerboard color. Then the four velocity vectors MUST be the
four distinct corners of a nondegenerate axis-aligned rectangle. Their
checkerboard colors alternate around that rectangle, with the northeast and
southwest velocity corners having the favorable color for the NE/SW clocks.
The origin belongs to the closed velocity rectangle; it can lie on an axial
boundary, which is not excluded here.

If all four extremal coordinate velocities are nonzero, the actual four
particle positions, not merely their velocities, must eventually form an
axis-aligned rectangle with odd side lengths. Zero coordinate velocities
allow fixed-row/column residue exceptions and are left explicit.

The same proof excludes fewer than four moving particles. A stationary core
of arbitrary fixed size does not change the argument.

## 1. Every non-axis one-sided clock diverges at the checkpoints

Use the signed one-sided exponential clocks from
sources/kehao95-core/wake_synthesis/PROOF.md, Section9. In a NE frame, for
positive u,v and a sufficiently large lambda, the field weight is

    w(x,y)=exp(lambda*(u x+v y)),

and the clock has field term -sigma sum_B chi(q)w(q), a bounded fixed head
term, and literal increment at least kappa*w(p)>0. Quarter rotations give
every non-axis normal. Their sector sign flips at each odd quarter rotation.

Although the lower bound is not uniform over arbitrary positions, the pose
at every checkpoint is fixed. The update immediately after each checkpoint
therefore contributes the SAME positive lower bound. These updates are
pairwise distinct. Thus every such clock tends to positive infinity along
this checkpoint sequence, not merely monotonically to a finite limit.

The fixed core and fixed head contribute constants. Consequently, for every
normal in the NE/SW open quadrants the asymptotically leading particle sum
must have the NE/SW-favorable checker color; in the NW/SE quadrants the
favorable color is the opposite one. With the normalized sector sigma=+1,
NE/SW favors chi=-1 and NW/SE favors chi=+1. A negative leading coefficient
would send the clock to negative infinity. If all relevant exponential rates
are nonpositive, the clock would instead stay bounded. Both are impossible.

## 2. The velocity hull cannot be a point or a line

If the affine line containing all velocities does not contain the origin,
a linear functional is a fixed nonzero constant on that line. All moving
particles in two successive sufficiently late checkpoint fields then lie
strictly on one side of the fixed pose. Their complete XOR is on that side,
since the core cancels. This contradicts the signed closed-pose identity

    conv(all read positions) = conv(complete XOR).

The same separation applies to a single nonzero velocity.

If the velocity line contains the origin, all particle positions and the
fixed core lie in one fixed-width strip parallel to that line. Compare one
fixed initial checkpoint with the r-th one. Their complete XOR, and hence
by the endpoint-inclusive hull theorem the whole intervening path, lies in
a strip segment of length O(r) and fixed width.

For an oblique strip the signed one-coordinate clock already bounds the
interval uniformly, since the complete XOR has bounded cardinality and all
normal weights are bounded. For an axial strip the signed fixed-height
rectangle escape theorem bounds the duration by a fixed polynomial in r.
Either contradicts t_r-t_0 growing exponentially. Thus the velocity hull
is genuinely two-dimensional.

## 3. Four particles force the rectangular velocity hull

Let xmax and xmin be the largest and smallest x velocities. They differ,
by Section2. For normals proportional to (1,epsilon) with positive and
negative epsilon arbitrarily close to zero, only the particles with x=xmax
can be leading: the finite gap to all other x velocities dominates for
sufficiently small |epsilon|.

The favorable checker color switches across epsilon=0. If every particle
at xmax had the same color, its leading coefficient would have the wrong
sign on one side (or all rates would be nonpositive and the clock bounded).
Thus BOTH colors occur at xmax. The identical argument at xmin, ymax and
ymin gives both colors at each of the four coordinate extremes.

Since xmax and xmin are disjoint groups and there are only four particles,
each has exactly two particles, one of each color. Likewise ymax and ymin
partition the same four particles into two two-element groups. Therefore
every velocity belongs to

    {xmin,xmax} x {ymin,ymax}.

Two particles at one velocity corner would force two at its opposite corner
by these row/column group sizes, leaving only a line, contrary to Section2.
So there is exactly one particle at every corner. Looking at normals strictly
inside each quadrant now fixes the alternating checker colors stated above.

If the velocity rectangle did not contain the origin, some non-axis normal
would have strictly negative projection on all four velocities. Its clock
would be bounded. Therefore the rectangle contains the origin. Axis equality
is possible because the clock family excludes exactly axis normals.

## 4. Nonzero coordinate speeds align the actual particle rows and columns

Fix a row whose y coordinate tends to infinity in magnitude along one of the
particle tracks. It is eventually outside every initially nonwhite row and
the fixed checkpoint head/core rows. Its alternating black sum is zero
modulo4 by the signed row-charge invariant.

At that y velocity there are exactly two possible particles. If their affine
y offsets differed, each occupied moving row would contain a single black
cell, contradicting the zero residue. Their y offsets therefore coincide.
The two particles then have opposite x parity, because their row sum is zero
modulo4. Apply this to both nonzero y speeds and, after rotation, both nonzero
x speeds. The four actual particles form one rectangle, and both side lengths
are odd. This argument does not silently apply to a zero-speed row or column:
its conserved residue can retain information from the initial finite seed.

## 5. Why this is useful, and what it does not prove

The separately signed finite-valued rational-series result in
computability/finite_power_exact_validator/bounded_particle_structure.md gives
finite affine particle tracks for genuine bounded-charge checkpoints in a
finite-power spatial refinement. Uniform substitutions supply exponential
checkpoint times. Hence a candidate with the minimal four moving particles
cannot evade the existing rectangular construction target by choosing a
triangle, oblique quadrilateral, or two nonparallel one-dimensional pairs.
Larger moving-particle sets and zero-speed side exceptions remain possible.

This does NOT prove that any rectangle can actually be renewed. The known
four-corner static chain passes endpoint charges and clocks but is not an
orbit. A core consisting of the current read cell is additionally impossible
for recurrent mass-five checkpoints: the next L read deletes it, leaving
mass four infinitely often, contrary to the signed eventual-mass>=5 theorem.
Off-head singleton cores and larger fixed cores need genuine chronology.
