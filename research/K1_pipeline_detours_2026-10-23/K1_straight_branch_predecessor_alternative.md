# Entering a straight max branch: LEFT is impossible, or a lower max supplier

23 October 2026, 19:18 UTC. New branchful entrance chronology, submitted
for independent review. Complete WHITE cap-four front, actual full P,d,
canonical maximum-face first-L curve Gamma, K=1. No leftmostness,
branch-free premise, leaf structure, or original-fuel bound.

## 1. Common straight-branch data

The current STRAIGHT face F has lower-left (0,0), entry U=(1,0), exit
A=(0,1), helper z=(0,0), and unused LEFT C neighbor J(-1,-1) at M.
Here and below a C-face coordinate denotes its lower-left corner.
The signed straight-flat history is

    z=WWEE, U=NNS or NNSS, A=NNS or NNSS.

Put q=(0,-1), r=(1,-1), and K=(0,-2). The C faces at q are J(NW)
and K(SE). Exact complete ports give

    T0(z)=T1(U)+1, T1(z)=T2(U)+1.

The first S input at q is therefore T2(U)+2. No omitted earlier S
supplier can be inserted: z's two S departures are its L1,R2 and are
the complete physical incoming S edge for q.

## 2. The predecessor cannot turn LEFT

Suppose the preceding curve face P=(1,-1) is LEFT. Its entry is r,
its exit is U, and its canonical parent is K. Consequently h(K)=M.
Its one-edge parent arc preserves the LEFT-L3 bit, so r has no LEFT L3:

    r=EEW or EEWW.

Its two N departures are L1,R2 and feed U's two N inputs R0,L1. Thus

    T1(r)=T0(U)-1,
    time(second E output at q)=T1(r)-1=T0(U)-2.

At q both C heights J,K are M. A complete white cap-four flat N/S
history can emit at most one E before its first S input. But the SECOND
E output just displayed precedes the first S input T2(U)+2. This is the
same whole-history first-port obstruction, now on the entrance side.
Hence a straight equal-M LEFT branch cannot be preceded by LEFT.

## 3. A preceding STRAIGHT is a strict state fall

If P is STRAIGHT, it cannot itself have an equal-M LEFT neighbor, by the
signed branch-to-bend theorem. Its LEFT neighbor K is strict, and the
signed straight table with output LEFT-L3 bit zero forces

    r=WWW, K=M-2,
    predecessor entry LEFT-L3 bit one, U LEFT-L3 bit zero.

At q both R headings are S and the complete S-input count is two.
It has no E output, since r has no E input. Its complete history is
exactly SNS or SNSN. Thus this alternative is a real strict-straight
state fall, not a hidden flat branch or an absent earlier-R supplier.
It need not leave U odd: U may retain RIGHT L3.

## 4. A preceding RIGHT has only two kinds of second helper

If P is RIGHT, normalize its entry V=(2,0), first LEFT helper a=(2,-1),
second LEFT helper r=(1,-1), and exit U=(1,0). The other C at a is
D=(2,-2); at r it is K=(0,-2). Their heights are independently at most M.
The retained complete ports are

    V --S--> a --W--> r --N--> U --E--> V,
    U --W--> z --S--> q --E--> r.

K1 gives T2(V)<T1(U). Optional RIGHT L3 at U is retained.
A complete cap-four heading/ordinal reconstruction leaves these cases:

(a) K strict. Then D is strict as well, and uniquely

    V=WWEW, a=SSSN, r=WWW, U=NNS,
    K=D=M-2, q=SNS or SNSN.

This is the genuine strict RIGHT state fall, with a final-black RLR U.

(b) K=M. Then r=WEE or WEEW and

    q=NSS, NNSS or NSSN.

D may be strict or M, and both U=NNS and U=NNSS remain where matched.
The exact clock shared by every such case is

    T0(q)=T1(U)-2.

Indeed q's FIRST E output is its R0 and feeds r.L1, which is its SECOND
N output into U.L1. Since q.R0 chooses K,

    B(K)<=T0(q)-1=B(F)-3.

Moreover neither of K's TOP corners can be K's canonical birth. At q,
R0 already chooses K; at r, R0 chooses P and L1(E) uses K's INPUT before
R2(E) uses K's output. Thus the birth parent Q is one of the two LOWER
max neighbors

    Q=(-1,-3) or Q=(1,-3), h(Q)=M,
    B(Q)<=B(K)-5<=B(F)-8.

These are both retained physical suppliers. The word LOWER means this
explicit coordinate normalization, not an unproved global LEFT-side
placement of their entire parent paths.

## 5. Finite complete-inventory control and cautions

straight_branch_predecessor_right_ports.py/json independently builds all
length-one through length-four white histories, keeps both possible R
counts at strict corners, shares the exact K R-count difference at q/r,
and matches the seven full physical edges listed above in actual ordinal
order. Same-cell gaps are at least four and T2(V)<T1(U). It finds 26
necessary rows: two strict-K rows and 24 equal-K rows (eight V/a/r/U
profiles times the three displayed q histories). It is a finite exact
local check, not a bounded translator, drift or radius scan. Exterior
connectors and actual one-cursor sufficiency are not asserted.

The entrance alternatives combine with the signed double-max RIGHT
successor theorem, but are not a global branch payment. The two birth
parents may belong to the same component, may return toward earlier
Gamma geometry, and are not proved to have a recursively identical local
pattern. A state fall may later be renewed using output produced by the
front. No original-input fuel or general K1 exclusion follows.

Signed dependencies:
K1_branches_force_bends.md SHA
57c354298337f3aa7e3b98ac44a0887729e473dc8c42264d737019ad5a631611;
K1_left_L3_state_gates.md SHA
ac025ac64acb980d7ace6b757f5c6d9902b4084529ff2d38e449f5f6a771130f.
