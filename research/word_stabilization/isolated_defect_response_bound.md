# Explicit finite-mass response bound for an isolated bad window

Status: the quantitative combination and the finite-prefix barrier have passed
independent analytic review; the H finite-path bounds were separately replayed.
It is NOT a universal
capture-time or total-defect bound.

## Statement

J(t) and K(t)=J(t-1)J(t) use the ending-time convention of
adjacent_defect_highway_theorem.md. Suppose J(t-1)=0 and J(t)=1. Let m bound
the black mass immediately before, or immediately after, turn t. Then a later
adjacent pair K(u)=1 occurs with t<u<=t+D(m), for the explicit primitive-recursive
function below. Its enormous size is deliberately not optimized.

Put N=270902, the number of vertices in the audited no-adjacent-J graph. For
nonnegative integer x define

    A(x) = (9/2)(x+11)(3^(x+7)-1) + 3x + 96,
    H(x) = 200 + A(x+100),
    T(x) = 12x + 400,
    F(x) = x + H(x) + T(x).

All quantities are integers since 3^k-1 is even. Finally put

    n0 = m+N+1000, n1=F(n0), n2=F(n1), D(m)=n2+2.

## Finite-prefix barrier against standard-cycle waiting

Consider any actual finite prefix from turn t-10 onwards with K(s)=0 for all
its available right endpoints s>=t. It is a path in the no-adjacent-J graph
once its first149 letters have been read.

Suppose a history on the W104 cycle occurs at time v. Its149 letters are a
standard-word factor, so J(v-139),...,J(v) are all zero. Let s be the latest
J event in [t,v]. It exists because J(t)=1, and satisfies s<=v-140. The absence
of K gives J(s-1)=0. If the graph path stays on W104 for nine further edges,
then no J occurs between s+1 and v+9. The160-turn word from s-10 to s+149 is
therefore one of the20 isolated-event survivors in the independently audited
certificate. Its149-letter suffix is outside the set of925 histories that
can reach W104 through ten-legal edges. But s+149<=v+9, and the actual
continuation supplies exactly such a ten-legal path to the W history at v+9.
This is a contradiction.

Thus no W104 visit can persist for nine further internal edges. In particular,
no W104 vertex repeats. This is a finite-prefix statement: it does not assume
that the no-K prefix continues forever or that the eventual ant orbit is standard.

## The other two cyclic components

The only other cyclic SCCs are T24 and H. Each can be visited at most once,
since the condensation graph is a DAG. Every vertex outside these two SCCs
is visited at most once, including W104 by the preceding argument. Hence
there are at most N+2 edges outside the two internal SCC visits.

For an H visit entered with black mass at most x, the marker return gaps are
at most74. Every nonmarker path in H extends at both ends to marker returns,
so its length is bounded by that same maximum. The before-marker cut is12 reads before its after-marker port. Thus
74+12=86<100 turns of padding at each end suffice. Removing at most100 turns
at each end of a finite H visit leaves a concatenation of complete before-marker
five-macros. Its entry mass is at most x+100. The arbitrary finite five-macro
bound in five_macro_finite_interval_bound.md is A(x), obtained by adding105
to the non-C-ended bound evaluated at x+12. Thus the whole H visit has length
at most H(x)=200+A(x+100). If no complete macro remains, its length is already
less than200.

For a T24 visit, discard at most23 turns at either end to align full copies of
the canonical24-word. Every full period needs two distinct first-L ray cells,
fresh relative to this period factor. If r full periods remain, then
2r<=x+23. Its length is at most46+24r<=12x+322<=T(x).

## Mass bookkeeping

Rewinding from the state at t to the cut before turn t-10 raises the mass by
at most11. The initial149 turns and all at most N+2 ordinary graph edges
raise mass by at most N+151 in total. Thus n0=m+N+1000 is a conservative
bound before the first exceptional SCC visit, even if all ordinary steps are
charged in advance. H and T are monotone. In either possible order of the
at most two SCC visits, the first costs at most H(n0)+T(n0), and the second
costs at most H(n1)+T(n1), with n1=F(n0).

Therefore the entire no-K prefix, counted from t-10, has at most

    N+151 + H(n0)+T(n0)+H(n1)+T(n1)
    = N+151+n2-n0
    < n2

turns. The ample slack in D(m)=n2+2 covers both endpoint conventions.
A prefix having no later K through t+D(m) is impossible. This proves the
claimed response bound.

## Scope

The bound applies after an isolated-on-left J event. It does not bound the
waiting time from an arbitrary configuration to its next bad window, the
capture time of an arbitrary finite seed, or the total number of bad windows.
Ordinary standard-highway flights before encountering distant debris remain
unbounded in distance at fixed black-cell cardinality.
