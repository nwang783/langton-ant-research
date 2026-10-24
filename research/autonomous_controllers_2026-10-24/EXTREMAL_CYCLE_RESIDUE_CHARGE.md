# An extremal cycle cannot pay the signed wake residues

24 October 2026. Author proof, submitted for independent review.
This is a targeted restriction on the E-cycle subcase, not a classification
of all growth-eight fronts. No missing width-ten exhaustion is invoked.

Assume the COMPLETE WHITE translating-front hypotheses of
EXTREMAL_SINGLE_USE_EDGE_LEMMA.md (SHA 5648cb495d0dd7fdcc4c35caed84deea60b0d0dd0149aec77234b99565afc1fe),
now independently PASS in report 9b0906ab. Let d=(a,b), D=max(|a|,|b|),
and suppose the first-R-to-last-read graph E has a cycle C of length ell.
All its ell distinct full-drift cell classes are odd output classes.
Let O be the full odd wake and O'=O minus the vertices of C.

## Exact cancellation

At each C vertex its incoming and outgoing cycle edges have perpendicular
axes. Thus the vertical C edges are a perfect matching of C's vertices,
and the horizontal C edges are another perfect matching. This assertion
counts actual port/edge identities on the full-drift quotient, not an
undirected projection or a primitive-drift replacement.

Each vertical pair has opposite checker signs chi=(-1)^(x+y) and the
same x residue modulo |a| when a != 0. Therefore, for EVERY x residue,

    sum_{q in C, x(q)=r mod |a|} chi(q) = 0 EXACTLY.

Similarly horizontal pairing gives exact cancellation in every y residue
modulo |b| when b != 0. If a coordinate of d is zero, the corresponding
pairing also cancels on each individual physical column or row. Checker
sign is well-defined on full-drift classes because a+b is even.

The signed-residue theorem for an actual finite-support periodic front
requires the full odd wake's checker sum to equal 2 modulo four in each
residue of either nonzero drift component. Since C contributes zero,
O' satisfies ALL the same signed-residue conditions by itself. Hence

    |O'| >= 2D,
    g >= ell + 2D >= 4D.                               (1)

The second inequality uses ell>=2D for an essential checker cycle of
winding -1. This is an output charge, not addition of overlapping event
time bounds. No chronology or ant realizability is asserted for O' itself.
In particular O' need not be the wake of another physical controller.

## Growth-eight corollary

The independently signed unit-axis and retained unit-diagonal exclusions
imply D>=2 for any actual nonzero full drift. If g=8 and E has a cycle,
(1) forces D=2, ell=4, and |O'|=4. The only possible full drifts in the
D=2 box are (±2,±2). Thus:

* Every growth-eight front at full drift type (4,0), (4,2), (4,4),
  (3,1), or (3,3), with all genuine rotated/signed cases retained,
  MUST have acyclic E.
* The sole E-cycle subcase left at growth eight has full diagonal drift
  (±2,±2), one four-edge E circle, two singleton R classes, two A,A,-A
  RLR classes, and exactly four other odd output classes.

For this last case the four classes O' must be checker-pure: the signed
x and y residues modulo two each need two equal signs, and four classes
total force either the two diagonal parity bins or the two off-diagonal
parity bins, each with population two. This does not invoke the theorem
excluding checker-pure PHYSICAL wakes at full drift (2,-2): O' is not
known to be a physical wake. The full O remains checker-mixed.

E can be acyclic or empty, including at the remaining diagonal drift.
Neither (1) nor the corollary forces an E cycle. The unrestricted g>=12
claim and standard104 classification are NOT proved.

## Exact dependencies and evidence status

1. Single-use theorem above, independently signed report SHA256
   9b0906abf802ce84e3ed4175696461e2dd8e90714311226878012ae8ba9a8a55.
2. Signed residue proof: ../sources/kehao95-core/wake_synthesis/proof/
   periodic-growth-closure.md, Section 2.3. Attribution there to
   A. Jillhewar is preserved; no external novelty claim is made here.
3. ../periodic_classification_new/minimal_full_drift_corollary.md,
   using the signed axis_negative_drift_extreme_exclusion.md and the
   retained all-cap full unit-diagonal exclusion.

The historical growth-eight width-ten exclusion is not a dependency.
Its recovered evidence status is reconciled separately in
../audits/width10_growth8_evidence_reconciliation_20261024.md.
