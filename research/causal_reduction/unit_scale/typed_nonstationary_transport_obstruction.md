# Arbitrarily phased elementary heading-dependent transport is bounded

23 October 2026, 04:43 UTC. Complete certificates and all-depth proof
independently signed. A no-import inventory/complex-heading replay matches
all counts and digests; see ../../audits/typed_directive_independent.json. This is an arbitrary-directive theorem for a fixed local alphabet,
not a bound on all ant excursions or all unit-scale mechanisms.

## Exact class

There are eight physical states (incoming heading, turn), ordered
N-R,N-L,E-R,E-L,S-R,S-L,W-R,W-L. At EACH refinement level, each state may
independently use its identity or one of the six internally legal length-nine
unit-geometry, exact-charge images listed in
`heading_dependent_transport_exclusion.md`. A word is interpreted in the
incoming heading of its state. Each image preserves the displacement and
final heading of its coarse one-step action. Opposite headings need not
share images. The entire eight-state phase map may vary arbitrarily with
level, with no periodicity, computability or finite-state assumption.

We consider finite compositions on a single typed root and growing rooted
limits of those compositions. We do NOT assume any intermediate level word
is an ant trajectory. The conclusion holds on arbitrary initial colorings,
not merely finite black support.

**Claim.** Every internally ant-legal composed root word has length at most
41. Therefore this class has no growing ant-realizable rooted directive
limit, irrespective of the number or order of phases.

## The structural facts that make a finite certificate sufficient

For every primitive nine-image of state s, its typed state-incidence vector
is exactly one copy of EACH of the eight states, plus one additional copy
of s. This is directly checked for all48 typed primitives. In particular:

1. Every phase preserves occurrence of each physical state already present.
2. Once any root expansion is effective, its word contains all eight states.
3. Any inner composed root word of length greater than one has a literal
   typed primitive nine-image as a factor. To see this, choose its last
   effective expansion, working outwards from the root; every later phase
   leaves the resulting word unchanged.
4. If C(v) is internally legal and v contains all states, every C(s) is
   internally legal, since each is a contiguous factor of C(v).

Literal color conflicts are invariant under translation and quarter rotation,
and cannot be repaired by prior history or another initial coloring.

## Complete finite reduction

Let f be one elementary outer phase and w a primitive at incoming north.
An exact on-demand assignment tree tests all7^8 independent image assignments.
There are312 legal pairs (w,f) over the twelve north primitives: twelve have
f equal to the identity, and300 are genuinely active. The resulting lengths
are9,17,25,33,41. The assignment cubes and surviving full assignments account
for all7^8 cases for EACH primitive, with no search cap.

Global rotation gives exactly544 distinct active outer phases f that can
legally expand at least one typed primitive. A phase outside that set cannot
occur as the outer factor of a locally legal two-active-phase composite.

For each such f and each state s, independently retain precisely the inner
choices g(s) for which f(g(s)) is internally legal. Taking their Cartesian
product, while excluding the simultaneous identity g, gives exactly29,840
ordered phase pairs and29,840 distinct locally legal composite controllers
C=f o g. This domain-product step is complete because internal legality of
one composite image depends only on that state's inner choice.

Finally, for EACH of these29,840 controllers C and EACH of the48 typed
primitive words w, C(w) has a literal color conflict. All1,432,320 cases fail
by zero-based read53. Thus no locally legal two-active-phase composite can
accept even one further effective primitive transport.

## Arbitrary-depth proof

Remove globally identity phases. If a composed root word has at most two
effective nonidentity levels, the one-phase primitive inventory and the
local two-phase root test bound its legal length by41.

Otherwise take the outermost two nonidentity phases f,g and write the word
as C(v), C=f o g. The remaining inner word v has length greater than one.
Indeed, once an inner effective expansion occurs, all states are present,
so each later nonidentity phase is effective. If v instead had length one,
only f and g could be effective, contrary to the present case.

By structural fact2, v contains every state. Legality of C(v) therefore
forces every image C(s) to be legal. Consequently C belongs to the complete
29,840-controller inventory. By fact3, v contains a typed primitive factor
w. But the extension certificate makes C(w) illegal. This is a literal
factor of C(v), a contradiction.

No assumption about legality of v or other intermediate phase words was
used. The proof is not an iteration of a false principle that outer
substitution preserves inner illegality.

## Frozen artifacts

- `probe_typed_transport_composition.py/.json/.records.json/.survivors.json`:
  all twelve root primitives, assignment-cube coverage,312 legal survivors.
- `analyze_typed_phase_pairs.py/.inventory.json/.json`: complete29,840 locally
  legal composite inventory. Its separate115,336 growing-root literal tests
  all conflict by41, but are NOT needed for the all-depth proof. They omit
  100 controllers with no growing first-state cycle, which ARE retained in
  the full inventory and extension test.
- `check_typed_third_level.py/.json/.conflicts.u16`: all1,432,320 extension
  conflicts, ordered by lexicographic controller tuple, then state0..7,
  then primitive palette order. Conflict indices are unsigned little-endian
  16-bit integers. Digest:

      0a52346ee1a8026d5becd89b683b71d2045147742fafb6692486b1a76d531ad8

  Full composite-inventory digest:

      14e05c4287eac6387e19d4ecba1087cf8e14a5602d0e8fbbee0f31f0a2967bea

The author scripts share code; the independent auditor separately regenerated
the palette and assignment trees, rebuilt the Cartesian domains, and streamed
every extension with a different literal representation.

## What is still not covered

Additional hidden/decorated states, occurrence-dependent image choices within
one level, a different local transport alphabet, nonpreserved headings and
other spatial transforms remain outside this result. In particular this is
not a general obstruction to finite-particle two-sided stationary mechanisms.
