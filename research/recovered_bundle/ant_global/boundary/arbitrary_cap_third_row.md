# Third-row accounting without an initial freshness assumption

Working theorem and proof, 21 October 2026. Independent source reviews
found no gap in the stronger injective charging argument. This extends the supplied fresh-cap
lemma. It concerns one finite actual trajectory. It is not a proof of global
highway capture. Independent review is requested.

## Statement

Use E,S,W,N as the four headings, with a white cell turning right and a black
cell turning left. Set

    T_r=(r,-r), A_r=(r,-1-r), B_r=(r,-2-r), C_r=(r,-3-r).

Take a finite trajectory segment that starts and ends at x+y<=-4, stays at
x+y<=0, and has the heading sector in which visits to the top row T arrive
from below with heading E. **All initial colors are arbitrary.** Only finitely
many processed events are counted; initial black support need not be finite.

For a row X, let N_X count processed events and let Delta_X be the sum of
final minus initial black indicators over its visited cells. Let M=N_T.
Let H count black A events with incoming S and outgoing E. Let E_B count
white B events with incoming W and outgoing N. Define

    D = E_B-M+2H.

Let Q count black A events with incoming N and outgoing W. Let K_C count
black C events with incoming S and outgoing E. Define

    Z = K_C+2D+H-Q.

Then D,Z are nonnegative integers, and

    Q   = 2M-Delta_A-3H,
    N_A = 4M-Delta_A-4H,
    N_B = 8M-4Delta_A+Delta_B-8H-4D,
    N_C = 12M-8Delta_A+4Delta_B-Delta_C-8D-4Z.

In particular,

    N_C <= 12M-8Delta_A+4Delta_B-Delta_C-8D.

Every H event is the first and only visit to an initially black A cell.
Thus H is at most the number of initially black A cells. That last number
is only needed on the visited footprint if the row has infinitely many blacks.

The third-row identity and upper bound have the same form as the fresh-cap
result. The definition of D changes by 2H. The first two row identities retain
explicit bridge corrections. When A starts white, H=0 and this reduces to
the earlier theorem. Initial black cells on T are never visited.

## 1. Top visits and roofs

A visit to T arrives E. A black read would turn N and leave the allowed
half-plane. Thus each top visit is white; a visited T cell is visited only once
and was initially white.

At A, the two possible upper ports are the arrival from T_r and the departure
to T_(r+1). Each occurs at most once. Every white A event uses exactly one upper
port. A black A event either uses no upper port (N to W) or both (S to E).
If the latter event occurs, it uses all upper ports at that A cell. There can
be no other white A event. Alternation of colors then excludes every other
visit. The cell was initially black and this is its only visit.

Call such a black S-to-E event a bridge. Each maximal chain of top visits joined
by bridges is a roof. A roof starts and ends on B. With k>=0 bridges, it has
k+1 top visits and follows

    B_r -> A_r -> T_(r+1) -> A_(r+1) -> ...
        -> T_(r+k+1) -> A_(r+k+1) -> B_(r+k).

The first and last A events are white. All k interior A events are black
bridges. The roof length, from departure from its first B cell through arrival
at its last B cell, is 4+2k. The endpoint condition makes all roofs complete.

Let J_0 count roofs with k=0, and let J_+ count roofs with k>0. Then

    M=J_0+J_++H,
    rho:=H-J_+ = sum_(positive roofs)(k-1) >= 0.

A zero-bridge roof is the literal B first-return diamond from the earlier
proof. Exactly one B endpoint is a white upper corner. Different zero roofs
use different B cells and therefore give different charged corners. Put

    D_0 = E_B-J_0 >= 0.

Then

    D = D_0+rho >= 0.

The extra contribution rho counts all bridges beyond the first bridge in each
positive roof. No symmetry or spatial connectedness of the top footprint is
assumed.

## 2. Upper port counts

The top visits supply 2M upper ports to A. A bridge uses two; a white A event
uses one. Therefore W_A=2M-2H. The total black A count is Q+H, so

    Delta_A=W_A-Q-H=2M-3H-Q,
    N_A=W_A+Q+H=4M-Delta_A-4H.

Let I_B be the number of B-to-A crossings, equal to the number of A-to-B
crossings. Row flow gives I_B=N_A-M. At B, a black event uses exactly one
upper port, a white upper corner uses two, and every other white event uses
none. If L_B is the black-event count on B, then

    2I_B = L_B+2E_B,
    N_B=2L_B+Delta_B=4I_B-4E_B+Delta_B.

Substitution gives the asserted N_B identity. These equalities use no initial
color assumption.

## 3. Marked black lower A events

Make Q vertices, one per black lower A event (N to W). Mark a vertex if its
immediately preceding or following B event is one of the D_0 white upper
corners not charged to a zero roof. Each such corner has at most two adjacent
A events, so at most 2D_0 vertices are marked. Let U be the number unmarked.
Then

    U >= Q-2D_0.

Each unmarked black A_s event gives a literal upper first return to C_(s-1).
The incoming path is C_(s-1) to B_s to A_s, with at most one zero roof inserted
at B_s. Indeed a white predecessor B_s is charged to a zero roof and must be
its second endpoint, since its successor A_s is black. The outgoing path is
A_s to B_(s-1) to C_(s-1), with at most one zero roof inserted at B_(s-1).
A white successor must be the first endpoint of its charged zero roof.

The combined path has no C event in its interior and contains only the chosen
black lower A event; the A events in inserted zero roofs are white. Its two C
endpoints are consecutive visits to the same physical cell and have opposite
colors. Exactly one endpoint is a black C upper corner. Assign that corner
to this unmarked A event.

Different physical A cells assign corners at different physical C cells.
Only two unmarked events at the same A cell can collide.

## 4. All assigned C charges are distinct

Only returns from the same A_s can assign the same physical C corner. Suppose
two assigned first returns share their black C corner. Then that corner is
the end of the earlier return and the start of the later return. The returns
are contiguous upper excursions at C_(s-1). There is no intervening activity.

Let a in {0,1} record whether the earlier return has its right zero roof at
B_s. Let b in {0,1} record whether it has its left zero roof at B_(s-1).
These are the only optional parts of an unmarked event's return.

If a=0, B_s was processed once, on black, and is left white. The shared black
C event next departs E to B_s. Its white turn goes S to the different cell
C_s. Thus the next upper excursion cannot be an assigned first return through
A_s. This excludes a=0.

Suppose a=1 and b=0. The right roof processes B_s twice, leaving it black.
It includes a white A_s upper departure before the selected black A_s event.
With no left roof, A_s is left white. The next C departure goes E to black
B_s, then N to white A_s, then E to T_(s+1). But this T cell was already used
in the first return's right roof. A second top visit is black and would leave
the cap. The proposed next assigned return cannot occur. This excludes b=0.

Finally suppose a=b=1. At the end of the first return the three relevant
colors are

    B_s black, A_s black, B_(s-1) white.

The first two follow from the right roof and the white A_s upper arrival in
the left roof. The left B color follows because that roof starts there on
white and ends there on black, leaving it white.

The next C departure therefore goes E to black B_s, N to black A_s, and W to
white B_(s-1). This white B upper corner is extra: the only zero roof at that
B cell would use T_s, which the preceding return already visited. Thus the
second selected black A_s event is marked, a contradiction.

All three possibilities are excluded. The assigned C charges are injective.
The proof uses only the two literal return shapes and their endpoint colors.
It needs no assumption about the initial color or total visit count of A_s.
Consequently

    K_C >= U >= Q-2D_0.

Define the nonnegative integer

    Z_0 = K_C+2D_0-Q >= 0.

Since D=D_0+rho,

    Z = K_C+2D+H-Q = Z_0+H+2rho >= 0.

This strengthens the initial version of the argument, which allowed a
hypothetical loss at the right endpoint of a positive roof. Such losses in
fact cannot occur: every assigned return itself contains only zero roofs.

## 5. Third-row identity

Let I_C count upward crossings from C. Row flow gives

    I_C=N_B-N_A+M
       =5M-3Delta_A+Delta_B-4H-4D.

At C, every white event uses one upper port, black upper corners use two,
and black lower corners use none. Hence

    N_C=4I_C-4K_C-Delta_C.

Replace K_C by Z-2D-H+Q and Q by 2M-Delta_A-3H. The H terms cancel:

    N_C=12M-8Delta_A+4Delta_B-Delta_C-8D-4Z.

One can retain the roof surplus for a stronger displayed bound:

    N_C <= 12M-8Delta_A+4Delta_B-Delta_C-8D-4H-8rho.

The exact identity can be written using only the four nonnegative quantities
D_0, H, rho, and Z_0:

    N_C=12M-8Delta_A+4Delta_B-Delta_C
        -8D_0-4H-16rho-4Z_0.

## 6. Scope and global gap

This removes the initial freshness condition from the third-row accounting.
It permits concatenating completed excursions under the same fixed cap without
resetting A, B, or C to white. The formulas still count the exact signed color
changes and include bridges through old A cells.

The cap condition remains. If a later segment crosses above T, it is not covered
by the same capped segment. Under a new cap, H,D,Z and the row roles change.
In particular, the theorem does not bound their accumulated values over moving
caps, and does not prove a finite budget for nonstandard motion.

The known 24-step fresh-cap witness still gives equality, so the upper bound
remains sharp in the class covered here. New exhaustive and random checks use
arbitrary initial colors on A, B, C and lower rows. Their purpose is to audit
the proof and definitions, not to establish universal truth by testing.
