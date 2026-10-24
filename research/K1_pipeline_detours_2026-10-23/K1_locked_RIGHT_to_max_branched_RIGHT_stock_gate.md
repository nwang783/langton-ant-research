# A maximum-branched RIGHT after locked row4 retains an exact stock gate

23 October 2026, 20:09 UTC. Necessary mixed-geometry closure, submitted
for independent review. This is NOT a realized exterior connector or a
WHITE translating front. It retains an escape from naive branch pruning.

## 1. Exact scope and cells

Use complete WHITE cap-four K1 and actual full P,d. Let a RIGHT face F
with lower-left (0,0) have signed locked row4 histories

    A=(1,0): NNSN, Z=(0,0): WWWE,
    Y=(0,1): NNNS, B=(1,1): EEWE.

The next face G=(1,1) is also RIGHT, with exit C=(2,1), and both its
selected LEFT-L3 bits are1. Assume it has an equal-M unused LEFT neighbor.
The complete right-turn bit11 inventory then makes BOTH other LEFT C
faces maximum: J=(0,2) at first helper n=(1,2), and I=(2,2) at second
helper p=(2,2). Rotate the two possible flat bit11 profiles into this pose:

    n=NNSN, p=EWWW, C=SSNS; or
    n=SNNN, p=WWEW, C=SSNS.

Put m=(0,2). Its NE C face J is M; SW C face (-1,1) was M-2 in the
locked F row. Thus both m R reads arrive W and choose J. n emits W
three times, and Y has exactly ONE S input, at L3. The complete m
possibilities are exactly WWW, WWWE, WEWW.

## 2. Exact chronological elimination and retained four-L supply

The unique S output of m must supply Y.L3, which supplies B.L3:

    time(m's only S output)=T3(B)-2.                (1)

If m=WEWW, its S output is L3 and is supplied by n's third W output,
which is n.L3 in either n profile. Since n.L3 is itself supplied by
B.L3, (1) creates the impossible cycle B3->n3->m3->Y3->B3.
Thus m is WWW or WWWE and its S output is L1.

If n=SNNN, its second W output is L1, supplied by B.L1. Equation (1)
would give T3(B)=T1(B)+4, impossible with B.R2 strictly between.
Consequently only

    n=NNSN, p=EWWW, C=SSNS,
    m=WWW or WWWE                                 (2)

remain. The actual consecutive stock route is

    n.R2 -> m.L1 -> Y.L3 -> B.L3 -> n.L3 -> m.R2.

Its middle four departures m.L1,Y.L3,B.L3,n.L3 are uninterrupted LLLL.
The cursor returns to m with incoming W and immediately reads its R2,
so T2(m)-T1(m)=4. The colors changed; no same-state deletion or fresh
fuel payment is justified. Optional m.L3(E) remains in WWWE.

Other exact clocks, with delta=B(G)=T1(B), are

    T2(B)=delta+4,
    T0(n)=delta+1, T0(p)=delta+2, T0(C)=delta+3,
    T1(n)=delta+5,
    T3(B)=T2(n)+3, T3(n)=T2(n)+4.

These are local actual constraints. A minimum-clock table is NOT one
continuous exterior cursor trace, and its freely separated times must
still meet literal head transport. No positive front is asserted.

## 3. The first maximum branch can be newly born or have an older LEFT parent

For J=(0,2), the lower-left corner m chooses J at R0 and cannot birth J.
The upper-right corner s=(1,3) emits S into n; n has exactly ONE S input
(R2). A negative J birth at s would emit S at L1 AND R2, at least two
occurrences. Hence s cannot birth J either.

The lower-right corner n is negative for J, with R0 around G and L1
entering J. Its candidate birth time is exactly delta+5. The upper-left
corner t=(0,3) is the only other possible birth. Therefore either

- parent(J)=G at n, B(J)=B(G)+5; or
- J is canonically born at t from maximum Q=(-1,3), with
  B(Q)<=B(J)-5<=B(G).

Both alternatives are retained, with full optional L3 at the earlier
supplier. In particular one cannot infer that every maximum branch after
a bend has a strictly older outward parent: the exact necessary local
inventory still permits a NEW branch born from the main G at its minimum
five-read birth gap. It is not claimed that the exterior realizes it.
No iterative regress, new max component, original-root charge or general
K1 exclusion follows.

Local control: locked_RIGHT_to_branched_RIGHT_ports.py/json keeps all six
n/m combinations and exact full physical port ordinals. Exactly the two
m alternatives in (2) survive. Its retained rows are necessary only.
Dependencies: signed locked RIGHT row4, complete bit11 RIGHT histories,
first-L max-face birth theorem, and K1 actual selected chronology.
