# Arbitrary literal affine-count laps reduce to the signed decision class

23 October 2026, 20:35 UTC. Author preprocessing addendum, separate from frozen
main note SHA0aca7916e6bc3fc9c4fb2c9e1f8469d650653e848315749018481f6532ec7524
and unchanged core validator SHAaacac03e02ecf0d332ed1bfe1f46ee9e813901194b9a71e217c8e31768e7a337.
No nonstandard finite-seed model is asserted. Independent audit requested.

The core accepts variable-count words which restore heading, and whole laps
which restore heading. Those restrictions can be eliminated by an explicit
finite preprocessing, without assigning a fictitious pose.

## 1. An unbounded nonrestoring word is impossible

Let w be any nonempty literal word with nonzero net quarter rotation theta.
Its four successive copies have displacements d,Rot(theta)d,Rot(2theta)d,
Rot(3theta)d. Their sum is zero, including theta=2. Thus w^4 returns to the
same complete physical pose.

If w^8 were legal, each cell would see the same finite local read string in
each w^4 copy. For their concatenation to alternate, every such string would
have even length. Hence w^4 has zero complete board XOR. The full board and
pose repeat, giving an impossible bounded periodic physical orbit. Equivalently
this contradicts the independently signed closed-pose hull theorem, which
requires a nonempty XOR for every nonempty closed-pose interval. The argument
works on arbitrary, even infinite, backgrounds.

Therefore a variable-count stage w^(alpha*n+beta), alpha>0, with nonzero net
rotation can be rejected for EVERY initial coloring: its affine count eventually
reaches eight. No increasing search bound is used. Similarly a heading-restored
but zero-displacement w cannot occur twice, so a positive-slope count of such
words is rejected at count two. These are necessary rejections, not new physical
components.

## 2. A whole lap's fixed nonzero rotation reduces to affine geometry

After those immediate rejection cases, every variable-count word restores its
heading. Consequently the total heading rotation theta of a whole lap is a
CONSTANT, independent of n; only the fixed-count stages contribute. Its relative
lap displacement is d_1*n+d_0 in the frame at that lap's actual incoming heading.

If theta=0, use the existing quadratic-lap compiler directly. If theta!=0,
concatenate the FOUR original laps 4n,4n+1,4n+2,4n+3. For every stage and phase
s in {0,1,2,3}, its literal count is now

    4*alpha*n + alpha*s + beta.

All actual intermediate headings remain in place. The four-lap block restores
heading, and its coefficient of n in the displacement is

    4*sum_(s=0)^3 Rot(s*theta)d_1 = 0.

The grouped displacement is therefore CONSTANT. Its start pose is affine in
n, and the retained affine ordered-event certificate already decides it. There
is no quadratic branch left for nonrestoring whole laps. This is grouping of
real consecutive updates, not replacement of the head or field.

If the first entire lap is empty because every beta is zero, omit that empty
index and replace beta by alpha+beta. If every alpha and beta is zero, the
expression contains no infinite physical event path and is rejected. No other
initialization is hidden.

Together with the signed main note, this proves exact finite-seed realizability
and standard104 capture are decidable for EVERY supplied fixed finite expression

    W(n)=w_0^(alpha_0*n+beta_0)...w_t^(alpha_t*n+beta_t),

with nonempty literal words and nonnegative integer affine counts. The class
allows arbitrary initial heading and actual intermediate head rotations. All
old XOR fields and retired garbage remain as in the signed inverse theorem.
Existence of one successful nonstandard member has NOT been established.

## 3. Executed normalization controls

The separate `normalize_affine_laps.py/json` leaves the frozen core untouched.
It performs the two impossible-power rejections and the four-lap normalization,
then delegates actual geometric compilation to the signed Program constructor.
Five fixed controls, not a cap or parameter search:

- R^(n+1) is rejected at the inevitable R^8 occurrence.
- (RRRR)^(n+1) is rejected at two same-pose copies.
- (LRRL)^(n+1) R has whole-lap quarter rotation. Its actual four-lap grouping
  has A=(0,0), B=(-4,4) from incoming E. All1224 individual reads over six
  grouped laps agree with direct ungrouped literal integration.
- Restored (LRRL)^(n+1) keeps A=B=(1,0), with84 direct read comparisons.
- The empty first lap of (LRRL)^n is skipped exactly, also84 direct comparisons.

The controls establish only normalization conventions. They do not turn any
of those infinite-supply or internally conflicting words into a finite-seed
trajectory. The general proof is the exact rotation and grouping argument above.
