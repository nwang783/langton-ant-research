# Span descent and a dual unit-face transport system

22 October 2026. Sections 1–4 are independently analytically reviewed; no global balance
or cap-three exclusion is claimed.

Write F_v<M_v<T_v for a complete white RLR cell's three read times and
ell_v=T_v-F_v. Unlike the absolute times, ell_v is invariant under translation
by the full drift. Set A=AAB and B=ABB.

## 1. Strict span descent at a one-A path

For p=(0,0)->u=(0,1)->q=(-1,1), with p,q double and u=A, let r=(-1,0).
The signed short-path theorem forces r=A. Exact local chronology gives

    F_r=M_u-2,             T_r=T_u+2,
    ell_u-ell_r=M_u-F_u-4.

Any closed square-lattice walk whose move axes alternate has length divisible
by four: its horizontal and vertical move counts agree, and both are even.
Here M_u-F_u is such a positive closed-walk length. If it were four, the
first R at u and return with the same heading force the clockwise R4 unit
square. Its last predecessor p would then read R, contradicting p's specified
L. Hence M_u-F_u>=8 and ell_r<=ell_u-4.

Consequently a chain consisting only of successive one-A opposite-corner
maps is finite. This holds on the physical plane without periodicity when
all the histories and predecessors exist, and on a translating quotient
because ell is translation invariant. No essential drift-parallel one-A
chain survives this span test. The chain may still terminate at the A of
a BA path or AABB square.

## 2. The complementary one-B calculation

Use the same coordinates, now with u=B. The two edges q->r and r->p are
forced H edges, so r is an opposite triple whose H incoming heading is
south and H outgoing heading east. Its only possibilities are A with
headings N,N,S, or B with headings S,N,N.

The middle L at u is followed by q's last L and a read at r, at times
M_u+1 and M_u+2. The last L at p is preceded by a read at r, at time T_u-2.
If r=A, the first of these r reads would be its third R and the second its
first R. Since p's final L occurs after its first R at M_u-1, the necessary
strict ordering would place p's final L among the already occupied reads
uL,qL,rR. This is impossible. Thus r=B and

    F_r=M_u+2,             T_r=T_u-2,
    ell_u-ell_r=M_u-F_u+4.

In particular the span decreases by at least eight (the closed positional
return has positive length divisible by four). The established L4 exclusion
can sharpen the first-return gap, but is not needed for strict descent.

## 3. Unit-face source and sink identities

Every D left corner follows the boundary of its unique counterclockwise
oriented unit face. At an A or B cell, H follows the opposite diagonal
counterclockwise face. Thus a triple joins a D face to an H face on the
rotated square lattice of counterclockwise face centers.

A D face with two adjacent D edges is a one-corner path. Its diagonally
opposite H corner has the same A/B type, by Sections 1–2. These are straight
transport wires on the rotated lattice.

A three-D-edge BA face is a source pair. Its A and B have

    F_A=F_B+1,             T_B=T_A+3,
    ell_B=ell_A+4.

For a four-D-edge A0,A1,B2,B3 square in directed cyclic order, the natural
pairs (A0,B3) and (A1,B2) satisfy respectively

    F_A0=F_B3+1, T_B3=T_A0+3;
    F_A1=F_B2+3, T_B2=T_A1+1.

Thus both pairs have ell_B=ell_A+4.

A one-D-edge counterclockwise face has two adjacent H-corner triples and
two double endpoints. Those H corners are one A and one B, and

    ell_A=ell_B+4.

For a direct check, normalize its sole D edge to p=(0,0)->u=(0,1), with
remaining face corners v=(-1,1), q=(-1,0). Put p's final L at time 0.
Then u's final L is at 1, the H-input R at v at 2, and the H-output R at
q at -1. The H edge v->q identifies v's H-output time plus one with q's
H-input time. AA and BB contradict the three-read order (in the AA case
also the occupied times 0 and 1). The AB and BA cases both yield
ell_A=ell_B+4.

These identities describe tiny source and sink tiles, not a pairing of
all one-A paths with distinct one-B paths.

## 4. A zero-D-edge H square

If a counterclockwise unit face has no D edge but all four boundary H edges,
its four corners are opposite triples. Let h_i be its successive H-edge
traversal times. At an A corner,

    h_out-h_in=1-ell_A,

and at a B corner the difference is 1+ell_B. Therefore

    sum_A ell_A - sum_B ell_B = 4.

The stronger pointwise statement is that the signed coverage by A first-to-
third half-open intervals [F,T) minus B first-to-third half-open intervals
[F,T) equals the coverage by the four unit intervals [h,h+1) of these H-edge
steps. No equality of the unweighted
A and B counts at this face has been established.

## 5. Exact limitation

The span descent rules out infinite all-one-A or all-one-B wires, but a
long A wire can feed one paired terminal B. That does NOT imply p_A<=p_B.
Source/sink tiles and possible all-H squares must be handled before claiming
a global balance or the exclusion of cap three.

The necessary finite-neighborhood constraints in
`probe_one_a_local_constraints.py` admit independently replayed open-boundary
models through radius 5; larger runs timed out. These models are not ant
orbits, do not have a finite-width translating strip, and do not disprove
an eventual finite-support theorem. They show why a bare small-neighborhood
contradiction is not currently supported. The solver has no time/period
bound, but it does allow unconstrained open boundary inputs.
