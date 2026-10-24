# V-tip freshness across one arbitrary mixed fold

Status: independently analytically audited and reproduced by a separate literal
complex-heading implementation: 112 states, 206 edges, no hit. See
`../audits/check_one_fold_sweep_independent.py` and its JSON output.

## Claimed statement

Let X F Y be a physically feasible macro word, with X,Y arbitrary finite
words over U,V and F in {Q,B}. Every V-tip (local (1,2) at the V entry pose)
is unread earlier in this entire word. This marked cell has its first L read
at V phase 13 (zero based), and its last R read at phase 17. Tips within X are already fresh by
the exact mixed-run geometry. The new certificate addresses tips in Y,
including possible old reads in X, F, or earlier Y.

The scope is one fold only, with no C blocks. No assertion is made about
multiple folds, earlier history before X, or the full highway conjecture.

## Exact two-frontier construction

Fix the fold entry at (0,0,N). Construct X backward by prepending U/V blocks
and Y forward by appending U/V blocks after F. Every finite X F Y can be
constructed this way, in any interleaving of these two operations. Physical
feasibility is equivalent to alternating consecutive read letters at each
cell. Thus a prepended block is checked in reverse read order against the
current earliest read; an appended block is checked in forward order
against the current latest read. Maintain both earliest and latest letters
at every retained cell.

Let the old/frontier head be O, northward, and the new/frontier head be N,
southward. A prepended U/V reads no higher than O_y. An appended U/V reads
no higher than N_y+1. These are exact future-read ceilings because U/V read
ranges are [-1,h] northward, with h their displacement height (3 or 4), and
[-h,1] southward. Both ceilings decrease as their side is extended.

Always extend whichever active side has the higher ceiling, breaking ties
in favor of prepending. Either side may be stopped permanently at any
point. For a prescribed finite X F Y, follow this schedule and stop a side
when its desired length is reached. Therefore the scheduling rule excludes
no finite target word.

Discard every cell strictly above both active ceilings. No future extension
can read it, so this is exact, not an overapproximation. Normalize after
each step by translating O back to (0,0); write N=(dx,dy).

## Detecting old tips despite construction out of chronological order

Each retained cell also records whether X, F, or Y has read it, and whether
it is the marked tip of some already constructed Y-V block. When appending
a V, an already recorded read at its tip is a hit. When prepending a block,
a read of a marked tip is a hit. A hit is accepted only if the entire newly
added macro is physically feasible.

The second test catches an X read constructed after its later Y-V tip.
The ceiling pruning cannot lose an undetected hit: a discarded cell is
unreadable by every remaining construction operation.

If Y is stopped and no marked tip remains, further X extension cannot
create a hit, so that branch can terminate. If X is stopped and no X/F read
remains, further Y extension cannot create a hit from X/F. A tip cannot be
reused within Y itself, by the independently proved arbitrary mixed U/V-run
freshness. Hence that branch can terminate as well.

## Finite conservative quotient of large horizontal separations

The exact sweep has a single potentially unbounded displacement dx. For
|dx|>=8, every reachable retained cell has exactly one of the X/Y source
classes, never F or a mixed class. In the finite certificate these supports
satisfy:

    X cells: -2 <= x <= 3;
    Y cells: -2 <= x-dx <= 3.

This is an inductive support property checked at every far state and every
far transition. The literal macro read bounds are:

    new prepend reads: -2 <= x <= 2;
    new append reads: dx-2 <= x <= dx+1.

Thus at separation at least 8, neither side can read the other's retained
support. All legality tests and color/tag updates then depend only on each
side's own bounded pattern and on dy, not on the magnitude of dx. Shifting
the complete Y support together with its frontier therefore preserves the
far transition relation exactly.

Keep dx exactly when -7<=dx<=7. At negative far separation, keep only its
residue modulo 4, using representatives -8,-9,-10,-11; at positive far
separation use 8,9,10,11. Shift only Y-tagged cells when changing the
representative. All first/last letters and tags are retained.

A macro changes dx by at most one. Ordinary far transitions are reduced
modulo 4. The only ambiguous cases are moves toward the near band from
representative -8 to -7 or 8 to 7. Such a move may mean either an actual
near-band return, or a still-far transition from a more distant level.
Include BOTH possibilities: the near state, and the far state shifted by
four units away from the origin. This deliberately permits premature
returns from arbitrarily distant levels. It is a conservative finite
abstraction, not an assertion that all quotient paths are physical.

Every exact state is represented, every exact transition has a quotient
successor, and every exact hit would be a quotient hit. Hence a no-hit
exhaustive closure suffices.

## Executed certificate

`one_fold_sweep.py` implements the exact retained-field sweep. Its bounded
separation controls have explicit frontier counts and are not proofs.
`one_fold_sweep_quotient.py` implements the conservative far quotient and
exhausts it with no research cap reached:

    112 states, 206 edges, 2 initial fold states, no hit.

The full states and edge relation are saved in
`one_fold_sweep_quotient_certificate.json`. The finite checker verifies all
far-source separation and support bounds as assertions. The independent
implementation and analytic audit both pass. This proof uses the separately
verified mixed U/V-run marker freshness when a sweep side terminates.
