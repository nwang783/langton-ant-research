# Affine-count laps with quadratically moving memory are exactly decidable

23 October 2026, 20:21 UTC. Author analytic theorem and executable exact-checker
controls. Independent audit requested. This is a NEW CLASS REDUCTION relative
to the retained affine-position ordered-event special case, not a constructed
nonstandard ant, not an undecidability reduction, and not a global theorem.

## 1. Why this is a different construction freedom

An expanding lap may translate its head by a quantity proportional to the lap
number. Its next lap then starts at a QUADRATIC position. The retained
`../computability/ordered_event_certificates.md`, Section 4, explicitly does
not include that geometry in its affine special case. Replacing the physical
position by a new free coordinate would silently assume multiplication in
Presburger arithmetic and is not legitimate.

Here the actual quadratic position is retained. A bounded lap-separation
lemma makes its SAME-CELL relation Presburger anyway. This gives an exact
finite-supply test for growing laps with variable-direction arms, remote cap
memory, and arbitrarily much retained garbage, provided their complete literal
lap program has the supplied affine-count form. It does not supply that program.

The old two-ended controlled-strip, swept-front, mirrored-builder, decorated
axial hierarchy, common expanding-matrix and phase-permuted frameworks were
checked before this statement. Ordinary finite-state endpoint-cycle reasoning
substantially overlaps them and is NOT claimed as new here. The new point is
the explicit quadratic-geometry collision compiler below. The general inverse
and automatic ordered-event principles are retained results and are credited.
No claim about the wider literature is made.

## 2. Supplied literal program and actual head continuity

Give finitely many nonempty literal words w_b, integer alpha_b,beta_b >= 0,
and a specified initial physical heading h. Lap n is exactly

    W(n) = w_0^(alpha_0*n+beta_0) ... w_t^(alpha_t*n+beta_t), n >= 0.

At least one beta_b is positive, so every lap has finitely many and at least
one physical update. A variable-count word must restore its incoming heading;
constant-count stages may turn the head and are literally unrolled. The
complete lap must restore h. These are all checked from the literal words,
not from desired endpoints. Negative counts or an unverified head relocation
are not allowed. This includes unbounded axial or oblique sweeps in different
headings, with fixed finite connecting words.

The lap displacement is exactly d_1*n+d_0. Hence its actual starting position is

    p_n = d_1*n*(n-1)/2 + d_0*n.

If d_1 has an odd coordinate, bundle original laps 2n and 2n+1. Their literal
counts remain affine, the combined heading still restores, and all resulting
quadratic coefficients are integral. Thus after at most this grouping,

    p_n = A*n^2 + B*n,       A,B in Z^2.

Every individual read has an event address e=(n,b,j,r), where b is its block,
0 <= j < alpha_b*n+beta_b its copy, and r its literal phase. The actual pose is

    p(e) = A*n^2 + b_f*n + c_f*j + d_f,       heading h_f, turn t_f.       (1)

Here f=(b,r), and ALL coefficients come from literal word integration and
within-lap summation. Event order is lexicographic in n,b,j,r. Its domain is
Presburger, has order type omega, and contains the entire continuous ant path.
Every prefix is finite. In particular there is no external reset or controller
that teleports between arms. Literal geometry also preserves the physical
checkerboard/heading sector automatically at every event.

When A=0 the entire position relation is affine, so the retained ordered-event
certificate already applies directly. The genuine extension is A != 0.

## 3. Bounded separation of laps which read one cell

Choose any integer functional ell with a=ell(A)>0. From (1) and the affine
copy bounds, compute integers L,l,U,u such that every read on lap n satisfies

    a*n^2 + L*n+l <= ell(p(e)) <= a*n^2 + U*n+u.             (2)

A completely explicit conservative choice takes the minimum slope and minimum
intercept of all affine lower endpoint expressions for j=0 or j=count-1,
and the corresponding separate maxima of upper endpoint expressions. This
remains sound for count-zero blocks, which contribute no actual event.
Put D=max(0,u-l).

If laps m and n=m+delta, delta>0, read the SAME physical cell, (2) forces

    (2*a*delta+L-U)*m + a*delta^2+L*delta-D <= 0.            (3)

Consequently delta is impossible whenever BOTH

    2*a*delta+L-U >= 0,       a*delta^2+L*delta > D.

There is an effectively computed K after which these inequalities hold
permanently: increase delta until they hold and

    a*(2*delta+1)+L > 0.

The linear expression and quadratic expression are then increasing for every
larger delta. Earlier admissible delta are a finite set, so K is its maximum,
with K=0 if the set is empty. Therefore

    p(e)=p(f) implies abs(lap(e)-lap(f)) <= K.               (4)

This is an all-history causal statement. It is NOT a guessed truncation based
on a finite trajectory. It also works when the finite arm width and the
number of live stored cells grow without bound.

## 4. The exact quadratic cancellation

For any one of the finitely many delta in [-K,K], put m=n+delta. The equation
p(n,f,j)=p(m,g,k) is EXACTLY the two affine coordinate equations

    (b_f-b_g-2*A*delta)*n + c_f*j-c_g*k
        + d_f-d_g-b_g*delta-A*delta^2 = 0.                 (5)

All remaining event-domain, phase and order constraints are Presburger. Thus
the COMPLETE same-cell relation Eq(e,f), including same-lap repetitions and
ALL older and later laps, is a finite union of Presburger relations.
No output-reuse matching, read cap, period horizon, black-count relaxation,
field core, or assumed cleanliness enters the equation.

The implementation avoids a phase-pair search: map each event to
[n,b_f*n+c_f*j+d_f]. For each fixed delta, map event (m,g,k) to
[m-delta,(2*A*delta+b_g)*m+c_g*k+d_g-A*delta^2]. Composing the first map
with the reverse of the second gives precisely the Eq-delta relation.
This is finite exact integer-set algebra.

## 5. Exact finite-seed existence, complete fields and ownership

Using the ACTUAL Eq from Section 4, define in event order:

- Previous(e,f): f<e, Eq(e,f), and no same-cell event lies strictly between.
- First(e): there is no same-cell event before e.
- FirstL(e): First(e) and t_e=L.

These are Presburger relations. In the executable checker Previous is the
lexicographic maximum of the strict-prior same-cell relation, not merely the
previous lap or previous copy. Test:

1. No Previous pair has equal turn letters.
2. FirstL is a finite set of EVENTS.

The supplied entire path is an actual ant orbit from some finite black seed
IF AND ONLY IF both tests pass. Necessity is the ordinary cell flip rule.
For sufficiency initialize exactly

    B_min = {p(e): FirstL(e)}.

First visits are one-to-one with visited cells, so this is finite exactly when
the event set is finite. Every first read sees its prescribed bit; every later
read sees the opposite turn from its literal preceding read. Induction on the
omega event order proves EVERY physical update. B_min is the unique minimal
seed; extra black cells are permitted only if they are never read.

The COMPLETE field at any event e is exactly B_min XOR all flips at earlier
events, counted modulo two. No black cell is removed when it leaves a stored
neighborhood. Equation (4) merely proves that a cell whose last read is on lap
n is permanently retired after lap n+K. Its actual final bit remains on the
infinite board as garbage and is never silently replaced by white.

Thus the supply is one common finite B_min, chosen once at initialization.
An unbounded FirstL relation certifies that the literal proposed schema needs
infinitely many originally black cells; varying a finite seed with the number
of laps cannot evade this test. Current mass, cap state and all passive old
fields are retained by the induction, including endpoint bits generated by
much earlier work whenever they can actually be reread.

A specified finite seed can also be checked. In the A != 0 branch, solve
p(e)=q for each supplied cell q. By (2), each fixed q has only finitely many
possible lap numbers, computably bounded by the growing positive quadratic
lower bound. Thus one can determine whether it is unread or which first-turn
bit it requires. In the A=0 branch use its directly affine Presburger
cell/first-read relation; no finite-recurrence claim for a fixed cell is needed.
Compare with B_min, allowing only genuinely unread extras. No enumeration to
an unknown capture time is involved.

## 6. Standard capture is exactly decidable for every passing program

The ordinary-time rank is quadratic in n and need not be Presburger. That
rank is not used. Immediate event successor is Presburger, including block
and lap joins, so any FIXED number of successor applications is Presburger.
Use the retained ordered-event104 query: a complete eventual standard word
at some event, followed forever by agreement with the turn104 successors
later, allowing its finitely many cyclic phases. This is a first-order
Presburger sentence in the event domain.

Equivalently, decide whether the events whose turns differ104 successors
later form a finite set, then inspect the resulting104-periodic suffix for
one canonical standard cyclic phase. If the mismatch set is infinite, standard
capture is impossible for the supplied path. Any accepted finite-seed program
with a negative answer is a real counterexample. None has been found here.

General arbitrary unknown eventual period is NOT asserted decidable by this
fixed-successor argument. That issue is separate from the standard104 target.

## 7. Scope and current controls

`quadratic_lap_validator.py` integrates the actual headings, checks lap joining,
bundles odd quadratic coefficients, computes (2)--(4), compiles (5), selects
literal previous reads, and decides exact alternating-history and first-L
finiteness using libisl. Integer-set errors and resource exhaustion raise,
never mean impossibility. Extraction has a declared finite-size resource limit;
it does not reinterpret a large finite set as infinite.

The positive control groups the SAME standard104 orbit as W(n)=W104^(n+1).
Its actual lap starts are (-1,-1)*n^2+(-1,-1)*n. The scalar bound gives K=1,
not a search horizon. The expected minimal seed is the signed13-cell standard
seed. This confirms the new geometric representation does not mistakenly
exclude an actual periodic ant merely because its lap lengths grow.

The exact LRRL^(n+1) control from E is internally alternating but needs
N*(N+1) initial black cells for N completed laps: two fresh L cells per copy,
with 1+...+N copies. It is therefore infinite prepared rail, NOT a finite-seed
model. Other controls deliberately produce equal consecutive L or R reads.
The frozen JSON records actual outcomes; a finite literal replay only checks
coordinate and composition conventions, not the all-lap inference.

This reduction does not settle the signed two-layer carried-endpoint seed or
reopen its certified captured sample. Its actual continuation has not been
encoded as a successful recurrent lap program. No cap, gap, horizon, parameter,
marker or original184/394 seed scan was run.

A concrete fresh search TARGET, not a claimed mechanism, is now falsifiable:
supply one finite affine-count word program with nonzero affine lap drift,
pass its full Eq/Previous/FirstL tests, and fail its standard104 query. If it
fails, report the exact same-cell conflict relation or unbounded first-L
relation rather than increase a simulation horizon. A construction may use
nonrestoring endpoint memory and two-dimensional debris, but cannot omit
those cells or change the actual head pose. More general nonstationary word
choices and superlinear word counts remain outside this supplied class.

## 8. New geometric supply filter: transverse crossings cannot fund a long arm

Assume A != 0 and that the program passes both actual-ant tests. Let f be any
L-read phase in a variable-count block with alpha_f > 0 and nonzero copy drift
c_f. Through the first N laps it has

    alpha_f*N*(N-1)/2 + beta_f*N = Theta(N^2)

actual occurrences. At most finitely many can be globally first L. All remaining
ones have a literal PREVIOUS R at their cell, not merely some older matching
output. By (4), that previous event belongs to one of finitely many R families
g and offsets delta in [-K,K].

For any one such pair and offset, write

    v = b_f-b_g-2*A*delta,
    z = d_f-d_g-b_g*delta-A*delta^2.

Its exact collision equation is

    c_f*j-c_g*k + v*n+z = 0.                             (6)

There are precisely the following geometric alternatives.

1. Nonparallel c_f,c_g: the 2x2 system fixes at most ONE (j,k) for each lap n.
   This pair can fund only O(N) target occurrences through N laps.
2. Parallel nonzero c_f,c_g: choose a nonzero integer normal nu to their line.
   Equation (6) forces nu(v)*n+nu(z)=0. Unless BOTH coefficients are zero,
   there are no matches or matches on only ONE lap. Its contribution is finite.
3. A zero-drift constant-count source has O(1) events per lap and again funds
   only O(N) targets. A zero-drift variable-count word is itself impossible
   once it repeats twice: same-pose repetition would require all its per-cell
   read counts even, returning the entire board and making a finite periodic
   orbit, contrary to the retained closed-pose hull/finite-domain theorem.

Therefore at least one previous-R family must satisfy the exact PARALLEL
AFFINE RESONANCE

    c_f parallel c_g,    nu(v)=0,    nu(z)=0,              (7)

and must cover quadratically many target occurrences over infinitely many laps.
Mere line resonance without actual earlier chronological order is insufficient.
The already compiled Previous relation checks that distinction exactly.

For nonzero parallel drifts, choose a primitive integer vector q on their
common line, writing c_f=s*q, c_g=t*q, v=a*q, z=b*q. Equation (6) reduces to

    s*j-t*k+a*n+b=0.

The source/target count bounds and strict event order are affine inequalities.
Projection to (n,j) is an affine interval with fixed modular restrictions, or
a finite union of such pieces. To supply Theta(N^2) target events, at least one
piece needs a POSITIVE linear interval-width coefficient on a permitted residue
class of n. A single crossing or bounded-width matching cannot replenish the
long arm. This is a finite rational/congruence check on a supplied program,
not another cap-length or parameter scan.

This filter is deliberately local to the new certificate class. It neither
forbids several differently directed long arms in one lap nor says their
complete periodic profiles reset. It says that changing direction and crossing
old outputs transversely cannot by themselves fund the quadratic number of
black reads in a growing arm. A successful construction needs a genuine
parallel, correctly phased, last-write supply channel, or must leave this
quadratic affine-count class. All old nonparallel crossings and garbage remain
present in the full equality and previous-read calculation.

## Frozen executed outcomes at 20:25 UTC

All five exact all-lap controls completed with libisl 0.27-GMP.

- Grouped104: alternating TRUE, FirstL finite TRUE, exactly the original13
  black seed cells, quadratic A=B=(-1,-1), computed K=1.
- LRRL prepared rail: alternating TRUE, FirstL finite FALSE, A=B=(1,0), K=0.
- Punctuated rail LRRL^(n+1) RRRR: alternating TRUE, FirstL finite FALSE,
  A=B=(1,0), K=1. Thus even an exact nonperiodic-looking variable lap schedule
  is not accepted when it requires infinite initial supply.
- Equal-L boundary control: alternating FALSE, FirstL finite FALSE, K=1.
- Affine repeated square: alternating FALSE, FirstL finite TRUE, A=B=(0,0).
  Empty minimum fuel does not repair illegal same-cell chronology.

The JSON contains the full exact bad-read/FirstL sets, minimal seed and event
coordinates where finite, conservative collision-bound derivations, source
hashes and literal compiler-control counts. No schema was selected by a search.
The separate `quadratic_lap_standard_query.py/json` now executes the fixed104
successor query from Section 6. Grouped104 has no mismatches and matches
canonical phase0. Pure LRRL has no104-successor mismatches but fails canonical
word matching, correctly distinguishing an alternative periodic word from
standard104. The punctuated LRRL program has an INFINITE104-mismatch set,
correctly detecting its nonperiodic turn schedule. The last two remain rejected
by infinite initial supply and are not finite-seed counterexamples. The core
geometry validator source and frozen JSON have not changed.
