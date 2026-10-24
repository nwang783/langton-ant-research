# Cap-free actual-channel packing and voltage cycles

24 October 2026. Author general chronology lemma pending independent
review. No multiplicity cap, first-color, stream-height, WHITE-front or
geometric noncrossing hypothesis is used. The key premise is known
CONTIGUOUS ACTUAL one-step successor channels of ONE cursor. A lifetime,
repaired contour, b-path or port-flow path is not automatically such a
channel. No known OPEN calendar is excluded merely by citing this lemma.

## 1. Finite physical channels occupy disjoint whole intervals

A finite literal channel C_i is a sequence of m_i distinct read EVENTS
whose consecutive events are known actual successors, exactly one step
apart. If it starts at S_i, it occupies EVERY integer time in
[S_i,S_i+m_i-1]. Distinct channel occurrences cannot overlap: one cursor
cannot perform two different reads at the same time.

Suppose a genuine physical per-cell rank order places event u of channel
A strictly before event v of a DIFFERENT channel occurrence B. The WHOLE
A interval must precede the WHOLE B interval, not merely u before v.
Thus

    start(B) >= start(A)+m_A.                          (1)

This is stronger than a relaxed constraint T(v)>=T(u)+4 when u is early
in A and v late in B. If two known rank orders demand A before B and B
before A, there is no actual cursor chronology even when those relaxed
event difference constraints are feasible.

For finite physical partial networks with all known successor components
open, form the channel-precedence graph from all genuine per-cell rank
orders. A directed cycle is impossible. Conversely, if this graph is a
DAG and every within-channel rank constraint is already correct, its
topological order gives an INJECTIVE ABSTRACT clock: place whole channels
far apart and satisfy all finite cross-channel rank gaps. When compatible
mod-four channel phases are supplied, choose each large gap in that
residue. This is not sufficient for physical exterior connectors or a
legal prepared board; it settles clocks only.

## 2. Full-drift quotient: occurrences, offsets and signs

Now assume one actual FULL P-event orbit with drift d and
T(e+d)=T(e)+P. P need not be minimal and d need not be primitive. Each
known event class belongs to one OPEN known successor channel. Lift that
channel's consecutive reads explicitly and let its start time be S_i.
At offset q, write its physical lifted event as

    e_(i,q) = canonical(u) + kappa_(i,q)*d.

Choose ONE canonical physical cell representative for all ranks of that
cell class. If representatives are instead chosen separately, first
insert their additional physical comparison voltage; do not compare
ranks at different physical translates as though they were one cell.
The canonical event time is exactly

    T(u) = S_i + q - kappa_(i,q)*P.                    (2)

For a physical rank comparison u<v at that SAME canonical cell, put
u in C_i at offset q and voltage kappa_u, and v in C_j at offset r and
voltage kappa_v. The actual channel occurrences containing these reads
start at S_i-kappa_u P and S_j-kappa_v P.

If i=j AND kappa_u=kappa_v, they are the same occurrence: check the
internal offset order and required rank gap directly. Do not add an
artificial whole-channel self precedence.

Otherwise they are different physical channel occurrences. Apply(1):

    S_j-S_i >= m_i + nu*P,  nu=kappa_v-kappa_u.        (3)

If the rank comparison also supplies a valid lower bound g on T(v)-T(u),
combine it with(3) to obtain

    S_j-S_i >= w + nu*P,
    w=max(m_i, g+q-r)>0.                              (4)

One may safely use only w=m_i when no stronger gap is supplied. All
channel lengths and voltages are actual; no graph repair is made.

## 3. Exact packing-cycle obstruction

Sum(4) around ANY directed cycle of channel precedences. Put

    k = -sum_cycle nu.

Then the necessary inequality is

    k*P >= sum_cycle w > 0.                           (5)

The sign k is the TEMPORAL winding of the physically aligned channel
occurrences. If k<=0, the proposed partial chronology is impossible for
EVERY positive P. If k>0, the bound retains that exact k:

    P >= ceil(sum_cycle w / k).

It is not legitimate to replace k by1 or declare every directed quotient
cycle impossible. A positive-voltage old-stock cycle is a real escape.
This is a necessary packing test, not a sufficient full-period solver.
Unrelated channels must also have disjoint phases, known classes fit in
P, and all exterior colors and connectors remain to be verified.

## 4. Closed known successor cycles are a separate case

If a known successor component is CLOSED with m distinct event classes
and full-drift voltage a, exact actual steps give aP=m>0. The full orbit
has P distinct event classes, so m<=P; therefore a=1,m=P. Such a known
cycle would already be the ENTIRE actual P-event orbit. Any required
event class outside it contradicts the one-cursor full orbit. An embedded
lifetime/flow cycle is not subject to this conclusion unless every edge
is a literal actual successor.

## 5. What the controls establish

The checker supplies an abstract two-channel relaxation with13 events
per channel and crossed rank orders at offsets0/12. Event max-plus
constraints allow equal starts, but the zero-voltage packing cycle
requires0>=26, impossible. This is explicitly not a physical ant factor.
It also gives a disjoint phase calendar at positive winding, including
winding2, to prevent a false acyclicity shortcut across period translates.
Those calendars are not color-correct exterior completions or fronts.

This lemma does not exclude the peer's retained OPEN79 calendar, which
already has disjoint whole-channel phases. It is available for other
partial interfaces whose relaxed max-plus constraints have not yet been
strengthened to actual whole-channel packing.
