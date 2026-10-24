# Two frozen modules: external old input or actual archive growth

24 October 2026. A corollary of `HELPER_RETURN_CONNECTOR_OR_ARCHIVE_GROWTH.md`
(69028ddf), specializing its old-cohort retirement to inputs OUTSIDE the two
marked complete modules. The underlying axial charge is retained, not new.

## 1. Full physical hypotheses

Keep a completed marked parent episode (e,d,c) and one selected remote old
helper f, consumed at j with d<=j<c. Let L=||p_j-p_d||_infinity>4M, and
suppose the COMPLETE active w component has at most M edges at EVERY fine
cut d-1,...,j. In particular the original parent bridge departure is covered.
All actual archive reattachments and all R births remain on the board.

At cut d let E and D be the COMPLETE dormant w components containing e
and f respectively. These are the ACTUAL frozen fields, with the black
lifetimes then present; membership in these two original modules is never
recomputed after subsequent merging, splitting or recoloring.

Then

    E and D are distinct,
    |E|<=M-1,   |D|<=M-1.                                (1)

For E, the actual preceding bridge L deletes one edge from an active field
of at most M, leaving its departed piece behind. Every E edge is within
M+1 of p_d by the predeparture metric; f at distance>4M is not in E.

For D, no PRIOR active-cap premise or R birth is needed. Before its first
activation after d, D is exactly frozen. Its first activation must be an
R that attaches the entire D to the current active vertex. The newly added
R edge is NOT in D; hence that post-R active field has at least |D|+1
edges. Its cap M proves |D|<=M-1, even for an initially dormant old root.

## 2. The extra-module input count is exact

Let U=E union D, and define H as the number of DISTINCT lifetimes already
black at cut d, OUTSIDE U, ACTUALLY consumed during updates [d,j).
These are additional old-at-departure inputs, not unread support and not
necessarily lifetimes older than the helper's own birth. R births after d
do not count toward H. Later recoloring does not refund a retired identity.

The helper f and parent e both remain black until cut j. Thus of the old-
cohort retirements K used in the return-leg lemma, at most |U|-2 can come
from the two original modules. Consequently

    K <= H+|U|-2 <= H+2M-4.                               (2)

Combine(2) with the exact return-leg bound

    |B_j|-|B_d|+2K >= 2(L-1).

This yields the full-field alternative

    |B_j|-|B_d|+2H >= 2L+2-2|U|
                    >= 2L-4M+6.                         (3)

In particular if the return does not increase COMPLETE black mass, then

    H >= L+1-|U| >= L-2M+3.                              (4)

A materially neutral long-range helper return therefore needs linearly
many old-at-departure lifetimes OUTSIDE BOTH frozen modules. It cannot pay
this cost merely by consuming other cells inside the helper/parent modules.
If there are NO such external inputs, whole-board growth is at least
2L+2-2|U|, and in particular at least2L-4M+6.

Writing P_t=|B_t|-|C_t| for complete dormant black mass also gives

    P_j-P_d+2H >= 2L+2-2|U|-M >= 2L-5M+6.                (5)

These are exact CHECKPOINT alternatives. Their endpoint is immediately
before the helper L. Including the helper's deletion would require the
corresponding one-cell/update correction and is not silently substituted.

## 3. Regeneration and scope

Equations(2)--(5) keep the two INITIAL module identity sets fixed. If their
cells are deleted and R-born again, the original lifetime remains retired;
the replacement is a new lifetime. Unknown archives that later merge into
the current active component contribute to H only when their cut-d black
identities are actually consumed. A fresh post-d bypass or output may be
used freely by the dynamics, but then its net material is part of B_j and
cannot be omitted from the growth side.

This does not prove infinitely repeated interleavings impossible: the
complete archive may grow, and inputs paid here may themselves be outputs
of earlier legs. Nor does it prove a finite input budget when overlapping
legs share preparation. A global invariant would still need to prevent
indefinitely usable regeneration/placement of that charged material.

If E stays wholly dormant until after j, none of its lifetimes can be
consumed in [d,j); this would strengthen the exact subtraction to |D|-1.
That is an ADDITIONAL itinerary premise, not assumed in the general bound.

## 4. Named full-field controls and honest limitations

`check_two_module_connector_or_growth.py` reconstructs BOTH complete modules
at d, literally replays through the helper read, verifies the first R import
of the unchanged complete helper module plus a new edge, and counts actual
cut-d lifetime retirements outside U. It uses the two earlier named fields,
not an arbitrary profile or an externally altered board.

* Blank actual17<18<53<59 interleaving: |E|=|D|=2, |U|=4. Of K=2 old
  retirements before helper L53, one is outside both modules, H=1. Total
  mass gain is7. The pair is fresh and SHORT-range, L=2; it does not meet
  the remote L>4M premise and is used only to check the exact U-size
  inequality, whose proof requires distinct modules but not remoteness once
  that distinctness is separately checked. No long-range inference follows.

* Signed20-cell n400 old-root helper: E is the full15-edge marked archive,
  D is the singleton {(400,400)}, U has16 edges. All K=12 retirements before
  helper20628 lie outside both modules, H=12. L=399, M=43, total gain2365,
  passive gain2328. Exact(3) has right side768 and left side2389; the cap-only
  right side is632. This satisfies the remote premise but the helper is an
  INITIAL root, not a newly produced helper with a prior departure. It
  demonstrates archive growth, not free renewal or a counterexample.

The known42-step non-LIFO control,20-cell remote-root feedback and184-cell
preparation remain compatible. No blanket stack, initial-mass fuel bound,
unbounded-cap theorem, eventual periodicity, or universal capture follows.
