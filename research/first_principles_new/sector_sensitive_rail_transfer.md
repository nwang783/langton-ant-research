# A sector-sensitive rail transfer and its non-reusable reversal

22 October 2026. Exact local identities, not a counter gadget or a counterexample. The basic sector/reversal observation is independently recorded in `causal_reduction/pose_sector_and_reverse_sweeps.md`.

Let headings N,E,S,W be0,1,2,3, and define the conserved sector

    s = x+y+h modulo2.

A step changes x+y parity and h parity, so s is invariant.

## 1. An arbitrary-length east sweep

Let A=RRLRRRRL. Starting at (0,0,N), its eight reads are

    (0,0)R, (1,0)R, (1,-1)L, (2,-1)R,
    (2,-2)R, (1,-2)R, (1,-1)R, (2,-1)L.

The endpoint is (2,0,N). Its only required black cell is (1,-1), and it preserves that cell. Its net changes add the four black cells

    (0,0), (1,0), (1,-2), (2,-2).

Translate the same list by (2k,0). Adjacent periods have consistent overlapping reads, and no period changes the required input of a later period. Therefore, for every n>=1, the finite seed

    S_n = {(2k+1,-1): 0<=k<n}

executes A^n, ends at (2n,0,N), and leaves

    T_n = S_n union {(x,0):0<=x<2n}
                    union {(x,-2):1<=x<=2n}.

The mass increases from n to5n. This is a finite prescribed sweep, not an eventual permanent-spine claim.

## 2. Literal time reversal switches sector

Put D=RLLLLRLL, the color-complement of the reversed word A. Direct reversal of the read list proves that D^n, started at (2n,-1,S) on T_n, restores S_n and ends at (0,-1,S).

However, the east endpoint has sector0 and this west start has sector1. No ant endcap, however long or complicated and regardless of the coloring, can connect these exact poses. Thus the two sweeps are NOT a reusable interface. General ant reversal J(B,p,h)=(B,p-e_h,h+2) always switches sector.

## 3. No translated literal D in the same-sector infinite bulk

Consider the infinite dense rail T with black rows y=0 and y=-2 and black odd-x cells on row y=-1, with all other cells white. A literal D at a south-facing pose (s,t,S) requires these first-read colors:

    (s,t) white;
    (s-1,t), (s-1,t-1), (s,t-1),
    (s-1,t+1), (s-2,t+1) black.

The black requirements on both rows t-1 and t+1 force t=-1. The required white current cell then forces s even, and the other middle-row requirement is consistent. This pose necessarily has sector1.

Hence not even one translated literal D period can start in the unmodified dense rail with sector0. This excludes arbitrary translations of this word, not only the nearest shifted alignments. It does NOT exclude a different periodic front or an interface whose finite defects alter the first-read pattern.

`check_rail_sweep.py` replays the literal eight-read certificates, checks the inductive formulas at several n as controls, and emits `rail_sweep.json`. The proof for every n is the local translated-read induction above, not the finite list of controls.

## Open transfer question

Can any sector0 west-traveling front convert dense T to sparse S, with a finite translating interface? The exact guarded-chronology search in `causal_reduction/front_surgery/search_reverse_rail_fronts.py` has found only opposite-sector D powers in its bounded-period class. No all-period exclusion is presently proved.
