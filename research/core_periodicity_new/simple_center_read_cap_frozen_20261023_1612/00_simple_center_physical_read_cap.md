# Simple atomic center paths read a physical cell at most 104 times

## Independent geometric statement

Take any finite actual raw path partitioned into atomic D, V, U, and C words.
Use corrected center head + rotation(−1/2, −1/2), and replace each atom by its
straight corrected-center chord. If this polygonal path is injective as a
function of path time, then every fixed physical cell has at most 104 reads
in the atomic raw path.

The statement uses only the literal atomic footprints and center injectivity.
It makes no independent assertion that ant histories have injective centers.
It is therefore separate from any pending language-specific simplicity theorem.

A following actual M11 can add at most two reads of a fixed cell, so raw plus
that marker has the bound 106. An infinite simple-center path has the same
104 bound, because it holds for every finite prefix.

## Proof

Fix the physical cell at q = (0, 0) by translation. If an atom of type a and
heading h reads q at local offset z, its head is −rotation_h(z). Its doubled
entry center relative to q is therefore

    rotation_h((−1, −1) − 2z).

For each of the four literal atomic words, enumerate its exact local raw read
trace and the multiplicity m_a(z) at each local cell. Rotate by all four
headings and group the possibilities by this doubled center.

There are exactly 60 possible entry centers. Their maximum possible raw read
multiplicities are one at 28 centers, two at 20 centers, and three at 12
centers. Since a simple polygonal path cannot have two distinct atomic entry
times at the same center, at most one atom contributes at each center. Thus

    reads(q) <= 28 + 2*20 + 3*12 = 104.

Two consecutive atoms share a single exit/entry path parameter, not two
visits. We count each atom's ENTRY once, so this ordinary continuity causes
no double-counting issue. The final atomic endpoint carries no raw read in
this convention.

The M11 footprint has eleven reads with maximum multiplicity two at any
local cell, giving the terminal-marker addition independently of its pose.

## Exact finite certificate and limits

The checker reconstructs the atomic raw words D, V, U from the signed literal
geometry and C from the suffix of DC after D. Their lengths are respectively
10, 18, 28, and 15. It traces every fine read and endpoint, then records all
local possibilities at each of the 60 entry centers and the exact maximum.

The sum 104 is a conservative independent maximum for each center. No claim
is made that all 60 maximizing choices coexist in one literal path, or that
104 is the optimal attainable visit cap. The numerical agreement with the
standard highway period has no role in the proof.

This is a physical read count, not a residual-identity lifetime or a count of
marked-pose visits. It supplies no global capture, period, branching budget,
first-discovery root expenditure, or finite-duration conclusion by itself.
