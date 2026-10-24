# Why sparse low-mass returns remain a separate question

## Status

This note concerns a gap in the attempted general proof. It does not prove
pointwise divergence of the number of black cells, eventual standard
highway capture, a counterexample to either statement, or impossibility of
a proof.

The completed results in the other notes give the following facts for the
ordinary finite-support Langton ant:

1. For every fixed K, the times at which the complete board has at most K
   black cells have uniform zero upper Banach density. An explicit uniform
   power-law bound is proved in `explicit_low_mass_occupation_bound.md`.
2. On one orbit, all ant positions at those times fit in one square with
   K+2 lattice cells per side. This follows from the two-endpoint signed-cut
   inequality in `signed_cut_and_explicit_mass_bound.md`.
3. No complete centered finite-support state repeats.

The desired stronger statement is that there are only finitely many such
times, for each K. It does not follow from the three statements above or
from the compactness and invariant-measure arguments used to prove them.
The explicit model below demonstrates that distinction. It is not a
Langton-ant trajectory.

## 1. The issue with a second minimal-set argument

Let G be the centered ant map on the compact space of all binary boards and
headings. Let X_K be the closed set of boards with at most K black cells.
If one whole forward orbit stays in X_K, its closure supplies a nonempty
compact invariant subset of X_K. A minimal invariant subset then gives the
bounded-mass contradiction already proved.

Infinitely many visits to X_K give less. A convergent subsequence of those
visits has a limit in X_K, but its forward image need not remain in X_K.
The limit set of the whole orbit is invariant; its intersection with X_K
need not be invariant. A minimal subset of the whole limit set can consist
entirely of infinite-support configurations.

The measure argument has the same precise limit. An infinite orbit can
visit a closed null set at infinitely many times of density zero. Its
empirical probability measures record the density, not finiteness of the
number of visits. Counting finite-support atoms as zero therefore cannot
by itself remove sparse returns.

## 2. An explicit compact countermodel

This construction preserves finite support in both time directions. At
every finite-support state it changes exactly one board bit. It has no
periodic points, and its bounded-mass sets have uniform zero density.
Nevertheless, one finite-support orbit returns to mass one infinitely
often.

The construction uses binary sequences indexed by i>=0. One may place
these bits on the nonnegative horizontal lattice ray, with all other cells
white. A separate control bit plays the role of a finite internal state.
There is no claim that its update is the ant rule.

### 2.1 Binary addition and a change of coordinates

Let Omega={0,1}^{N_0}, with the product topology. Regard x in Omega as a
2-adic integer with least significant digit x_0. Let T add one, including
the usual infinite-carry rule T(111...)=000.... T is a homeomorphism.

Let alpha have alternating digits

    alpha_i = i mod 2.

Thus alpha=...101010 in the 2-adic convention, or alpha=-2/3. Encode x as
one control bit a and a board b by

    a = x_0,
    b_i = x_i XOR x_(i+1) XOR alpha_i XOR alpha_(i+1)
        = x_i XOR x_(i+1) XOR 1.

This map H:Omega -> {0,1} x Omega is a homeomorphism. Its inverse is the
recursive rule

    x_0=a,
    x_(i+1)=x_i XOR b_i XOR 1.

Every output coordinate of H or H inverse depends on finitely many input
coordinates. Both directions are continuous, and the recursion proves
bijectivity.

Define the countermodel update by

    G = H T H inverse.

No point is periodic: T^r x=x would imply that the nonzero ordinary integer
r is divisible by 2^j for every j, which is impossible.

### 2.2 Finite support is invariant in both directions

The board b is finite if and only if x is eventually alternating. More
precisely, its tail then agrees either with alpha or with the bitwise
complement of alpha. Adding or subtracting one changes only finitely many
digits of every eventually alternating sequence. Neither an all-one nor
an all-zero infinite carry can occur there. Hence G and G inverse both
preserve the set F of finite-support boards with a control bit.

In particular, this construction does not have the defect of using an
ordinary nonnegative binary counter whose predecessor of zero has infinite
support.

### 2.3 Exactly one board bit changes per finite-support update

Let r be the least index for which x_r=0. Addition of one complements
x_0,...,x_r and changes no later digit. In the adjacent XORs defining b,
the two changes cancel for every i<r. Only b_r changes. The control a also
changes.

Thus the complete black mass M=sum_i b_i changes by exactly +1 or -1 at
every finite-support state.

The update also has a direct description in board coordinates:

* If a=0, flip b_0 and replace a by 1.
* If a=1, let k be the first white board bit. Flip b_(k+1) and replace a
  by 0.

The second rule leaves b_k white, so its inverse can identify the same k.
For an all-black infinite board the second rule leaves the board unchanged
and changes a; this is the image of the infinite-carry case above.

The control-plus-mass parity a+M modulo two is invariant on F. This is a
useful additional parallel with a phase invariant, although it is not the
ant's full heading invariant.

### 2.4 Infinitely many explicit returns to one black bit

Start at x=alpha, which is the empty board with a=0. For j>=0 put

    m=2j+1,
    n_j=(2*4^j+1)/3.

The first m bits of alpha have integer value

    r_m=2*(4^j-1)/3.

Complementing those m bits changes that finite prefix by

    (2^m-1)-2*r_m = n_j.

Therefore x=alpha+n_j is obtained from alpha by complementing precisely
its first m bits. In the board coordinates, the adjacent XOR differences
cancel everywhere except at the end of this block. Consequently

    G^(n_j)(a=0,b=empty) = (a=1, b={2j}).

The times are

    1, 3, 11, 43, 171, ...,

and tend to infinity. The mass is exactly one at each of them. The complete
states are distinct because the single black bit moves farther out.

### 2.5 The same compactness and measure conclusions still hold

For fixed K, the set

    X_K = {(a,b): sum_i b_i<=K}

is closed and countable in the compact state space. Since G has no periodic
points, every invariant probability assigns zero mass to each point of
X_K, and hence to X_K itself. If arbitrarily long orbit intervals spent a
fixed positive fraction of their observations in X_K, their empirical
measures would have an invariant weak limit assigning positive mass to this
closed set, by the same Portmanteau argument used for the ant. This is a
contradiction.

Thus the number of visits to X_K has uniform zero density, over all initial
states and all observation intervals, although the displayed orbit has
infinitely many visits to X_1. The same statement implies that interval
averages of the complete black mass tend to infinity uniformly.

One can give the countermodel a dummy position which is always the origin.
All its low-mass positions then lie in a single square, and any upper bound
on displacement in terms of endpoint masses holds trivially.

There are also computable strict integer clocks on its finite-support
orbits. If the tail of x agrees with alpha, write x=alpha+q with q an
ordinary integer; if it agrees with the complement alpha_bar, write
x=alpha_bar+q. These two tail classes are disjoint because
alpha-alpha_bar=-1/3 is not an ordinary integer. Define the clock to be q.
Each update increases it by exactly one. This observation concerns clocks
in general, not the specific signed local coefficients of the ant clocks.

### 2.6 What the countermodel does and does not show

The model rules out a purely formal upgrade from the established compactness,
no-repeat, one-bit mass-change, and zero-density conclusions to pointwise
mass divergence. It does not refute pointwise divergence for Langton's ant.

One violated Langton premise is unit-speed spatial access. When a long
initial block of board bits is black, the second rule can flip a bit
arbitrarily far from the dummy head in one update. The ant must physically
travel to every cell that it changes. The model also does not obey the
ant's local turn rule or all its exact signed-cut and clock identities.

This identifies requirements missing from the abstract argument. It does
not establish that adding locality alone would force divergence. A different
local machine could use temporary markers while walking and erase them
on its return. A successful ant proof must use enough of the actual
turning and alternating-color chronology to exclude its own version of
that process.

## 3. A precise sufficient return criterion

Here is one sufficient statement that would close pointwise mass divergence
if proved for the ant. It remains unproved.

For every finite initial state and K, suppose there is a finite R such that
whenever s<t are successive times of mass at most K, every ant position
between s and t is within L-infinity distance R of p_s.

If there were infinitely many low-mass times, all their positions already
lie in one fixed square of side K+2. The proposed condition would place
every intervening position, after the first such time, in that square
enlarged by R. All later toggles would be confined there. Exterior colors
would remain fixed. Only finitely many complete states would then be
possible, so one would repeat, contrary to unboundedness.

Thus a bound on the radius of excursions between successive low-mass
returns would suffice. Neither the signed cuts nor the occupation bound
provides that radius. Its failure has not been established either.

A weaker sufficient condition would bound the total set of cells written
between infinitely many such returns, rather than each individual radius.
An ant-specific proof might use another route altogether; this is a precise
remaining implication, not a claim that this particular criterion is
necessary for capture.

## 4. The arithmetic rectangle model has now been physically excluded

The four-corner endpoint states in Section 6 of
`signed_cut_and_explicit_mass_bound.md` pass the stated row, column, and
all-center clock tests. Those tests did not construct an actual transition.

The separate defect-dynamics investigation has now supplied an exact
all-size exclusion for that particular family and pose. Its result is in
`../defect_dynamics/four_corner_family_exclusion.md`, with a finite-ray
certificate and first-contact reduction. In particular, for every n>=1,
the trajectory from its four-corner B_n has mass greater than four at
every positive time. The n=0 trajectory has just four positive low-mass
observations and never returns to the stated pose. All members are
certified to reach a standard highway.

This is useful evidence about the missing chronology in that chosen family.
It does not invalidate the family as an endpoint countermodel, and does
not classify other placements of a bounded number of remote cells.

## 5. Remaining conclusion

The targeted recurrence attempt did not establish finite low-mass returns.
It did produce an explicit example showing why the current topological
argument cannot be strengthened by recurrence alone. The companion note
`transverse_clock_residue.md` proves a restriction on one proposed physical
return mechanism: a same-sector periodic front cannot cleanly erase a
standard wake, and confinement of its final residue to a fixed transverse
strip forces a linear number of residual black cells. Unbounded transverse
export of clock weight remains outside that restriction.

These are scoped deductions and obstructions to particular proof steps.
They do not settle the full finite-support highway conjecture or show that
it is unsolvable.
