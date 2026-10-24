# Mixed departure second lane forces an actual open junction

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Let gamma be a b-circle at selected GLOBAL C maximum M, with NO
single-used edge. Its physical flows may be 2,3,4. Author structural proof
pending independent review. No critical K1 assumption is needed here.
All odd source/sink and late-L3 ports remain present.

The signed whole-segment reduction a5d8cd2a leaves maximal flow3 macros
with turn templates RR,RLR,RLRR,RRLR,RRLRR, at most four physical edges.
Under the no-one-use premise their endpoints are source EWE(2->3) and
sink EEE(3->2), not the one-use rerouting alternatives. Interior RIGHT
signs EEEW/EWEE remain both possible. Every flow4 block is the signed
isolated EWEW->SSSS pair from 2->4->2. All other cycle vertices have flow2
on both adjacent cycle ports.

THEOREM. At least one of the following genuine exterior-lane junctions
occurs on gamma:

    a flow2 RIGHT contact EEWW/EWWE;
    a flow2 LEFT O/U contact WEE/WEEW;
    a longer flow3 macro RLRR, RRLR or RRLRR.

Its exact exit port is recorded below and in the executable control.
This does NOT exclude that port's exterior completion or bound how many
such junctions can repeat. It identifies an actual quotient-cycle
obstruction to the complementary closed macro library.

## 1. The persistent lane through each short macro is ACTUAL

Choose ordinal SECOND on every physical flow2 edge between macros.
For a short flow3 RR macro, the actual ranks are

    source.R2 -> sink.R2.

The middle physical edge is used at ordinal THIRD. At the sink R2 the
outgoing flow2 port is ordinal SECOND again. For a short flow3 RLR macro,
the actual path is

    source.R2 -> LEFT.L3 -> sink.R2.

Both internal flow3 edges use ordinal THIRD, and the output is again
SECOND. The first/second copies, crossing L1/R2 ranks and odd endpoint
histories still exist; selecting this one lane does not erase them.

For the isolated flow4 block, its source.R2->target.R2 edge uses ordinal
THIRD internally and restores ordinal SECOND on output. Its source/target
L1 and L3 bypass channels are retained separately, not spliced away.

At a flow2 LEFT V=WWEE contact, ordinal SECOND arrives and departs at
its ACTUAL L3. Thus this contact preserves the same lane too.

All these are uninterrupted actual successor edges/ranks. There is no
repaired-sheet transition or clock wait at a different rank of a cell.
The control derives them from complete physical port ordinals.

## 2. The other finite macros have exact open exits

At a flow2 RIGHT X=EEWW, ordinal SECOND arrives at L1, which exits through
its exterior LEFT port. At RIGHT Y=EWWE it arrives at L3, which also exits
LEFT. At a flow2 LEFT O/U it arrives at R2 and exits RIGHT. These are real
port uses, not a charge for a missing source.

Every longer three-macro stops the incoming second lane as follows:

    if its leading internal RIGHT is EEEW, the lane reaches the following
      LEFT.R2 and exits RIGHT;
    if that leading RIGHT is EWEE, it reaches its L3 and exits LEFT;
    with no leading internal RIGHT but a trailing EEEW, it reaches the
      sink.L1 and exits LEFT;
    with no leading internal RIGHT but trailing EWEE, it reaches that
      RIGHT.L3 and exits LEFT.

When both internal RIGHT contacts exist, the leading exit is the first
one encountered. The actual physical target coordinate and heading of
all eight longer-macro cases are retained in the control JSON. A target
may be another gamma vertex by a physical chord: that is an additional
known junction, not permission to declare the exterior empty.

## 3. Whole-cycle contradiction if no such junction occurs

Suppose none of the listed exits occurs. Every remaining flow2 contact
is LEFT V, every maximal flow3 macro is RR or RLR, and every flow4 block
is the exact isolated pair. Their matched input/output second ordinals
therefore compose to an uninterrupted ACTUAL successor path along gamma.
The path selects one genuine read at each physical b vertex, following
every physical gamma edge once. Its ordinal changes to THIRD inside the
short flow3/four macros are exactly reversed at their output.

Gamma winds -1 in the ACTUAL full-drift cylinder. Starting at its selected
rank at v, the lifted path would return to the same rank at v-d after
ell positive physical steps. Complete-front equivariance instead says

    T(v-d,rank)=T(v,rank)-P.

Thus -P=ell>0, impossible. This is an actual time/orbit contradiction,
not an upper bound on abstract exchange genus or an assumed simple
uninterrupted R0 spine.

## 4. What remains open

The conclusion forces a finite junction type, not single use. Its exit
may connect through arbitrary older LEFT/RIGHT stock, odd output roots,
other macros or nonlocal physical chords. At critical M=c_right+1 the
signed mixed first-track pipeline d5acded4 can additionally constrain
those crossings by same-contact LEFT returns, but the present lane proof
does not assume that critical specialization.

No bound on period, total macro count or repeat count follows. No local
open profile is promoted to an attained complete WHITE front. A complete
junction composition must still check every actual port ordinal, all
full-drift voltages and the one full event orbit; the next task is that
exterior composition rather than a numerical segment-length scan.
