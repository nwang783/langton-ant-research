# A finite record-clock window forces a translating future

24 October 2026. Author theorem and constructive finite-cover procedure; independent audit pending. The theorem proves translation, NOT canonical104 uniqueness. No unbounded certificate enumeration is executed in this package.

## 1. Statement

There is a total computable function F on positive integers with the following property.

Take ANY complete finite-seed classical ant orbit and ANY pristine strict record of the augmented initial-black-plus-head rectangle. Start the clock at that record. If, through the next F(H) updates, every H-step block contains another strict expansion of the running rectangle in at least one of the four directions, then the entire subsequent ant trajectory is eventually translating periodic in turns and head poses.

All black archive remains physically present. Translation does not mean equality of the complete finite black boards, whose permanent output may grow. No bound or classification of the eventual period is asserted.

F(H) is given by an effective terminating search for a finite cover by exact outward-translating certificates. The proof of termination is uniform and does not assume finite-seed attraction. No useful numerical estimate for F(H) is presently supplied; the search is not run for H>=2. The vacuous small case F(1)=3 is independently reducible to a125-class finite prefix test in the included checker. Explicit canonical examples show that the infinite bounded-clock class is nonempty at H=104, so the general theorem is not merely a vacuous clock obstruction.

## 2. Compact decorated record states

Rotate the incoming record normal to N. The head is at0, heading N. Decorate the COMPLETE initial field B with its old rectangle offsets

    M_N=0, M_E,M_S,M_W in N_0 union {infinity}.

Let R(M) be the generalized rectangle given by a·q<=M_a for every finite offset. Require B to be contained in R(M), and require EVERY cell with y>=0 to be initially WHITE. The latter is the genuine pristine north-record condition, including its entire boundary line. Infinite old support is allowed.

The space of binary fields has its product topology. Give N_0 union {infinity} the one-point compactification topology: each finite value is isolated and neighborhoods of infinity contain all sufficiently large integers. The product of these spaces is compact. The support constraints are closed: for each cell q, the forbidden condition BLACK at q outside one of the stated sides is an open finite condition. The record-line white condition is also closed. Thus the decorated state space X is compact.

These decorations may contain extra unused white space and need not arise from an actual history. Proving the result for this larger space avoids an unproved causal reachability assumption.

Run the ant and update every finite side maximum by the visited head positions. An initially infinite side stays infinite and never produces a record. Cut0 is the designated starting record event. For T>=0 define E_(H,T) by

    for every integer u>=0 with u+H<=T,
    some union-record event occurs at a cut in (u,u+H].

This includes all endpoint gaps that can be tested by time T. It is a clopen condition. A length-T trajectory reads only the radius-T square, and each side offset need only be distinguished as0,...,T or>T. The E_(H,T) decrease with T. Their intersection K_H is the compact class having a union event within EVERY future H-step block.

## 3. The old-rectangle argument survives infinite limits

The signed finite endpoint lemma extends verbatim to generalized rectangles. Only normals with finite offsets can occur in its last-record ordering. For any endpoint q in the earlier generalized rectangle, its finite normal maxima still satisfy M_a(s)>=a·q. Therefore, under the infinite H-clock,

    p_t is outside R_s for every t>s+G(H),
    G(H)=H(H+1)^4.

An infinite offset is never subtracted from another infinity; it is simply absent from the finite list of occurring record normals. This is the necessary justification for applying the argument in the compactified space.

In particular no initial BLACK cell is read after G(H), because all initial BLACK lies in R_0. Only finitely many initial BLACK sites are ever read. Delete all other initial BLACK sites once: deterministic first-difference coupling gives a finite board with EXACTLY the same whole future, even if the original B had infinite support.

Every consumed R lifetime has age at most G(H), by applying the same endpoint lemma at its birth. After the finite initial cohort has retired, the entire future-relevant field is therefore confined to a head-centered radius G(H). Exact pruning recurrence gives a periodic future turn word with a nonzero translation drift d. There are infinitely many union records, so zero drift is impossible.

At least one side that was FINITE at time0 has a·d>0. Otherwise the periodic tail would be bounded in every initially finite normal, and no infinite record stream would remain. This is stronger than merely proving some translation on the infinite limit: the translation actually leaves one of the specified finite old sides.

## 4. Why those translating futures form an open basin

Let a decorated state X have a finite-prefix/periodic translating future with a·d>0 for an initially finite side M_a=M. Its entire future read footprint in the old half-plane a·q<=M is FINITE. Indeed each tail phase q_i+kd enters that half-plane only for finitely many k>=0, and the prefix has finitely many reads.

Fix this FINITE side offset exactly at M, and fix the initial colors on that finite old-half-plane footprint. This is a finite clopen cylinder in the decorated space. Every other state in that cylinder has the same complete future:

- all reads in the old half-plane have the specified initial color and identical earlier flips;
- all reads outside it are initially WHITE, because the fixed finite side bounds the full initial support;
- arbitrary initial archive at every other unread site is retained.

Fixing the side offset is essential. Letting it grow would permit extra BLACK input on a formerly white outward ray. Other side offsets may vary, including to infinity; any newly allowed old-half-plane read site has already been included in the finite footprint.

Let O be the union of all such outward-translating forcing cylinders. Then O is open, and Section3 proves K_H subset O. No canonical word is assumed in defining O.

## 5. Compactness gives a finite window

If E_(H,T) were not contained in O for every T, the nonempty compact sets

    E_(H,T) intersect (X minus O)

would be nested. Their intersection would contain a point of K_H outside O, contradicting Section3. Hence for some finite T,

    E_(H,T) subset O.

Every actual normalized record state belongs to X, so this proves the finite-window statement non-effectively. The next section gives a total computable selection of such a T; it does not merely appeal to a non-effective maximum over unknown finite orbits.

## 6. Effective enumeration and decidable finite coverage

### Enumerate verified outward cylinders

Enumerate finite black boards K, finite prefix words u, nonempty period words w, a side a and a finite offset M. Require K to lie in a·q<=M. Check the literal finite prefix from head0,N. Require that the period restores the heading, has nonzero drift d, and a·d>0.

Validity of the entire repeated period is DECIDABLE, for an arbitrary word w, not only104. If Q_i are its phase reads and C the complete finite field after u, then at phase i in period k the read color is

    1_(Q_i+kd in C) XOR parity of all earlier phase-ray coincidences.

Each initial C hit occurs at at most one nonnegative integer k. Each earlier-phase contribution turns on at one nonnegative integer threshold, obtained by exact integer divisibility along d. Testing0, all thresholds, every initial-hit index and its successor checks every constant-parity interval, including the final infinite one. This is a finite exact calculation, not observation of repeated blocks.

For each valid candidate, compute the finite old-half-plane footprint and emit the cylinder from Section4. Invalid or empty cylinders are harmlessly rejected. These cylinders cover every member of K_H: Section3 supplies a finite comparison board with the same future, and its finite prefix/period, finite outward side and offset eventually appear in this enumeration. No total finite-seed capture procedure is assumed.

### Decide whether finitely many cylinders cover E_(H,T)

Given T and a finite list of cylinders, choose an integer cutoff L containing:

- T;
- every fixed side value appearing in those cylinders;
- every absolute coordinate of a cell they inspect.

Partition each free side offset into0,1,...,L and the single unbounded class>L, which includes infinity. For the last class, no coordinate or finite equality inspected by this test can distinguish its members. Partition field colors on the finite union of the radius-T square and the cylinder cell sets. Reject assignments violating the pristine line or the support inequalities.

Every surviving finite assignment extends to a decorated state: choose suitable side values in their classes and make all unassigned cells WHITE. Conversely every decorated state lies in one such class. Simulate each finite assignment through T and test the block condition and cylinder membership. It is therefore decidable whether E_(H,T) is contained in the given finite cylinder union.

The included implementation performs this same finite decision by online first-read branching and Boolean cofactoring of unassigned guard bits, avoiding unnecessary enumeration. It is still finite and exact. It does not use an oracle for forever-unread cells.

### The total search

Dovetail all finite T and finite initial portions of the certificate-candidate enumeration. For each pair, decide the finite-cover inclusion above. Output the first T for which inclusion holds, optionally replacing it by max(T,H).

Section5 gives an E_(H,T) contained in O. That compact E_(H,T) has a FINITE subcover by emitted cylinders. Its certificates and T all appear at a finite stage. Thus the search terminates for every H>=1. This defines a total computable F(H).

The unbounded search is NOT launched in this research package. Only small bounded basis tests and exact known certificate regressions are run. The result concerns computability in principle, not practical complexity.

## 7. Uniformly recurring droughts in a hypothetical nontranslating orbit

A nontranslating finite orbit fails the finite clock test from EVERY pristine augmented-hull record. Therefore, for every H, its next F(H) updates contain an H-step block with no record event.

More generally, start from ANY cut v. Either (v,v+H] already has no event, or it contains a record s. Apply the preceding conclusion at s. Hence EVERY interval of length F(H)+H contains an H-step record-free subinterval.

This is stronger than merely finding arbitrarily late droughts. For each chosen drought length H, the gaps between opportunities for such droughts have a universal finite bound. It does not force zero average expansion speed, does not prohibit all nonperiodic dynamics, and does not prove an outward record clock window actually occurs in every finite orbit. A noncanonical translating counterexample, if one exists, is outside this nontranslation conclusion and still requires separate controller classification.

## 8. Countercontrols and bounded verification

The signed MT all-n drought is compatible with the theorem: its exact58697+104n quiet interval fails a fixed H-clock long before the actual eventual outward tail. Different finite seeds do not provide a single orbit avoiding all finite forcing windows forever. The prepared20/16-cell families likewise do not contradict a statement using the augmented full-seed hull.

The finite-basis checker exhausts all125 side-offset classes for H=1,T=3 and finds no surviving clock prefix, while H=1,T=2 is nonempty. A separate finite Boolean cover regression checks the support/offset logic. Two true canonical north-outward certificates are reconstructed with a generic arbitrary-period parity verifier; their generalized one-finite-side record clocks satisfy H=104, and deleting a required BLACK bit is rejected. These are regressions for the proof machinery, not a computation of F(104).

The clock uses the globally specified full initial seed to define its augmented hull. It is not a certificate based only on an observed turn prefix and a few inspected cells. Adding a remote pre-funded port can change that initial hull and invalidate the clock, even when the observed turn prefix is unchanged. Thus the retained four-cell exterior-completion/density controls are respected.

No practical value of F(H>=2), universal capture time, canonical uniqueness, or finite-seed noncapture decision procedure follows.
