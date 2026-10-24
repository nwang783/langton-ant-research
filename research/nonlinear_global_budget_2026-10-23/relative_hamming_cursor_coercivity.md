# Finite-cap Hamming discrepancy controls the cursor, even on infinite backgrounds

23 October2026. New relative-state corollary of the retained exact axial
charges, submitted for independent review. Not a bound on that discrepancy
and not a global defect budget.

## 1. Statement

Let two ACTUAL standard Langton ants A and R start at the SAME physical pose
(p0,h0), on boards

    B_A(0)=Q XOR C,       B_R(0)=Q,

where C is a finite set of changed cells. Q may be arbitrary and INFINITE.
For any respective finite times t,s, let

    E_(t,s)=B_A(t) XOR B_R(s),
    m(p,h)=p-d_h/2.

The board XOR E_(t,s) is finite because both paths have made finitely many
updates. Then

    2||m(A_t)-m(R_s)||_infinity <= |C|+|E_(t,s)|.       (1)

In particular, for the transverse coordinate u=x-y,

    |u(p_A(t))-u(p_R(s))| <= |C|+|E_(t,s)|+1.         (2)

The two clocks t,s need not agree. The comparison preserves COMPLETE boards;
E cannot be replaced by a cropped cap window, a subset of roots, or a ledger
which has silently discarded old wake cells.

## 2. Retained exact charges and the relative proof

Dependency: ../continuation_2026-10-22/ant_continuation2/chronology/
axial_separator_proof.md Sections2-4. For each row r, its checker-signed black
sum minus its heading/side correction G_r is conserved modulo4. Columns have
the analogous F_c. The two ants have the same physical sector because they
start at the same pose. Thus the SAME correction tables apply to both paths.

First suppose Q finite. Let D_r(t,s) be the difference of their current signed
black sums on row r, and let c_r be the corresponding initial difference.
Subtracting their two conserved charges, with identical initial pose terms,
gives

    G_r(A_t)-G_r(R_s) = D_r(t,s)-c_r  modulo4.

Write delta4(z) for the distance of z modulo4 from zero. Every changed cell
contributes at most one to the absolute signed-sum difference. Hence

    delta4(G_r(A_t)-G_r(R_s))
      <= |E_(t,s) intersection row_r| + |C intersection row_r|.

Sum over all rows. The retained exact heading-corrected line calculation gives

    2|m_y(A_t)-m_y(R_s)|
      <= sum_r delta4(G_r(A_t)-G_r(R_s))
      <= |E_(t,s)|+|C|.

The same column argument bounds twice the x-midpoint difference. Taking their
maximum proves(1). This is a comparison of two different trajectories, not
an unjustified application of the same-orbit endpoint theorem.

For infinite Q, choose a finite board Q' agreeing with Q on C and on every
cell read by EITHER of the two finite paths. Initialize Q' and Q' XOR C at
the same initial pose. First-difference induction preserves both complete
finite read histories. Outside their finite read union and C, the two boards
agree with each other at both ends. Consequently the current XOR remains
EXACTLY E_(t,s), and the initial XOR remains exactly C. The finite proof
therefore transfers with no divergent infinite row sums or extra hypothesis.

Finally |u(v)|<=2||v||_infinity, while the heading correction changes u by at
most one between two unit headings. Applying this to(1) proves(2).

## 3. A genuine read-hull consequence for prepared standard scattering

Suppose the reference R is a clean standard104 front whose entire transverse
read/pose band lies in I=[a,b]. At a reaction time t define its distance from
the full comparison orbit by

    D(t)=min_{s>=0}|B_A(t) XOR B_R(s)|.

This minimum exists: all values are finite nonnegative integers, so the
nonempty set of values has a least attained element. No efficient minimizer
or uniform bound is assumed. Equation(2) yields

    distance(u(p_A(t)),I) <= |C|+D(t)+1.              (3)

Thus if a separate physical argument bounds D(t)<=M throughout a finite
collision, ALL reaction reads stay in the explicit transverse halo

    [a-|C|-M-1, b+|C|+M+1].                           (4)

This bounds arbitrary-cap read hulls without imposing a time bound, a bound
on the background's infinite black mass, or an a priori finite spatial box.
It is stronger than assuming a read halo directly, but it still needs an
actual bound on the COMPLETE renormalized Hamming defect ledger.

## 4. The widening control forces this ledger to grow

In the independently checked phase72 fourteen-cell control, compare the
actual ant with the unperturbed pristine standard ant. Their initial cap XOR
has |C|=1. The reference stays in[-28,-18]. The actual collision visits u=56,
74 levels beyond that reference band, so(3) forces

    D(t)>=72

at that record. This is true even after choosing the BEST longitudinal phase
and depth of the entire clean reference orbit. Thus the very small initial
cap does not keep the renormalized discrepancy small.

No inference from D(t) to actual K count is supplied. D(t) may contain long
zero-K wake strings, and changing the comparison background to absorb them
requires carrying the matching physical cursor and charge information.
The useful missing premise is an honest nonlinear discrepancy budget or
an amortized outboard-read budget, not just local cap connectedness.
