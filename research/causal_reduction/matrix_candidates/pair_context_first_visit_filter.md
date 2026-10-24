# First-visit functional graphs for eight-pair context substitutions

23 October 2026, 01:29 UTC. Analytic necessary condition; bridge analysis reviewed
it, independent analytic review passed. This allows noninjective refinement maps.

## Model and hypotheses

Use the eight perpendicular incoming/outgoing movement pairs (u,v) as states.
The image W(u,v) has common odd length k and displacement A*v, for a common
expansive integer A. The last movement of W(u,v) depends only on v; this is
the shared-last hypothesis of the exact pair-context recurrence adapter.
Require every image to alternate axes and each adapter seam G(u)->F(u,v)
to be perpendicular, so the pair/triple transition maps are total on their
stated finite state sets. Assume an actual fixed-root path with p(kn)=A*p(n),
and assume every image
meets A Z^2 only at its own source and target. Neither half-turn covariance
nor first-letter/first-endpoint injectivity is required.

Require the first endpoint arrival index j(u,v)>=2. This holds automatically
if every A*v has Manhattan norm at least2. This hypothesis is used only to
make the preceding fine movement local inside the incoming image.

## Exact sixteen-state first-visit map

A first visit at time n>=2 has a movement triple

    (w,u,v)=(d(n-2),d(n-1),d(n)),

with w perpendicular to u and u perpendicular to v. There are16 such triples.
Its scaled first visit lies in its incoming image W(w,u), by the same
source-or-target ownership proof as GN. Let M(w,u),H(w,u) be the two movements
immediately before and at this image's first endpoint arrival. Let G(u) be
the shared last movement. Let r(w,u) count its internal endpoint reads, and
write G(u)=epsilon(w,u)*H(w,u), with epsilon in{+1,-1}. Define

    sigma(w,u)=(-1)^r(w,u)*epsilon(w,u),
    F(u,v)=first(W(u,v)).

The actual outgoing movement at the scaled first visit is sigma(w,u)*F(u,v),
by the exact endpoint flip correction. Therefore the triple transforms by

    T(w,u,v)=(M(w,u), H(w,u), sigma(w,u)*F(u,v)).

This is a finite FUNCTION, not necessarily a permutation. Iterate at the
actual first-arrival time, as in GN. The next triple is genuine because j>=2.
The possible time-one first visit can use the model's initial heading as a
virtual w; after one refinement its triple is genuine. The infinite-occurrence
consequences below can simply discard the first two reads.

## Quantitative finite-fuel consequence

Call a triple R if its outgoing turn u->v is right. Define SafeR as the set
of triples all of whose forward T iterates, including itself, are R.
Every unsafe triple reaches L within fewer than16 iterations: if no L has
appeared by then, a state repeats and the future is entirely R.

If a nonzero cell q has an unsafe first-visit triple, there is r<16 such that
A^r*q is a first-L cell. It must therefore belong to the initial black support
B. Consequently ALL unsafe first-visit cells lie in

    union_(r=0)^15 A^(-r) B,

and there are at most16*|B| of them. In any norm in which A^-1 is contractive,
these cells lie within the initial seed's norm radius. If a triple's T orbit
has recurrent L, it cannot occur at a nonzero first-visit cell at all, since
expansiveness gives infinitely many distinct required initial black cells.

Thus every sufficiently late first visit has its triple in SafeR. This is a
necessary condition, not a construction theorem or a substitute for all-time
read alternation at internal nonvertex cells.

## Fresh-record constraints

A sufficiently high north first record forces two fresh R reads. Hence SafeR
must contain (N,E,S), and at least one of (E,N,E),(W,N,E). Rotate this condition
for south, east and west records. Each physical coordinate is unbounded in
absolute value for an expansive pure identity, by the signed dual-record
bridge. At least one vertical and one horizontal version must therefore hold.

For the concrete escape matrix A=[[3,2],[2,7]], k13, source/target-only overlap
and j>=2 hold throughout the internally legal image inventory. With shared
last map (N,W,S,W), the per-state signatures (F,M,H,sigma) have sizes
10,9,2,2,9,10,2,2 in incoming-heading/turn order. Restricting to the fixed
white horizontal root leaves77,760 signature assignments. The SafeR record
filter rejects51,136 and retains26,624. These are FEATURE assignments, not
counts of actual ant trajectories or complete word controllers.

`check_pair_first_visit_features.py` and `pair_first_visit_features.json`
freeze that small finite-graph diagnostic. In particular it is a positive
control showing that the first-visit filter does not alone exclude this
context architecture. A separate targeted literal prefix test of all25 root
images for this last-map/fixed-root choice fails by read222; that unreviewed
bounded test is not used in this analytic statement, and does not exclude
all possible eight-state or occurrence-dependent models.

## Audit sharpening

Only8 of the16 triples are R. An unsafe triple therefore reaches its first L
at some r<=8: otherwise an R state has repeated and its orbit stays R forever.
The preceding quantitative bound sharpens to union_(r=0)^8 A^(-r)B and at most
9*|B| unsafe nonzero first-visit cells. The conservative16*|B| bound above
remains valid; neither bound is a family exclusion.
