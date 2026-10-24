# Three locked packets force a return, and straight gates have positive density

23 October 2026, 17:47 UTC. Conditional finite chronology theorem,
submitted for independent review. Its density is geometric, not a paid
fuel or original-root count. No K=1 exclusion is claimed.

## 1. Hypotheses and notation

Assume the signed leftmost branch-free collar theorem: a complete WHITE
cap-four K=1 front, actual full P,d, and the canonical first-L circle
Gamma in the LEFTMOST maximum C component, with no LEFT maximum branch.
Put b=M-2=c_left. Every strict-LEFT C face has height <=b, every selected
contact has LEFT L3, and each straight face has the actual rank3-to-rank1
gate. The signed strict-right table and R,L row-4 theorem are retained.

Face types S,R,L mean the straight, right-bend and left-bend geometry
of Gamma's C-contact path. In particular a RIGHT face immediately
followed by a LEFT face has strict-right ROW 4; R,L,L is impossible.
The same-Gamma near-return classification remains conditional but exact.

## 2. A finite three-packet obstruction

Suppose Gamma has the six consecutive face types

    R,L,R,L,R,L.

After one genuine rotation and translation, its three RIGHT faces have
lower-left coordinates F_k=(0,2k), k=0,1,2. Their complete row-4 histories
are

    Z_k=(0,2k):   W,W,W,E;
    Y_k=(0,2k+1): N,N,N,S;
    A_k=(1,2k):   N,N,S,N;
    B_k=(1,2k+1): E,E,W,E,

all RLRL. No history beyond these six faces is prescribed. Define

    O_k=(-1,2k+1), E_k=(-1,2k),
    H_k = the C face with lower-left (-2,2k),
    S_k=T1(Y_k)+1, F_end_k=T3(Z_k)-1.

Each O_k has exactly ONE W input, at S_k. Each E_k has exactly ONE E
output, at F_end_k. The signed main port ordinals and K=1 chronology
apply locally, giving

    S_0 < F_end_0 < S_1 < F_end_1 < S_2 < F_end_2.       (1)

In particular a first N output from O_k at or before S_k reaches
E_(k+1) before its required output F_end_(k+1), for k=0,1.

Assume for contradiction that h(H_0),h(H_1),h(H_2)<=b.
The following argument is finite and retains all opposite-R suppliers.

At O_k with H_k<=b, its unique W input is an R read. If H_k<b it is R0;
if equality holds it is R0 or R2. In every case a first N output occurs
no later than S_k. Its arrival at E_(k+1) is earlier than
F_end_(k+1). If H_(k+1)<b, that first N input would be R0 and would emit
the unique E output too early. Thus

    h(H_1)=h(H_2)=b.                                  (2)

At E_1 and E_2 equal C heights require opposite N/S R headings. The
unique E output is an R(N); all L reads must arrive N to avoid a second
E output. Since a N input has already arrived too early, the only full
history is

    S,N,N[,N], with turns R,L,R[,L].                  (3)

Its future unique E output is at its SECOND N input.

At O_1, (2) leaves precisely the two histories

    type I:  W,E,E[,E], current W input at R0;
    type II: E,E,W[,E], current W input at R2.

If O_1 were type II, its first and second N outputs would be L1(E)
and its current R2(W), the latter at S_1. They would supply E_2's second
N input by S_1+1<F_end_2, contradicting (3). Hence O_1 is type I.

But E_1 needs its R0(S) before its first N input. That first N input is
supplied by O_0 no later than S_0+1. The only possible source of E_1's
R0(S) is O_1's S output; in type I this is R2(E), strictly AFTER its
current W arrival S_1>S_0+1. This is impossible. Therefore

    at least one H_k, k=0,1,2, has height >=M-1.       (4)

No periodic secondary rail, global half-plane hypothesis, or prescribed
old-side connector is used. One should not replace three packets with
two: the type-II right endpoint was eliminated using the THIRD packet.

## 3. The raised face is an actual row-5 return on Gamma

The low neighbors across O_k,E_k have height b and lie LEFT of Gamma.
If H_k is not a Gamma face, its contact path through these low neighbors
cannot cross Gamma: neither O_k nor E_k is a selected flat max contact.
It is then a strict-LEFT C face and has height <=b by the signed collar
criterion. Thus (4) forces H_k to be a Gamma maximum face.

The signed same-Gamma theorem now applies without any added supply
assumption. H_k is an oppositely oriented RIGHT face, has row 5, and its
selected exit birth is at least ten reads older than the main exit.
Its actual four-L old-stock cleanup and optional deeper suppliers are
retained. This is not a new fuel input or a realized complete connector.

There is also an exact geometric injectivity. A row-4 main RIGHT face
has one candidate opposite face, two units toward its local LEFT. If
that opposite face is the required row-5 RIGHT return, its own RIGHT
orientation is the opposite orientation. That fixed orientation and
position determine the original main face uniquely. Thus two distinct
row-4 main faces cannot have the SAME row-5 return face. The statement
holds for actual full-drift face classes, not just distinct drawings.

Consequently, in any maximal alternating run of r consecutive R,L
pairs, there are at least floor(r/3) DISTINCT row-5 return classes.
Use disjoint triples of main faces. Runs may choose overlapping stronger
returns, but the injectivity prevents any double counting across runs.
A row-5 return is never itself followed immediately by L, because the
signed R,L theorem would instead force the distinct row 4.

## 4. A global turn-word count

Let m be the number of R faces, also the number of L faces, and s the
number of S faces in one full quotient of Gamma. The equality follows
from zero signed turn of an embedded essential circle. Its total length
is ell=2m+s. The signed branch-or-straight theorem gives s>=1.

Three consecutive identical bends would traverse the four edges of a
unit C-contact square and return to the same physical point. Embedded
essentiality excludes that zero-displacement subloop, including small
full-drift quotients. Thus an L run has length at most two. The signed
R,L,L exclusion says every length-two L run begins after S. Writing
#XY for the number of adjacent ordered types X,Y, put

    r=#RL, q=m-r=#RR+#RS=#LL+#SL.

There is at most one LL edge per S-started L run, so

    #LL <= #SL <= s, and q<=2s.                       (5)

Partition all RL pairs into maximal runs (RL)^r_i, and let a be their
number. Between consecutive S faces, an R/L block can have LL only at
its beginning; otherwise the LL would be preceded by R. It therefore
has at most one initial RL-pair run plus one extra run per RR edge.
There are at most s such nonempty blocks, giving

    a <= s+#RR <= s+q.                               (6)

Let n_5 count the distinct row-5 RIGHT return faces. By Section 3 and
its injectivity,

    sum_i floor(r_i/3) <= n_5 <= q.

The upper bound holds because no row-5 face is followed by L. Since
r=sum_i r_i and floor(n/3)>=(n-2)/3, we obtain

    r <= 3q+2a,
    m=r+q <=4q+2a <=6q+2s <=14s,
    ell=2m+s <=29s.

Therefore the actual strict straight rank-lowering gates obey

    s >= ceil(ell/29).                               (7)

The constant is a conservative consequence of this explicit symbolic
count, not a numerical period or drift scan. It is not asserted optimal.
All counts use one actual full-drift quotient; lifted runs and their
returns are reduced only after the equivariant geometric injection.

## 5. Scope of the gain

The leftmost branch-free K=1 architecture needs a positive DENSITY of
strict straight rank3-to-rank1 gates. Every three alternating locked
packets force a concrete, older, same-Gamma row-5 return. Each such return
still has the signed graph alternative: nonbridge even excess >=2 or a
LEFT lower-sheet essential +/- pair. Several returns can share those
same graph resources. Neither (7) nor the finite chronology is an
original-black fuel charge, a global K>=2 theorem, or a white realization
of a nonstandard wave. LEFT maximum branches remain a separate escape.

Sources preserved unchanged:
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466;
K1_right_left_forces_row4_gate.md, SHA
04953c96737e932323f29e343dfd07096401c4fa74f710bec07a3c76a8fcc3ed;
K1_secondary_return_strand_row5.md, SHA
a46d61d8a2b88f9f8ba8525bf8c1d4d58a1a122c04e443be3e7c968721909e46;
bent_secondary_rail_height_obligation.md, SHA
f8a56ac667b3475e3328b86a6420d411c5fe4f03e735d0db02d5615e308185ce;
K1_outermost_component_needs_branch_or_straight.md, SHA
ba01934d6fa62077c5e8857f3e4921ffbb817734551d494961a1f1f8cf117067.
