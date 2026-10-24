# Literal sibling-clearance quotient of the signed ancestry role graph

23 October 2026 09:26 UTC. Author reconstruction; independent review pending.
This is a necessary physical identity-dependency law, not a finite fuel theorem.

Use the signed LA 272-role graph and KP/LB's fixed selected-input parentage. A
role records an actual packet, one residual output, and the packet birth heading.
For an edge from source output s to selected input q of a target packet, its
source-normalized target pose is p=s-Rot(q,delta_heading). Every OTHER source
output t has target offset Rot(t-p,-delta_heading). Compare that offset with the
target's complete entry context, including its actual right marker.

There are three different obligations:

1. CORE: t lands in the five-cell target core. Its source residual identity must
   retire strictly before the target starts. A matching black color does not
   allow an existing residual identity to be silently reclassified as core.
2. WHITE: t lands in a required-white target cell. Its source identity must
   retire strictly before the target starts. Repairing only a later color is
   not a separate way to keep that old residual identity alive.
3. OTHER INPUT: t lands in a target residual input other than q. Its source
   identity must retire by the target packet, inclusively. It may remain until
   that very packet and be consumed there; this is not a strict-before claim.

These are necessary retirements of exact source-born identities. Later reuse of
one cell creates a fresh identity. The requirements do not say which packet
retires the sibling, whether helper roots are fresh, or whether one marginal
transfer is physically realizable. A sibling outside these three sets is merely
locally unobstructed; it is not promised indefinite survival.

`annotate_genealogy_sibling_clearance.py` checks all 35,904 signed fundamental
edges and 4,224 distinct source-role/target-packet/target-heading transfer classes.
Larger admitted C ages have the same spatial intersections. It finds:

- 1,892 edges with no strict-before (CORE or WHITE) sibling retirement;
- 728 edges with none of the three by-target retirement obligations;
- restricting BOTH endpoint packets to positive-C types DC,VC,VCC,UC,UCC gives
  respectively 540 strict-before-free and 48 by-target-free edges.

The 48-edge positive-C by-target-free graph has exactly one cyclic SCC. Its four
roles are DC output(2,0), headings 0,1,2,3, in that order. Its four cyclic edges
have fundamental C gap 7. The only other source families occurring in those
48 edges are VC output(0,1) and UC output(-1,2), which lead into DC and cannot
recur inside that restricted subgraph. This identifies the isolated DC gate
studied separately by the chronology analysis. It does NOT allow zero-C packet
roles to be dropped from an actual ancestral chain: the full by-target-free
graph has a 76-role cyclic SCC and already contains unary D cycles.

A basic counting consequence is valid on ONE actual selected-input ancestry
path. If M of its edges have at least one by-target sibling obligation, choose
one such exact sibling identity per edge. They are distinct, because different
source packets install disjoint fresh identity families and a path cannot
return to an earlier birth. None is the chosen continuing spine identity. Thus
at least M nonspine input-identity retirements occur before/by the corresponding
consumers. A physical packet has at most five residual inputs, so at least
ceil(M/5) packet instances contain those retirements. They need not all be off
that path: a target may retire its sibling in another input slot. No fresh-root,
unused-root-pair, permanently dead side-branch, or nonrenewable resource is implied.
This positive cleanup rate is compatible with arbitrarily many total C turns.

In particular these finite intersection counts do not prove the open V1/U1
funding records, confinement, an upper bound on ancestry generations, or capture.
The signed repeated-root-pair spiral family also forbids interpreting the
retirement count as a uniform bounded-use initial-root-pair charge.
