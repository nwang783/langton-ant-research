# Opposed mixed runs across one fold have disjoint coarse centers

Status: the finite invariant and the scheduling argument have both passed
independent analytic review. This strengthens the older at-most-four
entry-center bound, and also includes terminal boundary centers.

Let X F Y be physically feasible, with X,Y over U,V and F in Q,B. The
coarse-center sets of the X and Y paths are disjoint. Each path includes
its macro-entry centers and its terminal boundary center. No assertion is
made about fold-interior centers, nonadjacent runs separated by several
folds, or C-containing histories.

For a north-facing head p, the center is p+(-1/2,1/2). For a south-facing
head p', the center is p'+(1/2,-1/2). Coincident centers therefore require
p'=p+(-1,1).

The audited downward-sweep certificate of `one_fold_v_freshness.md` has
56 states with both sides active. Every such state has dx<=-2, including
the conservative far representatives. Thus none has (dx,dy)=(-1,1).
The checker now explicitly asserts this maximum-dx invariant.

Suppose a shared center existed at old head height a and new head height
a+1. Before the old target is reached, its immediately preceding sweep
frontier is at least a+3, because every old backward step lowers height by
3 or 4. Before the new target is reached, its preceding frontier is at
least a+4, so its read ceiling is at least a+5.

If the old frontier reaches its target first, the new ceiling is higher
than the old ceiling a, so the scheduler must advance the new side until
its target is reached; the old side cannot pass its target first. If the
new frontier reaches its target first, its ceiling is a+2, while any
not-yet-arrived old frontier has ceiling at least a+3; the old side must
advance until it reaches its target. Hence a both-active state with
(dx,dy)=(-1,1) must occur.

An exhausted side need not be stopped immediately. It can be kept active
until the scheduler would next select it. The preceding inequalities show
that this does not prevent reaching the target state, even when the target
is a terminal boundary of Y. All both-active states are retained by the
original freshness sweep; its goal-dependent stop-side pruning therefore
does not affect this argument.

Finally, X's terminal center cannot equal any Y center already by the
kinematic count identity j=remaining(X)-2: at the X terminal boundary the
right side is -2, whereas j>=0. This also handles an empty X. The same
scheduler argument handles an empty Y whenever its sole terminal/initial
center is considered.

Therefore the assumed shared center is impossible.

Artifacts: `one_fold_sweep_quotient_certificate.json`,
`one_fold_sweep_quotient.py`, and
`../audits/check_one_fold_sweep_independent.py`.
