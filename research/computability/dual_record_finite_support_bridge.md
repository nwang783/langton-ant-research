# Dual-record half-planes for arbitrary expanding matrix inflation

2026-10-23 01:10 UTC. Independently analytically audited as GS at 01:14 UTC.
This formalizes the oblique-record mechanism behind the countermodel
analysis's matrix [[3,2],[2,5]],radix9 obstruction. It is a sufficient local
exclusion criterion, not a decision procedure for arbitrary finite seeds.

## 1. Coordinate records exist for every expansive affine identity

Let p be an actual ant trajectory with finite initial black support, and
suppose, for all sufficiently large integers n,

    p(kn+c)=A*p(n)+d,

where k>=2, c is integral, d is a lattice vector, and A is an expansive
integer2x2 matrix. No heading preservation, controller or fixed image words
are assumed. Expansive means both eigenvalues have modulus greater than1.

Each coordinate of p is unbounded in absolute value. Otherwise suppose its
j-th coordinate were bounded byC at all late times. Choose two consecutive
late unit steps, which are perpendicular and thus form a basis. Iterating
f(n)=kn+c at sufficiently large n keeps all indices in the identity domain.
The common affine spatial terms cancel in differences, giving

    p(f^r(n+1))-p(f^r(n))=A^r*(p(n+1)-p(n)).

The same holds for n+1,n+2. Bounded j-th coordinates therefore bound the row
e_j^T*A^r on a basis, hence bound that row uniformly. But
e_j^T=(e_j^T*A^r)*A^(-r) tends to0 because A^(-r) tends to0, contradiction.

At least one sign of the vertical coordinate has arbitrarily high first
records. A180-degree rotation makes that sign north without changing A.
All finite initial supports and finite exceptional early histories can be
put below a sufficiently high chosen record.

## 2. The integer dual normal

Write A=[[a,b],[c0,d0]], Delta=det(A), and g=gcd(|c0|,|a|). Define

    ell=sign(Delta)*(-c0,a)/g,          m=|Delta|/g.

Then ell is an integer covector, m is a positive integer, and

    ell*A=m*(0,1).

Translate the fine ant by -d, writing q(t)=p(t)-d. Its aligned positions
satisfy q(kn+c)=A*p(n), and therefore their ell-height is m times the coarse
vertical coordinate. This is a coordinate identity, not a physical reflection
of the ant: arbitrary determinant signs of A are allowed.

Let W_e be ALL geometrically possible length-k axis-alternating movement
words with endpoint A*e, for each compass direction e. Include both possible
initial movement axes whenever geometrically feasible. Discard no word on
the basis of an unknown color or heading context. If an entire W_e is empty,
the identity is already impossible, since every compass direction occurs
infinitely often in a finite-support ant. That latter fact also follows by
the usual eventual-fresh-row contradiction if one direction were omitted.

Define the exact geometric proper-prefix ceiling

    M=max ell(prefix_position(w,j)),  w in union_e W_e,  0<=j<k.

The dual-record condition is

    M<m.                                                     (D)

## 3. A high coarse record makes a pristine fine oblique half-plane

Take the first coarse arrival at a sufficiently high rowY, at positionz.
Every earlier coarse block starts at height at mostY-1. Every proper fine
prefix of such a block has ell-height at most

    m*(Y-1)+M < m*Y.

The aligned boundaries of earlier blocks are also below mY. ChooseY large
enough that the fine initial support and all exceptional early fine reads
are below mY as well. Thus, at q(kn+c)=A*z, every cell in the half-plane

    ell*(x-A*z)>=0

is untouched white. The fine aligned endpoint is itself a first visit.
This conclusion is valid for independently chosen image words at EVERY
occurrence and arbitrary final headings.

The coarse record is a fresh north-entered R, and its east neighbor on the
same row is also fresh, forcing a second R. Hence the next two coarse
movements are east and south. The incoming fine heading belongs to the
finite set of possible final directions of W_N.

Consequently a NECESSARY local condition for the affine identity is a
length-2k legal fine segment, starting at0 with one of those headings, with
positions A*E at timek and A*(E+S) at time2k, on a board initially white on
ell*x>=0 and arbitrary below it. Alternating reads and upper first-R reads
give an exact finite test. If the entire test is empty, the eventual affine
identity is excluded for ALL finite-support ants.

Passing the test asserts only local compatibility, not an actual model or
a finite-seed counterexample. If(D) fails, nothing is inferred.

## 4. Prefix ceilings need no exponential enumeration

For a fixed initial movement axis, let H,V be the total horizontal and
vertical slots and let the required endpoint be(x,y). The direction counts
are E=(H+x)/2,W=(H-x)/2,N=(V+y)/2,S=(V-y)/2; discard a phase if these are
negative or nonintegral. For a prefix of lengthj, let h_j,v_j be its two
axis-slot counts. Put ell=(alpha,beta), and let

    P_h=E if alpha>=0, otherwise W;
    P_v=N if beta>=0, otherwise S.

The EXACT maximum ell-height at that prefix length is

    |alpha|*(2*min(h_j,P_h)-h_j)
      + |beta|*(2*min(v_j,P_v)-v_j).

Choose all positive-weight moves first within each axis's slots; all remaining
moves still fit the remaining slots. The horizontal and vertical sign choices
are independent, so the bound is attained. Maximizing this formula over
four endpoints, feasible starting axes and j<k computesM in linear time
in k, using exact integers. The remaining2k local legality test is finite.

## 5. Current control and scope

For A=[[3,2],[2,5]],k9, the primitive normal is ell=(-2,3),m11. The raw
geometric image counts are4,20,4,20 for N,E,S,W. Both the formula and literal
enumeration giveM10. Every north image ends north because all five vertical
moves point north. The analysis's separate80-pair E/S certificate rejects the
necessary local test; see its dual-record note and exact artifact for that
concrete exclusion and its independent audit status.

This method uses an oblique physical white region even though the coarse
record is a coordinate record. It is not restricted to diagonal, Gaussian
scalar or monomial matrices. It does not manufacture a same-path identity
for arbitrary directive limits or state-dependent aligned endpoint offsets.
