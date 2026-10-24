# An actual all-parameter DC/V return family with fixed C age

23 October 2026 11:19 UTC. Author finite symbolic certificate passes; independent
reconstruction requested. This is a family of finite supported words, not an
infinite trajectory, renewal gadget, or an unfunded-record counterexample.

For EVERY integer r>=0 there is a finite board of exactly3r+9 black cells
whose actual ant, entering at(0,0,N), executes

  DC V^r VCC V^(r+2)

and its actual final M11 marker. The raw duration is36r+109, or36r+120 including
the final marker. There are exactly3 C. The final V starts at(0,1,E), consumes
BOTH original first-DC outputs(3,1) and(2,0), each source-included age3, and ends
at(3,0,E). Final raw black mass is11r+30. Thus even within this exact protected
two-sibling reconvergence, fixed C age allows arbitrarily many V helpers when
the entry mass grows. The r=0 member is the signed nine-cell control, and r=1
is the signed twelve-cell refinement. Initial helpers can fund later events;
this is not a positive strict-unfunded V1 record control.

## Complete finite proof for all r, without a parameter cutoff

Let p_n=(1,2)+n v, v=(-3,1), and w=(-4,0). The outgoing V packets are at p_n,W,
for n=0,...,r-1. The far VCC is at p_r,W. The returning V packets are at p_n+w,E,
for n=r,r-1,...,-1. The final marker starts at(3,0,E). These are exact literal
packet endpoints, not freely moved cores.

Every physical cell is uniquely represented by integers ell,delta as

  (x,y)=(1+ell-3delta, 2+delta).

For a literal read at local offset(dx,dy) from p_n, put ell=dx+3dy. It reaches
the cell with delta=n+dy. Write epsilon=delta-r. For each fixed ell, a finite
inventory of raw read atoms from DC, V, VCC and the final marker gives EXACT
membership conditions:

- Initial DC and final marker atoms: delta equals their fixed dy.
- Outgoing V atom: delta>=dy and epsilon<=dy-1.
- Far VCC atom: epsilon=dy.
- Incoming V atom: delta>=dy-1 and epsilon<=dy.

All parameter feasibility is delta>=epsilon, equivalent to r>=0. Atom order is
also exact and independent of the parameter: initial DC, outgoing atoms sorted
by DECREASING dy then local time, far VCC by local time, incoming atoms sorted
by INCREASING dy then local time, final marker. This follows respectively from
increasing and decreasing packet index n, since n=delta-dy.

For each ell, partition the integer delta and epsilon axes at ALL constants
occurring in these guards, using singleton constants and intervening integer
intervals. Discard a rectangle only if no delta>=epsilon is possible, i.e. if
its delta upper endpoint is smaller than its epsilon lower endpoint. Every
atom's presence and the complete ordered visit word are then constant on the
rectangle. Checking that consecutive turn symbols alternate is exactly the
literal color-consistency criterion at that cell. It is both necessary and
sufficient: choose initially black precisely those cells whose first symbol
is L. Every later visit then has the prescribed color after previous flips.

The complete certificate has177 feasible rectangles and339 read obligations.
ALL visit words alternate. It separately verifies that the canonical five-cell
entry core is initially black for every feasible parameter. All raw packet
entries carry the required M11 prefix, and the actual final marker is included,
so the signed literal packet ledger applies at every marked boundary.

## Exact finite seed and mass, rather than an asymptotic count

The initial seed is defined without guessing: for the chosen r, take the cells
(1+ell-3delta,2+delta) in the25 rectangles whose first turn is L, on the diagonal
epsilon=delta-r. Other cells are initially white. Each such rectangle with
bounds delta in[a,b], epsilon in[c,d] contributes exactly

  max(0, min(b,r+d)-max(a,r+c)+1),

omitting infinite endpoints from min/max. Each fixed-r contribution is finite.
Every branch change or zero crossing occurs at a difference of finite interval
endpoints (or the immediately adjacent integer). The largest nonnegative such
difference is4. Exact values through6 and the affine final-ray slope therefore
prove the closed formula3r+9 for ALL r, rather than extrapolating an empirical
scan. The certificate retains the interval bounds, all visit words, endpoint
differences and exact values so a separate checker can reconstruct this proof.

Literal controls for r=0,1,2,5 are also replayed directly with the current
ordered identities, canonical core partition, exact physical head, every turn,
and the final protected two-input ancestry. These are positive controls for
the parameter encoding; the universal theorem uses the finite rectangle proof,
not these sample values. The final mass formula follows from the exact packet
gains4 per V and3 per C: initial3r+9 plus4(2r+3)+9 equals11r+30.

Files: check_dc_V_return_family.py and chronology_dcuv/dc_V_return_family.json.
No capped search, new counted threshold, spatial teleport
is involved. This demonstrates why recursive helper obligations alone need a
separate bound on available resources/history before implying finite fuel.
