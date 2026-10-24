# Renewable expanding-track exploration

Protected fresh construction route, started22October2026. No counterexample,
renewable corner, or full expanding circuit has been found. This route does not
assume standard attraction and does not use the five-macro or low-mass models.

## Exact rail-shift primitive

S=RLLR from (0,0,N) reads, in order,

    (0,0) R, (1,0) L, (1,1) L, (0,1) R,

and ends at(0,2,N). Thus S^n shifts the solid black rail
{(1,y):0<=y<2n} left to {(0,y):0<=y<2n}, changing no other cells.
Its rotations shift an inside rail outward around a clockwise circuit.
This gives a potential way to manufacture the next lap's hardware, but the
corners and between-lap seam have not been made renewable.

## Initial exact finite-prefix construction family

Try lap words

    W_n = (S^n K)^4 T,

where K ends with heading east and T has displacement(-1,-1) and restores
heading north. The four rotated copies of S^n K return to the initial pose;
T moves the next lap's start one cell southwest. Replacing n by n+1 then moves
all four straight side tracks outward by one cell.

`search_spiral_caps.py` checks every physically feasible quarter-turn cap K
through13 steps and seam T through14. Of1669 caps,340 execute one whole n=5
circuit. There are73 candidate seams. All24,820 pairs contradict repeated-cell
color alternation within the fifteen attempted laps n=5,...,19. No successful
finite prefix was extrapolated. These exclusions are specific to that family;
they do not prove that every expanding racetrack is impossible.

## Isolating the remote corner from the seam

For a north-to-east corner, place the finite cap K at(0,0,N), ending(a,b,E).
Attach an incoming semi-infinite north S arm and outgoing east S arm. In an
outward-moving rectangle, this corner translates by d=(-1,+1) per lap.
The complete local read chronology is finite after quotienting by d:
physical cell classes are s=x+y, ordered by increasing x and then within-lap
phase. All classes outside the finite cap/end span are automatic RL pairs.
The explicit formula is in `exact_corner_chronology.py`; an independent-style
finite-arm implementation in `corner_chronology.py` agrees for all13,470
physically feasible quarter-turn words through17.

A finite initial black board requires every complete class to startR and
alternate: arbitrarily far translated cells were initially white. No cap
through17 passes. A further13,104 candidates formed by placing any cyclic
phase of the standard104 word before or after a cap through7 also fail.
These are local necessary tests, not a full finite-seed construction checker.

`periodic_corner_states.py` challenges the fixed-cap assumption by allowing
periodically changing caps with the same geometric endpoint. A local success
would still need a full-field, all-parameter racetrack certificate.

## Exact all-length corner budget

See `corner_black_wake_budget.md`: the two arms contribute precisely two
unmatched L reads after all automatic RL pairs are removed. Therefore any
finite-support renewable corner must have at least five more R than L in K,
and must leave at least three permanent black diagonal translation classes.
In particular a clean corner which only shifts the rail without extra corner
wake cannot renew, at any length. Complicated debris-emitting corners remain
open. This analytic observation is independently audited under its explicit
maturation/isolation premise. That count alone permitted a clean four-phase changing-state corner, but the
stronger row-parity theorem below now excludes clean renewal for every period.
The exact two-phase test covered82,037 pairs from2,650 arm-compatible caps
through17 and found no local corner; debris-emitting arbitrary caps remain open.

## Stronger clean-renewal obstruction and current boundary

`corner_row_parity_obstruction.md` strengthens the count budget by the universal
row/column visit-parity identity. It rules out a clean q-phase corner for every
q, and gives at leastq permanent black classes (q+2 whenq is odd). Under uniform
bounded cap footprints, the argument also handles aperiodic changing cap words:
every sufficiently far row of the local diagonal band retains odd black parity.
The maturation/isolation hypothesis is explicit. Independent analytic audit passed
for this stronger extension. It excludes CLEAN renewal, not renewal with debris.

The exact guarded-GF(2) changing-state synthesis in
`synthesize_corner_cycle.py` tested all82 geometric ports supplied by caps
through17, with four independent cap choices. Both clean and debris-allowed
systems were excluded, with no UNKNOWN outcomes. These bounded search outputs
have not been independently audited. The count/row-parity proofs do not depend
on those search outcomes.

`enumerate_solid_rail_shifters.py` is a separate exact primitive search: all
bounded periodic words converting one solid infinite black row into a shifted
solid row, restoring white elsewhere. It may supply alternatives to S whose
corner requirements differ. Infinite input hardware is not a finite-seed
construction; any eventual device must manufacture its own next input rail.

## Mixed W20/S shuttle: a new separated-endcap construction target

See `mixed_shuttle_architecture.md`. Westgoing W20^n followed by eastgoing
S^n moves a finite solid rail upward by four. Two renewable caps, one of
displacement(0,4) and one pose-return, would turn this into an axial
nonstandard front for every sufficiently large rail length. The bulk already
has exact white-first alternating read histories. No such caps are known.
`mixed_shuttle_caps.py` implements the two complete-history conditions;
through length16 neither cap is found. Those small searches are controls,
not the intended all-length construction argument. Exact modular charge
budgets require at least six black wake classes at EACH cap.

The independent solid-row primitive enumeration through period24 found only
cyclic powers of S (westgoing row shift -1) and the primitive W20 (shift +3).
The latter agrees with `first_principles_new/w20_rail_profile.md`. No all-period
primitive classification is claimed. A W20-based expanding NE corner also
has no cap through17 (`w20_corner_chronology.py`); that finite exclusion has
not been independently audited.
