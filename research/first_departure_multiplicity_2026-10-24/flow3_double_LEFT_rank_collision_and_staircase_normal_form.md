# Flow-three double-LEFT rank collision and staircase normal form

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Segments lie on an ACTUAL b-cycle, hence have constant selected C
height c and the signed corner alphabet. Author proof pending review.
The local double-LEFT obstruction needs no global-height bound. This
strengthens, rather than alters, the signed five-edge note 0a4a6a90.

## 1. Complete neighboring modes, including one-use endpoints

Suppose a constant-flow-three segment contains two consecutive LEFT
corners. Normalize the physical path around three edges of a unit square:

    A=(0,1) -> Z=(0,0) -> Y=(1,0) -> B=(1,1).

Both adjacent LEFT histories are fixed:

    Z=NSSS, Y=WEEE.

The preceding RIGHT A must have outgoing cycle flow3; its complete four
possible histories are

    EWE(2->3), EWWW(1->3), EEEW(3->3), EWEE(3->3).

The following RIGHT B must have incoming cycle flow3; its four histories
in the rotated N-input frame are

    NNN(3->2), NNSN(3->1), NNNS(3->3), NSNN(3->3).

Thus all 16 cases include both one-use rerouting endpoints, the two odd
source/sink modes and both internal RIGHT signs. The physical B->A W
edge closes the unit-square stencil but is not assumed a b edge.

## 2. All ten port-compatible cases give literal rank contradictions

Six choices fail full physical port counts. In the remaining ten cases,
ALL physical ordinal edges force one of these consecutive four-step
returns, with no intermediate Z read:

    A=EWE or EWEE, B=NNN or NNNS:
      Z.R0 -> Y.L1 -> B.L1 -> A.L1 -> Z.R2.

    A=EWWW, B=NNSN:
      Z.R0 -> Y.L1 -> B.L1 -> A.L1 -> Z.R2.

    A=EEEW, B=NNN or NNNS:
      Z.R0 -> Y.L1 -> B.L1 -> A.L3 -> Z.L3.

    A=EWE or EWEE, B=NSNN:
      Z.L3 -> Y.L3 -> B.L3 -> A.L1 -> Z.R2.

    A=EEEW, B=NSNN:
      Z.L3 -> Y.L3 -> B.L3 -> A.L3 -> Z.L3.

The first two groups skip Z.L1; the third skips two Z ranks. The fourth
runs backward to an earlier Z rank. The last closes an unchanged actual
event suborbit. Every failure is independent of unknown readers, older
stock and other exterior ports. The cap-four alphabet is used to derive
these profiles, not to forbid an unlisted supplier by assumption.

Hence a constant-flow-three segment has NO consecutive LEFT contacts.
The companion control enumerates exactly these 16 local profile pairs
and extracts every displayed actual route; it is not a period scan.

## 3. All-length geometric normal form

The signed RR-square obstruction 0a4a6a90 forbids LRRL at ANY selected c.
Three equal geometric turns close a physical square and are forbidden on
an essential embedded b-circle. With LL now excluded too, any two LEFT
contacts must be separated by exactly ONE RIGHT: a separation by two
RIGHT would be LRRL, and three RIGHT would close a square.

Thus every whole constant-three segment is an alternating diagonal
staircase in its body, with at most two leading and two trailing RIGHT
vertices. In symbols, if it has n>=1 LEFT contacts, its necessary turn
language is

    R^a (LR)^(n-1) L R^b,  with a,b in{1,2}.

If it has none, it is RR. This normal form imposes no upper bound on n
at a nonmaximal level; a higher-C shield remains possible. Every late-L3
source, first-R spine and G3 middle clock is still given by the exact
signed whole-segment interface b955fed1.

At a LOCALLY MAXIMAL selected C component, the signed LRL obstruction
also applies. Therefore n<=1, leaving only the five templates

    RR, RLR, RLRR, RRLR, RRLRR.

There are at most five vertices, hence at most FOUR physical edges,
with all one-use or odd source/sink endpoints retained. This is a
structural all-length reduction, not an empirical cutoff. The number
of segments, their ages, the period, odd stock supply and complete
variable-flow event orbit remain unbounded and unresolved here.
