# Adjacent-defect criterion for finite-support standard capture

## Exact statement

Use white=R, black=L, flip, then move. Let F be the84 cyclic length10 factors
of the standard104-letter highway word. Define J(t)=1 when the actual turn
window ENDING at t is not in F. Actual inverse steps define windows before a
chosen entry time; finite support is preserved by any finite number of inverse
steps. Let K(t)=J(t-1)J(t), the adjacent-pair flag indexed by its right endpoint.

For every finite-support ant orbit, the following are equivalent:

1. The turn stream eventually equals a cyclic phase of the standard104 word.
2. There are only finitely many future J events.
3. There are only finitely many future K events.

The new implication is3=>1. In particular, every counterexample to the full
highway conjecture must contain infinitely many ADJACENT forbidden-ten pairs.
This does not yet force arbitrarily long consecutive bad runs, positive bad
window density, or finiteness of K on arbitrary finite seeds.

## Finite-language bridge

The recovered exact no-adjacent-J enumeration lists304,468 physically feasible
150-letter words and their270,902 length149 history vertices. All actual
no-adjacent-J tails follow the prefix/suffix graph. It has exactly three cyclic
strongly connected components:

    T24:24 vertices and24 internal edges;
    W104:104 vertices and104 internal edges;
    H:34,712 vertices and36,277 internal edges.

An infinite path in a finite directed graph eventually stays in one SCC.
T24 needs two fresh initially black ray cells per period and is incompatible
with finite support. W104 spells the standard word. Every infinite H path
has infinitely many occurrences of the12-letter marker LLLLRLRRRRLR. Removing
its995 actual history ports is acyclic; all2,747 port-to-port paths have gaps
at most74 and spell exactly the five before-marker macros C,V,U,Q,B.

Our independently checked completed-C packet theorem and exact C-free fuel
exclude every infinite finite-support physical concatenation of those five
macros. They do not require the extra port-history constraints, so apply to H
in particular. Thus T24 and H are impossible and the tail eventually enters
W104. This proves3=>1. Implications1=>2=>3 are immediate.

## Stronger one-sided corollary

The previously checked isolated-last-event theorem states:

    J(t)=1 and J(t-1)=0 imply some later J event.

Combining it with the new equivalence shows that if K(t)=0 for every t>=T,
then J(t)=0 for every t>=T. Otherwise the equivalence makes the J events finite;
the last one at s>=T would have J(s-1)=1, giving K(s)=1, a contradiction.
Equivalently, every J event is at or before a later adjacent pair: for each t
with J(t)=1, some u>=t has K(u)=1. When a last J exists, its time is also the
time of the last adjacent pair, with the right-endpoint convention above.

## Scope of quantitative control

five_macro_finite_interval_bound.md gives an explicit mass-dependent bound
for every finite five-macro factor, not just infinite-tail exclusion. It does
not bound arbitrary stretches of standard highway inside the full graph or
the total defect count of an arbitrary trajectory. A separate quantitative
corollary, isolated_defect_response_bound.md, bounds the delay from an isolated
J event to a later K event by an explicit primitive-recursive function of the
black mass at that event; it is not a universal capture-time bound.

## Sources and reproducibility

The exact source files and SHA256 values are bound in
adjacent_defect_theorem_manifest.json. The upstream graph and marker bridge
are in continuation_2026-10-22/ant_continuation/factor_language/ under the
shared project root. The new proofs and certificates are in this directory.
The packet certificate has an independent literal-word/complex-coordinate
replay, and the no-marks C-free certificate has a separate independent replay.
The upstream graph and marker bridge are independently replayed in
audits/check_no_adjacent_language_independent.py, and the isolated-event
check in audits/check_isolated_last_event_independent.py. The packet replay
is audits/check_spatial_packets_independent.py; each has a retained JSON
result listed in the manifest. No bounded search or unverified solver UNSAT
result is used in the theorem.

The global highway conjecture remains open: proving finitely many adjacent
bad pairs is the exact unresolved global step in this approach.
