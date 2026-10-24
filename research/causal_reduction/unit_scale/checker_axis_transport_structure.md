# Exact checker-axis structure of unit transports

23 October 2026, 04:46 UTC. Independently signed analytic review and literal
positive-control replay completed at 04:59 UTC. This isolates a genuinely different local
transport degree of freedom; it does not construct a recurrent mechanism.

## 1. Every exact-charge unit image has only two incidence parameters

Use the eight physical states N-R,N-L,E-R,E-L,S-R,S-L,W-R,W-L. Put

    U = {N-R,E-L,S-R,W-L},    V = {N-L,E-R,S-L,W-R}.

Let an image of state s have precisely its coarse unit displacement, its
coarse final heading, and its coarse total charge (+1 for R, -1 for L).
Subtract the one coarse occurrence s from its state-incidence vector.
Then for unique nonnegative integers A_s,B_s the excess vector is

    B_s 1_U + A_s 1_V.                                    (1)

Consequently its length is 1+4(A_s+B_s). Define delta_s=B_s-A_s.

Proof: after subtracting the coarse step, heading-transition counts form a
circulation on the four-cycle. If r_h,l_h are its forward/backward counts,
flow balance gives r_h-l_(h+1) constant. Total charge zero makes the constant
zero. Zero physical displacement then gives l_N=l_S and l_E=l_W, yielding
(1). Each class contains four states and only one count was subtracted, so
its common value is nonnegative even when the subtracted state initially
appeared to permit a negative count.

If the image is internally ant-legal and nonidentity, BOTH A_s and B_s are
positive. Normalize to incoming N. For coarse R, A=0,B>0 leaves disconnected
heading pairs {N,E} and {S,W}, yet requires visits in both, impossible. For
B=0,A>0 the unique bridge is the coarse N-R edge and the word is necessarily
(LR)^A R (RL)^A. Its first and final reads of the origin are both L. For
coarse L, interchange the two roles: one case is disconnected, and the other
word (RL)^B L (LR)^B reads the origin R twice. Rotation covers other headings.
Thus every nonidentity legal image contains ALL eight physical states.

## 2. Literal unequal-incidence transports really exist

At incoming N the following are internally legal unit images:

    R21 = LRLLLLRRRRLRRLRRLRRLL,                    (A,B)=(3,2);
    R29 = RRLLRLRRRRLRRRRLLLLRLRLLRLLRL,            (A,B)=(4,3);
    L29 = RLLRLRRRRLRRRRLLLLRLRLLRLLRLL,            (A,B)=(3,4).

Their exact charges are respectively +1,+1,-1. In particular unequal A,B
and lengths5 modulo8 are possible. R29 has every charge prefix nonnegative;
L29 has every charge prefix at least -1. So the two-letter ballot condition
alone does not force equality of the two incidence parameters.

These words were found as literal subwords of the blank orbit (intervals
1974..1995,3736..3765,3737..3766), but the frozen controls do not rely on that
origin: they derive their minimum input black sets and replay every cell.
The last interval's incoming E frame is rotated to N when interpreting L29.
Minimum input sets, complete output sets, visit supports and counts are in
`checker_axis_transport_controls.json`.

R21 cannot be used as a recurrent N-R image in a fixed eight-state exact-
charge controller: at position6 it has an N-R occurrence preceded by charge
-4, a negative self-loop in the signed prefix graph. This is a specific
negative cycle, not an inference from an arbitrary finite deficit.

## 3. A complete parity-character boundedness criterion

Take a fixed eight-state controller of internally legal unit images as above,
with at least one nonidentity image. Let M be its row-incidence matrix and
let d=1_U-1_V. In the sector normalized by incoming N at an even cell, d_s
is exactly checker-signed turn charge of state s. Set column vectors
A=(A_s), B=(B_s), delta=B-A. Formula (1) gives

    M=I+B 1_U^T+A 1_V^T,    M d=d+4 delta.                  (2)

The sequence M^r d is bounded entrywise IF AND ONLY IF one of the following
three integer alternatives holds:

    (i)   delta_s=0 for every state s;
    (ii)  sum_U delta=-1, sum_V delta=+1;
    (iii) sum_U delta=-2, sum_V delta=+2.                   (3)

These are exact boundedness alternatives for this observable, NOT sufficient
conditions for an ant trajectory.

Proof: the aggregate pair (1_U^T z,1_V^T z) evolves by

    Q = [[1+sum_U B, sum_U A],
         [sum_V B, 1+sum_V A]].

The starting pair for z=d is (4,-4). Every active row has A_s,B_s>=1, so Q
has a real Perron eigenvalue greater than one. Both eigenvalues are real,
since its discriminant is (Q11-Q22)^2+4 Q12 Q21>=0. Boundedness therefore
forces (1,-1) into the other eigenspace, with integer eigenvalue mu in
{-1,0,1}. Hence

    sum_U delta=mu-1,    sum_V delta=1-mu.

This argument also handles a triangular Q with only one active class: its
strictly larger eigenvalue is still greater than one. Under these equalities,
M delta=mu delta. Consequently

    M^r d=d+4(1+mu+...+mu^(r-1)) delta.

For mu=1 boundedness requires delta=0; for mu=0 and -1 it is automatic.
Conversely the displayed formula proves all three sufficient alternatives.
Exactly the same necessity follows if boundedness is assumed only on the
positive-power subsequence r=mj, because the Perron mode still diverges.

## 4. Finite-fuel consequence and genuine remaining modes

In any growing rooted power-limit of this fixed controller, an active image
contains all eight states, so they all occur in the actual path. Exact charge
preservation implies that the mass at each refinement of a FIXED actual
prefix is independent of refinement depth. The block refining any occurring
state is bounded between two such mass checkpoints. Its checker-signed board
change is therefore uniformly bounded. Thus a finite-seed realization MUST
satisfy one of (3), also for genuine root cycles.

Case(i) includes the elementary identity/nine alphabet just excluded at
arbitrary directive depth. Cases(ii) and(iii) are new algebraic escape modes:
the parity charge respectively stabilizes after one refinement or alternates
with period two. Other Fourier characters and full chronology can still fail.
For example, choosing R29 and L29 only at N-R and N-L, with all six other
images identities, meets(ii), yet its two growing first images conflict at
reads29 and32 upon the second refinement. This is a negative control, not a
surviving controller.

For an undecorated two-turn pair, rotational covariance gives

    sum_U delta=2(delta_R-delta_L).

Thus(ii) is unavailable. The criterion reduces to EITHER delta_R=delta_L=0,
OR delta_L=delta_R+1. Equivalently, for a normalized one-letter block its
checker charge obeys

    D_r=[1+2(delta_R-delta_L)] D_(r-1)
        +2(delta_R+delta_L),

and both initial values D_0=+1,-1 must remain bounded on genuine levels.
This applies to unequal image lengths as well as equal lengths.

## Scope

The two-parameter incidence identity is local geometry/charge algebra.
The boundedness criterion concerns a FIXED eight-state exact-charge controller;
it is not silently extended to arbitrary level schedules, decorated states,
non-unit spatial transformations or controllers whose individual charges are
not conserved. The explicit21/29 words refute a proposed general equal-axis
or length1-mod8 invariant, but do not supply a reusable construction.
