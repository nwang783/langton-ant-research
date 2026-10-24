# Private-cell and outward-record fuel for geometric inflations

Status: independently audited analytic proof, complete image inventories,
finite-prefix trees and ownership checks, 22 October 2026. These are no-finite-seed obstructions, not
claims that all ant paths are self-similar.

Assume an ant trace satisfies p(k*n)=a*p(n), h(k*n)=h(n), with p(0)=0,h(0)=N,
Gaussian a of magnitude>1. A coarse R/L step chooses an arbitrary eligible
k-turn image with endpoint displacement a/-a and matching final heading.
Choices may depend on unlimited history. Let U_R,U_L contain EVERY eligible
internally alternating-valid image, not merely selected candidates.

For a macro entering north at coarse cell0, a fine read offset z can be read
by another macro only if

    z = a*q + Rot_h(o),

where o is a read offset of some image in U_R union U_L, q is a Gaussian
integer coarse center, and q_x+q_y+h is even (the normalized pose sector).
The set of possible q is finite and computed exactly: enumerate all image
phase offsets and four headings, divide z-Rot_h(o) by a, and retain precisely
the integral, sector-compatible quotients. This overapproximates every actual
prior macro; it makes no claim that all listed owners can coexist physically.

Translation and quarter-rotation covariance reduce every current entry pose
to this north-facing calculation. In particular rotating the physical offset
also rotates q, and the parity of q_x+q_y is unchanged modulo2.

## 1. Private first-L criterion

Suppose every image in U_R has a cell whose FIRST read within that image is L
and whose owner set is exactly {0}. At a coarse cell whose FIRST VISIT is R,
that selected fine cell has not been read by any earlier macro. It is therefore
a first-L read of the actual fine ant and must be initially black.

Distinct first-R coarse cells give distinct such black cells, because a private
cell cannot belong to two different coarse centers. If the initial board has
m black cells, at most m coarse cells can first be read R. At most m coarse
cells can first be read L as well. Thus the whole coarse trace visits at most
2m distinct cells, contradicting finite-domain escape (or the expanding
positions p(k^j)=a^j p(1)).

The trigger is a cell whose FIRST VISIT is R, not its first R visit after a
possible earlier L. This distinction is essential.

## 2. Forward-half-plane criterion

Private ownership is stronger than necessary. It suffices that every R image
has a locally first-L offset all of whose owners q satisfy q_y>=0.

Consider a strict new outer coordinate record of the coarse path: a first
visit beyond the old maximum or minimum of one fixed axis. The head enters
in the outward direction. Rotate that direction to N. Every earlier coarse
center then has relative y<0, including every center on the old boundary.
Hence none can own the chosen fine L cell. That fine cell is globally fresh
and must be initially black.

A record cell is also a genuinely first-visited coarse cell. There are at most
m record L reads and at most m record R reads, the latter charged to distinct
fine initial-black cells because each charged read is globally first. Thus
at most2m outward coordinate records can occur. Equivalently, the sum of the
four axis extrema from the initial position stays bounded by2m. The trace is
confined to a finite rectangle, again impossible.

One may instead select a single unbounded axis direction and use infinitely
many records there; the finite counting argument avoids any assumption of
monotone escape or bounded retreat. No internal finite-state controller is
assumed.

## 3. Exact closure at k7

At a=2+3i the complete images are:

 R: RLRLLRR, RLLRRLR, LRRLRLR;
 L: RRRLRLR, LLRLLRR, LLLRRLR.

The three R images have respective PRIVATE first-L offsets
(2,1),(1,1),(0,0). Gaussian division of all6 images times7 phases times4
headings proves each owner set is exactly {(0,0)}.

The other13 possible expanding k7 scales are already excluded by the
occurrence-wise nonincreasing mass inequality or by complete finite
alternation-prefix exhaustion (at most17 feasible prefix nodes and5 macros).
Therefore NO finite-seed pure heading-preserving inflation exists for k7.
Independent records: audits/check_arbitrary_inflation_small_independent.py and JSON;
computability/front_record_inflation_obstruction.py and
front_record_ownership_independent_comparison.json.
Together with the audited k<=6 result and even-k heading parity, this excludes
all temporal scales2<=k<=8 without a finite-state hypothesis.

## 4. Scoped k9 reduction

The complete k9 geometry yields23 possible expanding scales. Nonincreasing
mass and complete finite-prefix exhaustion exclude18. The unresolved five
scales from naive branching are then tested by the ownership criterion:

 a=1+4i,3-2i,3+2i: forward-half-plane fuel passes;
 a=3+4i: even private fuel passes;
 a=3: neither ownership test passes.

Thus any finite-seed
pure inflation with2<=k<=9 would have to use exactly k9 and a=3.
This is a necessary reduction, NOT existence or an exclusion at that last
scale. In particular the unresolved R-image RRLRRRRLR is A+R, where
A=RRLRRRRL is the known rail-building sweep; its only first-L input has
possible owners behind the new frontier. The tempting universal freshness
claim is therefore not available there.

Files: `check_private_macro_fuel.py`, `private_macro_fuel.json`, and the
complete per-scale image lists and bounded-tree records in
`free_inflations_k7.json`, `free_inflations_k9.json`. NODE_CAP results are used
only to identify what needed a different proof; they are never exclusions.
The k7 constraint solver's SAT finite refinement is likewise only a control:
its unrestricted initial black requirements grow and do not contradict the
new finite-fuel theorem.
