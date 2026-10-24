# One-renewal obstruction to reusing private pendant outputs

23 October 2026. Frozen author lemma for independent review. This is a
phase-local graph/ownership bound, NOT a universal no-regeneration theorem.

## General marked-path load lemma

Let G be the COMPLETE black w graph at a proper post-L cut, including all
passive components, and let A be any marked set of its current black
lifetimes. Suppose every vertex-simple path in G contains at most mu marked
A edges. Keep every old graph/coordinate/lifetime; no components are dropped.

Execute ONE complete actual R^r L block, r<=4. Let H be the complete w graph
just after that block and A' the surviving A lifetimes. At most THREE new
R lifetimes remain in H:

- for r<=3 the departing L edge was present before the block, so at most3
  new R edges remain;
- for r4 all four ports were written, and the L removes the first written
  edge, leaving exactly3 new R edges.

Thus H is a subgraph of G plus at most3 new edges (possibly with new
vertices); deleting old edges only reduces the available path set.

Consider the following ordinary epoch, with no additional exceptional block
inside it. Exact old-bridge inheritance says its w cursor follows one
vertex-simple path P of H-entry edges. Delete from P all edges not in G.
There are at most3 of them, so the remainder splits into at most4 contiguous
vertex-simple paths in G. Each uses at most mu marked A edges. Consequently

    number of surviving A lifetimes consumed in that ordinary epoch <=4mu.

This is independent of entry ports and of how large a complete old archive
is imported by the intermediate block. Newly written ordinary-epoch arms
stay behind and cannot let P leave its H-entry path. Non-LIFO archive order,
remote passive fields and opposite-graph erasures are all allowed.

More generally, if a specified intervening operation leaves at most k new
edges relative to G (plus arbitrary deletions), the bound is(k+1)mu. This
is a graph path-load bound, not a claim that k stays bounded across arbitrary
multiple ordinary epochs. Intervening long epochs can write many connectors;
the theorem does NOT silently ignore them.

## Private pendant outputs have mu<=4

Suppose G consists of an arbitrary tree K, plus edge-disjoint private
pendant paths of length at most2 attached to K at one endpoint each. Their
non-K vertices are disjoint. Let A be the pendant edges. Additional complete
components with no A edges are permitted.

Any simple path in this graph uses at most two pendants, one at each end.
Thus it uses at most4 A edges, regardless of the size, shape or mass of K.
The following ordinary epoch after one complete block therefore consumes
at most16 A lifetimes.

This is NOT a component-count or Euler potential. It is an exact restriction
on which marked old lifetimes fit on the actual vertex-simple zipper path.
It does not require the actual simple path to be a geometric shortest path.

## Application to the gaining detoured collector

Use the independently passed all-q construction
one_component_paired_forest_collector.md (SHA256ed7197b2f981ab73ef47df9a9c30d9a190bd739540bdd7cc19aae1875606956c).
Mark ALL first-epoch R lifetimes as A. At its end the complete black w graph
is exactly:

- K: the initially supplied collector plus3-edge root connector, retained;
- one private length-one pendant for each straight departed input root;
- one private length-two pendant at each counterclockwise corner root:
  one R edge joins the collector, the other joins its new private leaf.

All vertices and every R lifetime are retained. There are n-q straight
pendants and q-1 two-edge corner pendants, hence |A|=n+q-2. The w cursor is
isolated and the next actual complete block is RRRRL. It leaves only3 new
edges, so the next ordinary epoch can consume at most16 of the first
n+q-2 outputs, uniformly in q. In particular the number of gain-bearing
corner R edges it can consume is at most16 too.

Thus an immediately following long ordinary epoch, if the endpoint geometry
is modified within this same private-pendant output class, must use almost
entirely non-A backbone input, not the first gaining spiral outputs.
The actual canonical endpoint control is still sharper (only1 A edge), but
the16 bound does not depend on that particular port choice.

The collector is fully charged initial old fuel. Reimporting its huge
component does not invalidate the marked-edge bound; the old backbone can
be long while A has bounded path load.

## Applications and explicit limits

For the pure spaced spiral with no collector, A consists of disjoint
one/two-edge stars, so mu<=2 and the one-block/next-epoch bound is8.
For the mixed spiral+rod control, mark ONLY spiral-R output, not carrying
rod-R output. Its first output graph has one carrying component meeting A
only in the final tooth, plus disjoint one/two-edge spiral stars; again
mu<=2. One renewal cannot enable more than8 spiral-R inputs in the next
ordinary epoch, however long the carrying rod is.

The independently passed odd-rod recycling control evades this hypothesis:
there A itself is a long backbone with mu=2r, and all2r outputs really are
reused after one reset. This is why no universal small-output-reuse bound
follows merely from the zipper theorem or lifetime chronology.

To obtain substantial gain-bearing regeneration in the private-pendant
collector designs, one must change the output path-load structure, or add
many intermediate connecting writes/renewals and charge them. This note
rules out only the stated one-renewal protocol; it says nothing universal
about arbitrary future controllers or full Langton dynamics.
