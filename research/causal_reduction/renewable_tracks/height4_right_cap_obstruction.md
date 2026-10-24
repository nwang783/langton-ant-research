# No renewable right cap confined to rows 0 through 4

Status: elementary all-width/all-length argument; independent analytic audit
passed for the rows0..4 theorem and the final companion/span extension.
This applies only to the right cap J in `mixed_shuttle_architecture.md`, with
entry/exit(0,0,E), vertical renewal(0,4), and every cap read in 0<=y<=4.
There is no bound on horizontal extent or duration. Caps extending below0
or above4 are NOT excluded.

## Exact entry field under the complete-history hypothesis

Immediately before a sufficiently advanced J, all rows y=1,...,4 are white:
previous caps are shifted downward by at least4 and have maximum read height4;
previous W sweeps lie at y<=-1; incoming S reads only rows-1,0. On row0,
incoming S leaves every x<0 black and never touches x>=0. The latter positions
have some finite black set A supplied by previous cap reads in row4. There
are no other reads in this isolated endcap model. Thus the relevant entry
field is exactly

    { (x,0): x<0 or x in A },  with finite A subset {0,1,2,...},

and white above row0. Unread cells below0 do not matter unless the cap leaves
its stated read strip. The argument uses the assumed complete-history legality
of incoming arms; it does not treat their prescribed colors as arbitrary.

## A one-dimensional first-gap classification

Let r be the first nonnegative integer absent from A. It exists because A is
finite. Bits beyond r are irrelevant to the following trace.

* r=0: the first R moves from(0,0,E) to(0,-1,S), leaving the strip.
* r=2k, k>=1: the forced word

      L (RRLL)^(k-1) RRLR

  ends at(2k,-1,S), leaving the strip before any return to the entry pose.
* r=2k+1: the first return to(0,0,E) has the exact word

      J_k = L (RRLL)^k RRRR (LLRR)^k L RRRR LL.

  It has length8k+12 and signed turn excess4. Every read lies in rows0,1,2.

For the odd case, the initial L erases(0,0) and enters(0,1,N). Each RRLL
packet advances two columns east, writes the two upper cells and erases the
two next row0 black cells. The RRRR loop uses the first white gap at2k+1.
Each LLRR packet returns two columns west, erasing the upper pair and restoring
the lower pair. The final L RRRR LL is a fixed left-end return. The even case
is the same outward sweep stopped at an even-position gap.

Immediately after J_k, the relevant field is:

* row0: black at every x<=-2 and at x=0,...,2k+1; x=-1 is white;
* row1: black exactly at x=0 and x=2k+1;
* row2: black exactly at x=-1 and x=0;
* row3: white.

Unvisited bits to the right of the gap are unchanged. This table follows from
the two disjoint packet sweeps and the two literal four-turn loops above.

## There is no later return hidden after J_k

The field after J_k supports W20 forever to the west. One exact induction guard
at an entry(q,0,E) is:

* row0: all x<=q-2 and x=q black; x=q-1 is irrelevant;
* row1, x<=q: only(q,1) black;
* row2, x<=q-1: only(q-1,2) black;
* row3, x<=q-1: all white.

All other cells are outside the entire future read set. A literal W20 check
sends this guard to the same guard with q replaced by q-2. It writes only
irrelevant outgoing row3 cells(q-2,3),(q-1,3), apart from updating the moving
boundary. The post-J_k table satisfies the guard at q=0. W20 never returns to
(0,0,E) after its initial entry: its first period reads x=0 only at(0,0) and
(0,1), neither is an intermediate entry-pose return, and later periods have
x<=-2. Hence no longer finite cap can be obtained by concatenating more return
excursions after J_k.

## Renewal contradiction

Every candidate J restricted to read rows0..4 therefore either exits the strip
or equals one J_k. But J_k reads no cell in row4, so it cannot supply the black
entry bit(0,0) needed by the next vertically translated cap. Equivalently,
the complete class(0,0 mod4) has read string LRL: the initial J_k L, its later
R at(0,0), and the outgoing W20 L. Its first read is black, contradicting fresh
white input arbitrarily far along the vertical front. Thus no such J renews.

`height4_right_cap.py` is a finite control, not this proof: all32768 initial
row patterns through width16 either returned or left the strip within68 steps,
with exactly the eight J_k for0<=k<=7 and no valid complete cap. The analytic
first-gap classification handles arbitrary finite A and all lengths.

## Companion lower-strip argument and span corollary

The preceding 0..4 theorem and the following companion argument have both
passed independent analytic review. The cap is fixed across translated epochs;
a shorter phase preceded by a taller phase is not covered by this statement.

If every cap read has y<=2, no earlier translated cap can affect row0 or row-1
at the current entry. The prescribed arms leave row0 black exactly for x<0
and row-1 white. The forced word is RRR(LLRR)^infinity, escaping west without
an entry-pose return. Hence every renewable right cap must reach height at
least3.

If every read lies in -1<=y<=3, the entry field in those rows is the same black
negative half-row0, together with an arbitrary finite A on row-1 at x>=0.
All cells in rows1,2,3 are white, and nonnegative row0 is white. Earlier cap
row3 writes supply A; the legal incoming S arm leaves negative row-1 white.
Let r be the first nonnegative white position of A. The initial R enters
(0,-1,S). Each LLRR packet advances two columns east through a black pair
on row-1, erasing that pair and writing the corresponding upper row0 pair.

* If r=2k, the forced trace is R(LLRR)^k RR followed by (LLRR)^infinity
  in heading N, now moving west. This undoes the upper rail and then continues
  along the pristine negative input half-row. It never returns to(0,0,E).
* If r=2k+1, the word R(LLRR)^k LR ends at(2k+1,-2,S), leaving the strip.

Thus no cap restricted to rows-1..3 can return, regardless of horizontal
extent or the finite word A.

Consequently every FIXED vertically renewed right cap has vertical read span at least5.
Indeed its entry read is at height0. If the maximum read height is<=2 it is
excluded by the first case. For maximum3 and span<=4, all reads lie in-1..3;
for maximum4 and span<=4, all reads lie in0..4. A maximum>=5 already has span
at least5 because height0 is read. This corollary requires at least six
integer row levels, but does not exclude wider or taller renewable caps.
