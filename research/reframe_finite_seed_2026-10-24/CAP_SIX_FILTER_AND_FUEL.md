# Cap-six forced-output filtering and a seven-profile zero-fuel reduction

24 October 2026. Author exact certificates pending independent audit. This is a
necessary reduction for a hypothetical sustained cap-six finite-support orbit,
not a capture theorem, not yet a cap-six exit theorem, and not a reusable
computation construction.

## 1. Complete local kernel and first returns

The same rooted-edge enumeration and literal R-import/L-split generator used
in the independently signed cap-three through cap-five work gives, at cap six,
14,116 normalized active states and 12,060 cap-preserving transitions. Its
nonempty-state subgraph is a DAG. The unique recurrent SCC has 1,093 vertices
and 1,939 edges. Every hypothetical sustained cap-six orbit must therefore
return to the empty-active state infinitely often.

There are exactly 43,527 first-return local profiles, over 12 turn words.
The compact certificate lists transition-index sequences, a full nonempty
DAG order and SCC vertex/edge sets. No 399-MB expanded profile file is needed:
use component_kernel_M6.json and kernel_M6_compact_returns.json. Coverage of
the cap-six extension is submitted for independent audit, not inherited merely
from the signed smaller-cap computations.

## 2. Two distinct spatial filters

The general empty-root budget lemma is in the separate artifact
kernel_cycle_lift_2026-10-24/EMPTY_CURSOR_IMPORT_BUDGET_TRAPS.md. Its audit status
must be checked independently. For cap six, any empty root first makes four R
updates. If a mandatory final-black subset has at least three distinct old
edges in components touching neighbors of the root, cap six fails within four
updates. If that union has exactly two edges and does not contain the first-R
tip, either additional imports cause cap exit or the next L is an empty reset
that leaves a five-edge archive; the next four R updates then force cap exit.

First apply this lemma using only cells whose last read in the preceding word
was R. This excludes seven complete word classes and leaves 29,721 local
profiles in five classes. The excluded words are RRRRL, RRRRLL, RRRRLRRL,
RRRRLLRL, RRRRLLRRL, RRRRLLLLRL, RRRRLRLRRL. These exclusions do not assume
any arbitrary exterior is blank.

Next test within-profile physical realizability. At every cut, require every
edge of the prescribed COMPLETE active component to be black and every other
edge incident to any of its vertices to be white. Include the cursor vertex
when the component is empty, and include the final empty cut. Pull each bit
requirement back to the initial board using its exact earlier read parity.
A contradiction excludes the profile. If consistent, setting exactly the
required-one cells black and all other cells white constructs a finite seed;
replay it and check the complete active component at every cut.

This necessary-and-sufficient finite-prefix lift is the previously signed
full-profile constraint principle. The new cap-six batch is separately checked:
4,657 profiles are physically realizable and 25,064 are inconsistent. These
are individual finite prefixes, not a collection of composable gadgets.

For each of the 4,657 consistent profiles, its minimal initial black seed is a
MANDATORY subset of every realizing initial board. Under the fixed word its
final black field remains a mandatory subset: additional initially black cells
were never read, because every read cell had a fixed required initial bit.
Therefore the same import-budget lemma may use this entire mandatory final
field, not just the word's last-R cells. This stronger profile-level filter
excludes another 4,564 profiles, leaving exactly 93 possible profiles in a
hypothetical sustained cap-six orbit. Every exclusion records the mandatory
field, final pose, neighbor-component union and first-port membership.

Counts after both filters are: RRRRLRL 18; RRRRLRLL 2; RRRRLRRLL 1;
RRRRLRLRL 30; RRRRLRRLRL 42.

## 3. Exact integer fuel

For a complete passive w component D define its weight geometrically:

- one edge: weight 1;
- two collinear w-lattice edges (straight dimer): weight 2;
- two perpendicular w-lattice edges (corner dimer): weight 1;
- all other sizes: weight 0.

At an empty-active cut, let F be the sum of these weights over every black w
component. For finite black support F is a finite nonnegative integer. An R
import consumes an entire component and an L detachment creates an entire
component, so the exact change over a first return is the emission weight minus
the import weight. Unchanged archives cancel; there are no silent passive
merges. The checker also compares this ledger with the literal total field
weight before and after each constructed finite prefix.

All 93 surviving profiles have F_after<=F_before. Exactly 86 have a strict
integer decrease. Exactly seven have zero change, with original first-return
indices and minimal seed cells:

78: RRRRLRL, {(-1,1)}.
4554: RRRRLRLL, {(-2,1),(-1,1)}.
4555: RRRRLRLL, {(-2,-1),(-2,1),(-1,1)}.
4866: RRRRLRRLL, {(0,1),(0,2)}.
4895: RRRRLRLRL, {(-2,2),(-1,1)}.
5169: RRRRLRLRL, {(-2,-1),(-2,2),(-1,1)}.
33389: RRRRLRRLRL, {(0,1),(1,2)}.

Every listed seed starts at (0,0), north. The exact profiles, not only these
turn words or seeds, are in cap6_seven_zero_fuel_profiles.json. Different
profiles with the same word can have different complete imports and emissions.

Consequently every hypothetical sustained cap-six finite-support orbit must,
after finitely many first returns, use ONLY these seven complete profiles.
Whether such a zero-fuel tail is spatially composable is a separate question.
Pairwise compatibility would still not certify whole-cycle compatibility:
all older passive archives and the chronological cursor must remain present.
The physical-lift analysis is checking the 49 targeted ordered pairs next.

## 4. Audit and reproduction boundaries

check_cap6_filter_fuel.py checks exact path coverage, full-C lifts, profile
budget predicates and all integer fuel inequalities without any LP call. The
geometric weight test does not depend on arbitrary module-type IDs. Discovery
LPs were used to find the weight vector, not to justify it.

The kernel-generation coverage, general trap lemma, individual-prefix lift
batch, and cross-prefix composition are distinct proof obligations. This note
asserts the author's first three certificates only, pending their independent
binding; it does not conflate them with the fourth. Earlier failed type-fuel
attempts are resolved by excluding actual finite-exit profiles, rather than
ignoring their emitted resources.
