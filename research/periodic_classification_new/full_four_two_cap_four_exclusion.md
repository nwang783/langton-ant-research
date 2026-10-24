# Both chiral full drifts (4,±2) are impossible under visit cap four

23 October 2026, 07:06 UTC. Independently signed supplied-drift all-width,
all-period exclusions (audit KI). The two chiral cases are separate.

Use the signed nearest-row representatives p(t,i)=(i,t+floor(b*i/4)),
0<=i<4, for each b=2 and b=-2. All physical edges stay within one row or
join neighboring rows, with their exact seam voltage. Generate all31
complete white histories through four visits at every column, imposing
only exact internal edge counts. Each parity has63,001 matched row states.

The signed paired-left kinematic bound gives P>=g+2||d||_infinity>=16
for a complete white front, using the retained g>=8. Apply the signed
normalized-real frontier with N=16,M=32,q=2. Exact ordinal edge matching
and processed path connectivity are retained; strict representative-clock
constraints are safely relaxed and clipped. No width or period cutoff is
imposed. Complete reachability has no possible whole-front outcome:

    full(4,2):   1,672 states,1,672 edges,174,730 attempted extensions;
    full(4,-2):  1,580 states,1,580 edges,158,696 attempted extensions.

`../audits/check_general_normalized_real_independent.py` reconstructs both
physical geometries by complex coordinate reduction and strict-clock
feasibility by infinitesimal Bellman-Ford. For EACH drift it starts from
all1,847,042 unpruned row tuples, regenerates all internal port matches,
and replays every extension. Both frozen complete graphs pass.

Producer certificates have filenames
`general_d4_2_normalized_real_cap4_N16_M32_mod2.certificate.json` and
`general_d4_-2_normalized_real_cap4_N16_M32_mod2.certificate.json`.
Independent results use the same stems under `../audits/` with suffix
`_independent.json`.

Genuine quarter rotations of the TWO cases cover every vector of squared
norm20. No reflection is used, and the full displacement is not replaced
by a primitive vector. The separately signed white-history bridge carries
these bounded-multiplicity no-gos to eventual periodic suffixes from finite
black seeds.

This does not exclude cap five at these drifts, general cap four, all-cap
axis-four fronts, other displacement vectors, nonperiodic behavior, or
universal finite-seed capture. No literature-priority claim is made.
