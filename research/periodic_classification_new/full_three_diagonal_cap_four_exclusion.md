# Full diagonal-three drift is impossible under visit cap four

23 October 2026, 06:57 UTC. Independently signed supplied-drift all-width,
all-period exclusion (audit KH). No literature-priority claim is made.

## Theorem

No complete white-input translating front with at most four reads per
physical cell has actual full drift (3,3). Genuine quarter rotations
exclude all four vectors (±3,±3). The full displacement is not replaced
by its primitive direction.

## Finite necessary relaxation

Use exact diagonal representatives p(t,i)=(i,i+t),0<=i<3. Every physical
edge joins neighboring representative rows, with its exact seam voltage.
Each class has one of the31 complete white histories through four reads,
including the empty history. The signed static row-balance identity leaves
6,031 rows of one parity and5,627 of the other. It has no width or period
premise.

Apply the independently signed normalized-real frontier relaxation in
`normalized_real_frontier_abstraction.md`, with N=8,M=16,q=2. The retained
complete-white-front growth theorem gives g>=8 and P>=g>=8, so N=8 is a
proved lower bound, not a period cutoff. Exact directed-edge ordinal
matching and processed-path connectivity are retained. Strict normalized
physical clocks obey -8k<X_v-X_u<=1-8k on a seam-k edge, while local ranks
strictly increase. The common8/P increment and cyclic path order are
forgotten, only enlarging the possible state space.

The complete producer graph has51,930 states,91,690 accepted edges and
3,243,574 attempted extensions. It has no possible whole-front outcome.
The signed all-width bridge therefore excludes a genuine finite-width
front at every period. The clock-bound clipping is outward weakening,
not a geometric or chronological search cutoff.

## Independent replay

`../audits/check_diagonal_normalized_real_independent.py` starts from all
59,582 unpruned row assignments, reconstructs the physical port matches
using complex lattice geometry and checks every attempted extension. Its
strict-clock closure uses infinitesimal Bellman-Ford rather than the
producer's strict-bound integer encoding and Floyd closure. It reproduces
the complete reached graph and absence of a possible-front outcome.

Frozen producer certificate:
`diagonal_n3_normalized_real_cap4_N8_M16_mod2.certificate.json`.
Independent result:
`../audits/diagonal_n3_normalized_real_cap4_N8_M16_mod2_independent.json`.

Literal standard104 fronts and their full-period repetitions at208 and312
remain accepted by the SAME normalized-real core with exact clock witnesses;
see `normalized_real_positive.json`. These are positive controls, not a
claim that cap-four fronts exist at another displacement.

## Scope

This excludes a supplied full drift under a finite cap, with no width or
period bound. It does not exclude cap five at this drift, larger diagonal
drifts, all-cap axis-four fronts, general cap-four fronts, nonperiodic
behavior, or the finite-black-seed eventual-standard104 conjecture.
The separately signed stable white-history bridge carries the same
bounded-multiplicity exclusion to any eventual periodic suffix from a
finite black seed. No primitive quotient or reflection is needed.
