# Oblique-record exclusion for a genuinely mixing matrix

23 October2026,01:06 UTC. New analytic reduction and80-case geometric
certificate submitted for independent review. No uniform image/controller
assumption is used, and the universal finite-seed conjecture remains open.

## Statement

Let A=[[3,2],[2,5]]. No finite-support classical ant path satisfies

    p(9n+c)=rho A p(n)+d   for every sufficiently large n,

where c is an integer, d is an integer vector, rho is any orientation-preserving
quarter rotation, and all asserted indices are nonnegative. In particular,
both pure identities p(9n)=+/-A p(n) are impossible. The images used at
different coarse occurrences may be completely unrelated, and the headings
at n and9n+c need not agree.

A has determinant11 and eigenvalues4+/-sqrt5, both greater than1. It is neither
a Gaussian scalar nor a signed monomial matrix. Thus this is outside the
previous scalar/rectangular fresh-band arguments.

## 1. An exact dual-coordinate prefix ceiling

Put L(x,y)=-2x+3y. Then

    L(A(x,y))=11y.

Every nine-step ant macro alternates movement axes. Its compass counts are
forced by its displacement A times the coarse movement letter:

    source N: N5,E3,S0,W1, starting on the vertical axis;
    source E: N3,E4,S1,W1, starting on the horizontal axis;
    source S,W: half-turns of the above.

No color feasibility is imposed when enumerating these words. There are
4 north words,20 east words,4 south words and20 west words. Their PROPER
prefix L ranges, including the empty prefix but excluding the endpoint, are
respectively[0,10],[-7,7],[-10,0],[-7,7]. In particular every proper prefix
of every allowed macro has L<=10. Every north macro ends heading N because
all of its vertical movements point north.

These assertions follow directly by choosing sign positions in the alternating
slots; the frozen certificate enumerates all48 geometric words independently
of any substitution or ant simulation.

## 2. A pristine oblique half-plane at a coarse north record

First take the pure positive identity. Let n be the first coarse arrival at
a sufficiently high north row Y, at q=p(n). Every earlier coarse center has
y<=Y-1. For every earlier macro m<n and proper image prefix v,

    L(A p(m)+v) <= 11(Y-1)+10=11Y-1.

Choose Y so high that all initially black fine cells also have L<11Y. Then
immediately before time9n, the ENTIRE half-plane L>=11Y is pristine white.
Normalize A q to the origin. The fine ant faces north: its preceding coarse
step was N, and every possible corresponding fine north macro ends N.
The normalized fine coloring is white on L>=0 and arbitrary on L<0.

At the coarse north record, the first read is fresh R, moving E. The next
cell is also fresh in the same new row, so the next coarse read is R,
moving S. Therefore the next two fine macro displacements MUST be A E=(3,2)
and A S=(-2,-5). Their geometry is one of exactly20*4=80 east/south word
pairs. This uses only the actual two forced coarse turns, not repeated image
rules or a conjectured controller.

## 3. The eighty-case local contradiction

Replay each pair from(0,0,N), with every first read on L>=0 required R and
with every initially unknown cell below that half-plane assigned whatever
first color the pair demands. Any later visit must use the flipped color.
Every one of the80 pairs conflicts. The latest first conflict is at zero-based
read15, before the two nine-step macros end. Four east words survive their
first block, but none has a compatible south continuation.

This local relaxation forgets ALL actual previous colors on L<0. Thus its
impossibility applies to every finite-support history meeting the pristine
half-plane premise. `check_mixed_matrix_oblique_record.py/json/records.json`
contains the complete raw inventories, extrema and first-conflict records.
The proof needs no long-prefix search, state bound, seed bound or solver.

## 4. Eventual offsets and quarter rotations

For the stated affine identity, define the fine ant
q_f(t)=rho^(-1)(p(t)-d), retaining its rotated/translated finite coloring.
Then q_f(9n+c)=A p(n), so all macro geometry and dual-coordinate bounds above
are unchanged. Discard the finite fine history before9n0+c and choose the
coarse record Y beyond its L maximum and all initial black L values. This
also covers negative c once the asserted times are nonnegative.

Arbitrarily high records in at least one sign of the coarse y-coordinate
are guaranteed. Write B=rho A and T(n)=9n+c. B is expansive: for rho=0 or180
its eigenvalue magnitudes are4+/-sqrt5; for rho=90 or270, B^2=-11I. Subtract
its affine fixed point x_*=(I-B)^(-1)d. Iterating the index relation gives
p(T^r n)-x_*=B^r(p(n)-x_*). Choose a sufficiently late n with p(n)!=x_*.
If its y-coordinates stayed bounded, the nonzero entry B_yx and the recurrence
for consecutive y-coordinates would also bound its x-coordinates, contradicting
expansiveness. Hence the y-coordinate is unbounded in one sign. A global
half-turn selects the north sign and preserves the same relation.

The coarse record itself is beyond its finite initial black support, so its
RR launch is valid independently of the fine pristine-half-plane argument.

## 5. Reusable adjugate method, not an all-matrix conclusion

For a general integer matrix M of positive determinant D, the second row
lambda of adj(M) satisfies lambda M=D e_y^T. If every geometrically possible
macro's proper prefixes have lambda-value at most D-1, a coarse north record
creates a pristine fine half-plane through its aligned endpoint exactly as
above. Its required macro continuations can then be checked on that oblique
white half-plane. The analogous first adjugate row treats east records.

This gives a reusable sufficient obstruction test. It does NOT say that every
expansive matrix has the prefix ceiling, that every resulting local continuation
fails, or that arbitrary finite-support ants have a self-similarity relation.
