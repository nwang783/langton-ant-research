# Exact outward chamfered-frame regeneration, with a pose-sector obstruction

23 October 2026, 07:19 UTC. Independently signed coordinate and Presburger proof (audit KN). This is NOT a renewable ant orbit or counterexample.
It supplies an exact two-dimensional COMPLETE-field matching example whose
missing interface is impossible for a precise invariant reason.

## Two-parameter literal family

For integers r,k>=0 put

    W_(r,k) = ((LRRL)^r (RL)^k R)^4.

Start at(0,0,E). Each of the four identical side words turns the incoming head
clockwise by90 degrees. The complete word returns to(0,0,E), has length
16r+8k+4, and is SELF-AVOIDING: every read cell occurs exactly once.
Its minimum black input I_(r,k) has8r+4k cells, and its complete output
O_(r,k) has8r+4k+4 cells. Every other cell is white. The complete XOR has
16r+8k+4 cells, namely the entire read support, not merely four added cells.

Here is an exact coordinate definition, also proving all turns. Let
J(x,y)=(y,-x), v=(2r+k,-k-1), and c_j=sum_(i<j) J^i v for j=0,1,2,3.
The unrotated side has L-input and R-output sets

    L = {(x,0):0<=x<2r}
        union {(2r+s,-s-1):0<=s<k},
    R = {(x,1):0<=x<2r}
        union {(2r+s,-s):0<=s<=k}.

The entire input and output are respectively

    I_(r,k) = union_(j=0)^3 (c_j+J^j L),
    O_(r,k) = union_(j=0)^3 (c_j+J^j R).

The straight segments are the two colors of LRRL row transfer. Each RL adds
one southeast diagonal step without changing incoming E; the final R closes
the side with its clockwise turn. All sixteen indexed straight/diagonal
families are pairwise disjoint, including r=0 or k=0 with empty intervals.
Their exact pairwise intersections are empty over the entire parameter cone.
Thus the prescribed L cells are initially black and every R cell is white,
and there are no later read-color compatibility conditions to assume.

## Exact complete-field next-phase identity

The striking identity is

    O_(r,k) = I_(r,k+1) + (0,1).                 (1)

This is equality of COMPLETE finite black boards, with no omitted fringe,
controller bit, corner cell, or externally supplied rail. The shape is a
fourfold-symmetric chamfered square. Its center is

    c=(r-1/2,-r-k-1/2).

The north translation in(1) keeps the next shape's center equal to c.
Input/output masses differ by4, consistent with the four extra R turns.

Equation(1) has been verified as an exact Presburger-set equality in both
parameters, not extrapolated from finite samples. It can also be checked by
matching the straight sides and successive diagonal end cells in the displayed
coordinate formula. The case r=k=0 is the ordinary four-R square on blank input.

## Why this nevertheless cannot be renewed by any cap

The next literal W_(r,k+1) on the matching board would need pose(0,1,E).
The actual current pose is(0,0,E). Their invariant

    sigma=x+y+h (mod2), with N,E,S,W=0,1,2,3,

differs by1. Therefore NO legal ant path of any length connects those poses,
even if arbitrary extra board changes were allowed. This is the signed pose
sector obstruction, not failure of a finite cap search.

Nor does rotating the next phase about its fourfold symmetry center help.
A90-degree counterclockwise rotation about c has translation
(-k-1,-2r-k), whose coordinate sum is odd. The rotation also flips heading
parity. Their two contributions cancel, so every one of the four natural
rotated starts has the SAME opposite sector. Every cyclic cut of any one of
those actual side words preserves that sector too.

Thus this exact board matching is insufficient for physical renewal. It is a
sharp positive control against any abstraction retaining full fields but
silently resetting the head. It does not exclude a different two-phase
operator: a net north displacement2 is sector-compatible, but no legal path
implementing the required two-layer field update has been constructed.

## Verification and scope

`check_chamfered_frames.py` checks all120 pairwise family intersections, exact
next-phase field equality, and fourfold input symmetry using libisl exact
integer Presburger sets. `chamfered_frames_certificate.json` records the
hash, relations, counts and result. Resource failure is not accepted as a proof.
The geometry formulas separately give the actual word, headings and duration.

The five small fixed-corner exploratory templates in `probe_square_frames.py`
were only discovery. The theorem here has unbounded r AND k and does not
claim that those five templates exhaust possible corner mechanisms. The
older signed inward spiral is distinct: it consumes fresh corner fuel and
has its own complete eventual104 certificate. No conclusion about the
actual continuation of this chamfered-frame seed is asserted here.
