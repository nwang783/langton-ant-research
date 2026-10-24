# Fresh construction checkpoint, 23 October 2026, 06:44 UTC

The finite-support Langton-ant highway conjecture remains OPEN. No universal
proof, counterexample, or autonomous renewable builder has been constructed.
All actions remain local. The earlier0612/0534 checkpoints retain prior scope.

## New signed positive components

`unit_scale/axial_domino_transport.md` (audit JZ) gives actual closed-pose
finite rail operators, both starting/ending(0,0,E):

* G_r=(LRRL)^r LLLR (RLLR)^r RRRL, length8r+8, black input row0 x0..2r
  plus(-1,1),(2r,1). COMPLETE XOR4: move the vertical domino atx2r to x-2.
  Input/outputmass2r+3, support4r+6. Every other field cell restores.
* H_r replaces LLLR by LRRRRLLR and omits upper far input(2r,1).
  Its seedJ_r is row0 x0..2r plus(-1,1). Length8r+12, COMPLETE XOR4 new
  black cells at(-2,0),(-2,1),(2r+1,0),(2r+1,1); mass2r+2 ->2r+6.
  It is not renewal: the new endpoint pattern changes the next caps.

Independent all-r field proofs and literal controls throughr1024 are in
`audits/check_axial_domino_independent.py/json`. These positive controls are
compatible with all earlier bounds: long axial separation is allowed, and
the prepared rod's initial mass grows.

## Exact closure of the tempting H_r seed family

`unit_scale/domino_growth_capture.md` and its JSON certificate now independently
prove that EVERY J_r with r>=20 reaches a104-period highway at time60r+777,
pose(2r+2,7,N), subsequent drift(-2,2). There are seven counted finite arms
followed by fixed caps and the infinite tail. All973 affine read families
were checked for every parameter and every future tail period by exact
Presburger current-color XOR, not a bounded simulation.

Independent no-import checker `audits/check_domino_capture_independent.py/json`
avoids all author compatibility pruning, checks946,729 ordered family pairs,
recovers2,493 nonempty prior-read relations and all973 bad sets empty. Frozen
source/output hashes are `unit_scale/domino_growth_capture_hashes.txt`.
No minimalr threshold, all endpoint phases, or arbitrary rod seed is claimed.

## Current constructive direction and processes

Four rotated axial row transfers alone cannot regenerate an expanding frame:
their alternating bulk rails remain fixed. A genuine new rail-changing bulk
operator is needed. `unit_scale/period_two_rail_conversion_filter.md` is pending
analytic audit: exact alternating-row charge gives m[(O_even-O_odd)-
(I_even-I_odd)]=0 mod4 for a period-two full interface of drift2m. In particular
creating/erasing a mixed row requires8|d. Do not fold full drift into a primitive
2-column quotient.

One justified discovery control ran H5/W3 on input odd black row1: the full
3,932,160-state graph has only the known8-turn/drift2 front, no converter.
No larger window/height scan is planned. A DIFFERENT exact drift-class SMT
converter: drift8, length32, read rows0..4, input oddrow1, output fullrows0,2
plus oddrow3. It has no backwards-window restriction, but remains a single
bounded word target. Timeout/UNSAT is not a general exclusion. Artifacts:
`probe_mixed_rail_converter.py`, `mixed_rail_converter_n32.smt2/json/log`.
Inspect process/result before rerunning; do not blindly increase the bound.

The new bridge analysis has a separately frozen
multi-read macro-base extension of the signed flat exact solver. It derives
G/H all-depth fields/fuel directly from C->A C B and transientrootg->A C B D,
without falsely subdividing multi-readC into unit-pose states. It is pending
audit and covers exact remote-interface comparisons.

The positive capped operators and the now-signed capture closure are retained. The classification analysis received the row-charge source for
its separate full-period-four white-front pruning; its profile period is4,
not the period-two converter target here.
