# Finite order-free normalized real-clock frontier relaxation

23 October 2026, 06:34 UTC. Independently signed safe finite abstraction (audit KD).
Each supplied drift/cap application still requires its own complete graph replay.

Fix an actual full drift d, finite local visit cap, a finite row frontier,
and a proved positive integer period lower bound N. No primitive quotient
is substituted. Use exact complete white histories, directed-edge ordinal
matching and the signed processed-path connectivity construction.

## Clock inequalities with no phase order

For an actual front of period P>=N, take the physical representative read
clock t_e (not its phase modulo P), and put X_e=N*t_e/P. For every physical
successor arc u->v with seam voltage k, exact clocks give

    X_v-X_u = -N*k + N/P.

Since 0<N/P<=1, the following necessary real difference constraints hold:

    X_v-X_u <= 1-N*k,
    X_u-X_v < N*k.                              (1)

For consecutive local ranks j,j+1, impose only

    X_j-X_(j+1) < 0.                            (2)

The common N/P is forgotten, so these constraints are a relaxation, not
an exact alternative to the signed phase/voltage clock criterion. Distinct
phases and cyclic order of unfinished path blocks are also forgotten.
No cut reanchoring is needed: X consists of physical representative clocks.
The relaxation may have spurious whole-front outcomes.

## Strict real difference-bound matrices

A bound a<=b or a<b is encoded by an integer pair (b,s), with s=0 for
nonstrict and s=1 for strict. Smaller integer bound is stronger; at equal
integer, strict is stronger. Addition sums the integers and ORs strictness.
An inconsistent cycle has total bound b<0 or b=0 and strict. Ordinary
min-plus closure in this ordered semiring is exactly the strict real
DBM feasibility test. Projecting after closure onto surviving endpoints
is exact existential projection of these difference constraints.

The implementation encodes (b,s) as 2*b-s. Its sum is code1+code2+1 only
when both inputs are odd, and otherwise code1+code2. Infinity is separate.
A negative diagonal is exactly inconsistency. This representation does
NOT treat two strict bounds as two units of numerical slack.

For a fixed integer M>=0, weaken every projected bound larger than M to
infinity, and every bound stronger than the nonstrict bound -M to -M.
All retained codes belong to {-2M,...,2M,infinity}. These weakenings cannot
remove an actual solution. The stored matrix need not remain transitively
closed; close it again when a new row is added.

## Connectivity and finiteness

Every processed successor component is a directed path whose two endpoints
are on the frontier, unless a closed component has formed. Compress paths
to endpoints and retain their seam voltage modulo a fixed q>=2. Retired
clock variables are projected, not reset. Old compressed path arcs are
used only to splice connectivity; their complete clock consequence is in
the DBM. Sort paths by their start IDs solely to give a canonical state.
No cyclic-order hypothesis is imposed or used.

A closed component alongside another component is impossible in a single
full event cycle and is rejected. A sole closed component may be a full
front only if its voltage is one modulo q and (1),(2) remain feasible.
Such a component is retained as a possible-front outcome. No positive
realizability claim follows.

For fixed supplied drift, cap, M,N,q, the row histories, endpoint pairings,
voltage residues and finite-alphabet matrices have a finite state space.
An actual front supplies a path from the empty exterior state to a retained
possible-front outcome. Therefore complete graph exhaustion without such
an outcome would be an all-width, all-period exclusion at the supplied cap
and full drift. A state/resource limit is UNKNOWN, never an exclusion.

## Producer controls and present scope

`probe_normalized_real_zone_core.py` implements the strict DBM step.
`probe_axis4_normalized_real_zone.py` uses exact factorized axis-four row
histories and the previously signed physical splice. For axis-four, P>=8
follows already because P/2 horizontal moves must have net displacement4.
The first cap-four N=8,M=16,q=2 graph has 3,809 states,6,015 accepted edges
and365,713 attempted transitions, with no possible-front outcome. This is
a method control of an already signed classification, not a new theorem.
Independent replay of this cap-four method control passed in audit KD using
complex lattice geometry and infinitesimal Bellman-Ford strict bounds; see
`../audits/axis4_normalized_real_cap4_N8_M16_mod2_independent.json`. No cap-five result,
all-cap axis-four exclusion, general cap-four theorem, or finite-seed
capture theorem is claimed.
