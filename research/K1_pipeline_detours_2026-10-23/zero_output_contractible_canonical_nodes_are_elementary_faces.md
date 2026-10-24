# Zero-output contractible canonical nodes are elementary face loops

24 October 2026, 01:20 UTC. Complete WHITE cap-four translating front,
actual full P and nonzero d. Pending independent review. No K1 or
leftmost hypothesis. This uses the separately frozen two-level contact
barriers ad564468 and the signed finite prepared-plateau theorem
ab9fad0a, including its essential selected-curve alternative.

THEOREM:

1. Every CLOCKWISE contractible canonical sheet circle, on any sheet j,
   is the four-edge boundary of one C face of height j. This conclusion
   does not require zero odd output.

2. If Nodd=0, every COUNTERCLOCKWISE contractible canonical sheet circle
   is the four-edge boundary of one L face of height j-1.

Thus at zero output ALL contractible canonical nodes are elementary
C/L face loops. Every non-elementary canonical node is essential.
This is a shape classification, not a bound on how many such nodes or
essential pairs can exist, and not a complete front exclusion.

## 1. There is no finite physical C superlevel island

Fix any integer t. Suppose a connected component A of C faces with
height>=t is physically finite. Choose its largest height lambda and a
connected lambda plateau Q in A. Q is a locally maximal C plateau in
the whole plane: any larger adjacent C height would also belong to A.

All Q incident cells are initially WHITE. The signed prepared maximum
plateau theorem therefore supplies an essential first-L parent curve
inside Q (and lambda>c_right). This is impossible in a finite physical
set. Its full-quotient projection cannot hide a winding: if a connected
finite physical component overlapped its nonzero full-drift translate,
the components would coincide and the finite set would be invariant
under that translation. Therefore A cannot exist.

When Nodd=0, the time-reversed front is also completely WHITE: every
original cell has an even complete history and finishes WHITE. Apply
the same theorem after the signed reversal h_rev=-h and sector swap.
It follows that no physically finite L sublevel component exists.
This reverse step is NOT used when odd output is present; then reversed
initially-black classes must be retained.

## 2. Heights inside any contractible sheet-j disk

Let gamma be any contractible canonical sheet-j circle and D its bounded
physical disk, using the signed disjoint rounded embedding. The C
barrier preserves each C superlevel component >=j+1 on one side of gamma.
If D contained a C face at height>=j+1, its whole superlevel component
would be confined to the bounded disk, contradicting section1. Hence

    every C face inside D has height<=j.                 (1)

At zero odd output the dual L barrier gives, in the same way,

    every L face inside D has height>=j-1.               (2)

These are physical disk statements, not a claim that a zero-total-
homology sheet contains no essential circles. Both essential orientations
remain possible in other components.

## 3. Exact turn-level facts at a canonical corner

Let lambda be the higher of the two incident C heights at a cell.
The complete canonical local repair has two properties:

    any LEFT turn at sheet j has lambda>=j+1;            (3)

    any RIGHT turn at sheet j, except an actual
    singleton-R cell, has an incident L height<=j-2.      (4)

For (3), the local top sheet lambda consists only of RIGHT turns around
C faces. R0 is always at lambda. A one-R final L1 has level lambda-1;
any final L3 has level<=lambda-1. At a two-R exchange, a flat profile
has its upper RIGHT transition at lambda, lower LEFT at lambda-1; a
same-R profile has upper RIGHT at lambda-1, lower LEFT at lambda-2.
Thus a LEFT transition is strictly below the local C top.

For (4), an R0 of a non-singleton complete history has at least one L
heading somewhere in that history. The exact local face equations give
minimum L height<=lambda-2, while its level is j=lambda. For a repaired
RIGHT transition at a flat cell j=lambda and the same inequality holds.
For a same-R upper exchange j=lambda-1, the one or two L headings give
minimum L height<=lambda-3=j-2. These exhaust canonical RIGHT turns:
unchanged L1 or L3 turns are LEFT. A singleton-R is the exact exception,
with incident L heights j-1,j-1; it is itself an odd output class.

The independent local control reconstructs98 canonical turn occurrences
across all78 nonempty sheets of the thirty WHITE histories:44 LEFT,
52 non-singleton RIGHT and2 singleton RIGHT turns. All satisfy (3)/(4).

## 4. Clockwise circles cannot have a reflex LEFT corner

At a LEFT corner both diagonal C sectors lie on geometric RIGHT of the
oriented arc. If gamma is clockwise, that is the bounded interior D.
A reflex LEFT turn would therefore place a C sector of height>=j+1
inside D by (3), contradicting (1).

Thus every corner on a clockwise contractible circle is RIGHT. Every
edge has unit length and every canonical transition turns through90
degrees. The total clockwise turning is four quarter-turns, so the
circle has exactly FOUR edges: a unit C-face boundary. Its enclosed
C height is at least j by the sheet support, and at most j by (1),
therefore exactly j. Odd outputs elsewhere do not affect this proof.

## 5. Zero-output counterclockwise circles have no reflex RIGHT corner

At a RIGHT corner both diagonal L sectors lie on geometric LEFT of the
arc. For a counterclockwise gamma that is its bounded interior D. With
Nodd=0 no singleton-R cell exists. A reflex RIGHT turn would thus put
an L height<=j-2 in D by (4), contradicting (2).

Every corner on such a circle is consequently LEFT. Its total turning
again gives exactly FOUR unit edges, now around an L face. Its enclosed
L height is below j by the active sheet support and at least j-1 by (2),
therefore exactly j-1.

## 6. Scope and open geometry

Contractible C/L face loops may have several graph exchanges; the
classification does NOT make them graph leaves or give their actual
return spans. Repaired nodes are still not literal consecutive ant
factors. Essential canonical circles of either orientation, essential
flow-three circuits, graph excess and cross-component transfer remain.
No count of renewals, original black roots, period bound, attained WHITE
front, or general K1 exclusion follows without another argument.

Control `canonical_turn_reflex_level_inventory.py/json` checks all local
turn inequalities and finds no reflex survivor under the stated disk
height bounds. The proof of those disk bounds and physical quotient
closure is separate from the finite inventory; no bounded spatial or
period scan is substituted for it.
