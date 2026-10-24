# Forced-seed construction with finitely many spatial powers

Date: 2026-10-23. Both the finite-order corollary in Section1 and the general finite-power
extension in Section2 passed independent analytic review (04:56 UTC).
No integrated arbitrary-mass implementation or growing ant model is claimed.

## 1. Finite-order matrices: signed corollary

Suppose the fixed typed substitution has spatial matrix A of finite order,
with the same coarse final-heading condition as in the earlier validators.
For a chosen growing rooted-power limit, take a power q divisible by the order
of A and by the first-letter root-cycle length. The powered substitution has
spatial matrix A^q=I, is nonerasing and growing, and is prolongable at the
chosen root. It has the same selected nested limit. Apply the signed theorem
in `automatic_forced_seed.md`.

Thus fixed finite-order presentations have decidable realization by some finite
seed without any mass or coordinate bound. Root-cycle phases are handled as
separate chosen limits, not conflated with intermediate words on the same board.

## 2. General finite-power extension

Suppose A is an integer matrix with supplied mu>=0 and q>=1 satisfying

    A^(mu+q)=A^mu.

After taking a first-letter power if necessary, assume the same nonerasing,
growing, root-prolongable hypotheses. The exact parity arrays Q_s(r,z) are
already effectively automatic by the signed finite-power validator IJ.
We claim the selected-occurrence construction applies unchanged after adding
finite exponent phases to the occurrence graph.

For an actual leaf at depth r, the edge at level d has remaining exponent
r-d. Its geometric offset is A^(r-d) p_sj. All these matrix powers belong to
a finite known set. It remains to recognize exactly their legal descending
sequences, not arbitrary choices of phase.

### 2.1 The finite descending-exponent graph

For mu>0 use low labels 0,...,mu-1 and high labels mu,...,mu+q-1. A source
state consists of a typed letter s and a label h. An occurrence edge choosing
child j has weight A^h p_sj and leads to child t_sj with the next label:

* low h>0: h-1;
* low h=0: the terminal leaf layer (no outgoing edges);
* high h: the cyclic predecessor mu+((h-1-mu) mod q);
* additionally, at high h=mu an exit to low mu-1 is permitted.

The graph starts at (a,h) for any one of these finitely many labels and must
end at the terminal layer. A separate empty path handles r=0. For each chosen
start label, use only paths from that start to terminal leaves.

Every accepted path of length r gives exactly the exponent sequence
r-1,r-2,...,0 after replacing high exponents by their representatives. Indeed,
the low suffix has exactly mu edges; the high segment exits only after its
phase-mu edge. Counting backward from this exit fixes every preceding phase,
including the start phase. Conversely every depth r>=1 supplies such a path.
There is no premature-termination problem: terminal vertices have no outgoing
edges, and there is only one downward exit from the high cycle.

When mu=0, omit low labels. The high labels are0,...,q-1, with their cyclic
predecessor transitions; at h=0 an additional exit goes directly to a terminal
leaf. The same backward-count argument applies. Alternatively Section1 covers
this case because A^q=I.

Thus the accepted regular edge language represents genuine leaves of actual
root powers, with exact positions. Multiple initial labels form a finite union,
handled separately. The elementary bounded path-cover lemma remains applicable:
deleting closed segments preserves both graph endpoints, and reinserting its
cycles cannot create an invalid low suffix or terminal continuation.

### 2.2 Preceding-read parity on a scheme

For a selected graph edge e_d=(s,j,t,h), let V_(d-1) be the sum of prior chosen
edge weights. Each earlier sibling i<j contributes

    Q_t_si(r-d, z-V_(d-1)-A^h p_si).

This is exactly the same sibling decomposition as equation(1) of the A=I note,
with the known phase-dependent shift substituted. Along each repeated graph
cycle, h and each sibling type/offset at a fixed edge position are constant.
The depth r-d and accumulated position are affine in the scheme exponents and
its repetition counter. Consequently all prior parity is again a finite XOR
of automatic affine evaluations and bounded-fiber parity projections.

Select the least genuine scheme and its lexicographically least exponent tuple
for each spatial output. The selected terminal letter fixes the required turn.
Its preceding parity therefore constructs the automatic forced initial coloring,
white outside the visited set, exactly as before.

### 2.3 Decision and limits

If the forced black set is infinite, no finite seed works. Otherwise enumerate
it and use IJ to check the whole prescribed path. This yields a terminating
realization decision with no supplied mass bound for every fixed finite-power
presentation in the stated class.

This uses the ordered substitution and its finite set of spatial powers. It is
NOT a solution of arbitrary bounded-displacement automatic-graph connectivity,
and it does not decide arbitrary finite-seed Langton-ant behavior. The global
highway conjecture and an actual finite-support counterexample remain unresolved.
