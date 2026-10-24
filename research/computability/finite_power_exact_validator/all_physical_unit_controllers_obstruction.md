# Fixed physical-state unit controllers cannot generate an ant path

2026-10-23 05:25 UTC. Analytic assembly independently reviewed at05:27 UTC.
It removes the exact-charge assumption from the signed eight-state theorem JK.
Dependencies: the charge-free unit incidence lemma, the unique-parent origin
lemma, and the signed positive-clock/finite-valued rational-series argument.

## Statement

For each of the eight UNDECORATED physical states (incoming compass heading,
R or L turn), choose a finite nonempty turn image with the same incoming
heading, final heading and unit displacement as that single coarse action.
Lengths and signed turn charges may be arbitrary and unequal. Identity images
are allowed. Use the same controller at every refinement level.

No growing rooted power-limit of this controller is a Langton-ant trajectory
on ANY initial coloring. No finite-support, symmetry, image-length bound,
charge-preservation or primitivity assumption is imposed.

Extra hidden/context labels, changing controllers and unequal spatial rules
remain outside the statement. A root-cycle power is allowed, but only the
actual growing rooted phase is assumed legal.

## 1. Incidence domination and the unique-parent origin lemma

Pass to the controller power defining the actual fixed rooted limit. Exact
unit poses persist, and each reachable state's iterated images are actual
factors of the proposed path. Every such image is therefore internally legal.

The charge-free identity `unit_transport_incidence.md` proves that the count
vector of every unit-pose image dominates the identity parent vector. Its
correction has equal counts on opposite-heading R states and equal counts on
opposite-heading L states. Thus every image contains its own physical state.

If the parent occurs exactly once, its opposite-heading same-turn state occurs
zero times. Both the first and the last read of a nonidentity image are at the
origin: the last movement equals the coarse final heading and ends at its unit
endpoint. All origin reads have the initial incoming axis. Their alternating
turns include the parent's turn, since there are at least two such reads.
Among physical states with that turn and axis only the parent and its opposite
are possible. The latter is absent, so the unique parent read is at the origin.
For an identity image the same assertion is immediate.

This is exactly the companion `causal_reduction/unit_scale/
unique_parent_origin_lemma.md`, written without a rotation/reflection shortcut.
It uses physical-state uniqueness, not uniqueness of an arbitrary hidden label.

## 2. Choose a terminal component among active states

Call a reachable state active if its image is nonidentity. A growing root
reaches an active state. Consider the directed child graph restricted to active
states and select a terminal strongly connected component T. Its outgoing
children outside T are all identity states. Write the exact weighted incidence
matrix on T and these absorbers as

    M(X,Y) = [[B(X,Y), C(X,Y)], [0,I]].

Every diagonal of B has at least one parent occurrence. B is irreducible at
all positive characters.

A singleton T={s} with exactly one self occurrence is impossible. Write its
image as U s V, where every letter in U,V is an identity state. The origin
lemma says net(U)=0. Matching the complete unit endpoint then gives net(V)=0.
The physical poses also match at these seams. Consequently

    phi^r(s)=U^r s V^r

has a footprint in one fixed finite set, while its length tends to infinity
because s is active. Finite-domain escape rules out these legal blocks on any
background (copy the finite footprint's colors when necessary).

In all remaining cases, the incidence Perron value lambda(1,1) of B exceeds
one. This is immediate for a singleton with at least two self children. For
multiple states, B(1,1)>=I and irreducibility supplies an off-diagonal cycle.

## 3. A nonempty positive-clock domain

If every state of T has exactly one self occurrence, the origin lemma gives
B(X,Y)>=I at every positive character. Irreducibility and an off-diagonal
cycle give lambda(X,Y)>1 everywhere.

Otherwise some B_ss contains at least two monomial occurrences. If all these
self offsets are zero, B_ss>=2 everywhere. If a self offset q is nonzero,
choose a real vector z with nonzero coordinates and z dot q>0. Along
(X,Y)=(exp(t z_x),exp(t z_y)), that diagonal monomial tends to infinity.
A physical quarter rotation makes both transformed log coordinates positive.
For sufficiently large t, lambda>1 and the rotated strict exponential clock
has positive one-read increment g at every physical state. These inequalities
hold on a nonempty open set U. No reflection is needed.

## 4. The uncancelled Perron pole gives the contradiction

Let d be the rotated checker-signed turn vector and H its literal endpoint
head-correction vector. Exact unit poses give, for every r,

    M^r g = H-M^r d,                g=H-d>0 on U.

Since identity states are absorbers, the T-part of the generating resolvent is

    (I-tB)^(-1) [g_T+t C g_I/(1-t)].

At t0=1/lambda in(0,1) the forcing bracket is strictly positive. The Perron
pole is genuine in every T-coordinate, and the endpoint term H/(1-t) cannot
cancel it. Thus the checker-occupation series sum_r t^r(M^r d)_s has a genuine
pole at t0 for every character in U.

Every refined block is internally ant-legal, so its checker-occupation
coefficients are in {-1,0,1}. Exact unit geometry makes its read offsets O(r).
The independently signed finite-valued rational-series theorem supplies a fixed
semilinear denominator P_s(t,X,Y), a product of factors 1-t^a X^b Y^c with
positive integer a. Hence P_s(1/lambda,X,Y)=0 throughout U.

The Perron eigenvalue of the irreducible B is real-analytic on the connected
positive quadrant. Analytic continuation gives the same equality at X=Y=1,
where lambda(1,1)>1. But P_s(t,1,1) is a product of 1-t^a and has no positive
zero strictly below one. Contradiction.

## 5. Finite-order typed corollary and limits

If an eight-state physical controller instead has one common finite-order
spatial matrix A and the same coarse final-heading compatibility, take a power
divisible by its spatial order and by the actual first-letter root cycle.
Its powered images have exact unit poses and remain an eight-state controller.
The theorem therefore excludes that class too, without local charge bounds.

This is a closure of one fixed reusable-construction architecture, not a proof
of capture for arbitrary finite seeds. The arbitrary-mass realization decider
JE/JF still has residual scope for extra decorated states, general nonuniform
finite-power presentations, and other inputs not covered by this obstruction.
No growing ant model or finite-support universal compiler is supplied.
