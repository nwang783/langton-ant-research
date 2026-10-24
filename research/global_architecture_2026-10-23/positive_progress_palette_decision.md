# Strict-progress finite palettes: an exact finite-memory decision boundary

23 October2026. Analytic extension, submitted for independent review. No
compiler, candidate search or generated numerical certificate is claimed.
The finite-seed white-input periodicity special case is an application of the
retained stale-memory framework, not a newly discovered global theorem.

## 1. Supplied hypotheses

Give a finite palette Sigma of nonempty literal ant words, all with the same
incoming and outgoing heading h. Their displacements d_sigma may DIFFER.
Give an integer linear functional ell such that

    delta=min_sigma ell(d_sigma)>0.

Let E be the finite union of their relative phase-read positions, M the maximum
word length, and

    emin=min_E ell, emax=max_E ell,
    H=emax-emin, K=floor(H/delta).

Give a background T periodic under a supplied full-rank rectangular lattice,
for example explicit binary data of periods p_x,p_y in the two coordinates.
White input is a special case. Periodicity ONLY along one direction is not
silently substituted for this stronger input hypothesis.

We decide infinite legal palette execution from the origin on T with (a) a
specified finite cap, (b) some finite arbitrary-XOR cap, or (c) some finite
black-additions-only cap. All caps are initial changes, not adaptive external
board interventions during the eventual infinite execution.

## 2. Geometric return bound

If block i and block j>i read the same cell, write their phase positions as
e_i,e_j in E and their head starts as p_i,p_j. Then

    (j-i)*delta <= ell(p_j-p_i)=ell(e_i-e_j)<=H.

Therefore j-i<=K. No cell can be read in two blocks separated by more than K
block boundaries, regardless of the choices or of the background coloring.
Multiple visits inside one block remain governed by its exact literal order.

In particular, a currently read cell absent from the previous K blocks has
NEVER been read earlier in this one-sided execution. An old recorded cell
that ages beyond K can never be read by any later allowed continuation.
This is a geometric retirement theorem, not a guessed memory truncation.

## 3. Exact finite colored-history graph

At a block boundary store:

- head position modulo (p_x,p_y);
- the previous at most K block labels, in chronological order;
- the CURRENT colors on the union of those blocks' physical read supports,
  expressed relative to the present head.

The labels determine all their relative poses, read supports and last-read
ages. Crucially the state does not assign arbitrary ages to arbitrary relative
cells: its colored support is exactly the geometrically reconstructed union.
This avoids an invalid eviction rule based on fictional independent ages.

There are finitely many such geometric supports. At most K*M cells are stored,
and the label-history count is at most

    S=sum_(j=0 to K) |Sigma|^j.

Thus a deliberately coarse graph-state bound is

    V <= p_x*p_y*S*2^(K*M).

For a selected next word, execute its actual reads and toggles. A read already
in the colored support uses its stored bit. Every other first read uses T at
the actual head phase plus its relative position. Multiple new visits in that
same word use the same evolving bit. After executing the word, move the frame
by its actual d_sigma, append its label, remove the oldest label if necessary,
and retain colors only on the reconstructed new support.

Every discarded cell is proved permanently unreadable after retirement by
Section2. It stays on the board. Every introduced recorded cell was actually
read in this block, and its current color is known. Thus transitions are
exact for real reachable states, including partial-history warmup from the
initial EMPTY history at head phase(0,0).

For an arbitrary full-history graph state, its labels may represent only a
geometrically consistent fictional past. That is not used to assert actual
past reachability. All cap decision tests below start at the empty history and
use explicit finite reachability. Cycle certificates arise only after that
reachability test or from an actual infinite path.

## 4. Unknown finite caps: finite controlled input, not controlled survival

Let G be the UNCONTROLLED graph with fresh bits supplied by T. Compute Z, the
vertices from which a G cycle is reachable.

Make a CONTROLLED version of the same finite state graph. At every genuinely
new cell in a block allow an arbitrary initial bit in the XOR variant, or
allow T-black only as black and T-white as either bit in the additions-only
variant. Every later read of that same cell uses its literal toggled value.

A finite controlled path from empty history uses finitely many distinct new
physical cells. They are globally new, not merely absent from a truncated
record, by Section2. Hence the selected differences from T are one genuine
finite initial cap. Conversely any finite cap produces such a finite path
until its last cap cell is read. Afterwards it follows G.

It follows that an infinite execution with some finite cap exists exactly
when Z is reachable in the controlled graph from the empty-history origin
state. All graphs and their reachability sets are finite and effective.

A CONTROLLED cycle alone is insufficient: it might need infinitely many new
initial black cells. Likewise arbitrary G-cycle existence is not the stated
test. Varying block strides may skip the origin input phase, unlike the
unit-increment clock in the common-D theorem. These are genuine obligations,
not reset conventions.

## 5. A specified cap: exact finite transient, then autonomous graph

For a finite specified cap C put cmax=max_(q in C) ell(q). If C is empty take
N=0. Otherwise let

    N=max(0, floor((cmax-emin)/delta)+1).

For every block n>=N, all its read cells have ell-coordinate at least
n*delta+emin>cmax. Hence no cap cell can be read in those blocks.

Process the first N blocks by exact finite branching over the supplied
palette. During this prefix retain the actual head position as well as the
finite colored history, so membership in the specified cap is evaluated at
the correct physical cell. The set of prefixes is finite; no efficiency or
uniform small transient is asserted. Project the resulting states to the
finite phase/history graph, then test reachability to Z.

The colors left by earlier cap interactions remain in the stored history and
are not reset. No cap cell is read after N. This proves decidability for a
specified cap as well, including arbitrary offsets of its finite support.

## 6. Consequences, provenance and exact exceptions

For a FIXED specified board admitting an infinite execution, the actual
physical trace is eventually translating periodic. Finite-state cycle
reachability supplies an ultimately periodic literal continuation on that
SAME board; determinism identifies the real trace with it. Every cycle drift
has positive ell, so is nonzero. After the exceptional cap prefix, cycle and
entry lengths have the usual finite-state bounds V*M and (V-1)*M.

The retained `../sources/kehao95-core/memory_feedback/proof/stale-memory.md`
already gives a suffix predictor when stale black reads are absent. On white
input the return bound above supplies such bounded memory after the finite
cap is past. That finite-seed conclusion is attributed, not relabeled new.
The extension here packages the exact prepared-input graph and both finite-
cap reachability variants for variable displacements.

This is not the retained cone-domain transience theorem: that theorem concerns
finite ell-sublevel domains and repeated visits to finite pose sets. Here the
stronger per-BLOCK progress assumption directly bounds return TIME in blocks.
Nor is moving endpoint progress alone enough. The retained certificate target
`../causal_reduction/controlled_strip/swept_front_certificate.md` permits old
bulk cells to be reread on every growing out-and-back lap. Its lap footprint
is unbounded, so it violates the finite E hypothesis despite endpoint drift.

No conclusion is imported for palettes without a common strict-progress
functional, unbounded block footprints, nonperiodic input, or input periodic
only along one direction while blocks wander transversely. In particular,
changing drift is not by itself an escape: it must defeat these sufficient
finite-memory hypotheses. The unrestricted finite-seed eventual-translation
and standard104-classification gaps remain open.
