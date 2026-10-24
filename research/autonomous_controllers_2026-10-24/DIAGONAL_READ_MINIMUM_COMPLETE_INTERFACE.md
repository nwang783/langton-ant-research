# A complete diagonal read-minimum interface, without a visit cap

24 October 2026. Author proof and explicit finite cover, submitted for
independent review. This is a necessary interface for every complete
WHITE front with full diagonal drift of coordinate magnitude two. It is
not an existence theorem or an exclusion of the acyclic growth-eight
remainder. No historical width-ten certificate is used.

## 1. The actual support object makes the first row finite

Normalize by genuine rotations and translations to full d=(2,-2) and
sigma=+1. For the complete read footprint

    R = {q_i + k*d : 0<=i<P, k in Z},     t(x,y)=x+y,

its minimum t exists. At a minimum-level read the incoming heading must
decrease t, and the outgoing heading must increase t. If the level is
even, the invariant sector forces S -> E, a LEFT turn at every read of
that physical cell, contrary to its WHITE first read. Therefore the
minimum is odd. At that level every read is W -> N, hence R; complete
alternation forces a singleton. Translate the level to -1.

There are exactly TWO full-drift classes on a level, represented by
(r,t-r), r=0,1. No primitive-drift replacement is made. Up to a physical
translation by (1,-1), the minimum row is exactly one of

    (T0,T1) = (W,empty), or (W,W).

Every other read class has t>=0. This is a minimum of the FULL READ
FOOTPRINT, not the black board, odd wake, potential terrain, or a cropped
patch. All input/output fields remain as in the complete front.

Write B0=(0,0), B1=(1,-1) for the next Q row. Exact physical port counts
from the singleton row now bound their COMPLETE histories; the rest of
the front is not visit-capped.

### One singleton

B0 has one incoming N and zero outgoing W. Its entire word is N or NS.
B1 has zero incoming N and one outgoing W. Its entire word is S or SS.
These are all four possibilities, including all allowed parities.

### Two singletons

Each B has one incoming N and one outgoing W. If n is its length and X
its number of R reads arriving N, then

    1 = ceil(n/2) + 1 - 2X.

The fixed incoming count also gives X in {0,1}. Thus n is three or four,
and the complete heading word is exactly

    SSN, SSNS, NSS, or NSSS.

These 16 paired choices and the four one-singleton choices form the
complete 20-case lower domain. No arbitrary count bound was supplied.

## 2. Exact physical chronology, with the higher region left open

For each lower choice, pair every internal directed port by its physical
ordinal. Quotient edges carry the FULL d translation voltage k. Each
internal event equation is

    time(target) = time(source)+1-k*P.

No input color beyond the complete WHITE alternating histories is chosen.
Unmatched upper ports remain OPEN. Internal chains that leave a top cell
and return to that SAME physical cell force consecutive read ranks there.
Their event durations and both port ordinals are explicitly retained.

A possible next C cell A has I incoming E and J outgoing S occurrences.
Writing a for its R reads arriving E gives

    floor(n/2)+2a=I+J, so n<=2(I+J)+1.

For each n in this DERIVED range the certificate lists all placements of
I incoming E headings on alternating R/L ranks and applies only the
literal first-return rank equations. The other heading is W. Empty
histories are allowed when the counts permit them; no support shape or
continued two-cell occupancy is imposed on the higher region.

The retained certificate has all 20 lower cases. Four are rejected at
the lower stage. The other 16 give 444 paired next-row histories after
first-return filtering. Their exact outcomes are

    214 positive rank-clock cycles;
      3 proper closed internal event components;
    227 OPEN necessary interfaces.

A solver's status is NOT a proof premise. Every rejected paired case
contains its explicit checkable witness.

### Transparent clock witness

For an internal event chain c, write x_c for the clock of its first
representative read. If rank j at a physical class appears at position a
of chain u, with lift k_a, its representative time is x_u+a-k_a*P.
For consecutive ranks j,j+1 at the same class, actual square-lattice
return time is at least four, hence

    x_v >= x_u + (4+a-b) + (k_b-k_a)*P.

These are EXACT necessary rank inequalities, without an extra chain-
nonoverlap relaxation. A stored directed cycle sums to 0>=C+K*P. Each
certificate verifies K>=0 and C+K*N>0, where N is the number of named
complete read events. Since the full period satisfies P>=N, this is an
all-period contradiction. Bellman-Ford only discovers the displayed
cycle; checking its integer sum proves the rejection independently.

The three closed-component witnesses each have four events and winding
+1, but also 16 OTHER named events and four open chains. Thus each is a
proper event component, impossible in the single actual full event orbit.
Winding +1 alone is not declared contradictory.

## 3. Human-readable surviving boundary types

The complete stored lists are the theorem's exact finite interface. Several
small reductions can be read directly from them.

### One singleton

The B1=S choice is impossible in either B0 case. Its first R, T0.R, and
B0.firstR would force the first E arrival at A1 immediately after its
first S departure. With J=1 this has no complete WHITE alternating word.
Hence B1=SS is forced. The complete surviving pairs (A0,A1) are:

    B0=N:  (WE,WWE), (WEW,WWE).
    B0=NS: (WEWW,WWEE), (WEWW,WWEEW),
           (WEWWW,WWEE), (WEWWW,WWEEW).

These are SIX open interfaces, not six physical controllers.

### Two singletons

Both B words cannot begin N. If U_i is the first N read of B_i and V_i
its rank2 S/R departure W, the lower circle gives

    V0+2 = U1-P,       V1+2 = U0.

But V_i>U_i, so their sum requires a positive number to equal -P.
The four lower exclusions are this literal clock obstruction.

The remaining complete cover additionally rules out NSS altogether.
A surviving N-first corner must be the FOUR-read NSSS, and there is at
most one such corner. Up to exchanging lanes by an actual translation,
the mixed choices have these exact next-row modes:

    (B0,B1)=(SSN,NSSS):
        (WWEEWE,WEWWWWE), (WWEEWEW,WEWWWWE).
    (B0,B1)=(SSNS,NSSS):
        (WWEEWEWW,WEWWWWEE), (WWEEWEWW,WEWWWWEEW),
        (WWEEWEWWW,WEWWWWEE), (WWEEWEWWW,WEWWWWEEW).

When both B words start S, all four lower pairs remain possible at this
stage. Their open next-row counts, with the lanes ordered, are:

    (SSN,SSN): 9;
    (SSN,SSNS): 28;   (SSNS,SSN): 28;
    (SSNS,SSNS): 144.

The 28-case one-quadruple architecture includes the genuine complete
standard104 front, as separately reconstructed in
SINGLE_USED_FIRST_CIRCLE_MIDDLE_READ_INTERFACE.md. Standard104 has g=12,
not eight; it is only a positive control for the unconditional interface.

## 4. Exact use at growth eight

The nine (SSN,SSN) cases have the previously signed four-edge E cycle.
The all-period cyclic-E growth-eight exclusion therefore removes them
at g=8. Consequently every complete g=8 front of FULL diagonal drift
(±2,±2), after the stated genuine rotations/translations, must satisfy
one of the 218 remaining ordered local interfaces:

    6 one-singleton interfaces;
    12 mixed N-first/S-first interfaces;
    56 one-quadruple S-first-circle interfaces;
    144 two-quadruple S-first-circle interfaces.

This is a COMPLETE finite boundary reduction for this drift subcase,
not a finite-width or finite-period search. The higher region and P stay
unbounded. The other growth-eight drift types remain separate. None of
these 218 cases is certified physically completable, and none is rejected
merely for being open. There is no inference that g>=12.

## Dependencies and evidence

The certificate is certify_diagonal_read_minimum.py with its complete
JSON. It uses only literal lattice motion, WHITE alternation, ordinal
matching, full-drift quotienting, and displayed rank-clock witnesses.
The proof's Section4 alone uses G8_CYCLIC_E_EXCLUSION.md8981c7ff WITH
mandatory read-footprint addendum b24cf42a, independently signed report
e1d595f2. Sections1-3 are independent of that exclusion.

This parallels the retained signed AXIS read-extreme method, but does not
import its axis-specific formulas. A search of retained proof notes found
those axis reductions; no literature novelty claim is made for this
explicit diagonal formulation.
