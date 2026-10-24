# A transverse clock obstruction to erasing a standard wake

## Status and source

This is a consequence of Ke's integer clock, not a new construction of the
clock. The source is the pinned analytic proof:

https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/clock_escape/PROOF.md

The result excludes a clean periodic eraser of the standard wake in the
same invariant sector as the ant which wrote it. It also gives a linear
residue bound when final black cells lie in a fixed transverse strip.
Neither statement bounds transverse spread in an arbitrary trajectory.
Thus it does not prove pointwise mass divergence or highway capture.

 The companion
`check_transverse_clock_residue.py` checks the coefficient by direct
integer arithmetic and an independent literal replay of the 104 moves.
The symbolic argument does not depend on the particular coefficient.

## 1. The transverse clock

Use headings N,E,S,W=0,1,2,3, white-right / black-left, then flip and move.
Let

    chi(x,y)=(-1)^(x+y),
    sigma=chi(p) for a vertical heading,
          -chi(p) for a horizontal heading.

Sigma is constant on an orbit. Put ell(x,y)=x-y and

    eta(h)=+1 for E,S, and -1 for W,N,
    f(z)=3^abs(z)-1,
    J(z,e)=f(z)/2 if e*z>=0, and -3*f(z)/2 otherwise.

The rotated version of the source clock is

    Theta_c(B,p,h)
      = sigma * sum_(q in B) chi(q)*f(ell(q)-c)
        + J(ell(p)-c,eta(h)).

For a right or left update, sigma is unchanged and

    Theta_c(FX)-Theta_c(X)
      = 1+4*f(ell(p)-c)*1[eta'!=eta and eta*(ell(p)-c)<0]
      >=1.

This follows by a 90-degree rotation of the source formula: the rotation
changes its x+y coordinate to x-y and changes sigma to -sigma. In
particular, the field coefficient for this orientation is +sigma, not
-sigma. This sign matters to the eraser argument.

Fix sigma and c and write

    w_c(q)=sigma*chi(q)*f(ell(q)-c),
    A_c(B)=sum_(q in B) w_c(q).

Translations u with ell(u)=0 and even u_x+u_y leave these weights unchanged.
They also leave the head correction unchanged when the heading repeats.

Although the displayed clock is defined for a complete finite black set,
its change over a finite sequence makes sense on any board: sum only over
the finitely many changed cells. The same one-step identity then telescopes.
This observation permits the periodic-interface formulation in Section 4;
it does not assign a finite total clock to an infinite prepared wake.

## 2. A period of a genuine standard highway has positive transverse weight

Let S be a finite active seed, let d be the standard displacement, and
suppose one standard period of P updates gives

    B_after=(S+d) disjoint_union D,
    p_after=p_before+d,
    h_after=h_before.

Here D is the finite deposit of permanently black cells for that repeat.
Choose the diagonal coordinate transverse to d. The canonical orientation
used below has d=(-2,-2), so ell=x-y. Both the active seed's field weight
and the head correction are invariant under d. Therefore

    W_c := A_c(D)
         = Theta_c(X_after)-Theta_c(X_before)
         >=P>0.

The positivity is an analytic consequence of the clock. It is not an
assumption based on the number of black cells in D, whose coefficients
have both signs.

The same proof works for any finite-support periodic highway admitting
such a disjoint active-seed and permanent-deposit representation. The
restriction below concerns the exact deposit and the same sigma sector.

### Canonical numerical value

For the retained 13-cell seed, P=104, h=W, d=(-2,-2), sigma=-1. Its deposit is

    D={(-4,-1),(-3,-1),(-3,0),(-2,-1),
       (-1,-8),(-1,-7),(-1,-6),(-1,-2),
       (0,-7),(0,-3),(0,-2),(0,0)}.

Its transverse levels x-y run from -3 through 7. At center c=2,

    W_2=856,
    A_2(S)=-142,
    J(ell(0,0)-2,eta(W))=4,
    Theta_2(S,0,W)=-138.

The 104 individual gains have the following exact inventory:

| Gain | Number of updates |
|---:|---:|
| 1 | 88 |
| 9 | 8 |
| 33 | 2 |
| 105 | 6 |

Their sum is 856. The next section can instead be read with symbolic
W_c>=104 if a numerical control is not desired.

## 3. A finite wake cannot return to small mass inside a fixed strip

First consider the canonical state after n periods. Let X_n be the full
finite state produced from S. Its head is n*d with heading W, and its board is

    B_n=(S+n*d) disjoint_union union_(k=0)^(n-1)(D+k*d).

The disjointness and the standard repetition are properties of the
retained standard seed. Consequently

    |B_n|=13+12n,
    Theta_2(X_n)=-138+856n.

Suppose that from X_n an actual trajectory reaches Y=(B,p,h) after T>=0
updates. Write K=|B| and suppose

    |ell(q)-2|<=R_B for every q in B,
    |ell(p)-2|<=R_h.

The clock gives the exact lower constraint

    K*(3^R_B-1) + (3^R_h-1)/2 >= 856n-138+T.       (1)

Indeed, every field coefficient is at most 3^R_B-1 in absolute value,
and J is at most (3^R_h-1)/2. These are upper bounds on the final clock,
whereas its actual value must be at least its initial value plus T.

If the final head and all final black cells lie in the same fixed strip
|ell-2|<=R, this becomes

    (K+1/2)*(3^R-1) >= 856n-138+T.                 (2)

For fixed R it forces K to grow at least linearly with n. The intermediate
path need not have stayed in that strip: only the complete final board and
head are restricted in (1) and (2).

For example, R=5 contains the canonical wake's levels -3,...,7. Since
3^5-1=242, any endpoint contained in that strip satisfies

    K >= ceil((856n+T-259)/242).

If the final pose has ell(p)=0 and h=W, its head correction is exactly 4,
so the sharper endpoint constraint is

    K*(3^R_B-1) >= 856n-142+T.

Conversely, for a proposed return with K bounded and both head and board
inside radius R, (2) forces at least logarithmic transverse spread:

    R >= log_3(1+(856n-138+T)/(K+1/2))

whenever the expression on the right is defined and positive. The integer
radius must satisfy the corresponding ceiling. This is a necessary
condition, not a way to realize such a return.

### An arbitrary fixed front or controller

The unmodified canonical state simply continues along its standard
highway. The endpoint estimate is also useful when a different fixed
front or controller is installed. More generally, suppose a family of
initial states consists of n disjoint input deposit periods, a fixed
finite cap translated by n*d, a pose translated by n*d, and an optional
fixed finite base pattern. Require the same sigma sector and an exact
disjoint decomposition of these field portions. Then

    Theta_c(X_n)=n*W_c+C,

where C is independent of n. The cap and pose can be arbitrary; they need
not reproduce the standard word. For any actual T-step endpoint, the
corresponding necessary inequality is

    K*(3^R_B-1)+(3^R_h-1)/2 >= n*W_c+C+T.         (1')

Thus a fixed-size controller of fixed transverse extent changes only the
constant. The proof does not assume that the subsequent return follows a
standard or reversed-standard word. For nondisjoint descriptions one
must compute the exact initial signed field sum instead of adding terms
as though their cells were distinct.

### Fixed old cells

A retained exterior set E can be added to both endpoints provided it is
disjoint from the displayed varying portions. Its field contribution
cancels exactly. The same argument then bounds the varying endpoint
residue. If some old cells are changed, their contributions must instead
be included in the endpoint difference. They cannot be discarded merely
because they are far from the ant.

## 4. No same-sector clean periodic eraser

Here is a formulation that does not assume a reverse standard turn word.
Consider a proposed periodic interface on an already prepared standard
wake. Suppose that during one repeat of P_E>0 updates:

1. the head translates by u=-k*d, for an integer k>=1, and returns to the
   same heading;
2. its invariant sigma equals the sigma of the standard trajectory that
   deposited this wake;
3. the finite active cap is translated by u, so its signed field change
   has zero transverse weight;
4. the permanent field change removes exactly k standard deposit periods,
   up to translations along d, and writes no permanent output residue.

These statements can equivalently be expressed as an equality of finite
signed field differences. The active cap need not use a standard word or
have the standard width. What matters is its exact translated repetition
and the asserted complete removal of the input deposit.

The head correction and translated cap cancel in the transverse clock.
The remaining clock change is

    -k*W_c < 0.

The local gain identity, summed over the actual P_E updates, requires a
change of at least P_E>0. This is a contradiction.

Therefore no such same-sector clean periodic eraser exists, at any period
length or active-cap width. The proof applies to any putative turn word
satisfying the hypotheses, not just a spatially shifted time reversal of
the standard word.

### General output residue balance

If the proposed interface instead writes a finite output deposit E in
each repeat, the same calculation gives

    A_c(E) - k*W_c >= P_E.                        (3)

In particular, if all output cells satisfy |ell-c|<=R, then

    |E|*(3^R-1) >= k*W_c+P_E.                    (4)

It must leave a positive number of black cells per repeat. At any fixed
output width the amount has a linear lower bound in the number k of input
periods consumed.

Equation (3) is a weighted condition. It need not force |E|>=12k if the
output has a different transverse shape. It also does not prohibit later
interactions with the output wake. No irreversible freezing of E is
assumed outside the stated periodic-interface model.

## 5. The sector qualification is essential

The literal time reversal of a genuine forward wake-writing trajectory
exists in the reversed invariant sector. Under the corresponding
reversor, sigma changes sign. The field weights in the clock therefore
change sign as well. Removing the original deposit then contributes
+k*W_c to the reversed-sector clock, which is compatible with strict
increase. There is no contradiction with reversibility.

The same-sector obstruction is stronger than the observation that literal
edge retracing is unavailable. It excludes any clean periodic erasing
word with the stated input/output balance. It does not classify aperiodic
fronts or trajectories that move the residual information outside every
fixed transverse strip.

## 6. The remaining global gap

Weights grow exponentially with transverse distance. A bounded number of
black cells at sufficiently large transverse levels can carry a large
positive endpoint clock value. Thus the clock cannot replace a proof that
the old information remains within a bounded transverse region, or a
different argument that charges the physical transport needed to export it.

The four-corner states in the earlier endpoint example exhibit this
algebraic possibility for both diagonal clocks. The separate exact family
check shows those particular states do not regenerate under the ant rule;
it does not exclude all possible arrangements that export clock weight.

This targeted attempt therefore closes one precise eraser mechanism and
quantifies one necessary cost of a low-mass return. It leaves the actual
chronology of unbounded transverse export unresolved.
