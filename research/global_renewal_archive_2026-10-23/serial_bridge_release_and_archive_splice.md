# Serial bridge release and exact archive splicing at renewals

23 October 2026. A full-board graph theorem for ordinary Langton dynamics.
This extends the signed old-bridge zipper theorem, not standard104 capture.
The bridge-block graph facts themselves are standard elementary graph theory;
the active-cursor splice and following-zipper restrictions are their application
here. No claim of literature novelty is made.

## 1. Preserve the actual state

Fix the w BLACK diagonal lattice of the actual trajectory. Every physical R
inserts an edge incident to the stationary w vertex. Every L deletes its
current edge and crosses it. The opposite z BLACK graph is retained too,
as are the physical pose and the coordinates of EVERY edge in both graphs.
A cycle-erasing update means an L nonbridge deletion in either complete graph.

For a finite black graph, delete its bridges and call the resulting connected
components **bridge blocks**, including isolated vertices as needed at ports.
Contracting these blocks gives a forest. Each block in our state still stores
its COMPLETE embedded vertex/edge graph, every bridge's actual attachment
vertices, and the current physical cursor and port. This is a canonical
reorganization of the full board, NOT a finite boundary summary. In particular
one cannot route through a contracted block without knowing its actual edges.

## 2. A cycle erasure exposes only one serial bridge chain

**Serial release lemma.** Let an actual L delete a nonbridge e={u,v} in the
full current w graph, moving w from u to v. All previously present bridges
remain bridges. The newly created bridges in the graph without e lie on
ONE path in its bridge-block forest: the path from v's block to u's block.
They are exactly that path's bridge edges, hence have a unique linear order
from the arrival side v. Intermediate bridge blocks retain their full graphs
and all old off-path subtrees. Only the old block containing e can split;
no remote block changes.

Proof. A new bridge f was not a bridge before deletion. Restoring e must
remove its bridge status, so e joins the two components of (G-e)-f. Thus f
separates u and v. Conversely, a bridge of G-e separating u,v cannot have
been a bridge of G, because the restored e bypasses it. In a forest the
bridges separating two marked blocks are exactly their unique connecting
path. An old bridge has no bypass before deletion, and removing another edge
cannot create one. This proves every claim, including retention of branches.

Equivalently every new bridge lies on EVERY old e-bypass path. An arbitrarily
branched old bridgeless block does NOT release an arbitrarily branched set of
new bridges in one erasure: the new fuel is serial.

**Following zipper restriction.** Stop just before the next cycle erasure in
EITHER black graph. During the intervening actual erasure-free interval, the
newly exposed bridges consumed by L updates are a PREFIX, possibly empty,
of the above ordered chain. Once the w cursor leaves that chain into an old
side branch, it cannot return to any later chain edge during this interval.

Proof. The signed old-bridge zipper theorem says w follows one vertex-simple
path of bridges of the entire state immediately after the erasure. Its image
in that state's bridge forest is a simple path starting in v's block. Such
a path uses a prefix of the v-to-u chain, and after a side-branch exit cannot
return. The prefix can be empty even when the chain is nonempty: moving to
a different attachment vertex THROUGH a nontrivial block would itself require
a nonbridge deletion and is not allowed in this interval. Subsequent R writes
cannot manufacture a detour: if an L remained a bridge, its exact far-side
inheritance leaves all new attachments on the departed side. If an R makes
a needed chain edge nonbridge, crossing it would end this erasure-free phase.

This is a restriction on repeated renewals beyond their mere occurrence.
It does not bound the LENGTH of the newly exposed chain by a constant.

## 3. Exact elementary changes of the decorated archive forest

An R with endpoints in DIFFERENT old components joins their two decorated
bridge trees by the new bridge. An R with endpoints in ONE old component
creates one cycle, and contracts EXACTLY the bridge-tree path between its
endpoints into one new bridge block. All off-path bridge subtrees and all
embedded edges remain. This follows by the same separating-endpoints proof:
an old bridge loses bridge status exactly when the new edge bypasses it.

An L bridge deletion cuts one bridge-tree edge and retains both pieces,
marking the piece at the arrival vertex active. An L nonbridge deletion is
the serial block expansion of Section2. Apply the same exact rules in the
opposite lattice at every physical update. Thus the full archive is a PAIR
of decorated embedded forests with their shared physical color bits and the
continuous head. Archives are not discarded and need not be last-in-first-out.
Overlapping later path contractions can reactivate older off-path archives.

This supplies a canonical stateful path-contraction/path-expansion calculus.
It is not an independent finite-state automaton: removing the block interiors,
bridge attachment vertices, the opposite graph, or the continuous head loses
information needed for future routing.

## 4. Complete compressed blocks sharply restrict archive import

Consider a complete physical R^r L block that starts IMMEDIATELY AFTER an L.
The incoming edge at stationary w=v has just been removed and is absent.
The rule scans clockwise at v. Therefore r is0,1,2,or4, NEVER3.
The r=4 case starts at an isolated v; the fourth R completes the star and
the L removes/crosses its first inserted edge. These local facts are retained
in tait_cursor_and_loop_surgery.md; the full-component consequences follow.

For r<=2, let C be the COMPLETE block-entry component at v and e its departure.
Then e belongs to C at entry. Remove e from the entry graph and retain all
resulting components, including isolated marked vertices. The r new arms all
join the root piece at v to components at their far endpoints.

* If e is still a bridge at the actual L, the post-L active graph is EXACTLY
  the old far component of C-e. All new arms and attached full archives stay
  on the departed side, including any cycles among them.
* If e is a nonbridge at the actual L and e was already nonbridge at entry,
  both endpoints were in the same component of C-e. The active output is
  C-e together with the r arms and every full external component they touch.
* If e was a bridge at entry but nonbridge at the L, at least one new arm
  MUST land in the old far component of C-e. Otherwise the arms supply no
  bypass of e. On such a return, the output contains both old sides, all
  r arms, and all other full components touched by those arms.

There is a sharper uniform import bound: EVERY w-nonbridge L block with
r<=2 imports at most ONE genuinely external block-entry component into the
active output. For r=0 this number is zero. For r=1 it is at most one
trivially, and if its sole arm must restore an old bridge there is no external
import. For r=2 the block-entry degree of v is EXACTLY1: its incoming edge
and two scanned ports are absent. Hence e is an old leaf bridge; one of the
two arms must return to its far component, leaving at most ONE other arm
for an external component. A whole archive imported through one arm can
have unbounded mass and internal complexity.

For r=4, let u be the arrival endpoint of the first arm and C_u its FULL
block-entry component (possibly the isolated u). The other three arms remain
black after the L. Exactly two cases exist:

* None of these arms reaches C_u. The departing arm is a bridge, and the
  active post-L state is EXACTLY C_u unchanged. The new three-arm star and
  every component it touches remain behind.
* At least one of the remaining arms reaches C_u. The departing arm is a
  nonbridge. The active output is the remaining three arms and the full
  components at ALL their endpoints, together with C_u. There are at most
  THREE distinct block-entry components: C_u and at most two other archives.

Thus a w-nonbridge renewal cannot import an arbitrary number of independent
full components in one compressed block. The isolated-star case has at most
three sources; all other proper blocks have their original active source
plus at most one external source. This is an indegree restriction on a
chronological archive splice graph, NOT an upper budget on future renewals,
archive size, ancestry, or width.

Some z-only erasures with r<=2 still obey the STRICT w-bridge inheritance
law. They release topology in the opposite graph but do not themselves
reopen the active w component. Therefore it is useful to distinguish them
from genuine w-nonbridge splices and the isolated r=4 resets.

## 5. One erasure can release arbitrarily long nonstandard serial fuel

For every integer r>=1 construct the following exact finite board. In the
w lattice use integer coordinates (a,b), whose doubled physical vertex is

    (X,Y)=(2a+2b+1, 2a-2b+1).

The physical black rod {(x,0):0<=x<2r} is the staircase from (-1,0) to
(r-1,r). Close it by the lattice path through

    (r-1,r+2), (-3,r+2), (-3,0), (-1,0).

Interpret every lattice edge as its physical midpoint cell. The return path
has2r+8 edges, all physical cells have y<=-1, and the board has mass4r+8.
Its w graph is one SIMPLE cycle of length4r+8; its z graph is a forest.
Start the physical head at(0,0) facing E. The EXACT word is (LRRL)^r for
4r updates. The FIRST L is a w-nonbridge erasure, exposing one chain of
4r+7 bridges. There is NO other cycle erasure during these4r updates.
The following2r-1 L updates consume the rod-edge PREFIX of that chain.
All contained length-ten windows are nonstandard, as in the retained rod
transport certificate.

Why the claims are all-parameter: the return path is disjoint from physical
read rows y0,1, so literal turns are the established LRRL rod transport.
After removing the first rod edge, the w graph is the remaining rod/return
path. The growing upper row attaches to its rod frontier at at most one
vertex, exactly as in the retained paired-forest rod proof; the return graph
lies at doubled height Y<=-1 and cannot touch the new upper vertices Y>=3.
Thus the actual w graph is always a forest after the first deletion.
For z, the initial rod is a path and the return is a forest attached to that
path at at most one vertex per component. It cannot connect two rod vertices:
in (a,b) coordinates every white w vertex inside the simple polygon can
escape to the west along a white row, crossing its straight a=-3 boundary;
there is no finite w-white component, hence no z-black cycle by planar
duality. Return z vertices have Y<=-1, whereas new upper-row z vertices
have Y>=1; any common original rod vertices are just the retained old
attachments. Appending these pendant return forests to the paired-forest
rod evolution cannot create a z cycle. The first L is therefore the only
erasure. A direct finite implementation checks the exact bridge chain and
full trace for r1,2,3,10,30,100; it does not substitute for this geometry.

This countercontrol rules out bounded serial release, a bounded next-phase
length after one renewal, and standard local-pattern forcing from renewal
plus paired forests. Its mass grows with r; it is not a fixed-mass or an
infinite finite-seed counterexample.

## 6. Scope and targeted controls

The author checker uses exact current full edge sets, Tarjan bridges and
literal physical updates. It checks every bridge insertion contraction,
nonbridge deletion expansion, exposed-chain prefix, and proper compressed
block splice on three standard104 periods from its13-cell seed, the explicit
one-erasure rods, and one period each of the named1564 and4352 nonstandard
waves on their ACTUAL finite prepared full fields. The long preparation is
executed with every earlier write and all remote cap/rail cells retained.
No cap, word, seed, or alignment search is performed.

The standard and nonstandard cases all obey the same exact calculus. Nothing
here proves a distinction that makes nonstandard renewals terminate. What
is now restricted is how new old-bridge fuel is released and how many complete
archive sources one local renewal can splice, while preserving the archive
state that can later return. Universal finite-seed standard104 capture is
still open.
