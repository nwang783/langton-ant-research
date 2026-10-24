# A zero-state left/right pair needs both outward maximum neighbors

23 October 2026, 16:01 UTC. Analytic local extension, pending independent
review. The equal/equal histories are necessary controls, not asserted
whole-front connectors. No branch is charged as a resource.

## 1. Retained signed launch and notation

Use the exact three-face geometry and hypotheses of the signed note
K1_zero_state_left_right_launch.md: a complete WHITE cap-four K=1 curve,
LEFT then RIGHT faces, selected contacts C=(1,-1), A=(1,0), B=(1,1),
and LEFT-L3 state s_A=s_C=0. Put Z=(0,0), Y=(0,1). Let G be the C face
SW of Z, lower-left (-1,-1), and H the C face NW of Y, lower-left (-1,1).
The RIGHT face F has lower-left (0,0) and height M.

The signed launch theorem gives G=M and Z.R0 arriving E exactly at
T1(C)-2. A has exactly two W outputs, L1 and R2. Therefore Z is flat,
starts with R0(E), has exactly two W arrivals, and its complete history
is one of

    Z: E,W,W; E,W,W,E; E,E,W,W.                    (1)

Both possible Rs at Z select G and F once each. No optional RIGHT L3 at
A or C is discarded; it does not add a W output to Z.

B has 2+s_B E arrivals: R0, L1, and a possible LEFT L3. All of these are
supplied by Y's E outputs. Also B.R0(E) departs S into A's first S read,
which is A.R2. Thus

    T0(B)+1=T2(A).                                (2)

Z's N outputs supply all N arrivals at Y. There is one such output for
Z=E,W,W and two for either four-read profile in(1).

## 2. A strict upper neighbor H is impossible, including the one-R case

Suppose H<M. Every R at Y then arrives N and selects F. Y must emit E
at least twice, to B.R0 and B.L1, while it has at most two N arrivals
from Z.

The complete cap-four possibilities retain BOTH R counts:

- With one R, Y must be RL with headings N,S. Its R0 and L1 emit E.
- With two R reads, both arrive N. All L reads must arrive S, since
  the two R reads already consume the maximum two N inputs. RLR gives
  N,S,N and three E outputs; RLRL would give four E outputs, exceeding
  B's maximum three, so it is impossible.

In either surviving case, Y's FIRST N arrival is its R0, and its first
E output supplies B.R0. Hence Z's first N output starts the consecutive
chain

    Z first N departure -> Y.R0 -> B.R0 -> A.R2.

For Z=E,W,W or E,W,W,E, its first N departure is Z.R2(W), which is
itself supplied by A.R2 one step earlier. This is a strictly increasing
actual-time cycle and is impossible.

For Z=E,E,W,W, its first N departure is Z.L1(E). Its W arrivals are
Z.R2 from A.L1 and Z.L3 from A.R2. Therefore the same chain continues

    Z.L1 -> Y.R0 -> B.R0 -> A.R2 -> Z.L3

as FOUR actual consecutive steps. It leaves no opportunity for the
mandatory intervening Z.R2 visit. This is also impossible.

Consequently H=M. Both unused LEFT maximum neighbors G and H are
necessary, not only the earlier lower branch G.

## 3. Exact remaining flat helper profiles and the second outward launch

With H=M, Y has opposite R headings. Its N-input count is fixed by(1),
and its E-output count is 2 or 3. Exhausting these tiny local inventories
and retaining the same actual chain gives only:

    Z=E,W,W       -> Y=S,S,N or S,S,N,S;
    Z=E,W,W,E     -> Y=S,S,N,N;
    Z=E,E,W,W     -> Y=S,N,N,S.                    (3)

Here all histories are RLR or RLRL. The first line allows s_B=0 or1;
the last two have s_B=0. In particular Y.R0 arrives S and turns around
the outward maximum H, rather than around F.

For completeness, the eliminations behind(3) are as follows. With one
N arrival, Y has one N R and all L reads S. If R0 arrived N, the same
first-N chain in Section 2 would give the same impossible cycle or rank
skip. Thus the only profiles are S,S,N[,S]. With two N arrivals, at
least two E outputs force four reads, one N R, one S R, one N L and
one S L. The four profiles are N,N,S,S; N,S,S,N; S,N,N,S; S,S,N,N.
The first two start R0(N) and are excluded by the same chain.

For Z=E,W,W,E, the first N output is Z.R2 at T2(A)+1. Profile S,N,N,S
would put B.R0 at or after Y.R2, strictly after this first N input and
therefore after A.R2, contradicting(2). So only S,S,N,N remains.

For Z=E,E,W,W, the first N output is Z.L1 and its second is Z.R2 at
T1(A)+1. Profile S,S,N,N would send Y.R2, its first N read, to B.L1.
Then T1(B)=T1(Z)+2. But T2(Z)-T1(Z)>=4 and T2(Z)=T1(A)+1 imply
T1(B)<=T1(A)-1, contradicting the selected L1 order. Hence only
S,N,N,S remains.

These are exactly the four helper patterns in the existing 28-row
necessary local control, but the proof above does not infer their
literal realizability from that control. Their exterior suppliers,
including Y's S arrivals from the north, remain open.

## 4. What is now known about birth suppliers

The lower branch G retains its earlier exact launch Z.R0 at T1(C)-2
and its signed further-LEFT birth-predecessor obligation. The upper
branch H has an actual R0 launch at Y with incoming S, and

    B(H)<=T0(Y)-1.

Thus Y cannot be H's negative first-port birth corner: R0 already
selects H there. H's other corners and all their actual suppliers are
retained. In particular this note does NOT assert that H's canonical
birth must move strictly LEFT or that its launch precedes Z's launch.
The upper-right birth contact can require additional geometry, which
has not been removed.

The result is a second genuine maximum launch, not a fresh black-fuel
payment, a disjoint third current, an infinite regress, or a general
K=1 exclusion.

Source retained unchanged: K1_zero_state_left_right_launch.md, SHA
8fb5af1921bdad6dcb20b618d17e0c5e0d088a2a54c565684781477f9371feeb.
Existing necessary control: left_right_zero_launch_local_ports.json.
