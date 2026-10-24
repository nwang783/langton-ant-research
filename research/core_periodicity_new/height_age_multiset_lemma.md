# Current high-height residual age multisets

This is a mathematical overapproximation for the remaining unfunded DCUV record
cases, not a confinement theorem. It uses signed residual geometry, global
high-initial whitening and the signed all-input C-age rules in audit JO.

After whitening, every initial residual identity has height at most F. At each
selected integer height z>F, let x_j be the CURRENT number of residual identities
whose saturated age is at least j, j=0,...,4. Thus x0>=...>=x4>=0, and initially
all these coordinates are zero. Unselected heights are supplied without limit.
No producer-role, transverse-coordinate or literal spatial compatibility is
required, so physical words map into this relaxation.

If a packet contains c C macros, its surviving identities age by c (saturating at
4), and each output identity has age c. Let I_j be the number of its consumed
inputs at this height with signed minimum age at least j, and O its output count
at this height. An after-state cover requirement is another ordered vector t.
Define t_k=0 for k>4. Its exact minimal predecessor requirement is

p0 = I0 + max(0,t0-O,t_(c+1));
pj = Ij + t_(j+c), j=1,...,4.

Here c is in 0,...,4; actual recurrent-eight packets have c<=2. These formulas
are applied independently at every retained height.

Proof. A tail requirement t is equivalent to a multiset of obligations, with
(t_j-t_(j+1)) obligations of minimum age j. Fixed new age-c outputs should satisfy
the hardest obligations among those of minimum age<=c. After removing up to O
such obligations, exactly max(0,t0-O,t_(c+1)) obligations remain; every threshold
j>c still has t_j remaining obligations. Pulling those thresholds backward over
aging gives a survivor requirement with these tail counts: d0 as above, and
dj=t_(j+c) for j>=1. The required consumed inputs and the surviving obligations
are disjoint. Their union has tails I+d. A source multiset admits such a partition
if and only if it dominates those tails, by the elementary nested-threshold
matching criterion (match hardest obligations first to youngest eligible tokens).
This proves both directions and uniqueness of the minimal predecessor in the
ordered-tail domain. In particular a historical age-height maximum cannot stand
in for a token already consumed.

Backward coverability therefore needs no guessed token-count bound and no
matching disjunctions. Upward-closed sets have finite minimal antichains by
Dickson's lemma, restricted to the ordered-tail domain. The monotone finite-control
iteration terminates in principle. Its implementation may hit a stated discovery
resource cap; such a cap is not a no-hit certificate. An exhausted basis can be
independently verified by goal inclusion, predecessor closure and exclusion of
every zero initial marking.

Implementation: build_record_height_age_petri.py and
record_height_age_petri_backward.cpp. The builder checks its age-zero input counts
and output counts against every transition of the existing height-count model.
The 40,000 controls in check_height_age_preimage_controls.py independently enumerate
every consumed submultiset of each randomly chosen source and compare the claimed
predecessor against literal age shifts and output insertion. This is an engine
control, not a final independent audit.
