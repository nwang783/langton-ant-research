# Finite fuel for all pose-return detours of at most eight updates

Status: exact computer-assisted local certificate, independently audited with
a separate vector-heading/low-pivot implementation. Audit artifacts:
`audits/check_eight_step_detours_independent.py` and
`audits/eight_step_detours_independent.json`.
This strictly expands the preceding four-turn-loop-train language, but still
assumes the standard geometric backbone. It is not a global attraction proof.

At every letter of the standard104 backbone, allow either no insertion or
any physically feasible pose-returning turn word of length at most eight,
then execute that backbone letter. Choices can vary arbitrarily between
periods; no periodicity or eventual regularity of choices is assumed.

THEOREM: From an entry board with m black cells at a full W boundary, at most
4+8m backbone periods contain any insertion. Thus the actual trace is eventually
exactly W repeated. At most104(4+8m) backbone letters are decorated, and at most
832(4+8m) extra physical updates occur. A finite prelude or cyclic phase is
allowed by rebasing to a full boundary and using the black mass there.

## Exhaustive short insertion library

Direct enumeration of every binary word of lengths1 through8, checking exact
pose return and alternating reads at every repeated physical cell, gives
exactly these ten words:

    RRRR, LLLL,
    RRRRLLLL, RRRLLLLR, RRLLLLRR, RLLLLRRR,
    LRRRRLLL, LLRRRRLL, LLLRRRRL, LLLLRRRR.

Each is possible from an appropriate finite board because its first-read
colors determine a consistent finite seed. Before backbone letter c, its last
read at the entry cell must be opposite(c). This leaves five options at each
backbone phase, in addition to no insertion. The guard is necessary and exact;
all other compatibility constraints remain in the window system.

## Nine-period open-window certificate

Use periods -4,...,4, with independent option variables. There are4680 variables,
520 in the central period. All potential read positions determine206 physical
cells whose ENTIRE possible read history lies in this open window. Keep only
constraints at those cells and allow arbitrary fields outside them.

The white-first-read/alternating-read equations and guarded equations are
constructed exactly as in `four_loop_detour_finite_fuel.md`. There are663
unconditional original-read equations. Gaussian implication closure forces514
of the520 central options to zero. For each of the remaining six, assume that
option is selected and perform the same sound implication closure. Each
assumption gives a contradiction, so those six options are also impossible.
There is no general SAT-solver call or unresolved search cap.

The certificate code independently enumerates the ten words, asserts every
claimed result before writing its JSON, and checks that zero options satisfy
the original equations. Files:

- `certify_eight_step_detours.py`
- `eight_step_detour_certificate.json`
- `window_library_rigidity.py` (open-window geometry/constraint generator)

The six failed literals are the conjugated loops at phases32,44,59 and their
paired eight-letter loops at phases33,45,60. All option variables are distinct
between periods; no identification with a periodically repeated choice is made.

## Finite-seed conclusion

Let F be the206 complete-history cells. If period n>=4 is decorated, F+n*d
must contain an entry-time black cell: otherwise all those cells begin their
complete read histories white and the central-window exclusion applies.
The largest translation class in F has8 cells, explicitly checked. Therefore
each entry black cell can spoil at most8 translated windows. At most8m late
periods are decorated, and the first four periods add at most4. The time of
the last detour is not bounded by m, since seed cells can lie arbitrarily far
along the corridor.

## Boundary of the result

The same simple implication closure does not settle the library through12.
With a nine-period window,1415 central options remain unresolved; already one
forced-option probe survives closure. This is an inconclusive local relaxation,
not a physical alternative front and not evidence that the theorem extends.
The full finite-support conjecture also does not supply the fixed standard
backbone hypothesis used throughout this note.
