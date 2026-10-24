# Six-row right-cap polarity obstruction

Status: all-width/all-length analytic proof; independent analytic audit passed
22 October 2026.
This excludes a renewable fixed right cap, or any periodic or aperiodic chain
of right caps, ALL of whose reads lie in the SAME strip -1<=y<=4 relative to
their root poses. The roots advance by(0,4). The complete isolated W20/S arm
histories are those in `mixed_shuttle_architecture.md`.
No claim is made for a different six-row placement, variable-height phases,
or caps that read below-1 or above4. Complete isolated half-arm histories are
essential: this does not cover width-growing caps that reach and interact
with the remote opposite endpoint.

The key is a polarity mismatch of the FIRST black upper-input bit, not black
mass and not the previously conjectured lower-neighbor condition.

## 1. Necessary input polarity

Use headings N=0,E=1,S=2,W=3. At every mature cap entry(0,0,E), the input is:
- row0 negative x black; row-1 negative x white;
- positive/nonnegative finite words A_x at row-1, B_x at row0;
- rows1 through4 white.
This is the exact entry field previously derived in
`two_row_transfer_interface.md`. Let s be the least nonnegative x with B_x=1,
if one exists. A cap that returns to its entry pose without reading below-1
must have s EVEN.

Proof. Before the first B site, the only possible eastward progress consists
of S=RLLR packets. A packet starts at(2k,0,E) on a white B cell, reads the two
lower A bits black, then a white odd B cell, and arrives at(2k+2,0,E). It
writes the two B cells black and erases the two A cells.

If an even A cell in this process is white, the forced RR lower reflection
starts a westward(LLRR)^infinity sweep: every upper bit ahead is black,
every lower bit ahead white, including the pristine negative half-rail. If
an odd A cell is white, the next move enters row-2 and invalidates the cap.
Neither case returns to(0,0,E).

If the first B site is s=2k+1 odd, and no earlier A gap stopped the process,
it is reached at(s,0,N), after S^k RLL. Its black L starts exactly the same
westward(LLRR)^infinity sweep on the written/erased rail. In particular the
ant crosses x=0 only with N or W heading on row0, never with the entry E
heading. Thus an odd first B precludes a return.

If B is empty, finite support of A supplies a first missing A bit and one of
the preceding failures. Therefore an empty B also precludes a usable cap.
This proves the necessary condition: a nonempty B with least black index
even. It is not asserted sufficient.

## 2. Necessary output polarity

The top row y=4 starts entirely white. Since the pose sector is
x+y+h=1 mod2, every complete reflection at that row is one of:

- RR: create black bits at(2k+1,4),(2k+2,4), both previously white;
- LL: erase black bits at(2k,4),(2k+1,4), both previously black.

No other passage is possible without reading above4: the cap enters row4
from below with N heading, takes one horizontal step, then must turn down.
Every such passage is completed because the cap finishes back at height0.

Starting from an all-white row, if any black bit exists, its LEAST coordinate
is odd. Moreover this least bit can never be erased while it remains least:
an LL erasure of an odd bit requires its even left neighbor black. A new RR
pair can move the least bit left to another odd coordinate, never right or
away. Induction over the reflections proves this statement for every finite
cap, regardless of its width or the lower history.

A cap compatible with the next incoming S arm must leave row4 white for x<0.
Consequently its output B'_x=color(x,4), x>=0 is either empty or has least
black index ODD (necessarily>=1).

## 3. No two successive usable caps

After the outgoing W20 arm and the next incoming S arm, translated by4, the
next cap's upper input B is exactly this B'. No other region reads the
nonnegative cells of that row. The first lemma requires its least black
index even; the second gives odd or empty. Contradiction.

Thus the exact partial map T of the interface has T^2 nowhere defined.
This excludes fixed points, all finite cycles, and all infinite aperiodic
sequences of usable caps within the common strip. The outgoing guard is used
for the complete arm compatibility and the input/output identification;
there is no extrapolation from a bounded search.

## 4. Relation to the exploratory conjecture and negative controls

The earlier stronger conjecture that A'_s=0 at the first output B' bit is NOT
needed. It remains unproved, and its upper-strip relaxations have explicit
counterexamples. The polarity argument retains the actual lower scan from
the cap entry, which is precisely what arbitrary-port abstractions omitted.
Transfers may increase black mass, including8->12; the proof is not a fuel-
count assertion. The width10 controls are optional checks, not proof steps.
