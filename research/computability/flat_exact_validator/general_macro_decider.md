# General branching finite-base macro realization at spatial I

2026-10-23 07:17 UTC. New separate extension submitted for independent review.
It combines the signed KE finite-base semantics with KJ's generated genuine
cover and exact frame method. No unit subdivision is asserted, and no growing
ant model is accepted.

## Scope

A state has a finite nonempty literal base R/L word, its incoming/outgoing
headings and its full integer displacement, possibly zero. Every substitution
image preserves that complete base pose and has matching child boundary
headings. Arbitrary finite decorations, unequal base/image lengths and
BRANCHING occurrence SCCs are allowed. Physical depth-r words apply the macro
substitution r times, then expand every resulting state into its actual base.
The decision asks for one finite initial board realizing every depth word.
Only a separately flagged prolongable growing root defines an infinite model.

`GeneralMacroModel` retains the signed KE strict base/image geometry checks but
removes only its explicit flat-SCC filter. No malformed geometry exception is
swallowed. `general_macro_decider.py` is separate from every signed earlier
source.

## Cover and initial-color requirements

Use KJ's generated support-preserving cover with bound |V|(|E|+1)-1, counting
all macro child occurrences separately. A cover walk preserves the original
macro endpoint, total depth and offset. Split its terminal state over EVERY
physical base read. Its offset, required turn and earlier-read parity inside
the base are exactly those in KE. This covers every visited physical position.
The generated selected Black/White relations are handled exactly as in KJ:
partial genuine conflicts or infinite black demand certify  a consistent
finite family gives a candidate only after complete structural coverage.

## Exact macro given-seed frames

A finite chosen representative prefix for each reachable macro state is a word
of macro labels. At depth r, its parity is a finite sum of Q_t(r) shifted by the
prefix displacements of their BASE poses. Additivity at spatial I makes these
shifts independent of r. Canonical I_s templates therefore have the same exact
form as IJ/KJ, with the KE polynomial initial parity vector and its constant
coordinate shifts retained.

At r=0, the whole base word must be run, not merely one coarse turn. The program
checks EVERY base read against its canonical entry board and the parity of its
earlier base reads. Earlier representative-prefix macro reads are toggled ONE
PHYSICAL READ AT A TIME. Treating one base's position iterable as a set would
incorrectly discard repeated reads before parity; the dedicated positive
revisit control below exposes that error and it was fixed before this freeze.

For footprints, an occurrence path ending at state t reads every base position
q in t. `macro_relation` uses exact Euler-count balances with a FIXED endpoint
for each disjunct and imposes

    x = sum(edge offsets)_x + q_x,
    y = sum(edge offsets)_y + q_y.

Union over endpoints and terminal read offsets gives the complete all-depth
physical read set. Repeated base positions may be deduplicated for existence
ONLY; parity keeps every read. Connectivity ranks and signed ISL lifting are
exactly as in the signed unit read-set bridge. A canonical frame compares
parent-derived input with child I_t on this ENTIRE physical read set.

The same base/frame induction proves necessity and sufficiency for all depth
words, without assuming a macro represents a unit movement. Empty bases and
erasing images are not admitted. Explicit cover caps or exact-algebra/resource
errors return UNKNOWN, never an inferred realization answer.

## Executed controls

`general_macro_decider.json` records:

- An identity multi-read base exhausts2 schemes, returns its exact three-cell
  seed and passes4 all-depth frames.
- A two-state multi-read cycle exhausts6 schemes and passes8 frames.
- A transient root with base LLLRRRRL and image C D, C=LLLR,D=RRRL, exhausts29
  schemes and passes16 frames, returning the exact same prepared seed.
- A dedicated canonical-prefix revisit positive exhausts326 schemes and passes
  40 frames. Its first macro is LLLRRRRL; three fixed R reads precede a uniquely
  decorated R at a cell read twice in that first macro. This detects incorrect
  set-deduplicating prefix parity. Its exact three-cell seed is recovered.
- A genuinely BRANCHING zero-displacement state with base RRRR and image s s
  is rejected by generated requirements after3 schemes. A separate DIRECT
  general macro-frame run rejects at child1,r=0,origin, so the new read-set/
  frame path is exercised independently of early color rejection.
- An identity zero-parity illegal R^8 base is rejected immediately.
- Capped G and H same-board families fail after3 and5 genuine schemes. These
  are not claims that their individual prepared depths are illegal; KE and
  the constructor's direct proofs establish those positive local contracts.
- An intentionally incomplete cover returns UNKNOWN.

All positive controls are nongrowing. No macro family is treated as renewable,
no fixed background is silently reset, and no finite-seed capture theorem or
counterexample follows. Finite-order/singular spatial matrices and changing
heading-boundary maps are outside this new file's scope.
