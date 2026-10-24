# Exact integer transverse transport in the low zone

Status: proposed effective compiler lemma, pending independent analytic review.
No semilinear-profile implementation or ant record exclusion is claimed.

Use the signed exact-low setting of exact_low_excursion_summary_lemma.md: a fixed
finite packet DFA, fixed global height/transverse coordinates, and a cutoff below
all tracked high residual effects and record constraints. Fix any entry and exit
ports, including their exact finite boundary depths.

For c in{0,1,2,3,4}, let T_c be the set of INTEGER transverse displacements of
finite genuine low packet-DFA paths between the two ports, where c<4 means exactly
c C macros and c=4 means at least4 C macros. Then every T_c is effectively
semilinear in Z. In particular membership and emptiness, as well as intersection
with any specified Presburger displacement condition, are decidable. At a fixed
integer displacement delta, the greatest feasible saturated age is the maximum
c with delta in T_c; if it exists, some finite low path attains it.

Proof. Expand the actual packet transitions into private unit counter chains as
in the signed low compiler. Label each unit transition by its own distinct
terminal symbol, and attach the packet's integer transverse displacement to one
unit edge,0 to its other private edges. The language of actual finite graph walks
between the fixed ports whose counter never becomes negative is context-free:
a one-symbol pushdown automaton tracks the counter, with private finite chains
preserving whole-packet chronology. The fixed initial/final depths are compiled
by fixed pushes/pops. A five-state saturating C counter in the finite control
selects exactly the c class without changing context-freeness.

Effective Parikh semilinearity yields the finite union of linear sets of edge
multiplicity vectors for that context-free language. The integer linear map
sending an edge multiplicity vector to the sum of its attached transverse
weights maps each such linear set to an integer linear set. Its union is exactly
T_c: order is not being guessed, because each admitted multiplicity vector is
certified to have at least one genuine word in the original low-path language.
This gives the claimed effective representation, including negative offsets.

Primary constructive reference: Javier Esparza, Pierre Ganty, Stefan Kiefer and
Michael Luttenberger, “Parikh's Theorem: A simple and direct automaton
construction,” Information Processing Letters111(12),614–619(2011),
https://arxiv.org/abs/1006.3825 . Their construction effectively produces a finite
automaton with the same Parikh image as a supplied context-free grammar.
The original theorem is Rohit J. Parikh, “On Context-Free Languages,” JACM13(4),
570–581(1966), https://doi.org/10.1145/321356.321364 .

The maximum c is finite and attained: it is chosen from the five nonempty class
queries, not a supremum over an unrepresented limit. To recover an actual witness
at an admitted integer displacement, enumerate finite low graph paths until the
exact port/displacement/C-class test succeeds; membership ensures termination.
No efficiency bound for this brute recovery or general grammar compiler is
asserted here.

## Consequences and limits

1. Modulus-M summaries are projections of these exact sets. For residue r,
   query T_c intersect{delta:delta congruent r mod M} and keep the greatest
   feasible c. Thus changing M is not a fundamental mathematical obstruction.
2. A finite transverse-band abstraction can compile a ONE-STEP low summary by
   checking the Presburger condition: there exist actual source t in band B and
   delta in T_c such that t+delta lies in band B', together with any required
   residue constraints. The maximum permitted c is again attained by a genuine
   path and source t. Composing such abstract band steps can still lose the
   hidden exact t; no global exactness beyond the concrete relation is claimed.
3. The signed sufficient complete-context cutoff makes retained patch colors
   literally unchanged during these low paths. Any other metadata must still be
   updated exactly or conservatively abstracted. The theorem does not preserve
   unexamined nonmonotone effects.
4. This compiler does not solve the unbounded spatial high-token ledger, prove
   finite-seed capture, or exclude either remaining V1/U1 record case. It says
   only that exact low integer transport is effectively Presburger, rather than
   inherently limited to a finite transverse modulus.
