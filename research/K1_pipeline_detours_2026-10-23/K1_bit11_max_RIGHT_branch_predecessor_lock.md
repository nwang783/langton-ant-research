# Exact predecessor and helper orientation of a bit-11 maximum RIGHT branch

23 October 2026, 20:26 UTC. Submitted for independent review. Complete
WHITE cap-four translating front, canonical first-L maximum curve Gamma,
K=1, actual full P,d. No global constant state or leftmostness is assumed.
All cell histories and coordinates below are physical lifts.

## 1. Two maximum-branched bit-11 RIGHT faces cannot be consecutive

Normalize a RIGHT face F=(0,0) with selected A=(1,0):NNSN,
B=(1,1):EEWE. Suppose both F and its RIGHT successor G=(1,1) have
maximum unused LEFT branches and all three selected bits are1.
The complete bit-11 branch inventory makes both other heights at each
face maximum. With helpers Z=(0,0),Y=(0,1) for F and n=(1,2),p=(2,2)
for G, the possible profiles are exactly

    Z=WWEW,Y=NSSS or Z=EWWW,Y=SSNS;
    n=NNSN,p=EWWW or n=SNNN,p=WWEW.

At m=(0,2), NE and SW C heights are both M. It receives THREE W
inputs from n and sends THREE S outputs into Y. The complete flat
inventory is therefore m=WWEW or EWWW. In every combination, the third
occurrences on these actual ports match as

    Y.L3 -> B.L3 -> n.L3 -> m.L3 -> Y.L3.

They are the four edges of a genuine consecutive four-L route, closing
at the SAME occurrence Y.L3, not at its later translate or R2. This is
impossible because each edge raises actual event time by1. In particular
no deletion, stock charge or exterior realization assumption is involved.

## 2. A RIGHT predecessor must be strict locked row4

Retain G as a bit-11 maximum-branched RIGHT, and suppose its preceding
face F is RIGHT. Its entry A may initially have bit0 or1; a possible0->1 rise
at F is retained rather than assumed absent. First consider input bit1.
Section1 rules out a maximum branch at F. The strict bit-11 RIGHT table
leaves three F profiles: rows2,4,5. They have Z=WWW or WWWE and

    row2: Y=NSN; row4: Y=NNNS; row5: Y=NSNN.

For rows2/5 the only S input at Y is L1. At m=(0,2), the two R headings
are W; n emits three W outputs and Y receives one S input. Thus the
complete m possibilities are WWW,WWWE,WEWW. The actual second E output
of Y feeds B.L1, so its S input is at T1(B)-1.

If m=WEWW, its S output is L3, supplied by n.L3, itself supplied by
B.L3. It would give B.L3 -> n.L3 -> m.L3 -> Y.L1 -> B.L1, impossible
in the same physical B history.

If m=WWW or WWWE, its S output is L1. For n=NNSN, its second W output
is R2, while n.L1 is supplied by B.R2. Therefore

    T1(B)=T1(m)+2=T2(n)+3 > T2(B),

contradicting rank order. For n=SNNN, the second W output is L1,
supplied by B.L1, giving the impossible T1(B)=T1(B)+4.
Rows2/5 are excluded. Only locked row4 remains, and the independently
signed RR stock theorem forces n=NNSN,p=EWWW,m=WWW or WWWE.

For input bit0 at F, the signed RIGHT-L3 transport law makes A exactly
RLR (NNS), not RLRL with an unretained RIGHT L3. The complete0->1
inventory has four necessary profiles:

    Z=WW,   Y=NSSS, with first other strict, second maximum;
    Z=WWEE, Y=NSN,  with first other maximum, second strict;
    Z=WWE,  Y=NSSS, with both others maximum;
    Z=EWW,  Y=SSNS, with both others maximum.

In the three cases with second other maximum, m is flat with W-input
count3 and S-output count3. Thus m=WWEW or EWWW, and exactly the same
actual L3 cycle Y3->B3->n3->m3->Y3 from section1 occurs; that argument
never required Z.L3 or A.L3. In the remaining WWEE/NSN case, m is
strict and Y's unique S input is L1. The rows2/5 argument above applies
unchanged and excludes both possible n profiles. Thus the0->1
predecessor has genuinely been checked and is impossible.

Consequently any RIGHT predecessor of a bit-11 maximum-branched RIGHT
is strict locked row4, with input bit1, not an unexamined rise.

## 3. A strict STRAIGHT predecessor locks the other flat orientation

Independently normalize a strict STRAIGHT F=(0,0), selected
A=(1,0):NNSN, B=(0,1):NNSN and helper Z=(0,0):WWWE. Suppose the
RIGHT successor G=(-1,1) is bit11 and has a maximum LEFT branch.
Its helpers are w=(-1,1),Y=(-1,2), its exit C=(0,2):EEWE. The two
flat possibilities before further matching are

    w=WWEW,Y=NSSS; or w=EWWW,Y=SSNS.

Put e=(-1,0). Its NW C height is maximum and its SE C height is M-2.
Both its R headings are S. The three S outputs of w supply its three
S inputs, and its sole E output supplies Z.L3, hence B.L3. The complete
e inventory is SSS,SSSN,SNSS, with optional L3 retained.

If e=SNSS, its E output is L3, supplied by w.L3, itself supplied by
B.L3. This gives the impossible actual cycle

    B.L3 -> w.L3 -> e.L3 -> Z.L3 -> B.L3.

Thus e=SSS or SSSN and its E output is L1. If w=EWWW, its second S
output is L1, supplied by B.L1. Matching gives T3(B)=T1(B)+4, impossible
because the rank1-to-rank3 gap is at least8. Only

    w=WWEW,Y=NSSS,e=SSS or SSSN                       (1)

survive. Their exact surviving stock route is

    w.R2 -> e.L1 -> Z.L3 -> B.L3 -> w.L3 -> e.R2.

The middle four departures are actual uninterrupted LLLL. In particular
T3(B)=T2(w)+3, T3(w)=T2(w)+4, T2(e)=T2(w)+5, and T0(e)=T2(B)+2.
This is old white-cell stock followed by R2, not a closed actual-time
cycle or permanent input fuel.

## 4. Universal bit-11 orientation and safe whole-curve consequence

A bit-11 maximum-branched RIGHT has no LEFT predecessor by the signed
adjacency theorem. If preceded by RIGHT, section2 applies and locks it
to row4, including the excluded0->1 predecessor; if preceded by
STRAIGHT, that straight is strict and section3 applies. After rotating
section2 back to the pose of section3, BOTH cases force the SAME whole
flat profile for the branched RIGHT:

    first helper WWEW, second helper NSSS.

Thus the other initially necessary EWWW/SSNS orientation is absent at
ANY bit-11 maximum-branched RIGHT on Gamma. It is preceded by a strict
STRAIGHT or a strict locked RIGHT. These are local conclusions, not
premised on a globally constant state.

In CONSTANT-ONE mode every maximum branch on Gamma occurs at such a
bit-11 RIGHT. Its branchful geometry is therefore constrained by these
predecessor and actual-stock rules everywhere. Variable-state rises at
the branched face itself and falls remain separate possibilities; no
whole curve has been replaced by its constant-one subcase.

Neither the retained four-L cleanup nor the branch predecessor lock
implies that a further outward maximum parent is of the same type.
No iteration, new component, original-root, fuel or general K1 exclusion
has been proved.

Dependencies: signed strict/flat RIGHT inventories and state gate law;
K1_locked_RIGHT_to_max_branched_RIGHT_stock_gate.md SHA b9f4b64f...;
K1_bit11_max_RIGHT_branches_adjoin_strict_STRAIGHT.md SHA c3d29c45... .
Finite local controls general_RIGHT_to_max_RIGHT_ports.py/json and
strict_STRAIGHT_to_max_RIGHT_ports.py/json retain respectively two
necessary rows each. They close exact ports and clock gaps, not complete
exterior cursor traces or translating-front realizations.
