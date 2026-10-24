# Every pristine three-phase self-copy builder fails by its fourth excursion

Status: elementary analytic derivation; independent review requested. The right half-plane is initially all white. No row-span or width bound is assumed.

## Statement

Let three controlled right-half-plane entry poses be (0,r_j,E), and exits (-1,s_j,W), with the r_j all of one parity. Repeated rows are allowed. Suppose the half-turn self-copy port equations hold with delta=2:

    s_j=S-r_(j+2 mod3).

External resets change no right-half-plane cell. Then at most three prescribed excursions can complete from the pristine field. Exactly two normalized port families complete three, and both fail on excursion four.

The constant-entry special case is already impossible on its second excursion; any nonconstant three-period entry sequence has minimal period3 and therefore requires delta2 for this self-copy construction.

## Proof by the first three entries

Translate vertically so r_0=0. All other r_j are even. The first excursion is RR, exits at row-1, and leaves black cells (0,0),(0,-1). Success forces S=r_2-1.

### Case r_1=0

The second excursion is LRRRRL. It exits at row1 and leaves exactly

    (0,-1),(0,0),(1,0),(1,1)

black. Since s_1=S-r_0=r_2-1, success forces r_2=2 and S=1.

The third excursion from row2 is RR, exits at row1 as required, and adds (0,2),(0,1). The fourth excursion reenters row0 and is LL, exiting at row1. Its required exit is the first phase's row-1, so it fails.

Thus this branch's sole three-success family is

    r=(0,0,2), s=(-1,1,1), S=1.

### Case r_1=b is a nonzero even integer

The first entry into row b uses a disjoint two-cell pair, so the second excursion is RR and exits at b-1. Success forces r_2=b and S=b-1. The third excursion must exit at s_2=S-r_1=-1.

If b is neither0 nor-2, its second entry executes LRRRRL without touching either initial row0/-1 cell, and exits at b+1. That cannot equal-1. If b=-2, the third entry is instead LL: its second read at (0,-1) uses the first excursion's surviving black bit. It exits at-1 as required and leaves exactly (0,0),(0,-3) black.

The fourth excursion from row0 is then LRRRRL and exits at row1, again differing from its required row-1.

Thus this branch's sole three-success family is

    r=(0,-2,-2), s=(-1,-3,-1), S=-3.

This exhausts all same-sector entry rows. No bounded search or global highway claim is used.

## Scope

This excludes only pristine initialization for a three-phase half-turn copy with the stated port equations. It does not exclude a finite nonempty initial cap, a longer periodic port word with repeats, two different complementary builders, or an internal four-state controller at fixed physical ports. It also does not assert that a controlled prefix is itself autonomous.
