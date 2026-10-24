# A third-row charge from literal finite excursions

This note extends `fresh_excursion_diamond_accounting.md`. It concerns actual\
finite ant trajectories and explicit physical first returns. It makes no\
assumption about the initial colors of the B or C rows. It is a proposed\
analytic lemma independently reviewed by the parent and literature analysis,\
not a convergence theorem. Their audits found no gap; this is not a formal\
proof-assistant verification or a priority claim.

## 1. Setup

Write

```
T_r=(r,-r), A_r=(r,-1-r), B_r=(r,-2-r), C_r=(r,-3-r).
```

Take a finite ant trajectory segment that starts and ends at `x+y<=-4`,\
stays in `x+y<=0`, and initially has every T and A cell white. Use the\
heading sector in which a top visit has incoming heading E. Rows B and C,\
and all lower rows, may start with arbitrary colors.

All visit counts below count processed events, including the last departure\
from a visited cell. The endpoint condition ensures that none of the T,A,B,C\
rows has an unfinished initial or final event.

For any row X, define Delta_X as the finite sum over its visited cells of\
`final black indicator - initial black indicator`. Equivalently it is the\
number of white events minus the number of black events on that row. This\
definition remains meaningful even if an unrestricted old row contains\
infinitely many initially black cells; no subtraction of infinite\
populations is used.

By the diamond lemma, every visited top cell is visited once, and its visit\
belongs to the four-step first return

```
B_(s-1) -> A_(s-1) -> T_s -> A_s -> B_(s-1),
```

with directions N,E,S,W. The two B endpoint visits are consecutive. Exactly\
one of them is a white upper corner, with incoming heading W and outgoing N.\
We call that corner the corner charged by T_s.

A complete A cell means that both of its top neighbors are visited. It has\
one upper arrival and one upper departure, and its word is one of

```
F3=100, F4=1000, R3=001, R4=0010.
```

It has b=1 black event in the three-visit case and b=2 black events in the\
four-visit case. The black events are at visit rank 1 and, if present, 3.\
Every black A event has incoming heading N and outgoing W. Its unique\
upper arrival and upper departure are white events, at ranks 0 or 2.

The one-sided A words, when just one top neighbor is visited, are 0 or 00\
for only the right top neighbor, and 1 or 10 for only the left top neighbor.\
Their only possible black event is rank 1. An A cell with neither top neighbor\
visited has no events.

## 2. Local lemma

Let A_s be any visited A cell. Suppose each of its two neighboring B cells\
has exactly the number of white upper corners charged to it by a visited\
top cell: zero if that top cell was not visited, and one if it was. When a\
corner exists it is necessarily the charged corner. Let b be the number of\
black events at A_s, so b is zero, one or two.

**Claim.** C\_(s-1) has at least b black upper corners, where b is the number\
of black events at A_s. A black upper corner at C has incoming heading S\
and outgoing E.

### 2.1 Each black A event gives a physical first return to C

Fix one black event at A_s. It is reached from B_s and leaves for B\_(s-1).\
Trace the incoming side backward.

- If its predecessor B_s event is black, that event has incoming heading E\
  and outgoing N. It was therefore reached directly from C\_(s-1).
- If its predecessor B_s event is white, it is an upper corner of B_s.\
  Therefore the right top neighbor was visited, and this is its unique\
  charged corner. It cannot be the first endpoint of the top diamond: that\
  endpoint departs to the *white* upper-departure event of A_s, whereas our\
  target event at A_s is black. It must be the second endpoint of that\
  diamond. Trace the diamond backward to its immediately preceding B_s\
  visit. That visit is black, has incoming E/outgoing N, and was reached\
  directly from C\_(s-1).

Thus the incoming side is C to B_s to A_s, possibly with the four-step\
diamond through T\_(s+1) inserted at B_s. It never touches C in its interior.

Now trace the outgoing side forward.

- If the successor B\_(s-1) event is black, it has incoming W and outgoing S\
  and immediately reaches C\_(s-1).
- If it is white, it is an upper corner of B\_(s-1). Therefore the left top\
  neighbor was visited, and this is its unique charged corner. It cannot be\
  the second endpoint of the charged diamond: that endpoint receives the\
  *white* upper-arrival event of A_s, whereas the current A event is black.\
  It must be the first endpoint. Follow the diamond through T_s to the\
  next B\_(s-1) visit, which is black and has incoming W/outgoing S. It then\
  reaches C\_(s-1).

The resulting path is a first physical return to C\_(s-1), with base\
directions E,N,W,S and at most one four-step top diamond inserted on each\
side. All of its interior cells lie above C. It contains the chosen black\
A_s event and no other black event at A_s: the inserted diamonds only use\
the white upper-arrival or upper-departure event of A_s.

At the two endpoint C events the colors are opposite, because they are\
consecutive visits to that physical cell. The initial endpoint departs E,\
and the final endpoint arrives with heading S. If the initial C event is\
black, it is already a black upper corner. If it is white, the final event\
is black and is a black upper corner. Exactly one endpoint is a black\
upper corner. This proves the claim when b=1. It also covers the one-sided\
words explicitly:

- For A_s=00, only the right top neighbor was visited. The right B may use\
  the second-endpoint insertion just described; the left B has no upper\
  corner, so its outgoing side must be a direct black lower departure.
- For A_s=10, only the left top neighbor was visited. The right B has no\
  upper corner and the incoming side is direct. The left charged diamond\
  already occurred before A_s rank 1, so the outgoing side is also direct.

The one-visit words have b=0 and need no charge. Thus no endpoint correction\
is required in the local lemma.

### 2.2 The two returns for a four-visit A cell cannot share their charge

Suppose b=2, and consider the returns belonging to A_s ranks 1 and 3.\
They are two distinct C first-return excursions in temporal order: each\
contains exactly one black A_s event. Let u and v be their final B\_(s-1)\
events before returning to C, in visit-rank order. Both are black lower\
departures, with incoming W and outgoing S, and u\<v.

The visit at A_s rank 3 occurs after the unique white upper arrival at A_s\
(rank 0 for F4 or rank 2 for R4). Hence the diamond through T_s is already\
completed before this last black A_s event. In particular, v follows\
directly after A_s rank 3 and is not the return from that top diamond.

We show that u and v are not consecutive in the list of lower departures\
from B\_(s-1). Suppose they were. Every intervening visit to B\_(s-1) would\
then be an upper departure. Since u and v are black, their visit-rank\
difference is a positive even number. Every intervening white visit would\
be a white upper corner. There is exactly one such corner, so the difference\
must be two: the unique white corner Q is the intervening visit.

There are only two possibilities for Q in its charged diamond.

- If Q is the second endpoint, its immediately preceding B visit u is the\
  first endpoint and is an upper departure. This contradicts the definition\
  of u as a lower departure.
- If Q is the first endpoint, its immediately following B visit v is the\
  return from the diamond through T_s. It therefore follows the white upper\
  arrival at A_s, contradicting that v directly follows the final black\
  A_s event at rank 3.

Thus an additional lower departure from B\_(s-1) occurs strictly between u\
and v. Equivalently, the two C upper arrivals ending the selected returns\
are not consecutive in C's upper-arrival list.

If the selected C returns charged the same black C event, that event would\
have to be the end of the first return and the start of the second. The\
two ending upper arrivals would then be consecutive physical visits to C,\
and in particular consecutive upper arrivals. This contradicts the preceding\
paragraph. Hence the returns charge two distinct black upper corners at C,\
proving the local claim for b=2.

This proof uses actual colors and consecutive physical visits. It does not\
use parity relative to the initial B or C colors, or identify different\
translates of a cell.

## 3. Event-level charging: each extra B corner costs at most two A events

Let M be the number of visited top cells. Let E_B count all white upper\
corners on B and put

```
D=E_B-M >= 0.
```

For each B_r define

```
d_r = (number of white upper corners at B_r)
      - 1{T_(r+1) was visited}.
```

The diamond charging gives d_r>=0 and sum d_r=D.

Put `Q=2M-Delta_A`, the total number of black A events. We shall charge\
all but at most `2D` of these events, improving the cell-level estimate\
`K_C+4D>=Q` from an earlier version.

### 3.1 An extra B corner joins two black A events

Every white upper corner at B_r has incoming heading W and outgoing N.\
Its immediately preceding event is therefore at A\_(r+1), and its immediately\
following event is at A_r. If the B corner is not one of the M charged top\
corners, both of these A events are black.

Indeed, a white predecessor at A\_(r+1) has incoming heading S and outgoing W.\
It is that cell's white upper-arrival event, immediately after T\_(r+1).\
The B corner is then the second endpoint of the top diamond through T\_(r+1),\
so it is charged. A white successor at A_r has incoming heading N and\
outgoing E. It is the white upper-departure event immediately before\
T\_(r+1), making the B corner the first endpoint of that same diamond.\
Both alternatives contradict that the B corner is extra.

Make a finite event graph: its Q vertices are the individual black A\
events, and each of the D extra B corners supplies an edge between its\
black predecessor and black successor. This graph is used only to count\
incident vertices; no acyclicity or connectedness assertion is needed.\
At most 2D black A events are incident to these edges. Call the remaining\
events unmarked.

### 3.2 Every unmarked event has a C charge

For an unmarked black event at A_s, a white predecessor at B_s cannot be\
an extra corner, because that would mark this A event as the edge's\
successor. Likewise a white successor at B\_(s-1) cannot be an extra corner.\
Every white corner immediately adjoining this event is therefore a charged\
top corner.

The literal first-return construction in section 2.1 consequently applies\
to this event without any assumption about other corners elsewhere at\
those B cells. It supplies a black upper corner at C\_(s-1). One-sided A\
cells are included by the same argument.

### 3.3 Distinct unmarked events have distinct charges

Different physical A cells charge different physical C cells. A possible\
collision can therefore occur only when two unmarked black events belong\
to the same A_s. There are at most two black events at an A cell, so they\
must be its complete black-event list, ranks 1 and 3.

In this case neither neighboring B cell can have an extra corner anywhere\
in the trajectory segment. Every extra corner at B\_(s-1) would have one of\
these two black A_s events as its immediate predecessor, marking it.\
Every extra corner at B_s would similarly have one of them as its immediate\
successor. Thus both neighboring B cells satisfy the original local lemma's\
hypothesis. Section 2.2 proves that the two charges are distinct.

There are at least Q-2D unmarked events, each with a distinct charge. If\
K_C counts all black upper corners on C, we have proved

```
K_C + 2D >= 2M-Delta_A.
```

Define the nonnegative integer

```
Z = K_C+2D-(2M-Delta_A) >= 0.
```

No connectedness or component-count assumption on the finite top footprint\
is needed. An earlier version omitted one-sided A cells and included a\
footprint endpoint correction; the explicit endpoint cases and event-level\
argument remove that correction entirely.

## 4. The third-row flow inequality

Let N_C be the number of processed C events and Delta_C the change in the\
number of black C cells. The total upper arrivals and upper departures on C\
are equal and given by

```
I_C = N_B-N_A+M.
```

At an odd row such as C, white events have exactly one upper port. A black\
event has two upper ports when it is a black upper corner and none otherwise.\
Consequently

```
N_C = 4I_C-4K_C-Delta_C.
```

Substituting the exact diamond identities gives

```
N_C = 20M-12Delta_A+4Delta_B-16D-4K_C-Delta_C.
```

Substitute the exact definition of Z to obtain the third-row accounting\
identity

```
N_C = 12M-8Delta_A+4Delta_B-Delta_C-8D-4Z,
D >= 0, Z >= 0.
```

In particular,

```
N_C <= 12M-8Delta_A+4Delta_B-Delta_C-8D,
```

and, on discarding the additional nonpositive term,

```
N_C <= 12M-8Delta_A+4Delta_B-Delta_C.
```

This is an ordinary finite-excursion bound with no footprint endpoint term.\
It still permits arbitrary initial colors on B and C.

## 5. Full periodic upper rail

For a finite-support periodic trace with full physical displacement `(m,-m)`\
or `(-m,m)`\
and all m top classes visited, work in its stable physical visit lists. The\
top events are singleton white events, each A class is complete, and there\
are no one-sided endpoints. Every local proof above is a physical path and\
therefore survives wrapping the lane indices modulo m; translates must be\
kept distinct during each path. Counting one representative of each class,\
put M=m and Delta_A=O_A, Delta_B=O_B, Delta_C=O_C, where O is the\
number of odd-visit classes. Put D=E_B-m and\
Z=K_C+2D-(2m-O_A). Counting the event graph by translation classes preserves\
the preceding argument. The two endpoints of an edge may represent the\
same class; an edge still marks at most two event classes. If two black\
event classes at one A class are unmarked, every translated physical A\
cell has both black events unmarked, and the distinct-charge argument\
applies on each such physical cell. This gives

```
N_B = 8m-4O_A+O_B-4D,
N_C = 12m-8O_A+4O_B-O_C-8D-4Z,
D >= 0, Z >= 0,
```

and hence

```
N_B <= 8m-4O_A+O_B,
N_C <= 12m-8O_A+4O_B-O_C-8D.
```

For O_A=0, discarding the additional term -8D gives exactly\
`N_C<=12m+4O_B-O_C`, which generalizes the previous two-lane F4/R4\
catalogue bound. The proposed stronger coefficient\
`-12O_A` is not asserted; the explicit sparse-even necessary-prefix family\
shows why that extrapolation would require extra information.

For small m, a local path can meet other translates of a class. The proof\
requires only actual first returns and chronological rank 1 or 3 at the\
fixed physical A cell; it does not identify those different translates.\
The application assumes the complete stable-list interpretation established\
for finite-support periodic traces. Unlike the earlier directional all-R\
exclusion, this proof never uses the sign of the full displacement. A\
half-turn therefore gives the analogous bound at a full lower boundary,\
provided the corresponding stable complete lists begin on white as they do\
in the virgin tail of a finite-support periodic realization. This extension\
does not transfer any separate drift-sensitive F/R exclusion to the bottom.

## 6. A literal sharp example

Start with head (0,-4), heading W, and the single black cell (1,-3).\
All other cells are white. After 24 updates the head is (-2,-2), heading W.\
This entire segment stays at x+y<=0 and visits the top cells T_0,T_1,T_2.\
Its exact counts are

```
M=3,
(N_A,N_B,N_C)=(9,8,3),
(Delta_A,Delta_B,Delta_C)=(3,0,1),
D=1, K_C=1, Q=3, Z=0.
```

Thus K_C+2D=Q, and the refined inequality is an equality:

```
N_C=3=12*3-8*3+4*0-1-8*1.
```

The standalone script `check_third_row_sharp_witness.py` replays all 24\
elementary updates, checks the diamond endpoints, identifies the one extra\
corner edge between black A events 15 and 17, and checks the remaining\
unmarked A event 7 charges black C event 13. Its JSON output retains the\
entire trajectory and exact counts.

This example makes the refined bound sharp with the displayed other\
coefficients fixed. It does not, by itself, show that the coefficient -8\
of Delta_A is optimal after the -8D term is discarded. The exact witness\
and its literal step-by-step replay are retained separately.

## 7. Global scope

These inequalities give controlled accounting through three rows beneath a\
fresh boundary. They do not prove that successive record excursions shrink.\
The lower interface, the signed changes in old rows B and C, and excursions\
that never return below the displayed rows remain unbounded terms. No\
convergence or new global defect budget is claimed here.