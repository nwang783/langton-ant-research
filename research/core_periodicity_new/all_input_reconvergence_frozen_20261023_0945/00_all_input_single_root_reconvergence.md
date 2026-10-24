# An actual all-input reconvergence inside one residual-root component

23 October 2026 09:45 UTC. Author literal certificate, independent review pending.
This is a finite physical ant factor, unlike the freely transported core combs.
It supplies a limitation on a proposed root-import budget, not noncapture.

Take heading0=north, clockwise heading indices, and initial black cells

(-2,2),(-1,-1),(-1,0),(-1,1),(-1,3),(0,-1),(0,0),(0,1),(1,0).

Start at(0,0), heading0. The actual next complete recurrent-eight packets are
DC,VCC,V,V. Their raw lengths are25,48,18,18, totaling109 reads. Their starts are
(0,0,0), (1,2,3), (-3,2,1), (0,1,1), and the raw endpoint is(3,0,1).
The actual next eleven turns are the required right marker LLLLRLRRRRL.
All literal guards, raw XORs and head endpoints are retained without resets.

For the residual all-input incidence DAG, the entry core is the usual five-cell
K. Its four initial residual roots are q0=(0,1), q1=(-2,2), q2=(-1,3), q3=(-1,1).
The first DC consumes only q0 and produces outputs at(2,0),(2,3),(3,1),(3,2).
The intermediate VCC consumes q1,q2 and the next V consumes one of its outputs
and q3. Those packets remain in a different incidence component from q0.

The FINAL V at(0,1,heading1) consumes physical positions(3,1) and(2,0), both exact
still-current outputs of the FIRST DC. No new residual root or component enters
this final packet. Its two inputs already have one common incidence component,
so Delta beta=|I|-g=2-1=1. That entire component has just ONE initial residual
root q0. Explicitly the source DC, its two output identity vertices, and the final
V form an undirected four-cycle, while causal time remains acyclic.

Thus a reconvergence cycle does not necessarily import/merge a fresh residual
root component, even when endpoint continuity and all whites are enforced.
This does not say that other physical helpers are absent: the separate component
of q1,q2,q3 and the unique live core genuinely participate in the intervening
word. Residual incidence ancestry is not the same as physical cursor-token
ownership. No claim about the physical root labels of all reads is made.

The residual clock is3; the last two produced inputs have source-included C age3,
consistent with the signed V minima. Final residual mass is25, total mass30,
and the incidence graph has c=2 components, v=3 V-type packets, u=0, r0=4, so
beta=v+4u-r0+c=1, independently matching the explicit cycle.

## Small entry-mass minimality, restricted to complete recurrent-eight factors

A separate direct literal prefix tree checks all words whose complete required
entry board has at most8 black cells. The empty root and30 nonempty words form
an exact31-node tree of maximum packet length3. Every one of their248 one-packet
extensions is either present in that tree, demands at least9 initial black cells,
or has a repeated-read color contradiction. All30 nonempty accepted words have
beta=0 by direct all-input replay. There is NO word-length or node-count cap in
this finite closure. Hence9 is the least boundary total mass for a reconvergence
inside a complete recurrent-eight factor, up to translation and quarter rotation.

This is not a statement about all ant trajectories of initial mass at most8:
entry mass can differ from the original seed mass, and packets outside this
recurrent-eight alphabet are not covered. The finite witness does not bound
future cycles, disprove an O(m^2) or geometric reuse budget, close V1/U1 funding,
or establish capture. It only rejects the naive fresh-root-per-beta-cycle premise.

`check_single_root_reconvergence.py` derives initial first-read colors directly
from literal RAW+final marker, simulates the explicit nine-cell board for120
reads, reconstructs every all-input incidence, and closes the small-mass tree.
The earlier DFS is discovery only and is not needed for any certificate claim.
