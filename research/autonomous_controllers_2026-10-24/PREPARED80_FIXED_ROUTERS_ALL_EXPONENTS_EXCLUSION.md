# The prepared80 fixed routers cannot close their inputs at any run lengths

24 October 2026. Author proof and exact finite certificate; independent audit
pending. This is an all-parameter exclusion of one explicit constructive family,
not a controller classification or a WHITE unit-winding theorem.

## Family and conclusion

Let

    M = RRRRLLLLRL,
    A = RLRRRRL,
    B = RRRRL,
    C = RRRRLRLRLRRRRL,
    D = LRRL.

For independently arbitrary nonnegative integers a,b,c,e define

    W(a,b,c,e) = M^a A M^b B M^c C M^e D.

The supplied prepared80 wave is W(2,1,1,1). Its internal recycling of nominal
M-inputs motivated varying these four run lengths while retaining the actual
router words. The four M runs have incoming headings N,W,S,N; this is not a
same-axis/sector fixed-normal profile conversion loop.

**Claim.** No member W(a,b,c,e) is a complete WHITE translating front, and hence
no infinite repetition of one such member is realizable from a finite BLACK
seed. Arbitrary initial BLACK boards may realize prepared members. Changing a
router, intermixing different W members, adding new connectors, or permitting
additional macro runs is outside this theorem.

## Symbolic geometry and exact checker charge

A ten-step M restores its incoming heading. In the four run headings its
respective displacements are (1,1),(-1,1),(-1,-1),(1,1). The four fixed routers
have displacements (0,1),(0,-1),(3,-1),(0,2) in their actual incoming headings,
and together restore N. Consequently, with s=a+e,

    P = 30 + 10(a+b+c+e),
    X = 3+s-b-c,       Y = 1+s+b-c,
    #R-#L = 12.

Choose the initial read position as (0,0). Every update switches checker parity.
M has even/odd signed charges (1,-1) when begun at an even position, and
(-1,1) when begun at an odd position. The four runs start with checker parities
0,1,0,0 because router lengths are 7,5,14,4. The routers' combined signed
charges are (5,7). Thus the entire word has

    g_even = 5+a-b+c+e,
    g_odd  = 7-a+b-c-e.

The executable retains the literal router geometries and the local M charges.
These formulas follow by concatenation for every exponent, not extrapolation
from sampled run lengths.

## Derived finite reduction, without imposing any period or visit cap

Suppose the word were a complete WHITE translating front with full nonzero
drift (X,Y). Every complete physical history alternates from R, so its signed
R-minus-L count is 0 or 1. Since X+Y is even, every full-drift class has one
checker parity. Summing the classes on either parity gives g_even>=0 and
q:=g_odd>=0. No BLACK-first input class is silently discarded here: a prepared
front is allowed negative contributions and therefore cannot use this premise.

The retained full-drift signed-residue theorem gives

    12 = g >= 2 max(|X|,|Y|),

so -6<=X,Y<=6. Its precise dependency is section2.3 of
sources/kehao95-core/wake_synthesis/proof/periodic-growth-closure.md,
SHA256 bd3e74c5a2a87c4431fe4c777b9eeaa7010e42600ab9eb9bea6198e9ca249db7.
This uses the recovered general residue proof, not missing width-ten metadata.

Now exact algebra, without division by any unknown parameter, gives

    2(a+e) = Y-q+6 <= 12,
    2b     = Y-X+2 <= 14,
    2c     = 10-X-q <= 16.

Therefore every potential WHITE member belongs to the DERIVED finite box

    a,e>=0, a+e<=6,       0<=b<=7,       0<=c<=8.

It contains 28*8*9=2016 parameter tuples. This is a necessary superset; we do
not assert that all of it satisfies the simultaneous drift and parity premises.
In particular a prepared member in this box can have |X|>6.

## Exact complete-chronology cover

For every tuple in that box the checker reconstructs the full literal word and
all read positions. For nonzero drift it groups phases by the FULL vector
(X,Y), writes each read position as representative+k*(X,Y), and orders each
complete class by phase-P*k. This is the actual stable physical-cell order,
not cropped within-period order or the primitive-direction quotient.

The 2016 cases are partitioned as follows:

- 28 have zero full drift and are not translating words.
- 1984 have a complete class with two consecutive identical turns. The
  certificate supplies that full class, both actual phases and lifts. Repetition
  is impossible on ANY initial color assignment.
- Four have alternating stable classes but an explicit BLACK-first class.
  They are (a,b,c,e)=(2,1,1,1),(3,1,1,1),(4,1,1,1),(5,1,1,1), respectively
  P=80,90,100,110, drift=(4,4),(5,5),(6,6),(7,7), and input counts2,3,4,5.
  Their exact BLACK-first histories are retained. The P110 case already violates
  the WHITE drift bound, but is harmlessly included in the larger box cover.

Thus no tuple in the necessary box is complete WHITE. Together with the
analytic reduction, this excludes every nonnegative exponent tuple, including
arbitrarily long M runs. It does not exclude the prepared wave or turn its two
input rays into finite support. No solver status or timeout is used.

The finite-seed consequence is the retained stable-class necessity: in a
nonzero-drift repeated word, sufficiently far copies of every physical read
class initially lie outside any finite BLACK seed, hence must start R.

## Frozen certificate

certify_prepared80_router_family_exclusion.py
SHA256 7ed476d26bc7279da767b1d4fde9bb1d36cc1439e78d098d5c103020149b7cf5
prepared80_router_family_exclusion_certificate.json
SHA256 ccef3e0da42260660a71b745edd23aa2ac8393dd2270c880f1704ab4b240576b

All 2016 tuples have a checkable witness. This is a completed author argument;
independent review, if obtained, must be bound separately.
