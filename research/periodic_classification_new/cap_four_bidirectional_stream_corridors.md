# Cap-four stream superlevels carry essential flow in both directions

23 October 2026, 11:02 UTC. Analytic corollary candidate, not an exclusion.
Uses the independently signed cap-four first-R maximum rule and the signed
all-cap first-departure counterflow theorem. Actual FULL drift throughout.

For a complete bi-infinite WHITE front of cap four, put
m(v)=max of the heights of the two clockwise C faces incident to v. The
signed local stream table proves that v's first R turns around a maximizing
C face F. Its FIRST incoming edge AND its FIRST R outgoing edge are both
boundary edges of F. Consequently, if a(v) is the first-read predecessor
and b(v) is the target of the first-R departure,

    m(a(v))>=m(v),       m(b(v))>=m(v).

For any fixed threshold lambda, use CORNER-connected components of C faces
of height at least lambda. At any active vertex incident to such a
component, the selected first-R face is in this same component; both a(v)
and b(v) stay incident to it. Two high C faces meeting at a vertex are in
one corner-connected component, so no component ambiguity arises there.

Thus each component containing an active vertex contains both:
- a cycle of a, whose reversal is an ACTUAL-edge essential circle winding+1;
- a cycle of b, an ACTUAL-edge essential circle winding-1.

Both conclusions use complete chronology and embedded simplicity, not only
static stream-flow counts. This is a bidirectional essential corridor
condition, stronger than the earlier 'some essential backbone' condition.
It does not imply either circle is an uninterrupted ant time interval,
that the two circles are edge-disjoint, or that the component is impossible.

For r different active superlevel components at ONE fixed threshold,
choose one b-cycle in each. They are distinct and vertex-disjoint: a cycle
vertex incident to two high components would corner-connect them. The
signed additive counterflow bound therefore gives

    P>=sum_i ell_i+2D*(1+r) >= 2D*(1+2r).

This bounds the number of disconnected active high corridors in terms of
P and drift but gives no uniform bound on either. Do NOT add this bound
again across several thresholds: one cycle can persist through many levels.
Also do NOT add positive and negative cycle lengths without controlling
shared edges; the two selected graph families can overlap.

The first-R maximum rule and hence stream-superlevel localization remain
CAP FOUR. The separate first-arrival and first-departure cycle existence
and counterflow bound are ALL-CAP WHITE theorems. Prepared input, initial
head exceptions, nonperiodic capture and a global cap-four exclusion are
not proved here.
