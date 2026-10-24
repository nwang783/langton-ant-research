# RRLL G3 strips have positive winding and exact irreducible unit gates

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d, positive output retained. Any C level c. No K1, root-free, low-
minimum or sign-homogeneity premise. The physical turn word IS assumed
to be RRLL repeated; arbitrary axis-drift curves are not covered.
Pending independent review.

Normalize the physical strip downwards as

    Z_k=(0,2k) -> A_k=(1,2k) -> B_(k-1)=(1,2k-1)
        -> Y_(k-1)=(0,2k-1) -> Z_(k-1).

There are4a full-quotient vertices. All complete modes are retained:

    Z+:SSNS, Z-:NSSS;
    A+:EEEW, A-:EWEE;
    B+:SSSN, B-:SNSS;
    Y+:WWEW, Y-:EWWW.

Plus/minus labels refer to the middle G3 node's outgoing R2/L1. Every
mode has the SAME face field and physical triple ports at its role.

## 1. Two complete unit circles lie inside each strip unit

The C face F_k at lower-left(0,2k-1), height c, has all four corners on
gamma: Z_k,A_k,B_(k-1),Y_(k-1). On sheet c every repaired arc is a RIGHT
turn around this face, so it is an elementary canonical C four-loop.
Its only possible exchange incidences are

    Z_k positive: negative/outgoing L1;
    Y_(k-1) negative: positive/outgoing R2.

Z negative and Y positive instead give unchanged R0 corners of F_k;
A/B give R0 corners in either mode. No off-strip corner or exchange
is omitted.

The L face Q_k at lower-left(0,2k), height c-3, also has all four corners
on gamma: Z_k,A_k,B_k,Y_k. On sheet c-2 every repaired arc is a LEFT turn,
so it is an elementary canonical L four-loop. Its only possible exchanges
are

    A_k positive: negative/outgoing L1;
    B_k negative: positive/outgoing R2.

The other modes and Z/Y give unchanged L3 corners. These are actual
canonical unit nodes, not geometric TOP-side alternative pairings.

## 2. Unit clocks force Z and A positive, with exact four-step brackets

Write Delta(v)=T2(v)-T1(v)>=4. Each unit node is contractible, length4.
Its signed clock identity forces

    EVERY Z_k is positive,
    Delta(Z_k)=4+1{Y_(k-1) negative} Delta(Y_(k-1));

    EVERY A_k is positive,
    Delta(A_k)=4+1{B_k negative} Delta(B_k).

Otherwise that unit face would have no negative incidence to balance
its length. This keeps both B/Y modes and all actual R0/L3 corners.

Summing the middle circle's signed clock and the two brackets gives

    P*w =12a + sum_(positive Y_k)Delta(Y_k)
                + sum_(positive B_k)Delta(B_k) >0.

Thus w=+1. The actual full drift is d=(0,-2a) in this normalization.
Every RRLL-strip G3 circle is positively essential; a negative-winding
circle CANNOT have this physical turn word. No primitive quotient is
substituted. The equality is one whole-period clock, not an additional
current payment.

## 3. Negative free gates give nonleaf parallel cycles, not erased pairs

For Y_(k-1) positive, F_k is a graph leaf with one exchange and
Delta(Z_k)=4. For Y_(k-1) negative, F_k has degree TWO, both exchanges
joining it to the SAME essential middle node, with

    Delta(Z_k)-Delta(Y_(k-1))=4.

Likewise Q_k is a leaf if B_k is positive, but a degree-two parallel
unit node when B_k is negative, with Delta(A_k)-Delta(B_k)=4.

These two-edge cycles are NOT the matched-port erasures79dcbbd4:
a matched pair would have equal Delta, whereas these clocks differ
by exactly four. Each unit node has no other incident exchange, so
none of its one or two edges can match an outside exchange either.
All these unit gates survive the full matched-port core.

For one strip, different negative B/Y gates have different unit nodes
and independent two-edge graph cycles, so beta is at least their count
(with the usual global even rounding). This is a distinct-node graph
reservation, not a paid root/fuel or an additive claim with overlapping
old budgets. The necessary negative-gate profiles are not asserted to
have an attained complete-front exterior.

## 4. Consequence for a G3 circle beside ANY local L minimum

Signed2b33fcce proves that a G3 circle whose low-L component is locally
minimal has physical word RRLL repeated, even if that component has
odd corners. Section2 now also fixes its winding POSITIVE. Therefore

    every G3 cycle at a locally minimal L component is axis AND +1;
    every negative-winding G3 cycle has a lower neighboring L face.

In particular no negative G3 cycle can sit at the global minimum L
level. The last statement does NOT exclude mixed negative cycles at
nonminimal plateaus, or rule out their deeper-height transfer. Positive
axis strips with old L3 stock, negative free gates and genuine odd
output elsewhere remain a live assembly mechanism.

The companion axis_triple_strip_unit_face_clocks.py/json reconstructs
all eight complete profiles, their exact face fields, canonical repaired
unit arcs and incidence signs. No front, period, drift, width, radius,
seed or multiplicity scan is performed.
