# A transition-complete 331-layer causal frontier on retained U-entry histories

23 October2026,19:50 UTC. Author proof and exact all-role reconstruction;
independent review requested. This supplies a stronger frontier than deleting
identities merely because their294-C INPUT lifetime has expired. It handles
old black cells that could otherwise invalidate a candidate's WHITE guard.
The number of retained cells is finite but may grow; no finite-state or
stabilization theorem is asserted.

## 1. The key change: use the already actual source-to-CURRENT subarc

Fix an actual complete-eight history beginning U/UC/UCC, through a current
full boundary. Its corrected-center prefix is simple. Let a still-current
produced residual identity have source full-entry center A, source clock s,
and source output slot o. Let the current actual full-entry pose have center
B and clock j. Normalize the source head/heading to(0,0,N), and write c=(-1/2,-1/2).

For ANY candidate next packet b in the retained-eight alphabet, take ANY cell
v in its complete raw-plus-M11 context, including required WHITE cells and
core cells, not just residual inputs. If this candidate context cell were the
old produced cell, the CURRENT head p and relative heading h would satisfy

    p=o-rot_h(v),
    B-A=p+rot_h(c)-c.

These are the endpoints of an ALREADY ACTUAL simple subarc. Its C count is
j-s, regardless of whether candidate b is physically valid. Thus the signed
thin-chord bound applies without assuming the hypothetical next packet occurs.
This removes the circularity in input-age-only pruning.

## 2. Exact all-context horizon330

The retained eight complete contexts have186 cell slots in total, reconstructed
as first-read cells of each raw word followed by its actual M11. The source
outputs have68 slots. Across four current relative headings there are50,592
raw alignments and25,296 in the conserved sector. They give157 distinct center
displacements.

Exact thin-chord lattice-site enumeration gives

    max M(B-A)=80,
    max(4M+11)=331.

Only eight alignments attain the largest heading-rounded bound. Every one has

    B-A=(0,14), current relative headingS,
    p=(-1,13), candidate slot BEFORE color WHITE.

Since j-s is congruent2 modulo4 in these alignments, their age is at most330.
Every other alignment has a smaller rounded bound. Therefore:

**Current-context exclusion.** At any actual full boundary in this simple
history, a current produced identity whose full-source C age exceeds330 lies
outside the COMPLETE context of EVERY possible next retained-eight packet.
The candidate's validity and its required before color are irrelevant.

This theorem is stronger in a different direction than the294-C input lifetime:
identities of ages295..330 cannot be consumed by a valid future packet, but
keeping this small extra age band retains all possible old WHITE-guard blocks.
The proof uses actual source/current cursor history, not static root counts.

## 3. Untouched entry cells have a context horizon20R+271

Normalize the factor's initial head to(0,0,N). Suppose every entry residual
cell q has ||q||_infinity<=R. Include all remote unread entry debris in R.
If q lay in any candidate context slot v at current heading h, then

    B-A=q+rot_h(c-v)-c.

Exact literal context geometry gives

    max_(v,h) ||rot_h(c-v)-c||_infinity=8.

The all-displacement linear thin-chord theorem therefore gives

    j<=20(R+8)+111=20R+271.

After that clock, untouched entry identities are outside EVERY possible next
complete context, including WHITE requirements. This is a context exclusion,
not merely the earlier input-funding horizon20R+211.

## 4. Exact online packet-frontier invariant

At a current full boundary j, represent the true finite board by:

1. Its exact actual head and heading and transported five-cell core.
2. Every current produced residual identity with full-source age at most330.
3. Every still-current untouched entry identity until j>20R+271.

Discard older produced identities from the reduced board. At each valid packet
step, remove all exact input identities first and then install every output
with a fresh identity, even at a recycled black-to-black cell. Tag outputs by
the FULL source-entry clock, not a later atomic installation clock; add the
packet's C tails to ages and collect newly expired identities afterward.

At any current actual full boundary, Sections2 and3 show that every omitted
true black cell is outside the union of all candidate complete contexts.
Thus the reduced and full boards agree on every such context. In particular:

- Each candidate raw-plus-marker packet is compatible with the full board
  if and only if it is compatible with the reduced board.
- An incompatible candidate fails at the same first read on both boards.
- Every compatible packet has the same physical raw trace and marker and
  the same identity update on both.

Induct from the original U-entry state. Whenever the reduced system takes a
valid complete packet, the original board takes that SAME valid packet too,
so the actual U-entry simplicity premise remains established for the next
cut. No old center path needs to be stored or tested by the reduced algorithm;
the signed theorem supplies simplicity along the actual recognized factor.

Consequently this is a transition-complete online representation of the
retained packet factor, not only replay of a preselected valid future. It can
recognize the same allowed next packets and the first language exit. If the
retained factor ends, STOP: omitted archives can matter to subsequent arbitrary
non-language ant motion, which is outside this theorem. Keep the original
archive separately if full physical continuation beyond that exit is wanted.

If the packet parser carries additional finite maximal-C/DFA state, preserve
that state exactly on both sides; equality of all literal context tests is
unaffected. No new alphabet or arbitrary atomic word is licensed.

## 5. Finite, effective, but not uniformly bounded

Let r0=m-5 be original entry residual mass and let N_a count packets begun at
full-entry clock a. The signed zero-C fuel / fixed-heading projection theorem
gives N_a<=r0(2a+10), without assuming bounded current mass. Each packet has at
most15 outputs. Therefore the retained produced-ID count is at most

    15r0 * sum_(a=max(0,j-330))^j (2a+10).

For j>=330 this is

    15r0 *331*(2j-320),

so the frontier has O(r0*j) cells plus the core and, before expiration, at most
r0 untouched entry identities. The signed root-box radius also bounds its
spatial domain by the union of the original-root L-infinity boxes of radius
floor((2j+13)/3), with the exact core kept separately.

Thus arbitrary zero-C runs do not make the C-cut state infinite or undefined:
there is a proved effective finite bound at each j. But that bound grows with
j, and the actual age-two rail family in young_rail_reuse_all_N.md excludes
an age-only uniform head-radius/cardinality bound even at four C increments.
That family does NOT settle uniformity after entry expiration; its returns
still use entry roots. Neither the growing frontier nor the331-layer cutoff
proves that C, U, or V events stop, nor that the full ant captures.

## 6. Provenance and verification

The signed thin-chord geometric theorem is
causal_archive_spatial_lifetime_2026-10-23/manifest.json. The exact checker
check_full_context_horizon.py independently reconstructs each raw-plus-marker
first-read context and before color, every output/context alignment, all157
site sets, all eight maximizers, and every entry-context offset. Its complete
controls are full_context_horizon_controls.json. The two full-source age
conventions and remove-before-install identity semantics are unchanged.
