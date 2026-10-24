# Three exact outer modes at a four-edge extremal circle

24 October 2026. Author analytic refinement, submitted for independent review.
No arbitrary visit cap, width bound, or period cutoff is imposed.

Use the canonical hypothetical four-edge E circle from the independently
signed G8_EXTREMAL_CYCLE_FRONTIER.md (0e3f0ea3): full d=(2,-2), row t=-1
singleton W histories, row t=0 complete SSN/RLR histories. For this note's
first-row conclusion the global growth need not be eight. The conclusion
for the NEXT row uses g8's already proved absence of further odd Q cells.

Let A=(x,1-x) be either full-drift class in row t=1. From its two neighboring
SSN triples, A has exactly TWO incoming E occurrences and exactly TWO
outgoing S occurrences. Every other incoming heading is W; every other
outgoing heading is N. Nothing is assumed about its upper neighbors.

Denote the two E ranks by e0<e1 and the two S-departure ranks by s0<s1.
Start with A's first S departure. Its successive geometric positions are

    A=(x,1-x), B=(x,-x), T=(x-1,-x), B'=(x-1,1-x), A.

The three intervening reads are respectively B's FIRST R, T's singleton
R, and B's LAST R at the translated neighboring B class. The final A
arrival is its SECOND E arrival, by exact physical edge ordinal matching.
No intermediate position is A. Therefore this is a literal FOUR-STEP
FIRST RETURN to the same physical A cell, with no omitted complete rank:

    e1 = s0 + 1,       clock(e1) = clock(s0) + 4.       (1)

This does not claim that the initial A turn itself is R. It may be L.
Prepared higher cells cannot change this four-step identity because no
higher cell occurs in its interior.

## Exact analytic classification

Let n be A's total history length and a the number of its two E arrivals
at even (R) ranks. S departures occur at even E ranks and odd W ranks.
Their total is therefore

    2 = a + (floor(n/2) - (2-a)),
    floor(n/2) + 2a = 4.                               (2)

If a=2, n<=1, impossible with two E arrivals. If a=0, n is8 or9, both
E ranks are odd, and every S departure has odd W rank. Equation(1) would
make odd e1 equal odd s0 plus one, impossible. Hence a=1 and n is4 or5.

If s0 is even, it is e0. Then e1=e0+1. If e0>=2, the earlier odd W at
rank1 would already be an S departure, contradiction. Thus e0=0,e1=1,
and the complete incoming word is EEWW or EEWWW.

If s0 is odd, it is a W rank and e1=s0+1 is even. The other E rank e0 is
odd. With n<=5, s0=1 would force e0=1, contradicting that s0 is W.
Consequently s0=3,e1=4,e0=1, and the word is WEWWE.

These are exactly the THREE necessary complete heading words:

    X = EEWW  (n=4),
    Y = EEWWW (n=5),
    Z = WEWWE (n=5).

Their read letters are always R,L,R,L,... . Equation(1) is satisfied in
each word. This is a necessary mode classification, not a claim that
arbitrary neighboring mode choices are jointly realizable.

All four physical directed ports at each such A are used at least twice:
its E-in and S-out counts are2, and its W-in and N-out counts are n-2.
By the signed single-use lemma, no E edge can enter or leave ANY A cell.
Thus the next row consists of isolated vertices in E. The full first/last
causal graph really loses these middle-rank interactions; there is no
justification for charging an additional extremal edge through this row.

## The next even row has a DERIVED bound of twelve

At g8 the next Q row t=2 has even histories. Its lower incoming count I
and lower outgoing count J are each at most3, since the adjacent A upper
port counts are2 or3. If X counts incoming N events at even ranks, then

    J = I + n/2 - 2X,     0<=X<=I,
    n = 2(J-I+2X) <= 2(I+J) <=12.

This is a consequence of the forced E-circle geometry, not an externally
chosen global visit cap. Higher rows have not been bounded uniformly.

For equal adjacent A parity bits, the possible count-only Q totals are
4 or8 (both A even), and4,8,12 (both A odd). For mixed bits they are6 or10.
The complete heading choices and all ordinal chronology still matter.
Neither a negative opaque solver status nor a finite patch without all
phase/geometry obligations is used as a proof of exclusion.

## Local independent-check interface

The three-mode proof is purely analytic. It can be checked by enumerating
the22 count-compatible words of lengths4,5,8,9, computing their E/S rank
lists, and retaining e1=s0+1: precisely X,Y,Z survive. That finite list is
not an arbitrary multiplicity enumeration; (2) proves its completeness.
The existing signed seventeen-event open interface uses Y and X, so the
refinement does not empty the previously retained local interface.
