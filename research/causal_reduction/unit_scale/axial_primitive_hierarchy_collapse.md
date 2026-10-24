# Arbitrary finite decorations of the supplied axial primitive collapse to rays

23 October 2026, 14:56 UTC. Author structural consequence of complete local certificates, independent review requested. This is not a theorem about arbitrary axial bodies, arbitrary nonstationary directives, or general decorated substitutions.

## 1. Exact alphabet and wrapper

The sole nonidentity physical primitive is

    W = RRLRRRRLRLLRLLRLL = U R V,
    U = RRLRRRRL, V = LLRLLRLL.

For an R state of any incoming heading, use the properly rotated W; for an L state use the turn-complemented W at the same incoming heading. These preserve the exact single-read endpoint pose. Complementation here means only a reflected finite read contract, not a complement of an infinite background.

Allow ANY finite number of decorated physical-read states. Each is either a literal identity mapping to itself, or has an image of exactly17 decorated states whose physical word is the specified primitive for that state's physical type. Decorations can depend arbitrarily on the parent, and image children can refer to any states of the appropriate physical type. There is no bound on the number of states or hierarchy depth. One-letter aliases that later activate, other nonidentity words and varying directives are not part of this alphabet.

For the wrapper allow a special root a with any finite physical base word A and image a w. The fixed typed word w uses only these decorated read states, is closed at the endpoint pose of A, and contains no a. All unit images preserve pose. The growing rooted path is therefore

    A w phi(w) phi^2(w) ... .

If any nonidentity state is reachable from w, this rooted path cannot be an ant trajectory on ANY board. If all reachable states are identities, the root merely repeats a fixed closed word, also impossible by finite-domain escape.

## 2. Complete local child classification

Call a state active precisely when its image has length17. For a canonical N-R active state, inspect its depth-two image: at each of the17 child slots, either retain the literal read (identity child) or expand the child's one physical primitive (active child).

The complete binary classification has exactly these legal active-slot sets:

    empty, {8}, {11}.

The retained certificate has38 disjoint conflict-prefix cubes plus these three singleton survivors, covering all2^17 assignments. Each conflict cube comes with a repeated equal turn at one cell in a prefix determined solely by the cube. Thus every member of the cube is illegal on every board. The three survivors have lengths17,33,33. Proper rotation and local reflection/turn-complement preserve equal-turn conflicts and exact unit poses, so this applies to all eight physical types.

Consequently the directed active-child graph of ANY legal decorated controller has outdegree at most one. A branching hierarchy is already forbidden locally, with no bound on its depth.

## 3. A perpendicular edge can occur only at the top

For the canonical W, slot8 has physical type N-R at position(2,0), while slot11 has type W-R at(2,1). Once each active state has at most one active child, a depth-three chain is specified by two indices i,j in{8,11}. The exact49-read controls are:

    (8,8): legal;
    (8,11): conflicting L reads32 and44 at(2,2);
    (11,8): legal;
    (11,11): conflicting L reads35 and47 at(0,1).

Therefore no active state that is itself an active child may place its own active child at slot11. Along every active chain, slot11 can occur only as the FIRST edge. Every subsequent edge must be slot8, or the chain terminates. This conclusion holds even if the finite state graph has cycles or different decorations at every vertex.

Every state reachable from the actual fixed root occurs in a fixed finite root power. All of its later images are contiguous factors of longer genuine rooted prefixes. Thus the depth-two and depth-three requirements apply to every reachable active state; they are not assumptions that isolated replacement levels are separately realized without a root.

## 4. Eventual form of every component

A terminating active chain has a bounded physical expansion and eventually becomes one fixed finite word, regardless of its decorations.

An infinite active chain with only slot8 edges has the same physical words as the original axial hairpin:

    phi^r(s) = U^r c V^r,

with the appropriate proper rotation or local reflection for its physical read c. The labels along the chain may vary, but slot8 preserves the physical type, so this formula is exact.

If the first edge is slot11, write the outer W as P c' S at that slot. For r>=1 its expansion is

    P U'^(r-1) c' V'^(r-1) S,

where primes denote the primitive for the perpendicular child type. P and S are fixed literal words. This is again one supplied axial hairpin at one fixed center, with fixed work before and after it, not a moving two-dimensional hierarchy. A terminating version is bounded instead.

Thus, for all sufficiently late wrapper layers phi^r(w), every occurrence is either fixed work or one of finitely many supplied axial hairpins at fixed centers. The depth is r or r-1; a fixed offset in depth changes only the finite threshold at which a remote column becomes interior.

## 5. Existing fixed-ray potential closes the wrapper

Apply the independently signed parallel_axial_hairpin_wrapper_obstruction.md and fixed_ray_axial_hairpin_wrapper_addendum.md to that eventual decomposition. Choose any occurring ray and properly rotate it to the positive x direction. A sufficiently remote column misses the finite fixed work, all opposite rays and all perpendicular fixed-center rays. Every remaining legal hairpin reaching that column transfers one black cell down by four rows and hence lowers the same bounded column-height moment by4. Reflected/complemented copies have the same transfer orientation, as independently signed in the addendum.

An infinite number of late closed layers cannot continually lower that bounded potential. Overlapping components either create an earlier literal conflict or contribute their exact complete changes additively. Arbitrary charge in A or w cannot supply a correction at the chosen remote column.

If no infinite active chain remains, all late layers are one fixed finite closed word. Their infinite repetition stays in a finite footprint and contradicts finite-domain escape. This covers terminating decorations as well as recurrent ones.

The new content is the collapse of arbitrary finite decorations and hierarchy depth over this ONE primitive to the already signed ray obstruction. It does not infer a general no-go for moving emitters, other axial operators, alias-delay controllers, arbitrary control graphs, or directives.
