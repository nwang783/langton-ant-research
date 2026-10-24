# A strict-left straight K=1 ridge has a second, deep port pipeline

23 October 2026, 14:10 UTC. Analytic reduction and exact finite literal
controls, submitted for independent review. This is NOT a front exclusion.
The existing signed K=1 pipeline does not itself imply the extra straight
or strict-neighbor hypotheses below.

## 1. Exact hypotheses and coordinates

Retain a complete bi-infinite WHITE translating front of cap four, its
actual full P,d and the signed positively oriented first-L face-birth
curve Gamma. Assume its signed excess K=M-c_right is1. Thus the signed
crossing pipeline has RIGHT endpoints E(i)=i-1, next R0 index i+1, and
restricted chronology

    ... R0(v_i), R2(v_(i-1)), L1(v_i), R0(v_(i+1)), ... .

Now add two genuinely EXTRA geometric hypotheses:

1. Gamma is a straight diagonal, in the normalization
   v_i=(-i,i), d=(-ell,ell), all selected prefixes incoming N,N,S.
2. At the LEFT corner z_i=(-i,i-1) of the parent maximum face F_i,
   the other incident C face G_i has h(G_i)<M, for EVERY lifted i.

F_i has corners v_i,z_i,v_(i-1),w_i=(-i+1,i). Its SW corner is z_i.
G_i is the C face SW of z_i. LEFT is x+y<0 and RIGHT is x+y>0.
No condition is imposed on the other C faces at RIGHT corners w_i, and
no nearest-path restriction is imposed on actual RIGHT excursions.
Let T_r(x) be the complete physical rank-r read time, not its phase.

## 2. Forced selected and near-corner histories

Every R at z_i chooses F_i by the signed cap-four maximum rule; hence
it arrives W and departs N. The first W output of selected v_(i-1) is
its L1 and the first N input of v_i is its R0. Ordinal matching gives

    T_0(z_i)=T_1(v_(i-1))+1,
    T_0(v_i)=T_1(v_(i-1))+2.                         (1)

The next W arrival at z_i is supplied by R2(v_(i-1)). Suppose L1(z_i)
arrived E. It would depart N, the second N output of z_i, and would
supply L1(v_i). But z_i would still need its next W arrival R2, so
L1(z_i) would precede R2(v_(i-1)). This would put L1(v_i) BEFORE that
RIGHT endpoint, contradicting the signed K=1 chronological order.
Therefore L1(z_i) arrives W and departs S.

L1(v_i) still needs a second N output from z_i. It must be R2(z_i),
whose W input is the THIRD W arrival at z_i. The source v_(i-1) must
therefore have L3 arriving N and departing W. Applying this at all i
forces every selected contact to have the complete history

    v_i: RLRL, incoming N,N,S,N.                     (2)

R2(z_i) feeds L1(v_i) consecutively:

    T_2(z_i)=T_3(v_(i-1))+1,
    T_1(v_i)=T_3(v_(i-1))+2.                        (3)

Finally L3(v_i), the third N input, requires the third N output of z_i.
Since its L1 went S, this must be L3(z_i) arriving E. Consequently

    z_i: RLRL, incoming W,W,W,E,
    T_3(z_i)=T_3(v_i)-1=T_1(v_(i+1))-3.             (4)

Both R reads at z_i choose F_i and neither chooses G_i. The local
R-count height rule also gives h(G_i)=M-2, not M-1. In fact the exclusion
of h(G_i)=M-1 at any ONE such corner only uses its own strict inequality;
the all-i assumption is needed for the complete repeated strip below.
No optional L3 has been discarded: ordinal matching FORCES these L3s.

## 3. The contiguous LEFT stage and its deep boundary

Set q_i=(-i,i-2). Consider D_i, the actual interval from R2(v_(i-1))
to L3(v_(i-1)), including its two endpoint reads when naming the states.
Immediately after its first read the ant reaches L1(z_i), then q_i
with incoming S. At its other end it must come from q_i outgoing E,
through L3(z_(i-1)), then reach L3(v_(i-1)) with incoming N.

All other selected contacts are unavailable during the open interval:
older contacts have completed L3 by (3); future ones have not reached
their next permitted selected event. At z corners, only z_i at its first
step and z_(i-1) at its last step can be used. Their other required reads
are respectively before or after D_i by (1)-(4). Hence between those two
near-corner wrapper steps all reads lie in x+y<=-2.

The complete port counts are particularly rigid:

- z_i has one S output, namely L1, so q_i has ONE S input in its whole
  white history. This is the entry during D_i.
- z_(i-1) has one E input, namely L3, so q_i has ONE E output in its whole
  white history. This is the exit during D_i.

A prior first R of q_i with incoming N would already emit that sole E
output and force its exit through z_(i-1),v_(i-1) before the unique S
entry. The entry is two steps after R2(v_(i-1)) and that exit is two
steps before its later L3; their order cannot be reversed. In particular
there is no room for such a prior N read between R2 and the S entry.
White first-read R and the unique S input therefore force

    q_i: R0(S), L1(N), R2(N), optionally L3(N).       (5)

Its R2 is the unique E output. This is not an assumed empty deep input.
All earlier helper colors and visits strictly below the port row remain.

For j<i, R2(q_j) has already occurred, since
T_2(q_j)=T_1(v_j)-4<T_2(v_(i-1)). Its only possible remaining read during
D_i is one L3 arriving N. For j>i its first S entry has not yet occurred,
so it cannot be visited during D_i. Normalize q_i to(0,0). The exact
relaxed deep machine is therefore:

    interior x+y<0: arbitrary current colors, alternating repeats,
      at most4 visible reads if first visible R, at most3 if first L;
    old ports (a,-a), a>0: at most one read L incoming N;
    future ports (-a,a), a>0: forbidden;
    current port: R(S), then L(N), then endpoint arrival N for R.

The relaxed counts allow arbitrary omitted earlier R provenance. They
are necessary conditions, not sufficient conditions for any white front.

## 4. An exact finite lower bound, not an unbounded detour exclusion

The q0-to-q2 time span is a positive multiple of4. Each consecutive local
return costs at least4, so its span is at least8. The exact alternating-
color factor enumeration in lower_port_joint_return.py has no span8 or
span12 and has exactly two span16 factors (endpoint R not included):

    RRRLRRLRRLRRLLLL
    RLLLLRRLRRLRRLRR

The first visits future port(-1,1) at offset2 with R(N); the second does
so at offset6. Both violate the proved deep boundary. An independent
halfplane enumeration deep_lower_port_control.py gives respectively
0,0,0,1 factors at spans8,12,16,20. The unique span20 factor is

    RLRRRRLLLLRLLRLLRLLR .

It uses old port(1,-1) once with L(N), at offset18. Its helper colors are
explicitly prepared; whole-front history funding is NOT asserted.

It follows from the complete short-factor exclusion that

    T_2(q_i)-T_0(q_i)>=20,
    span(D_i)=T_3(v_(i-1))-T_2(v_(i-1))>=24.         (6)

Let a_i=T_2(v_(i-1))-T_0(v_i) be the RIGHT excursion length. Its endpoint
separation is(1,-1), so a_i>=2, even with arbitrary RIGHT detours.
After D_i, the route is forced through R2(z_i),L1(v_i),R0(z_(i+1)),
R0(v_(i+1)), costing four more steps. Thus

    T_0(v_(i+1))-T_0(v_i)=a_i+span(D_i)+4>=30,
    P>=30*ell.                                      (7)

This is conditional on BOTH extra hypotheses in Section1. It does not
prove K>=2, does not remove M-height branches on the LEFT, and does not
classify bent Gamma curves. It is not added to overlapping old budgets.

## 5. Controls against unjustified exclusion or fuel potentials

A prepared period10 translator RRRLLLLRLR with d=(-1,1) realizes the
straight contact and near-corner histories, but its q port is a singleton
L, not white-first R. It consumes one black lower-rail cell per stage and
leaves one black RIGHT cell. Explicit n-stage finite seeds are checked
for n=1,2,3,10,100 in straight_pipeline_controls.py/json. This refutes an
unconditional local/coloring exclusion, NOT the white-front claim.

Nor does every necessary deep packet consume total black mass. The
literal25-read word RLRRRRLLLLRLRRRRLRLLRLLRR (INCLUDING final q R)
obeys the relaxed deep rules and gains3 black cells. Its prepared input is

    {(-1,-3),(-1,0),(0,-3),(0,-1),(1,-2),(1,-1)}

and its output is

    {(-3,-2),(-3,-1),(-2,-1),(-2,0),(-1,-2),(-1,-1),
     (0,-2),(0,-1),(0,0)}.

One input is the explicit old L3 port(1,-1); the other helper provenance
is NOT constructed. This blocks a naive black-mass-loss potential for
individual deep packets. It does not establish a sustainable translator,
a complete white front, or any transport from the physical RIGHT current
back to the LEFT. Both side-current boundaries remain enforced.
