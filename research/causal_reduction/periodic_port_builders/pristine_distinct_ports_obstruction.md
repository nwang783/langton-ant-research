# Pristine distinct-port cycles cannot initialize the half-turn builder

Status: elementary analytic derivation; independent review requested. This is an initialization obstruction, not a general renewable-builder exclusion.

## Scope

Consider a controlled right-half-plane process on x>=0, initially all white. Its prescribed entry poses are (0,r_j,E) and exit poses (-1,s_j,W), with indices modulo an odd q>=3. Assume the q entry rows are pairwise distinct and all have the same parity. The parity assumption holds automatically for one fixed physical ant sector. External resets may move the head between excursions but do not change right-half-plane cells.

Assume these ports satisfy the half-turn self-gluing equations with a constant phase offset. For a minimal injective entry cycle, that offset is delta=(q+1)/2 modulo q, and there is one integer S such that

    s_j = S-r_(j+delta).

These are necessary gluing equations only. The theorem does not presume a completed autonomous construction.

## Theorem

At most (q-1)/2 prescribed excursions can complete from the pristine right half-plane before one requested exit fails. A vertical strip restriction can only make failure earlier.

## Proof

The first excursion from an unread entry row r is exactly RR. It reads (0,r) and (0,r-1), writes both black, and exits at (-1,r-1,W). Pairwise distinct same-parity rows give disjoint two-cell pairs. Consequently, throughout the first q attempted entries, each excursion is again RR, irrespective of the earlier RR excursions. Its actual exit row is r_j-1.

For a prescribed exit to agree, it is necessary that

    r_j+r_(j+delta)=S+1.

Write q=2k+1, so delta=k+1. If phases0 through k all succeeded, the equations at phase0 and phase k would give

    r_0+r_(k+1)=S+1,
    r_k+r_0=S+1.

Thus r_k=r_(k+1), contradicting distinctness. At most k excursions therefore complete.

## Sharpness

For every k>=1, set q=2k+1, S=4k+3, and choose

    r_j=2j+2                   for0<=j<k,
    r_k=2k+2,
    r_(j+k+1)=4k+2-2j         for0<=j<k.

These are distinct even rows. Define s_j=S-r_(j+k+1). The first k excursions are RR and have exactly their prescribed exits. At phase k the actual exit is2k+1, whereas the requested exit is4k+1, so failure occurs there. Every read and exit lies in a finite strip; no vertical boundary is responsible for this sharp example.

## Limits

- q=1 has a separate already-known obstruction: the first two identical-entry excursions from pristine cells are RR and LRRRRL, with different exit rows.
- Repeated entry rows in a longer minimal port cycle are not covered. Their early excursions can alter the later port pair.
- A nonempty finite warm-up or seed cap is not covered.
- Two genuinely different complementary half-builders need not satisfy the self-copy phase equations.
- The result does not eliminate the four-phase internal-state builder with fixed physical entry and exit ports.

The exploratory script probe_dense_odd_ports.py checks the narrower dense port sets for q=3,5,7,9, with2,24,720,40320 tested permutations after the first-RR necessary filter. All fail, with maxima1,2,3,4 completed excursions. These finite controls are not the proof above.
