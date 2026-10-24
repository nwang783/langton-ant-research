# No stationary finite CPU with all mutable memory on one side

Status: independently analytically audited, 2026-10-22 22:27 UTC. The core analysis also independently agrees with the closed-pose hull strengthening. This is a scoped architecture obstruction, not nonuniversality of the ant or a highway proof.

## 1. Closed-pose hull identity

For any actual finite classical-ant interval [s,t] with t>s and identical endpoint position AND heading, let

    A = B_s symmetric_difference B_t,
    V = {p_s,p_(s+1),...,p_t}.

The backgrounds can be arbitrary, including infinite. A is finite because only finitely many cells were read. Then

    conv(V) = conv(A).

In particular A is nonempty and the common endpoint position belongs to conv(A).

The prior endpoint-inclusive hull theorem is in `../continuation_2026-10-22/ant_continuation/wake_clock/proof_notes.md`, Theorem1. Its proof needs only a small cyclic-endpoint strengthening here.

Proof. Choose any exposed vertex v of the finite path hull. Its grid neighbors used by the path cannot include two opposite neighbors, since v would then lie between them rather than be extreme. Every read at v has a predecessor and successor. For the initial read, the predecessor is supplied by the last move of the interval; equality of both endpoint position and heading makes this the actual incoming direction of the initial pose. Thus these cyclic neighboring positions are also in V.

The incoming and outgoing axes are perpendicular. The fixed sector gives the same incoming axis at every visit to a given cell. Therefore the two available perpendicular neighbors force the same predecessor, successor, and turn at every occurrence of v. Alternation of consecutive reads at one cell forbids two such visits. Thus v is read exactly once and lies in A. Every hull vertex lies in A; conversely A is a subset of V. This proves the identity. The argument is local and does not require finite black support.

## 2. Finite checkpoint bound

Fix a finite physical pose set P and a finite controller cell set C. Let D be any fixed set of lattice cells such that no position appearing in P belongs to conv(D). Consider one actual uninterrupted trajectory with strictly increasing checkpoint times

    t_0 < t_1 < ... < t_M.

Assume:

1. Each checkpoint pose belongs to P.
2. The COMPLETE board XOR between successive checkpoints, outside C, is contained in D.

Then

    M+1 <= |P| * 2^|C|.

No restriction is imposed on the number of remote writes, their diameter, their movement, the duration of a checkpoint interval, or the trajectory between checkpoints. There are no external head resets or unrecorded field changes.

Proof. If there were more checkpoints, two would have equal pose and equal board restriction to C. Summing the intervening full XOR masks cancels the entire controller and leaves a total mask A contained in D. By Section1, the repeated position belongs to conv(A), hence to conv(D), contrary to the hypothesis on P. QED.

A particularly simple sufficient condition is that D lies in one fixed open half-plane strictly separated from every checkpoint position. The finite controller C may lie anywhere and may change in arbitrary ways. The initial background may be infinite; it is never discarded, and unchanged cells cancel exactly.

## 3. Interpretation and reduction scope

A literal ant CPU that returns to finitely many physical port poses, has only finitely many controller cells, and places all other mutable memory strictly on one side cannot execute indefinitely. This remains true if it writes an unbounded number of memory cells during each instruction, performs arbitrarily large temporary excursions, and cleans those excursions up before the checkpoint. Such writes must be counted in the complete endpoint XOR if they persist.

This strictly strengthens the prior single-moving-window obstruction for one-sided memory layouts. It requires neither a bounded moving window nor bounded tape-head motion, and gives a checkpoint count independent of the remote memory geometry.

It also rules out a computable faithful step-by-step HALT compiler of this architecture even if the compiler promises correct checkpoint simulation only up to source halting. The compiler's finite P and C give the computable source-step bound |P|*2^|C| on every halting simulation; simulating the source for that many steps would decide HALT. This statement assumes at least one checkpoint per simulated source step, or another stated computable bound on source progress per checkpoint. It does not apply merely because a target has one eventual accepting event.

The theorem does NOT exclude:

- A physically moving CPU or an unbounded set of checkpoint poses.
- Unbounded controller memory whose full state is not contained in a fixed finite C.
- A two-sided or surrounding memory layout whose convex hull contains the ports.
- External resets between half-strip excursions. In particular the protected externally driven half-plane builder target is not an actual closed-pose trajectory and is not covered.
- A mirrored pair of growing half-strip builders. Their two remote write regions can straddle the central port.
- A reduction with a materially different representation of computation.

The full-XOR and fixed allowed-memory-set premises are essential. Merely bounding the intended output while ignoring lasting garbage does not satisfy them.

## 4. Quantitative cone transience

Let an actual orbit, on any background, eventually remain in a fixed lattice domain E. Suppose a real linear functional ell has finite sublevel sets on E:

    E intersect {ell<=M} is finite for every real M.

Then the orbit is physically transient: every finite set of cells is visited only finitely often. More precisely, for any finite pose set P, put

    M = max {ell(p): p is a position in P},
    C = E intersect {ell<=M}.

After the confinement time, the number of checkpoints whose pose lies in P is at most |P|*2^|C|. Every full interval XOR lies in E; outside C its support has ell>M, which strictly separates it from every checkpoint position. Section2 applies. Taking P to be all four headings over a finite cell set proves transience.

Examples include translated quadrants, pointed cones of opening angle strictly less than pi, and one-ended fixed-width strips. The claim does NOT cover a two-ended axial strip or a half-plane with infinite boundary direction, because their relevant sublevel sets need not be finite. It does not exclude a physically transient nonstandard front.

The qualitative cone-transience conclusion can also be inherited from `../first_principles_new/recurrent_boundary_current.md`, Section2: a recurrent cell has at least three recurrent neighbors, whereas a nonempty recurrent set in a pointed cone has a minimizing cell with two missing lower neighbors. The explicit checkpoint-count bound here is the stronger quantitative consequence of the closed-pose hull identity. No novelty is claimed for the qualitative recurrence argument.
