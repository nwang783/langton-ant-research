# Cubic global bound on actual archive renewals

23 October 2026. Author theorem, frozen for independent audit. The geometric
dependency is bound below; do not call this independently signed until both
it and this application have received an independent PASS.

## Frozen geometric dependency

For a vertex-simple n-unit-edge path in the square lattice, n>=2, its interior
right-minus-left quarter-turn S satisfies

    |S| < 8*sqrt(n-1)+2 <= 8*sqrt(n)+2.

For n0 or1, interior S=0. The source is
../simple_path_turning_2026-10-23/PROOF.md, SHA256
8647be7a9158e11985f60a7643c64411d0cd396e73449ed02032c084f7e7303f.
It proves this by the chord-argument lift on the parameter triangle and
endpoint polar-angle crossing charges.
No mean winding, random-walk, or monotone-spiral heuristic is a premise.

## The actual w-exceptional renewal count

Partition an arbitrary actual finite interval into complete R^r L blocks,
plus a final R-only run. Call a complete block exceptional if r>=3 or its
L is nonbridge in the FULL current w black graph. Let E count these blocks.
Every such block ends in a cycle-erasing L in at least one black graph:
for r>=3 use the opposite unit cycle, otherwise the w nonbridge itself.
Consequently E<=D, where D counts all physical cycle-erasing updates once.
An r3 block can only be the initial partial block; proper post-L blocks
have r0/1/2/4. No complete R run exceeds4.

The E exceptional blocks divide ordinary r<=2 w-bridge blocks into E+1 epochs.
Let M_j be the COMPLETE actual black mass at epoch entry. The signed exact
far-side inheritance theorem implies that ordinary blocks traverse a single
vertex-simple path of n_j INITIAL w bridges, with n_j<=M_j. Their newly
written or newly attached state stays physically behind, even if some R
writes create cycles or some ordinary L deletes an opposite z nonbridge.
Thus no no-cycle-birth or no-z-erasure hypothesis is imposed.

## Mass gain is geometric turning, not independent reproduction

For each proper ordinary block, r0/1/2 corresponds to a left/straight/right
w turn and net mass change r-1. Thus the total ordinary-epoch mass change
is the interior signed turning of its n_j-edge path, plus its FIRST block's
contribution r-1<=1. The first ordinary block of an arbitrary interval may
lack a predecessor within the interval, but its mass contribution is still
at most1 and the subsequent turns are the same actual path interior turns.

The geometric dependency therefore gives, including n_j0/1 safely,

    mass after ordinary epoch <= M_j+8*sqrt(M_j)+3.

A following exceptional block has r<=4 and mass change r-1<=3. Hence

    M_(j+1)<=M_j+8*sqrt(M_j)+6 <= (sqrt(M_j)+4)^2.

By induction, with entry mass m=M_0,

    M_j <= (sqrt(m)+4j)^2.                              (1)

This is not mass descent: masses can increase at every epoch. It bounds the
rate at which successive archive renewals can grow their complete boards.

An ordinary block costs r+1<=3 updates. A following exceptional block costs
at most5. The final R-only run costs at most4. Therefore

    T <= sum_(j=0)^(E-1)(3M_j+5)+(3M_E+4)
      <=3*sum_(j=0)^E(sqrt(m)+4j)^2+5E+4
      =3(E+1)m+12*sqrt(m)*E(E+1)
        +8E(E+1)(2E+1)+5E+4
      <=16*(E+sqrt(m)/4+1)^3.                           (2)

The last inequality follows by expansion: putting a=sqrt(m), the right
cube minus the previous polynomial is

    24E^2+(12a+35)E+a^3/4+12a+12 >=0.

For T>=0, the implied lower bounds are

    E >= (T/16)^(1/3)-sqrt(m)/4-1,
    D >= (T/16)^(1/3)-sqrt(m)/4-1.                      (3)

Negative lower bounds on short intervals are harmless. In particular the
number of actual w-exceptional archive renewals, and hence actual dual cycle
erasures, grows at least on a cube-root scale, not merely logarithmically.
These bounds are uniform in the initial black-cell positions and diameter,
in the full passive field, and in the starting time/cut of the interval.

This still does not prove positive renewal density, a finite nonstandard
renewal budget, pointwise mass divergence, or universal standard104 capture.
Standard and known nonstandard translating waves both have such renewals.
The sharpness of the cubic ant bound is not asserted; only the geometric
square-root turning order is expected to have a separate spiral control.

## Targeted actual-ant controls

check_cubic_renewal.py checks every prefix and every actual ordinary epoch of
three standard104 periods, the single-erasure rods r1,3,30,100, and blank1000.
It verifies the geometric turn SIGN against full physical cursor vectors,
first-block correction, exact mass/turn identity, simple old-bridge path,
quadratic epoch-mass bound and both displayed cubic inequalities. Every full
board and all earlier writes are retained. These controls do not prove the
universal geometric premise or replace its separate analytic proof.
