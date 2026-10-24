# Two-sided section and topology-free hull growth

23 October 2026, 21:58 UTC. Author deduction; independent audit pending.
The signed forward section and event-interface notes are unchanged.

## 1. A new black cell outside the fixed rectangle union creates no cycle

Let a finite black board be contained in pairwise Chebyshev-distance>=2
integer cell rectangles. Let q be a white physical cell outside their union.
In EITHER diagonal black graph, adding the edge at q cannot create a cycle.

Proof: otherwise removing that new edge from a newly created simple cycle
leaves an old black path between the new edge's endpoints. All old edges of
that path must lie in one rectangle R, since edges from different rectangles
cannot even share a vertex. But q is outside R. In a coordinate in which q
is beyond R, one endpoint of the new diagonal edge is strictly beyond the
corresponding extreme coordinate of ALL black-edge endpoints in R. That
endpoint cannot meet the old path. Contradiction.

Therefore BOTH complementary white graphs retain exactly the same connected
components after this deletion of their white q edges: these white edges
are nonbridges. In particular no finite-white vertex set grows or splits.
This statement concerns a literal new edge and full current board, not the
endpoint-only XOR relaxation.

## 2. Bi-exterior checkpoints also recur in negative time

For an actual state (B,p,h), its exact predecessor is found as follows:
q=p-d_h. Toggle q. If q was BLACK in the current board, the predecessor
heading is h-1 (the undone forward turn was R). If q was WHITE, its
predecessor heading is h+1 (the undone forward turn was L). Headings here
are N,E,S,W modulo4.

Take the same fixed terminal rectangles of the CURRENT black board as in
the signed forward theorem, and suppose the current state is not bi-exterior.
Its head is in a unique R. Follow actual predecessors until a bi-exterior
state first occurs. As long as the predecessor head q remains inside the
rectangle union, only its own cell is toggled, the union still contains all
black cells, and the enclosure lemma forces every non-bi-exterior predecessor
head into the union. Cardinal unit steps cannot hop between rectangles.
Hence all such heads remain in the SAME original R.

If the predecessor head first leaves R, it is outside the whole rectangle
union. Its cell q was white, since the current board is still contained in
the union. The inverse update adds exactly one black cell there. Section1
proves that this addition creates no new black cycle in either lattice.
Every old black cycle stays in an old rectangle, none of which can enclose
either active vertex based at q outside the union. Therefore that predecessor
is necessarily bi-exterior. It is not possible to continue an alternating
finite-pocket relay backwards out of R either.

All pre-return predecessor states thus have head in R and fixed outside
field. The strict Ke clock DECREASES by at least one on each actual inverse
update. The same finite pre-return range proves termination and the same
bound as the signed forward theorem:

    tau_minus <= (|R|+2)*(3^ceil((a+b-2)/2)-1)+1.

Head displacement is at most a+b-1<=2m-1. The past return board has at most
m-k+|R| black cells if its head stays in R; if its last inverse update first
leaves R, it has at most one additional outside black cell. Thus the safe
uniform past-return mass bound is m^2+1. Already bi-exterior states use time
zero, and m0/m1 are already bi-exterior as before.

It follows that every finite-support physical orbit has infinitely many
bi-exterior states in BOTH time directions. The first POSITIVE return map
on bi-exterior complete states is therefore a BIJECTION, with inverse the
first NEGATIVE return map. Its state space still includes the whole board.
No finite quotient, monotone rank, or attraction theorem is inferred.

## 3. A genuine event distinction at the outer section

Consider a bi-exterior actual state and its current fixed black-rectangle
closure. If its white read cell p lies OUTSIDE that entire rectangle union,
then the R update is automatically an immediate bi-exterior-to-bi-exterior
step. It creates no black cycle in either lattice, by Section1. Equivalently,
both addressed white edges are nonbridges, so neither active cursor can lose
its infinite white connection when z traverses and w stays.

Thus a nontrivial section excursion can start ONLY on a WHITE cell INSIDE
an already existing black rectangle hull. Literal black-graph cycle birth
can occur only there too. A hull-expanding writer step outside all current
rectangles may merge black components, but it cannot create a cycle or
initiate an internal trapped episode.

This separates topology-free spatial growth from internal topological work
without dropping any actual head or field state. It does not say the former
is standard, nor does it bound the number of internal episodes. A single
large hull may contain sparse long rails and arbitrary unused cells, so a
bounding rectangle is not a filled prepared board or a bounded local memory.
