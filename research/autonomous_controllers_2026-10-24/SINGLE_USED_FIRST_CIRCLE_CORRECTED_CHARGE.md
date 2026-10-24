# Corrected full-fibre charge for a single-used first-R circle

24 October 2026. Author all-cap conditional theorem, submitted for independent
review. No visit, period, or support-width cap is assumed. The existence of a
single-used first-R circle is an EXPLICIT hypothesis, not a general property
of first-R departure cycles.

## Complete hypotheses and vertex inventory

Let a complete WHITE translating front have actual full drift d=(a,b), growth
g equal to its number of odd complete-history classes, and first-R-departure
map F. Let C be a quotient F circle whose physical cycle edges each have total
use ONE. By the independently signed single-used first-circle lemma29cce94f,
C is simple, embedded, essential, of winding -1; every geometric RIGHT corner
is a singleton, and every LEFT corner is a triple A,A,-A or a quadruple
A,A,-A,A. Its other used ports and all other read support lie on its right.
The quadruple's R2-to-L3 lifetime is retained, not reassigned to its F edge.

Write ell=|C|, let Q be its set of quadruple vertices and k=|Q|. The odd classes
on C are exactly C minus Q, of cardinality ell-k. Let O' be all odd classes
outside C, so |O'|=g-(ell-k). O' is not asserted to be a physical wake.
Checker sign chi=(-1)^(x+y) is well-defined on full-drift classes because a+b
is even. Unread exterior fields do not enter this partition and are not erased.

## Exact cancelled full-circle sums and the missing endpoints

The vertical C edges perfectly match ALL C vertices, and each matched pair
has opposite checker sign and equal x residue modulo |a| when a!=0. Therefore
C's complete signed sum is zero in every such x fibre. Horizontal edges give
the corresponding exact zero sum in every y fibre modulo |b| when b!=0.
For a zero drift coordinate the same cancellation holds on each physical
column or row, but no nonzero-coordinate residue obligation is claimed there.

Define q_x(r)=sum chi(v) over quadruples v in x fibre r, and likewise q_y(s).
Removing those EVEN-output vertices from the full cancellation gives exactly

    signed sum of O intersect C in x fibre r = -q_x(r),
    signed sum of O intersect C in y fibre s = -q_y(s).

The signed full-front residue theorem requires the full odd inventory's sum
to be 2 modulo4 in every fibre of a nonzero drift coordinate. Consequently
O' must supply 2+q_x(r) modulo4 in each x fibre, and similarly for y.
Define f(z)=min_{n integer}|z-4n|, and set

    Phi_x = sum_r f(2+q_x(r)) if a!=0, otherwise 0,
    Phi_y = sum_s f(2+q_y(s)) if b!=0, otherwise 0.

Every residual odd class supplies one signed unit to each applicable fibre.
Hence the exact separate-fibre deficit bound is

    g >= ell-k + max(Phi_x,Phi_y).                         (1)

The arrays q_x,q_y use FULL supplied-drift fibres; no primitive quotient,
reflection, deletion of an even helper, or balanced-wake assumption is made.
The bound is necessary; joint x/y/sign compatibility can be stronger. We do
not claim that (1) is attained or is the optimal combined transportation bound.

## A simple uniform correction, and triple-corner consequence

Since f(2)=2 and changing its integer argument by one changes f by at most one,

    Phi_x >= 2|a|-k,       Phi_y >= 2|b|-k.

The zero-coordinate convention also obeys the corresponding inequality.
Writing D=max(|a|,|b|), (1) implies

    g >= ell+2D-2k.                                      (2)

For k=0 this is exactly the earlier E-circle charge ell+2D, not a new
zero-output-front exclusion. The correction accounts for each missing odd
endpoint twice: once in the circle's odd population, once in the residual
fibre demand. It does not add overlapping event-time bounds.

An embedded essential rectilinear circle in the flat translation cylinder
has total turning zero. One elementary justification is to take a parallel
straight core outside its compact normal range. They bound an annulus; cut
that annulus along a simple transversal. The planar boundary turning formula
has cancelling contributions along the two copies of the cut, and its cut
corners contribute the full disk turn, leaving zero turn along C. Thus C has
ell/2 RIGHT and ell/2 LEFT corners. (A contractible circle would instead have
turning +4 or -4 quarter-turns; it is not the present case.)

If tau is the number of triple left corners, k=ell/2-tau. Equation(2) becomes

    g >= 2D+2*tau.                                      (3)

At g8, D=3 therefore permits at most ONE triple left corner on such a circle;
D=4 permits NONE. These are conditional restrictions, not existence claims.
The exact array bound(1) may further reject a placement with those counts.

## Finite geometric scope without a period or exterior cap

Each of the ell/2 right corners is a distinct singleton odd class. Therefore

    ell/2 <= g,             ell <= 2g.                  (4)

At g8 any such circle has at most16 edges, despite completely unbounded higher
traffic, period and transverse read support. Its geometric lift advances by
-d, so ell>=2D; its alternating horizontal/vertical steps also give the usual
coordinate parity restrictions. In particular full d=(3,1) allows only
ell=6,10,14 within this bound.

Equations(1)--(4) justify a FINITE conditional circle-shape/quadruple-placement
cover. They do not justify a finite cover of all fronts unless a separately
proved boundary theorem forces a single-used F circle. That forcing is now
signed only for the full-diagonal g8 situation in2cd87bff; arbitrary F circles
can have multiply-used edges, and no general one-use assertion is imported.

## Evidence and dependencies

Proof dependencies: SINGLE_USED_FIRST_CIRCLE_MIDDLE_READ_INTERFACE.md29cce94f
and its independent report01d7c9dc; the exact matching argument in
EXTREMAL_CYCLE_RESIDUE_CHARGE.md8716dd22/reportbf9f530b; and Section2.3 of
../sources/kehao95-core/wake_synthesis/proof/periodic-growth-closure.md (existing
attribution retained). The present result makes no literature novelty claim.
No historical width-ten computation, cap-four terrain theorem, or solver
status is needed. Independent review of this corrected formulation is pending.
