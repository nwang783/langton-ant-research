# A primary-source recurrence method, and its exact classical-ant obstruction

24 October 2026. Author derivations and literal checks below await independent audit.
This is not a proof of capture, transience, record-clock occurrence, or a new literature result.

## Result first

The most concrete external recurrence mechanism found in this pass is **completed-excursion expansion for simple rotor walks**. Its graph hypotheses really do match the classical ant's fixed checkerboard sector. Its essential local hypothesis does not. The mismatch is not just terminological:

* From the actual blank orbit's complete cut-8 board, the first repeated directed edge is `(0,1) -> (-1,1)`, at reads 9 and 13, before the return to the starting cell at 16.
* Its consecutive two-return packets `[0,8)` and `[8,52)` lose three previously read cells; the latter reads some cells four times. Thus neither excursion containment nor the degree-two local visit bound transfers.
* In the **certified whole-field standard tail**, reads `9980+104k` and `9984+104k` at `(8-2k,16+2k)` depart south twice, with no intermediate read of that cell. Consequently every 108-read window starting at or after 9980 violates the simple-rotor exit rule on the physical checkerboard graph.

This last statement rules out a particularly natural occurrence argument: one cannot find a sufficiently late, long, rotor-simple window and then import a rotor excursion theorem. It fails even for the successful blank orbit. It is not a counterexample to record-clock occurrence itself.

## 1. Primary sources actually inspected

The retained `literature.md` already covers classical unboundedness, Etse's finite confinement, finite/infinite-background complexity distinctions, hyperbolic transfer, and guarded finite-seed work. Those are not new findings here. This pass adds the following precise comparison.

### 1.1 The selected deterministic theorem

Florescu, Levine and Peres, *The range of a rotor walk*, §2, especially Lemmas 2.1, 2.2 and 2.4, defines a simple rotor walk by a fixed cyclic ordering of every vertex's outgoing edges. On a connected Eulerian graph, completed excursions visit each vertex at most its outdegree, and each subsequent completed excursion covers the previous excursion's sites and their outgoing neighbors. The proof uses the fact that an outgoing edge cannot be repeated before all other outgoing edges at that vertex have been used. Theorem 1.1 then gives a range lower bound on periodically embedded Eulerian graphs. These are deterministic statements, not random-environment assertions. [Primary PDF](https://arxiv.org/pdf/1408.5533).

This is an attractive candidate because it connects chronological last exits to forced exploration. Even if it transferred, range growth alone would not establish a bounded union-record clock or canonical capture. A separate return/clock argument would still be needed.

For cut conventions below, a packet ends at the second subsequent return to its starting site. The article's prose describes return excursions; its displayed visit-count threshold is also evaluated separately in the checker, and that convention does not repair the ant counterexample. No result here depends on silently shifting a source index.

### 1.2 Why finite-perturbation invariance is not available for free

Angel and Holroyd, *Recurrent rotor-router configurations*, Journal of Combinatorics 3 (2012), 185–194, Theorem 1 and Corollary 6, prove starting-vertex and finite-rotor-perturbation invariance of recurrence/transience for their fixed graph and fixed rotor mechanism. Their proof uses the abelian property. Proposition 7 gives a sufficient reflecting-boundary criterion for recurrence. Lemma 8 identifies the first repeated directed edge with the starting vertex. These hypotheses concern cyclic neighbor rotors, not a flipping turn relative to the incoming heading. [Primary journal PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/joc/2012/0003/0002/JOC-2012-0003-0002-a003.pdf).

This would be exceptionally powerful if a finite-perturbation-preserving conjugacy were supplied. None is supplied here. The local order test in §4 blocks the direct site-processor identification; it does not prove that every conceivable lift or encoding is impossible.

### 1.3 A genuinely applicable conjugacy, with the correct background

Rechtman and Rechtman, *Equivalence of Deterministic walks on regular lattices on the plane*, Theorem 1, gives an exact square-lattice flipping-rotator/flipping-mirror equivalence. For an origin start with horizontal heading, its scatterer signs satisfy `sigma_R(x,y)=(-1)^(|x|+|y|+1) sigma_M(x,y)`. Thus a uniform rotator background corresponds to a checkerboard mirror background. A finite black perturbation stays finite **relative to that checkerboard**, not relative to uniform mirrors. [Primary author PDF](https://www-fourier.univ-grenoble-alpes.fr/~rechtmaa/Documents/det-walk.pdf); [arXiv record](https://arxiv.org/abs/1603.08269).

The gauge is independently checked at all 10,081 actual reads here. It does not turn flipping mirrors into arrival-independent rotors. A theorem about uniform mirrors cannot be substituted for a theorem about checkerboard mirrors. The source's introductory illustrations of disorder followed by highways are not used as a universal finite-seed theorem.

### 1.4 Explicitly excluded nearby results

Webb and Cohen's *Self-Avoiding Modes of Motion in a Deterministic Lorentz Lattice Gas* concerns honeycomb flipping scatterers and specified initial configurations. Its self-avoidance-between-returns statement is not a square-lattice theorem. [Primary preprint](https://arxiv.org/abs/1404.3629).

Their *Self-Limiting Trajectories of a Particle Moving Deterministically in a Random Medium* concerns honeycomb scatterers with independent random initial orientations, with probabilities strictly between zero and one for the periodicity result. Neither the lattice nor the initial distribution is the present finite-seed square problem. [Primary preprint](https://arxiv.org/abs/1507.07133).

Bou-Rabee and Peres's 2026 preprint *Eulerian walkers on Z² have range exponent 2/3* studies the four-neighbor clockwise rotor mechanism with independent uniform initial rotors. Its recurrence and limit-shape statement is a different dynamical rule and a different initial class, not evidence that square RL finite seeds recur or capture. Only the model and principal claim were inspected; no independent verification of that paper is claimed. [Primary PDF](https://arxiv.org/pdf/2608.23545).

## 2. The graph hypothesis passes exactly

Use headings `N=0,E=1,S=2,W=3`, WHITE turns R, BLACK turns L, and initial pose `(0,0),E`.
Every step changes the parity of both time and the head coordinate sum. Because every turn is a quarter-turn, incoming headings are horizontal at even sites and vertical at odd sites.

Consequently the physical trace follows the directed graph with:

* even sites having both vertical outgoing edges and both horizontal incoming edges;
* odd sites having both horizontal outgoing edges and both vertical incoming edges.

It is connected, periodic and Eulerian, with indegree and outdegree two. This is not an obstruction caused by using the wrong graph or degree. The precise failed hypothesis is the order of its two exits.

## 3. Exact ordered-arrival identity

Fix a cell and a contiguous list of its visits. Let `e` be one positive incoming direction and `f=R(e)`. Write its j-th incoming direction as `a_j e`, where `a_j` is ±1. Let `r_0` be +1 for its first R and -1 for its first L. Since the cell flips, its j-th turn sign is `r_0(-1)^j`. Its outgoing direction is therefore

`z_j f`, where `z_j = r_0(-1)^j a_j`.

Three consequences are immediate and exact:

1. Two consecutive exits agree if and only if the corresponding incoming directions are opposite.
2. The outgoing signed imbalance is `sum z_j = r_0 sum (-1)^j a_j`.
3. Pair visits `(0,1),(2,3),...`. If J pairs have opposite incoming directions and n visits occur, then `|sum z_j| <= 2J + (n mod 2)`.

There is no cancellation assumption. Every defective pair can contribute the same sign. All two-color, two-axis and sign-word instances through length eight are checked independently of any simulated route (2,040 cases), in addition to the algebraic proof.

Thus the ant is rotor-like on a local visit list **if and only if all incoming directions on that list agree**. Alternating read colors do not imply alternating exit neighbors. Static R/L balance also does not control the alternating arrival-sign sum.

For comparison with harmonic/odometer methods, let `u(v)` count departures on any finite interval and let `d(v)` count exits in the positive allowed outgoing direction minus exits in the negative direction. For any test function F, direct summation over the actual path gives

`F(p_t)-F(p_s) = sum_v u(v) L F(v) + (1/2) sum_v d(v) [F(v+f_v)-F(v-f_v)]`,

where `L F(v)=[F(v+f_v)+F(v-f_v)]/2-F(v)` and `f_v` is the chosen positive outgoing axis. This is bookkeeping, not a new estimate. In a simple degree-two rotor walk `|d(v)|<=1`; in the ant, §3 supplies an ordered-arrival expression for d, not that bound. Any discrepancy-based transfer must estimate this additional term rather than discard it.

## 4. The two-input abelian test fails

Start one local WHITE scatterer. Supply incoming headings N then S. Its turns are R then L and both outputs are E. Reverse the supplied input order to S then N. The same turns leave the same final color, but both outputs are W.

The two input multisets and final local bit agree, while the output multisets differ. This is a local processor test, not a claim that both external routes were constructed. It excludes a direct abelian-network argument with the physical cell as one processor and arrival directions as input letters. Splitting incoming headings into separate vertices does not by itself fix the issue: those vertices still share one toggled color bit. A valid lift must explicitly solve that coupling and preserve the finite-background class.

## 5. Literal whole-field countercontrol

The initial seed is empty. At cut 8 the complete BLACK set is

`{(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)}`,

and the head is at `(0,0)` heading W. The first repeated directed edge after that cut occurs at ticks 9 and 13, from `(0,1)` to `(-1,1)`. No edge was repeated earlier in that reset segment. The first return to `(0,0)` is at cut 16. This directly falsifies the rotor first-repeated-edge conclusion for the ant, with every old cell retained.

For the two-return packets `[0,8)` and `[8,52)`, the second packet omits the first packet's cells `(0,-1),(1,0),(1,1)`, and its maximum read multiplicity is four, not two. The checker also retains complete fields at cuts 0,5,8,9,13,14,16,17,52. No arbitrary reset color assignment is used.

## 6. Why the defect cannot be dismissed as a transient

The full blank board at cut 9977 has 715 BLACK cells. Its infinite canonical continuation is checked by all exact ray-parity change points, not a finite repeated-word test. The drift is `(-2,2)` per 104 updates.

At ticks 9980 and 9984 the head reads `(8,16)`, with incoming headings W and E, turns L and R, and outgoing heading S both times. The intermediate three reads avoid that cell. Translation of the certified entire future gives the same consecutive-read pair at every `k>=0`.

For any integer start `a>=9980`, choose the first such pair whose first tick is at least a. That first tick is at most `a+103`, and the second at most `a+107`. Thus `[a,a+108)` contains a repeated-exit defect. In particular no sufficiently late window of the enormous retained forcing length `F*(H)`, for `H>=2`, can satisfy the simple-rotor hypothesis. The blank seed has cardinality zero, so a finite budget of these raw defects charged only to original inputs is also impossible.

This does not exclude signed cancellation, comparison after quotienting canonical behavior, or a different state encoding. It identifies exactly why a raw finite-defect rotor reduction is the wrong bridge.

## 7. Falsifiable proof attempt and remaining obligation

Attempt tested: represent the classical ant on its actual Eulerian checkerboard graph, use alternating cell colors to infer a simple rotor mechanism, then import completed-excursion expansion and seek a bounded-clock window. The first inference is false by §3–§6. The attempted route is now ruled out without a broad scan.

A materially different attempt would have to provide at least one of:

* a proved input-order-preserving rotor encoding with a finite-perturbation-preserving background map; or
* an ant-specific replacement for the excursion expansion argument, with an explicit estimate on the signed ordered-arrival term and a separate implication for union-record clocks.

Merely proving a range lower bound, observing a checkerboard mirror conjugacy, or counting all repeated-exit events does not provide these. No such estimate or encoding is claimed. The precise open global target remains occurrence of a finite forcing clock window (and then classification of the resulting translator), not a theorem about an unrelated random or supplied background.

## Reproduction

Run `python check_rotor_excursion_transfer.py` in this directory. The checked JSON contains all 10,081 literal turns, the selected complete fields, all early read events, exact source-dependency hashes, and the whole-field infinite-tail certificate data. Source literature was read-only. No upstream artifact was altered and no novelty claim is made.
