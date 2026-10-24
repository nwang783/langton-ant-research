# A strict-left K=1 right turn: exact first loop and six port families

23 October 2026, 14:35 UTC. Necessary local classification, submitted for
independent review. NO exterior connector or positive front is asserted.
The six surviving local tables are not proofs of physical realizability.

## 1. Normalization and hypotheses

Retain the complete white cap-four, full P,d and signed K=1 first-L
curve Gamma. Suppose it makes a RIGHT turn through a parent max C face F.
Normalize F's square to lower-left(0,0), with ordered selected entry
A=v_(i-1)=(1,0) and exit B=v_i=(1,1). Thus Gamma enters F northwestward
through its SE corner and exits northeastward through its NE corner.
The selected incoming prefixes are

    A: N,N,S, turnsRLR;
    B: E,E,W, turnsRLR.

The two intermediate LEFT boundary corners are Z=(0,0),Y=(0,1).
Assume their other C faces have heights STRICTLY below M. No assumption
is made on LEFT C faces elsewhere or either corner's omitted L3.
Every R at Z must arrive W and turn N around F; every R at Y must
arrive N and turn E around F.

## 2. A literal four-step first-L-to-second-R loop is forced

The first physical F-output at A is L1. Strict maximum at Z,Y forces
first-port matching along the three-edge LEFT arc:

    L1(A) -> R0(Z) -> R0(Y) -> R0(B).

The first S output at B is its R0 and its physical target A has its first
S input at R2. Thus the RIGHT excursion at this face is ONE edge:

    R0(B) -> R2(A).

Consequently, writing T_1(A)=t,

    T_0(Z)=t+1, T_0(Y)=t+2, T_0(B)=t+3,T_2(A)=t+4.

The literal read word from A's L1 through the other three corners is
LRRR, returning to A for R2 with the OPPOSITE incoming heading. It is
not a same-full-pose loop and cannot be deleted without a proven splice.
This fact uses no finite enumeration and no unproved detour shortcut.

It also forces Z's next W arrival at time t+5 to be L1, not R2: the
latter would require two local returns after t+1, each at least4 steps.
Thus L1(Z) arrives W. L1(Y) can still arrive N or S. The one-R possibility
at Z and Y MUST be retained; strictness alone does not force two Rs at
both corners. This is why the straight proof cannot be copied through
this bend.

## 3. Exact necessary finite port table

At each helper corner enumerate ALL complete white histories R,RL,RLR,
RLRL, with R headings fixed as above and each L heading either incoming
axis direction. At A and B keep all three possibilities: prefixRLR,
or RLRL with L3 on LEFT, or RLRL with L3 on RIGHT.

Match actual port ordinals on all FOUR boundary edges of F:

    A --W--> Z --N--> Y --E--> B --S--> A.

Keep local rank gaps positive multiples of4 and the signed K=1 inequality
T_2(A)<T_1(B). Exact equalities along matched physical edges increase
time by1. These necessary constraints leave EXACTLY SIX local rows.
Headings below are in complete rank order. A dash means no L3.

| row | A headings | Z headings | Y headings | B headings |
| --- | ---------- | ---------- | ---------- | ---------- |
| 1 | N,N,S | W,W | N,S | E,E,W |
| 2 | N,N,S,N | W,W,W | N,S,N | E,E,W,E |
| 3 | N,N,S,N | W,W,W,E | N,N,N | E,E,W |
| 4 | N,N,S,N | W,W,W,E | N,N,N,S | E,E,W,E |
| 5 | N,N,S,N | W,W,W,E | N,S,N,N | E,E,W,E |
| 6 | N,N,S,S | W,W | N,S | E,E,W,W |

All rows have the fixed initial t..t+5 clock from Section2. Row1 or6 has
one R at each helper and both other C heights M-1. Rows2-5 have two Rs
at each helper and both other C heights M-2. Mixed one/two R helper
counts are impossible by complete port counts. Row6 explicitly retains
a paired RIGHT-side L3 edge B->A; it is not removed by the K=1 pipeline.

The executable right_turn_local_ports.py/json lists all six rows and
minimal solutions of these LOCAL equality/inequality constraints. Those
minimal clocks are NOT literal exterior connector lengths. For example,
row1's locally permitted T_1(Y)=t+6 is not claimed geometrically attainable
from Z's L1 S output at t+5. Exterior physical paths may increase waits or
exclude rows; this table is a necessary over-approximation, not a solver
for a whole front.

No period/drift/radius scan is run. The analytic four-read loop and the
retained one-R/RIGHT-L3 alternatives are the useful output: any attempted
all-case extension must handle them, rather than forcing every bent
near-corner into the strict-straight RLRL strip.
