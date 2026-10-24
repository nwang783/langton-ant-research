# Exact fine-step active-vertex and edge-toggle formulation

23 October 2026 17:37 UTC. This is an exact coordinate reformulation of the
physical ant and its five-cell marked core, not a historical incidence
embedding or a component-merger theorem.

Let the physical head be p with heading index h, and define

    z = p + rotation_h(-1/2,-1/2).

The fine-step sector sigma = p_x+p_y+h modulo two is invariant. Let V_sigma
be the half-integer checkerboard lattice whose vertices satisfy

    z_x+z_y = sigma+1 modulo two.

Its nearest-neighbor edges have diagonal vectors (+/-1,+/-1). Every physical
cell q is the midpoint of exactly one such edge: its endpoints are
q +/- (1/2,1/2) when q_x+q_y=sigma modulo two, and q +/- (1/2,-1/2) otherwise.
Treat a black physical cell as an occupied edge and a white cell as absent.
This is a bijection between physical color configurations and edge subsets.

At head (p,h), the currently inspected edge is incident to z and points along

    d = rotation_h(1,1).

Direct substitution in the actual fine-step rule gives:

- L at black p: delete this occupied edge, leave z FIXED, and rotate the
  inspected-edge direction counterclockwise by 90 degrees.
- R at white p: add this absent edge, traverse it from z to z+d, and rotate
  the inspected-edge direction clockwise by 90 degrees at the new vertex.

The physical cell read is exactly the midpoint of the traversed/removed
edge. The ant uses the BEFORE color, then toggles it. This formulation must
not confuse the pre-flip routing with the stored post-flip edge field.

## The marked core has explicit separate ports

At a marked full or atomic cut, the four core cells

    p+rotation_h{(-1,-1),(-1,0),(0,-1),(0,0)}

are exactly ALL FOUR occupied edges incident to z. The fifth core cell,
p+rotation_h(1,0), is the edge from z+d to z+d+rotation_(h+1)(1,1).
Thus the marked five-cell core is a full occupied star with one extra edge
at the first neighbor. The core is a transported courier, NOT a residual
incidence component. Assigning it one historical root label would falsely
join separate residual components.

The first four L reads delete the full star while z stays fixed. The next R
adds an edge and traverses to its neighbor. Subsequent raw switches construct
the next marked star. This gives a literal port-level description of the
core-to-residual exchange, rather than an arbitrary geometric genealogy wire.

## Why it does not already solve the open geometry

The true fine-step center walk is NOT the straight atomic chord. For one D,
write d=(1,1), e=(1,-1) in the entry heading frame and set its initial z=0.
Its five R traversals visit

    0, d, 2d, 2d+e, d+e, d.

There is already a four-edge closed loop at d within one D atom. Its straight
atomic chord is merely 0--d and is injective. Therefore the signed atomic
center simplicity theorem cannot be imported as simplicity of this exact
fine-step graph walk.

The D residual input at physical (0,1) is not read during the ten raw steps;
it becomes an edge in the next core star, while the next marker reads it.
This is the exact reason residual identity retirement is not synonymous with
an immediate physical deletion. The fifth core edge is deleted and then
reinstalled in the D raw path, while other newly added edges become its
output and next core. A causal ribbon must retain those distinct ports and
the ordered input/output identities through the exchange.

This active-vertex formulation survives the known disconnected-archive,
convex-hull and straight-wire countercontrols, because it asserts none of
those false historical-component invariants. It is a precise starting
language for the missing core-port update proof, not that proof itself.
