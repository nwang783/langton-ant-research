# Exact path hulls and the cost of erasing a standard wake

Date: 21 October 2026

Status: analytic deductions with finite implementation checks. These results do
not prove the finite-seed highway conjecture. No claim of priority is made.
The hull argument extends the corner argument in Etse, Proposition 2. The
clock argument uses critical components of Hao Ke's clock construction.

## 1 Model

A complete state is X=(B,p,h), where B is the entire finite black set and h is
N,E,S,W, encoded 0,1,2,3. White turns right; black turns left. The read cell
flips, and then the head moves one unit. Write X_j=(B_j,p_j,h_j).

## 2 The endpoint field fixes the entire path hull

**Theorem 1.** For any integers s<t, put

    P={p_s,p_(s+1),...,p_t},       Delta=B_s symmetric_difference B_t.

Then

    conv(P)=conv(Delta union {p_s,p_t}).                    (1)

This is the ordinary Euclidean convex hull, including degenerate hulls.
The theorem uses the actual complete endpoint fields. It does not remove
old black cells or assume that the path stays inside a chosen strip.

**Proof.** Delta is the set of cells read an odd number of times. Hence Delta
is a subset of P. It suffices to show that every vertex v of conv(P), other
than p_s and p_t, belongs to Delta.

At a vertex of a finite convex hull, the neighbors in P cannot contain two
opposite grid neighbors. Such a pair would have v as its midpoint, so v would
not be an extreme point. Therefore there are at most two neighbors in P.
If there are two, they are perpendicular. Because v is neither endpoint,
every occurrence of v has both a preceding and a following path position.
Thus both neighbors must be present and used.

The fixed horizontal/vertical arrival partition of the ant makes one of the
two neighbors the only possible predecessor and the other the only possible
successor. Every visit would therefore require the same turn. The read color
flips after each visit, so a second visit would require the opposite turn.
No second visit is possible. Thus v is read exactly once and lies in Delta.
This proves (1). The same argument covers a line segment or a singleton hull.

**Corollary 1.1.** At every time t,

    conv(B_0 union B_t union {p_0,p_t})
      = conv(B_0 union {p_0,...,p_t}).                     (2)

The left side is therefore a monotone growing hull. This follows from (1)
and B_0 union B_t = B_0 union (B_0 symmetric_difference B_t).

**Corollary 1.2.** If every changed cell and both endpoint head positions lie
in a convex set C, the whole intervening path lies in C. In particular,
temporary trips outside a strip cannot be hidden by restoring all cells
outside that strip before the endpoint.

Equation (1) does not prove that the hull has bounded width or finitely many
changes. A later hull can contain an earlier large polygon while having only
a few new extreme points. This prevents a direct bound on black mass from
the number of previous hull vertices.

## 3 Two separately monotone diagonal clocks

Put chi(q)=(-1)^(q_x+q_y) and

    sigma=chi(p) for vertical headings, and -chi(p) otherwise.

The value sigma is invariant. First use z(q)=q_x+q_y and define e=+1 for N,E,
e=-1 for S,W. Define two rational quantities on the complete state:

    Psi_plus(X) = -sigma sum_(q in B) chi(q) 3^z(q)
                   + a(e) 3^z(p),
    Psi_minus(X)= -sigma sum_(q in B) chi(q) 3^(-z(q))
                   + a(-e) 3^(-z(p)),

where a(+1)=1/2 and a(-1)=-3/2. Direct substitution in the eight local
heading/color cases gives

    Psi_plus(FX)-Psi_plus(X)
        =4*3^z(p)       if (e,e')=(-1,+1), and 0 otherwise;
    Psi_minus(FX)-Psi_minus(X)
        =4*3^(-z(p))    if (e,e')=(+1,-1), and 0 otherwise. (3)

These quantities are separately nondecreasing. They need not be positive.
One alone need not increase at every step.

For the normal coordinate z=x-y, use -sigma in place of sigma and use
e=+1 for E,S and e=-1 for W,N. This is exactly a quarter-turn change of
coordinates. A shift z -> z-c multiplies Psi_plus by 3^(-c) and Psi_minus
by 3^c. Thus their product is independent of the choice of normal origin.

These are the one-sided critical components of Ke's clock family. The
integer clock in clock_escape/PROOF.md can also be used to derive them by
putting its centre far to either side and taking a scaled limit. Equation
(3), rather than a limiting argument, is enough for the deductions here.

## 4 A mass and width bound for every later state

**Theorem 2.** Fix either diagonal and a complete state X. Suppose that

    A=Psi_plus(X)>0,       C=Psi_minus(X)>0.

At every later state Y, let K=|B(Y)| be the COMPLETE black mass, and let

    m=min z(B(Y) union {p(Y)}),
    M=max z(B(Y) union {p(Y)}),       W=M-m.

Then

    (K+1/2)^2 * 3^W >= A*C.                              (4)

There is no assumption on the intervening path or on its width.

**Proof.** Monotonicity gives Psi_plus(Y)>=A and Psi_minus(Y)>=C.
Each positive field summand is at most 3^M in Psi_plus. A negative field
summand only reduces its value. The head term is at most 3^M/2, even when
its actual coefficient is -3/2. Hence

    A <= Psi_plus(Y) <= (K+1/2) 3^M.

Similarly C <= (K+1/2)3^(-m). Multiply the two inequalities to obtain (4).

The two separate bounds also locate the support:

    M >= log_3(A/(K+1/2)),
    m <= -log_3(C/(K+1/2)).                              (5)

Both endpoints refer to the current full black field plus the head.
Consequently a low-mass state must have support on both required sides;
a temporary excursion which leaves no such endpoint support cannot pay
the clock cost.

### A sharper version

Set a=3^(W/2). Center the clocks at (M+m)/2; a real centre is allowed because
this only rescales (3) by positive constants. Each positive field coefficient
in their sum is at most a+a^(-1). Their summed head correction is at most
a/2-3/(2a). The arithmetic-geometric mean inequality applied to the two
positive lower bounds therefore gives

    2 sqrt(A*C) <= (K+1/2)a + (K-3/2)/a.                 (6)

This is a stronger bound than (4), but (4) has a simpler statement.

## 5 Standard highway transport has a permanent cost

Suppose a complete trajectory executes n consecutive full periods of the
standard highway, from a fixed state X_0. Choose the diagonal normal to
the highway drift. Each period repeats the same normal coordinates and
heading changes. Therefore (3) adds the same positive constants alpha,beta
on every period:

    Psi_plus(X_n) = Psi_plus(X_0)+n*alpha,
    Psi_minus(X_n)= Psi_minus(X_0)+n*beta.                (7)

Positivity of alpha and beta follows because the normal coordinate returns
to its start and takes both upward and downward steps. Its step sign must
therefore change in both directions during a complete period.

At every later state, even after arbitrary nonstandard behavior and trips
outside the original band, Theorem 2 applies with

    A_n=Psi_plus(X_0)+n*alpha,
    C_n=Psi_minus(X_0)+n*beta,

provided both are positive. Thus

    (K+1/2)^2 * 3^W >= A_n*C_n.                         (8)

For a fixed width W, complete black mass at a later state is at least
sqrt(A_n*C_n)*3^(-W/2)-1/2. In particular it grows at least linearly with n.
For a fixed black-mass bound K, the width is at least

    2 log_3(n) - O(1),

where the constant depends on X_0 and K. Equation (5) shows that both
transverse sides must be represented. Equation (6) improves the constant.

This strengthens a fixed-strip erasure claim: the path itself need not stay
in that strip. It is enough to measure the COMPLETE endpoint state. If an
eraser avoids this bound by placing black cells far outside the strip, those
cells are part of its permanent endpoint cost and cannot be omitted.

It remains possible under (8) for a proposed counterexample to retain more
black cells, to retain larger transverse width, or both. No finite bound on
such growth has been proved. Thus (8) is an obstruction to specified erasure
schemes, not a proof that every old wake eventually becomes inactive.

## 6 Exact standard constants

For the known four-cell port

    B={(0,-1),(1,1),(1,3),(2,2)}, p=(0,0), h=E,

the state at time 182 has 36 black cells and pose ((5,1),E). Its standard
period has drift (2,2). Use the centered normal z=x-y-2. Literal exact
calculation gives

    Psi_plus(X_0) = 91105/162,
    Psi_minus(X_0)= 99149/162,
    alpha = 103364/243,
    beta  = 105524/243.                                 (9)

The standard mass gain is 12 per period. The normal span of this full port
state and its following full-period states is 10. The exact word is recorded
in check_results.json.

The phase calculation in (9) is a finite exact check. It does not by itself
prove the infinite standard tail; that known tail is separately certified in
Ke's four_cell_port/PROOF.md. For applying (7) to any actually executed
standard period block, the local identity (3) and its finite phase data suffice.

For this particular port orbit, A_n and C_n are positive for every n>=0.
Since sqrt(alpha*beta)=sqrt(10907382736)/243, which is about 429.788, (8)
has a concrete leading constant. Its numerical size depends on the units
of the exponential clock; it is not a rate of black-cell growth by itself.

## 7 Checks and source boundaries

Run:

    python3 check.py

The program uses exact rational arithmetic for (3). It checks 40,000 local
clock cases on 50 seeded trajectories and 5,000 random finite segment hull
identities. It also calculates the port period data in (9). These are checks
of the implementation, not replacements for the universal proofs above.

Primary sources inspected:

- K. R. Etse, How Long Can the Escaping Ant Be Confined?, Proposition 2,
  https://arxiv.org/html/2606.26677v1 ; published as MFCS 2026 article 49,
  https://doi.org/10.4230/LIPIcs.MFCS.2026.49 .
- H. Ke, clock_escape/PROOF.md, critical proof and manuscript,
  https://github.com/kehao95/langtons-ant-core/blob/main/clock_escape/PROOF.md
  and https://github.com/kehao95/langtons-ant-core/blob/main/clock_escape/evidence/critical/proof.md .
- H. Ke, four_cell_port/PROOF.md,
  https://github.com/kehao95/langtons-ant-core/blob/main/four_cell_port/PROOF.md .

The GitHub file blob SHA values returned on this run were
`a31945aed3504dc618f55a01b73c60cf6e68207f` for clock_escape/PROOF.md,
`18dcee4783f9c3fb7b0361a71b5ae45e1ad2403f` for the critical proof, and
`b7e9eca7a307c9588529c52d3111bb62f170d1c4` for four_cell_port/PROOF.md.

The exact whole-field reset idea was discarded after checking Etse:
Proposition 2 already rules out any repeated coloring at distinct times.
Its corner proof, rather than a weaker clock-only pose restriction, is the
appropriate starting point for Theorem 1.

## 8 Why four directional clocks do not finish the proof

There is a simple obstruction to an endpoint-only argument using these
clock inequalities. Fix sigma. Put a 2-by-2 black block at a lower-left
cell q whose checkerboard sign is -sigma. Its contribution to each of the
four one-sided clocks is positive. For z=x+y the two contributions are

    4*3^z(q),          (4/9)*3^(-z(q)).

For u=x-y the two contributions are

    (4/3)*3^u(q),      (4/3)*3^(-u(q)).

This follows by factoring the alternating four-cell sum. Each such block
also has even black parity in every row and column. Four appropriately
placed blocks near the corners of an expanding square have only 16 black
cells. Their hull can contain any fixed old path hull, and all four clock
values can be made arbitrarily large.

These are algebraically allowed endpoint candidates. They are NOT asserted
to be dynamically reachable from one fixed seed. In particular they do not
give a counterexample, a repeatable circuit, or an infinite sequence of
low-mass states on one orbit. They show why monotone clocks, row/column
parity and the hull identity alone do not supply the needed conclusion.
Actual reachability or a new restriction on how such endpoint support can
be created must still be controlled.
