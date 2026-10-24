# Exact local statistics cannot rank adjacent-defect renewal

Status: the analytic histogram argument passed independent review on2026-10-22 at21:13 UTC. This proof uses one actual physical orbit, so it closes the conserved-charge-fiber loophole of the earlier paired-path argument. It is a no-go theorem for a specified observable class, not a counterexample to highway capture.

## Statement

Fix any finite radius R. On a finite black board B, let H_R(B) be the multiset of all nonempty translated binary square patches of radius R. The infinitely repeated empty patch is omitted. Let P_R(B,p) be the radius-R board patch centered at the ant, expressed relative to p.

There is no strictly decreasing adjacent-K renewal rank of the form

    rho(B,p,h) = Phi(H_R(B), P_R(B,p), h; conserved parameters),

even if Phi is arbitrary and nonlinear, the rank is real-valued rather than natural-valued, and the function is separately selected using the full invariant charge data. The obstruction occurs at two endpoints on the SAME actual orbit with identical displayed observables. A finite collection of finite-range pattern histograms is a special case by increasing R.

This does not exclude an observable retaining the locations of distant patches relative to the head, or a genuinely nonlocal oriented rank. In particular, a count of black cells in an unbounded head-relative half-plane is outside this theorem.

## One rail traversal

Choose n>=1 and M>=12 with M>4R. Set

    B0 = {(0,y): -M<=y<0} union {(1,y): 0<=y<2n+M},
    X  = (B0,(0,0),N).

The exact word S^n, S=RLLR, is feasible. Each S period moves the head by(0,2) and transfers two black cells from column1 to column0. Therefore its endpoint is

    B1 = {(0,y): -M<=y<2n} union {(1,y): 2n<=y<2n+M},
    Y  = (B1,(0,2n),N).

All4n steps are immediate K renewals. The four cyclic ten-factors of S are all absent from the84 standard ten-factors. At the starting cut, the lower left rail is exactly the result of earlier S periods. The ten-step inverse history remains within10 lattice units of the seam, so M>=12 makes it identical to the bi-infinite rail history. The same holds at every subsequent checkpoint; alternatively, after the first ten reads the entire needed history is inside the displayed path. Thus this claim uses the TRUE inverse history, not an assigned symbolic prehistory.

## Exact feature decomposition of the histogram

For a patch center with vertical coordinate y, the radius-R patch can meet a transition across row b only if

    b-R <= y <= b+R-1.

The three transitions are the bottom endpoint b=-M, the moving seam b=0 initially or b=2n finally, and the top endpoint b=2n+M. Their bands are disjoint because each intervening segment has length at least M>4R. Partition the nonempty patch centers into these three bands and the straight-column bulk between them.

- The bottom endpoint band is identical on both boards, at identical coordinates.
- The top endpoint band is identical on both boards, at identical coordinates.
- The seam band in B1 is exactly the seam band in B0 translated by(0,2n).
- Between the bands, every patch sees only a complete vertical line of black cells. The column0 bulk length increases by2n, and the column1 bulk length decreases by2n. For each bulk row, the complete multiset of nonempty patches centered across the line is independent of the line's horizontal location: translating all centers by one translates the line and leaves every relative binary pattern unchanged.

The bulk changes therefore cancel exactly, proving H_R(B0)=H_R(B1). Near the ant, both boards show column0 black below the seam and column1 black at and above it, so P_R(B0,(0,0))=P_R(B1,(0,2n)). The heading is N at both ends.

Because Y is reached from X physically, every conserved parameter agrees. Yet strict rank descent at every immediate renewal would imply rho(X)>rho(Y), while the proposed observable representation gives equality. This contradiction needs no lower bound on individual rank decrements.

## Two additional nonlocal observable classes

The same pair also has exactly the same multiset of entire4-neighbor black connected components, each recorded up to translation: two vertical segments of lengths M and M+2n. Thus replacing H_R by this possibly unbounded-range component-shape inventory, or augmenting H_R by it, does not help when the head information remains radius-R local.

Moreover, B1 is the half-turn image of B0 under

    (x,y) -> (1-x,2n-1-y).

Consequently any collection of arbitrary board functionals invariant under translations and half-turns also agrees. Coupling such global unrooted board functionals to a fixed-radius head patch cannot produce a strict renewal rank either. These two extra conclusions are algebraic corollaries of the explicit boards; they do not assert that every possible long-range observable fails.

## Reproduction

check_local_histogram_rank.py independently enumerates the nonempty patch histograms, entire black component shapes, half-turn identity, exact physical trajectory, and true inverse-history K tests for35 cases with R=0..6 and n in{1,2,5,13,30}. The all-n proof is the feature decomposition above, not the finite controls.
