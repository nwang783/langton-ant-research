# Exact symbolic full-field guard for a capped first-return word

24 October 2026. Author theorem and CNF implementation pending independent
audit. This is a fixed finite-word reduction, not a global ant decision
procedure. No external SAT solver outcome is asserted.

## Theorem

Fix a finite nonempty turn word w of length L, an integer cap M>=0, and the
normalized initial head (0,0),north. One can construct a finite Boolean formula
Phi(w,M), with O((L+1)(M+1)^3) gates, such that:

1. Every complete board on which w is an empty-active-to-empty-active FIRST
   return with active w mass at most M at every cut supplies a satisfying
   assignment to Phi.
2. Every satisfying assignment extends to a FINITE complete black board on
   which the actual standard ant realizes precisely that capped first return.

The same physical cell uses ONE initial-color variable at all time cuts. Exact
visit parity determines every later color. Neither a separate board per cut
nor erased passive archives are permitted.

## 1. Local detection of a globally defined active component

Work in the fixed square w lattice selected by initial pose (0,0),north. For a
root vertex r let B_M(r) be its graph-distance ball of radius M. Let E_M(r) be
all edges with at least one endpoint in this ball. It has O((M+1)^2) edges.

Using only their color bits, compute by M layers of Boolean reachability which
vertices are connected to r by a black path of length at most M. Mark an edge
in E_M(r) if it is black and has a reached endpoint. Let N_M be the number of
marked edges. Then, even on an infinite exterior,

    |the COMPLETE black component at r| <= M   iff   N_M <= M.

Proof. If the complete component has at most M edges, every vertex in it is
reachable by at most M edges, and exactly all its edges are marked. Conversely,
if the component has at least M+1 edges, grow any rooted connected edge set one
edge at a time until it has M+1 edges. Before the j-th edge is added, one of its
endpoints is connected to r by a path of at most j-1<=M edges. Thus all M+1
chosen edges are marked. Every one lies in E_M(r), so N_M>=M+1. This proof also
covers an infinite component and does not need a blank exterior.

Reachability inside B_M(r) is exact for paths of length at most M: such a path
cannot leave that graph-distance ball. Edges to distance M+1 are included in
the marked-edge count. Omitting these boundary edges would be an error.

## 2. Shared cells, actual flips and first return

The word determines every head pose (p_t,h_t) and root r_t. Give each physical
cell appearing in any E_M(r_t), endpoint port guard, or actual read its one
initial Boolean variable x_q. At cut t use the literal

    b_t(q) = x_q XOR (number of reads of q before t mod2).

For each prescribed R require b_t(p_t)=0, and for L require it to be1. The turn
and move rules then inductively force the actual head to follow the prescribed
word. The implementation maps each w edge back to its unique physical cell,
so two cuts cannot silently use different variables for the same cell.

At cuts 0 and L require all four edges incident to r_t to be white, exactly the
empty-component condition. At every interior cut require at least one black
incident edge, exactly the nonempty-component condition. At every interior cut
also impose N_M<=M from section1. Endpoint caps follow from emptiness.

These requirements are exactly capped FIRST return, not merely ending at an
empty state after possibly earlier empty visits.

## 3. Both directions and finite extension

Given an actual capped first return, set each x_q to its actual initial color.
Its actual read parity satisfies every turn requirement. Its complete active
components satisfy the local cap equivalence and endpoint/interior guards.
Thus the reachability and counting gates have a satisfying assignment.

Conversely, take a satisfying assignment. Set exactly its true input cells
black and EVERY unmentioned cell white. This is a finite board. The shared
read-parity constraints force the stated head path and every color read.
The local component equivalence proves the cap on the COMPLETE board at every
cut, not merely on a truncated active view. The incident-port guards prove the
first-return conditions. There is no hidden outside connection: any component
with more than M edges would already have exposed M+1 marked edges in one of
the included local neighborhoods. In fact ANY exterior assignment matching
the represented cells leaves these finite-time cap/read conclusions valid;
choosing all white is simply an explicit finite-support witness.

## 4. Size and checkable implementation

Each cut has O(M^2) local vertices/edges, M reachability layers with bounded
fanin, and an at-most-M sequential counter of O(M^3) gates. Tseitin equivalences
turn every gate into a bounded number of clauses. Sharing physical input bits
across cuts reduces rather than enlarges the bound. The formula size depends
on L and M, not the number of normalized kernel profiles spelling w.

symbolic_capped_word.py constructs the circuit, DIMACS CNF and physical input
map. It has no SAT solver. A proposed satisfying assignment must satisfy every
CNF clause, then verify_model extracts the FINITE seed and replays the literal
full board, checking every complete active component and first-return cut.

A future UNSAT claim must include a separately checkable proof such as a
resolution/LRAT certificate; an opaque solver status would not be accepted.
The controls include only direct assignment equivalence tests, positive models
with complete finite-board replay, and a simple explicit contradictory-unit
regression. They do not claim UNSAT for an untested candidate word.

## 5. Relation to the cap-seven boundary

The bounded-core cap-seven kernel has 154,794,412 local profiles but projects
to just 58 words of length at most25. That quotient is only a discovery layer:
full component information is NOT retained by the word alone. Phi restores
that information through exact shared-cell reachability and boundary guards.
It offers a compressed route to full-field consistency for each word without
materializing its profiles. Satisfiability for these finite words would still
not decide infinite continuation, module transport, or standard104 capture.
No cap-seven exit theorem or usable infinite compiler is inferred here.

## 6. Frozen model and regression outcomes

The author checker compares the CNF with literal complete-board execution on
922 specified initial assignments, including all512 subsets of a3x3 patch for
one fixture, four further deterministic random fixture families, far unread
archives and long attached-component controls. Positive controls cover the
blank return, singleton return, two-cell splitter and writer, and three-cell
cap-seven splitter.

The longest word in the58-word quotient yields a circuit with117,640 variables
(372 initial physical-cell bits) and362,079 clauses. Its solver status is
NOT_RUN; that construction alone says nothing about SAT or UNSAT.

The separate sound word/budget filter leaves23 candidate words. For EACH of
these23, the supplied mandatory initial colors give a finite seed of at most
three black cells. cap7_word_cnf_models.json contains a complete packed Boolean
assignment, input seed and full-board replay trace for each word. Every CNF
clause and every actual cut were checked. Thus these23 formulas are explicitly
SAT, without an external solver. The largest of these positive circuits has
69,517 variables. This does not make the models mutually composable.

The word RRRR at cap4 is an explicit UNSAT regression: its initial and final
empty-root guards produce opposite unit clauses. The exact two clause indices
and literals are recorded in symbolic_unit_contradiction.json, so this negative
control needs no opaque solver result or heuristic timeout.
