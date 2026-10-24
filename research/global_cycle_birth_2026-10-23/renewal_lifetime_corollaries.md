# Direct phase and lifetime consequences of the signed zipper theorem

23 October 2026, 22:26 UTC. Deductions from the independently signed
old_bridge_zipper_and_cycle_erasure.md (bfd61ce9...). No capture claim.

## A cleaner full-phase proof of the global erasure count

Split an actual interval at EVERY cycle-erasing L. At a phase entry of mass M,
the signed erasure-free theorem gives time<=3M+4 and mass<=2M+4 up to but not
including the next erasure. The erasing L costs one update and lowers mass
by one. Therefore its full phase costs<=3M+5 and has outgoing mass<=2M+3.

For j completed erasures,

    M_j<=2^j*(m+3)-3.

Sum D completed phases and the final phase without an erasure:

    T<=sum_(j=0)^(D-1)(3M_j+5)+(3M_D+4)
     <=3*(m+3)*(2^(D+1)-1)-4D-5
     <=6*(m+3)*2^D.

This uses actual successive complete boards, not a reset or finite summary.
It is the same bound as the signed exceptional-block proof.

## Every produced black lifetime spans an erasure before consumption

Let one physical R create a black lifetime, and let its later matching L
consume that lifetime. At least one cycle-erasing L occurs AFTER that birth
and no later than that consumption; the consuming L itself may be the erasure.

Otherwise the actual birth-through-consumption interval contains no erasure,
but the signed zipper theorem says every lifetime born by an R within such
an interval remains current throughout. Contradiction. Thus a death that is
itself a bridge deletion in BOTH graphs requires some earlier erasure after
its birth. Recycling cannot occur entirely inside a topology-free phase.

This is a lower-age condition in the actual global erasure clock, not an
upper lifetime bound or a finite charge on descendants. One erasure may
reactivate a large old archive, and infinitely many erasures remain allowed.

## Topological meaning of an erasure

An L erasing a cycle in one black graph adds the perpendicular WHITE edge in
the opposite planar lattice. Since the old black edge was nonbridge, planar
duality says its two opposite white endpoints belonged to DISTINCT white
components; the L merges them. The opposite active cursor is an endpoint of
that edge, so this is a genuine active-component merger. At least one merged
white component is finite, since a finite black board leaves only one infinite
white component in each lattice.

Consequently the global theorem also forces repeated actual mergers of a
finite white pocket into the active white component. The pocket may be active
or passive, nested or connected through earlier changes. This does not give
a LIFO archive stack, a bounded pocket cost, or permanent forgetting.
