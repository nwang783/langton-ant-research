# Final research status for 21 October 2026

## General conclusion

The finite-seed standard-highway conjecture is NOT solved by this continuation.
No counterexample was found or constructed. The strongest results below are
restricted analytic theorems and exact finite certificates with written
unbounded-parameter arguments. No priority or external-review claim is made.

## Completed results

| Result | Scope | Evidence |
| --- | --- | --- |
| Exact path hull | Every finite actual orbit segment | Analytic corner proof; 5,000 finite implementation controls |
| Future mass-width cost | Every later complete state after two positive one-sided clocks | Analytic inequality; 40,000 local exact clock controls |
| Quantitative retreat area | Every non-ETC finite-seed orbit, every orthant | Exact partial automaton and pigeonhole proof; 88,096 transition controls |
| Canonical one-bit recovery reconstruction | One toggle at any age/site of the stated canonical complete highway | 739 leaves, 104 unbounded-age guards, independent C++ and Python audits |
| Sixteen-cell square-corner capture | Exactly the family B(a,u,n) in the proof, all n>=1 | 14 affine guards for n>=34; 462 exact smaller cases; independent base audit |
| Four-scatterer circuit obstruction | Exactly the specified affine layout, every L>=128 | All-parameter first divergence at t=416L+37740; complete-field parity proof |
| Isolated last forbidden event exclusion | Finite black fields with a preceding legal ten-window | Exact language enumeration plus existing ten-factor attraction theorem |
| Five-block reduction | Future words with no adjacent forbidden ten-windows | Complete finite graph, exact marker coverage, independently checked ports |
| Arbitrary U/V fuel formula | Every finite or infinite aperiodic mixture of the two straight blocks | Exact first-read sets and four interface checks; required fuel 4+5a+2b |
| Endpoint-clock obstruction | Algebraic candidate states, not asserted reachable | Two black cells pass all critical one-sided and both diagonal radial clocks |
| Ordinary local-energy ansatz exclusion | Nonnegative C4-invariant 3x3 pattern weights plus 995 port constants | Exact 159-cut integer Farkas witness, independent row reconstruction |

ETC means eventual translating periodicity with nonzero drift. It does not
mean that the translating period is the standard 104 word. Keep this distinction.

## The core unresolved local lemma

Let H be the 34,712-state large cyclic component of the 150-window graph allowing
isolated forbidden ten-windows but no adjacent pair. Prove that every infinite
physically consistent path in H has infinitely many distinct first-read-L sites.

Physical consistency means that successive reads of the same cell alternate
L and R. First-read-L sites are the cells that must already be black when the
word begins. Finitely many such sites give a finite initial field realizing
the entire word; infinitely many rule out finite support.

Every infinite H path crosses the marker infinitely often, with gap at most 74.
Its marker gaps are the five exact blocks C,V,U,Q,B. The arbitrary U/V fuel
formula rules out a tail consisting only of U and V. Hence a surviving
finite-support H path must use C, Q, or B infinitely often. No proof excludes
that case. Full 149-turn-history compatibility still leaves a 974-state cyclic
component after 45 impossible macro edges are removed.

Closing H would establish that finitely many adjacent forbidden-event pairs
imply standard capture. The full conjecture separately requires proving that
such adjacent pairs are finite for every finite seed. No claim here closes
that global step.

## Local energy search is finished for this continuation

The ordinary nonnegative quarter-rotation-invariant 3x3 rank is exactly
excluded for any nonzero nonnegative cost assigned by macro type. The same
integer certificate applies to all-block, turning-block-only, and J-only
costs. It has positive multiplier weight on every block type.

The checkerboard-sector J-only rank has a numerical infeasibility report on
6,268 cuts. Adding nine arbitrary signed coefficients for the radius 1 head
neighborhood has a numerical infeasibility report on 7,821 cuts. No exact
Farkas witness was produced for those two larger ansatzes. The earlier
sector/all-block search was interrupted without convergence; that is not an
infeasibility claim. These statuses are retained in global_structure/.

The exact ordinary witness does not transfer to sector weights: 104 of its
271 sector aggregates are negative. Do not reuse it to claim sector
impossibility. No valid decreasing rank was found in this continuation.

## Important limits and rejected shortcuts

- The endpoint two-cell family is NOT a reachable ant orbit. It only shows
  insufficiency of the tested necessary inequalities against one blank source.
- A large clock value does not by itself force large black mass. Width can
  pay for it, and two-cell candidates pass all the radial endpoint tests.
- The complete fields are retained. No old scar is deleted because it seems
  inactive in an unperturbed highway.
- One-bit recovery does not close under a second error. The first recovery
  can leave a complete field outside the canonical source family.
- The sixteen-cell corner theorem is not a theorem about all sixteen-cell seeds.
- The all-L circuit theorem proves a prescribed return word fails. It proves
  neither escape for every L nor the impossibility of all renewable circuits.
- Finite cycle enumeration through 12 blocks is not a proof about longer
  periods or aperiodic paths. Fuel searches with caps remain exploratory.
- The recurrence half-plane proof restates prior work already noted in the
  source bundle. It is not counted as a new conjecture-solving result.

## Reproducibility and sources

The README gives command lines. MANIFEST.json records archive-entry SHA-256
hashes. Exact certificates can be verified without rerunning exploratory LP
searches. The principal period certifier checks all possible initial-field
hits and self-write thresholds on every infinite phase ray.

The source repository was inspected at commit
22e0c9edcc566a4c2f7a9bf92f5cd05c19199617. The 739-case artifact in this archive
is newly reconstructed from its source thresholds and model. It is not the
missing original file; earlier certified recovery boundaries explain its
lower total replay count and radius. See one_bit_reconstruction.md.

The Word report contains the main statements, proof outlines, and references.
The proofs and exact data in this archive provide the complete reproducible
research record. No process is represented as continuing after this handoff.
