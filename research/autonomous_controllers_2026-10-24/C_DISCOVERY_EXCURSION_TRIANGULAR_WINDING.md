# One-sided winding of actual C-discovery excursions

24 October 2026. Author proof and literal controls; independent audit pending.
This is an all-cap chronological constraint on an existing translating history,
not a controller construction, finite macro alphabet, or WHITE winding theorem.

## Exact setting and notation

Use the signed active-C entry scaffold (1ae8a8e5, audit317e4dce) and actual
excursion normal form (a74e13f8, audit99d6b773). Choose a WHITE-owned first-entry
cycle and lift it in the direction of discoveries to an indexed spine of
physical C faces u_i, i in Z. If the cycle has m full-drift classes, then
u_(i+m)=u_i+d and A(u_(i+m))=A(u_i)+P. Its first activation times A(u_i)
strictly increase. The lifted spine is a proper embedded path of diagonal
C-face-center edges. These facts use the FULL supplied drift d, not its
primitive direction, and do not assume a bound on period or visits.

For the selected physical read cell between u_i and u_(i+1), let r_i be its
first R and l_i its first L. The incoming headings agree. The literal interval
E_i=[r_i,l_i) is closed in head pose, contains its root read exactly once, and
lies in [A(u_i),A(u_(i+1))). It may consume stock whose actual R owners occur
in other excursions or earlier full periods. Nothing below deletes that stock.

Let f_i(v) be the clockwise winding number of this CLOSED unit-step polygon
about the center of face v. This is the finite closed-walk stream, normalized
to zero in the unbounded component, not the stream of the whole translator.
Its value is an integer and has finite spatial support, even when the polygon
self-intersects or repeats edges. Face centers are never on a grid-step path.

## The triangular constraint

For every integer i,

    f_i(u_i)=1,
    f_i(u_j)=0 for every j>i.

Proof of the second assertion: throughout E_i, every face u_j with j>i is
still genuinely never active, since its first activation is at or after
A(u_(i+1))=l_i+1. All the selected C edges between these future faces are also
unread during E_i. Indeed, the two C faces at such a physical read cell are
exactly its endpoints. The fixed arrival-axis/checker sector implies that ANY
actual read at that cell activates one of them. Thus there was no such read.

Join the centers u_(i+1),u_(i+2),... by their actual diagonal C edges. Their
interiors lie inside square faces, and their only intersections with the
ordinary unit grid are their shared read-cell vertices. Since those vertices
are unread, this whole future half-ray is disjoint from the closed ant trace
E_i. It is proper and unbounded because it is a finite embedded pattern
translated by nonzero d. Therefore each future center connects to infinity in
the complement of E_i. Its winding number is zero. This is an actual
chronological escape path in the plane, not a prelaid BLACK rail.

For the first assertion, the diagonal segment from u_i to u_(i+1) meets E_i
only at its root. That cell has the sole R at r_i, then no further read before
the endpoint return at l_i. The closed polygon has the same incoming heading
on return, so its local root corner is precisely this clockwise right turn.
The clockwise stream is one larger on the active-C side u_i than on the other
C side u_(i+1). Equivalently, the finite closed-walk port identity at this
once-read root gives f_i(u_i)-f_i(u_(i+1))=1. The second assertion makes the
latter value zero, proving f_i(u_i)=1.

Neither part requires the immediate exterior C row to remain unread forever.
The future ray is unread only up to the selected discovery, exactly as needed.
In particular the theorem applies to the standard inner cycle with its actual
7/8-read selected cells, which fails the separate permanent-unread-row premise.

## Exact transfer semantics and a limited noncancellation corollary

Set a_(i,j)=f_i(u_j). For each fixed i, only finitely many entries are nonzero;
a_(i,i)=1, a_(i,j)=0 for j>i, and a_(i+m,j+m)=a_(i,j). The finitely many
backward coefficients per primitive cycle representation are arbitrary signed
integers at this stage. Their range and magnitude are NOT bounded uniformly
across controllers. This is an exact periodic triangular integer transfer,
not a finite-state abstraction.

Every finite square interval restriction has determinant1. More concretely,
the lifted closed-excursion winding fields are linearly independent under
FINITE integer combinations: in a putative nontrivial zero combination,
evaluate at u_b for the greatest index b with a nonzero coefficient. All
earlier excursions vanish there, while E_b has value1, a contradiction.
Thus the corresponding finite closed edge currents cannot cancel either.
This does not prohibit infinite periodic sums or cancellation after quotienting
by d. It does not certify legal deletion or a positive fuel charge.

## Literal standard countercheck to stronger signs and period-quotient claims

In the standard104 normalization, d=(-2,2), the inner cycle has the actual
excursions E8 at r=46 and E92 at r=56. The E92 parent is u_0=(-6,3), with
spine u_j=(-6-j,3+j). Complete geometric support enumeration, with no arbitrary
window, gives

    f_E92(u_0)=1,
    f_E92(u_(-2))=-1 at (-4,1),
    f_E92(u_(-3))=-1 at (-3,0),
    all other spine values zero.

E8 has only its parent coefficient +1. The outer cycle's E12 and E88 likewise
have only their respective parent coefficients +1. These are literal factors
of the same exact WHITE standard front, with full fields and cross-period R
owners already retained in the signed normal-form control.

Consequently older coefficients cannot be assumed nonnegative. Also, after
summing translates by the FULL d and using columns (E92,E8), the inner cycle's
face-type matrix is, in the checker's canonical order,

    [ 0   0 ]
    [-1   1 ].

It is singular, and the sum of its columns is zero at BOTH spine face types.
The outer cycle instead gives the identity matrix. Thus a unit diagonal on the
LIFTED causal spine does not give a unit determinant, positive cost, or even a
nonzero summed spine stream in the finite period quotient. The negative older
entries account exactly for this representation-sensitive cancellation; they
must not be discarded as obsolete history.

## Prepared controls and full scope

Prepared10 has a WHITE-owned C-entry cycle and its E8 has only the parent +1
coefficient. Its genuine BLACK fuel input remains and is not a discovery root.
So even this complete triangular property does not distinguish no input from
hidden prepared input. Supplied1564,4352 and prepared80 have no WHITE-owned
C-entry cycle; the theorem has no such selected cycle to apply to in them.
Their full first-entry graphs and explicit BLACK roots are retained, rather
than declared excluded by the new condition.

The checker reconstructs all selected physical lifts and first-activation
clocks in the five supplied controls. It finds every spine-face center in each
polygon's finite bounding rectangle by exact integer/Fraction bounds, records
all winding values, and checks forty rotation/power/phase controls for standard
and prepared10. This finite bounding rectangle belongs to the GIVEN excursion,
not to a proposed class of all controllers. The analytic future-ray proof
covers all lengths, turns, periods and higher multiplicities.

No sign for older coefficients, fixed backward radius, finite alphabet,
no-input detector, WHITE lifetime S1, autonomous nonstandard controller, or
finite-seed entry theorem follows. The useful new obligation is to combine this
one-sided geometric information with actual source ownership, without losing
the genuine negative backflow already required by standard104.

## Frozen artifacts

certify_C_excursion_triangular_winding.py
C_excursion_triangular_winding_certificate.json

Dependency hashes are embedded in the certificate. The exact full-field
standard realization and all prepared backgrounds remain the dependencies of
the signed supplied controls; no read footprint is substituted for a board.
