# Lifting a bulk input exclusion to every fixed finite cap

23 October 2026. Analytic lifting lemma. The concrete short-refinement
application below is CONDITIONAL on the independently audited correctness of
the construction analysis's all-translation CNF encoding and checked RUP proofs.
The separately reconstructed P108 application does not depend on those CNFs.

## Lemma

Let H be the standard104 writer at heading E, drift d=(2,2), mature output
profile T, and full mature read support S. Supply a literal heading-restoring
P at heading W with drift -d. Fix any finite cap C changing E to W and let q
be its displacement.

If the full chronological periodic histories of P are internally alternating
and their first-read colors match T at translation q, this is only a necessary
bulk interface condition. If this condition FAILS, the words

    H^n C P^n

cannot all be legal with uniformly bounded initial black mass. There are only
the following exhaustive failure mechanisms:

1. A P drift class has a nonalternating complete temporal history. For all
   sufficiently large n, a cell with that complete history lies inside the n
   copies. Its within-P consecutive equal turns are impossible on any board.
2. A P first-read color disagrees with T at a class in S. There are n-O(P,C)(1)
   remote cells with all H and P visits present. Each needs a cap read to change
   the producer output before the consumer input; C touches at most |C| cells.
   Hence all sufficiently large n are chronologically impossible.
3. A P first read requests L outside S. The producer never reads that drift
   class. At least n-(p_max-p_min)-|C| distinct cells must be initially black.
   In particular the required mass grows at least n-O(P,C)(1).

These cases retain the full field. No seed reset, black-count inference from
an endpoint XOR, independent-macro assumption, or capture-time bound occurs.

For case2 the exact boundary loss, using the class notation in the P108 note,
is

    D=max(p_max,K-h_min+1)-min(p_min-1,K-h_max)-1,

where q+r_P=r_H+K*d. Thus n>D+|C| gives a contradiction. Case1 has a complete
history on max(0,n-(p_max-p_min)) cells. These formulas make the finite
boundary premise explicit rather than assuming bi-infinite profiles apply at
the ends of a finite wake.

Why the list is exhaustive: T is black only at classes in S. At every other
class T is white. A mismatch with white T outside S must therefore be a first
L, namely case3. A match outside S needs no prepared input. All colors inside
S are fixed by H's last read, independent of the initial seed.

Consequently an exact exclusion of EVERY internally alternating P/T input
match for a supplied finite candidate architecture, at every conserved-sector
translation, rules out a bounded-fuel flat pump for that architecture and
every fixed cap. Output profiles remain completely free.

## Conditional application: all phasewise1/5/9 reverse104 refinements

The construction analysis supplies this precise finite architecture:

* Start with V=complement(reverse(H)), heading W.
* Independently replace each of its104 letters by any ant-legal literal word
  of length1,5,or9 having EXACTLY the same input-to-output pose as that letter.
* There are ten choices per phase, hence10^104 presentations; all have full
  displacement(-2,-2). Charges and output profiles are unrestricted.

The reported source certificate is
`../causal_reduction/unit_scale/reverse_short_all_translations/manifest.json`.
Its finite union of possible read classes determines24 same-sector translated
input cases; outside them every possible read sees white input. The25 CNFs
are reported UNSAT with250 total independently machine-checked RUP additions,
maximum45 per case. The correctness of the chronology encoding, its complete
candidate palette, and its geometric translation closure are distinct proof
obligations from checking a RUP proof against its generated CNF.

Coordinate convention matters. That source places the unshifted reverse word
at(-1,0,W), so its translation t equals q+(1,0). Its required odd coordinate
sum for t is exactly the even coordinate sum of physical cap displacement q,
as forced by the conserved ant sector. This removes an apparent parity
disagreement with the P108 note, which uses P at its literal origin.

CONDITIONAL ON those25 CNFs encoding all advertised bulk cases correctly,
the lemma above excludes H^n C P^n with bounded initial fuel for EVERY P in
this finite1/5/9 architecture and EVERY fixed cap C. No additional word,
period, translation, or cap search is needed for this lift.

This does not exclude longer refinements, different read scaffolds, different
drifts, changing directives, non-flat interaction cycles, or universal finite-
seed capture. It closes one defined architectural possibility, not the global
gap. The independently reconstructed prepared108 word remains a useful
positive prepared-input control even though its standard-wake pump is excluded.
