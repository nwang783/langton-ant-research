# One24-cell standard ant retains indispensable old z-cycle support forever

23 October2026. Separate author countercontrol, frozen for independent audit.
This is an actual finite seed with an infinite standard104 trajectory, not an
abstract state profile, a finite imitation, or a nonstandard counterexample.
The complete original field is retained at every update.

## 1. Exact statement and scope

Use N,E,S,W=0,1,2,3 and the retained standard word H of length104, started at
(0,0), heading W. Its displacement is d=(-2,-2). Let I be its retained13-cell
minimal seed:

    (-2,-4), (-2,-3), (-2,0), (-1,-5), (-1,-2), (-1,-1), (-1,0),
    (0,-6), (0,-5), (0,-4), (0,0), (1,-3), (1,-2).

Add EXACTLY these11 black cap cells:

    F={(-2,1), (-1,1), (0,1), (1,1), (1,0), (1,-1),
       (2,-2), (2,-3), (1,-4), (1,-5), (1,-6)}.

The fixed complete board I union F has24 black cells and follows H FOREVER.
Every F cell is unread throughout this entire infinite future. No distant
helper cells or N-dependent seed are used.

For EVERY period n>=1, at update18 of that period (global time t=104n+18):

- the actual head is q_n=(-2n-1,-2n-1), heading E;
- its current R-born black lifetime was born at104n+10, so has age EXACTLY8;
- the impending L is a bridge deletion in the FULL w graph (k=0);
- it is a nonbridge deletion in the FULL z graph (k=1);
- EVERY z black cycle through q_n contains at least one of the original,
  never-read F lifetimes.

Give original black lifetimes birth -1 and every R-born lifetime its actual
update index, with rewrites receiving NEW labels. Define the intrinsic cycle
bottleneck as the maximum, over cycles containing the edge, of the minimum
current-lifetime birth in that cycle. Its value at q_n is EXACTLY -1, so the
least possible age of the oldest support lifetime is EXACTLY

    104n+19 -> infinity,

while the deleted token always has age8. This is recurrent original support
within ONE fixed finite seed that is standard from its very first update.

The qualification matters: these are **z-only** erasures. The preceding
update17 is L too; update18 is a proper compressed block with r=0 and a w
bridge deletion. It is therefore an ORDINARY zipper block, not a genuine
w-exceptional renewal. This example does not contradict the oriented cubic
renewal law or the conditional w-input placement theorem. It refutes using
bounded-age support for ALL dual erasures as a necessary feature of capture.
An organization criterion must distinguish these orientations and scopes.

## 2. Certifying the infinite standard trajectory, without a horizon

Write E+j d for physical-cell translation. One literal104-update replay from
I is legal, returns the heading, and leaves exactly

    I+d union D,

where the disjoint12-cell output D is P union Q union R union S with

    P={(-4,-1),(-3,-1),(-3,0),(-2,-1)},
    Q={(-1,-8),(-1,-7),(-1,-6),(0,-7)},
    R={(-1,-2),(0,-3),(0,-2)},      S={(0,0)}.

For each physical cell x, all reads in the infinite geometric H stream are
exhausted by solving

    x=p_i+k d,     0<=i<104, k>=0.

For each i there is at most one integer k. The finite exact checker tests ALL
104 slots. It proves every D cell has no read with k>=1, and every F cell has
no read with k>=0. Thus D is permanent output, while F is completely unread.

Inductively the whole board at period entry n is EXACTLY

    (I+n d) union [union over j=0..n-1 of (D+j d)] union F.

All listed fields remain present. At any phase i, replace I by the actual
finite local phase-i state A_i obtained from I in the first period. The same
formula holds with A_i+n d. Old emitted outputs and F do not affect any
future read. This one-step induction and the complete integer read exclusion
prove H forever, rather than extrapolating from the finite controls.

## 3. A full-board two-rail decomposition at phase18

The proof below first describes the entire comparison board with F removed;
the ACTUAL board always retains F. This comparison is legitimate because
its infinite read stream was proved identical above, not assumed.

The z lattice is k=1. In doubled coordinates, the edge of physical cell(x,y)
has endpoints

    (2x-1,2y-s), (2x+1,2y+s),

where s=1 when (x+y) mod2=k and s=-1 otherwise. Put E_j=E+j d. Define

    W_n = union P_j (j=0..n-1)
          union R_j (j=0..n-2)
          union S_j (j=1..n-1),

    T_n = union Q_j (j=0..n-1).

An empty index range contributes nothing. Define the fixed current caps

    U={(-3,-1),(-3,0),(-2,0)},
    V={(-2,-4),(-2,-3),(-1,-5),(-1,-3),(-1,-2),
       (0,-6),(0,-5),(0,-4),(0,-3),(1,-3),(1,-2),
       (1,0),(2,-1),(2,0)}.

After removing the current q_n edge, the COMPLETE comparison graph has
EXACTLY these three components, including all its old output:

    C_u(n)=W_n union U_n,
    C_v(n)=T_n union V_n,
    S_0.

Their edge counts are8n-1, 4n+14, and1. The two endpoints of q_n lie in C_u
and C_v respectively. Thus q_n is a bridge before F is included.

Here are finite exact checks that establish the decomposition for EVERY n,
not merely its observed first instances.

1. A direct18-update local calculation gives

       A_18 minus {(-1,-1)} = U union (V minus (R-d)),
       R-d subset V.

   Splitting the old D copies into P,Q,R,S yields the displayed complete edge
   partition algebraically.
2. P,Q,U,V are connected. Each component of the fixed8-edge growth patch
   (P+d) union R union (S+d) touches P. Therefore W_n is connected by induction.
   The translated U cap touches its last P piece. Each Q copy touches the next,
   and the translated V cap touches the last Q. Thus both displayed rail-and-cap
   fields are connected for every n.
3. Their vertex sets, and the vertices of S_0, are mutually disjoint for EVERY
   n>=1. To check this, the code exhausts all possible collisions between
   vertices of the six fixed bases P,Q,R,S,U,V. Two translated vertices meet
   exactly when their translation indices differ by a particular integer.
   Each family has an explicit index interval, such as0<=j<=n-1 or j=n.
   For every possible collision offset, the two family index intervals can
   overlap only under four affine inequalities. Their exact integer-n domain
   is EMPTY. This excludes all remote parts of both rails; it is not a crop or
   an assumption that the graph has bounded size.
4. The q endpoints belong to U_n and V_n. There are no additional edges beyond
   the proved complete partition, so the two connected fields really are
   different complete components after q is removed.

The certificate records every base, family interval and possible collision
offset. The rail lengths grow with n; no finite-size summary is claimed for
arbitrary ants or arbitrary standard phases.

## 4. Why original support is both necessary and sufficient

The11 cap cells form a z path from (-5,1), a vertex of P_0, to (1,-13), a
vertex of Q_0. Both P_0 and Q_0 are present for every n>=1. Consequently F
connects C_u(n) to C_v(n), even after q_n is deleted. This gives a genuine
z bypass and makes q_n a nonbridge in the actual full board.

Conversely, in the complete comparison board those two components are
disjoint. EVERY actual bypass must therefore traverse some F edge. The same
is true of every black cycle through q_n. All F lifetimes are original and
never toggled, hence have birth -1. All other black lifetime births are >=-1.
Every such cycle therefore has minimum birth EXACTLY -1, and the intrinsic
maximum over ALL cycles is also -1. An arbitrarily chosen witness is not
being used to manufacture an old-age claim.

In particular the support age at the recurring target is104n+19, not merely
an upper bound from one unnecessarily long cycle. The unread cap persists
forever and supplies the indispensable old connection to every target.

## 5. Why these erasures are z-only, not w renewals

In the w lattice k=0, one endpoint of q_n is the vertex

    ell_n=(-1-4n,-1-4n).

Its four physical incident ports, normalized by n d, are

    (-1,-1), (-1,0), (0,-1), (0,0).

Before phase18, their last reads in the current period are respectively
R at10, L at11, L at9, and L at0. The latter three ports are therefore white.
Their complete read occurrence lists exclude any intervening read; they are
not F cells because all are actually read in this period. Hence ell_n has
EXACTLY degree1 in the complete w black graph, regardless of any other
unread archive. Its incident q_n edge is a bridge. The same local chronology
gives the consumed age18-10=8, including at every late period.

Together with the z bypass, this proves a genuine z-only erasure at a proper
r=0 ordinary block. Large and recurrent opposite-graph cycle support can
coexist with the desired standard zipper organization.

## 6. Frozen artifacts and implications

`check_standard_unread_cap.py` independently reconstructs the104-step local
trace, infinite read exclusions, complete all-n rail partition, every affine
vertex-collision exclusion, finite connectivity anchors, cap connection and
w-leaf chronology. Its artifact is `standard_unread_cap_certificate.json`.
The literal full-board controls through eight periods are only sanity checks;
the all-period deduction above does not depend on their horizon.

 This continuation does not modify the separately signed184-cell
finite-wave old-w-support theorem in
`../renewal_input_placement_2026-10-23/YOUNG_TOKEN_OLD_SUPPORT.md`.

The contrast is precise: fixed young DELETED lifetimes do not bound full
cycle-support age, even within a standard trajectory, if all dual erasures
are lumped together. The184-family theorem concerns genuine w-exceptional
renewals over arbitrarily long finite preparations. The present one-seed
infinite control concerns z-only ordinary deletions. Neither comparison
licenses a classification of arbitrary finite seeds or a capture proof.
