# A fixed max-plus candidate cannot be repaired by bounded future conditioning

Date: 22 October 2026. This is an all-parameter obstruction for the specific final tested port-dependent max-plus candidate in `maxplus_last_port_candidate.json`. It does not exclude other potentials, and it is not a finite-seed infinite H trajectory.

## Exact quantified two-successor test

The final tested candidate has 511 field-pattern weights and 3,980 heading/port weights. Among its 20,125 saved violating upper strips, an exact physical extension test gives:

| Extension of the prescribed first macro | Number of strips |
|---|---:|
| No following macro is possible | 6,550 |
| One following macro is possible, but two are impossible | 4,884 |
| Two following macros are possible | 8,691 |

All choices follow the actual 995-port graph. Initial cells below the fixed upper strip may receive either color when first read, subject to every known history color. Thus these counts quantify over all lower completions for each fixed upper-strip assignment, not only the originally returned all-white completion. The test examines 65,965 candidate macro extensions. The scripts retain a literal finite coloring for the first surviving V,U,U path and verify the potential increase directly.

## One survivor extends to every finite horizon

Use the after-marker convention. Let B0 be the 75-cell finite coloring recorded in `arbitrary_lookahead_verification.json`, with head (0,-3), west, at port 3. Its first three macro edges are

\[
3\xrightarrow{V}721\xrightarrow{U}282\xrightarrow{U}633.
\]

The head after these macros is (-11,-2), west. For each integer n>=0 put

\[
G=\{(0,0),(0,-1),(1,-1),(-1,0),(-2,-1)\},
\]

\[
B_n=B_0\;\cup\!\bigcup_{j=0}^{n-1}\left((-11-4j,-2)+G\right).
\]

Then B_n is finite and realizes

\[
V\,U^{n+2}.
\]

Its initial mass is |B0|+5n. All added cells have y=-3 or -2 and x<=-10. The exact graph path after the first two U blocks is

\[
633\xrightarrow{U}690\xrightarrow{U}749\xrightarrow{U}212
\xrightarrow{U}212\xrightarrow{U}\cdots.
\]

So these are actual H paths, not merely words over an unconstrained five-letter alphabet.

## All-parameter physical proof

An after-marker U started north at the origin ends at (0,4), north, and its read footprint is contained in [-1,2] times [-1,3]. For two consecutive U blocks, the second block's new initially black cells, relative to its own start, are exactly

\[
F=\{(0,0),(-1,0),(-1,-1),(0,1),(-1,2)\}.
\]

Rotating west gives G. Westward U blocks translate by (-4,0). Their read boxes intersect only those of immediately adjacent U blocks; nonadjacent boxes are disjoint. The exact U,U interface check therefore proves the arbitrary-length fuel formula inductively.

For the displayed base state, every prescribed 149-history cell has x>=-5, every initially black cell of B0 has x>=-9, and the first additional U reads only x in [-14,-10]. Its only possible contact with the earlier trajectory is the one-column interface with the preceding U, already covered by the exact pair check. Every later block has the same geometry shifted four cells west. The added cells are exactly the fresh first-L cells, and all other previously unvisited cells remain white. This proves feasibility for all n.

## Why the potential inequality remains false

For this tested candidate the restricted upper strip begins at y=0. Adding any of the displayed fuel cells affects only 3 by 3 centers at y<=-1; all pattern weights are at most zero. Hence these additions cannot create a nonnegative field contribution, and they do not alter any upper-strip pattern. The initial potential remains exactly zero.

The first V flips the cell (-1,0). At the patch centered at (0,1), this changes the binary mask from 390, whose weight is -1, to 391, whose weight is 0. That patch's contribution consequently increases from zero to one. The initial source and final target head terms do not dominate it. Direct full-field verification gives

\[
\Phi(B_n,(0,-3),W,3)=0,
\qquad \Phi(\text{state after }V)=1
\]

for every n. The added fuel lies far to the west and below the strip, so the same local mask change persists.

Therefore no fixed number of future H macros can remove all violating initial states of this particular candidate: choose n long enough. This identifies a concrete limitation of the candidate. A local edit changes the weight assigned to an existing upper pattern, while the ant subsequently moves away along a rail whose extra finite fuel lies below that pattern.

The family does not realize an infinite U tail from one finite coloring. Its required initial mass grows by five for each extra U, exactly as in the previously proved U/V fuel theorem. Nor does it refute the conjectured four-cell fuel-hull bound: all added fuel is itself part of the initial first-L set.
