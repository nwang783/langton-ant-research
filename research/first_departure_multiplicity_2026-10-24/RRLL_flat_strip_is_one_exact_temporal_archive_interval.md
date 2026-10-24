# An RRLL flat strip is one exact temporal archive interval

24 October 2026. Author analytic local identity pending independent review.
Use the ALL-Y flat strip a_j,b_j,u_j,v_j of signed c4faa17c, with k>=1.
The implication applies to ANY physical rank clocks satisfying its complete
WHITE histories and literal internal ordinals, not only the construction's
sample schedule. No exterior realization or ant splice is asserted.

## 1. The exact first/third-rank relay

Put s(p)=T1(p), e(p)=T3(p), and J_p=[s(p),e(p)) for the flat RIGHT cells.
The physical SECOND edge through each RR pair gives

    a_j.L1 -> b_j.L3,
    e(b_j)=s(a_j)+1.                                   (1)

For each internal LL bridge the complete ordinals give the ACTUAL chain

    a_(j+1).R2 -> b_j.L1 -> v_j.L3 -> u_(j+1).L3
                                      -> a_(j+1).L3 -> b_j.R2.

In particular

    s(b_j)=T2(a_(j+1))+1,
    e(a_(j+1))=s(b_j)+3.                               (2)

All these are real successor edges, not repairs or a deletion of the
interleaved R2 suppliers. Same-cell consecutive ranks are at least four
apart. Consequently the ordered interval list

    J_b(k-1), J_a(k-1), J_b(k-2), J_a(k-2), ..., J_b0, J_a0

has strictly increasing starts AND ends. Consecutive intervals overlap:
RR overlaps have length ONE by (1), and LL overlaps length THREE by (2).
Any interval and the interval two places later are disjoint, with a gap
at least four. Thus there is no hidden third overlap or age assumption.

For example e(b_j)=s(a_j)+1 while the next b start is
s(b_(j-1))=T2(a_j)+1>=s(a_j)+5. The other parity follows from
 e(a_j)=s(b_(j-1))+3 and s(a_(j-1))>=s(b_(j-1))+7.

## 2. Pointwise identity, retaining ALL old copies

Let U be the single positive interval

    U=[T1(b_(k-1)), T3(a_0)).

Let B_int(t) count the selected internal b-edge unit intervals of the
strip. They are precisely the RR overlap paths (one edge each) and the
LL overlap paths (three edges each). There are4k-3 such physical edges.
At every regular time on the physical line,

    sum_(j=0..k-1) (1_Ja_j + 1_Jb_j) = 1_U + B_int.    (3)

This is not merely an age sum. The long strip is a temporal RELAY:
its single-copy live Y multiplicity is one on the union and two exactly
on its selected internal boundary paths, independently of k.
Integrating gives

    sum_j (age13(a_j)+age13(b_j))
         = |U| + (4k-3).                              (4)

Both |U| and every separate age may be arbitrarily old. The strip has
one effective archive interval, not a fresh archive paid by every RR.

If this is embedded as a proper segment of a full P,d boundary with
distinct quotient event classes, sum (3) over ALL P-translates. Then

    nY_strip = nU + B_int

still holds, including multiple simultaneously live physical copies of
U or any flat. In the global pointwise identity5671be02, B_int cancels
EXACTLY from the two sides when the strip's Y terms are replaced by nU.
No arbitrary old copy is discarded. This is a valid temporal-cochain
reduction for critical matching, not an extra resource inequality.

## 3. Geometry and ports that must NOT be erased

The effective interval is the backward temporal transition from the
selected incoming rank a_0.L3 to outgoing rank b_(k-1).L1. It still has
spatial displacement (2k-1,0), signed turn +2, and every exterior channel
of the original rectangle. It is NOT one ordinary flat vertex or an
instantaneous legal head move. No physical flow subtraction, prepared
word, quotient orbit or exterior connector is produced by (3).

In particular the literal channels/ports in c4faa17c remain available
and obligatory; their elimination is not authorized by a cochain identity.
A curvature proof must retain +2 even though the temporal archive count
has been reduced to one interval. Any full-drift embedding must retain
the displayed spatial displacement and all voltages.

If the strip's two END flat histories are changed to X, the general
oriented-cochain telescoping still holds with the actual selected endpoint
times, but its effective interval may reverse sign. The positive relay
proof above is ONLY for the stated all-Y strip. No end-X old supplier
is silently converted into a positive Y interval.

Files: check_RRLL_strip_temporal_relay.py/json. Their finite controls test
the all-index formula; the proof of arbitrary k is equations(1)-(3).
