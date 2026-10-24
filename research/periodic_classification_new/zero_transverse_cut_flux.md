# Exact zero transverse cut flux for static row inventories

23 October 2026, 08:22 UTC. Analytically reviewed safe necessary optimization.
No period, width, visit or growth bound is introduced here.

Use full-drift Geometry(a,b), representatives(c,floor(bc/a)+r), and exact
internally matched row histories. The integer row coordinate r is unchanged
by translation by the ACTUAL full drift. Every real successor step changes
r by at most one. A complete event cycle therefore has zero algebraic
crossing of the transverse cut between rows r and r+1.

Count its upward crossings by the up-departure ports in row r, and its
downward crossings by the incoming-from-above ports in row r. Exact physical
edge matching identifies the latter with downward departures in row r+1.
Thus each complete row satisfies

    F = sum(upward outgoing port counts)
          - sum(incoming-from-above port counts) = 0.

This is an intrinsic linear condition on that row's complete histories.
It also follows inductively from the empty lower boundary, port matching
and vertex divergence. Hence all previously reached rows already satisfy
it; removing F!=0 rows only avoids storing unreachable static inventory.

For a row of parity p, upward outgoing ports are Geometry.arcs[p] with
rowdelta+1. Incoming-from-above ports are target-column/incoming-heading
entries of Geometry.arcs[1-p] with rowdelta-1. The source row is one higher,
which is why the parity is1-p in the second sum.

frontier_zero_flux_rows.py incorporates this into the exact row join,
using only safe independent min/max residual flux bounds while building
columns. Examples at visitcap4 are generic full(5,1) row counts149,751
unfiltered down to31,569 and26,429 for the two parities; full(4,4)
923,521 down to152,707 and151,297; full(5,3)1,953,031 down to303,851 and
312,455. The unequal parity counts are intentional. In the pure diagonal
case this is the earlier signed specialized row-balance condition.
No frozen certificate or old row ordering is changed in place.
