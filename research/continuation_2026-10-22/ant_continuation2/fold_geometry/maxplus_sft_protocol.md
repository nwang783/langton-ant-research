# Exact finite-field verification of directional max-plus potentials

Date: 22 October 2026. This describes a complete verifier for a proposed invariant, not a successful invariant. The searches recorded beside this note have returned counterexamples or reached explicit computational caps. No conclusion of impossibility follows from a capped search.

## Potential and its intended consequence

Let P_z(B) be the 3 by 3 bit pattern centered at z, with the bottom row in bits 0,1,2, the middle row in 3,4,5, and the top row in 6,7,8. For integer pattern weights w_1,...,w_511 and heading weights c_0,...,c_3, define

\[
\Phi(B,p,h)=\max\left(p_y+c_h,\;\max_{z:P_z(B)\ne0}\{z_y+w_{P_z(B)}\}\right).
\]

The all-white pattern is excluded. Thus Phi is finite for every finite black field, including an empty field because the head term remains.

The final extension replaces c_h by c_(s,h), where s is the actual normalized 149-letter history port. A transition from port s to t uses the corresponding source and target head constants. There are 995 ports and four physical orientations, hence 3,980 head variables. Every argument below is unchanged after making these source/target substitutions. In particular, the finite height interval uses U=-c_(s,h) and the final-heading term c_(t,h').

A certificate would prove Phi does not increase under every permitted macro transition, in all four orientations and on every finite surrounding field. Vertical translation adds its displacement to Phi, so integer sublevel zero suffices to check every sublevel.

Let m be the minimum of w_1,...,w_7. For a finite nonempty field whose top black height is Y, a patch centered at height Y+1 has a nonzero bottom-row-only mask. Therefore

\[
\Phi\ge Y+1+m.
\]

The head term similarly bounds p_y. Rotating the entire physical problem through the four cardinal orientations would give a bounding rectangle for every macro port, because the proposed inequalities are checked for all macro orientations. The fixed finite macro footprints would then bound all intervening reads. Since each of the five before-marker macros increases black mass (respectively 3,4,4,6,6 for C,V,U,Q,B), an infinite such trajectory in this fixed rectangle is impossible. This explains why a successful certificate would close H; no such certificate has yet been obtained.

## Sublevel zero is exactly a finite-height column language

Put

\[
\ell=-\max_{1\le P\le511}w_P,
\qquad u=-1-\min_{1\le P\le7}w_P.
\]

The coercivity argument above shows that Phi<=0 forces every black cell above row u to be absent. A patch centered at y<=ell automatically has y+w_P<=0, for every nonzero P. A patch centered at y>=u+2 is all-white. Consequently the field part of Phi<=0 is exactly the following condition:

* Every black cell above row u is absent.
* In rows ell,...,u, every consecutive triple of columns satisfies the 3 by 3 inequalities at center heights ell+1,...,u+1.
* Cells below row ell are unrestricted.

Each column in the restricted strip is a symbol in an alphabet of size 2^(u-ell+1). The restrictions concern three consecutive column symbols, so they define a finite directed graph with two-symbol states. An edge (a,b)->(b,c) exists exactly when the triple (a,b,c) satisfies every vertical patch inequality.

Finite fields correspond exactly to paths that start at the all-zero state (0,0), eventually return to (0,0), and otherwise have finite length. Trimming the graph to states reachable from (0,0) and able to reach (0,0) therefore quantifies exactly over finite surrounding fields. It does not silently replace them by arbitrary nonextendible local patches or by infinite periodic backgrounds.

The implementation generates triples row by row and rejects a partial triple immediately when its completed 3 by 3 patch violates a threshold. This is exhaustive integer enumeration with pruning; it makes no statistical assumption.

## Exact macro check

A physical template consists of fixed initial black and white cells, its odd-visit toggle set, and its final pose. The basic templates are the five before-marker words. The conditioned templates use the after-marker words together with the endpoint colors forced by an actual 149-letter history. All first-read colors of the future macro are retained explicitly, so every returned counterexample can also be checked by literal ant execution.

Fix a template, an orientation h, and an initial head height y0. Precondition Phi<=0 requires y0+c_h<=0. A required black cell above u makes the precondition impossible. Required colors in the restricted strip impose bits on finitely many columns. Required colors below the strip do not affect membership in the sublevel set and can be supplied literally in the finite witness.

The toggle set gives a fixed XOR mask for each affected strip column. A toggle above u creates a black cell above the certified strip, because the precondition forces that cell white. Otherwise the field postcondition fails exactly when a post-toggle triple is forbidden in the column graph. The head postcondition is checked separately.

For the finitely many columns containing a fixed strip bit or a strip toggle, expand the interval by two columns on both sides. A dynamic program begins in every trimmed graph state, follows every legal pre-field edge subject to fixed colors, and records whether any transformed post-field triple is forbidden. Every exit state is extendible back to zero by construction. The two-column margin contains every triple changed by a toggle. Thus a surviving bad flag is equivalent to a finite-field counterexample; no violation can hide outside the interval.

If a bad path exists, the program appends explicit graph paths to and from zero, adds the required black cells below the strip, then independently computes both full finite-field potentials and executes every ant step of the macro. The resulting JSON therefore contains a concrete finite coloring, rather than only a local satisfiability assignment.

## Why only finitely many head heights are checked

Let t be the largest relative y coordinate of an odd toggle, and let d_y and h' be the oriented final displacement and heading. Put

\[
L=\min(\ell-t,\;1-d_y-c_{h'}),\qquad U=-c_h.
\]

For y0<L, every toggle lies strictly below the restricted strip and the final head term is at most zero. Such a transition cannot leave sublevel zero. For y0>U, the initial head already violates the precondition. The inclusive finite interval L,...,U therefore covers every remaining case.

## Exact case deduplication

At a fixed candidate, two cases are identical for this decision problem when their required strip-column bits and toggle-column masks agree up to horizontal translation, and their above-strip-toggle and final-head-failure flags agree. Required lower colors are unrestricted by the sublevel and can always be filled separately. The verifier checks one representative per such exact signature, counts all covered cases, and retains one literal counterexample when appropriate. The equivalence is specific to the current candidate; signatures are rebuilt after every refinement.

## Refinement and limits

Every returned finite counterfield yields the exact inequality

\[
\max_j(w_j+b_j)\le\max_i(w_i+a_i),
\]

where repeated pattern types are represented by their highest center and head types by the head height. The refinement monotonically lowers violated post weights and rechecks all retained finite inequalities. Adding a common constant to every nonzero-pattern and head weight leaves all transition inequalities unchanged, so normalization is harmless.

A stable fit to retained witnesses is only a candidate. A theorem requires a subsequent complete SFT verification with no counterexamples. Conversely, failure to converge or an explicit strip-size/pass cap does not prove that the ansatz is impossible. The scripts preserve those statuses separately.

Files:

* `verify_maxplus_sft.py`: exact verifier, including finite witness reconstruction and literal checks.
* `refine_maxplus_sft.py`: counterexample-guided candidate refinement.
* `export_full_history_contexts.py`: complete after-marker history colors for all 2,702 retained physical edges.
* `maxplus_sft_verification.json`: explicit refutations of the initial sampled candidate.
* `maxplus_sft_refinement.json`, `maxplus_sft_refinement2.json`: capped unconditioned searches.
* `maxplus_conditioned_sft_refinement.json`: capped search using the older 166 truncated contexts.
* `maxplus_full_history_sft_refinement.json`: full-history search record; its machine-readable status determines whether the run completed or stopped.
* `maxplus_port_head_sft_refinement.json`: capped full-history search with port-dependent head constants.
* `maxplus_last_port_candidate.json`: the last separated port-dependent candidate and its literal finite counterfields.

All listed searches are now stopped without a valid invariant. The all-parameter family in `arbitrary_lookahead_obstruction.md` proves that the final tested candidate still fails after arbitrarily long finite H futures.
