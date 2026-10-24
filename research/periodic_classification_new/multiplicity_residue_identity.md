# An all-multiplicity residue identity for white-input periodic fronts

22 October 2026. Independently analytically reviewed on 22 October 2026.
This extends the cap-three growth congruence, not its nonexistence scope.

## Theorem

Let a finite-seed translating periodic front have full drift d=(a,b),
period P, class multiplicities m_v, and growth g equal to the number of
odd m_v. There is no bound on m_v or P. Then

    #{v: m_v=2 (mod 4)} = 0 (mod 2),                    (1)

and

    g/4 - a = g/4 - b = sum_v floor(m_v/4) (mod 2).     (2)

Equivalently, the parity discrepancy between g/4 and either drift coordinate
is exactly the parity of the number of classes whose multiplicity is
4,5,6, or7 modulo8. In particular, growth12 and even-even drift force an
odd number of such classes. All multiplicities at most3 make the right side
zero, recovering the preceding cap-three exclusion.

## 1. Odd-edge degree from multiplicity modulo four

Every stable physical history begins white and alternates R,L. Let
r=ceil(m/2), l=floor(m/2). At a vertex whose incoming axis is vertical, let
alpha_j and beta_j be the bits for positive incoming and outgoing headings.
Then beta_j=alpha_j for R and beta_j=1-alpha_j for L, so the positive-port
counts satisfy B=A+l modulo2. At a horizontal-incoming vertex, the formula
is B=A+r modulo2.

For odd m, each incident axis has exactly one odd-used edge, so odd-edge
degree is two. For even m, r=l=m/2. Each axis contributes either zero or two
odd edges. The two axis parities differ exactly when m/2 is odd. Therefore

    m odd:             degree2 (a corner),
    m=2 (mod4):        degree2 (straight source or sink),
    m=0 (mod4):        degree0 or degree4.

This also shows that an odd-m corner is directed R for m=1 modulo4 and
L for m=3 modulo4, though the latter fact is not needed below.

The finite odd-edge graph on the full-drift cylinder is bipartite and all
its degrees are even. Its edge count is even, by summing even degrees over
one bipartition class. Writing V2,V4 for the numbers of degree2 and degree4 vertices gives
E=V2+2V4. Thus V2 is even. No evenness of the total vertex count is
asserted when degree-four vertices occur. The odd-m degree2 vertices number g,
which is a multiple of four. The remaining degree2 vertices are exactly
the m=2 modulo4 classes. This proves (1). Unread degree0 vertices are irrelevant;
read degree0 classes with m>=4 are allowed and have not been discarded.

## 2. Chronological crossing parity

The independently reviewed integer Whitney identity gives g/4=K. Modulo2
the heading-dependent signs in K disappear. At a white-input class,

    K_v = r(r-1)/2 (mod2),  if m=2r,
    K_v = r(r+1)/2 (mod2),  if m=2r+1.

Indeed the successive R visits have respectively 0,1,... earlier L visits.
The pattern of K_v modulo2 for m modulo8 is

    m mod8:       0 1 2 3 4 5 6 7
    K_v mod2:     0 0 0 1 1 1 1 0.

Also P/2 = a = b modulo2, and

    P/2 = g/2 + sum_v floor(m_v/2).

Since g/2 is even, subtracting the latter sum from K gives the residue table

    m mod8:                     0 1 2 3 4 5 6 7
    K_v-floor(m/2) mod2:         0 0 1 0 1 1 0 1
    floor(m/4) mod2:             0 0 0 0 1 1 1 1.

The tables differ precisely for m=2 modulo4. Their total difference is zero
by (1), proving (2).

## Scope and exact standard control

For standard104 the previously independently checked multiplicity histogram
is {1:4,3:4,4:2,5:2,6:5,7:2,8:2,10:1}. Its sum floor(m/4) is17, odd, in agreement
with g/4=3 and even drift coordinates. This control is not the proof.

Initial white input is essential: an LR class contributes a chronological
L-before-R pair although its multiplicity is only2. The pre-existing A8
front on an alternating nonwhite rail has g/4=1, even drift and no class of
multiplicity4 or more, so (2) cannot simply be extended to arbitrary periodic
input without a color correction.
