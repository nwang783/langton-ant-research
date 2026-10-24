# Radix thirteen coordinate-mixing image residual

23 October 2026. Bounded-family computation submitted for independent audit.
No counterexample or general finite-seed theorem is asserted here.

Let A=[[3,2],[2,7]] and k=13. Consider all four-independent absolute-direction
substitutions with net image displacement A*d, odd alternating axes and
source-axis preservation. Neither half-turn covariance nor a bijective
first-letter map is assumed. The raw image inventories N,E,S,W have sizes
15,315,15,315. Internal ant legality for either possible perpendicular
incoming heading leaves 15,91,15,91 images, or 1,863,225 controllers.
Every retained image meets A Z^2 only at its own source and target. This
claim is frozen per image in `mixed_k13_3_2_2_7_inventory.json`.

North/south images have fixed first and first-endpoint-arrival directions
N/S. Of the controllers, exactly 581,175 have BOTH first-letter map F and
first-endpoint map H permutations; audit GN excludes them for finite support.
The remaining 1,282,050 controllers are the explicit residual tested here.
The program's 17,100 pruning counter counts DFS branches, NOT controllers.

`search_mixed_direction_residual.cpp` performs a literal last-turn DFS over
phi^2(E), with images chosen consistently on first occurrence. Every east
image contains all four letters, so reaching a leaf assigns every image.
Up to a global half-turn there is either a fixed E first letter or an E/W
first-letter two-cycle. Both perpendicular initial headings are tested.
This is complete because every first-letter map on the horizontal pair has
a cycle, and the whole family is closed under half-turn conjugation. The
long replay uses an even iterate, so the two-cycle prefix is genuinely
nested. N/S-rooted or shifted languages contain these same conflicting
factors: every phi^2 image contains every letter, hence the substitution is
primitive. That language argument applies to literal conflict rejection;
the GN branch instead uses GN's direct rooted-cycle finite-support theorem.

The completed uncapped run tested all 182 root-image/heading cases and
126,478 candidate-image attempts, reaching 18 full legal 169-read leaves.
All 18 fail by zero-based read221 in a longer even-iterate prefix. There are
no finite-prefix survivors. Exact images, first conflicts, scope counts and
hashes are frozen in `mixed_k13_3_2_2_7_manifest.json`; the untouched raw
output is `mixed_k13_3_2_2_7_residual.log`.

This parameter was selected because the preceding controller-free local
record test genuinely SURVIVES, not by merely increasing a failed scan bound.
The matrix belongs to A_l=[[3,2],[2,2l+1]], k=4l+1. For every l>=2 the dual
normal (-2,3) satisfies the exact pristine-record ceiling. At l=2 the forced
E/S continuation is impossible (GP). At l=3 it exists, and the stronger
occurrence-dependent two-level local record relaxation also has legal
16-coarse-step/208-fine-step fragments. Those positive local controls are
`oblique_family_ell3.json` and `oblique_twolevel_n16.json`; neither is a
finite-support model. They distinguish the failed fixed-controller reuse
from the remaining occurrence-dependent construction question.
