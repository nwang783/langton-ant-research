# Two bounds on retreat force an eventual periodic trace

## Status

This is a sufficient geometric condition for an arbitrary finite-support
Langton-ant trajectory to become periodic up to translation. It does not prove
that every finite input satisfies the condition, and it does not classify the
resulting period as 104. The proof retains all old black cells until a direct
inequality proves that the future cannot read them.

## Theorem

Let p_t be the ant position. Suppose that, from some time onward, there are
two linearly independent real linear forms l_1,l_2 on R^2 and nonnegative
constants b_1,b_2 such that

    l_i(p_t)-l_i(p_s) >= -b_i

for i=1,2 and every pair of times s<=t in that tail. Then the movement and
turn trace is eventually periodic up to a nonzero lattice translation.

Let

    W = {v in Z^2: -b_i <= l_i(v) <= b_i for i=1,2}.

The set W is finite. A period of the eventual trace is at most 4*2^|W|.

The hypothesis bounds every later retreat, not merely the distance behind
a linearly moving reference point. In the special case l_1(x,y)=x and
l_2(x,y)=y, it says that the ant never later falls more than a fixed amount
behind any earlier x-coordinate or y-coordinate.

## Proof

Restart time at the beginning of the assumed tail. This changes the finite
initial black set but preserves finite support. Write B_0 for that set.

### 1. At least one form tends to positive infinity

Each l_i(p_t) is bounded below by l_i(p_0)-b_i. If both forms were also
bounded above, linear independence would confine the path to a bounded
region. This contradicts the standard unboundedness theorem.

At least one form, say l_j, is therefore unbounded above. The retreat
inequality makes it tend to positive infinity: after a time s with
l_j(p_s)>A+b_j, all later values exceed A.

Choose a time t_0 such that, for every t>=t_0,

    l_j(p_t)-b_j > max {l_j(q): q in B_0}.

If B_0 is empty this condition is vacuous. At every such t, no future ant
position can equal a point of B_0, since all future l_j values are at least
l_j(p_t)-b_j.

### 2. Every old black cell that can be read lies in p_t+W

Fix t>=t_0. Each black cell q at time t is either in B_0 or was visited at
an earlier time s<t. The first type cannot be read after t, as just shown.

For the second type, q=p_s. Apply the retreat inequality from s to t:

    l_i(q-p_t) <= b_i.

For every future position p_u, u>=t, apply it from t to u:

    l_i(p_u-p_t) >= -b_i.

Thus, if this q is ever read after t, it satisfies both sides of the bounds
defining p_t+W. Every black cell outside that window is future-invisible.

This conclusion concerns actual physical cells. It is not based on a local
mask being repeated, a guessed future direction, or an erased history.

### 3. Delete only cells proved future-invisible

At time t keep the heading and position and replace B_t by

    C_t = B_t intersect (p_t+W).

The actual future movement and turn sequence do not change. If there were
a first change, it would occur when the original path first reads a cell
whose color differs between the two initial states. All such cells were
black cells outside p_t+W, already proved not to be read. This is a
contradiction.

### 4. Repeat a complete reduced state

The centered reduced state (C_t-p_t,h_t) has at most 4*2^|W| possibilities.
Two times s<t among any 4*2^|W|+1 consecutive sufficiently late times have
equal centered reduced states. The reduced states are literal finite
Langton-ant states. Determinism and translation covariance give, for every
n>=0,

    p_(t+n) = p_(s+n)+(p_t-p_s),
    h_(t+n) = h_(s+n),

and the turns at these two times agree. Section 3 transfers those equalities
to the original trajectories.

The displacement p_t-p_s cannot be zero: that would confine the tail to the
finite positions of one repeated period. Therefore the tail has a nonzero
translation period. Its period t-s is at most 4*2^|W|. QED.

## What this changes in the global target

A proof of bounded retreat in two independent directions would establish
eventual periodicity without first proving confinement to a strip. The
argument provides the required separation of active and inert cells.

Neither an asymptotic direction nor sublinear transverse error supplies
these inequalities. A path can have a limiting direction and make retreats
of unbounded size. The present theorem leaves that global issue open.

Even after eventual periodicity, a full proof of the standard-highway
conjecture still needs a classification of finite-support periodic traces.

## Dependencies and priority

The only Langton-specific theorem used is that a finite-support trajectory
cannot stay in a bounded region. The remaining proof uses locality,
translation covariance, and finite-state deterministic evolution after
the future-invisibility argument. No novelty or priority claim is made.
