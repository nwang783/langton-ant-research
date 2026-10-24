# Protected fresh exploration: inverse periodic-front synthesis


The full conjecture remains unproved and undisproved.

## Question

Can an explicitly engineered, finite-seed, translating front have a turn word
other than standard104? Rather than sample seeds and hope for rare outcomes,
we synthesize periodic trajectories directly and demand an exact all-future
white-front certificate. No low-mass, five-macro, bounded-retreat, or lifted
module theorem is assumed.

The archived direct periodic-word SMT already encoded arbitrary unknown
trajectories. We do not claim that criterion as new. The different construction
here fixes a translating geometric backbone and inserts optional finite
pose-return excursions. Its geometry stays known, and its complete consistency
conditions become guarded linear equations over GF(2), avoiding unknown
coordinate arithmetic and any installed SAT/SMT dependency.

## Exact reduction

For a backbone word whose heading returns and whose drift d is nonzero, put
a finite library of pose-returning words at every original phase. Choose at
most one optional word per phase. The library may be arbitrary; actual read
alternation within each optional word is required, not assumed from a grammar.

Create all potential read events, each with physical position, phase order,
turn letter, and a Boolean inclusion variable (original reads are always on).
Partition events modulo Z*d. Within each class sort by decreasing longitudinal
rank and then increasing phase/read order. Any selected periodic finite-seed
front must read R,L,R,L,... in that order, starting with R. Conversely that
condition constructs a finite seed and certifies infinite repetition, by the
inherited direct chronology theorem:
`first_principles_2026-10-21/ant_rethink/defect_dynamics/direct_periodic_chronology.md`.

For each event, the parity of preceding selected events is an affine GF(2)
expression in the optional-word variables. Its equality to the event's L-bit
is unconditional for original reads, and guarded by that option's inclusion
variable for optional reads. At-most-one choices per phase are explicit.
Potential events of mutually exclusive options can be placed in either order:
only selected events contribute. Therefore the reduction is exact, not a
relaxation or a simulated finite horizon.

`loop_decoration_solver.py` uses elementary Gaussian elimination plus complete
branching on unknown inclusion variables. Time/node caps produce UNKNOWN, not
UNSAT. Every SAT witness is independently reconstructed as a literal word,
checked class-by-class with integer coordinates, given an explicit finite
seed, and replayed for five periods as an additional control. The chronology
check, not the five-period observation, certifies the infinite tail.

## Initial construction families and results

At each phase with original turn c, the first library offers:
- no loop;
- four turns opposite to c;
- four turns c, then four turns opposite to c.

These are exactly all possible trains of unadorned four-turn loops immediately
before that original turn. Three such loops are impossible: the third loop
would reread a non-entry cell of the first loop with the same letter.

For standard104, no nontrivial choice is valid. Single-loop original-read
equations have rank102 in104 variables, leaving only four assignments; each
of the three nonzero assignments fails an inserted read. The double-loop
family has208 variables. The initial solver excluded it in209 search nodes; the independently audited implication-closure version excludes it at its root node.
For the axialT24 backbone, single loops already contradict the original-read
linear equations; single/double loops are excluded by a17-node branch search.
These are narrow family exclusions, not a classification of all fronts.

Positive controls remove one RRRR or LLLL from standard104, then recover a
verified104-step front by insertion. The zero-decoration standard control also
passes. `standard_single_four_solutions.json` records the particularly small
single-loop certificate.

`search_backbones.py` tests binary necklaces of bounded length, all nonzero
drifts and heading-returning backbones, with the single/double library. It
retains UNKNOWNs explicitly. This bounds BACKBONE length, not total period;
a length n backbone can yield periods up to9n. No negative result is silently
extended beyond this exact construction family.

## Broader, genuinely non-module excursions

`enumerate_pose_loops.py` enumerates all physically feasible pose-return words
through a specified length by first-read branching and forced alternation on
repeated cells. Through length24 the counts are2,8,26,88,366,1998 at lengths
4,8,12,16,20,24. Some loops are not free-product-identity module decorations:
for example (RRL)^4 is a legal12-step physical pose return. Thus the construction
can change the symbolic backbone as well as adding trivial four-turn loops.
The current broader tests use every pose loop through length12. Inconclusive
solver caps remain visible in `loop_library12_results.json`.

The guarded-GF(2) reduction and solver soundness passed independent audit on22October2026 at14:54UTC; the standard single/double exclusions and zero control were independently replayed. The large bounded-backbone and loop-library search outputs have not yet been independently audited.

No new nonstandard highway has been found. A SAT model will not be reported
as a counterexample until its finite seed and exact all-future certificate
have been independently checked.

## Exact local front substitutions and backbone mutations

`standard_loop_skeleton.py` extracts a32-letter geometric backbone and seven
pose-returning excursions from the104-word; the seven lengths are20,4,8,8,12,4,16.
The extraction keeps a literal chronological subsequence and checks every
removed interval returns to its starting pose.

`search_skeleton_mitm.py` allows every feasible excursion up to length N, or
the original excursion, independently at each of the seven sites. Original
backbone read constraints give a32-bit parity signature for each choice.
Meet-in-the-middle exhausts the exact XOR equation, then every surviving
assignment is checked against all inserted-event guards and the direct
integer chronology verifier. At N=12, only the original highway survives
among990,439,600 choices. At N=16, the same is true among4,001,504,141,376
choices;3,141 pass the original-read equations, and only one passes all reads.
These large family counts are not counts of independent simulation runs.

`search_pair_substitutions.py` instead allows arbitrary feasible loops up to
N at any one or two of the seven sites, keeping the rest fixed. Two changes
can preserve original reads only when their parity-change signatures agree,
so a hash join checks the entire pair family without quadratic enumeration.
The N=24 run gives2,078 original-read-compatible candidates and only one valid
front, which is again a cyclic standard104 word. No alternative was found.

`search_core_mutations.py` changes any two of the32 geometric-backbone turns,
then permits the independent seven-site excursion choices. For N=12,484
nonzero-drift edited backbones are excluded; the unchanged standard backbone
is retained as a positive control. Twelve edited backbones have zero drift
and are skipped. Of the485 nonzero-drift cores including the control,434
already fail the relaxed original-read linear equations. No low-mass, lift,
or macro-grammar restriction was used in these synthesis tests.

These additional bounded-family programs/results await independent audit.
They challenge nonstandard periodic-front constructions, but do not eliminate
aperiodic finite-seed behavior or arbitrary different periodic geometries.

## Aperiodic four-loop detours have finite fuel

`four_loop_detour_finite_fuel.md` and `window_detour_rigidity.py` prove a new
restricted trace-language theorem, independently audited with a separately
generated vector-heading/low-pivot certificate. Even if four-turn
loop trains before the standard backbone letters are chosen arbitrarily and
aperiodically, a finite entry board forces only finitely many detours. Seven
independent open periods give a complete-history set of143 cells; exact linear
implication propagation forces the middle period undecorated whenever those
cells were white. Each entry black cell lies in at most7 translated witness
sets, giving at most3+7m decorated backbone periods. This does not prove that
an arbitrary finite-seed orbit has the fixed-backbone decomposition.

## Resource outcomes are not mathematical exclusions

An early length24 loop-library build materialized all pairwise one-hot guards
and was killed with exit137. The exact meet-in-the-middle code now omits those
redundant guards because its Cartesian choice enumeration already enforces
one choice per insertion site. General solver time/node/recursion caps remain
UNKNOWN, not UNSAT. The versioned general length12 results and failure record
are `loop_library12_v1_results.json`, `loop_library12_v2_results.json`, and
`loop_library12_v1_failure.txt`.

## Completed additional bounded synthesis controls

The seven-site pair-substitution search through arbitrary pose loops of length32
finds no alternative:86,822 library words,2,045,408 original-read-compatible
assignments, and one valid cyclic standard front. The two-core-turn mutation
search with loop length16 finishes with484 nonzero-drift edited cores excluded
plus the unchanged standard positive control;65,344 assignments pass original
read equations and only the control passes all read guards. The four-core-turn
mutation search with loop length12 excludes35,125 nonzero-drift edited cores
plus retains the control. These are finite construction families, not global
front classification. Versioned result JSON files preserve exact scope/counts.

The separate infinite-background reverse-rail primitive test is specified in
`reverse_rail_front_criterion.md`. Complete periodic-word enumeration through28
finds only the known opposite-sector reverse sweep and its powers. There is no
same-sector reverse front within that bound; unbounded nonexistence is open.
The rail medium is infinite and is NOT a finite-support counterexample.

## All eight-step pose detours

`eight_step_detour_finite_fuel.md` expands the audited open-window theorem to
every physically feasible pose-return insertion of at most eight updates, not
just concatenated four-turn loops. The exhaustive ten-word library gives520
central options in a nine-period window. Independent implementations force514
to zero and refute the remaining six selected literals. The206 complete cells
have translation multiplicity8, yielding at most4+8m decorated periods from
a finite seed. The fixed-standard-backbone hypothesis remains essential.
The analogous length12 local relaxation is unresolved, not a counterexample.
