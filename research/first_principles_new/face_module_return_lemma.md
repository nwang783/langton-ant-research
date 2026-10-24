# A two-return face-module lemma and sharp autonomous visit bounds

Status: independently reviewed autonomous coset-ant theorem. The alias geometry, earliest-violation trapping argument, return ledger, finite six-coset interfaces, and sharp five-group refinement passed independent analytic review and snapshot replay on22 October2026. Records are `../audits/face_module_snapshot/`, `../audits/face_module_replay.log`, and `../audits/face_group_replay.log`. This is not a theorem about standard highway attraction. A separate square-to-coset bridge is developed in `completed_fingers_and_no_interleaving.md` and is under its own audit. No appeal is made to the published four-cell-visit bound, which has a counterexample.

## 1. Abstract modules

A module of sign a (R or L) has boundary cells p,w and interior cells x,y. Its primary face is the directed four-cycle

    w --a--> x --a--> y --a--> p --a--> w.

Two child modules of sign b=opposite(a) attach at directed incoming edges w->x and x->y. Their boundary pairs are (w,x) and (x,y), respectively. All other interior cells of the two children are disjoint from each other and from the exterior. Exterior activity may change p and w between calls but cannot change x,y or any child interiors.

A call starts at w by reading a. It flips w to b and moves to x. At x, reading a advances to y, while reading b invokes child 1. At y, reading a advances to p, while reading b invokes child 2. Reaching p and reading a completes the module call. Reading b at p would be an exit through a forbidden boundary port; initially exclude such exits.

A completed return is type G if w is left in state b (its entry read was toggled), and type B if w is left in state a. These letters are just names, not cell colors.

## 2. Return-language induction

Assume each child has completed-return language among the prefixes of G, B, or GB. In particular it has at most one G return, any B is its last possible completed return, and an immediate repeated call after B cannot finish.

For a parent call to finish, every child call it makes must return G. A B child return leaves the child entry cell in color b, so the parent immediately calls that child again; that repeated call cannot finish. Consequently a finishing parent calls each child at most once, and only with outcome G.

Normalize a=0, b=1. Just before the parent call, let X,Y be the interior colors. For a finite return:

- Child 1 is called exactly when X=1, and then uses its unique G return.
- Child 2 is called exactly when Y=1, and then uses its unique G return.
- The parent outcome is G exactly when child 1 was not called, and B otherwise.
- After the return, Y=1 always, while X=0 if child 2 was called and X=1 otherwise.

These observations completely determine repeated finite returns:

- If child 2 was used on the first return, a second return would require its second G and is impossible.
- Otherwise after the first return X=Y=1. A second return requires the first G of both children. Thus the first return must have skipped child 1 too, hence was G; the second is B.
- A third return would require another G from child 2 and is impossible.

Therefore the parent's completed-return language is also contained in {empty,G,B,GB}. This is valid even with arbitrary exterior resets of the two boundary lamps between calls, provided the exterior cannot touch the interior.

For an infinite module tree, every finite alleged counterexample uses a finite depth. Induction from the deepest used modules proves the same assertion; no compactness or limiting periodicity is invoked.

## 3. Algebraic realization inside the trapped prefix region

Let G=C4*C4 and H=<R L^3>, with cells right cosets gH. See `coset_canonicalization.md` for the independent coset calculation.

Let S be reduced words whose syllable exponents are at most 2. Each such word is the unique minimum-syllable representative of its cell. There is one additional boundary cell p represented by R^3 and L^3.

The relevant group-state region is S·{R,L} together with the identity. Its only states not in S end in a syllable a^3. Write such a state as v a^3, with v ending in b. Its cell is the cell of v with its final b deleted. Indeed, multiplication by the appropriate H generator cancels a^3 and removes one b. A further a closes the a-face and returns to v; a further b produces an internal exponent 3 and leaves the region.

At the initial edge (p,1), there are two root modules of signs R and L. A module rooted at v with sign a has interior canonical addresses va and vaa, and two opposite-sign child modules rooted there. Thus its directed face is

    v -> va -> vaa -> parent(v) -> v,

where parent(v) deletes its final letter b. The root modules use the special boundary p. Different canonical addresses in S are different cells, so the required interior disjointness can be verified directly by prefixes. The overlaps of parent and child modules are exactly the stated boundary pairs.

### Explicit alias and separation lemma

For a canonical cell z in S, its only group-state representatives in the trapped region are:

- z itself;
- z R L^3, when zR lies in S;
- z L R^3, when zL lies in S.

For the special predecessor cell, they are exactly R^3 and L^3. This follows directly from the coset normal form: a noncanonical trapped state must end in a^3, and its canonicalization deletes that syllable and the final opposite letter of its prefix. Conversely the two displayed aliases reduce to z under multiplication by the appropriate generator of H.

In particular, all aliases of an ordinary interior cell retain its full canonical prefix. Exterior branches cannot modify it without first leaving the trapped region. In a module rooted at v with sign a, the predecessor cell parent(v) occurs in that branch only at v a^3. Thus it is untouched until the last boundary read. This establishes the interior/exterior separation used by the return table.

## 4. First-exit strategy for proving trapping

Start at a directed edge whose two endpoint lamps have the same color. Root the module region there. Every ordinary entry into a module has its boundary predecessor p in the module's sign a: the preceding opposite-sign turn at p has just flipped p to a. This is also true for the initial root entry.

The only exception is immediate re-entry after a B return of the same module. That return leaves w=a and p=b, so the ant immediately tries the same module with mismatched boundary colors.

Consider a first escape from the prefix region. It must occur at a module's last boundary p, by reading b instead of a. Since p is untouched during a module call until this last boundary, the call must have started with mismatched boundary colors. Hence it was an immediate re-entry after B.

A more precise first-violation argument closes the apparent recursive gap. Consider the earliest event of either kind: (i) an escape through a wrong last-boundary port, or (ii) a module's completed-return sequence first ceasing to be a prefix of G, B, or GB. All child returns strictly preceding that event have valid sequences. During any call that reaches its last boundary, a child B return cannot occur: the child entry lamp still requests that same child, and any subsequent child return would violate its sequence before the parent's event; an escape inside it would also occur earlier. Hence every used child returns G once. The exact interior-state table in Section 2 therefore applies also to arrival at the last boundary, before reading it.

The table excludes an arrival after a previous B, and excludes all completed-return sequence violations. A wrong last-boundary port, however, can only arise after immediate re-entry following B. Both types of earliest violation are therefore impossible. This proves trapping and the return ledger simultaneously, using the stated module/cell identification and exterior-interior separation.

The algebraic geometry and first-violation argument have now passed independent review. This argument alone does NOT prove that every square-ant word is legal for the autonomous coset ant; that is the separate projection bridge.

## 5. Initial coarse consequences of the trapping realization

Each module has at most two completed returns and therefore at most three entries (the final entry may never return). Each canonical interior group state is reached either by one parent-face entry or by a child-module return. Thus it is visited at most 3+2=5 times. A group state ending in exponent 3 is the last boundary of one module, and is visited at most twice. The root group state has at most one initial visit plus four module returns; in fact the return types improve this to four, since a B return immediately launches a nonreturning call.

Each coset represented by a canonical S-word has at most three group-state representatives in the trapped region. Hence the coarse bound 15 visits per coset is immediate; using the terminal-state bound gives 5+2+2=9. These bounds are deliberately not claimed sharp. Experiments suggest the sharp coset bound is six.

Any coset-ant orbit has a color-change in its turn stream within its first five letters: four equal turns return to the starting cell, whose color has flipped. At the first turn change, the previous and current cells have equal colors, so rebasing gives the trapped situation. This yields a safe global bound of six visits per group state and ten per cell (at most one earlier visit to any state/cell before that first change). The sharper five/six global bounds require a little more case accounting and are not used here.

## 6. Remaining projection gap

The square ant flips one projected lamp. An autonomous coset lift flips only one coset lamp. Different cosets can project to the same square cell. Therefore a legal square word need not be declared legal for this model without proving the relevant parity/inclusion theorem. Likewise a finite square seed can lift to infinitely many nonwhite cosets. Even a completely audited uniform lift-visit theorem would establish properness in the symbolic lift, not standard highway attraction on the square lattice.

## 7. Finite interface certificates for the sharp six-cell bound

The coarse bounds above can be sharpened without enumerating ant trajectories. `check_six_cell_bound.py` keeps one parent face and its two children explicit, and replaces the four grandchildren by arbitrary interfaces with completed-return language {empty,G,B,GB}. Those deeper interiors cannot touch either tracked parent interior cell, so this is an overapproximation, not a depth cutoff. It exhausts the64 local initial interior color assignments and permits arbitrary exterior resets of the parent boundary lamps between calls.

The maximum total reads of either tracked interior cell is six. If its initial lamp is opposite the sign of the parent face, the maximum is five. `check_root_cell_bound.py` similarly keeps the two root faces explicit and treats their four children as interfaces. It finds at most five reads of the canonical root cell and three of the special predecessor.

These are exhaustive finite interfaces whose correctness is conditional only on the module return/separation lemmas, not on an empirical visit cutoff.

Finally, before the first turn change there are at most four identical turns a, at distinct cells. Rebasing at the change b=opposite(a), the previously read cells are among the root, the special predecessor, and the two interior cells a,a^2 of the root a-face. The latter cells, when previously read, have lamp b, opposite that face's sign, and therefore have at most five remaining reads. Each previously read cell has just one earlier read. The root has at most five remaining reads, and the predecessor at most three. Hence the resulting global bound is **six visits per coset cell**. The existing six-visit witness makes this bound sharp for the autonomous coset model.

This sharp-bound extension passed independent audit of its finite interface implementation and initial-prefix accounting. By itself it does not remove the square-to-coset legality gap or the projection-to-highway gap.

## 8. Sharp five-group-state bound

The same finite interfaces can count canonical group states rather than coset cells. A tracked canonical interior state is read either directly on its parent face or as the entry root of its own opposite-sign child. Reads of that physical coset as a descendant's last boundary are aliases and must not be counted as the canonical group state.

`check_five_group_bound.py` is the Section7 interface with exactly this marking. The maximum canonical-state counts at the first and second parent interiors are respectively4 and5. Conditioned on initial color [same as parent face, opposite], they are [[4,4],[5,4]]. `check_root_group_bound.py` similarly gives at most4 reads of the canonical root group state, excluding all last-boundary aliases. States ending in exponent3 are last boundaries of a unique module and are read at most twice.

Before the first turn change, the distinct earlier group states, in the rebased coordinates, are among the root, a^3, a, a^2, where a was the original repeated turn. The two canonical interior states a,a^2, when present, start the rebased suffix with lamp opposite a, giving at most4 subsequent canonical-state reads. The root gives at most4, and the a^3 state at most2. Adding the single prior read yields the global bound **five visits per group element**, for arbitrary initial coset lamps. The known 37-letter witness attains five. This sharpening and its canonical-state marking passed independent review and snapshot replay; see `../audits/face_group_replay.log`.
