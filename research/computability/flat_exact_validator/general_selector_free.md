# Generated genuine covers and selector-free finite-seed realization

2026-10-23 07:03 UTC. New integrated arbitrary-branching A=I implementation,
submitted for independent review. No finite-power matrix extension or accepted
growing ant model is claimed.

## Exact scope and new implementation boundary

The input is a finite nonerasing exact additive-I physically typed UNIT-READ
presentation. It may have arbitrary decorations, unequal image lengths,
arbitrary signed charges, reducible incidence and BRANCHING occurrence SCCs.
Every image's physical headings/displacement are checked literally. The target
is whether ONE finite initial board realizes EVERY depth block phi^r(root).
A separately checked growing prolongable root makes this an infinite-model
question. All positive controls here are nongrowing families.

The previously signed JE theorem already proves decidability mathematically.
Its canonical least-scheme/least-exponent selector has NOT been implemented.
The route below avoids that selector and now integrates cover generation,
forced requirements, finite-seed extraction and the general given-seed frames.
This is a new execution boundary, not a new global ant decidability theorem.

## 1. The selector is unnecessary for this decision

Suppose a finite collection of GENUINE linear occurrence-walk schemes covers
all visited physical positions. It need not cover every occurrence WORD, and
need not preserve the first visit. Every scheme instance selects an actual
read in some root depth block.

Use the exact complete preceding-read parity to form its required INITIAL
color, and union separately over all scheme instances to obtain selected
Black and White relations. If they intersect, no board can realize even those
genuine selected occurrences. If selected Black is infinite, no finite board
can realize them. Neither negative conclusion requires complete coverage.

Otherwise selected Black is a finite set B*. If position coverage is complete,
every visited cell has at least one selected requirement. Any realizing board
must agree with B* on the WHOLE visited set: selected Black cells must be black,
and every remaining visited cell must have a selected White requirement.
Thus B* is the unique possible minimal seed. A general given-seed validator
checks ALL unselected occurrences. If it accepts B*, return it; if it rejects,
there is no finite realizing board. Off-read black cells can never repair it.

This logical simplification was independently confirmed before implementation.
It does not claim that selected consistency alone establishes legality.

## 2. Complete generated covers from the signed bounded-base lemma

Use the JE elementary support-preserving bound. Every occurrence walk has the
same edge counts and endpoints as a walk built from a base of length at most

    L = |V|(|E|+1)-1,

with fixed powers of simple directed cycles inserted at first visits to their
chosen basepoints. |E| counts CHILD OCCURRENCES, keeping parallel children
distinct. Hence both physical position and total depth are preserved.

`generated_cover_decider.py` enumerates ALL genuine root-started bases of
length0..L. For one base it finds EVERY simple cycle whose edges lie in that
base's support, gives it a fixed canonical cyclic rotation, sorts those cycle
types, and inserts stars at their first basepoint visits in the base. Every
exponent tuple gives an actual graph walk. The signed support-preserving lemma
ensures the resulting finite scheme family covers every original edge-count
vector, hence every visited position (indeed every depth/position/endpoint).

Early rejection from any genuine partial requirement family is safe, so the
program checks conflicts and infinite forced-black sets while enumerating.
If no early rejection occurs, exhausting the proved L bound establishes
coverage structurally. No expensive spatial cover equality test is needed.
It then extracts B* and runs the general exact given-seed frames.

A caller may impose a smaller base-length or scheme-count cap. If no genuine
negative certificate has appeared, an incomplete enumeration returns UNKNOWN,
never YES or  Arithmetic/ISL, memory and recursion resource errors similarly
return UNKNOWN. The finite mathematical algorithm is obtained without
experiment caps and with unlimited exact-algebra resources; its complexity
is not claimed practical. The complete finite-power A!=I extension is NOT
implemented here.

## 3. Given-seed frames now integrated without flatness

`general_given_seed.py` implements the signed IJ construction at A=I. It derives
all parity machines from the images. It chooses a finite actual representative
prefix for each reachable state, and builds its complete input template
I_s(r) directly from the supplied B and preceding-prefix parity. No template
or first-visit-color certificate is supplied by the caller.

The exact all-depth read footprints use the signed Euler-count construction.
Duplicate edges with the SAME source,target,offset may be merged for existence
only; parity retains every occurrence. Degree balances choose an endpoint,
and used-support rank conditions ensure weak connectivity to the start.
These are exact Presburger read sets.

`isl_automatic.py` converts an ISL set through public integer-set APIs, not a
printed-formula parser. It lifts existential local integers to explicit set
dimensions using isl_basic_set_lift and flattens the wrapped space. Each lifted
integer is represented as a difference of two naturals; ordinary existential
projection removes them. Constraint coefficients are read exactly as integers.
Visible x,y use four sign orthants. This supports congruences, floors and
signed hidden witnesses. 

For each parent, child and depth, the exact automatic check compares its actual
parent-derived entry board with the chosen child template ON THE CHILD'S WHOLE
READ SET. Base turns are checked separately. The signed IJ induction supplies
necessity and sufficiency. A returned frame witness is a finite discrepancy,
not a claim that its tested template cell was necessarily the earliest physical
failure. Positive growing-root acceptance is separately flagged.

## 4. Executed controls and important resource limitation

`isl_automatic.json` checks14,400 exact ISL point memberships across signed rays,
modulo/floor sets, signed integer witnesses and two local-div expressions.

`general_given_seed.json` accepts identity R/empty and L/origin, a nonprolongable
two-state same-read cycle, and a nontrivial transient nine-read family whose
unique seed is{(0,1),(1,0),(1,1)}. The latter completes68 full all-depth frame
checks. The recurrent branching R5 controller fails at child4,r=0,origin.

`scheme_cover_decider.json` checks supplied position covers explicitly. A
one-position R5 cover is correctly INCOMPLETE, not negative. Four literal R5
occurrences cover all visited positions and force an empty seed, but the general
frames correctly reject it. A genuine two-edge cycle in the unit-nine control
already forces infinitely many black cells, so no exact global read set is
requested for that negative proof.

`generated_cover_decider.json` executes automatic cover generation:

- Identity R/L exhaust2 schemes each and return exact positive nongrowing seeds.
- A two-state cycle exhausts6 schemes through bound5 and is positive nongrowing.
- Recurrent branching R5 rejects after6 genuine schemes at base length1.
- Recurrent branching unit-nine rejects after21 schemes at base length2 by
  infinite forced black demand; its theoretical full base bound is583.
- The transient nine-read positive EXHAUSTS1,450 generated schemes through the
  proved bound161, extracts its three-cell seed and completes68 exact frames.
- An intentionally capped enumeration returns UNKNOWN.

One earlier attempt to force the dense unit-nine GIVEN-SEED read-set construction
ended with process exit137 before a read-set result. Its log is preserved as
`general_given_seed_dense_readset_failed.log`; this is strictly an UNKNOWN
resource outcome, not evidence of nonrealizability. The later generated-cover
negative avoids that stage by a valid unbounded forced-seed certificate. No
retry of the same dense read-set calculation is represented as a success.

No positive control is a growing ant trajectory. No general finite-seed capture
decider, finite universal computer, finite-seed undecidability result, or global
highway proof follows from this fixed-presentation execution milestone.
