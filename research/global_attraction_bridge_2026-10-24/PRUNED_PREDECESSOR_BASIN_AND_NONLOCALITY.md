# Exact pruned preimages of the canonical basin, and a fixed-mass locality obstruction

24 October 2026. AUTHOR theorem and bounded complete controls. Independent audit requested. This is a structural inverse interface and a literal countercontrol to a local inverse-branch mechanism, not a proof of basin coverage.

## 1. The new target and the retained control

The question is whether reversibility and backward images of capture certificates supply a locally checkable invariant of the basin complement. The ant itself is reversible, but its ENTIRE future-relevant pruning is retrospective. These are different statements.

The already retained four-cell exterior-completion theorem, and `../computability/finite_prefix_density.md`, show that every finite legal observation has a finite-seed canonical completion with at most four additional black cells. That density theorem is not claimed anew here. It already prevents a robust finite-prefix noncapture certificate. The sharper question below is whether the inverse law becomes local AFTER passing to complete future-relevant states.

We give the exact inverse law, an effective ancestry parametrization of the canonical basin, and an all-parameter family proving that its branch condition cannot be recovered from any fixed-radius observation of the actual full board, even with fixed initial mass and a uniform bound on the ENTIRE relevant population.

## 2. Full reversibility versus the pruning quotient

A complete finite state is X=(B,p,h), with headings N,E,S,W numbered0,1,2,3 and unit vector v_h. Let F(X) be one actual ant update. If X is a post-update state, set r=p-v_h. Its unique FULL predecessor is

- if r is BLACK in B: (B minus {r},r,h-1), with an R update;
- if r is WHITE in B: (B union {r},r,h+1), with an L update.

All heading arithmetic is modulo4. This is local and single-valued. No reversal is treated as a physical routing trick, and no sector is changed without changing the actual pose as displayed.

Write C*(X) for current black lifetimes that are eventually read, including the current update. A pruned state (C,p,h) means that every cell in C is actually read in its complete future, so C*(C,p,h)=C. Write W(C,p,h) for the complete future READ set, not just black inputs.

Any complete finite board with this exact pruning is C union A, where A is finite and disjoint from W(C,p,h). Conversely every such A is forever unread and gives that same future and pruning. This is the exact one-time deletion coupling; it retains A as a real field rather than physically erasing it.

## 3. Complete predecessor law in the pruning quotient

Fix a pruned target (C,p,h) and put r=p-v_h. The following are ALL possible pruned predecessors of complete full states whose target pruning is C:

1. If r belongs to C, there is exactly one class:

       (C minus {r}, r, h-1), previous relevant R.

   The update writes the future-consumed r, so its complete post-update field can contain C plus arbitrary unread archive.

2. If r does not belong to C, there is always the class

       (C union {r}, r, h+1), previous L.

   The added original input at r is consumed immediately.

3. In case2 there is a second class IF AND ONLY IF r is not in W(C,p,h):

       (C, r, h-1), previous permanent R.

   The update creates BLACK r, but that new lifetime is never read again.

Proof: apply the unique full inverse from Section2 to every permitted target C union A. If r is in C, it is necessarily black. If r is absent from C but is later read, it cannot belong to unread A, so it must be white. If r is never read, both its white and black target values are permitted. Other archive bits are never read at the single predecessor update, whose head is r, nor in the target future. Thus they do not enter the predecessor pruning. Each displayed class is realized by its finite pruned predecessor board: its post-update full board is either C or C union {r}, and all predecessor black cells are actually consumed. This proves both sufficiency and exhaustion.

The two branches in case3 are NOT two inverses of the same full board. Their post-update full boards differ at r. The branch condition is a NEVER-READ condition on the complete future, not the weaker condition r not in C. If r is first read WHITE later, only the L branch is allowed.

## 4. Canonical-root ancestry is effective, but coverage is not proved

For a fixed infinite future word, C* is exactly the sites whose FIRST future read is L. The signed standard104 word consequently has104 distinct normalized pruned phase states, with heading normalized to N by genuine quarter-rotation and head translated to0. The checker reconstructs these from the fully certified G future; their relevant masses range from11 to22.

For a canonical root or any finitely prepended valid ancestry, the complete future is an explicit finite prefix plus a canonical104 ray tail. Membership in W is decidable by a finite prefix search and exact integral ray intersections. Therefore the predecessor law can be recursively applied without any new capture assumption.

The resulting unfolded ancestry graph parametrizes exactly the canonical-capturing pruned finite states, up to actual translations and quarter-rotations:

- Every generated node has a complete future certificate by prepending its verified single update.
- If an arbitrary full state captures canonically, take a later actual104 cut, prune that cut to its phase root, and follow its actual finite past backward using the exhaustive law. Its initial pruning occurs as an ancestry node.
- A full board X captures if and only if X equals some generated node C plus a finite archive A disjoint from that node's whole future read set, at the same pose.

This is an explicit basin parametrization, not a proof that every finite board belongs to it. The normalized graph can contain repeated nodes, including the natural104 phase cycle; no well-founded rank or decreasing mass is inferred. The algorithm carries a known complete future at every generated node. It is not an algorithm for pruning arbitrary unknown futures.

The104 roots have the following exact predecessor-type inventory:

    46 unique relevant-R roots;
    36 unique L roots;
    22 double L/permanent-R roots.

All126 displayed predecessor branches are physically replayed for their first update, their full successor fields pass exact infinite-tail parity, and every listed predecessor black bit is verified relevant. These finite counts are an auditable interface, not a proposed exhaustive search of the basin complement.

## 5. A same-mass, arbitrarily-large-local-agreement obstruction

Let G={(0,-1),(1,1),(1,3),(2,2)}, head(0,0), heading E. Its complete reference future stays in x>=0 and captures into its signed standard tail. Define, for every EVEN n>=20,

    P_n = G union {(-n,j): 0<=j<16}.

All sixteen added bits are forever unread. This is an actual complete20-black input, not a cropped reference field.

Let Q_n be the signed twenty-cell five-port circuit, with G placed at poses

    (0,0), E;
    (n-1,n), N;
    (-n,3n-4), W;
    (-5n+5,-n), S;
    (-3n,-3n+8), E.

The complete retained stage separation, protected90 field and all-future closure apply to every even n>=20. In particular the entire future-relevant population is at most132 at every cut. The P_n reference has the stronger all-time bound22. Both seeds have EXACTLY20 black cells.

At the common cut61:

- Both trajectories have exactly the same first61 turns and pose p=(0,3),h=N.
- Both full fields have EXACTLY31 black cells.
- Their full board colors agree on the entire closed head-centered L-infinity box of radius n-3.
- The nearest differing cell is at distance n-2. This is an exact affine bound for all n, not extrapolation from samples.
- The preceding head cell is r=(0,2), and BOTH actual full histories just wrote it by the same R60 update.

Nevertheless their pruned target states have different inverse degrees:

- For P_n, R60 is permanent. Its cut61 pruning has11 cells and omits r. The entire future misses r. Therefore it has TWO pruning-quotient predecessor classes, L and permanent R.
- For Q_n, R60 is consumed at e=624n-1516. Its cut61 pruning is the ENTIRE31-cell full field, hence contains r. Therefore it has exactly ONE pruning-quotient predecessor class, relevant R.

For each proposed finite observation radius R, choosing even n>R+3 gives two genuine finite20-black histories with identical full local observations, identical actual cursor and prefix, identical total cut mass31, and a common all-time whole-relevant cap132, but different exact quotient branch degrees. Thus no fixed-radius local rule on the full board, even with these mass/cap data, can implement the exact pruned predecessor law.

This does not contradict full reversibility: their FULL predecessor is uniquely the R branch in both cases. It shows that the attempt to simplify inverse basin geometry by removing forever-unread archive imports genuinely nonlocal future information. It does not refute an orbit-dependent radius or a rule supplied with the actual complete C* oracle.

## 6. What remains a global obligation

No capturing member of this family avoids every backward image of capture. These are countercontrols to a proposed LOCAL inverse-branch mechanism, not noncapturing examples.

The basin complement, if nonempty, must lie outside the exact ancestry parametrization, but saying that alone is tautological. A useful global argument would need an independently controlled resource or geometry restriction on the repeated never-read/read distinction. Neither bounded relevant population nor arbitrarily large local agreement decides that distinction, as Section5 proves. The known rho(t)->infinity alternative for nontranslation remains separate, as does uniqueness of attainable translating tails.

The retained finite-prefix density theorem also prevents promoting a finite observed avoidance prefix into a noncapture certificate. None of this proves noncapture unrecognizable or undecidable: the complete finite-input encoding includes the global all-other-cells-white promise, and a valid noncapture invariant could use it.

## 7. Verification boundary

`check_pruned_predecessor_basin.py` reconstructs all104 roots and126 inverse branches. It independently forms the literal P_n and Q_n seeds for n20,80,400, simulates their complete prescribed finite futures, and verifies infinite tails against every retained black cell. It checks the16 symbolic affine exclusion witnesses for the remote Q_n bits. The all-n lifetime and relevant-cap premises are inherited from `TWENTY_CELL_RELEVANT_STOCK_AND_OUTPUT.md` and its signed sources, not inferred from the three literal controls.

The four-cell one-sided future is checked by its entire finite prefix and the positive x drift of every later104 ray. No remote bit is omitted from the literal terminal fields or assumed harmless from its distance alone.
