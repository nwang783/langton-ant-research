# Recurrence and the fixed direction of grid edges

## Status

These are exact local deductions. The half-plane corollary is already covered
by prior work mentioned in `ant_global/global/record_birth.md`; it is not a
new solution step. The proof is retained to make the geometry explicit.

## Fixed input axis

At each step the ant changes square parity and heading axis. Therefore, for
each lattice cell, all its visits have the same incoming axis. One parity
class receives vertical headings and exits horizontally. The other class
receives horizontal headings and exits vertically. Every undirected grid
edge can consequently be crossed in only one direction during the orbit.

## Recurrent cells have at least three recurrent neighbours

Let R be the set of cells visited infinitely often. Let q be in R. Its read
colours, and hence its right and left turns, alternate on successive visits.

Suppose at most two neighbours of q belong to R. After some finite time all
visits to q use only those two neighbour ports. If the two ports are opposite,
both are inputs or both are outputs, so they cannot support a passage. If
the two ports are adjacent, one is an input and the other an output. Their
directions fix one turn sign. This contradicts alternating turn signs. The
case of zero or one recurrent neighbour is immediate. Thus q has at least
three neighbours in R.

## Four unbounded diagonal directions

At any q in R, at least one of its east and north neighbours is in R. Choose
one and continue. This constructs an infinite path in R on which x+y grows
by one at every step. The same construction with west/south, east/south,
and west/north gives paths on which -x-y, x-y, and -x+y grow by one.

More generally, for any linear form a*x+b*y with a,b both nonzero, choose
the two coordinate directions that increase the form. At least one remains
in R. Along the resulting path the form increases by at least min(|a|,|b|)
per step. Thus no nonempty recurrent set fits in any oblique half-plane.

It follows that an orbit eventually confined to an oblique half-plane is
transient: every individual cell is visited only finitely often. This is
stronger than leaving every finite set at least once, but it is still a
conditional result. It does not establish the required confinement.

## Exact edge toggle formulation

Take initial pose (0,0),N for the coordinate formulas. At an even cell (x,y),
assign the primal edge joining

    ((x+y)/2,(x-y)/2) and ((x+y)/2,(x-y)/2-1).

At an odd cell assign the edge joining

    ((x+y-1)/2,(x-y-1)/2) and ((x+y+1)/2,(x-y-1)/2).

A black cell means that this primal edge is present. The ant pose specifies
one endpoint and a next incident edge. Its update is:

- If the edge is absent, insert it, stay at the endpoint, and rotate the
  next-edge pointer clockwise.
- If the edge is present, delete it, cross to the other endpoint, and rotate
  clockwise from the arrival edge there.

This follows by checking the eight heading/colour cases. A bridge deletion
can leave an entire component behind. The black graph need not stay connected
or acyclic: from the blank grid, it has two components at update 6, and first
contains a cycle at update 14. These facts block a proposed root-to-head
connectivity invariant. Prior work also excludes simple monotonicity of its
component count, cycle rank, and detached loop sizes.
