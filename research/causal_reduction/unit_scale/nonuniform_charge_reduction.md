# Exact charge preservation for growing unit-scale two-turn morphisms

23 October 2026, 02:27 UTC. Analytic result independently reviewed and signed.
No general unit-scale exclusion or finite-support construction follows.

## Scope

Let phi(R)=u and phi(L)=v be nonempty finite turn words, not necessarily of
equal length. From incoming north require u to finish heading east at a*E,
and v to finish heading west at a*W, for the same Gaussian unit a. Refinement
therefore preserves the coarse final heading and rotates every coarse net
position by a. Consider a growing rooted power-limit: a letter d and m>=1
such that phi^m(d) begins d, its iterates have lengths tending to infinity,
and the resulting infinite turn word is a legal ant trajectory on SOME
initial coloring. No finite-support hypothesis is needed in this note.

Then both images have exact signed charges

    #R(u)-#L(u)=1,       #R(v)-#L(v)=-1,

provided both letters are in the growing rooted component. In a reducible
case the unused fixed letter is its own length-one image, so the same
conclusion still holds. A component consisting only of a fixed letter is
not a growing rooted limit and cannot itself give an infinite legal
monochromatic ant word.

## Polynomial geometric ceiling

Every prefix position in an r-fold refined letter is a sum of r bounded
local image offsets, rotated by powers of a. The image lengths may differ:
only the maximum finite local footprint is used. Since |a|=1, the radius
is O(r), hence at most O(r^2) lattice cells are read. At each cell legal
successive turns alternate, so its total R-minus-L contribution has
absolute value at most1. Therefore the signed charge of every legal
refined prefix or factor is O(r^2). For a rooted power-limit this applies
along the corresponding residue class of refinement depths.

## Irreducible incidence matrix

Use row convention

    M = [[#R(u), #L(u)], [#R(v), #L(v)]],   z=(1,-1)^T.

The charge vector of the r-fold images is M^r z. If M is primitive, its
positive Perron root rho is strictly dominant. If rho>1, the polynomial
ceiling on the rooted coordinate forces the Perron coefficient to vanish.
For a positive left Perron vector w, this says w*z=0, so w_R=w_L. Thus the
two column sums of M agree, equivalently the two image charges sum to0.
Writing e=#R(u)-#L(u), we get M*z=e*z. Polynomial growth then gives |e|<=1.
The endpoint heading condition gives e=1 mod4, so e=1.

An irreducible integer two-by-two matrix with rho=1 is the two-letter
permutation matrix, hence not growing. The only irreducible imprimitive
case has zero diagonal: both images are monochromatic opposite letters.
If growing, their iterates are arbitrarily long monochromatic blocks,
which are illegal because reads0 and4 coincide and demand the same turn.
Thus cancellation on a first-letter two-cycle cannot bypass the argument.

## Reducible cases

A monochromatic image of its OWN letter is necessarily its length-one
identity. Indeed heading preservation requires its length1 mod4, while
any monochromatic block of length at least5 is internally inconsistent.
If the incidence matrix omits one letter entirely, every growing rooted
limit is monochromatic and impossible. The remaining genuinely growing
case, after possibly exchanging R and L, is

    phi(L)=L,       #R(u)=p, #L(u)=q>0.

Here a=1. If p>1, direct triangular-matrix iteration gives

    charge(phi^r(R)) = p^r - q*(p^r-1)/(p-1).

The polynomial ceiling forces q=p-1, giving charge(u)=1. The fixed left
image already has charge-1. If p=1, a growing rooted limit must be rooted
at R, and prolongability forces u=R L^q. Its limit is R L L L ..., which
is not ant-legal. If u starts L, R is not on a first-letter cycle and
there is no growing rooted power-limit from R. The exchanged case is
identical, with the sign of the charge reversed.

This covers all growing rooted power-limits under the stated two-image,
common-unit and heading-preserving assumptions. It does not classify
arbitrary shifted factors, infinitely varying directives, or decorated
state/context-dependent refinements.

## Consequence for finite fuel

For a finite initial black set B, the black mass after each refined copy
of a fixed coarse prefix equals |B| plus that prefix's original charge.
It is therefore bounded independently of refinement depth. If F_r is
the Laurent polynomial of signed cell occupancy of that refined prefix,
then every coefficient is in{-1,0,1}, its negative support is contained
in the fixed initial B, and its l1 coefficient norm is uniformly bounded.
The exact Laurent/Fourier transfer developed separately can exploit this.
Neither bounded total charge nor bounded tested Fourier characters is an
all-time positive certificate.
