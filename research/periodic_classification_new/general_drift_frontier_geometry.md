# A nearest-row cylinder model for every supplied full drift

23 October 2026, 03:33 UTC. Geometry extension and both (3,+/-1) cap-four applications independently signed.
The finite clock-zone framework itself is already signed.

An orientation-preserving quarter rotation puts any nonzero full drift
into d=(a,b), with a>0 and |b|<=a. Heading reset ensures a+b is even.
For integer row t use representatives

    p(t,i) = (i, t + floor(b*i/a)),      0<=i<a.

Every lattice cell has a unique representative modulo the FULL vector d:
reduce x modulo a by k=floor(x/a), subtract k*d, and set t to the remaining
y minus floor(b*i/a). No primitive-vector quotient is introduced.

For a physical step (dx,dy), put

    k = floor((i+dx)/a),
    j = i+dx-k*a,
    Delta = floor(b*i/a)+dy-k*b-floor(b*j/a).

Then the neighbor representative lies in row t+Delta, column j, and its
exact seam voltage is k. Vertical edges have Delta=plus or minus one and
k=0. Horizontal edges have Delta in {-1,0,1}, since |b|<=a. This remains
true at the seam and for negative b. Thus every physical edge is internal
to one row or joins two consecutive rows.

The parity of p(t,i) is t+i+floor(b*i/a) modulo two. With the usual checker
sector, even vertices have vertical exits and odd vertices horizontal
exits; incoming axes are perpendicular. Generate every finite complete
white history up to the supplied cap at every column. Within-row edge
counts must match, as must each adjacent-row pair's cross-boundary counts.
Match chronological kth traversals exactly. These are finite discrete
constraints with no chronological clock bound.

When exposing a new row, include all its internal arcs immediately, every
old-to-new arc with Delta=+1, and every new-to-old arc with Delta=-1. All old
frontier ports are then resolved. The previously signed path compression,
cyclic-block order, canonical lexicographic cut, integer normalized-clock
zones, projection and safe weakening apply without change.

Sources: `frontier_drift_geometry.py`, `probe_general_drift_zone_core.py`,
and `probe_general_drift_zone.py`. The cap-four full-drift (3,1)
graph has 440 states/edges; its chiral companion (3,-1) has 400 states/edges.
Independent direct lattice reduction, starting from all 59,582 unpruned
row assignments for each case, reproduces every reachable transition and
finds no potential whole-front terminal. See
`../audits/check_supplied_drift_zones_independent.py` and
`../audits/general_d3_{1,-1}_zone_cap4_bound2_mod2_independent.json`.
Therefore every complete white-input front with either supplied full drift,
or its quarter rotations, must have some physical cell visited at least
FIVE times. This has no transverse-width or period cutoff.
The two slopes are not silently identified by reflection, which would
exchange R and L. Quarter rotations alone preserve the classical rule.

This is an all-width method for each supplied finite drift and cap, not a
finite enumeration of all drift vectors, and not a global cap-four proof.
