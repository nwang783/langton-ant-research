# Global-max flow-three segments have at most five physical edges

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Consider a maximal constant-TOTAL-flow-three segment of an ACTUAL
b-cycle at selected GLOBAL C maximum M. Equivalently its selected C level
is explicitly constant and locally maximal, with the signed first-R
corner alphabet available. This does not classify arbitrary b-tree paths.
Author structural proof pending independent review.

THEOREM. Every such nonclosed segment has at most FIVE physical edges.
Its exact odd source/sink or one-use rerouting endpoints are retained.
The proof is an all-length corner-word reduction, not a numerical cutoff
in period, width, support, drift or segment length.

## 1. Exact profiles and endpoints

Use the independently signed maximal-segment alphabet b955fed1. A LEFT
internal flow-three corner is uniquely WEEE after normalizing cycle
incoming E/outgoing N. Both R headings are opposite, and its G3 middle
turn is negative incoming R2->outgoing L1. RIGHT internal profiles are
EEEW and EWEE, normalized incoming E/outgoing S.

LEFT corners preserve physical multiplicity, so changes at the ends
occur only at RIGHT corners. The complete endpoints are

    START: EWE(2->3), an odd same-R G3 source;
           EWWW(1->3), an exterior rerouting vertex;
    END:   EEE(3->2), an odd same-R G3 sink;
           EEWE(3->1), an exterior rerouting vertex.

Those one-use endpoints are not silently excluded. If the whole b-cycle
has no one-use edge, the first pair are the actual entire G3 source/sink
path endpoints, as already signed. No initial-fuel payment is added.

## 2. A constant-three LRRL subpath is impossible without a height bound

Normalize four consecutive corners of geometric types L,R,R,L to

    Z=(0,0), A=(1,0), B=(1,-1), Y=(0,-1),

where their b path uses Z->A->B->Y, with Z's incoming direction S and
Y's outgoing direction S. Complete flow-three LEFT histories are

    Z=NSSS, Y=EWWW.

The two RIGHT alphabets are

    A=EEEW or EWEE; B=SSSN or SNSS.

The missing physical unit-square edge Y->Z goes N. Its total flow is
ONE at both ends: Y.R2 is its departure and Z.R0 its arrival. Match the
FIRST physical ordinal around the square E,S,W,N. At Z,A,B the incoming
and outgoing ranks are both R0. At Y the incoming rank is L1 and outgoing
rank R2. Exact physical-time telescoping would therefore give

    0=4+(T2(Y)-T1(Y))>0.

Contradiction. This uses the actual physical first ordinal and complete
ranks; the boundary is not asserted to be an uninterrupted ant factor.
All four RIGHT profile choices fail the same analytic identity. No global
maximum is needed for this LRRL obstruction.

## 3. The locally maximal LRL obstruction is retained with its scope

The independently signed section 6 of b955fed1 excludes a constant-three
LRL subpath at a locally maximal selected C component. Its two LEFT
profiles WEEE and either RIGHT sign force the opposite helper's W output
before its S input; the complete helper is NNNS and puts an adjacent C
face at M+2. Both RIGHT signs and the exterior supplier are retained.
At GLOBAL M that is impossible.

This is the only height-maximality step. At a nonmaximal c a higher-C
shield is not ruled out by this proof, and the five-edge conclusion must
not be imported there.

## 4. The complete all-length turn reduction

Three consecutive identical geometric turns would close a physical
unit square on an embedded essential b-circle; hence each RIGHT or LEFT
run has length at most two. Suppose there were two distinct LEFT runs
within the flow-three segment. Between them is a RIGHT run of length
one or two. The last LEFT of the first run and first LEFT of the second
would give LRL or LRRL, excluded by sections 2-3. Thus there is at most
ONE LEFT run, itself of length at most two.

The source and sink are RIGHT, so any nonempty LEFT run has a leading
RIGHT run of length 1 or 2 and a trailing RIGHT run of length 1 or 2. All
possible necessary geometric templates are therefore

    RR;
    RLR, RLRR, RRLR, RRLRR;
    RLLR, RLLRR, RRLLR, RRLLRR.

The longest has six vertices, hence five physical edges. This list is
not an assertion that all nine templates have an exterior completion.
All physical clock spans and outside ports remain governed by the signed
whole-segment interface, not bounded by the segment's geometric length.

The closed all-three case at a local maximum was already excluded by
b955fed1. The present theorem sharpens each OPEN maximal segment and
retains every permitted one-use endpoint, source L1 and late L3 channel.
It does not bound the number of such segments, the variable-flow cycle,
its full period, or the stock supplying the odd endpoints.
