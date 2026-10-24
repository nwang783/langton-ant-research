# Distinct row-5 return ears reserve independent graph cycle rank

23 October 2026, 17:57 UTC. Conditional extension of the pending bounded
return-ear argument, submitted for independent review. The resource is
canonical graph cycle rank, not finite-seed fuel or persistent roots.

## 1. Scope

Assume the complete WHITE cap-four leftmost branch-free K=1 hypotheses
and the exact same-Gamma row-4/row-5 return configuration in
K1_row5_return_ear_forces_nonbridge.md. Let A be the unique LEFT canonical
MIDDLE node. Select n DISTINCT return pairs modulo the actual full drift,
including all their physical translates. Each pair has a short LEFT
chord chi_i between its row-5 return H_i and row-4 main face F_i, a bounded
LEFT ear Omega_i, a distinct all-L LOWER cleanup leaf C_i, and a LOWER
node D_i containing the actual outgoing E_i.R2 occurrence. Every e_i
joins A to D_i and is nonbridge by the bounded-ear argument.

The new claim is that the D_i belong to DIFFERENT connected components
of G with vertex A deleted. This prevents the selected returns from
sharing the same elementary graph cycle space.

## 2. The short return chords are disjoint

Each chi_i consists of two horizontal or two vertical unit face-center
segments, joining opposite C centers across ONE intermediate L center.
Its two max C endpoints have fixed opposite RIGHT orientations. A
row-5 oriented return face determines the opposite main face uniquely;
a row-4 face likewise has only its one opposite candidate. A face cannot
simultaneously have the distinct complete row-4 and row-5 inventories.
Therefore distinct return pairs have no common C endpoint.

Two perpendicular such length-two face-center chords could meet in
their interiors only at a common L midpoint. But a horizontal return at
that midpoint requires the west/east C heights to be M and north/south
to be b; a vertical return requires the reverse. Since b<M, both cannot
occur. Parallel chords can overlap only by sharing a C endpoint or
coinciding; these are already excluded. Thus all distinct physical
chords, INCLUDING their distinct full-drift translates, are disjoint.

They are crosscuts of the same LEFT side of the embedded Gamma. Their
bounded ears are consequently disjoint or nested. Distinct translates
cannot form a nesting cycle: strict containment decreases the finite
physical disk area, whereas translation preserves it. Short quotient
seams do not identify distinct endpoints or permit an overlap, by the
same complete-history distinctions above.

## 3. Different return nodes occupy different chord regions

For a return i, its D_i edge points W into the selected contact just
AFTER H_i in the positive Gamma order (use the displayed normalization;
rotate for other orientations). It lies inside Omega_i, immediately
LEFT of that initial Gamma arc.

A strictly nested return ear has its own H endpoint strictly AFTER H_i
and before F_i on this boundary arc. Its boundary interval cannot
contain the first selected contact after H_i, unless its H center
preceded that contact; no distinct face center lies between H_i and
its immediately next contact. Thus a sufficiently short initial part
of D_i's edge lies OUTSIDE every strictly nested ear. Disjoint ears do
not contain it either. So each D_i starts in the unique shell of its
ear: inside Omega_i and outside its strictly nested child ears.
Different chords have different such open regions.

At level b a canonical node cannot cross any chi_j except if it is
precisely the cleanup node C_j; the two crossing occurrences of chi_j
belong to that all-L square. Node D_i contains an actual R2 outgoing
occurrence, so D_i is not ANY all-L cleanup node C_j. It stays inside
its own open chord region.

More generally, remove A from G. Each C_j is then isolated, since it
was a leaf attached only to A. A component containing any D_i cannot
reach MIDDLE or higher levels: its first MIDDLE node would have to be
the unique LEFT A. Until such a first step it remains on LEFT. It also
cannot use an isolated C_j. At levels below b no edge crosses any chi_j,
and at level b all crossings are precisely those excluded C_j nodes.
All remaining exchange connectors are localized at primal cells away
from the chords. Therefore the WHOLE component of G-A containing D_i
is confined to that same open chord region.

It follows that distinct physical return ears have different lower
components. This remains true modulo full drift. If two inequivalent
return classes belonged to one quotient component, lift a component
path from D_i. It would reach some translate of D_j without crossing a
chord or Gamma, contradicting their different physical chord regions.
Thus there are at least n distinct components Q_i of G-A.

## 4. Exact graph reservation

For any connected graph G and vertex A, let Q run over the components
of G-A. Put d_Q equal to the number of edges from Q back to A, retaining
multiplicity. With beta the ordinary graph cycle rank,

    beta(G)=sum_Q [ beta(Q)+d_Q-1 ].

This is the direct edge/vertex count; no ribbon embedding is assumed.
For every selected return component Q_i, e_i is nonbridge, so d_Q_i>=2.
Each selected summand is at least one. Therefore

    beta(G)=N2-C_nodes+1 >= n.                         (1)

The signed parity gives the slightly stronger integer form

    beta(G) >= 2*ceil(n/2).                           (2)

No claim is made that each individual summand is even. The graph can
have other components, internal cycles and additional exchange sites.

Combining with the finite three-packet theorem, if r_i are the lengths
of maximal alternating R,L-pair runs, then their selected opposite
returns are distinct and

    beta(G) >= sum_i floor(r_i/3),

with the same global even rounding as in (2). This is a count of
independent canonical cycle rank forced by DISTINCT literal return
geometries. It is not a claim that every rank-lowering gate supplies
such a return; short alternating runs may not force any return.

## 5. What remains open

This is stronger than the abstract observation that many renewals may
share one graph cycle. Under these additional physical ear separators,
the selected distinct return geometries cannot share that same cycle
rank. Outside this leftmost branch-free same-Gamma configuration, no
such general additive claim is made.

Cycle rank itself still has no finite-original-mass bound. Equations
(1)-(2) do not establish K>=2, white-front existence, standard capture,
or a permanent renewal payment. They preserve all actual source L3s,
all lower sheet nodes, and both physical side-current boundaries.

Dependencies retained unchanged:
K1_row5_return_ear_forces_nonbridge.md, SHA
25aca7954d9658cceecd179393dee27226801c6bac4b1aea6711fc3538b60cd9;
K1_three_packet_return_and_straight_density.md, SHA
24dc6f859cc6df9095465757eab2f9eadf5321492ffca88f924785c1554de838;
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466.
