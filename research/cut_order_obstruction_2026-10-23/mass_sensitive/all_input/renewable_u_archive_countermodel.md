# A renewable same-root U archive: the stronger all-input relaxation control

23 October 2026. Abstract all-input resource model, not a literal recurrent
packet history or ant orbit. This refines `aged_cleanup_countermodel.md` by
making U-family count, rather than only V-family count, unbounded. It therefore
addresses the actual missing budget in signed HS, without claiming a physical
realization of the helper archive.

## Eight fixed roots and an exact update

As before, roots r=0,...,7 start at(0,10r). Process r=k mod8 at C clock k.
The family has a current main at(x,y), x=4n,y=10r. A DC-count update removes
that main and installs next main(x+4,y) plus three spares

    a=(x,y+1), b=(x+1,y+1), c=(x+2,y+1).

All installed identities are fresh. Before the next DC of that family, clear
all three original spares. On its FIRST such cleanup, use V(a,b) with outputs

    (x,y+2),(x+1,y+2),(x+2,y+2),(x+3,y+2),
    (x,y+3),(x+3,y+3),

and D(c) with output(x+2,y+3). Reserve the V outputs(x+3,y+2),(x+3,y+3) as an
archive pair; the other five outputs become permanent dormant buds.

On EVERY later cleanup, the current three spares occupy a new block at x,
and the two reserved archive inputs from the preceding cleanup occupy
(x-1,y+2),(x-1,y+3). A single U-count update removes all FIVE inputs and
produces nine outputs

    (x+i,y+2) for i=0,1,2,3,
    (x+i,y+3) for i=0,1,2,3,
    (x,y+4).

Reserve the two right-edge outputs(x+3,y+2),(x+3,y+3) for the next cleanup;
leave the other seven dormant forever. Then perform the next main DC update.
Every old original spare identity is thus retired before main continuation,
and its cell is white. The archive is renewed from outputs of the same U.
No fresh initial root, different-root co-input or silently relabelled spare
is used. The packet names here denote exact INPUT/OUTPUT COUNTS, not literal relative
packet masks: DC has1/4, V2/6, D1/1, U5/9.

## Ages, cells and the exact historical identity

Generation blocks have disjoint four-column ranges, and different families
have disjoint five-row bands. Old archive cells are removed before their
successors are installed in the next block. Current cells remain distinct.
Every produced identity that is ever consumed has C age EXACTLY8. Every
input-to-output displacement of EVERY parent of a multi-input update has
L-infinity norm at most4, including the left archive inputs to the rightmost
new outputs. Thus the same plain speed<=1/2, marginal birth-heading rule
h(k)=-k mod4, and separate first-edge convention apply.

After K main DC updates, define

    v=min(max(K-8,0),8),
    u=max(K-16,0).

There have also been v startup D updates. Exact live mass and historical
rank are

    r(K)=8+3K+4v+4u=8+3K+4max(K-8,0),
    c(K)=8,
    beta(K)=v+4u.

Each U consumes five identities already in the SAME historical component.
It therefore adds exactly four independent reconvergence units. All complete
ancestor-root sets stay singleton. Both U count and beta grow without bound.
Every current cell remains within K/2+4 of its own root and hence within the
numerical LB radius floor((2K+13)/3). The initial root segment is fixed.

## Even a planar bounded-width graph is insufficient

The historical graph is no longer a cactus. Contracting identity vertices
of degree two displays, in each root component, a one-sided ladder: a main
DC chain, a helper U chain, and rungs from each source DC to the helper that
clears its three spares. The rung consists of three parallel subdivided edges;
the helper-chain link consists of two parallel subdivided archive edges.
The startup V/D vertices are finite initial decorations, and all unused
outputs are pendant leaves. Draw the two rails horizontally, the rungs
vertically, and the parallel arcs narrowly alongside them. This proves
abstract planarity and bounded strip width. It does NOT respect the stated
cell coordinates or any literal footprint.

Each component has only one infinite UNDIRECTED end: deleting finitely many
vertices leaves one connected ladder tail; off-tail pieces are finite. A
second infinite directed causal rail is allowed, rather than claimed absent.
Thus finite roots, finite ends, abstract planarity, full input provenance,
bounded all-input speed, compulsory spare clearance, and a renewable helper
archive can coexist with unbounded U count in this relaxation.

## Scope

The exact physical restrictions still omitted are literal DC/V/D/U masks,
one transported five-cell core, complete RAW+marker white contexts, full
role-potential inequalities and consecutive head endpoints. In particular
we do NOT assert that a literal U can consume the specified archive/spare
configuration. Signed HS applies only to actual chronological histories;
there is no conflict with its physical U-dependent cubic bound.

This rules out an attempted U budget based only on the included resource,
ancestry and abstract-topology premises. It neither proves the physical
archive exists nor defeats a budget retaining literal chronology. Independent
review requested.
