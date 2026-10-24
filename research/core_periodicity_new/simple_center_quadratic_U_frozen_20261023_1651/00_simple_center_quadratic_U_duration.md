# Quadratic U-count duration from confinement and center simplicity

23 October 2026 16:50 UTC. This is a consequence of the signed HS confinement
and signed U-entry simplicity theorems. It does not bound the number of U
packets or prove capture. The complete recurrent-eight factor scope is
indispensable.

Let a finite, physically feasible, context-complete recurrent-eight factor
start with m >= 5 black cells. Let u be its number of U/UC/UCC packets. Write

    B(m,u) = 57 + 38(m - 5) + 60u,
    R(m,u) = ceil(2 B(m,u) / 5),
    t(m,u) = floor((2 R(m,u) + 1)^2 / 3),
    F(m,u) = 20 R(m,u) (t(m,u) + 1) + 28 t(m,u).

These are the signed HS bounds. Put R0 = R(m,0) and F0 = F(m,0).
For u = 0, the raw duration L is at most F0. For u >= 1,

    L <= F0 + 28 (2 R(m,u) + 2)^2
       = F0 + 112 (R0 + 24u + 1)^2.

Thus every such factor has diameter-independent raw duration
O(m^3 + u^2). An actual terminal M11 adds eleven fine steps to total
duration. No estimate in this note includes arbitrary non-language history.

## Proof

Take the full-packet prefix strictly before the first U-family packet. It
contains no U-family packet, starts from the original entry board of mass
m, and has the actual marker required by HS: if the prefix is nonempty,
the following U-family raw word begins with that marker. HS with u = 0
bounds its raw duration by F0. An empty prefix has duration zero.

The remaining full-packet suffix begins with U/UC/UCC. By signed U-entry
simplicity, its continuous corrected-center atomic path is injective.
In particular every atomic entry center in this suffix is distinct.

Apply HS confinement to the WHOLE original factor, with its actual u.
Every atomic entry head is a visited read position, so it lies in the
integer square of radius R = R(m,u) around the original entry head.
For heading h its corrected center is

    head + rotation_h(-1/2, -1/2).

Every coordinate is therefore a half-integer in the interval
[-R - 1/2, R + 1/2], after subtracting the original entry head. There are
2R + 2 choices per coordinate, hence at most (2R + 2)^2 possible atomic
entry centers. Simplicity permits each one at most once in the suffix.
Every atom has raw length at most 28 (D: 10, V: 18, U: 28, C: 15).
Consequently that suffix lasts at most 28(2R + 2)^2 raw steps. Add the
prefix bound. Finally, R(m,u) = R0 + 24u because u is integral.

No simplicity is assumed for the U-free prefix, and no reset of its mass
is used in the quadratic term. Remote initial debris remains harmless by
the already signed HS confinement statement.

## Necessary recurrence, not finite fuel

For fixed m, any hypothetical infinite complete recurrent-eight factor
would have to satisfy u(T) = Omega(sqrt(T)) along completed-packet times.
Indeed every finite completed-packet prefix satisfies the bound above.
Equivalently, when L > F0,

    24u >= sqrt((L - F0) / 112) - R0 - 1.

This is compatible with unbounded u. No component merger budget, initial
root expenditure, highway conclusion, or V1/U1 record closure follows.

## Dependencies

- word_stabilization/dcuv_epoch_reset_bound_manifest.json: signed HS
  complete-factor confinement and duration, including actual marker scope.
- U_entry_simplicity_frozen_20261023_1616/manifest.json: signed U-family
  entry simplicity, including internal C cuts and finite terminal scope.
- chronology_dcuv/literal_residual_geometry.json: literal atomic words and
  their true common marker; C is the suffix of DC after D.
