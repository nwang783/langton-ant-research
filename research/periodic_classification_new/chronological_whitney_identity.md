# An integer chronological crossing identity for translating turn paths

22 October 2026, 22:10 UTC. Sections 1–3 independently analytically reviewed on 22 October 2026.
Section 4 is explicitly scoped finite-path boundary bookkeeping.
This is a necessary identity, not a highway classification.

## Statement

Let a finite word of quarter turns R,L have length P, restore its heading,
and have nonzero full displacement d. Repeat it in both time directions.
No color feasibility assumption is needed.

For each displacement class, write the phase positions as q_i=b+k_i d.
Order that class's events by tau_i=i-P k_i. These are the chronological
reads of any sufficiently translated physical representative. Let c_i be
the turn and h_i the incoming heading. Any two h_i in one class are equal
or opposite: heading reset forces P even, and the checkerboard/time-parity
invariant fixes the incoming axis at each physical cell.

Define

    K = sum over classes, and i before j with c_i=L, c_j=R,
          { +1 if h_j=-h_i,
            -1 if h_j= h_i }.

Then the exact identity is

    (#R - #L) / 4 = K.                                  (1)

The drift must be the full displacement, not its primitive direction.
Stable chronological order, not raw phase order, is essential.

## 1. Chronological lanes

Every lattice edge used by the repeated path is traversed in only one
direction. Indeed the checkerboard parity fixes the incoming axis at a
vertex and hence the outgoing perpendicular axis. An edge joins vertices
of opposite checker parity, and its other direction is incompatible with
this axis assignment.

Replace the occurrences of each directed physical edge by parallel lanes,
ordered increasingly in time from right to left as viewed along travel.
The same chronological order appears at the two ends of the edge, so
lanes join without crossings along edges. Use the entire doubly infinite
periodic trace to choose the ranks; each edge has finitely many occurrences,
and the construction is translation-periodic.

Around each lattice vertex take a small disjoint disk. The endpoints of
all incident lanes lie on its four small port arcs. Join each incoming
endpoint to its prescribed outgoing endpoint by a chord, with a small
smoothing near the disk boundary. A generic perturbation removes triple
crossings. The arcs have total tangent turn -pi/2 for R, +pi/2 for L;
there are no extra full turns. Straight lane portions contribute none.

The cyclic port order gives the following complete pair table:

- Equal-turn pairs do not cross.
- R followed by L does not cross.
- L followed by R crosses exactly once. Equal incoming headings mean
  a shared incoming port; opposite headings mean a shared outgoing port.

For an explicit endpoint check, label the earlier arc a and later arc b,
rotate the earlier incoming heading to north, and read boundary endpoints
clockwise in port order N,E,S,W. Within an incoming port the clockwise order
is a,b; within an outgoing port it is b,a. Up to cyclic rotation, the eight
pair cases are:

    turns    equal incoming     opposite incoming
    R,R      b,a,a,b            b,a,a,b
    L,L      a,b,b,a            b,b,a,a
    R,L      a,a,b,b            b,b,a,a
    L,R      b,a,b,a            b,a,b,a

Only the last row alternates. Equal-turn arcs with opposite incoming
headings also lie at opposite corners, in agreement with the table.

Here the ordering is chronological at that physical vertex. Chords meet
exactly when their endpoints alternate around the disk. This proves the
table even if many other arcs occur in the same disk.

For a crossing, order its tangent vectors earlier then later. Let its
sign be sign det(v_earlier,v_later), with the usual counterclockwise plane
orientation. A shared incoming port has sign -1; a shared outgoing port
has sign +1. For example, with common northward incoming direction,
the earlier L tangent points northwest and the later R tangent northeast,
giving a negative determinant. With eastward common outgoing direction,
the earlier L tangent points southeast and the later R tangent northeast,
giving a positive determinant. Rotations preserve these signs.

Thus the signed crossing sum per translation is exactly K.

## 2. Close a long finite segment outside the strip

The regularized curve is contained in a strip of bounded width transverse
to d. Take N consecutive periods. Join the final endpoint to the initial
endpoint along a line outside the strip, with bounded endpoint connectors.
The connectors may be chosen in bounded neighborhoods of the two ends,
so they intersect only O(1) pieces of the periodic trace, independent of N.
The long outside portion has no crossings with the trace. Smooth the
closure with bounded total tangent turn and choose the curve's base point
on an outside support line.

For every local crossing orbit, N periods contain N+O(1) copies with both
visits inside the segment. The O(1) depends on the fixed word's largest
chronological span, not on N. Consequently the closed curve has:

    clockwise rotation number = N (#R-#L)/4 + O(1),
    signed chronological crossing sum = N K + O(1).

Whitney's plane-curve index formula, with an outside base point, says that
the clockwise rotation number equals this determinant-signed crossing sum
plus a base-point term of magnitude one. (Whitney uses the opposite sign
for a positive crossing and counts counterclockwise rotation.) Divide by
N and let N grow. This proves (1).

The only external geometric ingredient is the classical index formula:
Hassler Whitney, “On regular closed curves in the plane,” Compositio
Mathematica 4 (1937), 276–284, Theorem 2.
https://www.numdam.org/item/CM_1937__4__276_0/

## 3. White-input cap-three consequence

Assume now each class has history R, RL, or RLR. For a triple, normalize
its first incoming heading as A. The four heading patterns and their
contributions to K are

    AAA : -1       A,-A,A : +1
    A,A,-A : +1    A,-A,-A : -1.

The same-heading triple-edge pairing theorem gives equal numbers of the
first two patterns. Write A_count for the number of A,A,-A classes and
B_count for the number of A,-A,-A classes. Then

    g = 4(A_count-B_count),                              (2)
    n1 + ns + 5 B_count = 3 A_count.                      (3)

Here g is the odd-class count, n1 the singleton count, and ns the total
same-heading triple count. In particular A_count-B_count >=2 by the
existing all-period growth lower bound g>=8.

A separate sharpened use of the earlier port-capacity proof notes that
an R4 marker is specifically of type A,A,-A, so R4<=A_count. Combining
this with L1<=A_count+B_count-L4+ns/2 and
 g=-R1+2R4+L1-2L4 gives

    n1 + R1 + 3 L4 + ns/2 <= 2 A_count.

Using (3) yields

    A_count + R1 + 3 L4 <= 5 B_count + ns/2.              (4)

For the late cap-three periodic setting L4=0 by the separately reviewed
L4 exclusion. Equations (2)–(4) remain necessary restrictions only.

## Scope and controls

Identity (1) is geometric and does not require alternating color reads,
finite initial support, or a multiplicity cap. Only the consequences in
Section 3 require white input and cap three. The existing nonwhite rail
word RRLRRRRL has K=1 and excess4, so is fully consistent with (1).
Standard104 has K=3 and excess12. Exact finite random checks are controls,
not the proof. No uniqueness or nonexistence conclusion follows here.

## 4. Finite-path boundary term, without a uniform bound

For a finite turn path, make the same chronological lane regularization,
including a virtual incoming stub before the first read and the actual
outgoing stub after the final read. Its local signed crossing sum K_T is
given by the same L-before-R pair formula over the actual physical read
histories, not displacement classes.

Choose a simple generic closing arc eta from its endpoint to its start,
with some point of eta on an outside support line of the entire closed
curve. A two-segment detour through a sufficiently distant exterior point,
with smoothed corners and endpoint joins, is enough. Let C_eta be the
clockwise tangent turn along the closure, including the endpoint joins,
divided by 2pi. Choose the outside base point on eta. Let I_eta be the signed sum of
closure/trace crossings in the resulting base-point order: a closing-arc
piece traversed before the trace has its tangent first in the determinant,
and a piece traversed after the trace has its tangent second. The trace
events retain their original chronological order, and Whitney's formula gives

    (#R-#L)/4 - K_T = I_eta + kappa - C_eta,              (5)

where kappa is the outside-base-point correction, equal to +1 or -1.
The closure itself is simple, so it contributes no self-crossing sum.
The two-segment construction has bounded turning, but I_eta is NOT
uniformly bounded for arbitrary finite paths.

For example, the geometric turn word R^(4N) traces the same right-turn
square N times. It has K_T=0 while (#R-#L)/4=N. Its regularization is a
nested clockwise spiral, and any suitable exterior closure pays the
corresponding unbounded boundary intersection term. This word is not a
feasible white-input ant history for N>1; it is an exact warning against
silently dropping the boundary term in an arbitrary finite-path argument.
Thus (5) is an identity, not a finite-seed core-curvature bound.
