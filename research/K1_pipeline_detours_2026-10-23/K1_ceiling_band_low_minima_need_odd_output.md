# Low minima inside one K1 ceiling band cannot use root-free counterflow

24 October 2026, 01:53 UTC. Complete WHITE cap-four K1 translating
front, actual full P,d. Positive required odd output is retained.
Pending independent review, including the exact essential-band walk
fd44da68. This is NOT a per-branch or per-renewal charge.

Use a ceiling band B from fd44da68: either an annulus between consecutive
canonical essential circles with signs +,- at sheet c_right, or the
final RIGHT outer region. Its base is c_right=M-1. Its boundary collars
have F>c_right-1/2; in the outer case the eventual exterior value is
c_right. No canonical essential circle of ANY sheet lies inside B.

THEOREM, pending review: every locally minimal L plateau Q contained in
B at height

    m<=M-3=c_right-2

must touch an actual odd-output cell. This holds even if Q is itself
essential in the cylinder. Its previously allowed root-free essential
reverse-birth alternative is incompatible with the canonical band.

If q counts DISTINCT such minimum components over any selected family
of ceiling bands, then

    q<=Nodd-Ntop+J,

where J is the number of G3(M) source-sink path components. Different
heights and actual quotient translates are retained. No minimum is
charged again each time a supplier visits it.

## 1. A root-free reverse plateau embeds below sheet m+2

Suppose Q has no odd-output incident corner. Under exact time reversal
its incident cells start WHITE, although cells elsewhere may start
BLACK. The signed prepared plateau theorem ab9fad0a gives positivity:
all original C faces neighboring Q have height>=m+1. It also gives an
essential reverse first-L parent curve inside the diagonal L-contact
component Q. The alternative m<c_left is not being discarded; this
argument explicitly handles the essential curve it supplies.

At any corner joining TWO L faces of Q, both have height m. Write the
scalar local formula as L1=a-l_1,L2=a-l_2. Equality gives l_1=l_2.
No odd output means the complete original history is even, with zero,
one or two L reads. Zero L reads would make both l counts zero and
all ports at an inactive WHITE corner zero; this contradicts the C
neighbor positivity >=m+1. One total L read cannot split equally.
Therefore the corner has FOUR reads, l_1=l_2=1 and

    a=m+1.

Its central scalar value is m+1, while both L-face centers have value m.
Thus each diagonal Q contact can be drawn entirely in

    F<m+3/2,

connecting through this central vertex. The reverse parent curve in Q
is consequently an essential curve inside the LOW scalar component
at half-level m+3/2, which is canonical sheet j=m+2.

This is an actual exact local embedding, not identification of the
reverse cursor with a forward canonical contour. The reverse curve
only witnesses essential topology of the low component.

## 2. The low component forces an internal canonical essential circle

Because m<=c_right-2,

    m+3/2<=c_right-1/2.

Every ceiling-band boundary collar is strictly HIGHER than this level.
In the right outer region the eventual constant is higher too. Hence
the low component containing Q is confined away from all ends of B.
It contains the essential reverse curve from section1. Such a low
component inside an annulus, bounded away from both ends, must have
an essential level-circle boundary: a finite union of contractible
circles cannot separate an essential low core from both high collars.
The same holds in the outer region using its high eventual exterior.

That boundary would be a canonical essential circle at sheet m+2
INSIDE B, forbidden by the definition of consecutive essential bands.
This contradiction proves that Q has an odd-output incident corner.
No assumption that Q is physically finite has been made.

## 3. Distinct minimum components cannot reuse one odd class

A physical odd cell has only two incident L faces. If they are at the
same minimum height, they are corner-connected and in the SAME plateau.
If their heights differ, the higher one has a strictly lower neighboring
L face and therefore cannot belong to a locally MINIMAL plateau. Thus
one odd cell can touch at most one locally minimal L component, even
when different candidate components have DIFFERENT heights.

The component and scalar band constructions are equivariant under the
actual full drift. Translating a proposed class alias reduces it to
the physical statement, so short quotients cannot increase capacity.
The L<=M-3 barrier at ceiling boundaries confines these components to
their respective bands, so different bands cannot share a component.

A TOP odd root at m<=M-3 must be same-R three-read at m=M-3; the other
top odd types have higher L levels. Its signed G3(M) pairing stays on
the SAME Q. Different components assigned top roots therefore use
different complete G3 paths among J. Other components use distinct
non-top roots among Nodd-Ntop. Choosing non-top roots when available
proves q<=Nodd-Ntop+J.

## 4. Consequence for same-band max-face birth curves

Choose r_B ordered disjoint selected maximum-face parent cycles in a
ceiling band B. Their K1 crossing theorem supplies an L face<=M-3 in
each of their r_B-1 intervening strips. The signed selected-contact
barrier confines the L sublevel there. Taking an actual minimum gives
a locally minimal Q within that strip. Different intervening strips,
and different ceiling bands, give different Q.

Consequently, for any such chosen family,

    sum_B max(0,r_B-1)<=Nodd-Ntop+J.

The old root-free lower-counterflow escape cannot occur INSIDE one
canonical ceiling band: it would create a missing internal essential
canonical contour. Cross-Gamma transfer still may occur between the
remaining finitely many curves, and many source sites may reuse one
strip minimum. No injection of branch sites, no temporal nonreuse,
no initial-fuel upper bound and no global front exclusion follows.

## 5. Strict supplier pits

If an actual strict supplier route places a low L face<=M-3 in the same
ceiling band as its maximum-face suppliers, its sublevel cannot leave
that band. A minimum reached from it is odd-rooted by sections1-2,
rather than using an independent essential reverse-counterflow option.
This is a necessary root per DISTINCT minimum component only. It does
not make earlier supplier packages recursive or assign every route a
new output class. The actual local route and its band membership must
still be proved separately.
