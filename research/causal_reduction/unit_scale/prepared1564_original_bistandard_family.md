# The original184-cell family is already bi-standard

23 October 2026. Author backward certificate, submitted for independent review.

Keep the exact signed seed family and poses in
`prepared1564_uniform_support_manifest.json`, SHA256
90fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399.
For every N>=1 it has184 black cells and original head
(33+14N,70+14N), heading W. No completion cells are added.

Forward capture for EVERY N is separately independently signed in
`prepared1564_source_endpoint_capture.md` SHA256
0570b39260cb809fc6287561d8a34ef4b5a9a1c4dffcaee6ec7b09d536572f75.
For N>=4 its exact complete future adjacent-defect count is614N+25508.
The present additional certificate proves backward capture for the ORIGINAL
same state, hence already bi-standard examples at mass184 rather than196.

Use the exact reversal conjugacy: leave the board unchanged and replace pose
(p,h) by(p-d_h,-h). Since the original heading is W, the backward ant begins
at(34+14N,70+14N),E. Normalize by the ORIGINAL head(33+14N,70+14N).
Its13-cell canonical source is independent of N and the backward pose is(1,0),E.

The complete canonical backward trajectory has2589 reads and527 distinct read
cells before a permanent standard104 tail at(9,-25),S, drift(2,-2). Its board
then has286 black cells. The literal word and complete final field are in
`prepared1564_reverse_source.json`; the retained exact finite-board tail checker
proves every future tail read, not merely repetition through a chosen horizon.

All other171 original black cells have normalized positions

    b_j + a_j*N,

where both coordinates of a_j are equal and nonzero. For each of the527 finite
prefix cells, exact coordinate equality excludes every integer N>=1. For each
of the104 infinite tail read slots q_i+k(2,-2), k>=0, the coordinate sum determines
N uniquely because the tail drift has coordinate sum zero, while a_j has nonzero
sum. Exact divisibility and the second coordinate then exclude every integer
N>=1,k>=0. This includes ALL remote original router and launch cells. No claimed
bounded radius or finite repeat horizon replaces these checks.

Consequently the171 extra cells are inert throughout the entire backward
trajectory. The complete family's backward ant reaches its permanent104 tail
at time2589, pose(42+14N,45+14N),S, current mass286+171=457. Its full future drift
is(2,-2). Together with the separately signed forward capture, this establishes
bi-standard capture for every original184-cell member.

Artifacts:
- `check1564_reverse_source.py`, `prepared1564_reverse_source.json`.
- `certify1564_backward_family.py`, `prepared1564_backward_family.json`.
- Canonical source JSON SHA2566ac01ba866e858f229f7f765b58a7c13ede913ec3cc863e8163ca8f8302c8e69.
- Affine ownership checker SHA256095502139c19ca5185d466c296e724828d3520dc9feca6a40fdcde726aca2ce3.

The conclusion is an unbounded defect budget within already bi-standard finite
orbits of fixed current mass184. The different members have increasing seed
diameter; this does not produce one finite seed with infinitely many defects,
renewal, or a counterexample to eventual capture.
