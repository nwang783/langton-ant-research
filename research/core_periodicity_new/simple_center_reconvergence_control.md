# A simple corrected-center path can have all-input reconvergence

23 October 2026 16:18 UTC. Actual finite-board positive control; independent
replay requested. No discovery-search completeness or minimum-mass claim.

The complete packet word

    UCC, V, DC, D, VC, D, U

runs on the following nineteen initial black cells, every other cell white:

    (-2,0),(-2,1),(-2,3),
    (-1,-1),(-1,0),(-1,1),(-1,2),(-1,4),
    (0,-2),(0,-1),(0,0),(0,2),(0,3),
    (1,-1),(1,0),(2,-1),(2,3),(3,1),(3,2).

Initial head is(0,0,N). Direct fine-step replay verifies all182 raw turns
and the actual following M11 marker. Raw exit is(3,3,N), with47 black cells,
42 residual identities and four C atoms. The board is exactly the minimal
first-L field of THIS fixed literal word, not a claimed globally minimal
simple-path reconvergence seed.

## Exact geometric and identity facts

There are eleven actual D/V/U/C chords of the corrected-center path. The
checker constructs their endpoints from the fine-step raw-cut poses. All55
segment pairs are tested with exact rational determinants and collinear
interval tests. Ten adjacent pairs share only their prescribed endpoint;
all45 nonadjacent closed pairs are DISJOINT. The center path is simple.

There are fourteen initial residual roots. The first UCC merges five
entry components and installs its fresh outputs. The following V consumes
its lower old output(-1,2) at source-included age two, joining one further
entry component; its incidence-rank increment is zero.

The final U at(3,-1,N), clock four, consumes original first-UCC outputs
(2,0) and(2,1) as its two lower inputs, both age four. They are already in
one incidence component. Its other three inputs are distinct entry roots
(2,3),(3,1),(3,2), still in separate components. Thus that U has FIVE inputs
from FOUR distinct components, and increases the undirected incidence
cycle rank by ONE. All earlier packets have rank increment zero.

Complete DSU replay gives beta=1 and five final incidence components. The
identity beta=v+4u-r0+c checks as 2+8-14+5=1. All three produced-input
HB/count-five clauses are explicitly replayed and remain allowed.

## Exact limitation, without exaggeration

This actual control REFUTES the proposed implication

    simple corrected-center path => all-input incidence beta=0.

It is compatible with the prospective geometric theorem for a U-family
factor entry: the path is genuinely simple. Therefore center simplicity
cannot automatically be treated as absence of causal reconvergence.

A single beta-one control does NOT refute every possible mass-dependent
rank bound. Here the rank-producing final U also merges four previously
separate components, so a separately proved component-merge payment rule
would remain an open, stronger hypothesis. There is no renewal, infinite
trajectory, repetition, fresh-root-per-cycle theorem or capture conclusion.

Checker: check_simple_center_reconvergence_control.py.
Exact board, full ledger and all55 pairs:
chronology_dcuv/simple_center_reconvergence_control.json.
