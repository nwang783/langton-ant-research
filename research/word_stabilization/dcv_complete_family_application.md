# Complete producer-family application to the D/C/V language

Status updated 2026-10-23 01:31 UTC: the 198-clause family and its D/C/V-tail consequence are independently signed. See audits/closed_producer_family_independent.json and check_dcv_tail_boundary_ledger_independent.json. The quantitative bounds below remain a separate analytic strengthening pending review. This is not global mixed-K finiteness or the universal finite-seed highway conjecture.

## Frozen proof chain

1. The exact marked residual ledger and the ordinary/protected pair relations are independently signed. An infinite marked D/C/V tail can be cut into maximal packets D C^k and V C^k. Its recurrent packet types are precisely D, DC, V, VC, VCC; DCC and DCCC are finite boundary exceptions. Pure C runs are bounded by the literal grammar.
2. The 102-clause companion-source family is independently signed, hash 8da1a5e5fc5c1162c1938890c836602ffd7ea4fa8d91831d0510425bcc16368e.
3. The larger candidate family `dcv_producer_closed_family.tsv` has 198 rows, hash c4585979213b8f6bdec63aee6daec119ab16226bce6a9d5401a3ae5968d994e4. Its manifest supplies exactly 96 new obligations. Every final graph uses that exact family, signed102 as its only additional signed relation, and a separately checked inductive no-hit invariant. The simultaneous least temporal-gap argument, including all outer-origin goal exemptions, is the one in `../core_periodicity_new/chronological_producer_certificate_protocol.md`.
4. This family contains every tuple in the independently audited directional25 sufficient list. The four-rotation potential argument in `dcv_directional25_confinement.md` therefore applies by the independently completed family signoff.

Consequently, no finite-support ant trajectory can have an infinite marked D/C/V tail. This is a theorem about this restricted literal language. It does not assert that an arbitrary finite-seed ant eventually enters that language, nor that arbitrary mixtures of all eight studied K labels are covered.

The old 69-case potential would still have one unproved transfer, old index7=(1,1,1,0,1,2,0). This is harmless for the different tilted potential: it obeys the new weight inequality. The other three rows removed during family discovery are also not needed by the tilted potential. They are neither declared feasible nor implicitly forbidden.

## Uniform finite-factor bound

The same argument yields a finite bound for any factor of recurrent packets, with an actual M11 context at each packet boundary. Let its initial black set be B0, with N0 cells and axis-aligned bounding-box widths W=xmax−xmin and H=ymax−ymin. The chosen packet entry is black because the signed five-cell core contains its origin.

Use L(x,y)=x+3y and its four rotations. For the frozen integer weights, the core offsets after including the anchor are a_h=(2,52,54,−8). The initial-token weight is60 and every stored output weight is at least−60. Hence every initial potential is at most 2 max_(q in B0) L_r(q)+60.

The exact arithmetic in `derive_dcv_directional_factor_bound.py` gives:
- every residual black cell: L_r(q)<=max_(B0)L_r+60;
- every core black cell: the same bound with37 instead of60;
- every intermediate head position, including packet endpoints: the same bound with48 instead of60.

A changed intermediate color lies at a read position, so the margin60 bounds all black cells at every fine time, not just packet cuts. Unchanged debris remains in B0. These statements use the maximum over all recurrent packet prefixes and all four headings, not only packet endpoints.

Writing L0=x+3y and L1=−3x+y, inversion gives x=(L0−3L1)/10 and y=(3L0+L1)/10. Thus every head and black cell lies in the integer rectangle obtained from the initial bounding box by adding x-margin 24+ceil(3H/10) and y-margin 24+ceil(3W/10). Put

X=W+48+2ceil(3H/10), Y=H+48+2ceil(3W/10),
A=(X+1)(Y+1), d=min(X,Y), m=floor((A−N0)/3).

Each C adds3 black cells and each V adds4, while D adds0. Therefore the number of C and V macros combined is at most m. Between them, a run of D has fixed heading and moves by a rotated (1,1) at each macro, so at most d consecutive D macros fit in the rectangle. There are at most m+1 such D runs. Hence the recurrent factor has at most

(m+1)d+m macros,
10(m+1)d+18m fine steps.

The latter uses the literal lengths |D|=10, |C|=15, |V|=18. No claim is made that these conservative constants are sharp. The bound depends on initial support diameter as well as mass; it does not assert fresh fuel at every V and preserves the known DCVCCVV recycling control.
