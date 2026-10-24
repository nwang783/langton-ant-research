# Exact finite fuel across one arbitrary mixed U/V fold

Status: independently audited by a separate literal complex-heading sweep,
including the marked-site sets and all seam identities.

## Theorem

Let W = X F Y be physically feasible, where X and Y are arbitrary finite
words over {U,V} and F is Q or B. Either run may be empty. If u and v are
the total numbers of U and V blocks, then the exact minimal number of
initial black cells required to execute W is

    19 + 5u + 2v, if F = Q;
    22 + 5u + 2v, if F = B.

Equivalently, this number is 4 + 5u + 2v + c_F, where c_Q=15 and c_B=18.
Every first-L input of every block, apart from its four seam inputs, is
unread earlier within W. The four seam inputs are new only in the first
block; in every subsequent block they have already been read in the
preceding block's terminal R-star.

This is a statement about the factor W and a board at its entry. It says
nothing about reads before that entry. It does not cover C blocks or more
than one fold.

## Marked first-L inputs

In each block's north-facing entry frame, let

    SEAM = {(0,0), (-1,-1), (0,-1), (1,0)}.

These four cells have first letter L. The remaining first-L sites are:

    U: {(-1,0), (-1,1), (-1,2), (0,2), (0,3)};
    V: {(-1,0), (1,2)}.

The Q and B marked sets are computed directly from the literal traces by
subtracting SEAM from their first-L sets. They have respectively 15 and 18
members. No site is counted twice within a block.

Each relevant macro pair's seam check shows that all four successor seam
sites were read by the preceding terminal R-star. Conversely, the marked
sites in a mixed U/V run are fresh within that run: literal pair checks
cover adjacent blocks, and the y-ranges [-1,h] with h>=3 exclude overlap
with nonadjacent blocks. This is the already audited mixed-run fuel proof.

## One-fold freshness certificate

Use exactly the two-frontier downward sweep and conservative far-distance
quotient of `one_fold_v_freshness.md`, with the following marker change:

- Initially mark each F first-L site outside SEAM.
- When appending a Y block, test and then mark all its first-L sites outside
  SEAM, not merely V's tip.
- A prepended X read of any marked cell is a hit.

An appended marker already present in the retained field is also a hit.
The entire newly added block must pass all read-alternation tests before a
hit is accepted. Earliest/latest read storage, decreasing-ceiling pruning,
source tags, and the conservative separation quotient are unchanged.

The graph exhausts with no hit:

    82 states, 147 edges, 2 initial fold states.

The all-fuel extension uses the same support invariant and independently
passes the same far-distance soundness audit. The separate implementation
recomputes all marked-site sets from literal turn words, rather than
trusting the discovery lists.

## Counting the exact seed

At any physical cell, a feasible finite word requires an initial black
cell exactly when its globally first read is L. The initial macro has four
seam sites plus all its marked first-L sites. Every later macro has its
seam sites already read, while its marked sites are fresh by the run lemma
and the one-fold certificate. Therefore the number of distinct globally
first-L cells is exactly four plus the sum of the marked-set sizes.

This both lower-bounds every realizing board and constructs the minimal
finite seed: make precisely those globally first-L cells black. Physical
read alternation then realizes the complete word.

## Artifacts

- `one_fold_sweep_all_fuel.py`: exact retained-field transitions.
- `one_fold_sweep_all_fuel_quotient.py`: finite conservative closure.
- `one_fold_sweep_all_fuel_certificate.json`: full states and edges.
- `../audits/check_one_fold_all_fuel_independent.py`: independent checker.
- `../audits/one_fold_all_fuel_independent.json`: independent result.

The copied discovery-only witness replay has been repaired to check
arbitrary marked first-L reuse rather than insist on a V-tip witness. That
helper is not used by the no-hit finite-quotient proof.
