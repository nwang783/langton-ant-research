# Uniform cut-forest bounds for completed module calls

Status: analytic proof completed by the causal-reduction analysis, 2026-10-22.
Independent analytic audit passed on22October2026 at14:34UTC. Exact controls are in
`probe_completed_module_forests.py` and `completed_module_forest_controls.json`.
The controls are not the proof.

## Statement and conventions

Use the audited completed-call grammar from
`first_principles_new/completed_fingers_and_no_interleaving.md`:

- G_a(0)=a^4; G_a(n+1)=a^2 G_b(n) a^2, where b is the other turn.
- B_a(n)=a G_b(n) a^3.
- B_a(n,m)=a G_b(n) a G_b(m) a^2.

Normalize each whole call to physical pose (0,0,N). Arbitrary translations
and quarter-turn rotations preserve everything below. The claims concern a
physically feasible completed interval, with the causal forest CUT at entry:
the initial cursor is a depth-zero root; each entry-time black token first
consumed inside the interval creates a new depth-zero cursor root; each L
consuming an interval-produced R token creates a child of its producer node.
All remaining interval-produced R tokens are boundary buds, one edge below
that producer. Ordinary cursor nodes with no output also count.

THEOREM.

1. Every G_a(n) component has size 1 or 5. Its bud-inclusive depth is at most2.
2. Every one-finger B_a(n) component has size 1 or 5, with depth at most2.
3. Every two-finger B_R(n,m) component has size 1 or 5, with depth at most3.
4. A two-finger B_L(n,m) has exactly one component of size9; all other
   components have size1 or5. Its depth is at most3.

Thus every completed call, regardless of the finger lengths, has causal
component size at most9 and depth at most3. These bounds are sharp.
The number of components is not bounded independently of finger length.

For any component, size = 1 + the number of R tokens born in that component:
each such token contributes either its eventual L-child or its boundary bud.
This identity includes zero-output roots and the terminal cursor.

## Ladder proof

For k>=0 the literal words are

G_R(2k)   = (RRLL)^k RRRR (LLRR)^k,
G_R(2k+1) = (RRLL)^k RR LLLL RR (LLRR)^k,

and G_L is obtained by swapping R and L. At pose (x,0,N), RRLL moves to
(x+2,0,N), reading top-row cells x,x+1 with R and bottom-row cells x+1,x+2
with L. At pose (x,0,N), LLRR moves to (x-2,0,N), reading top-row cells
x,x-1 with L and bottom-row cells x-1,x-2 with R. This gives the exact
outward/returning two-row ladder, not merely its boundary.

In G_R, each pair of outward R's at top-row coordinates x,x+1 and its
returning pair at bottom-row coordinates x+1,x belong to one plaquette.
The first outward R token survives as a bud (at the initial plaquette), or
is consumed into a zero-output cursor. The second outward R token is
consumed immediately before that plaquette's returning RR, linking the
two positive cursor nodes. The latter two R tokens survive at interval end.
At an even-depth far end, the central RRRR is a single positive node instead.
Distinct plaquettes never share an R-read cell or a positive cursor ancestry.
All other cursor roots have zero output. Hence every positive component
contains exactly four R births and either one or two positive cursor nodes.
Its forward offspring are leaves, and its only possible productive parent
edge joins the two RR nodes. Thus size5 and bud-depth<=2.

In G_L the same two-row computation runs from left to right on return.
The two R pairs are now bottom-outward and top-returning. Again the second
outward R token joins the returning RR node, while a later L can consume
the first token only into a zero-output node. A central RRRR, when present,
is a single four-output node. This proves the same conclusion. G_L(0)
has no R births and only size-one components.

Two interface facts, also visible directly in these two-row formulas, will
be used below:

- G_R(n) starts by reading its entry cell R. That cell's token is never
  consumed within the ladder. Its final active cursor is a descendant of
  the entry cursor at the SAME Tait vertex. The entry cursor's positive
  component has exactly four R births. Its entry-cell token is produced
  by the INITIAL positive cursor node, not by the returning RR node.
- G_L(n) first reads its normalized cell (0,-1) only at its LAST L. Its
  final cursor is the root/child obtained by consuming that token and has
  no R output within the ladder. The entry active cursor has no R output
  before the ladder's first L.

## B_R: one or two left-turning fingers

The four R's outside the G_L children traverse the parent unit square.
The first child starts at (1,0,E). Its normalized last-read cell (0,-1)
is physical (0,0), exactly the first parent R token. This token is consumed
backward, returning the active cursor to the original Tait vertex.
No other child read overlaps that first parent R token.

For one child, the remaining parent RRR has this returned cursor as its
producer. The parent component therefore has R-output counts 1+3=4.
For two children, the next parent R is at (1,0), and the second child starts
at (1,-1,S). Its normalized last-read cell is physical (1,0), consuming
this second parent token backward. The final RR again has the same parent
ancestry. The parent positive chain has output counts 1+1+2=4.

The first child's two-row footprint is x in {0,1}, y>=0; the second child's
is x>=1, y in {-1,0}. They meet only at (1,0), the explicit parent handoff.
All other positive components inside either child are therefore independent
size-five ladder components. The parent component has size5 and has depth2
for one child, depth3 for two children. Other zero-output roots have size1.

## B_L: one or two right-turning fingers

The initial parent L at (0,0) creates a cut root. The first child G_R starts
at (-1,0,W), with footprint x in {-1,0}, y>=0. Its entry component has four
R births. The next parent L at (-1,0) consumes the first R token of this
entry component, creating a child of its INITIAL positive node.

With one child, the remaining parent LL are at (-1,-1) and (0,-1), outside
that finger. They consume entry-time black tokens and create only zero-output
roots. All positive components still have size5 and depth<=2.

With two children, the new cursor instead executes G_R(m) starting at
(-1,-1,S), with footprint x<=-1, y in {-1,0}. Its entry component has four
additional R births, linked to the first child's entry component by exactly
the parent L just described. The two footprints meet only at (-1,0), that
same handoff cell. Thus exactly these two size-five components merge, replacing
one old boundary bud by the second root, to give size5+5-1=9. All other
positive components remain independent size-five components. The final two
parent L's add only zero-output nodes (one consumes the second entry-cell
R token, and the other is an entry-time black token).

The first positive node of the second child's entry component is at depth1;
its optional returning RR node is at depth2, and its buds at depth3. The
first child's optional returning RR node has depth1, not on the handoff
path. Hence the maximum bud-inclusive depth is3, regardless of either
finger length.

## Scope and remaining obstruction

These are local cut-forest bounds for completed calls, not a global bound on
causal bushes along the unique nonreturning module spine. Entry-time black
tokens of one call may themselves have arbitrarily old parents. Furthermore,
restoring the color of an interior lamp does NOT restore its token ancestry.
For example G_R(1)=RRLLLLRR replaces the restored interior token at (1,-1)
by an entry-cursor descendant. A later distinct coset can consume that token.
Consequently a future call may reconnect or reproduce ancestry stored by a
finished call; no finite number of global ancestry ends has been proved.
