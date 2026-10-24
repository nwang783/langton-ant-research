# Exact adjacent-sheet exchanges of a white cap-four cursor

23 October 2026, 16:25 UTC. New exact occurrence-level interface, pending
independent review. Static level flow is not identified with a continuous
actual cursor, and zero-homology cycles are not paid resources.

## 1. Chronological labels, not just static contours

Use a complete WHITE cap-four translating front, actual full P,d, with
integer stream f(e)=h(C_right)-h(L_left) and c_right-c_left=1. Number the
actual occurrences of each physical directed edge chronologically from
one. Give its r-th occurrence the integer label

    j(e,r)=h(C_right(e))-r+1.

Every physical edge occurrence gets exactly one label. The occurrences
at level j project to the indicator flow

    g_j(e)=1{h(L_left(e))<j<=h(C_right(e))}.

This is balanced: it equals the difference of the two threshold face
indicators 1{h(C)>=j}-1{h(L)>=j}, whose corner divergence telescopes.
Its oriented homology is

    1{c_right>=j}-1{c_left>=j} = 1{j=c_right}.

Thus precisely one sheet has total homology +1, all others total zero.
Summing g_j over all integers recovers the full physical flow f. There
are finitely many nonempty sheet occurrences in the full quotient.

The actual ant need not preserve j when a read joins its incoming and
outgoing occurrence. The next section identifies every possible change.

## 2. Complete local exchange law

For a cell let a_r,b_r be the labels of the incoming/outgoing occurrences
at complete read rank r. Its history is R, RL, RLR or RLRL. Then:

- rank R0 preserves level: a_0=b_0;
- every one-R cell preserves level at ALL of its reads;
- at every two-R cell, and only there, L1 and R2 exchange adjacent levels:

      a_1=b_2, b_1=a_2, |a_1-b_1|=1;

- optional L3 preserves level: a_3=b_3.

Write lambda for the higher incident C height. At a flat two-R contact,
the exchanged levels are lambda and lambda-1. At a same-face height-two
contact, they are lambda-1 and lambda-2. All L1 source visits and the
possible L3 stock are explicit; none is replaced by an earlier R.

### Direct proof retaining every heading

Fix incoming axis N/S. Put h_NW=0, h_SE=delta; translations of h do not
affect the law. If r_N,r_S count the R headings, edge balance gives

    delta=r_N-r_S.

Incoming N and outgoing E use right C height delta. Incoming S and
outgoing W use right C height zero. Subtract the chronological port
ordinal minus one in each case to obtain its occurrence label.

R0 has ordinal one at both ports and uses one C face, so preserves its
height. In a one-R RL cell, delta=+/-1; its possible L1 uses the next
ordinal of one R0 port and the first ordinal of the other C port, giving
equal labels. In a two-R cell, R0/R2 either have opposite headings
(delta=0) or equal headings (delta=+/-2). The intervening L1 shares
exactly ONE physical port with R2. Its two occurrences at that shared
port have consecutive ordinals. Substitution gives the exchanged pairs
above. The remaining final L3, if present, has equal labels by the same
port counts. This covers all choices of L1 and L3 heading.

stream_sheet_local_controls.py/json independently enumerate all 30
length-at-most-four complete histories in this incoming axis, including
all 24 two-R rows, with both incident L heights reconstructed from the
port counts. Rotation gives the other checker phase. This is a local
identity check, not a front or period search.

## 3. Canonical level repair of the full actual itinerary

Let O be the P actual directed edge-occurrence classes in the full
quotient. The actual successor permutation sigma sends an incoming
edge occurrence to the outgoing occurrence at its next read. In actual
time order it is the single P-cycle. This uses the stated full event
period, not a primitive spatial assumption.

At each two-R cell, swap the OUTGOING occurrence successors attached to
the incoming L1 and R2 occurrences. In symbols replace

    in_1 -> out_1, in_2 -> out_2

by

    in_1 -> out_2, in_2 -> out_1.

Section 2 shows that this repaired pairing preserves j. All other
successor pairings already preserve j. Different cells have disjoint
outgoing occurrence pairs, so the repair is a product of commuting
disjoint transpositions. Call the repaired permutation sigma_0.

Every sigma_0 cycle is a balanced physical cycle at a single sheet j;
these cycles partition all actual edge occurrences. They are NOT
consecutive actual time intervals. A repaired pair may join events at
very different actual times, so no telescope of actual delays is being
asserted for such a cycle.

The repair changes only the association of edge OCCURRENCES. Its two
repaired physical turns have the same aggregate corner-turn inventory:
L1 and R2 share one input or output physical port. Hence at a sheet with
four active incident ports the two pairings are the two R corners or
the two L corners; with two active ports there is one ordinary turn.
Rounding those disjoint corner arcs yields disjoint embedded sheet
circles. Each canonical sheet circle has winding 0,+1 or -1. This
primitivity is asserted ONLY for these new embedded repaired circles,
not for any actual mixed-rank dependency cycle.

At the global top sheet M, all L heights are below M. Its repaired
pairing always turns R around a max-C face. Consequently its cycles
are exactly the four-edge clockwise boundaries of the individual
maximum C faces, one per max-face class, with winding zero.

## 4. A connected adjacent-level cycle graph with even cycle excess

Form a finite graph G:

- its C vertices are the cycles of sigma_0;
- each two-R cell contributes one edge between the two sigma_0 cycles
  containing its outgoing L1/R2 occurrences.

The two endpoints are on adjacent distinct sheets, so the graph has
no loops and is bipartite by sheet parity. Multiple edges are retained.
Let N2 be the number of two-R physical cell classes.

G is connected. Indeed sigma_0 preserves each node-cycle. Undoing a
local repair exchanges only occurrences in the two endpoint cycles,
so the union of node-cycles in any graph component is preserved by
both sigma_0 and every repair transposition. It is therefore preserved
by sigma. Since sigma is one actual P-cycle, no proper nonempty graph
component is possible.

There is also the exact parity relation

    N2 congruent C-1 modulo 2.

To see this, sign(sigma)=(-1)^(P-1), while
sign(sigma_0)=(-1)^(P-C). The product of the N2 transpositions relates
them, giving the claim. Connectivity and parity together yield

    N2-C+1 is a nonnegative EVEN integer.

This is a global rank-two coupling, not a conjectured local payment.
For example, a graph consisting of a single independent cycle cannot
be the complete repaired graph: its cycle excess would be one. Extra
connected cycles or trees cannot simply be omitted from this register.

At each sheet, the sum of canonical node windings is exactly one at
j=c_right and zero elsewhere. This describes signed total flow, not
absence of essential oppositely oriented node pairs on zero sheets.

## 5. K=1 interpretation and unresolved next step

For K=1, M=c_right+1 and c_left=M-2. The max-face flat contacts exchange
top sheet M with the sole nonzero-homology sheet M-1. Height-two helpers
on the strict LEFT collar exchange M-1 with the zero-total-homology
sheet M-2. Optional L3 preserves its sheet even when it is genuine old
stock supplied by a nearby return strand.

This exactly distinguishes a rank-lowering gate from a purported fresh
resource. The row-5 near-return control transports old L3 stock on the
lower sheet; the graph does not discard it because that sheet has zero
TOTAL homology. Its component cycles and all exchange edges remain.

A possible next use is to combine the connected adjacent-level graph
with chronological order of K=1 interleaving LEFT excursions. No bound
on graph genus/cycle excess, no paid gate density, no K>=2 theorem and
no standard104 capture conclusion is proved here. This cap-four repair
must not be imported into the actual 1564 cell with at least 20 recorded
visits.
