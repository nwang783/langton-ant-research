# A continuous-cursor return bound from the COMPLETE changed support

23 October 2026. Exact deduction from the retained Ke strict integer clock.
This is a spatial necessary condition on an actual interval, not a capture
proof, a new invariant, or a claim of literature priority. No original source
documents are changed.

## 1. Exact return-discrepancy theorem

Let an actual standard Langton ant have the SAME physical head position AND
heading at the two endpoints s<t. Keep complete boards and put

    E = B_s XOR B_t,       T=t-s.

For z=x+y or z=x-y separately, write

    lo_z=min_{q in E} z(q), hi_z=max_{q in E} z(q), w_z=hi_z-lo_z,
    A_z(E)=min_{c in Z} sum_{q in E} (3^|z(q)-c|-1).

Then E is nonempty and

    T <= A_z(E) <= |E| (3^ceil(w_z/2)-1).                   (1)

The minimum exists: the positive sum diverges when |c| goes to infinity.
The same estimate holds if the endpoint positions differ but their z
coordinate and the clock's heading sign agree. The identical-pose version
is sufficient below and avoids accidentally forgetting cursor information.

In particular, if a proposed return changes at most e cells in a set whose
z span is at most w, its duration is at most e(3^ceil(w/2)-1), INDEPENDENT
of how far away that changed set is from the cursor or initial seed.
Since every changed cell was read at some tick before the last update,

    1 + max_{q in E} ||q-p_s||_1 <= T <= min(A_(x+y)(E),A_(x-y)(E)). (2)

Thus a complete discrepancy of bounded oblique span cannot be placed
arbitrarily far from the actual starting cursor. The statement is
therefore a genuine causal tether for a bounded-SPAN complete discrepancy,
not just a bound on the separation of the two endpoint cursors.

## 2. Proof and shared infinite backgrounds

For z=x+y the retained strict integer clock is

    Theta_c(B,p,h)=-sigma sum_{q in B} (-1)^(q_x+q_y) f(z(q)-c)
                    + J(z(p)-c,epsilon(h)),
    f(a)=3^|a|-1.

Every actual fine step raises it by at least one. The rotated x-y clock has
the corresponding opposite sector sign and rotated heading sign. At equal
endpoint pose, the J terms cancel EXACTLY. All field terms outside E cancel
as well. Thus for EVERY integer center c,

    T <= Theta_c(X_t)-Theta_c(X_s)
       <= sum_{q in E} f(z(q)-c).

Taking the least right-hand side proves the first inequality. Choosing an
integer midpoint of [lo_z,hi_z] puts every q in E within ceil(w_z/2) and
proves the second. If E were empty, this would instead give T<=0.

The full field may have an arbitrary common INFINITE background at both
ends. Restrict the starting field to the finite cells read by this finite
actual interval. First-difference induction preserves the path and both
endpoint poses; its endpoint XOR remains exactly E. Apply the finite-board
proof there. No infinite field sum is assigned a value.

Dependency: continuation_2026-10-22/ant_continuation2/planar_structure/
finite_white_episodes.md Section 4 records the exact strict clock and its
rotated version; its underlying source is the retained Ke clock theorem.
This note adds the optimized COMPLETE-XOR comparison, not a new clock.

## 3. What a sparse recurrent-pose sequence would have to do

Suppose a single actual orbit has infinitely many checkpoints of black mass
at most K. The retained axial separator theorem puts all such heads in a
fixed bounded set of at most (K+2)^2 cells, with two sector-compatible
headings per cell. Hence an infinite subsequence has one identical pose.
Fix its first checkpoint s. At each later such checkpoint t, |E|<=2K.
For either z separately, (1) forces

    ceil(span_z(B_s XOR B_t)/2)
       >= min { r>=0 integer : 2K(3^r-1) >= t-s }.

Thus the COMPLETE discrepancy must spread in BOTH oblique coordinates at
least logarithmically with the elapsed return time. A proposed return whose
ENTIRE changed support is one bounded-span cap, placed remotely, is not
sufficient: its small complete-XOR span would
bound that actual interval's duration and hence its distance from the cursor.
If one cap is moved away from an old cap, BOTH belong in E; then E can have
large span, and this theorem does not discard the old cap for free.

This does NOT prove pointwise black-mass divergence. Sparse boards can have
large two-dimensional spans, and different checkpoints may carry far-separated
archive pieces. Initial black mass plus current black mass bounds the number
of discrepancy cells, not their positions. No such support-tether theorem for
arbitrarily spread discrepancies has been proved here.

## 4. An exact small countercontrol to a clock-only closure

Even identical cursor pose, all axial charges, and ALL translated oblique
strict-clock inequalities do not enforce continuity between endpoint states.
For n>=1 define candidate states

    p=(0,0), h=N,
    B_n=F UNION {(0,2n),(1,2n)},
    F={(-10,-10),(-10,-11),(-11,-10)}.

Every board has exactly FIVE black cells. The fixed F is an inert common
background for this endpoint calculation, not a claim of physical inactivity
on an actual orbit. Every exact alternating row and column sum is unchanged
between B_n and B_(n+1). Both pose and sector agree. The boards are distinct.

For z=x+y, the changing board contribution to Theta_c is

    g(2n-c),        g(a)=f(a+1)-f(a).

For z=x-y it is -g(-2n-c). Therefore the two successive clock differences are

    g(2n+2-c)-g(2n-c),
    g(-2n-c)-g(-2n-2-c),

respectively. The exact values g(-1)=-2, g(0)=2 and

    g(a)=2*3^a for a>=0,
    g(a)=-2*3^(-a-1) for a<=-1

show each difference is at least EIGHT for EVERY integer c, with equality
at the two central choices. So the entire infinite endpoint chain can be
assigned eight units of elapsed clock time per edge while passing every one
of these strict-clock tests and all exact axial charges. It even keeps mass
five, so invoking only the retained eventual mass-at-least-five result does
not distinguish it.

But NONE of these proposed eight-read transitions can be an actual ant
interval. The NEW black cell (0,2n+2) must be read. Starting at (0,0),N,
movement axes alternate with the first movement horizontal, so this read
cannot occur before tick 4n+4; its enclosing interval has length at least
4n+5>8. The strict clock centered at the appropriate central c, on the other
hand, bounds any actual such interval by eight. Contradiction.

This is a nonreachable endpoint RELAXATION, not an ant counterexample or a
proposed simulation. It is a sharper small illustration of the already
retained teleporting-face-loop limitation. If one ignores live-cursor
continuity, each domino shift can also be implemented by filling the white
square one level above the old domino, then erasing the black square below
it, teleporting the live ant between the two legal four-read loops. The
moving part has mass two at boundaries and at most six during the two loops;
F makes those bounds five and nine. No physical concatenation is asserted.

## 5. A usable global route and its exact missing premise

The new proved estimate supplies a correct terminal test for a spatial
archive ledger: a claimed bounded complete-XOR return cap must obey (1),
so relocating it far away cannot be used as a free cursor reset. Keep the
entire changed support, including dormant archive strings, in the ledger.

To turn this into a global theorem one would need an independent causal
statement controlling the SPREAD of complete discrepancies at repeated
nonstandard return sections, or a paid decomposition into physically
connected return excursions whose total span/refund credit is finite.
No mass-only root count, profile count, core-grafted connectivity predicate,
bounded C-age statement, or finite collection of endpoint clock inequalities
supplies that premise. The five-cell endpoint chain above gives a compact
countercontrol to a proposed proof that omits actual travel between changes.

The generic support-spread premise remains OPEN. This note neither establishes
universal capture nor silently promotes a clock reformulation to a proof.
