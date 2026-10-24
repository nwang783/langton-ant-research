# A finite-support chain splitter and its inverse-port obstruction

24 October 2026. Author proof and actual finite-board controls, pending audit.
This is a one-shot module transformation, not a reusable compiler or a
counterexample. Exact finite-board reversal is a RETAINED fact, not a new result.

## 1. Explicit forward construction

Start at cell (0,0), north, with exactly the n black cells

    Q_n = {(-i,i): 1<=i<=n},    n>=1.

In the fixed w sector k=1 this is one straight n-edge passive component, and
the initial w cursor (1,-1) in doubled coordinates is isolated. On this exact
finite board the next 5+2n turns are

    RRRRL (RL)^n.

The head ends at (-n-1,n), west. The complete final black field is

    H union P_n,
    H = {(0,-1),(1,-1),(1,0)},
    P_n = {(-i,i-1): 1<=i<=n}.

In k=1, H is a complete three-edge star and each member of P_n is a separate
singleton component. The maximum active w mass in the prefix is exactly n+4.
Thus n=2 is an actual cap-six control converting one 2-edge module into two
singleton modules plus a three-edge star. Singleton count increases from zero
to two. This falsifies singleton-only monotonicity at cap six, not every weighted
component-type potential.

Proof by exact fields. The first four R updates add the four edges around the
initial w vertex, importing Q_n at the first update. The L removes the cell
(0,0), leaving H passive and Q_n active. After j further RL pairs, 0<=j<=n,

    head = (-j-1,j), west;
    field = H union {(-i,i-1):1<=i<=j} union {(-i,i):j<i<=n};
    active component = {(-i,i):j<i<=n}.

The next R adds cell (-j-1,j), and the next L deletes (-j-1,j+1), verifying the
induction directly. The new singleton and older outputs have disjoint vertex
sets in k=1, so no passive component or output edge is being erased from the
bookkeeping. After four initial R turns the active mass is n+4; subsequent
masses are at most n+1. The formulas prove the construction for every n.

## 2. The retained inverse, and why it is not a linked merger

Let T be the standard ant update, with DIR(h) the incoming unit heading.
The retained finite-board reversal involution is

    J(p,h,B) = (p-DIR(h), h+2 mod4, B),
    J T J = T^{-1}.

It does not complement the infinite background. Applying it to the splitter's
exit gives the inverse prefix entry at (-n,n), east, on the SAME field H union
P_n. After 5+2n updates it reaches (0,-1), south, on Q_n.

However, this is not a dispersed-module merging gate in the forward component
system. The reversed entry uses sector k=0. In that sector ALL n+3 edges of
H union P_n form one simple active path. Its endpoints are (-2n-1,2n-1) and
(1,1) in doubled coordinates, and the reversed cursor is at the first endpoint.
Thus the forward singleton decomposition is not preserved by time reversal:
J exchanges the paired w/z roles.

There is also an exact pose obstruction, independent of the board. Every
standard update preserves

    epsilon = p_x+p_y+h mod2,

because both position parity and heading parity toggle. J changes position
parity but not heading parity, so it flips epsilon. The forward splitter exit
and its required inverse-entry pose therefore lie in different invariant
sectors. NO standard-ant continuation of the forward run can reach that exact
inverse-entry pose on the same coordinates, even if arbitrary extra routing
cells were available. This rules out the naive "split, route back, reverse"
compiler, not a separately translated or rotated inverse gadget.

An odd translation or a quarter rotation can repair sector compatibility of a
separately placed gadget, but it also changes the required spatial field and
ports. A legitimate reusable compiler still owes a single finite pre-funded
field that transports the actual cursor and all required complete modules
between compatible ports, accounting for every emitted archive and fresh
blank-cell use. No such linked construction is supplied here.

## 3. Exact controls

chain_splitter_control.py checks every intermediate complete field, active
component, invariant sector, end state, and literal inverse replay for n=1..64.
The output includes full cut traces at n=1,2,3. These are finite controls for the
all-n proof, not a simulation-based proof of indefinitely reusable behavior.
The n=2 prefix is also cap-six kernel first-return path 4895; its complete
transition profile is frozen separately as kernel_M6_two_singleton_births.json.
