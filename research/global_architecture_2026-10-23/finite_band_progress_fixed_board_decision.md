# Finite-band periodic inputs under strict progress: fixed-board decidability

23 October2026. Analytic extension, submitted for independent review. No
implementation, unknown-cap decider, or global ant decision claim.

## 1. Fixed supplied instance

Use the finite literal palette, common heading and strict-progress functional
from `positive_progress_palette_decision.md`. In particular every block has
ell(d_sigma)>=delta>0, and any two reads of the same cell occur at most
K=floor((max_E ell-min_E ell)/delta) blocks apart.

Supply a NONZERO translation period W and a prepared input T invariant under
translation by W. Its black support lies in finitely many transverse levels:
if nu is a primitive integer normal to W, T is white outside

    A<=nu(q)<=B.

The input is given by its finite table of full-W classes at those levels.
At a fixed transverse level there are gcd(|W_x|,|W_y|) longitudinal residue
classes. Several parallel standard rails are examples of this input form.

Fix ONE SPECIFIED finite set C of initial XOR flips relative to T. The question
is whether the actual ant on this board admits an infinite supplied-palette
decomposition. Existence over an UNKNOWN unbounded finite cap is expressly
outside the decision theorem here.

## 2. Exact recent history and a single unbounded coordinate

After the specified finite cap has passed the strict-progress bound, its cells
are never read again. Their earlier effects remain in the exact last-K-block
colored history. The state consists of:

- the exact transverse head level c=nu(p);
- its finite longitudinal residue modulo W;
- last at most K block labels and CURRENT colors on their reconstructed read
  supports, relative to the head.

All but c have finitely many possibilities. A full-W head class and the colored
history determine every future transition: old forgotten reads cannot recur,
and fresh input colors are given by the supplied finite-band profile.
Retired debris is left on the board, not reset.

## 3. Every infinite execution has an ultimately periodic macro witness

Take any infinite legal palette decomposition after the cap has passed.

If c_n visits a bounded interval infinitely often, the exact finite residue/
colored-history state at one exact transverse level repeats. The intervening
finite block segment is a cycle of this exact state model. Repeating it gives
a genuine infinite continuation on the SAME specified board, translated by a
period of T. Its drift is nonzero because ell strictly increases in each block.

Otherwise |c_n| tends to infinity. Block transverse increments are uniformly
bounded, so its sign is eventually constant. The head and every phase read
therefore eventually stay on one white side of the expanded input band.

Suppose c_n tends to positive infinity; the other case is symmetric. Among the
finitely many colored-history types choose two occurrences i<j of one type
with c_j>c_i, both after every phase read stays beyond the black band. This is
possible because some history type occurs at unbounded transverse levels.
The segment i..j lies entirely on the white side. Repeating that segment
translates each next copy farther outward, so every copy also has white input.
Its identical colored histories and geometric retirement make it a genuine
periodic continuation on the SAME specified board. Choosing an arbitrary
white-memory cycle without the outward drift condition would be insufficient.

Thus in both cases an existing infinite decomposition implies a finite prefix
followed by an endlessly repeated finite block segment. Deterministic ant
dynamics then forces the actual PHYSICAL trace to equal that continuation.
The original macro parsing itself need not be periodic.

## 4. Exact periodic-witness checking is effective

For a proposed finite macro prefix U and nonempty macro period V, concatenate
their literal words. Simulate U exactly against T plus the specified finite
cap. It leaves T plus finitely many color changes, with all other debris still
present. The literal V restores heading and has a nonzero drift d_V.

Group V's finitely many phase reads by full-d_V orbit. For each orbit, the
complete visit order at cell r+z*d_V is the order of the finite affine times

    |V|*z + i - |V|*k_i,

subject to z-k_i>=0. These finite threshold conditions determine when each
phase becomes eligible. Beyond their maximum, the complete ordered history
is fixed; successive required turns must alternate, and its first required
initial color is fixed. The finitely many exceptional cells are explicit.

If nu(d_V)!=0, every phase's proposed initial cells cross the prepared black
band only finitely many times. All such indices, and all finite cap indices,
are computable. Beyond them the initial input is white.

If nu(d_V)=0, the drift is parallel to W. At each fixed normal level the
prepared input is periodic along the primitive direction of W, with a
computable common period. Finite cap changes are isolated exceptions. Check
that common period after all visit-eligibility thresholds, as well as the
finite transient.

Consequently legality of U V^infinity on this FIXED supplied board is decided
by finitely many exact chronological/color checks. No tail is accepted from
a sampled finite run.

## 5. Two terminating semidecisions give the decision procedure

YES: enumerate all finite supplied-palette prefixes U and nonempty periods V;
apply Section4's exact infinite-witness test. Section3 proves this search
succeeds whenever an infinite decomposition exists.

NO: breadth-first enumerate the actual legal finite palette-prefix tree on the
SPECIFIED board. Each node has at most |Sigma| children. If no infinite path
exists, the finitely branching tree has finite height by the elementary
infinite-path lemma, so eventually an entire level is empty.

Dovetail the two procedures. Exactly one succeeds. This is a decision proof,
not an efficiency bound or an implemented one-counter compiler.

## 6. The unknown-cap quantifier is not solved by this argument

The NO search above cannot be applied to an existential union over all finite
caps: every finite controlled prefix may need a different, growing cap. The
resulting infinite controlled branch need not correspond to ANY one finite
initial cap.

The signed prepared108 family is a concrete control. On white input,
P108^n has a legal canonical seed with11n+13 black cells for every n. The
infinite P108 word needs11 initial-black orbit classes per new period and
therefore cannot be realized by any finite white-board cap. Arbitrarily deep
finite-cap prefixes do not imply an infinite finite-cap realization.

A separate effective one-counter reachability argument might extend the
unknown-cap decision, but it is NOT supplied or assumed here. The earlier
finite-graph controlled-input proof applies to fully2D-periodic input or the
common-D architecture, not automatically to this unbounded transverse model.

## 7. Provenance and strategic limit

The positive-progress/finite-white-input mechanism is attributed to retained
stale-memory work. Section4 is the same complete full-drift chronology idea
already retained for supplied periodic words, now with an explicit finite-band
input-period distinction. The new indexed combination here is the exact
FIXED-board survival decision for this prepared-input architecture.

A global finite-seed trajectory is not known to admit any such strict-progress
finite palette. This theorem neither removes that eventual-representation
quantifier nor classifies the resulting translator as standard104.
