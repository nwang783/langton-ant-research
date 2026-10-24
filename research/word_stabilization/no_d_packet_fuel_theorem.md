# Linear fuel for C,V,U,F,Q,B factors (no D)

Status: independently verified on 2026-10-22 by a separate literal-word and complex-coordinate reconstruction. The certificate uses the older unmodified generic_spatial_kernel.cpp, not the new odd-reader or multi-cell rules.

## Literal language and scope

Use the six words in seven_sub_no_d_port_quotient.json, before C-run packetization: C15, V18, U28, F56, Q64 and B74. All six start with M11 = LLLLRLRRRRL. A finite factor starts with a non-C macro and is followed in its actual turn stream by M11. Entry mass m is the total finite number of black physical cells at this factor's start. Freshness is relative only to this factor.

The five literal words A C^3 M11, for A in {V,U,F,Q,B}, are physically infeasible. Hence every C run after a non-C consists of at most two C macros. Group each non-C with its maximal following C run. This gives the fifteen packet words A C^k, k=0,1,2, listed in the frozen quotient JSON. The quotient is deliberately the one-state graph admitting every packet; physical short-factor checks supply the only grammar restrictions. There is no 149-history or original H-port premise.

## Certified freshness

The frozen generic engine builds 71,960 overlapping pair types, removes 79 realizable short types, and stabilizes after four removal rounds at 69,158 forbidden pair types. The ordinary source-LAST/target-FIRST and neighbor-descent rules use only strictly shorter actual packet-index gaps. The target is the entire packet followed by actual M11, while every source and intermediate reader owns only its raw packet. Thus proper subpairs inherit their actual context.

The selected raw first-L inputs are:

- V, VC: V's tip (1,2), at phase13.
- VCC: that tip and the first C's input (0,3), phase19.
- U, UC, UCC: (-1,0), (0,2), (0,3). The latter two also use the first C input (-1,4), phase29.
- F, FC, FCC: (-1,0), (-3,1), (-4,0), (-3,-1), (-2,-1), (-4,-1). The latter two also use the first C input (-3,-2), phase57.
- Q, QC, QCC: the same six F inputs and (-4,-3). The latter two also use the first C input (-3,-4), phase65.
- B, BC, BCC: the same six F inputs and (-3,-3), (-2,-3), (-2,-2), (-3,-4). The latter two also use the first C input (-2,-5), phase75.

Every alignment of any earlier packet's RAW read footprint with one of these target cells belongs to the forbidden kernel. Therefore each selected cell is unread earlier in the factor. Each is a first-L input within its own packet, so it is black at factor entry. The selected cells are pairwise distinct across packets.

The first packet also needs the four startup black cells (0,0), (-1,-1), (0,-1), (1,0), at phases0,2,3,5. None is among the selected marks of that first packet. Any selected mark of a later packet is unread earlier, hence cannot equal a startup cell already read by the first packet. Thus these four contributions are disjoint from every selected mark.

## Weighted and length bounds

Assign packet weights in the displayed order:

V,VC,VCC: 1,1,2;
U,UC,UCC: 3,4,4;
F,FC,FCC: 6,7,7;
Q,QC,QCC: 7,8,8;
B,BC,BCC: 10,11,11.

Then 4 + sum(weights) <= m. Every packet has at most33 times its weight raw turns, with the maximum ratio33 attained by VC. Hence the entire factor has at most33(m-4) raw turns. Its mass gain is at most7 times the weight, so its exit mass is at most8m-28.

For an arbitrary finite physically feasible six-macro word with no right-marker assumption, remove at most four leading C macros and its last macro. The leading part costs at most60 turns and increases mass by at most12; the last macro costs at most74 turns. If a nonempty middle remains, its true next macro supplies M11. This gives the conservative unconditional finite-word bound 33m+398 turns. A word containing only initial C macros is covered separately by C^5 infeasibility. Consequently no infinite finite-support trajectory can remain in this six-word language. This strengthens the previous arbitrary-five-macro finite-fuel theorem by allowing F and replacing its exponential finite-factor estimate by a linear one.

## Frozen artifacts

- seven_sub_no_d_port_quotient.json: exact fifteen packet words and one-state graph.
- seven_sub_no_d_grammar.json and seven_sub_no_d_kernel.input: literal feasible pairs/triples and raw/context footprints.
- seven_sub_no_d_plain_kernel.tsv: stable spatial certificate.
- seven_sub_no_d_plain_kernel.fresh.tsv: discovered marked cells.
- no_d_packet_fuel_marks.json: selected weighted raw marks and direct finite ingredient checks.
- no_d_packet_fuel_manifest.json: SHA256 provenance.

Independent checker: ../audits/check_no_d_packet_kernel_independent.py and its JSON output. The independent replay checked all 69,158 ordinary-rule clauses, 15,094,968 intermediate-reader options, 670,492 neighbor options, and 95,760 marked-site overlaps.
