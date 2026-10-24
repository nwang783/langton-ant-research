# The fresh-A cap-shift inequality at an unfinished endpoint

21 October 2026. This proof extends the completed-segment result in
`../global/fresh_a_cap_shift_inequality.md`. It is a proposed exact lemma
checked in an independent internal mathematical review. It has not received
formal verification or external review. It does not prove global highway
capture.

## 1. Statement

Use the same rows T,A,B,C and heading sector as the completed-cap theorem.
The trajectory starts at level x+y<=-4. Row A is initially white; all other
initial colors are arbitrary. Stop before any processed event leaves the cap
x+y<=0. The endpoint is not processed and may be a black T cell immediately
before the first exit.

Let L_C count processed black C lower corners. Set

    S=7 Delta_A-4 Delta_B+Delta_C-8M.

Then the following bounds hold:

| Unprocessed endpoint | Upper bound for S+L_C |
|---|---:|
| T,E | 14 |
| A,N | 9 |
| A,S | 4 |
| B,E | 5 |
| B,W | 11 |
| C,N | 0 |
| C,S | 6 |
| below C | 0 |

In particular S+L_C<=14. The T,E constant 14 is sharp, as shown by the
two-black twelve-step first-exit witness in
`../global/partial_cap_sharp_witness.json`.

These are bounds on a different row functional from the earlier third-row
prefix bound. Neither inequality follows from the other by discarding a
signed old-row term.

## 2. Remove the completed upper runs

For S, the contribution of a processed event is:

| Row and color | Contribution |
|---|---:|
| T white | -8 |
| A white / black | +7 / -7 |
| B white / black | -4 / +4 |
| C white / black | +1 / -1 |

Every completed upper run and every positive-run sponsor preceding the final
unfinished run are contained in the earlier completed part of the trajectory.
The completed-cap proof therefore shows that their total contribution to
S+L_C is nonpositive. Equivalently, truncate just before the final departure
from level -4 into C: the truncated trajectory ends below C, and the following
level -4 event does not change any of the four row counts.

If there is no unfinished upper run, this already gives the bound zero.
This includes an unprocessed endpoint C,N. Otherwise the unfinished run starts
with a processed white C event and hence starts with S contribution 1. It
contains no black lower C corner. It remains to bound the contribution of
this one unfinished run.

All processed C returns in the unfinished run are black. A white processed
return would end that run. A zero-displacement upper excursion is a literal
first return and changes its C endpoint color. Hence any completed zero
excursion in this unfinished run must be its very first excursion. Every later
completed excursion is a short or a long.

## 3. The maximum contribution of a partial upper excursion

Do not count its starting C event in this subsection; that event is already
included in the running score. The following table bounds the contribution
of the partial excursion itself:

| Endpoint | Maximum partial contribution |
|---|---:|
| B,E | 0 |
| A,N | 6 |
| T,E | 11 |
| A,S | 3 |
| B,W | 10 |
| C,S | 5 |

Here is a direct verification of the table. The first B event is either
white, with contribution -4 and immediate return to C, or black, with
contribution +4 and next endpoint A,N. If that A event is white, the score
becomes 11 at T,E. Processing a white top gives score 3 at A,S. A white A
arrival then gives score 10 at B,W. The B cell is now white, so its next read
gives score 6 at A,N. This A cell is now black. Reading it gives score -1 at
B,W. This completes a right top diamond before the first selected black A
event.

If the initial A,N event was black, the score is instead -3 at B,W. Thus at
the first selected black A event, and before reading its next B cell, the
score is

    c=-3+2a, where a is 0 or 1.

The next B event is black, giving score c+4 at C,S, or white, giving score
c-4 at A,N. A black A read in the latter case replaces c by c-11 and repeats
the same state one cell to the left. These are precisely the extra-chain
edges, and each lowers the score by 11.

A white A read instead gives score c+3 at T,E. If that top is processed white,
the next scores are c-5 at A,S, then c+2 at B,W after a white A arrival, and
c+6 at C,S after the black B endpoint. This is the optional left diamond.
Since c<=-1, none of these scores exceeds the table.

There is one extra possibility at an unprocessed record endpoint. An A,S
arrival can be black and turn E toward a previously visited top. Because A
started white, such a black upper A turn requires an earlier white departure
from that same A cell to its right top. Its outgoing top is therefore already
black. It can only be the final unprocessed T endpoint; processing it would
leave the cap. Its scores are -4 in a partial right diamond or c-12 in a
partial left diamond, and also satisfy the table.

This case analysis covers the whole partial excursion. A completed right
diamond is followed by black A events and extra edges, then at most one left
diamond. The only attempted repeated top visit can be the final endpoint.

## 4. Completed moving excursions lower the running score

A completed short contributes -4 before its C return. Processing that black
C return subtracts one more. Its total change is -5.

A completed long with k>=1 extra edges and j<=2 top diamonds contributes
1+2j-11k before its C return. Processing the black return gives total change

    2j-11k <= -7.

Consequently, if the first completed excursion is moving, every completed
excursion before the final partial one lowers the initial score 1. Adding
the partial-excursion table gives endpoint bounds

    B,E:1; A,N:7; T,E:12; A,S:4; B,W:11; C,S:6.

The same bounds hold if there are no completed excursions yet. A C,S endpoint
at the end of the current excursion is treated before its C return is read.

## 5. The four possible initial zero excursions

It remains to treat an initial completed zero excursion z_ab. Its C return
is black and has already been processed. The resulting score is

    1+2(a+b).

The three relevant colors are (B_s,A_s,B_(s-1))=(a,b,0).

If a=0, the next excursion is forced to be a short through white B_s. Before
that B read the score is at most 3; at its C endpoint it is at most -1.
If the return is processed black, the score is at most -2. Every subsequent
completed moving excursion lowers it further, so the general table in
Section 3 proves all the asserted bounds in this case.

If a=1,b=0, the current score is 3. The next three unprocessed endpoints are

    B,E with score 3;
    A,N with score 7 after the black B read;
    T,E with score 14 after the white A read.

That top was used in the preceding zero excursion. It is black and cannot be
processed under the cap. Thus this case stops there and gives the maximum 14.

If a=b=1, the current score is 5. The next events are forced: black B_s,
black A_s, white B_(s-1), and black A_(s-1). The last color is black because
the preceding zero excursion's left diamond just processed A_(s-1) white.
Their successive unprocessed endpoints have scores

    B,E:5; A,N:9; B,W:2; A,N:-2; B,W:-9.

The new excursion has no right diamond and has at least one extra edge.
If completed, its total change including the black C return is at most
2-11=-9, leaving score at most -4. If it remains partial, the same left-chain
calculation in Section 3 bounds all its later endpoints. None can exceed the
displayed bounds. All later completed moving excursions lower the score.

These cases prove the table in Section 1.

## 6. Exact record-birth bookkeeping

For actual row black counts b_j, define

    E_h=12 b_h-8 b_(h-1)+4 b_(h-2)-b_(h-3),
    R_h=8 b_h-7 b_(h-1)+4 b_(h-2)-b_(h-3).

A virgin +2 record birth starts at a black top cell on row h with incoming E.
The six turns LRRRRL preserve all old row colors and add one black cell each
on rows h+1 and h+2. At its end,

    E_(h+2)-E_h = 4-R_h.

For a cap prefix with A initially white, this note bounds the change in R_h:

    Delta R_h >= L_C-14

at a T,E endpoint. Its initial B,C contributions must remain present when
turning this into a bound on R_h itself. If all four rows were initially white,
then R_h>=L_C-14 and

    E_(h+2)-E_h <= 18-L_C.

The initial-row restriction holds for sufficiently high first record caps
above a finite initial support, when the prefix is measured from the original
starting time. It does not give a finite total budget: the number of record
births is not bounded, and the inequality has a positive allowance per birth.
No global capture conclusion follows by summing this estimate alone.
