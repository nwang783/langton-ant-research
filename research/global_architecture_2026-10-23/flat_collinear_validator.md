# Executed exact validator for supplied collinear flat pumps

23 October 2026. The executable `flat_collinear_validator.py` checks one
supplied literal family H^n C P^n, n>=n0. It does not search for H,C,P, synthesize
a cap, or implement the general semilinear extraction theorem in
`flat_pump_budget_falsifier_decider.md`.

## Supported geometry and outputs

H and P must be nonempty, restore their respective incoming headings, and
have nonzero collinear integral drifts. C is any finite R/L word, including
empty. P's incoming heading is computed from C. The finite seed is allowed to
depend on n. H need not itself be standard, which permits nonvacuous legal
growing-fuel controls.

For all n>=n0, the implementation returns:

1. Exact chronological legality, including the set of illegal n.
2. The exact relation (n,x,y) for cells whose FIRST requested read is L.
3. A uniform upper bound on this relation's fiber cardinalities, or an exact
   unbounded-interval certificate. If an unbounded basic piece unexpectedly
   retains local division/existential structure, it returns UNKNOWN instead.

When legality passes, the first-L set is exactly the minimum initial black
seed. When legality fails, it is merely a necessary first-read color demand;
calling its cardinality the mass of an executing seed would be incorrect.
In particular, bounded first-L demand does not replace chronology.

Any libisl parsing, arithmetic, or resource error raises an exception. It is
not interpreted as an empty relation, a  or a bounded-fuel certificate.
Integer maxima are read as arbitrary-precision decimal integers, not C longs.

## Exact finite row reduction

Write d_H=a*v, d_P=b*v with primitive integral v and nonzero a,b. Group all
literal phase positions modulo Z*v. For one representative r, every physical
read has position r+z*v. Each phase contributes one row:

* producer: z=k+a*j, time |H|*j+i, 0<=j<n;
* cap: z=a*n+k, time |H|*n+i;
* consumer: z=a*n+k+b*j, time |H|*n+|C|+|P|*j+i.

The cap displacement is included in the consumer's k. Let
M=lcm(|a|,|b|). Split n=M*N+r_n and z=M*Z+r_z into their finitely many residues.
Every congruence is then either true or false. Every surviving row domain is
a div-free integer polyhedron in N,Z, and its time is rational affine in N,Z.
Time comparisons are cleared of denominators using exact integer arithmetic.

For a row requesting L, subtract every earlier active row. Their union is
exactly first-L. For a same-letter ordered pair, intersect their active domains
and subtract all domains having a read strictly between them. The union of
the remaining cells is exactly the consecutive-same-turn violation relation.
This retains the full chronological cell history, not an endpoint XOR.

Reconstruction is injective within each group/residue case since v!=0.
Different primitive-lattice groups are disjoint; different z residues within
a group are disjoint. At a given n only one n residue occurs.

## Why the fuel test is exact in the div-free fragment

The implementation deliberately does not coalesce the planar first-L relation
before decomposing it into its finitely many basic sets. A div-free basic
set is an integer polyhedron. Fixing N leaves a convex real interval in Z,
intersected with the integers, possibly empty.

For each such basic set form exactly the pair relation of Z values at the SAME
N, then its set of differences. libisl computes the supremum W of these
differences. A finite W bounds that piece's fiber by W+1. If W is infinite,
integer interval fibers have arbitrarily many points. Injective reconstruction
therefore gives arbitrarily many distinct required initial-black cells.

A finite union is uniformly bounded iff every piece is; overlaps make the
sum of upper bounds loose but cannot invalidate it. Summation is over pieces,
groups and z residues, followed by the maximum over n residues. An unbounded
piece with local divs is not assumed to have interval fibers and is rejected
as an UNKNOWN fuel decision. No arbitrary Presburger cardinality solver is
claimed.

An explicit control uses the union Z=0 or Z=N: its global diameter is
unbounded, but its two basic pieces each have width0, so the checker correctly
certifies cardinality at most2. A congruence-restricted growing interval tests
the conservative UNKNOWN branch.

## Executed controls

`check_flat_collinear_validator.py` and
`flat_collinear_validator_controls.json` contain50 exact supplied-family
cases and249 literal parameter controls. For each literal control, a separate
direct history dictionary reconstructs first-L and all cells having consecutive
same-turn reads, then compares BOTH sets to the exact all-n relations.
Whenever legal, a fresh ant simulator executes the full word on its canonical
first-L seed.

Nonvacuous controls include:

* Standard H^n H^n: legal for every n, uniform minimum initial mass13.
* Prepared RLLR^n RLLR^n: legal for every n, unbounded initial fuel.
* The construction analysis's legal prepared108 word, doubled similarly:
  legal for every n, unbounded initial fuel.
* H^n R D10^n at heading W, with D10=LLLLRLRRRR: first-L demand is bounded
  by13, but chronology fails for EVERY positive n.
* Unequal collinear copy rates and reversed drift, plus44 short deterministic
  geometry controls. These are validation controls, not a pump search.

The key interval-fiber argument has been analytically checked independently.
Independent executable reconstruction of the complete checker is tracked
separately in the audit ledger; literal controls alone are not that audit.

## Use and current substantive outcome

Provide a JSON object with H,C,P strings, optional integer heading (default3,
W), and optional positive n0 (default1), then run:

    python flat_collinear_validator.py supplied.json --output result.json

The implemented decision boundary is explicitly narrower than arbitrary flat
presentations, zero drift, noncollinear paths, arbitrary directives, or seed
capture. There is no accepted bounded-fuel positive-K pump.

The construction analysis supplied a concrete prepared108 rewriter. A separate
finite all-translation interface certificate now excludes EVERY fixed cap
feeding its return from a standard producer. That structural result is in
`reverse108_flat_interface_exclusion.md`; it is not inferred from a few supplied
caps or from a broad scan of periods.
