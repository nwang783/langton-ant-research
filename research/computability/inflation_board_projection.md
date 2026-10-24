# Board projection and plaquette discrepancy at the remaining inflation scale

22 October 2026. Status: analytic proof and complete finite certificates independently
audited. Independent replay is in
`../audits/check_inflation_projection_independent.py` and its JSON. This does NOT exclude the
remaining adaptive inflation p(9n)=3p(n), h(9n)=h(n).

## 1. A simple block projection almost works

Work over F2. Partition fine cells into centered3-by-3 tiles

    T_q = 3q + {-1,0,1}^2,

and let P(B)(q) be the parity of black cells in T_q. For a north-entry
nine-letter image w, let V_w be its odd-read set: the board toggle made by
that macro. The complete previously audited image inventory has nine images
of R and nine of L. For14 of these18 images,

    P(V_w) = {0}.

For the other four, the error P(V_w) + {0} is exactly the four-corner boundary
of one unit coarse plaquette. Its lower-left corner is:

    RRLRRRRLR : (0,-1)
    RLRLLLLRL : (0,0)
    LRLRRRRLR : (-1,0)
    LLRLLLLRL : (-1,-1).

At other poses, rotate and translate these plaquettes. Centered tiles commute
with quarter rotations, so no tile convention changes are needed.

Thus, along ANY proposed adaptive inflation, the discrepancy

    D_n = P(B_(9n)) + B_n

satisfies D_(n+1)+D_n equal to either zero or one translated/rotated plaquette
boundary. In particular every row parity and every column parity of D_n is
constant. If H_n records modulo2 the selected exceptional plaquettes, then

    D_n = D_0 + boundary(H_n),

where boundary maps a unit plaquette to its four vertices. H_n has finite
support at every finite time. This is an auxiliary height-field formulation;
there is no proved sign, monotonicity, or boundedness of H_n.

The independently audited late-record pair is

    RRLRRRRLR RLRLLLLRL.

Its first plaquette has lower-left(0,-1). The second macro enters E at coarse
center(1,0), giving lower-left(1,-1). They do NOT cancel. Their sum is the
four corners of the2-by-1 rectangle:

    {(0,-1),(0,0),(2,-1),(2,0)}.

The actual block-parity toggle of the full18-letter word is
{(0,-1),(1,0),(2,-1),(2,0)}, versus {(0,0),(1,0)} for coarse RR.
Equal signed turn excess2 does not mean zero projection discrepancy.

## 2. No finite linear translation-covariant projection removes every error

There is no F2-linear map Q from finite fine boards to finite coarse boards,
commuting with translations by3 fine cells versus1 coarse cell, such that

    Q(V_w) = {0}

for every one of the18 north-entry images. In particular no fixed-radius
linear parity stencil can make ALL18 macro updates exactly one coarse flip.
The result already uses six image words. It does not assume rotation covariance.

Proof. Let r range over {-1,0,1}^2. Translation covariance means Q is specified
by nine finite Laurent polynomials K_r(X,Y), the images of the nine singleton
residue positions. Decompose each odd-read field as nine residue polynomials
V_(w,r)(X,Y). The required identities are

    sum_r V_(w,r) K_r = 1.

Evaluate X=Y=a in F4=F2[a]/(a^2+a+1); a is nonzero, so all Laurent monomials
are defined. Take the following weighted sum of six image identities:

    1       * RRRLRRLRL
    (a+1)   * RRLRRRRLR
    1       * RLRRLRRRR
    a       * LLLRLLRLR
    1       * RLLLLRLLR
    (a+1)   * LRRLRRLRL.

Direct odd-read enumeration gives zero for EACH of the nine weighted residue
coefficients on the left. The sum of the right sides is a+1, nonzero. This
is a contradiction. The exact nine-vectors and their zero sum are recorded
by the checker. No bound on the stencil radius is used. QED.

An affine projection has the same linear update differences, so adding a
fixed offset board does not repair this obstruction. A phase-dependent,
head-dependent, nonlinear, or restricted-palette projection is NOT excluded.
Nor does a projection obstruction prove that the underlying trajectories
are impossible.

## 3. A separate affine read-bit obstruction

Suppose one wants an affine parity expression in finitely many fine input
cells that returns the coarse R/L input bit for EVERY legal input of each
north-entry image. Any cell not read by some image is freely variable in
that image's input guard, so its coefficient must be zero. The common read
intersection of all18 images is only the origin. Both coarse R and coarse L
have legal images beginning with R, and both have images beginning with L.
Therefore no affine expression in the origin bit alone can return the coarse
bit for all18 guards. This does not rule out a nonlinear local computation:
ordinary simulation of nine steps can recover the image and its coarse turn.

## 4. Finite artifacts and limits

`probe_inflation_projection.py` regenerates all odd-read sets directly from
the complete image list, computes the F4 obstruction, and writes the witness.
`check_inflation_board_projection.py` verifies the14/4 split, the record-pair
rectangle, the six-image zero vector, and the read-set intersection.

These are exact finite certificates for the stated auxiliary algebra. They
supply no new finite-support counterexample, no universal exclusion at k9,
and no autonomous computer or halting reduction.
