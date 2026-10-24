# A strict-fall entrance forces a lower maximum and a paired RRRR stock loop

23 October 2026, 19:24 UTC. Exact branchful supplier closure, submitted
for independent review. This is old stock plus black output production,
not an original-fuel payment or a general K1 exclusion.

## 1. Scope and retained entrance alternatives

Use the complete WHITE cap-four K1 scope of the signed double-max
successor and predecessor-alternative notes. The current STRAIGHT F=(0,0)
has LEFT max J=(-1,-1), entry U=(1,0), exit A=(0,1), helper z=(0,0),
with z=WWEE and U,A=NNS or NNSS. Here C coordinates are lower-left corners.
Its RIGHT successor has helpers w=(-1,1), y=(-1,2), exit B=(0,2), and
lower corner e=(-1,0). The signed successor table gives e=NSS or NSSN.

Assume the entrance is one of the genuine STRICT state falls retained
by the predecessor theorem: either the preceding face is strict STRAIGHT,
or it is RIGHT with strict second LEFT neighbor. Both have

    r=(1,-1): WWW, K=(0,-2) at M-2,
    q=(0,-1): SNS or SNSN.

Put u=(-1,-1), whose two C faces are J(NE) and Q=(-2,-2)(SW).
All complete histories, including earlier R0 suppliers, are retained.

## 2. Closing the three/four-W supplier exactly

q emits W at EVERY read. Its three or four outputs are the COMPLETE
W inputs at u. Its N/S headings are SNS or SNSN, while the signed
forward corner gives e's complete N/S headings NSS or NSSN.
Match the complete physical ports

    q --W--> u --N--> e --E--> z --S--> q.

If u has three W inputs, its possible complete headings are

    WWW, WWWE, WEWW, WWEW, EWWW.

If it has four, its complete headings are WWWW. This exhausts cap four
with the incoming axis E/W and every possible R0/L1/R2/L3 ordering.
WWWE and WEWW emit N three times, but e has at most two N inputs, so
both are impossible.

For WWW or WWWW, the actual ordinal matches force

    u.R0 -> e.R0 -> z.R2 -> q.R2 -> u.R2.

This would put two R ranks at u only four reads apart, with its L1
strictly between: T2(u)-T0(u)>=8. Contradiction. For WWEW they force

    u.R0 -> e.R0 -> z.R2 -> q.R2 -> u.L3,

placing rank0 and rank3 four reads apart instead of at least12.
Consequently the ONLY remaining possibility is

    u=EWWW, q=SNS, e=NSS, h(Q)=M.                    (1)

In particular the optional q.L3 and e.L3 have now been genuinely
eliminated by exact supplier chronology, not dropped from the input.
A saved closure control reconstructs exactly these possibilities from
the independently signed successor histories and complete physical ports.

## 3. A second actual stock loop, not a removable state identity

In (1) the exact consecutive events are

    u.R2 -> e.R0 -> z.R2 -> q.R2 -> u.L3.            (2)

The four departures are uninterrupted R,R,R,R. Thus T3(u)-T2(u)=4.
The cursor returns to u with the same incoming W heading, but four
cell colors have changed. This is not a same-state deletion or a fuel
identity. It is paired with the separately signed actual four-L loop

    e.L1 -> z.L3 -> A.L1 -> w.L1 -> e.R2.

Let beta=T1(z), gamma=T2(z). Additional exact clocks are

    T0(q)=beta+1, T1(u)=beta+2,
    T1(q)=gamma-3, T2(u)=gamma-2,
    T0(e)=gamma-1, T2(q)=gamma+1, T3(u)=gamma+2,
    gamma-beta>=8.

The final inequality is the same-cell u.L1-to-u.R2 spacing; it is not
an additive extra period payment.

## 4. Canonical births of J and the lower supplier Q

The other three corners of J cannot be its negative birth contact:
q.R0 and e.R0 choose J, while u.R0 chooses Q and u.L1(W) uses J's INPUT
before J's first output u.R2. At z, R0 chooses F and L1(W) uses J's
OUTPUT before J's first input z.R2. Thus z is the UNIQUE negative
first-port corner and

    B(J)=T1(z)=beta, parent(J)=F.                    (3)

u.R0 chooses Q, so B(Q)<=T0(u)-1. From T0(u)<=T1(u)-4=beta-2,

    B(Q)<=beta-3=B(J)-3.                            (4)

Both TOP corners of Q cannot birth Q. The upper-right corner u already
chooses Q at R0. At the upper-left a=(-2,-1), the E output edge into u
has exactly ONE occurrence, since u has exactly one E input. A negative
flat birth at a would emit E at BOTH L1 and R2, requiring at least TWO
occurrences. Hence it is impossible. The canonical parent of Q must be
one of its two BOTTOM max neighbors:

    parent(Q)=(-3,-3) or (-1,-3),
    B(parent(Q))<=B(J)-8.                            (5)

Both alternatives remain. They may connect to the same existing maximum
component; the proof neither iterates this local configuration nor
charges a distinct original root.

A useful subcase of the forward side follows from the SAME one-occurrence
birth test. If w=EWW (no L3), its single E input means that H=(-2,0)'s
upper-left corner (-2,1) cannot be its negative birth. Its two RIGHT
corners were already excluded by the signed successor theorem. Therefore
H is born at its lower-left corner and has parent (-3,-1), with
B(parent(H))<=B(G)-9. For w=EWWE both original LEFT parent alternatives
remain; this restriction must not be imported there.

## 5. A safe new output reservation

Let n_f count straight LEFT-max-branch faces of one chosen Gamma whose
entrance is the strict-fall alternative of section 1. Each has the
complete odd cell q=SNS in (1), so it leaves final BLACK output.
Distinct such faces give distinct q classes in the actual full-drift
quotient: q's two R headings are the SAME and determine the unique
oriented straight-face normalization and its associated F. Different
rotations cannot assign the same complete q history to different faces.

These q cells are disjoint from ALL selected first-L contacts, whose
two R headings are opposite. In particular they are disjoint from the
selected RLR entry cells reserved by the signed LEFT-L3 rise theorem.
If n_up is the number of those rises and N_odd is all odd complete cells,

    N_odd>=n_up+n_f.

Using the signed canonical turn identity, clockwise contractible excess
is at least ceil((n_up+n_f)/4). This is the SAME output production written
in the sheet register, not another charge. Constant-state branchful
modes may have n_up=n_f=0 and remain open. No initial black-input budget,
renewal obstruction or front exclusion follows.

## Dependencies and local control

K1_straight_branch_double_max_successor.md SHA
fdb4444ddd0593fdb361cc0e734fb408038339a1b40ddb9e986ff6362e60d8eb;
K1_straight_branch_predecessor_alternative.md SHA
a1f32674b55569559888acafd854403fa7e70b91e1da75ae9a196bc27228740b;
K1_right_L3_transport_and_odd_renewal_sources_v2.md SHA
6c107bd7ea9360b14afaa7a2de74bbd96745ad3880ac73ed23f246183496290e.

Local control: straight_branch_strict_fall_corner_closure.py/json.
It matches complete ports and exact finite difference constraints only;
its retained ten profiles are not claimed literal exterior connectors.
