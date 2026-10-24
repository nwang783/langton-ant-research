# The strict-fall lower supplier has a unique earlier bottom-left parent

23 October 2026, 19:30 UTC. Actual-cursor and exact-port refinement of
the signed stock closure. No iteration, new component or fuel inference.

## 1. Exact inherited physical lift

Use precisely the complete WHITE cap-four K1 front and strict-fall
straight-branch configuration of K1_strict_fall_branch_stock_loops.md,
SHA730d9bb19a41dfbdd490b835f3c67679c5d54bc842739c7b62ca9eb2522a6536.
In particular

    F=(0,0), J=(-1,-1), Q=(-2,-2), all at height M;
    U=(1,0), A=(0,1), r=(1,-1), z=(0,0),
    u=(-1,-1), q=(0,-1), e=(-1,0);
    r=WWW, z=WWEE, u=EWWW, q=SNS, e=NSS.

C-face coordinates are lower-left corners. Let delta=B(F)=T1(U).
The previously signed closure gives parent(J)=F, while F's successor
on the chosen Gamma is the RIGHT face G=(-1,1), not J.
The exact uninterrupted chain is

    r.R2(delta-1) -> U.L1(delta) -> z.R0(delta+1)
                  -> A.R0(delta+2).                 (1)

No phase substitution or primitive quotient is used below.

## 2. The whole closed J square is physically LEFT of Gamma

Since parent(J)=F, J cannot be a face on Gamma. If it were, its own
canonical incoming edge would make it F's cycle successor, which is G.
The same reasoning holds for any physical translate: the canonical
parent map is full-drift equivariant, so a translated cycle membership
cannot identify distinct actual parents with the fixed physical F.

None of J's four primal corners lies on a selected Gamma edge:

- q has equal R headings, so is not a selected flat first-L contact;
- u and e have L1 incoming opposite to R0, so are not selected contacts;
- z has the selected transition F->J, but J is not on the cycle.

The diagonal C-contact embedding intersects a physical face boundary
only at these primal corners. Therefore the entire closed J square is
disjoint from Gamma. It meets the known local LEFT sector of the
STRAIGHT F, so all of that square, including u, lies in the LEFT open
component of the physical lifted cut. This does not assume a globally
straight Gamma, leftmostness, or any absent further branches.

## 3. u.R0 must precede the previous helper's final R2

Put t=T0(u). The stock closure gives T1(u)=T2(U)+3. Since the two local
reads are at least four apart,

    t<=T2(U)-1.

The K1 RIGHT excursion starting at A.R0 ends at U.R2. The cursor is
strictly RIGHT throughout its interior. Since u is strictly LEFT, u.R0
cannot occur in that interval. The preceding inequality rules out a
time after U.R2, so

    t<T0(A)=delta+2.

The three integer times delta-1, delta and delta+1 are already occupied
by the different physical cells r, U and z in (1). Thus t<delta-1:
u.R0 occurs strictly BEFORE r.R2, with no unexplained phase shortcut.

## 4. Literal heading transport forces at least eight reads

At u.R0 the incoming heading is E and the turn is R, so its FIRST step
is S. The endpoint r.R2 has incoming heading W, so its LAST step is W.
The displacement from u=(-1,-1) to r=(1,-1) is (2,0).

Every literal ant step turns by ninety degrees, so step axes alternate.
A path starting vertical and ending horizontal has equal numbers n of
horizontal and vertical steps. Net horizontal displacement +2 implies
n is even. Therefore its positive length is a multiple of four.
Length four has only two horizontal steps, one of them the final W;
they cannot sum to displacement +2. Hence its length is at least eight.
Because the endpoint time is delta-1,

    T0(u)<=delta-9,
    B(Q)<=T0(u)-1<=B(F)-10.                         (2)

This is an actual-cursor birth deadline, not the sum of overlapping
flow-cycle or local return bounds.

## 5. Three S inputs remove the remaining bottom-right birth

The signed stock closure already excludes both TOP birth corners of Q.
At its lower-right corner v=(-1,-2), the physical incoming S edge is
supplied by u's THREE S departures R0,L1,L3. Hence v has exactly three
S inputs in its complete white cap-four history.

A negative birth of Q at v, where Q is NW, would have complete prefix
N,N,S: R0 around the SE parent, L1 entering Q and R2 around Q. Even
with L3 present such a history has at most TWO S inputs. This contradicts
the actual complete incoming edge inventory. Thus the bottom-right
corner cannot birth Q either.

The unique remaining canonical birth contact is Q's BOTTOM-LEFT corner
(-2,-2). Its parent is exactly

    parent(Q)=(-3,-3), height M,
    B(parent(Q))<=B(Q)-5<=B(F)-15.                  (3)

The birth read there has prefix E,E,W, but its optional L3 and remaining
suppliers are NOT discarded. This is one exact further-left/lower
supplier step. Its parent is not proved to have the same local pattern,
can be in the same existing maximum component, and is not a new root.
The result does not iterate to an infinite regress or exclude K1.
