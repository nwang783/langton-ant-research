# Finite support excludes every infinite complete-eight factor

23 October2026,20:57 UTC. Author corollary submitted for independent review.
This combines the new finite-support U-entry exclusion with the earlier signed
D/C/V theorem. The entry board means the COMPLETE black board, not only its
active core or current read window.

## Literal statement

Let the ant have finitely many black squares at the entry of an actual,
context-complete factor of the eight full packet types

    T8={D, DC, V, VC, VCC, U, UC, UCC}.

The base words are

    D=LLLLRLRRRR,
    C=LLLLRLRRRRLRRRR,
    V=LLLLRLRRRRLRRLRRRR,
    U=LLLLRLRRRRLRLLLLRRRRLRRLRRRR.

Packet names mean literal concatenation with their C tails. Every claimed
packet has its true raw word and actual required M11 marker; no fictitious
future or arbitrary relaxed packet concatenation is allowed. The exact literal
U word is checked against the retained source by the accompanying checker.

There is NO infinite actual T8 factor from such a finite complete entry board.
In particular, no finite-seed ant has an eventual infinite tail with this exact
context-complete T8 decomposition. The theorem does NOT assume every ant
eventually has that decomposition.

## Proof: a genuine first-U/no-U dichotomy

Assume an infinite T8 factor.

1. If it contains a U-family packet at ANY finite packet index, take its first
   such packet. The physical ant has taken only finitely many steps before
   that entry. A finite black board stays finite under finitely many flips.
   The suffix starts U/UC/UCC, retains the actual complete-eight decomposition
   and markers, and has finite COMPLETE black support at its own entry. This
   contradicts the independently passed finite-support U-entry theorem.

2. If it contains NO U-family packet, all its packets lie in
   {D,DC,V,VC,VCC}. Expanding the packet names gives an infinite concatenation
   of the exact raw macros D,C,V. The signed D/C/V finite-tail theorem excludes
   this on a finite-support board, at arbitrary head pose and heading.

These two cases exhaust an infinite factor. No assumption that U occurs
infinitely often, no recurrence extraction, no bound on U count, and no
finite total entry-root count across restarted histories is being smuggled in.
The finite-support board is taken at the ACTUAL first-U cut, not reset to only
newly touched cells.

## An optional quantitative first-U interface

The signed HS epoch-reset bound F(m,u), for complete T8 factors of entry mass
m and u U-family packets, gives

    B=57+38(m-5)+60u,
    R=ceil(2B/5), t=floor((2R+1)^2/3),
    F(m,u)=20R(t+1)+28t.

Every U-free complete prefix before the first U therefore has raw length
T<=F(m,0). Its terminal next marker is the actual beginning of the next U
packet, so the complete-factor hypothesis is retained. If the entry board has
mass m and radius R0 about its entry head, the actual first-U board satisfies

    m_U<=m+T,
    R_U<=R0+T.

The mass bound uses one flip per fine step. For radius, an original black cell
is at most R0+T from the new head. Any newly black cell was visited at time tau
and is at most T-tau<=T from that head along the remaining real cursor path.
Thus no unread old debris or old core black cell is discarded at the cut.
This is only a clean interface for a separately derived effective bound; no
new total duration expression is asserted here.

The no-U case can alternatively use the same signed bound with u=0 on every
finite prefix: one fixed F(m,0) cannot bound prefixes of an infinite factor.
This is an equivalent use of the existing DCV theorem, not another new proof.

## What this bridge does and does not establish globally

This is a genuine extension of the restricted-language exclusion beyond
U-free DCV factors: arbitrary mixtures of U-family and D/V-family packets are
covered without closing the old strict V1/U1 record-funding cases.

It is NOT yet a claim that arbitrary raw D/C/U/V tails can all be packed into
T8; that lifting needs the separately signed boundary/maximal-C grammar.
It is NOT a claim that arbitrary ant trajectories eventually enter that raw
four-macro language or T8. It also does not automatically enlarge the existing
six-label global defect UNION. This corollary supplies no new K-label set or
complete global first-marker-return graph. The old UNION6 M-return packets
are a different presentation (for example V+=V LRRRR has length23 and is not
a literal T8 packet). A new label-union consequence needs its OWN exact return,
context, graph and SCC bridge, being checked separately.

The original V1/U1 strict funding implications, infinite prepared backgrounds,
behavior after a finite T8 factor exits its language, and arbitrary finite-seed
standard104 capture remain outside this corollary.

## Immutable dependencies

- finite_support_U_entry_exclusion_manifest.json, main qualified finite-support
  U-entry proof a2c4a8d5.
- word_stabilization/dcv_finite_tail_theorem.md and its signed producer-family,
  complete-ledger and directional-potential audits.
- word_stabilization/dcuv_epoch_reset_bound_manifest.json (HS), only for the
  optional quantitative first-U interface and equivalent U-free-prefix proof.
- Literal residual geometry for the exact base words and packet expansions.
