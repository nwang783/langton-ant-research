# A finite upper cap bounds forward packet supply

22 October 2026. Independently analytically audited chronological strengthening of the packet endpoint lemma. It is independent of row/column root multiplicity. Without an additional geometric hypothesis it does not bound backward fingers. The oblique-strip refinement below bounds them conditionally; none of these results proves highway attraction.

## 1. Local cap lemma

Consider any finite legal sequence of elementary turns and complete G packets. Suppose every elementary read and every G near-end pair lies in the southwest quadrant

    x<=X,    y<=Y,

for fixed integer X,Y. G lengths and the lower/left extent of their roots are unrestricted. Fix a column z>X.

Only eastward Gs can read column z. At event boundaries, crossing Gs restore it; only far endpoints at z change its bits. Put

    n_y = (1+sigma*(-1)^(z+y))/2
          -sigma*(-1)^(z+y)*black(z,y).

These are0/1 occupancies. Every eastward far endpoint at z has signed change -1 at its lower cell and +1 at its upper cell, so it is exactly an exclusion hop

    (n_r,n_(r+1)) : (1,0) -> (0,1).

No endpoint uses a row above Y.

For any r<Y, the particle count in the FINITE cap [r+1,Y] changes only when a hop crosses edge(r,r+1). Such a hop increases that count by1; no hop crosses out above Y. Therefore the number of hops on this edge is at most Y-r, independently of all activity below it and of the initial colors.

For a valid adjacent pair(r,r+1), r<Y, the endpoint events that can change its colors use one of edges(r-1,r), (r,r+1), (r+1,r+2). Their counts are at most

    (Y-r+1), (Y-r), max(Y-r-1,0),

respectively, with the last edge absent when r+1=Y. Their sum is3(Y-r). Thus the pair's event-boundary colors change at most3(Y-r) times.

Between these events its colors are fixed. If it is an eligible eastward interior pair (physical lower1,upper0), adjacent overlapping pairs are ineligible. The established endpoint barrier therefore allows at most one G on this pair with far endpoint strictly beyond z during the interval: disjoint eligible pairs cannot repair its far barrier, and packets ending at or before z cannot touch that barrier. If the pair is ineligible, no such packet occurs.

Consequently at most

    3(Y-r)+1                                             (1)

east G far endpoints strictly beyond z occur on the pair(r,r+1).

A fixed row r<=Y belongs to at most two pairs, with lower rows r and r-1. Summing (1), and omitting any pair above Y, shows that at most

    6(Y-r)+5                                             (2)

east G far endpoints strictly beyond z touch that row. This is a bound on the NUMBER of such corner additions, not only their net parity. It permits infinitely many potential root rows below r; the finite upper cap replaces the old finite-height-band assumption.

## 2. Black supply and a forward depth bound

Restart the square ant at a permanent cut, with finite black mass m. Suppose its permanent roots q_i=(x_i,y_i) obey bounded northeast retreat:

    j<=i implies x_j<=x_i+Bx and y_j<=y_i+By,              (3)

where Bx,By are nonnegative integers. No strip confinement, periodicity, or uniform line multiplicity is assumed.

Expand B packets as before. Every earlier elementary read and G near-end pair before a packet in stage i lies in

    x<=X_i=x_i+Bx+4,
    y<=Y_i=y_i+By+4.

This includes earlier packets in the same stage. Apply Section1 to their finite chronological prefix at column z=X_i+1.

An east G in stage i uses a rail row r with |r-y_i|<=4. Outside z, only earlier eastward far endpoints can have changed that row; all other event masks lie on the root side. By (2), the black supply there at the current entry is at most

    m+6(Y_i-r)+5 <= m+6By+53.

The current near-end column is at least x_i-4, so at most Bx+9 strict-interior columns lie at or left of z. Its required black rail then yields

    east G depth <= m+Bx+6By+62.                         (4)

For a northward far endpoint at a row above all prior roots, the signed change is -1 at its left corner and +1 at its right corner. Hence its occupancy hop is to the RIGHT. The identical finite-cap argument, with x and y interchanged, gives

    north G depth <= m+By+6Bx+62.                        (5)

This interchange is a proof using the symmetric mixed difference and exact G masks, not an invocation of reflection symmetry of the white/right ant rule. No global color complementation is used.

The two bounds are noncircular: neither uses a bound on any other G depth. All earlier vertical fingers stay behind the x slab regardless of their length, and all earlier horizontal fingers stay behind the y slab regardless of theirs.

## 3. Exact scope and remaining memory

Bounds (4)-(5) improve the forward half of the periodic-core supplier proof: they require only the two core-retreat bounds, not line multiplicity or an oblique strip. Westward and southward fingers remain uncontrolled. Their roots may advance while they repeatedly access old rails extending arbitrarily far behind.

There is nevertheless a precise geometric consequence. Every physical read in stage i lies at coordinates

    x <= x_i+4+max(1, east-depth-bound+1),
    y <= y_i+4+max(1, north-depth-bound+1).

So a bounded-retreat northeast core cannot conceal arbitrarily large FORWARD excursions. Any unbounded decoration must be backward archival access. This does not imply bounded physical retreat: a completed west/south finger may still travel a long distance and return to the current root.

For a later stage k>=i, its roots satisfy x_k>=x_i-Bx and y_k>=y_i-By. Horizontal packets and elementary reads have row within4 of their root; vertical packets have column within4. Therefore no later event can read a cell in the strict southwest quadrant

    x < x_i-Bx-4 AND y < y_i-By-4.

Together, these facts confine potentially reusable old information to two backward axis-parallel arms, after separately accounting for initial bits that have not yet been passed. The arm lengths and their information content are not bounded. A proof that these arms cannot sustain nonstandard recycling is still missing.

## 4. A backward upper cap under oblique core confinement

Add the oblique-strip hypothesis

    c <= v*x_j-u*y_j <= c+Delta,

with u,v>0. The forward bounds (4)-(5) are already valid without this hypothesis. Let N be the uniform north-depth bound from (5), and consider a west G in stage i with rail row r. Define

    J = ceil((u(N+10)+Delta)/v),
    z = x_i-J-5,
    Y = y_i+By+4.

We first exclude non-west suppliers throughout the WHOLE region

    x<=z,    y>=r-1.                                   (6)

An earlier north G that touches a row y>=r-1 has root

    y_j >= r-1-N-5 >= y_i-N-10.

An earlier south G touching that row must start high enough to reach it, giving the stronger y_j>=r-5. The same stronger bound holds for an elementary read there and for a horizontal G near-end pair touching those rows. In every case the oblique strip yields x_j>=x_i-J. Therefore all these vertical/elementary sites and horizontal near ends have x>=x_i-J-4=z+1. Eastward packets start to the right of z and move farther right. Hence they cannot enter (6). Only westward packets, with near ends to the right of z, can read the region.

This exclusion is deliberately for all y>=r-1 and all x<=z. A statement only about the cut column would not prevent remote barrier repair.

At column z, west far endpoints are DOWNWARD exclusion hops. In the finite cap [ell+1,Y], each hop across edge(ell,ell+1) decreases particle mass by1; there is no incoming activity above Y. Thus the same bound Y-ell applies to each such edge. In particular, even the lowest relevant hop across(r-2,r-1) is bounded by the finite cap[r-1,Y]. Activity below r-1 cannot replenish that cap because all allowed hops go downward.

The two rail pairs meeting row r therefore have at most6(Y-r)+5 far endpoints strictly left of z, by the same three-edge count and disjoint-pair barrier. Region (6) ensures that no other event can repair the barriers farther left.

At current entry, row r consequently has at most m+6By+53 black bits left of z. At most J+9 strict-interior columns of the current west G lie at or right of z. Hence

    west G depth <= m+J+6By+62.                        (7)

Interchanging coordinate labels, with the exact south endpoint hop directed LEFT, gives

    K = ceil((v(E+10)+Delta)/u),
    south G depth <= m+K+6Bx+62,                       (8)

where E is the already established east-depth bound (4).

Thus oblique core confinement plus bounded coordinate retreat directly yields uniform depths in all four directions. Neither row/column multiplicity nor the finite-state dwelling bound is needed for these explicit depth estimates. The full trace lies within a bounded enlargement of the core strip, and the inherited non-axis-strip theorem gives translating periodicity. This is the same qualitative implication already proved by the independently audited dwelling route, now with much smaller quantitative constants.

## 5. Unconditional historical core/trace envelope

The finite-prefix proof did not require the retreat constants to remain valid in the future. At a packet in stage i, it suffices to substitute the actual lags

    Bx_i = max_(j<=i) x_j-x_i,
    By_i = max_(j<=i) y_j-y_i.

Let a finite complete-stage prefix have root bounds xmin,xmax,ymin,ymax and spans

    Dx=xmax-xmin,    Dy=ymax-ymin.

For an eastward packet in stage i, its farthest x coordinate is at most

    x_i+4 + [m+Bx_i+6By_i+62] +1
      <= xmax+m+6Dy+67.

The longitudinal lag Bx_i cancels against x_i. Apply the half-turn version to westward packets, using lags above historical minima, to obtain the corresponding lower bound. North and south give the analogous estimates with coordinates exchanged.

Every elementary read is already within distance4 of its stage root. Hence the ENTIRE physical read trace through this finite stage prefix is contained in

    [xmin-m-6Dy-67, xmax+m+6Dy+67]
      times
    [ymin-m-6Dx-67, ymax+m+6Dx+67].                      (9)

The same bound holds during the last packet of the prefix, since its whole finite support was bounded at entry. The finite initial ant prefix before the chosen permanent cut is not included; its black field at the cut is represented by m.

In particular, if every core root in this prefix is at l_infinity distance at most R from its first root, all physical reads have distance at most13R+m+67 from that root. This is an unconditional historical-size comparison. It does not compare the current physical head with the current core root, does not bound retreat, and does not imply that physical or core sites are visited only finitely often.

The envelope gives an alternative quantitative proof that a bounded physical permanent core would force a bounded full trace. It does not replace the stronger mass-independent consecutive-stage dwelling bound, whose control concerns stage count rather than read extent.
