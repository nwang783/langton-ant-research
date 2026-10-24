# A fixed-184-cell family with unbounded nonstandard transients

23 October 2026. Explicit construction and exact verification package.

## Result

For every integer N ≥ 1, the supplied formulas specify a finite Langton-ant board with **exactly 184 initially black cells**, all other cells white. Every member of the family has an ordinary standard104 highway in both time directions. Nevertheless, its forward nonstandard activity is unbounded as N grows.

The initial head is at (33 + 14N, 70 + 14N), facing west. The complete seed coordinates are in `family_data.json`: each coordinate pair `[[a,b],[c,d]]` denotes the cell (aN+b, cN+d). Translation and proper rotation can put the initial head at any fixed conventional pose without changing the result.

The actual ant executes a connected sequence of seven standard flights, six finite routers, a 24-turn launch and N periods of a primitive 1564-turn nonstandard translating word. All 184 bits are present from time zero; no cell is subsequently edited externally. The word's displacement is (14,14) per period.

For N ≥ 4, the ant then executes a fixed additional 56,504-turn continuation and reaches a permanent southwest standard104 tail at the certified section

- time 148251 + 25588N;
- head (14N−104, 14N−24), facing north;
- current black mass 13137 + 2876N.

These are certified tail sections, not claims of the earliest possible highway onset. The three smaller members are verified separately.

## An exact measure of nonstandard activity

Let H be the supplied standard104 turn word. Its cyclic length-ten factors form a set of 84 words. At each update, count one defect when **both** the preceding and the newly shifted ten-turn windows lie outside that set. The windows use the ant's genuine inverse history, not an artificially padded prefix.

For this family the inverse ten turns at time zero are `LRLRRRRLLL`. Through the end of the prescribed N wave periods, the exact defect count is

**614N + 92.**

For every N ≥ 4, the complete future defect count, including endpoint scattering and the permanent highway, is

**614N + 25508.**

The three exceptional complete counts are:

| N | Certified permanent-tail time | Total future defects |
|---:|---:|---:|
| 1 | 168023 | 23473 |
| 2 | 304638 | 78226 |
| 3 | 285897 | 49897 |

Thus no finite bound depending only on the number of initially black cells can bound this actual defect count, **even when restricted to already bi-standard, capturing finite orbits**. In particular, the supremum over such inputs with at most 184 black cells is infinite.

## What this does not prove

- It is **not** a finite-seed counterexample to eventual standard-highway capture. Every supplied member captures.
- It does not give one finite board with infinitely many defects. Different N give different cell positions and increasing seed diameter.
- It does not establish the universal finite-seed capture conjecture, which remains open.
- The value 184 is not asserted minimal. No claim of literature novelty or external publication is made.
- The wave alone requires increasing current-board fuel. Its exact minimum input for n isolated wave periods is 197n+1 black cells. The earlier standard flights manufacture that fuel from the 184-cell original board; there is no contradiction.

## Why the verification is all-parameter, not extrapolation

### 1. Exact initial input and full prefix chronology

Every stage is a fixed literal word repeated an affine number of times. Every read and initial cell therefore has an exact form

`position = constant + coefficient*N + drift*k`, with `0 ≤ k < cN+d`.

The verifier groups physical cells by transverse coordinate, parity and a residue modulo seven. Within each group, eligibility is an integer interval with affine endpoints. Every pairwise endpoint crossing partitions the entire integer domain N ≥ 1 into regions of fixed ordering. On each region and spatial interval it checks the **complete chronological read list**, alternating colors, and equality of its first-black requirements to the supplied seed.

This proves all of the following simultaneously for every N:

- the whole connected prescribed word is legal;
- all earlier writes and all preloaded seed bits are retained;
- the 184 seed cells are distinct;
- each seed is genuinely needed and used;
- no unlisted initial black cell is required.

There are 1,460 physical classes, 1,508 parameter regions, 4,581 spatial intervals and 17,470 read obligations. The resulting global integer-region starts happen to be 1 and 2, but the proof explicitly checks the infinite terminal region. It is not a two-sample extrapolation.

### 2. Exact endpoint stabilization

At the checkpoint after N wave periods, translate by (−14N,−14N). For each of the 11,684 cells read by the fixed continuation, the verifier solves its equality to **every** previous affine seed/read family. XOR of those exact eligibility intervals gives the complete checkpoint color, including all remote old writes.

The 33,568 nonempty intervals show that all relevant colors are constant for N ≥ 4. Exactly 514 cells have small-N exceptions, all confined to N=1,2,3. A literal replay from the independently reconstructed N=4 checkpoint therefore proves the same continuation for every N ≥ 4.

The first unmet wave request occurs after three additional periods and 854 further turns. It asks for a black cell that has never previously been read and is still white. This is a true finite-fuel endpoint, not an omitted interaction.

The final standard tail reads only normal coordinates x−y in [−86,−76]. Every initial cell and every read before the continuation has normal at least −72. Therefore the entire future tail can depend only on the continuation's finite XOR in its strip, which has 508 black cells. An exact infinite-ray checker verifies that tail; a remote flipped cell on each of its 22 active orbits is rejected as a countercontrol.

The small N cases are full original-seed simulations followed by the same exact all-future ray checks, not repeated-prefix heuristics.

### 3. Genuine backward standard ancestry

Reversal leaves the board unchanged and sends a pose (p,h) to (p−d_h, opposite(h)). Relative to the original head, the canonical 13-cell source's reversed ant starts at (1,0), facing east, and reaches a permanent southeast standard104 tail after 2,589 updates.

All other 171 initial cells have nonconstant affine offsets. Exact equations exclude them from every one of the 527 backward transient read cells and every infinite tail ray, for all integers N ≥ 1. Hence they are inert throughout the entire backward orbit. No added completion cells are needed.

## Files and reproduction

- `family_data.json`: all seed formulas, stage words and counts, continuation words, small exceptions and reverse-source data.
- `verify_prefix.py`: exact all-N initial-input and chronological-prefix proof, plus genuine inverse-ten and defect seam checks.
- `verify_capture.py`: exact all-N endpoint color partition, all small cases, standard tails and total defect counts.
- `verify_reverse.py`: canonical reverse replay and all-N remote-cell ownership proof.
- `common.py`: exact finite-board translating-tail checker.
- `verify_all.py`: runs all three verifiers.
- `*_result.json`: results from the packaged verifiers.
- `manifest.json`: SHA-256 hashes of the frozen package files.

Run `python verify_all.py` from this directory. Only Python's standard library is required; there is no network access, solver dependency or external data download. Successful execution checks every integer parameter through exact arithmetic, rather than enumerating a chosen range of N.

The package is a reproducible result about this explicit family. Its exact finite coordinates and complete words, rather than a visual resemblance or a conjectured routing principle, are the construction.
