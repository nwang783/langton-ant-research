# Finite control with amortized spatial progress: exact cap and memory theorem

23 October2026. Analytic extension submitted for independent review. No new
compiler or candidate scan. Existing finite-memory and cycle-cone mechanisms
are attributed below; the claim is the precise prepared-input/control/cap
combination, not a global representation theorem.

## 1. Supplied finite control and checkable certificate

Supply a finite directed multigraph of control states s. Each state has a
specified incoming physical heading h_s. Each edge e:s->t carries a nonempty
literal ant word, whose actual geometric trace from h_s ends with heading h_t
and displacement d_e. Parallel edges and differing headings are allowed.
Specify the initial control state s0 and head at the origin.

Supply an integer functional ell, a state potential phi(s), and delta>0 such
that every allowed edge satisfies

    ell(d_e)+phi(t)-phi(s) >= delta.                         (1)

Rational certificates may be scaled to integers. Let R=max(phi)-min(phi),
M be the longest edge word, and E the finite union of all physical relative
phase-read positions of the edge words. Put

    H=max_E ell-min_E ell,
    K=floor((H+R)/delta).                                  (2)

The certificate permits individual BACKWARD edges with ell(d_e)<0. It forbids
only unlimited backward progress after control-state potential is accounted
for. All inequalities and headings are verified on the supplied finite data.

## 2. Exact geometric memory bound

If the same physical cell is read in block i and block j>i, their relative
phase offsets are e_i,e_j in E. Telescoping (1) over the intervening path gives

    (j-i)*delta
      <= ell(p_j-p_i)+phi(s_j)-phi(s_i)
       = ell(e_i-e_j)+phi(s_j)-phi(s_i)
      <= H+R.

Thus j-i<=K. The previous K completed EDGE LABELS determine the correct recent
read supports and their last-read ages. Store CURRENT colors on precisely
their reconstructed support, with current control state and prepared-input
phase. Handle repeated visits inside the selected edge word literally.

A current block's FIRST read of a cell outside the recorded support is
globally new in the one-sided execution. A read color evicted after K blocks is proved permanently invisible
to every later allowed continuation. The cell and its debris are NOT erased.
This includes the exact-gap-K case; K=0 leaves only within-word memory.

## 3. Fully periodic prepared input: supplied-cap and unknown-cap decisions

Assume T is explicitly fully two-dimensional periodic, for example given by
an exact binary p_x by p_y torus. More generally an explicitly finite background
observer invariant under all generated displacements would suffice; mere
periodicity along one old rail vector is NOT asserted sufficient.

The state stores head phase modulo (p_x,p_y), current control state, at most K
recent edge labels, and their actual colored read support. Histories must be
valid control paths ending at the current state; independent fictional ages
are not allowed. A coarse finite-state bound is

    V <= p_x*p_y*|States|*(sum_(j=0 to K) |Edges|^j)*2^(K*M).

The exact transition construction is the same as the independently signed
positive-progress palette theorem: actual stored reads, fresh T reads, literal
toggles, actual frame displacement, then safe retirement. An edge is present
only if all literal turns agree with those colors.

For a SPECIFIED finite XOR cap C, let cmax=max_(q in C) ell(q). Empty caps need
no exceptional prefix; otherwise

    N=max(0,floor((cmax-min_E ell+R)/delta)+1)               (3)

suffices. Indeed ell(p_n)>=n*delta-R, so no cap cell can be read in any block
n>=N. Process that finite prefix with actual head positions and specified cap
membership, then project into the finite graph. The prior cap's effects remain
in the colored history. Infinite survival is exactly cycle-basin reachability.

For SOME finite arbitrary-XOR cap, or SOME finite black-additions-only cap,
start at the GENUINE empty-history state, control s0 and origin input phase.
Allow legal choices of fresh initial bits during a finite controlled prefix
(arbitrary bits for XOR; T-black fixed black and T-white either color for black
additions). Each chosen cell is globally new by Section2, so finite choices
are one genuine finite initial cap. Reach an UNCONTROLLED periodic-input cycle
basin, then stop making changes. This condition is necessary and sufficient.
A controlled cycle alone may spend infinite fresh fuel and is not accepted.
An arbitrary cycle need not be reachable at the original phase/control, so it
is not accepted without the finite reachability test either.

Thus the fully supplied finite-control survival problem is decidable in all
three cap modes. This is a finite analytic construction, not an implemented
control-graph compiler or an efficient complexity bound.

## 4. Cycle-cone criterion and an effective progress-potential test

If (1) holds, every directed control cycle C has

    ell(sum_(e in C) d_e) >= delta*|C| > 0.                (4)

Conversely suppose one functional ell is strictly positive on the displacement
of EVERY directed simple cycle. Choose rational delta smaller than the minimum
simple-cycle average ell-displacement. The edge weights

    w_e=ell(d_e)-delta

have no negative directed cycle. Add a zero-cost source to every control
vertex and compute shortest-path distances q_s. They obey
q_t<=q_s+w_e. Setting phi(s)=-q_s gives exactly (1).
This argument includes disconnected control components and arbitrary backward
acyclic edges. If the control graph is acyclic there is no infinite path at all.

Consequently a certificate is effectively testable on the finite graph:
enumerate its simple cycles and solve the finite rational inequalities

    ell(cycle_displacement)>=1.

Strict feasibility is equivalent after scaling, and shortest-path difference
constraints then construct phi and delta. Any zero-displacement cycle makes
this sufficient test fail. In planar displacement space, the nonempty cycle
vectors admit such an ell exactly when zero is outside their convex hull.
Zero vectors must NOT be silently removed.

This is the standard finite cycle/difference-constraint mechanism written out
here, not a claim of a new graph-theory result. The retained
`../causal_reduction/unit_scale/recursive_cycle_geometry.md` already uses a
related simple-cycle cone decomposition for substitution occurrence graphs.
That different theorem excludes recurrent fixed-root checkpoints; it does
not supply this prepared-input/control/cap decision.

## 5. Physical periodicity and finite-band specified-input extension

On one FIXED board admitted by Section3, any infinite controlled-language
execution has an ultimately periodic literal continuation on that SAME board.
Ant determinism identifies its real physical trace with the continuation.
A control cycle has nonzero drift by (4). Alternative macro parsings may remain
nonperiodic. The coarse entry/period lengths after the exceptional prefix are
(V-1)*M and V*M.

The independently signed fixed-board finite-band proof extends with exactly
the same K and bound (3): its finite recurrence key additionally stores the
control state. Bounded transverse recurrence repeats that exact key. Outward
escape permits a repeated colored-history/control segment with outward drift
that stays beyond the black band on every copy. Exact full-drift prefix/period
checking and fixed-board finite branching again decide survival. Existence
across UNKNOWN caps on such an unbounded transverse input remains outside
this extension; the finite torus argument is not imported there.

## 6. Exact global limitation

The all-white finite-seed special case remains an application of retained
stale-memory mechanisms, now with a supplied amortized progress certificate.
No claim is made that an arbitrary finite-seed ant eventually admits this
finite controller, bounded footprint and certificate.

A coarse grammar may fail the cycle-cone test even for a standard trace:
unused concatenations can create zero or opposing combinatorial cycles.
Its failure therefore proves neither an actual legal cycle nor noncapture.
Conversely any actual non-eventually-translating trace represented by this
finite controller cannot satisfy (1) on that representation's allowed graph.
This is an architecture boundary, not a new global obstruction.

Increasingly long out-and-back laps evade the bounded-E premise even when
their endpoints progress. Fixed-size routing excursions with some backward
edges do NOT evade it when the control-state potential supplies (1). A global
proof would still need an eventual representation/progress theorem and a
separate classification of the resulting translators as standard104.
