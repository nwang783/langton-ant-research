# Quadratically many adjacent defects in certified capturing seeds

22 October 2026. Status: independently audited, including the all-n
spiral geometry, event lower bound, completion coupling, and coordinate-size
claim. On 22 October 2026 at22:34 UTC the original spiral seed's exact
continuation was independently audited too, strengthening the capturing mass
from11n+6 to11n+2 for n>=11. No fixed-mass unboundedness claim is made.

## Construction and event count

The source is ../core_periodicity_new/quadratic_inward_spiral.md. It supplies
for each n>=1 a literal feasible prefix W_n with

    minimal initial black mass 11n+2,
    length 8n^2+14n,
    at most two reads per physical cell.

For n>=2 it contains at least 8(n-2)^2 actual adjacent bad-ten events K.
The lower bound counts only eleven-letter windows wholly inside its four
S^j blocks at each level, S=RLLR, so it is independent of the inverse-history
convention and of whatever follows the prefix.

The exact continuation in
../causal_reduction/spiral_endpoint/README.md proves that the ORIGINAL
minimal seed H_n captures for every n>=11. Its guaranteed standard-tail
phase boundary is

    8n^2+36n+3021,

not asserted to be the earliest capture time. The independent all-parameter
and infinite-tail verifier is
../audits/check_spiral_affine_continuation_independent.py/json. Consequently

    |H_n|=11n+2,
    total future K events >=8(n-2)^2                 (n>=11).

For comparison, the earlier general four-cell completion argument remains
valid for every n>=1: it constructs a capturing seed of exactly11n+6 cells
preserving W_n, without needing this special continuation. It is no longer
needed for the asymptotic lower bound.

Thus even among inputs already guaranteed to capture, no upper bound on
total K count can be linear in initial black mass. The two-visit prefix
already generates quadratically many defects before any third read.

This is a lower bound on event count, not merely on physical delay or on a
chosen certification checkpoint. The earlier one-black delayed-collision
families did not have growing K counts, so they did not imply this result.

## Encoding-length form

The spiral read/pose set and its original seed H_n have coordinate magnitude
O(n) directly from their explicit formulas. No added port, exit-time search,
or nonuniform choice is needed for the stronger n>=11 family.

The earlier four-cell variant also has O(n) coordinates: choose a square Q
of side O(n) containing the entire spiral read/pose set and seed, and attach
the port at the original orbit's first exit. That exit is after W_n and lies
on Q's boundary, regardless of the possibly much larger exit time.

A conventional explicit binary list encoding of H_n therefore has length
O(n log(n+2)). For the bounded-encoding positive-input maximum C(N) defined
in adjacent_renewal_normal_form.md, monotonicity then yields

    C(N) = Omega(N^2 / log^2(N+2)).

The implied constants depend on the chosen explicit encoding. This lower
bound does not imply undecidability, non-primitive-recursive growth, or an
unbounded count at a single fixed black mass. It merely supplies a rigorous
quadratic negative control for proposed initial-fuel ranks.
