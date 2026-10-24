# One exact full odd inventory is excluded by two actual read boundaries

24 October 2026. Author proof with an exhaustive, solver-free certificate;
independent review requested. This is not a general drift(3,1) exclusion.

## Exact statement and dependencies

Consider a complete WHITE front with actual full drift(3,1), growth8, and the
signed two-quadruple single-used F-circle prefix

T0..7 = S, W, S, EEWE, SSNS, EEW, NNN, EEEW,

where T=3y-x and the representative of T is(-T,0). Suppose its FULL odd-read
inventory is exactly O={0,1,2,5,6,8,13,20}. No such front exists.

The prefix is the two-quad branch of the signed shape cover102da4e3, extended
by signed middle-read cover92380db9/report7506b927. The supplied O is the
(a,b,c)=(2,1,3),s=2 member of the now signed interleaving familyb5f64068.
The signed COMPLETE READ extreme lemma2d5bb1e6/report4d51e33e implies actual
read minimum0 and maximum20, with T20=N singleton. These are not field extrema,
wake-span bounds imposed on even traffic, or C/L potential extrema. The full
read support lies on the RIGHT of its single-used F circle, so nothing reads
below0. Its maximum is an odd class, so no even-read classes may hide above20.

We name the empty READ classes-3,-2,-1 and21,22,23. All other unnamed classes
remain UNKNOWN. The decisive rejection leaves T13 completely unassigned.

## Why the search domains are complete without a multiplicity cap

At a cell, first read is R and turns alternate R,L. If one incoming port has
I uses and one perpendicular outgoing port has J uses, partition those uses
between even and odd ranks. Counting the two rank parities gives
n <= 2(I+J)+1. This loose derived bound works for either boundary orientation.
We enumerate every word over that cell's invariant incoming axis up to this
bound, with n odd exactly on O. Each actual first-return path to the SAME
physical cell enforces that its incoming port ordinal is the next read after
its outgoing ordinal. Such paths are recorded with complete drift voltages.
No exterior path is supposed absent unless excluded by the actual extrema.

The recorded domains are checked by the literal ordinal successor graph.
Rejections carry one of:
- a complete physical return skipping a chronological read rank;
- a closed difference-inequality cycle C+K*P>0, with K>=0 and positivity already
  at P equal to the number of distinct named events;
- a closed actual event component, either impossible winding or demonstrably
  proper because other named events remain outside it.

The graph uses each chronological ordinal on both physical ports, not just
undirected flow counts. Incoming WHITE histories are complete histories, not
histories merely observed in a finite factor.

## Top boundary propagation

Starting from T20=N, exact count and return constraints give:

T19=EW; T18=NN; T17 in{EWWW,WWEW}.

At T16 there are exactly three complete candidates after actual returns:
(T16,T17)=(NNNNSS,EWWW),(NNSSNN,WWEW),(NNSNNS,WWEW).
Their five complete T15 extensions have three skipped-rank obstructions, one
positive-clock cycle and one survivor. Thus

T15=EWWEEW; T16=NNSNNS; T17=WWEW.

The five T14 extensions have three skipped-rank obstructions and exactly

T14 in{NNSSNSNN, NNSSNNNS}.

All these lengths are derived. The largest loose domain bound used on this
side is13. Neither a finite period nor any unread lower boundary is assumed.

## Bottom boundary and meeting

T8 is odd in O. The two complete possibilities are NNSSSSS or SNSSNSS, and
T9=WEWEWEWE. Their16 T10 extensions leave four open pairs after12 explicit
positive-clock cuts:

(T8,T10)=(NNSSSSS,SNSSSSSSSS),
(SNSSNSS,NSSSSS),(SNSSNSS,SNSSSSSSSS),(SNSSNSS,SSSNSSSSSS).

Combine these four lower interfaces with the two upper interfaces. They are
all locally open before T11, with T11,T12,T13 unknown. Both outgoing ports of
T11 are now known: five S moves feed T8 and five N moves feed T14. Consequently
T11 has EXACTLY10 reads, not an assumed bound. Enumerating its124 complete
words gives68 positive-clock cuts,12 skipped ranks and44 open interfaces.

For each of those44 interfaces, BOTH incoming ports of T12 are fixed: eight N
arrivals from T9 and four S arrivals from T15. Thus T12 has EXACTLY12 reads.
Thirty-one parents have empty complete T12 domains after their recorded
first-return constraints. The other13 parents supply58 complete words:

43 have a skipped read rank;
9 have an explicit positive-clock cycle;
6 have a proper30-event component of winding+1, with67 other named events.

There is no surviving interface. In particular, the six positive-winding
components are not rejected merely for being cycles: their explicit outside
events make them improper pieces of the required single actual event orbit.
No claim is made that the unknown T13 must be empty; every contradiction is
already fixed by the named events and persists under arbitrary T13 traffic.

## Auditable artifact and scope

`certify_drift31_inventory20.py` regenerates the complete case tree in under a
second here, using simple finite word enumeration and literal port/clock
calculations. `drift31_inventory20_certificate.json` records every parent,
complete domain, same-physical return, rejected word and obstruction. It has
no solver status, timeout, or opaque UNSAT premise.

This removes ONE exact supplied full odd inventory from the live two-quad
branch. The symbolic family s=2,c>=3,1<=b<a<=c remains open except for this
specific triple and the previously excluded c2 case. There is no unconditional
single-used F-circle existence theorem for arbitrary full drift(3,1), no
classification of growth8, and no alternative finite-seed controller.
