# Every uniform finite-power spatial refinement is excluded

2026-10-23 05:16 UTC. Corollary of independently signed inputs JJ and
`causal_reduction/matrix_candidates/halfturn_matrix_dichotomy.md`, Section6.
The combined formulation independently passed analytic review at 05:18 UTC.

## Statement

Let phi be a fixed uniform substitution of length k>1 on absolute movement
directions E,N,W,S, with net(phi(v))=A v for an integer two-by-two matrix A.
Suppose A has finitely many distinct powers, equivalently a supplied identity
A^(mu+q)=A^mu with mu>=0 and q>=1. No growing rooted power-limit of phi is a
Langton-ant trajectory on ANY initial coloring.

The same conclusion holds for a finite decorated physical-state alphabet
whose refinement is geometrically coherent, has common spatial matrix A,
and whose unit-matrix case preserves the physical incoming and final poses
as in the signed primitive Perron theorem. It suffices to have the exact
nested footprint recurrence and the stated unit-scale pose condition; hidden
states do not defeat the uniform terminal-component proof.

No image-length bound, seed-mass bound, symmetry assumption or global
primitivity is required. Arbitrary changing directive sequences and general
nonuniform presentations are not covered.

## Proof

Pass first to the power defining the actual fixed rooted limit. Uniformity,
finite powers of A and exact geometry persist. Each refined root word is an
actual legal finite prefix if a realizing ant exists.

If A is invertible, cancel A^mu in the finite-power identity to get A^q=I.
For direction presentations apply the signed adjacent-pair theorem JJ. For
typed presentations take a spatial-order power and apply the signed unit-scale
typed terminal-SCC theorem. Both exclude legal growing rooted limits on any
background.

If A is singular, its eigenvalues are zero and the integer trace t. Finitely
many powers force t in {0,1,-1}. Cayley-Hamilton gives A²=t A.

For t=0 the entire depth-r footprint is contained in the fixed finite set of
sums b0+A b1, where the local offsets b_i range in one finite set. Its legal
prefix length k^r diverges, contradicting finite-domain escape.

For t=±1 all terms after the first in

    b0+A b1+...+A^(r-1)b_(r-1)

lie on im A and have bounded norm. Thus the depth-r footprint lies in a
fixed-width strip about im A with length O(r). The already signed singular
strip argument gives a polynomial upper bound on the duration of any legal
interval confined to this footprint: fixed-height rectangle escape for an
axis-parallel strip, or the strict bounded-weight oblique clock for an
oblique strip. This contradicts k^r.

For an infinite background, copy its colors on the finite footprint to a
finite otherwise-white board. The finite interval is unchanged, so these
escape bounds apply without assuming finite initial support. This is exactly
the already signed Section6 argument; no half-turn hypothesis enters it.

## Relation to the new realization decision theorem

The arbitrary-mass decision theorem JE/JF is NOT vacuous. It covers fixed
nonuniform growing presentations as well, where a terminal component may
consist only of identity letters and exponential root growth is not forced.
The present corollary says that its uniform finite-power input subclass
always returns  It does not decide arbitrary finite-seed ant behavior,
prove universal capture, or construct a finite universal simulation.
