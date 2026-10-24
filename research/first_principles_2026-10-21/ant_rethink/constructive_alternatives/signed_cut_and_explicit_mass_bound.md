# Signed cuts and an explicit bound for escape from low black mass

## Status and sources

The exact signed-column potentials below are inherited from Atharva
Jillhewar's source at commit
`76a7e234e577d992d086c204c3dea00ae72cf10a`:

https://github.com/Atharva12456/langtons-ant-highway/blob/76a7e234e577d992d086c204c3dea00ae72cf10a/lean/Langton/DirectedPoseDiscrepancy.lean

The relevant definitions are `columnStep`, `exactColumnWeight`, and
`exactColumnPotential`. The theorem `exactColumn_localPotential` proves all
eight local equations, and `additiveStateCharge_run` proves conservation for
every finite run. This is not limited to equal-pose endpoints or periodic
traces. The same formulas can be checked directly as below.

Ke's `research/README.md` at commit
`22e0c9edcc566a4c2f7a9bf92f5cd05c19199617` already states the resulting distance
bound `|B_t| >= 2 max(d-1,0)` beyond the initial box:

https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/research/README.md

The uniform time bound in Section 4 is an added consequence derived here.
The switching-geometry analysis supplied the two-endpoint improvement that
removes an initially derived recursive bound. The parent analysis then used
the optimal containing square and Ke's integer clock to strengthen the
bound. Both steps were independently checked. No novelty claim is made.

## 1. The exact column invariant

Use headings N,E,S,W in clockwise order. White means turn right, black means
turn left, then toggle the current cell and move one lattice edge.

Fix an integer column c. Define, modulo four,

    chi(x,y) = (-1)^(x+y),
    a_c(x) = 1[x=c],
    G_c(x) = 0 if x<c, 1 if x=c, 2 if x>c,
    w_c(x,y) = chi(x,y)*a_c(x).

For a position p=(x,y), write a=a_c(x), G=G_c(x), chi=chi(x,y). Set

| Heading h | F_h(p) modulo four |
|---|---|
| N | chi*(-G) |
| E | chi*(G-a) |
| S | chi*(-G+2a) |
| W | chi*(G+a) |

Then the quantity

    I_c(B,p,h) = sum_(q in B) w_c(q) + F_h(p)  (mod 4)

is conserved under every Langton update.

### Direct one-step check

At a white/right step the black sum increases by w_c(p). At a black/left
step it decreases by w_c(p). The needed changes of F are therefore -chi*a
on a right step and +chi*a on a left step.

Every move changes chi to -chi. Also

    G_c(x+1)-G_c(x) = a_c(x)+a_c(x+1),
    G_c(x)-G_c(x-1) = a_c(x-1)+a_c(x).

Substitution gives the following eight differences. Entries of -3chi*a
equal +chi*a modulo four.

| Old heading | Right-step difference of F | Left-step difference of F |
|---|---:|---:|
| N | -chi*a | +chi*a |
| E | -chi*a | +chi*a |
| S | -chi*a | -3chi*a |
| W | -chi*a | -3chi*a |

For example, a right step from N moves east. Its difference is

    -chi*(G_c(x+1)-a_c(x+1)) - chi*(-G_c(x))
      = -chi*a_c(x).

A left step from S also moves east. Its difference is

    -chi*(G_c(x+1)-a_c(x+1)) - chi*(-G_c(x)+2a_c(x))
      = -3chi*a_c(x) = +chi*a_c(x) mod 4.

These checks require no time parity, common incoming axis, period, or
restriction on how often a column was visited.

## 2. A complete crossing forces two black cells in the column

If the ant is strictly left of c, G=a=0, so F_h=0 for all headings.
If it is strictly right of c, G=2 and a=0, so F_h=2 for all headings:
the signs and the checkerboard factor disappear modulo four.

Consequently, whenever the ant's two endpoint positions are on opposite
strict sides of c,

    sum_(q in B_t, q_x=c) chi(q)
      - sum_(q in B_s, q_x=c) chi(q) = 2 mod 4.

The equation holds for either crossing direction. It records the endpoint
sides, not the number of intermediate crossings.

If column c had no black cell at time s, its black checker-signed sum at
time t is 2 modulo four. Zero black cells would give 0; one would give +1
or -1. The column must therefore contain at least two black cells at t.

A quarter-turn rotation gives the identical result for rows.

### The stronger two-endpoint displacement bound

The two endpoint black sets need not be empty on the intervening columns.
Whenever x_s<c<x_t, or x_t<c<x_s, the signed sum of their difference on
column c is 2 modulo four. Unchanged black cells cancel. A single changed
cell contributes +1 or -1, so at least two distinct cells of B_s symmetric
difference B_t lie in each intervening column. Therefore

    2 max(|x_t-x_s|-1,0) <= |B_s symmetric_difference B_t|
      <= |B_s|+|B_t|.

The same inequality holds with y in place of x. In particular,

    ||p_t-p_s||_infinity <= (|B_s|+|B_t|)/2+1.

This holds for every finite interval, even if the intermediate mass is much
larger than the two endpoint masses. All positions on any one orbit whose
black mass is at most K have pairwise L-infinity distance at most K+1.

## 3. The distance bound

Let Q_0 be the smallest axis-aligned rectangle containing the initial black
set and the initial ant position. Let d_t be the integer L-infinity distance
from p_t to Q_0. If d_t>=1, choose a coordinate in which p_t is d_t beyond
the corresponding side of Q_0. There are d_t-1 integer columns, or rows,
strictly between that side and p_t. Each was initially black-free and has
the two ant endpoints on opposite strict sides. Each now contains at least
two black cells, with disjoint cells in different columns or rows. Hence

    |B_t| >= 2 max(d_t-1,0).

In particular, while |B_t|<=K, the ant remains in Q_0 enlarged in every
coordinate by floor(K/2)+1.

This already proves that black mass is unbounded on every finite-support
orbit, using unboundedness of the ant position. It also excludes a complete
finite pattern that translates with nonzero drift and bounded mass.

The statement bounds current distance beyond the initial box. It is not a
bound on distance behind a moving record or on retreat from a previous
position.

## 4. An explicit uniform time bound depending only on the mass ceiling

Ke's independently inspected square-clock proof gives first exit from any
square with n lattice cells per side by

    E(n) = [13*3^(n-1)-2n^2-4n-5]/2.

The exit move is included. Arbitrary exterior colors are allowed. Source:

https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/clock_escape/PROOF.md

Define

    U(K) = E(K+2) = [39*3^K-2K^2-12K-21]/2.

### Theorem

Every initial state with at most K black cells has more than K black cells
at some time t satisfying 1<=t<=U(K). The bound holds for all positions of
the initial cells and all headings.

### Proof

Suppose, for a contradiction, that the mass stays at most K at every time
from zero through U(K). The two-endpoint bound in Section 2 gives pairwise
coordinate differences at most K+1. Thus the complete finite list of ant
positions in this interval fits in one fixed square Q with K+2 lattice
cells per side. The square can be chosen after examining the prefix: its
placement is not used in the ant's dynamics.

No exit from Q occurs through time U(K). The first-exit clock, applied at
time zero to this square, forces exit by E(K+2)=U(K). This is a contradiction.

Thus the mass exceeds K no later than U(K). QED.

### Strength and limits

The displayed bound is exponential and far above the exact values known
at small K. Its purpose is to give a finite formula, uniform in every
coordinate of the input, rather than a compactness existence statement.

The bound does not prove that mass tends to infinity at every time. It also
does not control the number of nonstandard turns. The ant can in principle
make increasingly large mass excursions and return to low mass at sparse
times.

### An elementary finite-state alternative

Without using the quantitative clock, let n=K+2. If a trajectory remains
at mass at most K through an interval, all its ant positions fit in an
n-by-n square Q. All toggles occur inside Q. Initial black cells outside Q
stay fixed, even when there are some arbitrarily far away.

At most

    V(K) = 4*n^2 * sum_(j=0)^K binomial(n^2,j)
      <= 4*(K+1)*(K+2)^(2K+2)

complete states can occur in this interval: the external field is fixed,
and the heading, internal position, and internal black subset determine the
remaining data. Survival from time zero through V(K) repeats a complete
state. Determinism would then give a bounded periodic orbit, contrary to
the classical unboundedness theorem. Thus V(K) is a second, weaker uniform
time bound with no quantitative-clock dependency.

## 5. Why these charges do not yet give bounded retreat

For an interval whose two ant endpoints are on the same strict side of a
column, the ant-potential change is zero. Its signed black sum can return
to the same residue after arbitrary intermediate visits. A crossing and
later reverse crossing cancel in the mod-four endpoint equation. The
invariant therefore gives no accumulating penalty for repeated retreat.

In an axis-directed escape, it forces black cells in the intervening
columns. It does not bound the heights of those cells or the number of
returns across an old column.

In an oblique escape, both the row and column versions apply. A black cell
can satisfy a row requirement and a column requirement at once, so the two
bounds cannot simply be added. They still give no fixed width or fixed
upper bound on retreat.

For a path in a cone of variable width, every required column and row sum
can remain compatible with unbounded excursions inside that cone. An
additional chronological argument is needed to derive the two retreat
bounds in `bounded_directional_retreat.md`.

This is a precise limit of the displayed endpoint charges, not a proof
that no other invariant or chronological method can supply the bound.

## 6. A four-cell endpoint model passes all fixed-center clock inequalities

The following are candidate endpoint states only. No trajectory between
them is asserted. They make the remaining chronological requirement explicit.

Keep the ant at p=(0,0), heading E, and for n>=0 take

    B_n = {(-n,-n), (-n,n+1), (n+1,-n), (n+1,n+1)}.

Each row and column has two opposite checker signs. Thus all exact-row and
exact-column checker-signed mod-four sums vanish, as for an empty board at
the same pose. The ordinary row/column parity charges vanish as well.
The four black cells also preserve heading minus black mass modulo four.

These states have bounded black mass and a fixed ant pose, but their black
support has unbounded diameter. The endpoint cuts do not exclude them.

### All-center, rather than pointwise, clock comparison

Put f(z)=3^|z|-1 and L_n=2n+1. For heading E at the origin the invariant
sigma is -1. The black-field term in the x+y clock is

    H_n(z)=f(z-L_n)+f(z+L_n)-2f(z),  z=1-c.

For the quarter-turned x-y clock the same expression holds with z=-c.
The head correction is the same at the two endpoints and cancels.

For m>n, put a=L_n and b=L_m. The clock difference at either orientation is

    D(z)=f(z-b)+f(z+b)-f(z-a)-f(z+a).

This function is even. Writing r=|z| gives

| Range of r | D(z) |
|---|---|
| 0<=r<=a | (3^b-3^a)(3^r+3^(-r)) |
| a<=r<=b | (3^b-3^a-3^(-a))*3^r+3^b*3^(-r) |
| b<=r | (3^b+3^(-b)-3^a-3^(-a))*3^r |

The first expression is minimized at r=0. The middle expression increases
for integer r>=a because a>=1 and b>=a+2; subtracting its value at r from
that at r+1 gives

    2*[(3^b-3^a-3^(-a))*3^r - 3^(b-r-1)] > 0.

The final expression also increases, and the formulas agree at the two
boundaries. Therefore, uniformly over every integer clock center c,

    Theta_c(B_m,0,E)-Theta_c(B_n,0,E)
      >= 2*(3^(2m+1)-3^(2n+1)) > 0,

for both diagonal clock orientations and their reversed choices of center.

Consequently the inequalities that a putative transition of duration t must
satisfy, namely every clock difference being at least t, are compatible
with these endpoints for any t at most that positive minimum. Choosing
larger clock centers does not create a negative increment. The elementary
clock congruences can also be met by a suitable multiple-of-eight duration.

This does not prove that an actual transition exists. Joint local gain
counts, the required physical visit order, and all unchanged cell colors
remain to be satisfied. The example only rules out an inference of
pointwise mass divergence from these endpoint residues and clock
inequalities alone.

### Marginal exact clock counts also admit a nonnegative solution

There is a further exact check for the adjacent endpoint comparison n to
n+1. Let a=2n+1 and b=a+2, and define

    g(k)=3^k-1 if k>0, and g(k)=0 if k<=0,
    A_d=1 for d=-a or d=b,
    A_d=2 for -a<d<b,
    A_d=0 otherwise,
    B_d=A_(-d).

For every integer z, finite geometric sums give

    f(z-b)+f(z+b)-f(z-a)-f(z+a)
      = 32(n+1) + 4 sum_d [A_d*g(z-d)+B_d*g(d-z)].

All A_d and B_d are nonnegative integers, and both have total 8(n+1).
The right side has exactly the form of the clock's gain identity for a
putative duration 32(n+1). For this interpretation, use evenness of D to
write z=c-1 for the x+y clock, with d=ell-1 at physical diagonal level ell.
For the rotated x-y clock, use z=c and d=ell. A physical epsilon change
from + to - contributes 4*g(c-ell); thus A_d counts these changes, and
B_d counts changes from - to +. These choices reverse the earlier sign
convention for z; keeping that earlier convention would exchange the
transition labels.

One direct way to verify the identity is to put

    V(z)=sum_d A_d*g(z-d).

Its three formulas are

    V(z)=0,                                      z<=-a;
    V(z)=2*3^(z+a)-2(z+a)-2,                     -a<=z<=b;
    V(z)=2*3^(z+a)-2*3^(z-b)-2(a+b),             b<=z.

Substitute V(z)+V(-z) and use b=a+2. The middle interval between a and b
has only three integer points. An additional exact arithmetic replay checked
the identity for n=0,...,19 and z=-100,...,100 (4,020 equalities).

These are separate counts in each diagonal projection. They have not been
matched to a common sequence of headings, physical cells, alternating
colors, and intermediate boards. They therefore do not construct a
transition or a nonstandard infinite orbit. They show that even these
projected exact gain counts leave a further path-consistency requirement.
