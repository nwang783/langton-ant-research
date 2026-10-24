# Exact local-energy certificate protocol

This document describes a sufficient certificate, not a certificate already found.

## Physical coverage

After removing a finite prefix, any finite-support orbit with no adjacent forbidden ten-windows either follows W104, follows T24, or remains in the 34,712-state component H. T24 requires two infinite initial-black rays and is impossible. Every H path returns to the marker `LLLLRLRRRRLR` at gaps at most 74, with one of the five recorded return words.

The actual marker graph has 995 histories and 2,747 edges. On each source history, the past reads determine the current color at every cell they visited. For the 45 edges whose future first-read requirements contradict those colors, the full history-plus-macro word is impossible. Each remaining edge is assigned one of 166 color contexts. Unknown cells are arbitrary. Consequently a verified inequality on all assignments in a context applies to every actual orbit using its edge.

## Ordinary pattern energy

For a 3x3 pattern p, let w(p) be a nonnegative weight invariant under quarter rotations, with w(0)=0. Put

\[
E(B)=\sum_{q\in\mathbb Z^2} w\bigl(B\cap(q+\{0,1,2\}^2)\bigr),
\]

encoding each local pattern in row-major bits. A finite black set B intersects at most 9|B| such patches. Thus E(B) is a finite nonnegative number, and changes in E under a macro depend only on patches intersecting an odd-toggle cell.

Let phi be an arbitrary real potential on the finite set of 995 port histories. If every retained edge e:s->t satisfies

\[
\sup_{B\text{ compatible with context }e}\bigl(E(B')-E(B)\bigr)+\phi(t)-\phi(s)\le -1,
\]

then E+phi decreases at each marker return and has a finite lower bound. Infinite H paths from finite support are excluded.

A weaker sufficient certificate assigns edge cost 0 to U,V and cost 1 to C,Q,B. It forces finitely many turning blocks; the proved U/V fuel theorem then excludes the remaining eventual U/V tail.

Another sufficient choice assigns cost 1 only to V and Q, and cost 0 to C,U,B. Each after-marker V edge has exactly one forbidden ten-window, ending at appended index 1; each Q edge has exactly one, ending at index 47. The other three edge types have none. (The preceding marker supplies the full required nine-letter history.) This cost counts all future J events after the first port. A certificate would therefore force finitely many J events, and the existing finite-support ten-factor attraction theorem would finish the argument.

The ordinary 3x3 version is now exactly ruled out for every nonzero nonnegative cost assigned by macro type. The 159-context integer certificate in `../wake_clock/fold_farkas_certificate.json` cancels the port-potential columns and leaves all nonnegative pattern-weight columns nonnegative, while assigning positive total multiplier to every macro type. It therefore contradicts the required strict decrease for any such nonzero cost. Its independent verifier is `../wake_clock/verify_fold_farkas.py`. This is a negative theorem about the specified rank, not about highway convergence.

## Checkerboard-sector energy

Write chi(x,y)=(-1)^(x+y). Heading h is numbered north=0,east=1,south=2,west=3. During every ant step both heading parity and position parity flip, so

\[
\sigma=\chi(p)(-1)^h
\]

is constant along an orbit. Give each 3x3 pattern a weight w(s,p) where s is a sign, subject to

\[
w(s,0)=0,\quad w(s,p)\ge0,\quad
w(-s,\operatorname{Rot}_{90}p)=w(s,p).
\]

There are 272 combined rotation/sign orbits including the zero pattern, hence 271 independent nonzero weights. Define the fixed global energy

\[
E_\sigma(B)=\sum_q w\bigl(\sigma\chi(q),\operatorname{patch}_q(B)\bigr).
\]

Again it is finite and nonnegative on every finite black field.

The normalized contexts put the current ant at (0,0) facing north. Translation by the current position p changes the patch-origin checkerboard sign by chi(p). Rotating the pattern by h quarter turns changes the weight's sector sign by (-1)^h. Rotating a 3x3 square can also shift its lower-left origin by coordinates involving 2, which do not change checkerboard parity. Hence the resulting normalized sign is

\[
\sigma\chi(p)(-1)^h\chi(q_{\rm local})
=\chi(q_{\rm local}),
\]

using sigma=chi(p)(-1)^h. Thus the same normalized rule applies at every port: the phase bit is (q_x+q_y) mod 2, independent of its global position and heading. This establishes that the context oracle computes changes of one fixed global energy, not a different unrelated energy at each port.

The same strict, fold-only, or event-only inequalities, with E_sigma replacing E, would exclude H. No such certificate was obtained in this continuation. The event-only system was reported infeasible numerically after 6,268 explicit context cuts. No rational dual certificate was recovered, so this is not an exact exclusion theorem. The stricter sector search requiring decrease on every macro was interrupted; its nonconvergence is not a proof of infeasibility.

## Bounded head-local correction

The final targeted extension adds

\[
P(B,p,h)=\sum_{r\in\{-1,0,1\}^2}a_r\,1_B(p+\operatorname{Rot}_h r),
\]

with nine arbitrary signed coefficients. Its absolute value is at most sum_r |a_r|, so E_sigma+P+phi has a finite global lower bound. Across a fixed macro, P changes by a sum of unary functions of initial cell colors. The exact oracle can therefore add this correction without increasing its elimination width. The existing contexts retain all relevant known bits for radius one.

The sector event-only system with this correction generated 7,821 explicit context cuts before an interior-point solve reported infeasibility. Again this status is numerical: no exact dual certificate was recovered. No positive rank was found. The tested extensions are closed for this continuation; the remaining infinite-fold obligation stays open. Full search outcomes and compressed constraints are indexed in `../global_structure/macro_energy_status.md`.

## Exhaustive context optimization

Each affected 3x3 patch gives a factor in its unknown cell bits, equal to its weighted contribution after the macro minus before. Shared outside bits are shared variables. Binary variable elimination repeatedly adds all factors involving one variable, maximizes over that variable, and replaces them by the resulting factor. This algebra is exact for a finite maximum. It retains an attaining assignment by backtracking recorded argmax choices.

For the 166 conditioned contexts, the chosen elimination order has width at most 7: no combined factor has more than 8 bits. Therefore the complete maximum can be evaluated economically despite 15 to 70 unknown cells. With integer candidate weights, `exact_local_energy.py` performs exact int64 operations and checks a sufficient no-overflow bound. Each returned witness is directly rescored against all affected patches. A separate audit also compared one 15-bit context against all 32,768 assignments, without using elimination.

To make a discovered floating solution into a proof, scale and round all pattern weights and port potentials to integers, then recompute every context maximum and every edge inequality with exact integers. The final certificate must record all 166 maxima and all 2,702 edge slacks. Feasibility or apparent convergence of a floating LP alone is insufficient.
