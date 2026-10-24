# Exact coset model used in the exploratory free-product experiments

This is an algebraic model, not a proved reduction of every square-ant trajectory to an autonomous ant on the quotient. The distinction matters: a square cell may have many lifts, and the square lamp is shared by all those lifts.

Let G = <R,L | R^4=L^4=1>, with its unique alternating syllable normal form, each exponent in {1,2,3}. Set u=R L^3 and H=<u>. The exploratory `cactus_*.cpp` programs assign one binary lamp to each right coset gH. A step reads that lamp, flips it, and replaces g by gR or gL. Initial lamps are sampled independently at their first read. Thus each finite generated word is exactly legal for this abstract coset ant. This is not merely a parity test on group vertices: multiple group vertices can share one lamp.

## Canonicalization proof

The implementation repeatedly compares the syllable length of g, gu, and gu^{-1}, moves to a strictly shorter neighbor when possible, and identifies the possible equal-length tie. Here u^{-1}=L R^3.

If the last syllable of g is R^a:

- Right multiplication by u^{-1} appends the two syllables L,R^3, increasing syllable length by 2.
- For a=1 or 2, multiplication by u merges R^a R and appends L^3, increasing length by 1.
- For a=3, the R syllable cancels. If g had a preceding L^b syllable, the remaining L^3 merges with it: b=1 removes it too (length decreases by 2), while b=2 or 3 reduces its exponent by 1 (length decreases by 1).
- For the singleton g=R^3, gu=L^3, an equal-length tie.

The L-ending cases are symmetric, exchanging u and u^{-1}. The identity has both neighbors of length 2.

Consequently a coset has a unique minimum-syllable representative except for the single coset containing R^3 and L^3, whose two minima tie. A normal form ending in exponent 1 or 2 is already a unique minimum. Any normal form ending in exponent 3 and having at least two syllables has exactly one strictly shorter neighbor. Once moving away from a minimum along either direction of the coset line, the above cases strictly increase length thereafter. The exceptional tie has increasing length on its two outward directions. Since u has infinite order (its powers are reduced alternating words), the coset adjacency really is a two-sided line and has no other ties or minima.

The code chooses the smaller interned node ID for the exceptional {R^3,L^3} tie. Both nodes are created by either lookup, so this representative does not change later. All other recursion steps strictly decrease syllable length. The cache therefore computes exact coset equality.

## What remains unproved

Experiments found at most five visits to one group element, and at most six visits to one coset. A sharper observed condition is at most two completed first-return excursions from a group element beginning with R, and at most two beginning with L. None of these bounds is proved here. The counterexample to the published four-visit statement prevents citing that statement as a shortcut.

Even a proved uniform group/coset visit bound would establish only a transient lift, not a standard highway in the square projection. New projected visits and new lifted visits need not coincide, and a finite square seed need not lift to a finite lamp support.
