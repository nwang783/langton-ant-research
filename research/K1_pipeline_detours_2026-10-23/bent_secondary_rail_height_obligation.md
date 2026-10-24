# A white completion of the locked bent rail needs a raised secondary C face

23 October 2026, 15:30 UTC. Analytic all-period necessary geometry, submitted
for later independent review. This does NOT claim K>=2 or exclude the
whole bent K=1 architecture. No finite search or per-packet fuel charge.

## 1. Prescribed main histories, arbitrary deeper detours

Take a COMPLETE WHITE cap-four front with the signed K=1 alternating
RIGHT/LEFT first-L curve. Retain actual full d=(0,2a), P, with a>=1;
no primitive reduction is used. For all lifted integers k, suppose the
four main histories are exactly the locked bent pattern:

    Z_k=(0,2k):   RLRL, incoming W,W,W,E;
    Y_k=(0,2k+1): RLRL, incoming N,N,N,S;
    A_k=(1,2k):   RLRL, incoming N,N,S,N;
    B_k=(1,2k+1): RLRL, incoming E,E,W,E.

The last two are selected Gamma contacts. Main max C faces have lower-left
coordinates (0,2k) and (1,2k+1), height M. Their complete R counts force
the LEFT neighboring C faces with lower-left (-1,2k+1) to have

    b=M-2=c_left,  c_right=M-1.

No prepared black input is allowed. No history is prescribed for cells
strictly to the LEFT of the main column, and actual detours there may be
arbitrarily long. RIGHT-side detours are also not excluded.

Put secondary ports

    E_k=(-1,2k), O_k=(-1,2k+1),

and let H_k be the C face with lower-left (-2,2k), incident SW at O_k
and NW at E_k. The other incident C at each port is at baseline b.

Main Y_k has exactly one W output, its L1. Hence O_k has ONE W input,
at actual time S_k=T_1(Y_k)+1. Main Z_k has exactly one E input, its L3.
Hence E_k has ONE E output, at F_k=T_3(Z_k)-1. They are the beginning
and end of one actual LEFT packet. The main port matching and signed
K=1 chronology give

    S_k < F_k < S_(k+1) < F_(k+1).                 (1)

All N outputs of O_k enter E_(k+1), while all S outputs enter E_k.
This retains the secondary-rail suppliers; no omitted earlier R is free.

## 2. Assume all secondary C heights remain at/below baseline

Suppose h(H_k)<=b for EVERY k. At O_k its unique W input must be an R:

- If H_k<b, every R selects the baseline NE C face and arrives W. The
  unique W input makes it R0. Any L must arrive E; no earlier R0(E) can
  select the lower C face.
- If H_k=b, opposite R headings are required. The unique W input is
  either R0(W) or R2(W). All L reads arrive E.

In all cases O_k emits a first N traversal no later than time S_k.
It enters E_(k+1) no later than S_k+1, well before the required future
E output F_(k+1) in(1).

If H_(k+1)<b, every R at E_(k+1) arrives N. Its FIRST N input would be
R0 and would already emit E, contradicting that unique future output.
Thus H_(k+1)=b. As k was arbitrary,

    h(H_k)=b for EVERY k.                          (2)

## 3. The two opposite-R supplier alternatives cannot close chronologically

By(2), every O_k has two opposite R headings and its unique W input is
one of them. There are just two types, retaining optional L3(E):

    type I:  W,E,E[,E], with current W input at R0;
    type II: E,E,W[,E], with current W input at R2.

At E_(k+1), equal C heights require opposite N/S R headings. Its unique
E output already comes from R(N), so every L must arrive N (an L(S)
would emit an additional E). If R0 arrived N, the first N traversal from
O_k would emit that unique E too early. Therefore E_(k+1) has

    S,N,N[,N], with R0(S), L1(N), R2(N),

and its unique future E output is at its SECOND N input.

If O_k were type II, its first N output is L1(E), before its current W
read; its SECOND N output is exactly its current R2(W), at S_k. This
would put the unique E output of E_(k+1) at S_k+1, violating(1). Hence
EVERY O_k is type I.

But now R0(S) at E_(k+1) must precede its L1(N), which is supplied by
O_k's current R0(W) at S_k and arrives at S_k+1. The only supplier of
that earlier S input is O_(k+1). In type I, O_(k+1)'s S output is its
R2(E), AFTER its own current R0(W) at S_(k+1)>F_k>S_k. It cannot supply
the already required earlier R0(S). This is the contradiction.

## Conclusion and scope

A COMPLETE WHITE completion of this locked bent main rail must have

    h(H_k)>=b+1=M-1=c_right for at least one lifted k.

Thus arbitrary deeper detours cannot keep the entire first secondary
C row at the LEFT exterior baseline. They must introduce a raised C
face behind the low barrier. Since M is the global maximum, the raised
height is M-1 or M. If it is M, it lies in a DIFFERENT global-max component
from the main rail: the entire intervening C row x=-1 has height M-2
and separates the two components in the C-contact lattice.

No proof is given here that the M-1 alternative is impossible, nor that
such a raised row can be supplied. No new K>=2 conclusion follows.
The literal W20 prepared control evades the proof exactly at Section2:
its O_k input is a singleton L, not a complete white R history. This
identifies the genuine missing geometry of a white fuel completion,
without discarding the actual old-L3 cleanup or either side current.
