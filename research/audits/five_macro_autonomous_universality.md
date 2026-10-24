# Every five-macro word is autonomous-coset legal

Status: analytic argument by the independent-audit analysis, independently
reviewed by the causal analysis with a separate canonicalizer and155 finite
checks (all macro words of lengths1–3). This is a limitation of the new inclusion bridge, not a
physical-realizability theorem.

Let C,U,V,Q,B be the literal before-marker macro words and let G=C4*C4,
H=<RL^3>. Every finite or infinite concatenation of these five macros is
legal for some autonomous coset-lamp assignment. The assignment need not have
finite support and need not be compatible at distinct cosets projecting to
one physical square cell.

## Exact finite ingredients

The independently implemented checker `check_macro_autonomous_language.py`
uses direct normal-form canonicalization, not a finite search in H. It checks:

1. Each endpoint reduction F_M is an S word (all exponents1 or2), begins R
   and ends L. Its syllable length is2,4,6,16,18 for C,V,U,Q,B respectively.
2. The largest canonical read-coset syllable length within macro M is exactly
   |F_M|+1.
3. Every local canonical read coset is empty, L, L^2, the special R^3=L^3
   coset, or an S word beginning R.
4. Each of the five single macros,25 ordered pairs, and25 triples A C D has
   alternating read letters at every coset. These are55 exact finite tests.

## Why these finite tests cover all concatenation lengths

Endpoint words concatenate without cancellation, remaining in S and ending L.
If an endpoint prefix P is followed by any local canonical read representative,
item3 shows its resulting coset's canonical length is at least |P|-2:

- An S word beginning R concatenates without cancellation.
- Empty leaves P unchanged.
- L or L^2 only modifies the final L syllable. At exponent3 canonicalization
  deletes that syllable and decrements the preceding R syllable, removing at
  most two syllables in total. At exponent4 it removes just the final syllable.
- The special representative R^3 deletes itself under canonicalization and
  decrements the final L syllable of P, removing at most one syllable of P.

Consider a repeated coset read in macros A and D, and left-cancel their common
prefix preceding A. If W is the complete intervening macro word, the earlier
read has canonical length at most |F_A|+1, while the later one has length at
least |F_A|+|F_W|-2. They cannot coincide when |F_W|>=4.

Every nonempty endpoint word has length at least2. The only intervening word
with length below4 is one C. Hence every repeated-coset interaction occurs
within a single macro, across adjacent macros, or across A C D. Item4 checks
all of these, including all intermediate reads. In particular every two
successive reads of any coset have opposite letters.

Assign each coset the letter of its first occurrence. Then the entire finite
or infinite macro word is exactly the autonomous trajectory. This proves the
claim without a bound on macro count.

## Consequence and explicit warning

All autonomous consequences already apply to the RAW five-macro syntax:
no-A-B-A at projected physical cells, at most five visits per group state,
six per coset, and proper symbolic boundary escape. They therefore cannot,
by themselves, exclude any five-macro word or prove physical V-tip freshness.

For example BQV obeys the known short-gap grammar and the three-U-fold
exclusion, and its projection has no-A-B-A. It geometrically reuses the V tip,
but is physically impossible due to repeated equal letters at shared square
cells. Its exact local failures are recorded in `macro_grammar_noaba_vreuse.json`.
The missing condition is consistency of the lamp shared by distinct projected
cosets, not consistency within a coset or proper escape in the lift.
