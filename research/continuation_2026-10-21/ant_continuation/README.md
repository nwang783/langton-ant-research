# Langton's ant research continuation — 21 October 2026

## Status

The general finite-seed highway conjecture is **not proved or disproved** by
this work. This is a reproducible research continuation, with analytic lemmas,
finite exact certificates, failed approaches, and explicitly open obligations.
No publication-priority or external peer-review claim is made.

Read STATUS.md for the final result of this continuation and the exact remaining
obligations. The included Word report gives the statements and proof outlines.

## Model

The grid is Z^2. North is (0,1), east is (1,0). A white cell turns the ant
right; a black cell turns it left. It then flips the cell and moves one unit.
Headings N,E,S,W are encoded 0,1,2,3. All finite simulation checks retain the
entire black set. A standard tail means a cyclic phase of the known 104-letter
word, with a nonzero diagonal drift, certified for every future update.

## Main results and their limits

1. `wake_clock/proof_notes.md`: an analytic equality between the convex hull
   of an entire finite path and the convex hull of its odd-read cells and its
   two endpoints. It also proves an all-future mass/width cost using two
   monotone clocks. Neither result bounds the growth of a hypothetical
   counterexample's support.
2. `global_structure/retreat_area.md`: an analytic finite-state bound. A
   nontranslating-periodic orbit needs retreat area at least
   log_2(T)-O(log log T). No upper bound on retreat is proved.
3. `one_bit_certificate_restored.json`: a new reconstruction of the missing
   739-leaf certificate for an existing canonical-highway one-bit stability
   claim. It has independent C++ and Python audits. This repairs evidence
   for that restricted theorem; it is not a proof for arbitrary finite seeds.
4. `wake_clock/corner_blocks_proof.md`: an all-scale, computer-assisted
   recovery theorem for the specific 16-cell square-corner family in the note.
   Fourteen affine guards cover all n>=34; 462 exact leaves cover 1<=n<34.
5. `factor_language/isolated_last_event_theorem.md`: a finite exact language
   check plus Ke's conditional attraction theorem shows that a last forbidden
   ten-window event must immediately follow another event. Infinitely many
   isolated events are not ruled out by this lemma.
6. `global_structure/two_black_clock_obstruction.md` and
   `global_structure/radial_clock_obstruction.md`: algebraic candidate
   endpoints pass several known necessary invariants with only two black
   cells. They have NOT been shown reachable. This records a limit of the
   proposed endpoint-only proof method, not a dynamical counterexample.

7. `factor_language/five_macro_status.md`: an exact reduction of the
   no-adjacent-forbidden-event language to five blocks, with a proved fuel
   formula for every aperiodic mixture of the two straight blocks. The
   infinite turning-block case remains open.
8. `wake_clock/four_scatterer_loop_proof.md`: the specified geometrically
   closed circuit first disagrees with the real ant at exactly 416L+37740,
   for every integer L>=128. This does not prove escape for every L.
9. `wake_clock/fold_farkas_proof.md`: an exact integer certificate excludes
   the specified ordinary nonnegative 3x3 pattern energy plus history
   potential. Sector and head-corrected extensions only have numerical
   infeasibility reports, not exact exclusion certificates.

## Important distinction

A simulation that happens to show several highway periods is not an infinite
certificate. `ant_exact.certify_period` instead checks every possible initial
field intersection and every prior-write threshold on each infinite phase ray.
A finite set of parity breakpoints then proves all future reads by induction.
The proof of this criterion is supplied in the report and the corner-block note.

## Reproduce the main checks

Core proof checkers use the Python standard library. The independent verifier
requires a C++17 compiler. Exploratory energy optimization uses NumPy and SciPy;
its exact integer Farkas verifier does not. Rebuilding the optional Word report
requires Pandoc, python-docx, and Matplotlib. Run commands from this directory unless stated otherwise.

    python3 audit_reference.py
    python3 restore_one_bit_certificate.py
    g++ -O3 -std=c++17 verify_one_bit_independent.cpp -o /tmp/ant_one_bit_verify
    /tmp/ant_one_bit_verify one_bit_records.tsv
    python3 factor_language/audit_parent_one_bit.py
    python3 wake_clock/check.py
    python3 global_structure/audit_retreat_automaton.py

For the corner-block family, run from `wake_clock/`:

    python3 single_blocks.py
    python3 certify_corner_blocks.py
    python3 check_small_corner_blocks.py
    python3 audit_corner_blocks.py
    python3 certify_four_scatterer_prefix.py
    python3 verify_fold_farkas.py

For the exact isolated-event language lemma, run from `factor_language/`:

    python3 one_defect_exit.py 10
    python3 isolated_defect.py --pre 10 --post 149
    g++ -O3 -std=c++17 check_one_defect.cpp -o /tmp/ant_one_defect
    /tmp/ant_one_defect cpp_isolated_words.txt

For the five-block coverage and its geometric exclusions, run from
`factor_language/` using the included graph and certificate inputs:

    python3 verify_five_macros.py
    python3 build_macro_footprints.py
    python3 verify_uv_fuel.py
    python3 verify_t24.py

The exact radial-clock control can be rerun from this directory:

    python3 global_structure/check_radial_clock_obstruction.py

Some language-search scripts are exploratory. Bounded searches and their logs
must not be used as universal conclusions. Each proof note states its actual
scope and dependencies. A construction cap is only a search limit: successful
leaves are justified by their exact certificates, not by the cap itself.

## Sources

 The primary external source is Hao Ke's repository
`https://github.com/kehao95/langtons-ant-core`, inspected at commit
`22e0c9edcc566a4c2f7a9bf92f5cd05c19199617`. The hull argument extends the
corner argument in K. R. Etse, *How Long Can the Escaping Ant Be Confined?*,
Proposition 2, MFCS 2026, DOI `10.4230/LIPIcs.MFCS.2026.49`.

SOURCES.json records pinned links and hashes for the external reference notes.
The archive does not redistribute their complete prose. Exact mathematical
input words and finite certificates needed by the checkers are included.
No external source claim is silently substituted for a new proof.
