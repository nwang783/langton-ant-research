# Standard highway already requires an infinite nonwhite autonomous lift seed

This is an all-epoch algebraic certificate, independent of the proposed face-module theorem.

Let G=C4*C4, H=<R L^3>, and assign one ordinary flipping lamp to each right coset.  Its normal form is

    q = LRRLLRLLRLRRLRLLRLLRLLRRLRLLRLLR.

It has 32 letters, 22 syllables, different first and last generators, and contains exponent-2 syllables. Thus the normal form of q^n is simply n copies, for n>0.

Write p_i for the normal form of the first i letters of W, 0<=i<104. A cell read in epoch k, phase i is q^k p_i H. The all-epoch certificate establishes:

1. Cell sets belonging to different epochs are disjoint.
2. Each epoch reads 50 different cosets.
3. Exactly 19 of those cosets have L as their first read in that epoch, while 31 have R.
4. Within an epoch every repeated coset read alternates, so this is a legal autonomous-coset word when those first-read lamps are supplied.

For item 1, equality between different epochs would require p_j^{-1} q^n p_i in H for some n>=1. Every p_i has at most 21 syllables. Multiplication at the two ends can remove or modify at most 21+21+2=44 syllables of the q^n middle block. Every length-3 syllable block in q^n contains an exponent 2. Nonidentity elements of H have only exponents 1 and 3. For n>=3, an untouched exponent 2 therefore survives, ruling out H membership. The script checks the remaining n=1,2 and all104^2 phase pairs exactly. There are no collisions.

The 19 black first-read phases (zero based) are:

    0,2,3,11,12,33,34,35,44,50,76,77,80,81,82,98,99,101,102.

Any finite prehistory can already have touched only finitely many of these disjoint future cosets. Hence an autonomous coset realization of an eventual standard highway requires infinitely many initially black coset lamps, at asymptotic rate 19 per104 steps. This holds even when the square trajectory producing the highway started from a finite seed, including a blank initial board once a standard tail is certified.

Consequently, the implication 'finite square seed -> finite autonomous-lift seed' is false in the desired attracting regime itself. A repaired transient lift can still be useful, but the projection information must be treated as a structured infinite input, not as finitely many nonwhite lift defects.

Files:
- `certify_standard_lift_seed.py`: exact finite checker with the all-epoch syllable bound.
- `certify_standard_lift_seed.json`: certificate summary.
- `standard_lift_seed.py` and `.json`: separate100-period finite replay, included only as a cross-check, not the proof of all epochs.
