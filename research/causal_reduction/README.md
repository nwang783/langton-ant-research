# Edge-token causal reduction, 22 October 2026

## Current proof status

The finite-seed highway conjecture is NOT proved. This work supplies an exact finite-root causal forest, and a finite all-epoch arithmetic certificate identifying the standard highway's causal forest. It also records where this formulation does not supply a decreasing rank.

The useful new structural observation is that the standard highway has exactly **two** infinite token-ancestry spines. Each spine is a straight Tait-lattice ray. Its producers are all degree-zero arrivals (`r=4`), and its successor is always the second inserted edge, later consumed away from its writer. Non-spine cursor-node bushes have depth at most six; including terminal buds, maximum depth is seven. This is proved for the known standard word, not for arbitrary finite seeds.

Files:
- `root_reactivation.md`: an all-parameter colored extension of the inherited twenty-cell family; one root is dormant for an unbounded interval, then supplies both final infinite standard spines.
- `forest_theorem.md`: precise all-input forest, the productive-ray obstruction, and explicit limits.
- `causal_strip_corollary.md`: finite strip-confined ancestry spines plus uniformly bounded finite bushes force eventual translating periodicity, using the inherited strip theorem.
- `standard_forest.md`: exact all-future standard-kernel theorem and arithmetic coverage proof.
- `certify_standard_forest.py`: independent finite checker, importing only the literal W104 input, no ant simulator.
- `standard_forest_certificate.json`: generated exact phase/lifetime/parent data.
- `ancestry.py`, `blank_ancestry.json`: independently implemented physical replay used to discover the structure. Its sampled tail is not the all-future proof.

## Existing obstructions read first

The inherited `memory_feedback/proof/remote-stale-feedback.md` already proves that a non-eventually-translating orbit must consume late-born, remote, arbitrarily old black lifetimes. The inherited `factor_language/proof/silent-archive-amplification.md` already disproves a J10-event-only last-writer genealogy: J10-free episodes manufacture arbitrarily many later-J10 lifetimes, after all initial lifetimes have been consumed. The new forest retains every insertion, including these silent writes. It does not pretend the number of initial black cells is a budget on descendants.

The Tait cursor reformulation is inherited from `first_principles_2026-10-21/ant_rethink/switching_geometry/tait_cursor_and_loop_surgery.md`. The forest and its standard two-spine decomposition are the present work. No priority claim or external peer review is asserted.

## Next exact gap

A possible global target is an exclusion of a nonstandard productive infinite ray in the edge-token forest, with its complete side branches retained. The canonical allowed renewal is now explicit. There is no proof yet that productive rays straighten, that the forest has at most two ends, or that its nonstandard bushes have bounded size or occur finitely often. Those are questions, not consequences of finite roots.

## New macro-genealogy constraints

- `cvb_bounded_ancestry.md` and `certify_cvb_ancestry.py`: cut forest depth at most eight for every feasible C/V/B interval, sharp at CCCVV. Independent audit passed.
- `probe_full_phase6_patch.py`: exact local closure extends the common phase-5 producer restriction and C11 separator lemma to the full five-macro language. No exit-freshness claim.

### Common-star correction and simplification
The full-five common-star certificate passed independent audit, but its conclusion is built into the literal seam. `macro_seam_identity.md` gives the stronger immediate-predecessor proof in six read positions. This is an elementary identity, not a new global theorem. The C/V/B height-eight theorem remains audited and nontrivial. Joined-patch terminal-renewal tests remain inconclusive.

### Sharper C/V/B component count
`cvb_component_bound.md` derives a sharp bound of 36 vertices, including boundary buds, per cut-forest component. It uses audited fresh-V and short-word facts plus literal seam structure; independent analytic audit and literal controls passed. `cvb_component_size_controls.json` supplies finite controls through eight macros.

### Completed-call and symbolic refinements, before protected exploration switch
- `completed_module_causal_bound.md`: analytic all-length proof that completed G/B calls have cut-forest components at most9 and bud-depth at most3, independent of finger length; audit requested. Controls cover both finger lengths through100. This does not bound global components after later calls reuse stored tokens.
- `exit_coset_blocks.md`: each non-C macro exit coset has exactly the L,R,L block (the last L is next-macro phase3), with no later occurrence in the concatenation. Physical-site freshness remains open.
- `audits/five_macro_autonomous_universality.md`: independently reviewed negative result by the audit analysis: EVERY raw five-macro concatenation is legal in the autonomous coset model. Thus its universal lift properties impose no additional restriction on that macro syntax.
- `probe_v_three_input_fuel.py`: three prior-read flags and exact77-state port grammar; the14-cell V footprint gives an abstract all-stale witness. The20-cell union of three3x3 neighborhoods reached500k live BDD nodes, inconclusive. These are conservative abstraction diagnostics, not physical counterexamples.
- `search_repeated_macro_starts.cpp`:20m exact feasible prefixes with depth ceiling16 found no repeated actual macro-start pose, but the search was truncated and proves no universal statement. The weaker boundary-pose version is false at CVVCCVVC; its return boundary cannot execute another macro.

 `front_surgery/` now investigates exact periodic-front construction and possible nonstandard highways, independently of the five-macro, low-mass, and lifted-module restrictions. Existing results are preserved above for the analyses pushing those routes.


## Current protected exploration: renewable axial shuttles

`renewable_tracks/mixed_shuttle_architecture.md` gives an independently audited
conditional construction of a nonstandard axial front from W20 and RLLR rail
shifters plus two complete renewable caps. Each cap must leave at least6 black
wake classes, hence total growth at least12. No cap pair has been found.

`renewable_tracks/height4_right_cap_obstruction.md` independently excludes a
fixed right cap confined to rows0..4 at every width/duration. Its audited
companion shows every fixed vertically renewed right cap must span at least
six integer row levels. This does not automatically cover mixed-height phases.

`renewable_tracks/two_row_transfer_interface.md` defines the next surviving
six-row geometry as an exact partial word map, allowing debris and growing
boundary fuel. `renewable_tracks/six_row_polarity_obstruction.md` now proves all-width
non-composability by an independently audited first-black-bit parity mismatch.
It applies to fixed or changing caps in the common[-1,4] strip with complete
isolated arms. The stronger prefix invariant is still unproved and unnecessary.
Explicit upper-strip port counterexamples show why the actual lower relay
must be retained; a top-boundary-only prefix argument is false.

## Protected exploration update: exact inflation countermodels (22 October,19:54 UTC)

The fresh route now seeks genuinely aperiodic, self-similar finite-seed paths,
not further bounded-cap optimization. No countermodel has been found.

- `morphic_candidates/complementary_root_exclusion.md`: independently audited
  exclusion of all1,241,057 additional rooted two-letter geometric substitutions
  through odd image length17. This includes L-prolongable roots and both phases
  of first-letter two-cycles. Two length17 survivors of finite simulation are
  excluded exactly by Gaussian-sublattice first-L replication, not by horizon.
- `morphic_candidates/pure_small_inflation_obstruction.md` and
  `macro_ownership_fuel.md`: independently audited obstruction to ANY pure
  p(kn)=a*p(n),h(kn)=h(n) finite-seed inflation for2<=k<=8, with no finite-control
  assumption. A private/forward-owned first-L cell charges genuinely fresh
  coarse visits/outward records to distinct initial black cells. At k9 only
  a=3 remains after complete image, prefix-tree and ownership checks.
- `morphic_candidates/k9_record_normal_form.md`: review requested. In that
  remaining scale, every sufficiently high first outer record tau(Y) obeys
  tau(3Y)=9*tau(Y), with the unique18-turn refinement
  RRLRRRRLR / RLRLLLLRL. This is a renewable behind-frontier pattern, not an
  exclusion. The five-pair and four-top-image geometry is explicitly asserted
  in `check_k9_record_pattern.py`.
- Multi-symbol candidate synthesis is active. Exact local regular constraints
  in `free_inflation_generic_csp.py` find finite81-turn refinements but have
  UNKNOWN capped deeper cases. No finite-prefix survivor is a counterexample.
  `search_palette_inflations.py` already exhausts every fixed image palette of
  total size<=7, even with arbitrary occurrence-by-occurrence choices. This
  finite search extension has not yet been independently audited. The full
  nine-plus-nine palette is running at a bounded node cap; any cap stays UNKNOWN.
- Heading/time-residue/digit controllers also fail by explicit chronology;
  several of those larger enumerations are superseded by the smaller palette
  argument. `renormalize_macro_grammar.py` gives a NEGATIVE METHOD CONTROL:
  the tested order2,3,4 necessary grammars do not shrink under one-step
  renormalization. This is not a proof that a globally compatible refinement
  exists, only that this specific finite relaxation adds no restriction.

The earlier controlled-strip endpoint resets and half-arm certificates are
preserved under `controlled_strip/`; no renewable endpoint cycle was found.
Informal H12/H13 pristine-width observations have no saved witness and are
NOT established. The audited height9 barrier remains the valid reference.

### Exact k9 refinement closure (22 October, 20:32 UTC)

The sole remaining pure position-and-heading inflation scale k9,a=3 is now
independently computer-assisted excluded on ANY initial coloring: all 1,280
self-consistent coarse81 prefixes have no feasible729 refinement. Independent
encoding and positive controls pass. See morphic_candidates/k9_exact_refinement_exclusion.md.
All 1,280 explicit CNFs now also have separately checked monotone-RUP proofs
through the final empty clause: 102,992 additions, maximum828 per case, zero RAT
steps/deletions/UNKNOWNs. The hash-bound final manifest is
morphic_candidates/k9_rup/manifest.json. A complete independent replay reconstructed
every CNF and checked every proof using a different occurrence-count propagator;
see audits/check_k9_rup_independent.json. Together with prior scales and even-k
heading parity, the finite-seed pure-inflation exclusion extends through k=10.

### Broader position-only exploration (22 October, 20:32 UTC)

Dropping h(kn)=h(n) gives a genuinely larger candidate class. The new
morphic_candidates/position_only_small_exclusion.md excludes finite-seed pure
position-only inflation for2<=k<=5 by exact short prefix trees and a two-phase
forward-owner fuel lemma. The phase normalization and every owner set have been
independently replayed; all nine short EXHAUSTED trees have now also passed
independent no-cutoff replay.
Critical-area cases k8,a=2±2i and k9,a=3 remain open after100,000-node searches
(reaching36,39,85 macros, respectively). All are UNKNOWN, not countermodels or
exclusions. Their images include unprotected first-L sites, so the earlier
heading-preserving result cannot simply be transferred.

### Checkerboard-specific fuel (22 October, 20:48 UTC)

checkerboard_turn_fuel.md gives a new all-length physical-turn normal form: an
interval whose pair-first turns are all R has at most3 pair-second R turns and
at most m_odd+3 pairs. It implies at least(N-m_odd-6)/8 first-position L turns
in any N pairs, hence positive L/revisit density on each checkerboard. The normal form, sharp local bound, and global density claim passed independent
analytic and literal audit; it is not a highway theorem.

### Heading-free critical-area k8 (22 October, 20:56 UTC)

All2,784 exact k8,a=2+2i coarse64 roots have no512 refinement in the direct solver,
zero UNKNOWN. Position/head boundary bits remain free subject to continuity.
Independent audit is requested, and the monotone-RUP batch is running. See
morphic_candidates/position_only_k8_critical_exclusion.md. The k9 heading-free
class remains open: one literal765-turn survivor exists from230 initial black
cells, but its particular6561-turn refinement is UNSAT. This is not an exclusion
of all729-turn alternatives.

### Heading-free scale-nine record exclusion (22 October, 21:14 UTC)

The preceding open status for k9,a=3 is superseded by
morphic_candidates/position_only_k9_record_exclusion.md. No finite-support ant
can satisfy p(9n)=3p(n), without any heading condition or finite-controller
assumption. Pristine coordinate records force a unique nine-turn prefix; two
successive scales would require an impossible 81-turn refinement. All six local
record pairs and the complete 635-node refinement tree pass independent analytic
and exact replay in computability/check_position_k9_record_independent.py/json.
This is a finite-support theorem, not an arbitrary-background exclusion.

Finite-controller controls also exclude the four-rule and two-private-state
heading-phase controller families on arbitrary backgrounds. The three-state
search is capped and inconclusive. These controls are superseded for finite
support by the new record theorem, but their arbitrary-background scope differs.

### Heading-free critical-area k8 finalized (22 October, 21:39 UTC)

The pending k8 status above is superseded: every one of the 2,784 refinements
has a fully independent original-CNF reconstruction and monotone-RUP replay.
The separate checker verifies all 42,696 additions and every final empty clause,
without trusting a SAT solver. Thus pure position-only scale 2±2i at radix8
is impossible on any initial coloring, already at512 turns. The narrower
finite-support scale3/radix9 result also has independent analytic signoff.

### Eventual affine ninefold exclusion (22 October, 21:48 UTC)

The fresh-record argument now independently excludes every eventual relation
p(9n+c)=a p(n)+b for integer offsets and a in {±3,±3i}, with finite support.
The proof retains the time phase, clears both finite exceptional prefixes, and
uses separately rotated frames. See morphic_candidates/eventual_affine_k9_exclusion.md.
This does NOT extend every earlier small pure-inflation exclusion to arbitrary
affine phases: radix7/scale3 with odd time phase is a genuinely new open class.

### Current fresh-exploration checkpoint (22 October,22:30UTC)

The immediately preceding radix7 affine-phase open status has since been closed
by the computability analysis's independently audited forward-ownership argument.
See computability/affine_seven_owner_probe.json and its current extension notes;
this does not automatically close arbitrary affine radix8/diagonal-scale phases.

The same-direction, same-sector A12/B28 bulk inverse pair is independently
checked. It restores an alternating two-row catalyst while moving a solid rail
up and back down. periodic_port_builders/same_sector_12_28_bulk.md gives exact
stable profiles and an all-n EXTERNALLY RESET finite composition. No reset cap
or autonomous renewable mechanism exists here. Complete fixed-port restoration
must obey the newer single-window and one-sided-CPU obstructions.

A proposed height-ten white-input wake was WITHDRAWN: its column charge was0,
but a translating front crossing a column must leave charge2 modulo4. That
error affected only a speculative search target and its inconclusive timeouts,
not the checked nonwhite bulk identities or returning-half-builder filters.
The correction is explicit in periodic_port_builders/README.md and the general
alternating_row_charges_mod4.md source.

The inward-spiral countermodel search now has an independently audited exact all-n capture
certificate, in spiral_endpoint/README.md. For n>=11
the core analysis's11n+2-cell family enters standard104 by time8n^2+36n+3021.
A solver-free affine-incidence arrangement reduces all n and the infinite tail
to39 finite representatives, not a horizon extrapolation. This is a scoped
family result and reusable verification method, not a global capture proof.

A small elementary two-column frontier obstruction is recorded separately:
periodic_port_builders/two_column_fresh_front.md. No right-escaping finite-support
ant can eventually remain in only its newest column and predecessor, regardless
of vertical height. It is a direct ladder calculation, not a major new invariant.

The independent spiral continuation checker rebuilt all geometry and the full
incidence arrangement, rather than importing the source reduction. It reproduces
all395,343 representative reads and proves the infinite tail. The original
11n+2-cell seed needs no extra completion cells. Independent files:
audits/check_spiral_affine_continuation_independent.py/json.

### Fresh construction checkpoint, 23 October09:01UTC

See fresh_checkpoint_2026-10-23_0901.md for the current state. New signed
positive controls include a33-black delayed orthogonal104 corner and a43-black
arbitrarily large closed-pose excursion. Their markers are consumed, and the
unmodified43-cell family has a separately signed two-contact capture proof.
No renewal or counterexample is inferred. A shifted exact-reversal104 bulk
cannot reuse its own forward wake in the same pose sector with finite end
repairs; different prepared return mechanisms remain open.
