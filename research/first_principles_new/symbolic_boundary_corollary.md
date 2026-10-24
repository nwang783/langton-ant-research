# Proper symbolic boundary coding, and its exact limitations

This note first concerns the autonomous coset ant. The separately audited projection bridge in `completed_fingers_and_no_interleaving.md` now transfers its proper-boundary conclusion to every square-ant orbit.

Let G = <R,L | R^4=L^4=1>, H=<RL^3>, and let the ant read and flip a fixed lamp at its current right coset gH before multiplying g by that lamp's turn. The face-module return and separation lemmas in `face_module_return_lemma.md`, together with its finite interfaces, give at most six reads per coset, for arbitrary initial lamps.

## Corollary: convergence to one infinite reduced ray

Every group element belongs to one coset, so it too is visited at most six times. There are finitely many reduced normal forms of syllable length at most k. Consequently, for every k the ant eventually avoids all of them. Its syllable length tends to infinity.

Right multiplication changes only the final syllable, or removes it when its exponent reaches four. Once the ant remains above syllable length k, its first k syllables cannot change. These stabilized prefixes are compatible and define a unique infinite reduced syllable sequence. Thus the orbit converges to a boundary ray of the free product.

After the first change of turn, rebase as in the trapping lemma. Every proper internal syllable then has exponent one or two. Hence every syllable in the limiting ray has exponent one or two. This conclusion needs neither finite support nor a probabilistic initial distribution.

## Every such ray is possible with unrestricted lamps

Conversely, take any infinite R/L word all of whose maximal runs have length one or two. Each finite prefix lies in S, the set of normal forms with all exponents at most two. Distinct prefixes are distinct canonical cosets, by the coset canonicalization lemma. Give the coset of prefix w the initial lamp equal to the next letter after w. The ant follows the prescribed word and never rereads a coset. Lamps away from this ray can be arbitrary.

There are therefore uncountably many possible boundary rays for unrestricted coset lamps, including aperiodic rays. The proper-stack theorem itself supplies no selection of the standard ray. Nor does it bound the sizes or durations of finite side excursions.

## Two separate missing implications

1. Square-to-coset legality is now proved separately: projected square lamps are shared by many cosets, but each coset occurs in only one contiguous block of its physical site's visit chronology. The no-A-B-A theorem and first-violation coupling establish the required alternating subsequences. See `completed_fingers_and_no_interleaving.md`.
2. Finite projected support to eventual standard behavior: even if (1) holds, a finite square seed generally induces infinitely many initially black coset lamps. Indeed `standard_lift_infinite_seed_obstruction.md` proves that the desired standard104 ray itself needs nineteen fresh initially black cosets per period. One must exploit compatibility between these infinitely many lamps at their common projected sites, not simply finite support in the lift.

Even eventual periodicity of the limiting boundary ray alone would not immediately imply eventual periodicity of the actual turn stream: arbitrarily large finite excursions could remain attached to its successive prefixes. A separate bound or stabilization of those excursions would be needed.
