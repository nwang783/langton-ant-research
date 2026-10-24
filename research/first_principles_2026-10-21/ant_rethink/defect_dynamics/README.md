# Defect dynamics: exact checks, failed ranks, and return scars

## Status

This branch has not proved the full finite-support highway conjecture. It
has not found a counterexample or proved undecidability. Its completed work
is an independently reconstructed scattering audit, exact finite-support
capture checks for a specific return family and its source corrections,
and explicit counterexamples to proposed boundary budgets.

The conjecture's truth is not inferred from these finite cases. No timeout
is counted as either capture or exclusion.

The later all-size exclusion of the literal expanding four-corner endpoint
model is in `four_corner_family_exclusion.md`. It proves that no B_n can
return to any B_m at the model's stated ant pose. All n>=21 follow the blank
trajectory with four unread cells; complete exact tail certificates handle
the finite remaining parameters. This does not cover arbitrary four-cell
patterns.

## 1. First-marker scattering and the exceptional reversal

 Its headings are N,E,S,W; white
turns right and black turns left. The reference drift is (-2,-2).

There are 22 physical first-visit phases in one two-sided highway period:

    13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89.

For each phase, the code changes its fresh white cell to black at canonical
age 50. It finds a standard suffix, proves that entire suffix using the
finite-ray parity check described below, and checks that its finite prefix
and infinite suffix avoid every additional older wake cell. Thus these
responses apply to every older canonical age >=50, with the same local
coordinate normalization.

The direction counts are nine SW, seven NW, five SE, and one NE. Phase 72
is the only reversal. Its checked recovery is 51,272 updates. Relative to
the impacted cell, the recovered pose is (44,-24). The incoming strip is
x-y in [-3,7] and the outgoing strip is [67,77]: reversal moves to a parallel
lane with transverse shift +70. The recovery word contains 27,024
nonstandard ten-letter windows wholly inside that recovery word.

`first_marker_scattering.json` contains all 22 results and the all-older-age
guards. The check also verifies the canonical seed, its one-period 12-cell
deposit, and the deposit's disjoint translation classes. It does not assume
that a finite number of repeated periods establishes a highway.

This is an independent reconstruction of a subcase of existing canonical
one-bit stability. It is not a new unrestricted one-black-cell theorem.
The sources include Ke's `canonical-highway-one-bit-stability.md` and his
guarded scattering/renewal note, together with the more recent unrestricted
two-black-cell theorem in `imfinn/langton-two-black`.

### Exact infinite-tail check

Let B be the complete finite black set at a candidate suffix start, and R
the 104-cell read list, with multiplicity allowed. Simulating once gives
black set B1, the same heading, standard turn word, and drift d. Put

    D = B1 XOR (B+d).

If D misses every future read ray R+k*d for k>=1, then the same standard
word repeats forever. Indeed the board at period j is

    (B+j*d) XOR XOR_{i=0}^{j-1}(D+i*d).

The discrepancy terms miss all reads of period j. This gives an induction
on j. The code checks the ray condition by exact integer translation classes
and longitudinal thresholds. All old black cells remain in B.

## 2. Two phase-72 markers do return to the old lane

`double_reversal.py` installs both marker cells at time zero on the canonical
13-cell seed. With parameters N,n, their coordinates are

    q1=(-2N-2,-2N-8),
    q2=(2(n-N)+43,2(n-N)-25).

Two phase-72 reversal offsets cancel, which makes the second returned
highway meet the original lane. This is a real return to prior writes.

All 14 parameter pairs retained in `double_reversal_results.jsonl` reached
an exactly certified NW suffix. They are:

    (50,50),(50,100),(50,200),(50,400),
    (100,50),(100,100),(100,200),
    (200,100),(200,200),(200,400),
    (400,200),(400,400),(400,800),(800,400).

The three observed nonstandard-factor totals were 53,862, 54,892, and
55,233, depending on the source/return geometry. These are records for the
listed inputs, not an all-parameter classification. No autonomous renewed
shuttle is present in any of these exact captured trajectories.

## 3. A targeted correction of the source collision

The case N=50,n=100 has markers

    q1=(-102,-108), q2=(143,75).

It first reads those markers at updates 5,272 and 66,998. After both
canonical reversal responses, it returns to the original source. The
nonstandard-factor interval associated with that source collision has
window endpoints from 123,301 through 125,414. The unmodified case has a
certified NW tail by update 125,424.

`source_correction_probe.py` considers every initially white cell first read
during updates 123,291 through 125,414 of that source collision, within
radius 45 of the source. There are 359 such cells; all have radius <=20.
Each candidate is preinstalled black at time zero, so the two earlier
reversal responses remain unchanged. The complete physical board is then
retained throughout the continuation.

All 359 cases have exact infinite-tail certificates:

| Final direction | Cases |
|---|---:|
| NW (-2,2) | 220 |
| SE (2,-2) | 112 |
| SW (-2,-2) | 16 |
| NE (2,2) | 11 |

The longest checked response after reading the correction is 88,296
updates. These certificates establish capture for this finite inventory;
they do not cover corrections at arbitrary cells or with several cells.

Five corrections cause a later physical revisit to q1, and one causes a
later physical revisit to q2:

| Correction | Returned gate | Visits after correction | Certified exit |
|---|---|---:|---|
| (4,-5) | q1 | 3 | SW |
| (1,5) | q1 | 1 | SW |
| (-4,6) | q1 | 1 | SE |
| (-1,10) | q1 | 1 | SW |
| (-3,15) | q1 | 1 | SW |
| (-7,16) | q2 | 3 | NE |

`audit_source_correction_returns.py` independently replays these six cases
from their complete 16-black-cell initial boards, rather than using the
probe's saved checkpoints. It verifies the same infinite tails.

The original canonical response reads 4,391 distinct physical cells. At
the returns with the same heading and a black gate cell, 2,248–2,264 of
those cells have a different color from their original incoming state.
The other return cases also have the opposite heading. A restored black
marker bit therefore does not restore the original scattering control.
These comparisons explain why direct reapplication of the original macro
would be invalid. They do not rule out a different controller or a more
general construction.

The primary results are `source_correction_probe.jsonl` and
`source_correction_return_audit.json`. A preliminary broader scan was stopped
after 118 completed captures when its inventory was found to include clean
incoming transport; its partial file is not treated as completed coverage.

## 4. The standard-subtracted boundary rank fails

For a completed two-row fresh cap, let T be x+y=0, A be x+y=-1, M the
number of visited T cells, and Delta_A the change in A's black count. The
known exact identity is

    N_A = 4M-Delta_A.

A natural quotient of standard tangent transport is

    Phi = 2N_A-7M = M-2Delta_A,

because one standard tangent period contributes (M,N_A,Delta_A)=(2,7,1).
This removes the unbounded linear term in the previously found delayed
five-black family. It does not have the proposed budget Phi<=2m+1, where m
is the total number of initially black cells.

### First exact counterexample

- Start at (0,-13), facing south.
- The only black cell is (2,-29).
- Run 7,849 updates.
- End at (1,-5), facing west.
- The path never has x+y>0.
- M=8, N_A=30, Delta_A=2, hence Phi=4>2*1+1.

The final top cells have x coordinates 3,4,5,6,7,9,10,11. The only final
black A cells are (2,-3) and (11,-12). The excursion starts and ends at
levels <=-4. All four cap rows were initially white.

The retained file `quotient_charge_counterexample.json` contains the full
turn word and setup. `replay_quotient_counterexamples.py` is an independent
direct simulator without any search pruning or highway detector. It
checks the word, cap condition, visit counts, and the known B/C accounting
identities. Here D=4, K_C=7, Z=1, with row visits (8,30,42,46) from T to C.

### A single top run also has positive excess

- Start at (0,-122), facing east.
- The only black cell is (-5,-111).
- Run 72,218 updates.
- End at (59,-63), facing west.
- The path stays at x+y<=0.
- M=4, N_A=16, Delta_A=0, so Phi=4.

The top visits occur in spatial order 64,63,62,61. They form one consecutive
top run. The five adjacent A cells have visit counts 2,4,4,4,2 and all finish
white. Thus a proposed bound Phi<=2 times the number of top runs also fails.
This does not contradict the established prohibition on four top visits in
increasing spatial order.

Both counterexamples are in `quotient_counterexample_replays.json`. The
second corresponds to initial black (-11,-5), origin N-start, after a
quarter-turn and translation.

### Exact top-run accounting

If the finite visited top set has c consecutive runs, then exactly M+c
physical A cells are visited: the A cells adjacent to those top cells.
Let E be the number of those A cells ending white. Since A is initially
white,

    Delta_A = M+c-E,
    Phi = 2E-M-2c.

This is an exact geometric reformulation, not a bound. Controlling E is
precisely the missing part. The second counterexample has c=1 and E=5.
Neither the number of initial black cells with the proposed coefficient
nor a simple top-run endpoint correction supplies that control.

### Finite exploratory scope

The counterexamples were found while scanning 1,804 one-black seeds, at
the distinct cells first read by the blank origin N-start in its first
12,000 updates. Each seed ran 200,000 updates, with all four cap orientations
tracked. The maximum observed Phi was 4. This finite maximum is not a
universal bound. The already known unrestricted one- and two-black capture
theorems make a further capture scan of these seeds unnecessary.

`cap_quotient.cpp` additionally contains a finite exact turn-word enumerator.
Its records are finite-depth checks only. They are not used to establish
any unbounded claim.

## 5. A sound transport quotient, without a termination claim

`transport_quotient_lemma.md` proves an elementary fact: inserting a
standard 104-letter period at matching phase preserves the ordered
sequence of nonstandard ten-letter windows. In physical corridor families,
the corridor transport theorem justifies such insertions, with all old
writes retained.

The two-black-cell paper uses this type of transport to extend already
certified one- and two-corridor base members to all corridor lengths. Its
proof and coverage are substantial prior work. The transported collision
word still has to terminate at the checked base, so corridor length alone
is not a new well-founded measure on arbitrary scar interactions.

## Source and priority boundary

A later direct periodic-word route is recorded in
`direct_periodic_chronology.md` and `periodic_word_smt.py`. The exact
leading-first parity criterion was proved equivalent to finite-support
realizability, with an explicit finite seed. The standard104 positive
control passed, while axial P52 and P104 searches timed out and remain
UNKNOWN. No alternative highway was found. The local solver dependency
directory is excluded from the research artifact.

The inspected primary sources include:

- [Ke's canonical one-bit stability note](https://github.com/kehao95/langtons-ant-core/blob/main/highway_stability/proof/canonical-highway-one-bit-stability.md).
- [Ke's ten-factor language note](https://github.com/kehao95/langtons-ant-core/blob/main/factor_language/proof/ten.md).
- [Ke's mass note](https://github.com/kehao95/langtons-ant-core/blob/main/factor_language/proof/mass.md).
- [The revised two-black-cell manuscript](https://github.com/imfinn/langton-two-black/blob/main/paper/TWO_BLACK_CELLS_REVISED.md), draft revision 5, dated 5 October 2026. Its statement covers arbitrary placements with at most two initial black cells; it explicitly leaves the general finite-support conjecture open.
- The prior session's fresh-cap diamond, third-row charge, and visit-order notes,
  retained in `ant_global/foundations` and the earlier phase2 workspace.

The local finite checks here are not a proof-assistant verification or an
external review. No novelty or priority claim is made for the source
theorems, the canonical scattering responses, or the elementary word lemma.
The exact new counterexamples are counterexamples to attempted ranks, not
counterexamples to the highway conjecture.
