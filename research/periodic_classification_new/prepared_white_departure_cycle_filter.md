# Input-white first-departure cycles in prepared translating fronts

23 October 2026, 11:56 UTC. Scoped analytic corollary candidate for audit.
This does NOT import a white-front exclusion into prepared-input synthesis.

Take a COMPLETE bi-infinite translating front with an arbitrary prescribed
periodic INPUT coloring and finite complete physical visits per cell. Its
actual full drift is d!=0, event period P, and first physical times satisfy
T(v+d)=T(v)+P. Some first reads may be L. There is no initial head.

Restrict b(v)=target of the first departure to active classes whose INPUT
bit is WHITE, hence whose first read is R. Stop b when its target is input
BLACK. Inactive classes have no b-edge. This is a PARTIAL functional graph.

Every quotient cycle ENTIRELY within the input-white domain must have
winding MINUS ONE. Proof: at a cycle R corner, first-R outgoing/incoming
port ordinals give first-time increment+1; at a L corner the incoming
heading is opposite its first heading and first time decreases by at
least3. An essential simple circle therefore has negative winding, hence
exactly-1. Counterclockwise finite cycles contradict the same time sum.
For a clockwise finite cycle, take all ACTIVE physical cells in its closed
finite interior. They may include INPUT-BLACK cells. Every such interior
cell still has an actual older first-read predecessor; the boundary's
first-R geometry makes the whole set predecessor-closed. With no initial
head, its oldest time is impossible. Thus winding0 and+1 are excluded.

Unlike the all-white theorem, the partial graph may have NO cycle at all:
its white trees can terminate at periodic input-black classes. Do NOT
require a negative cycle or impose the white-front speed/growth bounds.
There is no numerical finite-root budget because the prepared physical
input can contain infinitely many black translates.

## Finite synthesis cuts, if desired

For a fixed supplied finite cylinder, enumerate simple directed cycles
using only input-white classes and the geometry-allowed first-R departures.
For every cycle with winding0 or+1, forbid the conjunction that all its
cells are active and each first heading selects the corresponding outgoing
edge. It is enough to include these finite necessary clauses; source and
target event ordinals or full chronology must still be enforced elsewhere.

An input-black cell in the candidate cycle INVALIDATES this white-boundary
lemma; do not emit that clause. Input-black cells merely inside the Jordan
region do NOT invalidate it. Never use a primitive quotient to compute the
winding. This is a possible solver optimization, not a front exclusion or
an implemented/independently tested encoder change.
