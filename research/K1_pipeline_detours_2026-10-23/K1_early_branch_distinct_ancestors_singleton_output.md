# Early branches have distinct older ancestors; S ancestors reserve singleton output

23 October 2026. Submitted for independent review. Complete WHITE cap-four
K1, actual full P,d. Count only the surviving EARLY-S bit11 maximum-
branched RIGHT main faces. Their complete source-L3 cleanup and two
actual ancestor profiles are retained. No initial-fuel, original-root,
new component or repeated-pattern claim is made.

## 1. The equivariant actual ancestor assignment

For each counted main branch F, use the already proved canonical chain

    I(F) <- P0(F) <- Q1(F),
    p(I)=P0, p(P0)=Q1.

In the fixed branch pose, F=(0,0), I=(-1,1), P0=(-2,0), Q1=(-3,1).
Their canonical contacts are u=(-1,1):EEWE and g=(-2,1):SSNS. The
complete Q1 profiles from the actual left-square closure are

    R ancestor: entry j=EEWE, helper k=NNNS, f=EEEW, exit g=SSNS;
    S ancestor: entry k=SSNS, helper f=EEEW, exit g=SSNS,
                unused other corner j=W (a singleton R).

Everything is full-drift equivariant. These are real canonical faces
and actual complete cell histories, not paths repaired from flows.
We prove that F->Q1(F) is INJECTIVE on physical faces and therefore
on the actual full quotient. The older ancestor is not paid as a new
root merely because it is distinct.

## 2. The first two links lose no identity

A physical I has a unique canonical parent contact u. For a surviving
early branch, this is exactly the LOWER-I-birth geometry: the main F
is the clockwise90-degree diagonal neighbor of I relative to the
incoming P0->I direction. Thus the actual parent edge and its fixed
heading determine F uniquely. Two packages cannot share I with
alternative main F poses.

A physical P0 likewise has its unique canonical incoming Q1->P0 edge.
It is LEFT on the actual parent/child chain Q1->P0->I. The outgoing
P0->I direction is its incoming direction turned LEFT90degrees, hence
I is unique once P0's canonical birth edge is fixed. Consequently two
packages cannot share P0 while having distinct I/F.

These are local geometric uniqueness statements. They do not assume
that arbitrary maximum faces have at most one child in the parent forest.

## 3. A fixed Q1 cannot supply both allowed child geometries

For a fixed physical Q1, its canonical birth edge and incoming heading
are fixed. Relative to that frame, the complete ancestor theorem leaves
only one STRAIGHT child position and one RIGHT child position for P0.
There is at most one physical child face at each of these positions.
The two alternatives cannot BOTH be present.

To see the exact conflict, rotate/translate Q1 to the unit face with
canonical entry at its NW corner (0,1), incoming S and complete SSNS.
In the S package, the SW corner (0,0) is the singleton history W.
In the R package with the SAME canonical entry, rotate the displayed
R profile by90degrees: its selected EXIT is that same SW corner with
complete history WWEW. One physical cell cannot simultaneously have
one read and four reads. Optional L3 and all earlier suppliers were
already included in these complete profiles.

Thus fixed Q1 permits at most ONE of the two package child positions.
Two early branches sharing Q1 would have the same P0, then the same I,
then the same F by section2. The assignment is injective.

For full-quotient injectivity, if two Q1 classes agree, translate one
whole physical package by an integer multiple of actual d to align
the Q1 faces. Canonical p and all complete histories translate with it.
The physical proof then makes the F faces agree as well. No primitive
period, distinct-component or unproved lift-label assumption is used.

## 4. The S subset injects into distinct singleton-R final-black classes

Let n_Sanc count the early branches whose assigned ancestor is S.
Its j cell has complete WHITE history W: exactly one R, hence ends
black. That R selects the unique maximum C face Q1; its opposite C face
has height M-1. Therefore a physical singleton cell j cannot serve as
the reserved j of two DIFFERENT maximum ancestors, in any rotated
pose. Full-quotient alignment is the same as section3.

The previous injectivity hence yields a genuine reservation

    n_Sanc <= N1 <= N_odd=R-L,

where N1 counts full-quotient physical one-read classes and N_odd counts
all final-black odd-read classes. This is OUTPUT production, not finite
initial fuel. It does not say every early branch has an S ancestor:
the strict locked-R ancestor alternative has no such singleton and
remains explicit.

## 5. Safe combination with existing odd-output reservations

The signed selected0->1 rise reservation uses selected RLR (three-read)
classes. The signed strict-fall/straight-max-branch reservation also uses
three-read classes and was independently proved disjoint from those
rises. Our reserved singleton classes have ONE read, so they cannot
coincide with either existing three-read family, even after full-drift
translation. With their existing counts n_up and n_SB, the union gives

    N_odd >= n_up + n_SB + n_Sanc.

This does not add to an original-root budget or reserve distinct
clockwise cycles per branch. The signed canonical turn identity gives
clockwise-contractible minus counterclockwise-contractible cycle count
N_odd/4, so it equivalently requires clockwise excess at least
ceil((n_up+n_SB+n_Sanc)/4). That is the SAME output reservation, not a
second additive payment.

No injection of the locked-R ancestor subset into singleton output,
fresh maximum components or original fuel is claimed. Distinct actual
ancestors may lie on an older Gamma segment, share other cells, or be
attached to the same maximum component. No global K1 exclusion follows.

Dependencies: surviving Q1 two-profile closure a7f57d46 (submitted
separately), signed early-parent/source-L3 profiles 8592d1c4 and 48494491,
selected rise/RIGHT-L3 reservation 6c107bd7, signed strict-fall stock
730d9bb1 and straight-branch entrance exclusion c945fd54. No new period,
drift, radius or multiplicity computation is used.
