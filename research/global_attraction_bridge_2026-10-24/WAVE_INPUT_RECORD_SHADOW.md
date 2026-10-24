# A last-copy old input shadows the interior record clock

24 October 2026. Author exact lemma and three full-word specializations. Independent audit is separate. This is a geometric consequence of a proved first-input condition, not a universal language cover.

## 1. Main statement

Let a finite-seed Langton orbit execute N>=1 consecutive copies of a supplied length-P turn word w. One copy must restore the actual heading and have nonzero drift d. Retain the entire field and all prior history. Use the four strict axial record clocks of the rectangle containing all original black cells and all earlier head positions.

Suppose the one-copy read positions q_i admit a phase i0 such that:

1. w[i0]=L;
2. whenever q_j=q_i0+m d for an integer m, we have m<=0;
3. among phases with q_j=q_i0, i0 is the earliest.

This is an exact stable first-read BLACK input condition. It is checked on the whole literal word, not inferred from period, pose, or a supplied-field approximation.

For each positive-drift axial normal a, define

`C_a = ceil((max_i a.q_i - a.q_i0)/(a.d))`.

Every record event in that normal lies in the last C_a copies of the block. For every nonpositive-drift normal, every event lies in the first copy. The claim concerns the half-open block of head cuts 0,...,NP-1; its final endpoint belongs to the next interval.

### Proof of the actual old-input premise

The physical cell X=q_i0+(N-1)d is first read inside this block at tick P(N-1)+i0. Indeed, an occurrence q_j+k d=X would require k=N-1-m>=N-1. Equality can first occur in copy N-1, and condition 3 selects phase i0 there. Thus this first read is L, so X was already BLACK at the beginning of the block and has stayed unread throughout the preceding portion of the block.

Every black cell present at a finite-seed cut either belongs to the original initial support or was written at an earlier head read. Consequently X is inside the augmented historical rectangle BEFORE the repeated block. This is where finite causal reachability and the full initial support are essential. We do not assume every old black cell lies inside the head-only hull.

For a.d=delta>0, the maximum head projection in copy k is max_i a.q_i+k delta. If k<=N-1-C_a, this is at most a.q_i0+(N-1)delta=a.X. Such a cut cannot be a strict augmented-hull record. For delta<=0, each phase in any copy k>=1 is dominated by its same-phase occurrence in copy zero. These two observations prove the claim for the actual orbit with every exterior archive retained.

No physical inverse, deletion, new seed addition, or changed continuation is used.

## 2. Three exact one-copy fringe constants

The following witnesses refer to the literal orientations of the signed supplied words. Proper physical quarter-rotations and translations preserve the statement.

### Supplied1564 word

- P=1564, actual initial heading N, d=(14,14).
- Phase i0=1455 is L at q_i0=(4,35).
- The ENTIRE drift orbit in one copy has only this visit: phase1455, shift0, L.
- Maximum head projections are max y=40 and max x=18.
- Therefore C_N=ceil(5/14)=1 and C_E=ceil(14/14)=1.

### Supplied4352 word

- P=4352, actual initial heading W, d=(26,26).
- Phase i0=1687 is L at q_i0=(29,10).
- The whole same-drift orbit has only phases1687 L,1695 R,3163 L, all shift0.
- Maximum y=36 and maximum x=55.
- Therefore C_N=C_E=1, with exact differences26 in both directions.

### Supplied15324 return word

- P=15324, actual initial heading N, d=(-78,-78).
- Phase i0=4264 is L at q_i0=(-32,-28).
- The entire same-drift orbit has only this visit, shift0.
- Maximum -y=106 and maximum -x=108.
- Thus C_S=ceil(78/78)=1 and C_W=ceil(76/78)=1.

For EACH of these three words, in ANY actual finite-board legal N-copy occurrence, all strict axial union-record events lie in its FIRST or FINAL copy. Every intermediate copy is entirely record-free. This applies to an arbitrary causal producer and arbitrary retained archive, not only the 184/394 sources used to discover the words. It does not assert that such arbitrary producers exist.

The separately signed named-family event projection is stronger for its particular histories: their entire long wave stages, including the first and last copies, have no record events at all.

## 3. Completed drought count consequence

Let H>=0 be an INTEGER. For N>=2, at most

`2 floor((P-1)/(H+1)) + 1`

completed >H gaps can have both endpoints INSIDE one of these N-copy blocks. Each allowed endpoint window has at most P cuts and span P-1; at most one gap joins the two windows. For N=1 use the smaller bound floor((P-1)/(H+1)). Empty event windows only reduce the bound.

At most two additional global gaps can cross the endpoints of the block. These joins cannot be added independently if blocks overlap or if a common global gap crosses several empty blocks. The assertion is a per-block bound, not a disjoint global fuel sum.

Hence increasing N alone cannot make the number of completed >H droughts unbounded, even when H is smaller than the nonstandard period. This removes the small-H loophole from the coarse repeated-template bound in the preceding package, for these exact supplied words.

The fixed cardinality of the producer is not used in this deduction. The ant may have manufactured the required old input from a small original seed. The obstruction concerns the chronology and geometry of a whole repeated block, not a mass-only resource potential.

## 4. Relationship to the retained input-fuel calculation

The same argument applies to q_i0+j d for every j=0,...,N-1, so these N distinct old-at-entry black lifetimes are each consumed later within the block. Distinct stable first-L drift classes give disjoint such inputs. The full literal inventories have197,406,1439 such classes for1564,4352,15324 respectively. This is the familiar linear old-input requirement in causal form, not a claim of new original-seed fuel.

In particular the entire future-consumed current cohort at block entry has at least197N,406N,1439N members respectively. These are lower bounds only; additional finite fringe inputs may be required. The retained exact minimum-fuel work already contains the stronger detailed field inventories. Fresh production can supply these old-at-entry lifetimes, so one cannot sum this charge over later blocks without an actual non-reuse argument.

The new point here is that a SINGLE selected late input already constrains the whole pristine record clock before it is consumed, independently of how the other required inputs were produced.

## 5. Full-field controls and scope

The checker evaluates every phase and every integer drift-orbit equality in all three words, confirms the actual heading and drift, and proves the positive-axis inequalities with their exact integer slack. It replays complete original184 N4/N10 and original394 M1/M3 histories. At each selected wave entry it records the full board hash and the selected true old lifetime, then verifies its exact first within-block L consumption. All final black fields are retained and certified against their complete infinite canonical futures.

The all-N theorem comes from the orbit equality and projection proof, not from these four controls. The controls specifically protect against mistaking an abstract supplied input for a genuinely present old lifetime in the actual producer.

What remains unproved is the existence or impossibility of an actual fixed-cardinality architecture generating arbitrarily many SEPARATE returning blocks with intervening pristine records. Neither this shadow lemma nor the finite-template event bound controls how often a new block can be generated, and neither proves compact-return occurrence or canonical104 attraction.
