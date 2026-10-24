# Global-max flow-two staircase segments have one core and cannot close

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Consider a constant-physical-flow TWO portion of a first-R departure
b-CYCLE whose selected C height is GLOBAL M. Geometry in this note is a
diagonal staircase (alternating physical RIGHT/LEFT turns). Nonstaircase
double turns and multiplicity changes remain outside the theorem.
Pending independent review. No period, width, drift or segment-length
bound is imposed.

THEOREM: every sufficiently internal portion has one exact symbolic core,
A=NNSS and B=WEEW. Boundary caps are retained. This core carries a strict
last-L3 clock decrease in the actual drift direction, so a whole closed
constant-flow2 staircase b-cycle at M is impossible. This is NOT a theorem
that every b-cycle is one-used.

## 1. Complete primary alphabet and the finite exterior cover

Normalize A_k=(k,k), B_k=(k+1,k), physical path A_k->B_k->A_(k+1).
All internal RIGHT and LEFT profiles preserving flow2 are exactly

    A_X=NNSS, A_Y=NSSN;
    B_O=WEE, B_U=WEEW, B_V=WWEE.

The odd three-read LEFT mode O is explicitly included. For each symbolic
five-corner word B_(k-1),A_k,B_k,A_(k+1),B_(k+1), retain all complete
WHITE1..4 histories of D_k=(k+1,k-1), D_(k+1)=(k+2,k) and E=(k+2,k-1).
Their adjacent port counts, all zero ports, actual ordinal edges and
same-cell rank spacing are retained. Every forced physical return must
land at the NEXT read of that cell; skipped middle ranks are rejected,
not merely hidden inside a feasible difference-constraint assignment.

Finally reconstruct every incident dual-face equation and require
C<=M, normalizing the selected M face to zero. This GLOBAL maximum
premise is essential. At a non-global level a higher-C exterior shield
may evade this cover.

There are108 primary words, with5700 port-compatible D/E completions.
Exactly eight primary words have any surviving necessary completion.
Written as (Bprev,A,B,Anext,Bnext), they are

    (U,X,O,X,V), (U,X,O,Y,V),
    (U,X,U,X,O), (U,X,U,X,U),
    (V,Y,O,X,V), (V,Y,O,Y,V),
    (V,Y,U,X,O), (V,Y,U,X,U).

These are OPEN necessary rows, not attained board factors or front
positives. Their exterior ports beyond this fixed stencil remain open.
The cover is one fixed local relation used on ARBITRARILY long words,
not a scan over arbitrary periods or finite segment lengths.

## 2. Exact overlap gives the all-length language

Every surviving window has current B in{O,U} and previous B in{U,V}.
A symbol appearing as BOTH a current and previous B must therefore be U.
Where that overlap holds, the A symbol is X. Thus the interior of a long
constant-flow2 staircase segment has only the core

    ... B_U, A_X, B_U, A_X, B_U, ... .

The eight rows above explicitly retain the endpoint cap alternatives:
a leftmost V/Y cap, or an O followed by V at the right cap. They are not
silently extended through an indefinite homogeneous mode.

On a closed full-quotient staircase every symbol occurs in both roles.
Hence B is U everywhere and A is X everywhere. No smaller primitive
quotient, representative phase replacement or unproved mode preservation
is used; this is exact overlap of complete physical histories.

## 3. The unique core has a last-read monotone clock

For the core, D_k has incoming S2 and outgoing W2. Exact first-R ports
give its FIRST W departure before its FIRST S arrival:

    D.W(first)=T0(A_k)-2,
    D.S(first)=T2(B_k)+1 > T0(A_k)+2.

The complete WHITE cap-four possibilities with S2/W2 are
NNSS,NSSN,SNNS,SSNN. Only NNSS has its first W departure strictly before
its first S arrival. Thus every core D is NNSS; this is the complete
rank interface, not an assumed extra row.

Now the physical SECOND port occurrences force the actual consecutive
factor

    B_k.R2 -> D_k.R2 -> B_(k-1).L3.

Since each B=WEEW has T3(B)>=T2(B)+4,

    T3(B_(k-1))=T2(B_k)+2<=T3(B_k)-2.             (1)

This is a genuine rank3 supplier clock across the whole core. It cannot
be replaced by a source-R0-only edge or charged as fresh output.

## 4. Full closed-cycle contradiction

A staircase b-cycle with2a vertices has physical displacement(a,a),
but every complete WHITE first-departure cycle has winding-1. Thus actual
full d=(-a,-a), a>=1, and

    B_(k-a)=B_k+d,
    T3(B_(k-a))=T3(B_k)+P.

Iterating(1) through exactly a core units instead gives a decrease by
at least2a. Contradiction. All roles repeat with their verified full
histories; the actual full quotient is closed explicitly, not by a bare
infinite spatial argument.

For a finite maximal segment this is only a monotone age obligation
between its endpoints. Its length is NOT bounded here: a flow change,
nonstaircase turn, odd cap or other profile reset may absorb the age.
Such reset mechanisms remain the next open task. An arbitrary global
one-use premise or a complete cap-four front exclusion is not inferred.

## 5. Executable finite cover and safety of rejection

flat_flow2_symbolic_row_with_odd_left.py/json independently enumerates
all1..4 WHITE D/E histories for the FIXED eight-cell stencil. It checks
full physical port counts, literal next-read returns, max-plus rank/edge
clock feasibility and every shared dual-face equation, including unused
ports, against global C<=M. It does not solve a full event orbit or fill
the farther exterior. Every listed rejection is a necessary local failure;
surviving windows may have additional global obstructions.

This extends the signed specific five-corner obstruction90b57415 to a
complete primary alphabet and an all-length overlap argument. That older
checker has a harmless preserved comment typo: D1 rank3 is its SECOND
incoming N occurrence, not a third. Its note, JSON and proof are unchanged
and correct.
