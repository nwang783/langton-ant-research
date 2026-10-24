# A simultaneous-white-exterior section for every finite ant

23 October 2026, 21:48 UTC. Author derivation, not independently audited.
This is an arbitrary-word global reduction, not universal standard capture.
It does not use a packet language, an assumed visit cap, or mass-only defect
budgets. It sharpens the retained one-cursor finite-white-episode reduction
by controlling alternating traps in BOTH diagonal lattices at once.

## 1. Definitions and quantitative statement

Keep the actual complete board, physical head, and heading. For headings
N,E,S,W let r_h denote clockwise rotation and define the two active vertices

    z = p + r_h(-1/2,-1/2),
    w = p + r_h( 1/2,-1/2).

The two checkerboard diagonal lattices are planar duals. A physical cell q
is the common midpoint of one edge of each lattice; the two edges cross
perpendicularly. In EACH lattice declare its edge WHITE exactly when q is
white. Thus these two white graphs are NOT complementary to one another.
The planar dual of either white graph is the BLACK graph in the other
lattice. Both white graphs have a unique infinite component because the
black board is finite.

Call a physical state **bi-exterior** if z and w each belong to the infinite
white component in their respective lattice. This tests two actual ports,
not an unlabeled black component or a frozen-loop summary.

**Theorem (simultaneous return).** Start from any finite black board of mass
m, at any actual physical pose, in either checkerboard sector. If the state
is not already bi-exterior, let tau be its first later bi-exterior time.
Then tau is finite. There is a FIXED integer cell rectangle R, computed
from the entry board, and k entry black cells belonging to R, such that:

1. Every read before tau lies in R. All black cells outside R stay EXACTLY
   unchanged; none is cropped, reset, or silently forgotten.
2. If R has width a and height b, then a+b<=2k and |R|<=k^2, with k<=m.
3. Every pre-tau head lies in R, and the head at tau lies in R or one ordinary
   physical step outside it. In particular the entry-to-return L1 head
   displacement is at most 2k-1<=2m-1.
4. The return mass is at most m-k+|R|<=m^2.
5. Writing r=ceil((a+b-2)/2)<=k-1, the retained strict Ke clock gives

       tau <= (|R|+2)*(3^r-1)+1
            <= (m^2+2)*(3^(m-1)-1)+1.

   A clock-independent alternative using the established no-bounded-orbit
   theorem is tau<=4|R|*2^|R|<=4m^2*2^(m^2).

For m=0 the state is already bi-exterior, so no negative exponent is used.
The constants are deliberately coarse. No monotonicity of successive return
masses, rectangles, frozen-loop lengths, or topology is claimed.

## 2. Fixed rectangle closure, with no actual evolution suppressed

Initially give every black cell its singleton integer rectangle. Repeatedly
merge any two rectangles whose minimum Chebyshev cell distance is at most
one, replacing them by their smallest axis-aligned bounding rectangle.
Continue until no such pair remains. This terminates since each merger
reduces the number of rectangles. Any merger order may be fixed.

A terminal rectangle R has a set of k original black cells. If its width
and height are a,b, then

    a+b<=2k.

Proof: a singleton contributes a+b=2. For a merging pair, the coordinate
intervals overlap or have integer gap one, so the new width is at most the
sum of the old widths, and the same holds for height. Induction proves the
bound. Hence ab<=(a+b)^2/4<=k^2.

Terminal rectangles have mutual Chebyshev cell distance at least two. They
are disjoint, and an ordinary cardinal unit head step cannot go directly
from one to another. Every initial black cell belongs to exactly one
terminal rectangle, including those swallowed by an earlier bounding box.
No black edge in either diagonal graph can share a vertex with a black
edge in another terminal rectangle: midpoints of incident diagonal edges
have Chebyshev distance at most one.

## 3. The geometric trapping lemma

Suppose a black board is contained in a union of these fixed separated
rectangles. If either active vertex is in a finite WHITE component, its
physical head cell p belongs to one of those rectangles.

Proof: a finite white component in one planar lattice is separated from
infinity by a simple cycle of black edges in the opposite lattice. This is
the usual finite planar cut/dual-cycle fact; one can take an enclosing
simple component of the finite dual boundary. Consecutive cycle edges have
physical midpoints at Chebyshev distance at most one. Therefore the ENTIRE
cycle lies in one separated rectangle R.

If R's cell coordinates are [x0,x1] by [y0,y1], every point of the cycle has
coordinates in [x0-1/2,x1+1/2] by [y0-1/2,y1+1/2]. Each active vertex has
coordinates p+(+/-1/2,+/-1/2). If integer cell p lies outside R, then at
least one coordinate of that active vertex is on or beyond the corresponding
extreme line of this enlarged rectangle. It cannot be strictly enclosed.
At equality there is no loophole: a diagonal edge meets its extreme vertical
or horizontal line only at an endpoint, and the active vertex belongs to
the OPPOSITE checkerboard lattice, hence cannot be that endpoint. The
active vertex cannot lie on the black cycle either. Contradiction.

The lemma applies separately to z and w, whichever lattice each occupies
in the given physical sector. It does not confuse white graphs with dual
complements and does not rely on a black edge being a permanent barrier.

## 4. Confinement until the FIRST simultaneous exterior time

At the initial non-bi-exterior state, Section 3 puts p in a unique terminal
rectangle R. Assume no bi-exterior state has yet occurred. Then the current
head must be in one of the fixed rectangles as long as the black board
remains in their union. Reading a cell inside the union preserves that
containment, since only that physical cell is toggled.

Induct on actual fine updates. All pre-tau read cells are in the union.
A unit step cannot switch between separated rectangles. Thus they all lie
in the SAME initial R. If a step first leaves R, it also leaves the whole
union and its endpoint is already bi-exterior by Section 3. Hence no
alternating sequence of finite traps in the two lattices can relay the ant
out of this fixed box before a simultaneous exterior state occurs.

This proves the spatial and complete-field claims. At time tau the final
pre-tau read still lies in R, so at most |R| black cells lie there; precisely
m-k original black cells remain outside. The mass bound follows. The
L1 diameter of R is a+b-2, with one possible exit step, proving 2k-1.

## 5. Termination and the explicit strict-clock bound

The physical ant's strict integer clock at any chosen integer center c is

    Theta_c = -sigma * sum_black_q (-1)^(q_x+q_y) f(q_x+q_y-c)
              + J(p_x+p_y-c, epsilon(h)),
    f(v)=3^|v|-1,
    J(v,e)=f(v)/2 if e*v>=0, and -3*f(v)/2 otherwise.

Every actual fine update increases Theta_c by at least one. This is the
retained clock theorem; the present argument does not assert its novelty.
Choose c to center the diagonal coordinates x+y of the fixed rectangle R.
Their range has width a+b-2, so |x+y-c|<=r=ceil((a+b-2)/2).

At every pre-tau state all mutable black field terms lie in R and every
head lies in R. All exterior field terms are constant and cancel. Each
mutable binary field term has range at most f(r), and the head term has
range at most 2*f(r). Therefore all pre-tau clock values lie in an interval
of length at most (|R|+2)*f(r). They cannot support more than that many
internal-to-internal updates. This both proves termination and gives

    tau-1 <= (|R|+2)*f(r).

Equivalently one may first use the finite-state/no-bounded-orbit argument,
then compare the first and last pre-return clock. Either way no assumption
of future standardness is used.

## 6. Exact global consequences and the remaining gap

Every finite-support ant has infinitely many bi-exterior checkpoints.
Otherwise applying the theorem after the last one gives a later one.
Thus universal finite-seed standard capture is equivalent to capture for
all bi-exterior finite states. Taking one ordinary physical step and then
the first simultaneous return defines a TOTAL computable Poincare return
map on this section, carrying the complete actual board and pose.

A non-bi-exterior episode cannot by itself perform arbitrary long-range
transport at fixed ENTRY mass: it is confined to the single fixed R above.
This is a spatial statement, not a uniform total-defect budget over whole
trajectories. The explicitly signed 184-cell family may pass through the
section arbitrarily many times and remains entirely compatible.

No finite boundary word, routing map, loop length, mass, topology signature,
or finite-state summary replaces R's mutable full interior in this theorem.
The return state retains it. Nor do the bounding rectangles give a permanent
pruning rule: after the return, the head may leave, write new edges, revisit
old components, and create larger enclosures. The open global question is
control of the complete sequence of bi-exterior returns. The section rules
out an endlessly alternating bounded-pocket mode; it does not make the
outer evolution standard, periodic, bounded-mass, or finite-memory.

## 7. Retained dependencies and literal controls

- paired cursor coordinates: spatial_cursor_2026-10-23/
  coupled_dual_cursors_and_gate_memory.md. The two-WHITE use here is stated
  explicitly to avoid treating its two BLACK graphs as complements.
- retained one-cursor theorem: continuation_2026-10-22/ant_continuation2/
  planar_structure/finite_white_episodes.md. That result fixes one white
  finite-vertex set until its own exit, not the simultaneous section proved
  by the rectangle closure above.
- strict clock: the same retained theorem's Section 4, and the independently
  signed clock controls in global_constraints.md.
- check_biexterior_return.py independently constructs both diagonal WHITE
  graphs by physical midpoints, performs literal ant updates, checks all
  512 masks on a 3x3 board, all 9 internal starting cells and all 4 headings,
  and also checks a blank trace and spatially separated cluster controls.
  These are convention/counterexample controls, not the all-size proof.

### Actual alternation control

The blank physical ant at tick582 has pose(7,1,S) and exterior flags
(z exterior,w exterior)=(true,false). Its next two states have flags
(false,false) and (false,true), before the first (true,true) state at
tick585, pose(7,0,E), mass73. Thus one cursor can exit its finite white
component while the OTHER remains trapped, and the identity of the exterior
cursor can switch before simultaneous return. The new conclusion is not
obtained by simply stopping at the first individual white exit. The exact
entry board and literal three-state trace are in alternating_trap_witness.json.
