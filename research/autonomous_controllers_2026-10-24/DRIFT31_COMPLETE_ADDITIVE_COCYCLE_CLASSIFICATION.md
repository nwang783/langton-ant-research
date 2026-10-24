# Complete universal additive cocycles on the full (3,1) quotient

24 October 2026. Analytic author result, submitted for independent review.
This classifies a specified invariant ansatz, NOT ant controllers. It supplies
an exact stopping point for the additive-count route into the remaining
middle-short family. No claim of novelty relative to literature is made.

## 1. Scope: no assumed spatial period

On the physical sector with vertical incoming headings at even T=3y-x and
horizontal incoming headings at odd T, let w and psi take values in Z/4.
Suppose they are invariant under full displacement (3,1) and obey, for EVERY
right and left move from EVERY permitted position/heading state,

    psi(after)-psi(before) = w(T)*sigma - rho*delta_y,

where sigma is +1 for R and -1 for L, and rho is any element of Z/4. Full
(3,1)-periodicity makes position-dependent functions exactly functions of T:
two integer lattice points have the same T iff their difference is an integer
multiple of (3,1). No period in T is assumed. No WHITE assumption or trajectory
legality is needed for this local kinematic identity.

Then ALL such cocycles are given by four arbitrary potentials x0,x1,x2,y0,
and rho, each in Z/4, by the recurrence below. Every solution automatically
has T-period12. There are 1024 potential/weight/coefficient solutions, and
256 distinct (w,rho) pairs after the constant potential gauge. The result is
not inferred from enumerating a preselected normal period.

## 2. Derivation on the entire infinite quotient

Write A_t for the potential at N when t is even and at E when t is odd.
Write B_t for the opposite heading potential. The four R/L moves at a
vertex give B_t-A_t=2w_t. At even t they further give

    w_t=A_(t-1)-A_t,       B_(t+1)=2A_t-A_(t-1).

At odd t they give

    w_t=A_t-A_(t+3)-rho,   B_(t-3)=2A_t-A_(t+3).

All equations are in Z/4. Put x_j=A_(2j) and y_j=A_(2j+1). Eliminating B gives

    x_(j+2)=x_(j-1)+2y_j-2y_(j-2),
    3y_j-2x_(j+2)-2rho=2x_j-y_(j-1).

Substitution yields

    y_j-y_(j-1)=2(x_j+x_(j-1)+rho).                 (1)

Apply (1) at j and j-1. Their sum says y_j-y_(j-2) is divisible by2,
so 2(y_j-y_(j-2))=0. The first eliminated equation therefore reduces to

    x_(j+2)=x_(j-1).                               (2)

Thus x has period3. Summing (1) over three consecutive j gives

    y_(j+3)-y_j=2rho,                              (3)

because every x in the period appears twice. Hence y has period6. This is
why T-period12 is FORCED, not imposed.

Conversely choose arbitrary x0,x1,x2,y0,rho. Extend x with period3, and extend
y in both directions using (1). Equations (2),(3) ensure this is consistent.
Define A_(2j)=x_j, A_(2j+1)=y_j, and use the displayed formulas for w and
B=A+2w. Direct substitution recovers all four move equations at every vertex.
This proves both necessity and sufficiency. Adding one constant to all four
initial potentials is exactly the kernel of the (potential -> weight) map:
if two solutions have the same w and rho, their potential difference is
constant along every allowed move, and the state graph is connected. The
finite table also directly checks that precisely four potentials occur for
each of the256 distinct weight/coefficient pairs.

An explicit useful parameter form is

    y1=y0+2(x1+x0+rho),     y2=y0+2(x2+x0),
    y3=y0+2rho,            y4=y1+2rho,    y5=y2+2rho.

The first six weights, and the others by w_(t+6)=w_t+2rho, are

    w0=y0+x0+2x2+2rho,
    w1=y0-x2-rho,
    w2=y0-x1,
    w3=y0+x0+2x1+rho,
    w4=y0+2x0+2x1-x2+2rho,
    w5=y0+2x0-x1+2x2-rho.

## 3. Exact effect on the live FULL odd inventory

For a complete WHITE full drift (3,1) front, stable class histories alternate
R,L beginning R. Summing the cocycle through one full event period therefore
gives the necessary relation sum_(T in O) w_T=rho, where O is the FULL odd
inventory. This reduction does not discard even-read classes: their signed
contribution is exactly zero. A BLACK-first odd class would contribute -w_T,
so the conclusion is not valid for prepared-input waves without that correction.

For the independently signed middle-short branch, complete ownership gives

    O={0,1,2,6,7,6c+1,6a+2,6a+4},     2<=c<=a.

Using the six weight formulas, including w_(t+6)=w_t+2rho, yields exactly

    sum_(T in O) w_T = 3rho+2rho*c,
    sum_(T in O) w_T-rho = 2rho*(c+1).               (4)

Every x and y0 parameter cancels; the a terms cancel too. Thus even c fails
whenever rho is odd, while odd c passes EVERY cocycle in the stated family.
The existing signed mod-four law is therefore the full obstruction from all
universal position/signed-turn Z/4 cocycles, including those with no assumed
spatial period. The live range remains c odd and3<=c<=a. Passing these laws
is NOT evidence of complete chronological realizability or a controller.

The signed modulus-limit note f55830ec independently rules out a larger
modulus with a UNIT winding coefficient within this same universal ansatz.
It does not classify chronological or nonlinear invariants. Neither note
rules out a transfer retaining rank permutations, clock spans, additional
multiplicity terms, or the complete evolving board.

## 4. Checkable artifacts and scope boundary

`certify_drift31_complete_additive_cocycles.py` reconstructs all1024 parameter
solutions, checks all49152 local transitions, verifies both derived parity
cases for a and c, and checks the local modular elimination without division.
`drift31_complete_additive_cocycles_certificate.json` stores all potentials
and weights. The infinite-quotient completeness proof is Section2, not a
bounded sample or an opaque linear-system solver.

The retained count-only12-level cycle adding296 reads is NOT used anywhere
here. Its first step is already incompatible with the actual lower-prefix
ordinal return. Counts, stream heights and residue cycles do not by themselves
supply a legal transfer loop. Actual chain pairing, rank chronology and
unbounded canonical clock spans remain the missing state for a stronger
invariant. No such state has been proved finite, bounded or unreachable.
