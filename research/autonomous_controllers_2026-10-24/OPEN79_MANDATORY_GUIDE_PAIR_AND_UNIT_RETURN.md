# Mandatory guide-pair restoration and a forced physical unit return

24 October 2026. Author proof, with exact finite controls, submitted for
independent review. This is conditional on the signed OPEN79 gap3 fork.
All named histories are COMPLETE. All higher histories, periods, excursion
lengths and visit multiplicities remain unrestricted.

## Result

Use the physical coordinates and prefix from aebe0b7c and 9287061e:

    X=(2,1), Q=(1,1), A=(1,0), B=(0,0),
    U=(0,1), V=(-1,1), C=(-1,0), Z=(2,0).

The prefix at times 0 through 6 reads X S/R, Q W/L, A S/R, B W/R,
U N/L, V W/L and C S/R. These are C rank8, X rank0, A rank2 and B rank8.
Let J be the physical open excursion between C ranks8 and9.

Every legal completion has all of the following properties:

1. U is read EXACTLY ONCE inside J, arriving S and turning R. Hence the
   X-first alternative of the earlier two-port theorem cannot by itself
   complete J. It must subsequently reach the U-restoration port too.
2. V has EXACTLY THREE reads inside J, consecutively W/R, E/L, E/R.
   The W/R read immediately follows U's restoration. The final E/R read
   immediately precedes the return to C rank9. The two intervening first
   returns to V have no asserted length or support bound.
3. C rank9 is followed by the literal physical square

       C(S,L) -> B(E,L) -> U(N,L) -> V(W,L) -> C(S,R).

   Thus t_(12,10)-t_(12,9)=4 exactly. U and V's restored BLACK lifetimes
   are consumed in that square. They are not free permanent guides.

These are actual physical read identities, including their previous R/L
owners, not statements merely about parity counts or reduced clock phases.

## A locked future named chain

Reconstruct the complete internal successor graph by physical port ordinals
with the full drift (3,1). Its retained 35-read chain starts at C rank11.
It reaches Z rank0 after 25 steps, X rank2 after26, Z rank1 after29,
Z rank2 after33, and X rank3 after34. Every physical coordinate and voltage
is supplied in the certificate and checked by literal movement.

Consequently no Z read and no X rank2 or later read can occur before C's
rank9 return. The only W departure at X before its locked rank3 is its
already-used rank0. Its possible rank1 read departs E, not toward Q.
A's next read, rank3, departs E to Z's unique E arrival, rank3, so that A
read is locked later as well. These conclusions use the complete histories,
not a guessed empty region or a visit cap on the exterior.

B is also inaccessible inside J: after its prefix rank8, its next complete
incoming heading is E. Its physical predecessor would be C, ending J first.
At these fixed physical cells the incoming axis is invariant: U and A are
vertical; Q and V horizontal. Thus U can only be approached from the north
inside J, and Q's two possible immediate predecessors are U and X.

## U must be restored

Suppose U is not read inside J. Then Q is not read either: its U predecessor
is absent and X has no available W departure. A is also untouched. At C rank9
return the successive reads are forced:

    C(S,L), B(E,L), U(N,R), Q(E,R), A(S,L), Z(E,L).

The R turns at U and Q use their still-WHITE state after the prefix L reads.
The Z read would have to be complete rank3. Let c9 and c11 denote the actual
physical C clocks. The forced path gives Z3=c9+5, while the locked chain and
three ordinal gaps at Z give

    c11 >= c9+8,   Z0=c11+25,   Z3 >= Z0+12.

Adding gives the explicit positive-clock contradiction 0 >= 40. All clocks
are physical, so no period coefficient or lift was discarded. U must be
read in J. Its first such read arrives S because B is inaccessible; its
previous read was L, so it is an actual R restoration.

## U cannot be read twice

The first restoration turns from S to W and therefore goes to V, not Q.
Before any second U read, Q is still untouched: neither that first U read
nor X's available departures can reach it. A is still locked as above.
A second U read inside J would have to arrive S and turn L. It would then
force Q(E,R), A(S,L), Z(E,L). None of these three positions is C, so this
would reach the locked A and Z before the first return to C. That is
impossible. Hence there is exactly one U read in J.

## The exact three V reads

Before the first U restoration, V cannot be approached from U. Its only
other possible arrival is E from the west. Since its previous read was the
prefix L, that first V reimport would be R, departing S immediately to C.
It would end J without the mandatory U restoration. Therefore V has not
been revisited when U's restoration reaches it.

That read is consequently W/R, restores V, and departs north. Any later V
read inside J must arrive E: a W arrival would require another U read,
which was just excluded. The next E arrival turns L and departs north. The
following E arrival turns R, departs south and ends J at C. There cannot
be a fourth V read inside J, and the C return's required S arrival requires
this final V departure. This proves the precise W/R, E/L, E/R block.

At that return, C and B are BLACK after their prefix R reads, U is BLACK
after its unique restoration, and V is BLACK after its final R. Hence the
four L turns around C,B,U,V are forced, followed by C's rank10 R. No exterior
cell is read in this square.

## Genuine finite controls and the non-gluing countercheck

The certificate retains complete initial and final fields for three SEPARATE
controls. They establish that the displayed local operations are physical;
they do not collectively realize the complete OPEN79 interface.

- The signed 17-read U-restoration factor extended by the immediately forced
  V R is a genuine 18-read factor on its six explicit BLACK inputs. This
  realizes both guide restorations together.
- A standalone higher motif starts at V incoming W and has word
  RLLLLRLLRLLRLRLLRLLRR. Its V reads are W/R at0, E/L at4, E/R at20, and it
  then reaches C incoming S. It has twelve explicit BLACK inputs, never
  reads U, and every read has normal level at least13. It demonstrates a
  physically possible pair of higher return excursions of lengths4 and16.
- Starting at C incoming S with exactly C,B,U,V BLACK, LLLLR clears the
  three other cells and leaves C BLACK. The full field is retained.

The standalone higher motif CANNOT simply be appended to the retained
17-read restoration factor: the certificate gives an explicit same-turn
physical collision. No connector, unread field or clock completion has
been silently discarded. A separate bounded search for full first-return
completions was inconclusive and is not a theorem premise.

## Scope and next obligation

This is an exact state transition, not monotone stock: the guide pair is
restored and then consumed. B's prefix-born BLACK lifetime is also consumed
in the square, so the local state does not return unchanged. The two higher
V excursions still require a completion compatible with the full named
chronology and all unknown higher histories. No finite-state quotient,
repeated debt growth, total period bound, full WHITE front or alternative
regenerative controller is established. Longer outer gaps and other OPEN79
clock placements remain outside this conditional fork.
