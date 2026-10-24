# Retaining complete first-read cycle length as a clock lower bound

23 October 2026, 10:45 UTC. Analytic implementation refinement candidate.
No new exclusion or computation is claimed. The existing first-cell run is
unchanged.

For a complete bi-infinite WHITE front at its ACTUAL full drift, take ANY
cycle of the first-read predecessor functional graph, reverse its direction
and lift it to a winding-one simple cylinder circle of length ell. The
signed coupled-run proof in white_front_coupled_run_speed.md applies to
this arbitrary cycle, not merely to one chosen maximum or shortest cycle.
Before using ell>=2||d||infinity, it proves

    P>=4*ell.                                             (1)

Its sharper integral form is

    P>=ell+4*ceil(3*ell/4).                               (2)

Indeed its Q>=3m/2 with m=ell/2 gives Q>=ceil(3ell/4), and P=ell+4Q.
Since ell is even, this is4ell when ell is divisible by four and4ell+2
when ell is2 modulo four. It is safe to retain only the weaker(1).

The existing first-cell monitor stores a nonnegative saturated path debt
sum(1+4j) from the acyclic component root to each exposed vertex. A separate
second coordinate may store

    L(v)=min(S,4*distance_in_edges(root,v)).

On attaching a rooted component at an edge u->v, its root length offset is
min(S,L(u)+4); add that nonnegative offset to every descendant's stored
coordinate and saturate. On closing its unique cycle, the root-to-source
path followed by the closing edge is EXACTLY that complete simple cycle.
Therefore min(S,L(u)+4) is the safe saturated lower bound min(S,4ell).
Keep the maximum over completed cycles in the global period lower-bound
register, just as for the existing ordinal debt.

After a component has closed its unique cycle, its attached-tree distances
need not be retained for future cycle tests: the indegree-one invariant
forbids a second cycle in that component. Multiple disjoint essential
components remain permitted, including the TWO actual first-read cycles
of standard104. No uniqueness or connectivity requirement is introduced.

IMPORTANT: use the MAXIMUM of the ordinal debt and4ell, not their sum and
not the edgewise maximum of their weights. The inequalities are different
whole-cycle lower bounds; their payments can overlap. The fixed real-clock
scale is unchanged. Saturation does not upper-bound the actual period.

This is a direct reuse of an independently signed all-cap structural
inequality. An implementation and independent full-prefix replay would be
needed before using this extra coordinate in any new certificate. It is
not needed by the pending fixed-N32 cap-six certificate or its replay.
