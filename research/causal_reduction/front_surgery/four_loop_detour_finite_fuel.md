# Finite fuel for arbitrary four-loop detours of the standard highway

Status: computer-assisted local-closure proof,22October2026; independent
audit passed. A separately generated vector-heading/low-pivot certificate is
`audits/check_detour_window_independent.py` and `audits/detour_window_independent.json`. This is NOT a global attraction theorem. The hypothesis
already fixes the entire geometric standard backbone. Detour choices need
not be periodic, deterministic in backbone phase, or eventually repetitive.

## Exact trace language

Fix the standard104-letter word W and its physical drift d=(-2,2), normalizing
the initial heading to north. Before any individual backbone letter c, permit
an arbitrary train of pose-returning unadorned four-turn loops, followed by c.
Every feasible such train has one of these three forms:

1. no inserted loop;
2. opposite(c)^4;
3. c^4 opposite(c)^4.

Indeed consecutive loops must alternate their letters because they revisit
the same entry cell, and the final loop must have letter opposite(c). Three
loops are impossible: at least one non-entry cell of the first loop is not
visited by the second, and the third would reread it with the same letter.
Thus the above finite library is exhaustive for four-turn-loop trains.

Suppose an ant from an arbitrary finite black board B, |B|=m, has its whole
future trace in this language over W^omega. The same statement applies after
any finite prelude, using the board at the start of the described tail.

THEOREM: Only finitely many backbone periods contain any nonempty train.
More explicitly, at most3+7m backbone periods contain a detour. Consequently
at most104(3+7m) backbone-letter sites are decorated, and at most
832(3+7m) inserted physical updates occur. The actual tail is eventually W^omega.
Translations and quarter-turn rotations preserve the statement and its bound.
For a cyclic choice of backbone phase, move to a full standard period boundary;
eventual standardness still follows, and the numerical bound uses the black
mass at that new boundary, not necessarily the mass before the partial period.

No claim is made that an arbitrary ant trace admits this decomposition.

## Seven-period white-window lemma

Consider backbone periods k=-3,...,3, with TWO independent optional-word
variables at every one of their104 phases: the single and double train above.
Keep the at-most-one guard for each phase. Variables in different periods
are completely independent; there is NO periodic wrap or identification.

List all potential read events, including both optional words and the fixed
backbone. For each translation class modulo Z*d, let alpha and beta be the
minimum and maximum longitudinal ranks of the one-period potential positions.
A cell of rank l has all of its potential backbone/optional reads in the
seven-period window exactly when

    -3 <= l-beta  and  l-alpha <= 3.

Let F be this set of complete-history cells. It has143 cells. Discard every
read constraint at every other cell; this deliberately permits arbitrary
outside fields and arbitrary compatible excursions through them.

For each cell in F, sort its potential events by actual time
(period, backbone phase, optional substep). Require its first selected read
to be R and successive selected reads to alternate. Original events give
unconditional GF(2) equations; optional events give equations guarded by their
option variables. This is the same exact parity reduction audited in
`README.md`, now using physical cells rather than periodic quotient classes.

The checker `window_detour_rigidity.py` forms1,456 Boolean variables and533
unconditional original-read equations. Exact Gaussian elimination plus sound
implication propagation forces EVERY one of the208 central-period optional
variables to zero. No branching or solver trust is required beyond ordinary
integer XOR arithmetic. The final linear rank is1,128, leaving328 outer
variables unconstrained. The two nontrivial propagation passes add591 and4
zero-variable equations. The corresponding certificate is
`window_rigidity_certificate.json`, including the literal standard word,
all143 cells of F, the central variable indices, and the numerical replay.

Propagation is elementary: if existing equations make a consequence of
'z=1 implies parity equation E' false, add z=0. If they make z=1 true, add
its consequences. A Gaussian row addition is accepted only if consistent.
In this run no positive guard activation is needed. Since the all-zero
choice is genuinely feasible, the constraint system itself is not empty.

Thus if all cells of F are white before their complete window history begins,
no detour can occur in the central backbone period, whatever the other six
periods' detour choices and whatever colors lie outside F.

## Passing from the window to an arbitrary finite seed

For a central period n>=3 in the actual one-sided trace, all of the potential
reads of F+n*d occur in periods n-3,...,n+3. In particular no earlier tail
event can have touched any of these cells. If

    B intersect (F+n*d) = empty,

the white-window lemma applies and that period has no detour. Therefore every
decorated period n>=3 requires at least one entry-time black cell in F+n*d.
This is not a causal-label injection: a black cell may be used by several
windows, and we count that multiplicity explicitly.

For a fixed black cell q, the integers n with q in F+n*d correspond to the
cells of F in q's translation class. The certificate verifies that the largest
such class has exactly7 cells. Hence q can account for at most7 decorated
periods. Summing over the m entry black cells bounds the number of decorated
periods n>=3 by7m. The first three periods add at most3.

Every permitted train has at most8 inserted updates, and each period has104
backbone letters. This proves all stated bounds and eventual exact standardness.
The location of the LAST detour is not bounded by m alone: a black cell can
be placed arbitrarily far ahead along the fixed geometric corridor.

## Why this is stronger than the preliminary periodic tests

Testing one, two, or finitely many backbone periods with periodic option
choices would not exclude longer-period or aperiodic renewal. Here the seven
periods are an open spatial/time window; outside variables and fields are not
identified or assumed blank. Only the complete-history set F is initialized
white. The finite seed can spoil finitely many translated copies of this
local white-history certificate, with the explicit multiplicity bound above.
