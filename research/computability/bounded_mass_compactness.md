# Bounded first-L fuel restores a valid compactness argument

22 October 2026. Status: independent analytic audit passed for Sections1–6 and8, and independent numerical replay passed for Section7. This does not prove the highway conjecture. It identifies a stronger finite-prefix target for counterexample synthesis and a useful uniform early-episode consequence of fixed-mass capture results.

## 1. A compact tree whose every branch is a finite-seed ant

Fix the initial pose, and let m be a nonnegative integer. A finite relative turn word determines its geometric path without knowing the board. It is realizable exactly when the successive reads at each repeatedly visited cell alternate R,L,R,L,... or L,R,L,R,.... Its minimal initial black set consists of the cells whose FIRST read is L. Write mu(w) for the size of that set.

Let T_m contain every finite realizable turn word w with mu(w)<=m. This is a computable, prefix-closed binary tree. Every infinite branch has at most m first-L cells: otherwise a finite prefix would already exhibit m+1 distinct such cells. Initializing precisely those cells black realizes the entire infinite word by induction. Conversely, every ant starting from at most m black cells gives a branch of T_m; initially black cells that are never read are irrelevant.

Therefore the space of finite-seed turn streams with black mass at most m is exactly the compact branch space [T_m]. Coordinates of initial black cells are NOT bounded. Compactness nevertheless holds because cells escaping to infinity disappear from each fixed observed prefix.

Every individual branch is computable, since it is the orbit of a particular finite board. This does not give a uniform algorithm for selecting a branch from an arbitrary promised-infinite subtree.

## 2. Uniform finite-time occurrence of a finite word

Fix a nonempty finite turn word u. The following are equivalent:

1. Every finite seed of black mass at most m eventually exhibits u somewhere in its turn stream.
2. There exists a finite time T such that every such seed exhibits u within its first T turns.
3. The computable subtree of T_m whose words avoid u is finite.

Proof: (2) implies (1). If (3) fails, the avoidance subtree has arbitrarily long words; finite branching and Koenig's lemma give an infinite avoidance branch. Section1 realizes that branch with at most m initial black cells, contradicting (1). A finite avoidance tree has finite maximum depth, yielding (2). QED.

The same proof works for occurrence of at least one word from any fixed finite target family, including all cyclic phases of a standard block.

The universal occurrence assertion in (1), despite quantifying over arbitrarily distant seed coordinates, thus has a c.e. finite certificate: completely expand the finite legal-prefix tree until every branch has already exhibited u. Equivalently, search T and exhaustively verify all realizable words of length T with mu<=m. This is not claimed practical for large m or T.

## 3. A correct counterexample reduction

If one can construct arbitrarily long realizable words avoiding u, with a UNIFORM bound m on their first-L counts, there exists a finite-seed ant avoiding u forever. When u is the standard104 word, this refutes eventual standard capture.

The fixed bound is essential. Merely realizing each length with some finite seed permits the required first-L count to grow without bound and gives no finite-support limit. The earlier four-cell capturing-completion theorem is consistent with this result: every finite avoidance prefix can still be completed into a capturing orbit, but those completions eventually leave the avoidance subtree.

This route is sufficient, not necessary for a counterexample. A genuinely noncapturing orbit could contain arbitrarily long standard104 episodes, and hence would not lie in any fixed bounded-standard-run avoidance class. Likewise, unbounded permanent-capture delay at fixed black mass does not supply the required avoidance words: the delayed singleton family already has long standard episodes before its late disturbance.

## 4. What a fixed-mass highway theorem would imply

If every seed of mass at most m captures standard104, then for every K there is a COMPUTABLE finite bound T(m,K) by which every such seed has exhibited K consecutive copies of the standard word. Search the complete prefix tree for that finite witness. The assertion is uniform over all initial black-cell coordinates, even though the least PERMANENT capture onset has infinite supremum already at m=1.

This is an early-episode bound, not a capture-time bound or a bound on the total number of later defects. It does not imply that the first observed repeated block is permanent.

## 5. A finite singleton calculation

Let T_0 be any verified time by which the blank orbit exhibits u, and let V_0 be the finite set of cells read before T_0. A singleton outside V_0 cannot alter that prefix. Thus the uniform singleton first-occurrence bound is obtained by testing only the singleton seeds at cells of V_0, together with the blank seed. If all those finitely many trajectories eventually exhibit u, the maximum of their first-occurrence times is a valid bound for EVERY singleton anywhere on the infinite grid.

The same idea iterates conditionally: for each partial seed whose trajectory exhibits u, any avoiding extension must place its next first-read black cell somewhere in the finite prefix preceding that occurrence. This yields a finitely branching adaptive seed search with depth at most m, but its individual simulations need not terminate if a genuine avoidance seed is found.

## 6. Exact scattered rank of the bounded-mass trajectory space

There is a more precise unconditional topological statement. Let K_m=[T_m], and let K'_m denote its set of nonisolated points. Then

    K'_m = K_(m-1) for m>=1,
    K_0 is the singleton blank turn stream.

A branch with exactly m first-L cells is isolated in K_m: its prefix through the last first-L read has exhausted all m choices, so every continuation in K_m is the unique orbit of that completely specified minimal seed.

Conversely, take a branch whose minimal seed B has j<m black cells. The finite-seed escape theorem guarantees infinitely many fresh cells along its path. Choose a fresh cell q first reached after both an arbitrarily long prescribed prefix and all j first-L events. Adding q to B preserves that prefix and changes the read at q from R to L. The new stream has exactly j+1 first-L cells: all j old ones were already read before the disturbance, and the only new initially black cell is q. Such streams are distinct and converge to the original branch. Hence every branch in K_(m-1) is nonisolated in K_m.

Thus successive Cantor-Bendixson derivatives are K_m,K_(m-1),...,K_0,empty. The rank is exactly m+1. This uses no highway conjecture. It does not make capture membership decidable: topological isolation of a branch supplies a finite board, not an answer about that board's infinite future.

## 7. Singleton first-block computation

Status: complete literal computation, independently replayed with a different pattern detector.

With initial pose (0,0),N, the blank trajectory's first occurrence of any cyclic phase of its certified standard104 word ends at time10081. Exactly1398 distinct cells are read before that time. The complete calculation of Section5 checks a singleton at every one of those sites, using exact104-bit rolling words and literal ant updates. All1398 reach a standard104 block. Their maximum FIRST block-completion time is

    106362 moves,

attained only at singleton coordinate(7,7) among those candidates. The first such block there starts at time106258. Singletons outside the candidate set preserve the blank block ending at10081. The blank seed itself does too.

This gives a uniform first-block bound for mass at most1, over the entire infinite coordinate domain, with independent implementation replay. Translation and quarter-rotation invariance extend it to every initial pose. It says nothing about permanence of that block. The separate certified far-singleton family has unbounded permanent onset despite this bound.

Artifacts: singleton_first_block.cpp, singleton_first_block_input.json, singleton_first_block_input.txt, singleton_first_block.csv, singleton_first_block.log. The supplied standard word is independently checked by the exact all-time tail verifier at blank time9977. The candidate calculations total14,740,545 physical updates.

The independent replay reconstructs the blank read set and uses a10,119-state trie/failure automaton rather than rolling104-bit codes. It matches every candidate result row, not only the maximum. Audit artifacts: ../audits/check_singleton_first_block_independent.py and .json, ../audits/singleton_first_block_independent.log.

## 8. A second obstruction to naive HALT reductions: two monotone parameters

Status: independent analytic audit passed.

Fix the standard word W, and let Occ(m,K) mean that EVERY seed with at most m initial black cells eventually exhibits K consecutive copies of W. One can instead allow any cyclic phase, with the same conclusions. The failure set

    Bad = {(m,K): not Occ(m,K)}, m>=0, K>=1,

is upward closed in BOTH coordinates. Increasing the mass budget retains a counterexample, and avoiding W^K implies avoiding any larger power.

Every upward-closed subset of N x positive-N has a finite minimal basis. Here is the elementary two-dimensional proof, without any effective assumption. If Bad is nonempty, let m0 be its smallest first coordinate, and let K0 be the smallest failure at m0. Every other minimal pair must have K<K0, otherwise (m0,K0) dominates it. For each of the finitely many K<K0, at most one first coordinate can be minimal. Thus the basis is finite.

Consequently Occ(m,K), for this FIXED ant rule and fixed W, is a recursive predicate in the classical NONUNIFORM sense: hardcode the finite minimal failure pairs, then compare the two coordinates. If Bad is empty, use constant YES. We do not know the basis, including whether it is empty, and this argument supplies no current implementation of that decider. Nonetheless it rules out a many-one reduction from HALT to this two-parameter predicate. The same warning applies to its complement.

Combining this recursion fact with the compact finite-occurrence search gives another exact existence result: there exists a total computable function U(m,K) which bounds the first W^K occurrence uniformly over all mass<=m seeds whenever Occ(m,K) is true. On false pairs it may return0. Indeed use the hardcoded finite-basis decider and, on true pairs, run the finite-tree exhaustion. This is an existence/nonuniform computability theorem, not a displayed numerical bound or a claimed known program.

This does not decide standard capture for an INDIVIDUAL finite seed. It also does not prove that every seed exhibits arbitrarily long standard runs, much less eventual permanence. The fixed universal sentence “Occ(m,K) for all m,K” can remain unproved in a named theory even though the actual two-parameter relation is recursive. Allowing the local rule or an arbitrary, nonnested target word as an additional input changes the scope and is not covered by this argument.


## 9. Why the same compactness does not bound permanent onset

The topology pinpoints the distinction. The first occurrence time t_u of a fixed finite target word (or finite target family) is continuous wherever it is finite: the prefix through the first occurrence both witnesses that occurrence and rules out any earlier one. If t_u is finite on all of compact K_m, its image is a finite subset of the discrete natural numbers, so it has a uniform maximum.

By contrast let tau be the least standard-tail onset, allowing infinity. The set {tau<=t} is CLOSED, because the entire suffix from t must equal one of the finitely many cyclic standard streams. Thus tau is lower semicontinuous, not generally continuous. A finite-valued lower semicontinuous function on a compact space need not be bounded above.

The certified far-singleton family makes this failure literal, not abstract: its streams converge to the blank stream as their first disturbance times tend to infinity, but their permanent onsets tend to infinity while the blank onset is finite. Therefore bounded-mass compactness is a legitimate tool for finite-episode occurrence and a demonstrably invalid shortcut to uniform permanent capture time.
