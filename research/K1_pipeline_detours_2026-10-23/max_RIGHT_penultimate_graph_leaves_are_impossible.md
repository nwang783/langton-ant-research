# A max-RIGHT penultimate graph leaf necessarily has a second exchange

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. No K1, output-zero or leftmost hypothesis. This concerns exactly
the old restricted max-RIGHT contractible graph-leaf family counted by
max_turn_leaf_stock_balance.md and penultimate_leaf_top_R0_supplier_capacity.md.
Nonleaf stock holes and other leaf root types are NOT excluded.

THEOREM: the restricted family is empty, so its h equals zero.

## 1. Retain the exact graph-leaf premise and bridge sign

Use the signed canonical sheet repair fd20e425 and clock/bridge
addendum552d5aa8. A contractible canonical cycle gamma of sheet j=M-1
is a GRAPH LEAF when it has only ONE incident exchange edge, retaining
multiedge incidence. Suppose that unique root corner v is a RIGHT turn
around a global maximum C face at M. Its two R headings are the SAME,
and its exchanged sheets are M-1 and M-2.

Because gamma is contractible, the signed clock identity at its sole
exchange is

    0=ell-Delta_v or 0=ell+Delta_v,

where ell>0 and Delta_v=T2(v)-T1(v)>0. Thus only the negative repair is
possible: gamma contains outgoing L1, not outgoing R2. This is the
already signed leaf-bridge sign, not a newly chosen orientation.

## 2. The outgoing L1 port has at least three complete uses

Normalize the same-R headings at v to E. To have outgoing L1 on sheet
M-1, its heading must be W, opposite to the R heading. R0,R2 then
both depart S, and L1 also departs S. Its outgoing S occurrence is
ordinal TWO, after R0 and before R2. L3, if present, can give either
another S departure or the other direction. Therefore the full port
count is exactly THREE or FOUR. Both RLR and RLRL are retained.

The same conclusion in all rotations is also immediate from the
complete local sheet law: L1 on the upper same-R exchanged sheet is
the second occurrence of the port already used at R0 and still to be
used at R2. It is a physical occurrence, not a repaired artificial edge.

Let w be the neighboring target cell of this directed physical edge.
Actual chronological ordinal matching sends v's outgoing ordinal-two
edge to the SECOND incoming occurrence of the same port at w. That
incoming edge has label M-1, and gamma follows it to w.

## 3. The target necessarily supplies another exchange edge

The complete input count at w on this port equals THREE or FOUR.
With at most four total white reads, the second of at least three
identical input headings can occur only at rank1 or rank2. It cannot
be rank0 (it is second) or rank3 (a third occurrence must still follow).
Thus the arrival is EXACTLY w.L1 or w.R2. The cell has two R reads.

At either rank, the canonical repair changes this successor by the
L1/R2 transposition. Hence gamma is incident to the exchange edge at w.
The other endpoint is on an adjacent distinct sheet, so this is a real
incident graph edge, not a self-loop or an unchanged R0/L3 visit.

Cells v and w are neighboring physical cells of opposite checker
parity. The signed full-heading period is even and full drift preserves
checker parity. Therefore v and w cannot become the same full-quotient
cell class. Their exchange edges are DISTINCT even in a short quotient;
parallel graph edges, if any, retain multiplicity.

Gamma therefore has at least TWO incident exchange edges, contradicting
the graph-leaf premise. This proves the theorem.

## 4. Exact scope and relation to earlier notes

The older length/clock/R0-supplier lower bounds for this family remain
correct but are now vacuous for complete WHITE cap-four fronts. Their
frozen sources are not edited. The argument does not eliminate arbitrary
contractible penultimate cycles, nonleaf stock holes, positive graph
excess, ordinary prepared controls or canonical leaves on other sheets.
It is not a general front or fuel exclusion.

This theorem is independent of the pending no-contractible-G3-cycle
claim5036e7c2. It needs only one physical outgoing occurrence, its
chronological port ordinal, and the actual target rank. It does not
promote a spatial path to a literal ant itinerary or add a period cost.

Control `max_RIGHT_penultimate_leaf_second_exchange.py/json` checks all
six same-R root histories giving outgoing L1 at M-1 and all six possible
target histories with at least three arrivals at that port. Every
root occurrence is ordinal2 and every target occurrence is rank1/2.
No front, period, drift, radius or multiplicity scan is performed.
