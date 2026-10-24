# Bounded checkpoint charge, without per-image conservation

2026-10-23 02:54 UTC. Extension of signed Fourier bridge HN, submitted for audit.

## 1. The relevant hypothesis is an output sequence

Take a finite typed substitution, in particular the eight physical states
(h,turn), with nonempty finite image words. Images preserve their coarse
final heading and have one common Gaussian-unit displacement multiplier.
The images may have different lengths. Their individual signed charges
NEED NOT equal the parent turn sign.

Let c_s=+1 for an R state and -1 for an L state, and let M be the ordinary
image-incidence matrix. The signed charge of an r-fold refined root is

    E_r=(M^r c)_root.

Only the powers belonging to a genuine growing first-state root cycle are
actual proposed prefixes. As in the preceding adapter, take the lcm of that
cycle length and the Gaussian unit's order and treat each genuine phase
separately.

If these scalar charge sequences are bounded, any finite-seed realization
has uniformly bounded black mass at its refining checkpoints:

    |B_after|=|B_initial|+E_r.

Its signed occupation polynomial still equals final-minus-initial black
indicators. Hence

    ||F_r||_1 <= 2|B_initial|+E_r
              <= 2|B_initial|+sup_r E_r.

The full bounded-Fourier theorem HN therefore applies unchanged. Exact
per-image charge conservation was one sufficient way to obtain bounded E_r,
not a necessary premise. A state-potential coboundary is another sufficient
way; no supplied coboundary is required when the incidence recurrence itself
is checked exactly.

At the trivial character X=Y=1 the same transfer already computes E_r.
Consequently boundedness of the required output sequences is decidable by
HN's minimal integer-recurrence criterion. It is unnecessary and would be
incorrect to require the entire incidence matrix to be power-bounded: it
always has growing length modes which may be invisible to signed charge.

## 2. Implementation and exact phase ownership

bounded_charge_state_transfer.py is a separate adapter, leaving the original
signed exact-charge implementation unchanged. It accepts eight independent
base-turn image strings in state order N-R,N-L,E-R,E-L,S-R,S-L,W-R,W-L.
It verifies geometry, derives the selected first-state cycle, rejects a
nongrowing root, and groups the unit/root periods. It does NOT impose a
per-image charge equation.

checkpoint_charge_certificate computes the exact trivial-character output
recurrences. bounded_fuel_character first requires those outputs to be bounded
and only then applies the strong bounded-output Fourier test. An unbounded
charge answer is NO BOUNDED-CHECKPOINT-CHARGE CERTIFICATE, not an automatic
finite-support exclusion. The separate positive_test uses the one-sided
lower-bound theorem HO and also permits these nonconservative images.

The caller may apply character_test algebraically without the charge check,
but its unbounded answer alone then does NOT imply finite-support failure.
It must be compared with an independently justified mass-growth ceiling.

## 3. Broader polynomial-growth version

The same argument has a useful analytic extension. If the genuine checkpoint
charge outputs satisfy E_r=O(r^d), d>=0, then finite support forces EVERY
unit-torus output to be O(r^d). Integer scalar recurrence outputs have this
bound precisely when their nonzero minimal factors are cyclotomic and each
has multiplicity at most d+1; a zero-root factor is harmless transient data.
The conjugate-basis justification is exactly HN's.

Unit geometry confines each refined image to radius O(r), so ant legality on
ANY initial background independently gives the weaker universal O(r^2)
ceiling for signed occupation. A noncyclotomic output or a cyclotomic Jordan
multiplicity exceeding three therefore contradicts arbitrary-background
legality. Multiplicity between d+2 and three can instead be a specifically
finite-support obstruction when d<2.

These statements do not decide arbitrary recurrence positivity, do not prove
bounded charge for arbitrary controllers, and do not certify a model when
all tested characters pass. The current wrapper implements the bounded d=0
case; the polynomial d>0 extension is a mathematical criterion only.

## 4. Nontrivial bounded-charge controls

The identity/five-step alphabet supplies genuine non-exact-charge controls.
Its right images RLLLL and LLLLR have charge-3, while its left images LRRRR
and RRRRL have charge+3. The countermodel analysis's rank-two incidence reduction
identifies balanced selections with one or two active states of each turn.
Their root charges stabilize or alternate, rather than being constant.

check_five_charge_controllers.py independently checks the incidence formula,
literal geometric transfer and exact output recurrences for this bounded
class. Its character results are necessary-test controls. Any surviving
Fourier candidate remains unvalidated, and this note does not claim a new
construction-family exclusion before those complete results and their audit.
