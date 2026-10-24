# Chronological leaf-port matching: a local repair and exact Hall obstructions

24 October 2026. Author-checked finite certificates; independent audit pending.

## Result first

The signed blank interval's unpaid terminal chain can be repaired without reusing an input or output: two different leaves use the two different lifetime ports of one BLACK-to-BLACK cell. This repair extends to an explicit injective matching of all 27 leaves of that interval.

Two natural ways of turning this into a universal gross leaf bound fail on actual complete histories:

* In the EMPTY-seed prefix ending at fresh cut 1579, three leaves have only ONE input/output port on their entire ancestor paths. One additional free root still leaves a Hall deficit of one.
* In the completed MT100 pristine drought, four leaves have the same unique first-mark predecessor-chain port. One free root still leaves a deficit of two.

Even the finer pairing of the COMPLETE visit order into true R-to-L lifetimes and adjacent same-axis steps has a closed four-event component containing a last-exit leaf but no input/output endpoint. A leaf charge cannot stop inside one such temporal component.

These are exact obstructions to specified matching rules, not a counterexample to the numerical gross inequality. The inequality remains OPEN:

    leaves(T_[s,t]) <= |C_[s,t]| + |O_[s,t]| + 1.

No renewal fuel, global attraction, or new standard104 classification is claimed.

## 1. Full interval region, actual ports, and the proposed matching problem

Use an actual interval [s,t] whose final head p_t has no read in [s,t). T_[s,t] is the last-exit tree on EVERY cell read in that interval, with the fresh final head added as its root. It is not a chosen-patch tree and it is not, in general, the whole pre-s historical tree. In the EMPTY prefix s=0, these two notions coincide.

At every read vertex v, retain its complete ordered visit list. Let C be its BLACK-at-s lifetime if that lifetime is consumed in the interval, and O its final interval-born R lifetime if it survives to t. These are DISTINCT capacity-one ports even when they occupy the same physical cell. An unmarked vertex starts and ends WHITE. A BLACK-to-BLACK vertex has two ports, not one.

For a proposed bipartite admissibility graph from leaves to ports, an injective charge exists precisely when every set A of leaves has at least |A| neighboring ports. Adding one free global root increases each nonempty neighbor set by at most one. The finite Hall witnesses below list the complete allowed neighbor sets, so they refute their particular rules independently of any matching heuristic.

For a last read ell(v)>s, define f(v) as its last-arrival predecessor u when ell(u)>ell(v). The signed first-step result proves that f is injective and defined at every leaf except the possible initial-cut exception. It does not make f chains into disjoint leaf charges: multiple leaves can lie on one chain.

## 2. A repaired local charge, extended without reuse to all 27 leaves

Use the actual empty-seed interval [5710,6042]. The previous obstruction was

    v=(0,8) --f--> u=(-1,8),

where u is unmarked and f(u) is undefined. The last-exit tree has the descendant path

    w=(0,7) -> (-1,7) -> u.

Both v and w are leaves. The cell w has two different actual ports:

* Its old BLACK lifetime R2997 is consumed at update 5809.
* Its new surviving output is R5881.

Assign w to C(w), and v to O(w), using the path

    v --f--> u --tree child--> (-1,7) --tree child--> w.

No lifetime port is reused. All four vertices, their complete visit lists, and EVERY crossing into or out of this four-cell set are retained in the checked data.

This is not merely a two-leaf assignment that steals a port from the rest of the tree. The checker reserves these two assignments first and then constructs an explicit matching for every other leaf using other ports. All 27 leaves are matched to 27 distinct actual C/O ports. Every certificate path consists of an f step or a reversed last-exit edge. The interval has 47 old-input ports and 67 output ports. This is a literal finite construction, not a proof that this matching rule always works.

## 3. Ancestor-only charge fails, even with the free root

Start on the EMPTY board at (0,0), heading E, and stop at cut 1579. The endpoint is the fresh cell (11,2). The complete interval tree has 322 read vertices and 81 leaves; C is empty and O has 163 cells.

For the leaves

    (8,-2), (9,-1), (9,1),

the union of ALL C/O ports on their ancestor paths is exactly

    { O(10,1) }.

The full ancestor paths are:

    (8,-2),(8,-3),(9,-3),(9,-2),(10,-2),(10,-1),
    (11,-1),(11,0),(10,0),(10,1),(11,1),root;

    (9,-1),(9,-2),(10,-2),(10,-1),(11,-1),(11,0),
    (10,0),(10,1),(11,1),root;

    (9,1),(9,0),(10,0),(10,1),(11,1),root.

The three leaves are WHITE-to-WHITE. Their exact reads are respectively

    R1112,L1116,R1120,L1544;
    R1118,L1554;
    R726,L1574.

The sole eligible output is R1577 at (10,1). Thus three demands have only one port, or two capacities if the one free root is allowed. No ancestor-only injection exists. This does not refute 81 <= 163+1; it says that some charges must leave their ancestor paths.

## 4. First-mark predecessor charging also fails

Use the genuine completed MT100 pristine drought [40071,109168], preserving its entire original finite board and all later writes. The four cells

    (197,231), (198,231), (198,232), (197,232)

are ALL leaves of the interval tree. Their f chain, in that order, ends at (197,232), whose surviving output is R71039. The first three cells have no C or O port. The last cell has O only. The f last-read times are

    71006 < 71021 < 71036 < 71039.

Consequently, if a leaf stops at the first marked vertex on its predecessor chain, these four leaves have exactly one eligible port. Even a free global root leaves deficiency two. The four actual last-exit edges go OUTSIDE the square; all crossing events are retained. This is not an autonomous four-cell subsystem.

There is also an exact unmarked descendant subtree rooted at (234,169), with leaves (234,168) and (234,170). Its complete visits are

    root: R87757,L87817;
    lower leaf: R87748,L87756;
    upper leaf: R87524,L87816.

All three cells are WHITE at both interval cuts. The subtree has two leaf demands and zero ports. Therefore a universal 'one free root per descendant subtree' bound is also false. Its external chronology cannot be discarded.

## 5. The lifetime-plus-axis decomposition has genuine unpaid cycles

This tests a more chronological candidate, using ALL visits, not just first and last visits.

Pair each R birth with the next L at that same cell when that death lies in the interval. Unpaired L reads are precisely C ports, and unpaired R reads are precisely O ports. Separately pair adjacent event times of one parity. These adjacency edges are all steps of one fixed coordinate axis, because the ant alternates movement axes. Any unpaired first or final event is retained as a partial-episode endpoint.

The union of the two matchings is a disjoint union of alternating paths and cycles. Every path has exactly two endpoints, counting C/O and partial endpoints; a cycle has none. This elementary degree-two identity is exact but gives no leaf charge unless leaves on zero-endpoint cycles and multiple leaves on one path are controlled separately.

In the same EMPTY prefix [0,1579], pairing even/odd adjacent events gives the closed component

    R1420 at (10,-12) --axis--> R1421 at (10,-13),
    L1448 at (10,-12) --axis--> L1449 at (10,-13),

with true lifetime pairings 1420--1448 and 1421--1449. Both cells start and end WHITE. The read at 1449 is the last read of the genuine tree leaf (10,-13), and is an incoming-axis-paired event. There is no C port, O port, or partial endpoint in this component.

The actual 26 reads between updates 1421 and 1448 take place outside this two-cell set. The full field and every boundary crossing remain in the certificate. The closed COMPONENT is a combinatorial decomposition of an actual finite history; it is not a bounded ant orbit or a causal time loop. Any port charging scheme based only on this one lifetime/axis component fails and must use information crossing between these components.

## 6. A broader finite interface, still not a universal theorem

Allow f steps and reversed last-exit edges without stopping at marked vertices. This is the interface used for the valid 27-leaf matching in Section 2. At cut 1579 it matches 80 of 81 leaves to distinct real ports. Its remaining exact Hall witness has leaves (3,-8),(4,-9) and only O(4,-8). The full reachable set is the eight-cell rectangle {2,3,4,5} x {-9,-8}; it does not contain the initial head. One free global capacity repairs this particular finite deficit.

This does not establish a universal '+1' Hall bound for the enlarged interface. Nor does the finite success on the signed interval prove the numerical gross bound. The current concrete obligation is to control deficient chronological catchments jointly without granting each its own free capacity. The actual unpaid axis cycle and the eight-cell catchment show why purely local port inventories do not finish that obligation.

## 7. Audit and scope

The checker independently replays the actual EMPTY source through cut 6042 and the literal MT100 source through cut 109168: 115210 updates in total. It retains full endpoint fields, all interval last-exit trees, all actual C/O identities, complete interval words, selected full visit lists, all proper-patch crossing events, explicit injective assignments, and explicit Hall neighbor sets. It compares the entire replayed words against the signed whole-field source histories.

No sampling inference is used for any stated finite result. The preceding bounded diagnostic checks of additional intervals remain UNKNOWN with respect to the universal gross inequality and are not premises here. The larger question of recurring drought renewal, eventual compact relevant geometry, and canonical104 attraction remains open.
