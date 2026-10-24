# Why generic infinite-board aperiodicity says nothing against finite-seed capture

2026-10-22,23:30 UTC. Status: Sections1--4 independently analytically audited, including the effective null cover. This is not a finite-seed undecidability reduction. The domain and input representation are essential.

Fix a launch pose and let X={0,1}^{Z^2}, with its product topology. A basic cylinder specifies finitely many initial cell colors and leaves every other cell free. Let H be the boards whose turn stream eventually becomes cyclic standard104, and let P be the boards whose turn stream is eventually periodic with ANY finite period.

## 1. Closed realization sets for prescribed eventually periodic words

For a fixed finite prefix u and nonempty period v, the prescribed infinite turn word u v^infinity determines the entire pose path. At each visited cell its requested turns must alternate. If they do not, the realization set R(u,v) is empty. If they do, the initial color at each visited cell is fixed by its first requested turn. Thus R(u,v) is the intersection of the corresponding single-cell closed cylinders, and is closed.

Every nonempty R(u,v) fixes infinitely many distinct cell colors. Otherwise the legal path would be confined to finitely many cells; copying their initial colors to a finite seed would reproduce the entire bounded orbit, contradicting the established finite-seed escape theorem. Alternatively, in the geometrically unbounded periodic-tail case this follows directly from its nonzero translational drift. Heading-nonrestoring or zero-drift prescribed periods have bounded paths and hence cannot be legal on any board.

It follows that R(u,v) has empty interior and is nowhere dense. Under independent Bernoulli-p initial colors, 0<p<1, the probability of its first N distinct read constraints is at most max(p,1-p)^N. Hence R(u,v) has probability zero.

There are only countably many pairs(u,v). Consequently P, and also H, are F_sigma, meager, and Bernoulli-p null. The set of genuinely aperiodic boards X minus P is a dense G_delta and has probability one.

This is a theorem about arbitrary infinite boards, not a finite-seed counterexample. The finite-support boards themselves form a countable, dense, meager, null subset of X.

## 2. Capture is nevertheless dense

Given any finite cylinder, choose a square containing all its specified cells and the head. Make the specified black cells the only initial black cells. The independently verified four-cell exterior-completion theorem adds four black cells outside a sufficiently large protected square and forces eventual standard capture, without altering the prescribed cylinder.

Thus H is dense in X. This is an inherited application of `finite_prefix_density.md` and `../sources/kehao95-core/four_cell_port/PROOF.md`, not a new gadget.

In particular H is dense but meager. It is neither open nor closed, and is not G_delta: a dense G_delta in the Cantor board space is comeager, whereas a nonempty Baire space cannot have a set both meager and comeager.

The same conclusions hold for P. Universal finite-seed capture is perfectly compatible with all these facts: it would simply put the entire countable finite-support domain inside the dense meager null set H.

## 3. The representation changes what can be semidecided

Suppose an algorithm receives an arbitrary board only through individual cell-color queries, and halts with an acceptance answer after finitely many such queries. Its accepting transcript specifies a finite cylinder on which it gives the same answer.

Since H has empty interior, no such algorithm can soundly accept even ONE capturing board while being sound on every arbitrary board. Since H is dense, its complement likewise contains no cylinder, so no such algorithm can soundly accept even ONE noncapturing board while being sound on every arbitrary board. In particular neither property is semidecidable in this finite-query oracle representation.

There is no contradiction with the finite-seed semidecider: a sparse finite input includes the GLOBAL promise that all unlisted cells are white. An oracle transcript specifying finitely many colors does not include that promise. The exact finite-field tail verifier uses it essentially.

Nor does this prove undecidability for finitely described infinite periodic backgrounds, or for finite seeds. Those are different countable input classes with more informative representations.

## 4. Effective null covers (fair independent colors)

The aperiodicity statement can be made effective. Enumerate all pairs(u,v). Their prescribed path is computable. Its eventual geometric period either has nonzero drift after heading restoration, or is bounded; this case distinction is finite arithmetic on v. Bounded prescribed paths have empty realization sets by Section1 and can be discarded.

For the i-th remaining pair and integer n, compute its first n+i+2 distinct read cells. Their required first colors give a finite cylinder of fair-product measure 2^(-(n+i+2)); an already contradictory prefix can instead be omitted. Taking the union over i covers P with an effectively open set of measure at most2^(-n). Thus P admits a uniform effective null test. In the usual terminology, every Martin-Lof random board has a genuinely aperiodic trajectory.

The countable choices of launch pose can also be incorporated into the enumeration. This still says nothing against the finite-seed conjecture: no finite-support board is random in this sense.
