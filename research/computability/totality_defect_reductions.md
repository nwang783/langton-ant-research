# A precise independence target that does not automatically refute capture

22 October 2026. Status: independently audited conditional logical reduction, not an ant compiler or an independence result. This is distinct from reducing unrestricted HALT to standard capture.

## 1. Why unrestricted universality has the wrong consequence for independence alone

A verified compiler with “the source machine halts iff its finite ant seed captures” would refute the universal highway conjecture, because nonhalting machines exist. It would not merely show that the conjecture is difficult or unprovable. Likewise, a finite-seed compiler in which every indefinitely running source emits infinitely many nonstandard ant factors would turn any explicit looping source into a counterexample.

To seek a true-but-unprovable universal statement instead, the source family should be a terminating family whose universal termination is unprovable in the named theory. A compiler for that restricted family need not yield a standard-model noncapturing ant.

## 2. Formal finite-defect reduction

Fix a theory T that formalizes the elementary finite ant updates, primitive recursive functions, and the fixed standard104 word W. Let F be the finite set of length10 factors of the cyclic W word. Let D_X(N) count positions i<N at which the length10 word beginning at i lies outside F. This is a finite, primitive recursive calculation from the finite seed X and N+9.

Let R(n,k) be the primitive recursive predicate that a specified source computation on n has halted within k steps. Assume it is monotone in k. The target source sentence is

    Tot_R: forall n exists k R(n,k).

Suppose there are primitive recursive functions f(n) encoding valid finite ant seeds and G(n,k), and T proves the following FINITE simulation implication:

    for every n,k,
    not R(n,k) implies D_(f(n))(G(n,k)) >= k.

The stronger function G is convenient, not logically essential: a T-provable existential finite-prefix witness also suffices. Its totality and the finite-prefix simulation must be proved in T, rather than importing the source termination theorem being reduced.

Then T proves

    HC implies Tot_R.

Proof: If f(n) has a standard tail starting at t, no forbidden length10 factor can START at i>=t. Hence D_(f(n))(N)<=t for every N. If the source had not halted within k=t+1 steps, the finite simulation implication would give at least t+1 distinct forbidden starts, a contradiction. Therefore R(n,t+1). Universalize n. QED.

This proof uses only the easy direction “standard tail gives finitely many forbidden factors”; it does not depend on the more delicate converse finite-factor theorem. Counting distinct starting positions is essential. Repeatedly reporting one old defect would not satisfy the premise.

Consequently, if T does not prove Tot_R, then T does not prove HC. Nothing here proves HC true, or proves T cannot refute HC. An independence claim needs that additional side; a one-way reduction establishes only nonprovability of HC.

## 3. A concrete source target

The standard hereditary-base Goodstein process supplies a classical example of an actually terminating family whose universal termination is not provable in Peano Arithmetic. This exact distinction is Theorem1(i),(ii) of Kirby and Paris, “Accessible Independence Results for Peano Arithmetic,” Bulletin of the London Mathematical Society14(1982),285–293. Primary article: https://www.cs.tau.ac.il/~nachumd/term/Kirbyparis.pdf ; publisher DOI: https://doi.org/10.1112/blms/14.4.285 .

Thus one possible protected research target is a PA-verifiable finite-seed implementation of the Goodstein STEP relation, with one distinct forbidden10 factor per unfinished source step. Since every standard Goodstein computation terminates, this restricted compiler would not by itself exhibit a noncapturing seed. It would instead transfer the known PA nonprovability to HC.

No such ant implementation is known here. This is much more demanding than observing long transients, high black mass, or a finite sequence of rail rewrites. It requires a fixed finite seed for each n, arbitrarily many verified consecutive simulated steps, complete color consistency, and a fresh defect-count witness for each step. Ordinary single-use infinite-background circuits do not provide these obligations.

## 4. How this interfaces with current finite-fuel work

A proof of a global finite-defect bound from a well-founded rank would prove HC if it also covers all legal words. A successful source compiler of the kind above would show that any such universal rank proof has at least the strength needed for Tot_R. Conversely, a sharp obstruction to renewable source memory might show that the compiler premise cannot hold for a proposed hardware family.

Existing local fuel arguments do not currently establish either conclusion for all ant paths. The one-sided builder and two-backward-archive geometries are possible interface targets, not implementations of Goodstein, tag systems, stacks, or counters.

## 5. A bounded-mass compiler cannot hide unbounded computation before every standard block

The bounded-first-L compactness theorem gives an additional, nontrivial constraint even for an actually terminating source family. Suppose a compiler has one UNIFORM upper bound m on the number of initially black cells, although it may encode the source input in arbitrarily distant coordinates. Suppose its source runs are arbitrarily long, and its verified ant simulation avoids a particular fixed finite standard word u throughout arbitrarily long corresponding prefixes.

Then these prefixes have uniformly bounded first-L mass and avoid u for unbounded lengths. Compactness produces an actual finite-seed ant of mass<=m that avoids u forever. Thus this stronger compiler property would REFUTE HC, even if every source run in the compiler's image eventually terminates. The limiting counterexample need not belong to the image of the compiler.

Accordingly, an independence-only construction using a fixed black-mass input family must allow arbitrarily long standard-looking episodes during the computation. Merely emitting a new defect at each simulated step, with long gaps between steps, is not excluded by this compactness argument. Alternatively, the seed mass may grow with the source input. This distinction is exactly why Section2 requires distinct defect production but does not demand that every computation prefix avoid a standard block.

For mass<=1 there is already an unconditional numerical version: every seed exhibits some cyclic standard104 block by106362 moves. No singleton-coordinate encoding can continuously suppress all such blocks for an arbitrarily long simulated computation, whatever the eventual outcome.
