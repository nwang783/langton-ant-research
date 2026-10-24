# Age-five residual genealogy has coordinate speed at most three quarters

Status: author exact arithmetic controls pass, 2026-10-23 08:27 UTC; independent corollary review requested. Uses the independently replayed KV age-five consequences. This is a strict spatial-speed and quantitative-duration improvement, not a C upper bound or confinement.

Use the signed KP auxiliary forest: every fresh residual output is a child of one chosen consumed residual input. Choose D/DC input(0,1), V/VC input(1,2), and VCC/U/UC/UCC input(0,3). The chosen produced-input age minima are now A=3 for D/DC/V/VC and A=5 for VCC/U/UC/UCC, by JO and KV. The exact-age4 holes for D/V are NOT needed in this corollary.

An identity's birth clock b is the C count at its producer packet START; its birth heading is that packet's heading. If a produced parent has heading h and its child has heading h', the C gap n is at least the child's required A and satisfies n=h−h' modulo4. Let d be the physical +y displacement from parent input cell to child output cell. Define

Phi=(0,5,6,3).

Every literal output satisfies

4*d <=3*n+Phi(h)−Phi(h').                         (1)

It suffices to check the least n>=A in its residue class; increasing n by4 adds12 on the right. The author checker reconstructs all1,088 fundamental output cases and all four rotated directions. Telescoping along produced-parent ancestry gives coordinate speed at most3/4, with endpoint potential error at most6/4. This is about ancestry, not instantaneous head speed.

## Initial identities are exempt: a separate boundary calculation

Do NOT apply the new age-five premise to an initial identity using virtual birth−4. Instead handle the first edge separately. If the factor's entry heading is h0 and the first output in an ancestry chain is born at clock b and heading h, then h=h0−b modulo4. Let d0 be its displacement from its initial-root input cell. Direct finite geometry gives

4*d0−3*b+Phi(h) <= K(h0),
K=(16,13,18,15).

For fixed h, it suffices to check b=(h0−h) modulo4 in{0,1,2,3}; adding4 only lowers the left side. Combining this first-edge bound with(1) gives, for any descendant born at clock B,

4*(y_descendant−y_initial_root) <=3*B+K(h0)−Phi(h_descendant).

All four rotated coordinates obey the same bound, with rotated headings. Since K<=18 and Phi>=0, every current residual cell at total C count j lies within L-infinity distance

R_j=floor((3*j+18)/4)

of one of the m−5 entry residual cells. Surviving entry identities have distance0. This improves KP's radius j+4; R_j<=j+4 for every j>=0.

## Duration consequence

The signed fixed-heading epoch proof applies with this smaller radius. Every consumed input in an epoch is an epoch-entry identity. Its chosen relative diagonal projection is1 or3. A packet start associated to root z therefore lies in

[p(root)−2R_j−3, p(root)+2R_j−1].

This interval contains at most2R_j+2 positions of the fixed start parity. Thus

L <=28*(m−5)*sum_{j=0}^k(2*floor((3*j+18)/4)+2)+15*k.   (2)

For q=floor((k+1)/4) and s=(k+1) modulo4, the sum is exactly

12*q^2+38*q+6*q*s+[0,10,22,36][s].

A simpler, slightly weaker polynomial bound is

L <=7*(m−5)*(k+1)*(3*k+44)+15*k.

The leading quadratic coefficient improves from28(m−5) to21(m−5); the exact floor sum never weakens the preceding signed bound. The asymptotic order stays quadratic.

## The speed and recurrence bounds are compatible

The necessary lower recurrence k=Omega(sqrt(L)) and the upper spatial radius O(k) with coefficient3/4 are NOT contradictory. Substituting L proportional to k^2 satisfies both; reducing a positive spatial-speed coefficient changes constants, not exponents. Mass creation is also compatible:3k new mass fits inside O((m−5)k^2) available cells. No global lower linear speed for the actual cursor follows from packet endpoints. At the purely kinematic level, four rotated blocks(D^r DC)^4 have zero net displacement, restore heading, use4 C macros and have duration40r+100. This is NOT asserted to be a physically legal ant family; it only prevents a displacement-only contradiction.

Even adding the new exact-age4 holes and physical output parity does not improve the coefficient3/4 in the limited age+heading+output-slot relaxation: there is an abstract cycle

(h0,odd output) --U/VCC,n6,dy3--> (h2,even output)
 --DC,n3,dy3--> (h3,even output)
 --VC,n3,dy3--> (h0,odd output).

Use child outputs(0,0),(3,1),(2,5), respectively. The total gap is12 and displacement9. These states and ages satisfy only the stated relaxed per-edge conditions; no common physical word, HB realization, or renewable ledger is asserted.

A multigeneration contradiction would need an additional conserved/decreasing quantity coupling branches, actual chronology or complete white contexts. Positive speed slack alone can accumulate without bounding the total C count. Finite initial roots do not bound descendants. No further generic capped record search is used here.
