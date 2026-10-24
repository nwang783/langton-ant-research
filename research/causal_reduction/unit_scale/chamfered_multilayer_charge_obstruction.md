# All clean layer jumps fail, not only odd-sector jumps

23 October2026,07:41 UTC. New analytic addendum submitted for independent audit.
This does NOT exclude decorated frame phases or wake-emitting corner work.

Fix r,k>=0 and write B_j=I_(r,k+j)+(0,j), j>=0, using the exact chamfered
input boards. All these boards have the same center. The signed frame identity
says that the literal frame at pose(0,j,E) takes B_j to B_(j+1) and returns to
that SAME pose. Each such individual operation is legal. They cannot simply
be concatenated because their starting poses differ.

## Board-charge equality

For every physical row y, define A_y(B)=sum_(x,y in B)(-1)^x modulo4, and for
every column x define C_x(B)=sum_(x,y in B)(-1)^y modulo4. The exact conserved
row/column charges in `../alternating_row_charges_mod4.md` imply

    A_y(B_j)=A_y(B_0), C_x(B_j)=C_x(B_0) for ALL j,x,y.          (1)

Indeed every individual frame has identical entry and exit pose, so its head
corrections cancel. This argument is finite at each j; no divergent sum is used.

## Pose separation by all row and column charges

Take the basis row test a_y(t)=[t=y], with antiderivative [t>y]. At pose
p=(x,z), its row head-correction vector is

    N: 2 on y<z, 0 on y>=z;
    S: 2 on y<=z,0 on y>z;
    E: 2 on y<z, (-1)^x on y=z,0 above;
    W: 2 on y<z,-(-1)^x on y=z,0 above.                         (2)

Compare with the vector at(0,0,E). Equality forces z=0 and a horizontal head.
The column correction is obtained by applying(2) to the counterclockwise
rotated pose(-z,x,h-1). It then forces exactly one of

    (0,0,E),   (-1,0,W).                                      (3)

The latter has the OPPOSITE invariant sector x+y+h modulo2. Therefore, in the
actual sector of(0,0,E), any pose with identical row and column head corrections
is precisely(0,0,E). This is a general charge-separation fact, not a clock or
an assumption about an ant path's spatial footprint.

By(1), ANY actual path from(B_0,0,E) ending on the exact clean board B_j must
end at(0,0,E). In particular no positive clean jump j can end at the natural
next pose(0,j,E), EVEN WHEN j is even. The earlier parity argument alone did
not rule out such even jumps.

The other three natural starts are rotations about the fixed center. Their
positions/headings are

    (-k-j-1,-2r-k,N),
    (2r-1,-2r-2k-j-1,W),
    (2r+k+j,-k-1,S).

For j>0 none is the first pose in(3), and the only alternate charge-equivalent
pose in(3) is sector-forbidden. Thus all four clean natural starts fail for
EVERY positive number of layers. A cyclic cut uses the corresponding intermediate
board and pose; conservation along that literal frame preserves the same
mismatched total invariant, so cutting the word cannot repair the obstruction.

## Quantified correction needed at a prescribed even jump

Suppose the desired final pose is(0,s,E), with s>0 even. Its row-head correction
minus the initial one is+1 in rows0,s and+2 in every row1,...,s-1. Therefore a
board D differing from the clean B_s must supply the negative of this vector.
Every changed cell contributes only+1 or-1 to its row charge. Consequently

    |D symmetric_difference B_s| >= 2s.                       (4)

This is a necessary interface correction, not sufficient ant chronology.
There is no extra column-head change for these two E poses at x=0.

The bound is SHARP for the modular constraints at s=2. For r,k>=3, the four
cells

    F={(1,0),(1,1),(-3,1),(-3,2)}

are white in B_2. The additive board B_2 union F has row-charge changes
(-1,-2,-1) in rows0,1,2 and zero column-charge change: F is two vertical black
dominoes in odd columns. Thus(B_2 union F,(0,2,E)) matches every row/column
charge and the invariant sector of the original state. This is only a positive
INVARIANT control. No legal path, renewal, or all-future mechanism is asserted;
other exact clocks and remote corner requirements may reject it.

The clean all-layer conclusion is stronger than a failed two-phase search.
The corrected four-cell control identifies the minimum missing bookkeeping
without pretending that a conserved-charge match constructs a physical cap.

## A strict clock also forbids bounded central repairs of even jumps

This additional argument uses the separately signed positive exponential clock
(`primitive_perron_clock_obstruction.md` Section3, inherited from the general
clock proof), not an assumption that modular invariants are complete.
In sector1, at X=Y=a>3, the strictly increasing state functional is

    Phi(B,p,h)=gamma_h a^(p_x+p_y)+sum_(x,y in B)(-a)^(x+y),

with gamma_E=2/(a+1) and the other standard clock coefficients. Every actual
update increases Phi strictly. Put P(r,k)=sum_(x,y in I_(r,k))(-a)^(x+y).
Directly summing the eight straight/diagonal black-side families gives

    F_r=(1-a^(2r))/(a+1),
    P(r,k)=2F_r(1-a^(-2r-2k-1))
           -k a^(2r-1)-k a^(-2r-2k-1)+2 sum_(i=1)^k a^(-2i).  (5)

At a=4, write P(r,k)=-16^r(2/5+k/4)+R(r,k). For r,k>=0,

    0 <= R(r,k) <= 19/30.                                    (6)

The upper bound drops the negative k term and bounds both geometric tails.
For the lower bound, the only negative remainder is k*4^(-2r-2k-1), at most
1/64, while the first constant is2/5 and the other remainder terms are
nonnegative. This includes k=0 separately with that negative term absent.

For fixed positive EVEN s, the clean target B_s has checker sum4^s P(r,k+s).
Its clock difference from B_0 at the prescribed pose(0,s,E) is therefore

    (2/5)(4^s-1)+4^s P(r,k+s)-P(r,k),                         (7)

which tends to negative infinity like-16^r, uniformly for k>=0. Allowing
arbitrary initial/final changes in one FIXED finite set of central cells changes
(7) by only a bounded amount. Hence no such bounded-support central controller
can implement these even clean layer jumps for unbounded straight-side length r.
The missing repair must reach remote growing regions, not merely reset a local
head or constant near-cap field. No restriction on cap duration is used.

In particular the four-cell modular control F above is physically impossible
as a complete two-layer target for every r,k>=3. For s=2, the clean checker
change is at most-14*16^r+152/15. The head contributes6, and F contributes
189/16. Their sum is negative already for r>=1. Thus all row/column charges
and pose parity pass, but this exact strict clock rejects the proposed path.

This is still not a theorem against new remote wake-emitting corners, changing
bulk profiles, or a genuinely different multipass frame mechanism. Those are
precisely the architectural freedoms not silently erased by the calculation.
