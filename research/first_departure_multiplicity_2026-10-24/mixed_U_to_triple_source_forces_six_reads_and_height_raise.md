# A mixed U-to-triple source forces six reads and a height raise

24 October 2026. Complete WHITE translating front, actual full P,d.
Only the displayed boundary histories are fixed; the exterior helper
has ARBITRARY multiplicity at the start of this proof. Author structural
proof pending independent review. No period, width or initial-fuel bound.

## 1. Exact mixed outgoing interface

Take consecutive physical b vertices

    u=(0,1): WEEW, a flow-two LEFT U;
    s=(0,2): NSN, a RIGHT 2->3 odd source;
    w=(1,2): WEEE, a flow-three LEFT.

They share selected clockwise C level c, as on a cap-four boundary
b-circle. Retain every optional/late source rank; in particular u.L3 and
w.L3 are distinct actual later reads. Exact ordinal edges give

    u.R0 -> s.R0 -> w.L1,
    u.L1 -> s.R2 -> w.L3.                           (1)

Let D=(1,1), the opposite physical helper. Its COMPLETE incoming S count
is ONE, from w.R2, and its outgoing W count is TWO, feeding u.R0 then
u.L3. These follow from complete physical ports, not from an assumed
first-read time at D.

Put times A=T0(u), B=T1(u), C=T2(w), E=T3(u). The first W departure of D
occurs at A-1; its unique S arrival at C+1; its second W departure at E-1.
By (1) and same-cell gaps,

    T1(w)=A+2, C>=A+6,
    T3(w)=B+2, C<=B-2,
    E>=B+8.

Consequently the three actual helper port events satisfy the STRICT
ordinal ordering

    first W departure < unique S arrival < second W departure.       (2)

This preserves all arbitrarily old earlier D reads. No source-L3 stock
has been discarded or charged as fresh input.

## 2. Complete uncapped WHITE count calculation

Let D's complete history length be n, with exactly one S incoming read,
at rank j; all other incoming headings are N. Let m=floor(n/2) count L
reads. An outgoing W is produced by L(N) or R(S).

If j is even, Wout=m+1=2, so m=1 and n is 2 or 3. The unique S arrival
itself produces one of the two W departures, violating strict (2).

If j is odd, Wout=m-1=2, so m=3 and n is 6 or 7. Its possible ranks are
j=1,3,5. Strict(2) requires one W departure before and one after j, so
j=3. Thus the ENTIRE complete helper history is exactly

    NNNSNN or NNNSNNN.

The bound n<=7 is DERIVED from physical counts, not imposed as a scan
cap. In these two histories the first W departure is L1, the unique S
arrival L3, and second W departure L5. Therefore any completion needs at
least SIX reads at D. A cap-four exterior is impossible.

The simpler cap-four argument would force D=NNS from first-W-before-S,
then actual w.R2->D.R2->u.L3 and (1) would give T3(u)<=T1(u). The uncapped
calculation above explains exactly how arbitrary older stock can avoid
that rank reversal: it must pass through D.L3/L5 instead, not an unlisted
cap-four supplier.

## 3. Cap-free local stream height forces a higher C face

The six-read helper has THREE R(N) and zero R(S). The unrestricted
local stream curl therefore raises its SE C face by THREE above its NW
C face; the optional seventh R(N) raises it once more. The NW face is the
shared selected level-c face of u/w. For the six-read case, the exact port counts are D outgoing E4,W2 and
incoming N5,S1; the edge equations give

    h(C_NW)=c, h(L_NE)=c-1, h(L_SW)=c-2,
    h(C_SE)=c+3.

The optional seventh N is an R read, so for NNNSNNN it instead contributes
one more R(N), outgoing E5 and incoming N6. In that case the corresponding
height is c+4. Thus the universally safe conclusion is

    h(C_SE)>=c+3.

This count/stream conclusion uses no exterior multiplicity cap. In
particular if c is known to be the GLOBAL C maximum, the displayed mixed
boundary interface is impossible even with arbitrary old helper stock.
At a nonmaximal boundary level it remains an exact six/seven-read,
higher-C escape, not a contradiction or an infinite regress.

The boundary-local first-R maximum theorem must not be applied to this
six/seven-read helper itself. No all-cap global first-R maximum rule,
whole-front exclusion or original-fuel budget is inferred.
