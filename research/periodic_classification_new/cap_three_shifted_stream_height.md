# Shifted stream height excludes complete white cap-three fronts

23 October 2026. Independently analytically reviewed, all sections.
Literal independent controls: `../audits/check_cap_three_stream_height_independent.py/json`.
No claim about the unrestricted finite-seed conjecture or novelty is made.

## Statement and inherited premise

A nonzero translating Langton-ant front with complete initially white
histories of at most three visits per physical cell cannot exist.
The period, drift and support width are unrestricted. The translation used
is the full displacement d of one whole event period, not its primitive
lattice divisor. We use the signed all-period same-type exclusion in
`cap_three_same_type_exclusion.md`: every triple has opposite first and
third incoming headings. Apart from this premise, no chronological
Whitney count or A/B balance is needed.

Lift the event cycle to a path indexed by every integer time. Its local
histories are R, RL, or RLR, and all are complete. The event successor on
the full-drift quotient is one cyclic permutation. The path changes axis
at every step. After choosing a checkerboard sector, vertical edges point
out of even vertices and horizontal edges out of odd vertices. Every
traversal of a physical edge has this same direction. The alternative
sector is handled by a translation of the coordinate origin.

## 1. The stream function and its exterior values

Let f(e) be the total number of traversals of a directed physical edge by
the bi-infinite path. These numbers are finite, d-periodic and supported
in a finite-width strip parallel to d. They are divergence-free, because
each complete physical-cell history has equally many arrivals and exits.
After the same-type exclusion, f(e) belongs to {0,1,2}.

The directed checkerboard edges orient each unit face either clockwise
(C) or counterclockwise (L). Every directed edge has its C face on its
right and its L face on its left. On the simply connected plane,
divergence-freeness gives an integer face stream function h, unique up to
an additive constant, satisfying

    f(e) = h(C(e)) - h(L(e)).                         (1)

For completeness, define h by integrating across dual edges, taking the
increment dictated by (1). Independence of dual path is exactly zero
signed circulation around each primal vertex, which is divergence-free
flow there. The plane, rather than the quotient cylinder, is used in this
construction.

The difference h(F+d)-h(F) is constant in F, since all edge differences
are d-periodic. Far outside the support strip, each of its two half-plane
components has f=0, so h is constant on it; F and F+d can be chosen in the
same such component. Thus this difference is zero. Consequently h itself
is d-periodic and descends to the full-drift cylinder.

Call its two exterior constants c_minus and c_plus. They are different.
Indeed, their difference, up to the choice of transverse orientation, is
the algebraic flow through a dual arc joining the two ends of the cylinder.
The flow is the sum of all actual directed traversals in the event cycle.
That one closed cycle lifts from p to p+d, so has winding number one on
the cylinder R^2 / Zd. Its algebraic intersection with a transverse arc
is one. Hence |c_plus-c_minus|=1. This remains true if d is nonprimitive
as a vector in Z^2: the quotient here is by d itself, and the full event
cycle still has winding one.

## 2. The local maximum rule

Define the shifted face height

    H(F) = h(F)       if F is C,
           h(F) + 1  if F is L.                      (2)

The translation d preserves checkerboard parity. To see this directly,
heading reset implies the period is even, and each lattice move changes
vertex parity, so d has even coordinate sum. Thus H is also d-periodic.

The four incident face values at every primal vertex obey the following
complete local table, up to rotation and adding an integer constant.
The words "adjacent" and "opposite" refer to corners of the surrounding
dual unit square.

- Empty vertex: two opposite values k, two opposite values k+1.
- Singleton R: three values k+1 and one value k.
- Double RL: two adjacent values k+1 and the other two values k.
- Opposite-heading triple RLR: three values k and one value k-1.

Here is an explicit way to verify the table without assuming a drawing.
At an even primal vertex, order the faces NW, NE, SE, SW and write their
unshifted heights b1,a1,b2,a2, where the a faces are C. The port traversal
counts then satisfy

    f_N=a1-b1,  f_E=a1-b2,
    f_S=a2-b2,  f_W=a2-b1.                           (3)

Insert a singleton R, either RL heading pattern (equal or opposite
incoming headings), or either opposite-first/third RLR pattern AAB/ABB.
More generally, if r_E,r_W count the R reads with incoming E,W, and
l_E,l_W count the L reads with those headings, formula (3) gives the
shifted tuple, up to an additive constant,

    (H_NW,H_NE,H_SE,H_SW) = (1-l_E, r_W, 1-l_W, r_E). (4)

The odd-vertex cases are rotations. The empty case has all unshifted
heights equal. This gives exactly the displayed table. The literal
local controls in `check_shifted_stream_local_table.py/json` check all
22 parity-oriented histories, the two-diagonal replacement rule, and
the horizontal doubled-edge barrier. They support the proof and are not
an independent audit.

In particular the maximum of the four H values is never unique. Therefore
both three-corner paths across either diagonal of a dual square have the
same maximum: deleting either one of the two nonendpoint corners cannot
remove every maximizing corner. Replacing an EN corner of a dual path by
its NE alternative preserves the maximum along the entire path. The same
statement holds for any rotated orientation. Notice that unique minima
are permitted and not used.

## 3. Every non-axis drift is excluded

An orientation-preserving quarter-turn puts any non-axis d in the form
(a,b) with positive integers a,b. Consider dual lattice vertices (face
centers). For each base vertex z and each monotone word w with a east
steps and b north steps, the lifted dual path P(z,w) goes from z to z+d.
It projects to a closed path on the full-drift cylinder. Define

    M(z,w) = maximum H on P(z,w).

All words with those counts are connected by adjacent EN/NE exchanges.
Section 2 therefore says M(z,w) is independent of w; call it M(z).

Choose a word beginning E. Delete that first E and append an E at its
end, now beginning at z+E. The resulting lifted path is the cyclic shift
of the same projected cylinder path: all its vertices agree with the old
ones except that the removed initial vertex z is replaced by z+d+E,
whose height equals H(z+E), already present. More explicitly the vertex
list z,z+E,...,z+d is replaced by z+E,...,z+d,z+d+E; periodicity gives
H(z+d)=H(z) and H(z+d+E)=H(z+E). Its maximum is unchanged. The shifted word
still has a east and b north steps, so

    M(z+E)=M(z).

A word beginning N exists because b>0. The identical cyclic-shift argument
gives M(z+N)=M(z). Thus M is constant over the entire dual lattice.

Translate a fixed finite monotone cut sufficiently far to either exterior
side of the support. On either such cut, h is the corresponding constant
c, and H alternates c,c+1 on consecutive face centers. Its length a+b is
positive, so it contains both face colors and has maximum c+1. Constancy
of M therefore forces c_minus+1=c_plus+1, contrary to Section 1.
This excludes every non-axis drift, without a strip-width or period bound.

## 4. Axis drift forces a separating row of doubles

Rotate an axis drift to d=(a,0), where a>0 is even. Index the horizontal
rows of dual face centers by y in Z and put

    m_y = max { H(x,y) : x modulo a }.

Far above and below, these row maxima are c_plus+1 and c_minus+1, which
differ. Therefore some two adjacent rows have unequal maxima. Name the
larger-max row U and the smaller-max row V; the argument does not depend
on which is geometrically above. Write M for the larger maximum.

Choose a face in U with H=M. In either neighboring dual square spanning
U and V, both V-corners are strictly below M. Since a unique maximum is
forbidden, the other U-corner must also equal M. Repeating horizontally
shows that every face of U has value M. Each intervening dual square now
has two adjacent maxima M and two strictly smaller values. The local table
forces the double-RL case, with both smaller values exactly M-1.

Thus every primal vertex of the entire horizontal row between U and V
is a double RL cell. At each such vertex, the two vertical ports have
count one; exactly one horizontal port has count two and the other has
count zero. One can obtain this either from (3), or from the double case
of the local table with its maximum pair horizontal. The doubled horizontal
edges therefore form a perfect matching of the row into adjacent dominoes.
This statement is in the physical plane; it also holds across the seam of
the cylinder, including a=2.

## 5. The double row cannot belong to one event cycle

Take a doubled horizontal domino directed east. Its source has two opposite
vertical incoming headings, and its target has two equal east incoming
headings. Because both complete histories are RL, chronological order
matches the first traversal at both ends and likewise the second. The
first passage is

    incoming N, then R to E, then R to S,

and returns to the lower side of the row. The second is

    incoming S, then L to E, then L to N,

and returns to the upper side. A west-directed domino has the rotated
version of exactly the same side-preserving property. No other horizontal
edge on the row is used.

Partition all actual event phases into two sets, the lower and upper
ones. Off-row events belong to their geometric side. Each of the two
paired two-event passages on a domino belongs to the side from which it
arrives and to which it returns. This assigns every row event uniquely.
All successor edges preserve the partition: crossings of the row can only
use its listed vertical ports, and the full passage returns to its own
side. Both sets are nonempty, since every domino has one passage belonging
to each side. The partition remains well defined in the full-drift quotient
because horizontal translation preserves the two sides.

This contradicts the fact that successor is the one cyclic permutation of
all event phases. Hence an axis drift is also impossible.

## Conclusion and scope

Sections 3 and 5 exhaust nonzero drift directions. Under the independently
signed same-type exclusion, no complete white-input translating Langton
front can have all physical-cell histories of length at most three.
Equivalently, any such front has at least one full-drift cell class with
multiplicity at least four. The theorem says nothing yet about cap four,
uniqueness of the standard104 front, eventual periodicity, or universal
capture from arbitrary finite black seeds.
