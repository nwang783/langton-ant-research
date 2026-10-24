# All exactly matched L1/R2 ports admit simultaneous pair erasure

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Positive output, three-read classes and every L supplier are retained.
No K1 premise. Pending independent review.

This extends signed7d357e69 beyond flow four. A physical directed edge
is MATCHED when its source L1 and R2 both depart along that edge, and
its target L1 and R2 arrive along it in those SAME chronological port
positions. Equivalently, actual successors send source.L1 to target.L1
and source.R2 to target.R2. Let Q count these full-drift edge classes.

## 1. Exact ten-profile inventory

Normalize travel to S, source incoming axis E/W, target incoming N/S.
The following are ALL matched complete heading pairs; a comma separates
source and target. Headings name actual rank0,1,2[,3], not turn letters.

    flow2: (WWE,NSS), (WWE,NSSN), (WWEE,NSS), (WWEE,NSSN)
    flow3: (EWE,SSS), (EWE,SSSN), (EWEE,SSS), (EWEE,SSSN),
           (WWEW,NSSS)
    flow4: (EWEW,SSSS).

For flow2 the common port ranks are1,2. Flow3 uses either ranks0,1,2
at both ends, or ranks1,2,3 at both. Flow4 uses all four. Full port
ordinal matching gives T1(target)=T1(source)+1 and likewise for rank2.
No local profile is asserted to be an attained exterior or front.

A cell can be a source of such a pair ONLY when its rank1/2 headings
are opposite, and a target ONLY when they agree. Its unique rank1/2
common port therefore participates in at most one matched edge, and
it cannot play both roles. Thus ALL matched edges have disjoint source
and target cell classes. Opposite checker parity prevents an edge's
endpoints identifying under the actual full drift. Rank1/2 occurrences
are distinct for nonzero d. Three-read endpoint classes are allowed.

## 2. The stronger connected core

For each matched edge let s transpose the source's outgoing L1/R2
occurrences. The target transposition is t=sigma s sigma^(-1), where
sigma is the actual single P-cycle. Products S,T over all Q edges have
disjoint supports and T=sigma S sigma^(-1). Therefore

    sigma_Q=ST sigma=S sigma S

is one P-cycle. The proof of7d357e69 applies verbatim: delete BOTH
exchange graph edges at all Q matched ports, keeping every canonical
node. The graph G_core remains CONNECTED, and

    beta(G_core)=beta(G)-2Q is nonnegative and even.

At each pair the two graph edges really are parallel: sigma0 maps the
source.L1 occurrence directly to target.R2, and source.R2 directly to
target.L1. Their graph endpoints are distinct adjacent sheet nodes.
Their opposite clock transfers cancel because their actual Delta
values are equal. All physical flow-four edges belong to this class,
so Q>=F4, but flow-two and flow-three matches also occur in the exact
necessary inventory.

This is an occurrence-permutation reduction, not a physical ant splice,
board deletion, or higher-cap theorem. No beta upper bound follows.

## 3. Residual ports are compulsory at every proper canonical node

Write length(gamma)=ell and winding(gamma)=w. After matched pairs
cancel, the signed clock identity remains

    P*w=ell+sum_residual(outR2 Delta)-sum_residual(outL1 Delta).

For a proper node 0<ell<P. Thus a contractible or negatively essential
node has at least one residual outgoing L1 incidence. A positively
essential node has at least one residual outgoing R2 incidence.

In particular, an elementary TOP C unit loop must have an UNMATCHED
source port: TOP is the upper exchange endpoint and its negative L1
incidence is the common outgoing rank1/2 port. Dually an elementary
BOTTOM L unit loop must have an UNMATCHED target port. This is exact
rank chronology, not a distinct defect, fuel payment or forest root.

The unmatched source's two successors cannot both be target ranks1/2.
At least one is target R0 or target L3. Dually an unmatched target's
two predecessors include source R0 or L3. These genuine early/late
ports, rather than mere parallel graph geometry, are the remaining
assembly channels.

## 4. Why arbitrary elementary two-level patches cannot be erased

A tempting false step is that adjacent C and L unit loops always give
a matched flow-two port. The local inventory explicitly rejects it.
For a source WWEE using its S port at ranks1,2, the far endpoint may
be SSNN, whose same S port occurs at ranks0,1. Full ordinal matching
then gives

    target.R0=source.L1+1,
    target.L1=source.R2+1.

Both repaired arcs at the target make the required unit-C right turn
and unit-L left turn, but its exchange is with a DIFFERENT C loop.
No paired exchange at this edge may be erased.

All target profiles with exactly two S inputs and the two required
unit-loop turns are

    SS, NSS, SSN, NNSS, NSSN, SNNS, SSNN.

Only NSS and NSSN match source ranks1,2. The others may use ranks0/1,
2/3, or0/3; SS has no exchange at all. These are necessary local port
controls, not complete-front positives. Thus free two-level face
patches remain live, with exact rank-shift transfers. The connected
core theorem does not exclude them.

Companion matched_rank12_port_inventory.py/json reconstructs every
1..4-read WHITE history at this prescribed edge. It is not a period,
drift, width, multiplicity, seed or controller scan.
