# A prescribed-input oblique cylinder has a computable all-period bound

23 October2026,09:21UTC. Independently signed LK analytic derivation from the
previously signed scalar clock. This is a FIXED-width
construction/decision bridge, not a global front classification.

## Precise setting

Fix a nonzero lattice drift D=(dx,dy) with BOTH components nonzero. A front
has a heading-restoring turn period, hence dx+dy is even. Fix a finite set Q
of physical cell representatives modulo ZD which contains every read orbit.
Its complete bulk input bit I(q) is specified on Q. Bulk OUTPUT bits O(q)
are not prescribed. Fix one of the two physical pose sectors.

A complete front means each orbit's finitely many chronological reads in the
bi-infinite translated period alternate, starting with R if I=0 and L if I=1.
Equivalently a one-sided infinite front may have a finite head correction to
the periodic input. No initial infinite background is being confused with a
finite-on-white counterexample; this is an interface model.

There is an effectively computable finite upper bound for the period length
P, and hence for every per-orbit visit count, depending only on D,Q,I and the
sector. Consequently existence in this precise fixed cylinder is decidable
without supplying a visit or period cutoff.

## Proof by the existing strict scalar clock

Choose an integer normal ell to D. Since D is oblique, both coordinates of
ell are nonzero. A physical quarter rotation makes its coefficients u,v
positive. Use the signed clock in
`computability/oblique_strip_clock_obstruction.md`, Section1, with

    a=4^u, b=4^v, w(q)=a^(q_x)b^(q_y)/r,
    f(q)=M(w(q)+1/w(q))-2,
    Theta=-sigma sum_black chi(q) f(q)+J_h(p).

Here chi(q)=(-1)^(q_x+q_y), sigma chi(p)=(-1)^h, r may be any positive rational
normalization, and the stated rational M and J make EVERY literal update
increase Theta by at least2. All f(q) are positive. Since ell(D)=0, both f
and J are invariant under translation by D. The checker sign chi is also
D-periodic because dx+dy is even.

Sum the literal clock increment over the period's event occurrences modulo D.
Every outgoing pose is matched to the next incoming pose, possibly translated
by D. Hence all head terms cancel EXACTLY. At cell q, R-count minus L-count
is O(q)-I(q). Therefore

    2P <= -sigma sum_(q in Q) chi(q) f(q)(O(q)-I(q)).       (1)

No divergent sum over an infinite rail is taken. This is a finite sum over
one complete set of event-orbit representatives. Spectator input cells not
read in Q contribute zero.

The right side is bounded even when output bits are free. In particular it
is at most sum_Q f(q). A sharper computable bound maximizes each independent
term over O(q) in{0,1}, keeping the known I(q). All quantities are rational
under the displayed choice, so floor(bound/2) is an exact integer bound.

The same proof applies to a nonnegative REAL aggregate incidence relaxation:
introduce counts c(q,h,R/L), match each directed edge's outgoing and incoming
counts on the quotient, and impose R-L=O-I with 0<=O<=1. It has no nonzero
homogeneous even-visit circulation. Thus linear programming can sharpen all
count bounds before any chronology search. A rational dual, checked exactly,
is a standalone certificate of the sharpened bound.

Finally, with P bounded, choose the initial read representative in Q and its
heading. There are finitely many turn words of length at most P. Their lifted
positions are bounded by their length; all period endpoints and chronological
same-cell histories can be checked exactly. This is a terminating decision
procedure, not a claim of practical efficiency.

## Concrete return-wake control

The target is D=(-2,-2), sector BIT1 (x+y+h=1 modulo2), with the mature NE104 wake input from the
signed shifted_reverse104_bulk.md. Before any physical rotation, this bit convention
means multiplicative sigma=-1 in the clock formula, not sigma=+1. Physical
quarter rotation changes both the heading parity and that sign consistently.
For the13-row representative strip

    Q={(x,x+y-4):x in{0,1},0<=y<13},

OUTPUT bits were left completely free in[0,1]. Exact rational duals give
P<=224 and the successive per-site bounds

    0,0,0,0,0,1,2,3,11,6,29,24,35,42,22,27,10,6,3,2,0,1,0,0,0,0.

The central four-row strip Q={(x,x+y-2):x in{0,1},0<=y<4} gives P<=12 and
bounds0,1,2,3,3,2,1,0. These are incidence necessary bounds, not ant paths.

`bound_wake_return_flow.py` constructs the geometric equality system.
SciPy proposes equality/upper-bound multipliers, but Python Fraction arithmetic
checks EVERY coefficient inequality and the exact objective bound before
saving the JSON. The frozen JSON contains the complete rational multipliers
for total P and every individual site's count. No numerical tolerance is used
for certificate validity. The independent no-optimizer checker audits/check_oblique_cylinder_flow_independent.py
rebuilds the outgoing-event geometry and verifies every rational coefficient;
the concrete numbers are independently signed too.

## Scope and implementation caution

The normal of an AXIAL drift is axis-aligned, so the strict scalar clock used
here is unavailable. No corresponding axial all-cap bound is claimed.
The strip width, input profile and drift remain fixed. No global bound in
width, arbitrary initial seed diameter, or ant lifetime follows.

The adapted compact chronology solver must NOT inherit the white-front
normalization n0>0. A fixed prepared profile need not read its first strip row;
indeed the exact dual forces that row unused here. An actual-used-event time
anchor replaces that normalization. Early free-pattern UNSAT artifacts before
this correction are not used as proofs. The fully fixed opposite-sector
inverse104 positive control is unaffected and reconstructs exactly.
