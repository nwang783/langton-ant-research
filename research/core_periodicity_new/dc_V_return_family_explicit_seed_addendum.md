# Explicit seed and funding margin for the signed DC/V return family

23 October2026 11:48 UTC. This clarifies the immutable1119 proof; that bundle is
not modified. The independent all-r checker already verifies this simple seed.

The seed is exactly the canonical K, the cell(0,1), and for j=0,...,r the three
cells(-2-3j,2+j),(-1-3j,1+j),(-1-3j,3+j). In the certificate coordinates the
three disjoint rails are ell=-3,delta=0..r; ell=-5,delta=-1..r-1; ell=1,
delta=1..r+1. The six fixed cells are K plus(0,1), so mass3r+9 is immediate.

For canonical diagonal height X+Y the sourceDC score is16, outgoingV at p_n
has score12-4n, farVCC has score20-4r, and incomingV at q_n has score24-4n.
The strict incoming indices are n=r,...,0 and the final target is n=-1.
Consequently ALL earlier created peaks are<=24 and the target peak is28.
The entering-core values obey the same strict upper bound24. This does not
make the event unfunded: the initial residual(-1,3), always consumed by the
first outgoingV or the farVCC when r=0, has activation I+4>=32 at I>=28. The
funding margin is a constant4, independent of r, while the far low rails grow.

Thus neither an unbounded helper count nor the fact that the target is a new
CREATED record can be substituted for the full unfunded historical premise.
