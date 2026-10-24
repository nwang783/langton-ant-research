# Effective lifetime within the terminated movement language

The independently checked raw DCUV termination theorem also implies a total
computable mass-only lifetime for this restricted language. This does not
restore a global mass-only defect budget, which the fixed-mass long-wave
families disprove.

For each integer m, enumerate the four-ary tree of raw D/C/V/U concatenations
whose per-cell read letters alternate and whose number of distinct first-L
cells is at most m. Membership is decidable from the literal physical path.
An infinite branch would be realized by placing black at exactly its union
of first-L cells, a single set of at most m cells. Raw DCUV termination rules
this out. Finite branching then makes the whole tree finite.

Its maximum raw length L(m) is therefore a total computable, monotone,
diameter-independent bound. Exhaustive enumeration defines it effectively;
no numerical tree enumeration, practical complexity claim, or small explicit
value was needed or performed.

In the separate seven-word language D,C,V,U,F,Q,B, the foreign words F,Q,B
have lengths56,64,74 and net black gains2,6,6. If a factor starts at mass m
and contains k foreign words, set a_0=m and

    a_(i+1)=a_i+L(a_i)+6,
    G(m,k)=74k+sum_(i=0)^k L(a_i).

Splitting at the foreign words and retaining each actual complete entry board
shows that G(m,k) bounds its raw duration. This does not bound k or justify
transporting a DCUV provenance clause across a foreign block.

The exact seven-word graph remains one214-vertex/993-edge mixed component.
Its DCUV-only subgraph has a93-vertex/417-edge cyclic component; its foreign-
only subgraph has no cycle. Physical restricted-language termination is not
a deletion of DCUV edges from arbitrary mixed paths.

Author bundle: word_stabilization/dcuv_raw_bridge_effective_frozen_20261023_2100,
manifest SHA25650664f91cce11a73443850ca8de824e789c32c1d87b1f1d88bb3ad5d25073b74.
Independent verification: audits/check_dcuv_effective_mass_bound_independent.py/json.
The final complete-eight manifest da766cab53d45efb5ea75167b176ad851ce3c85212ce9a544d75dcb474a47c93
is additionally pinned there. The original termination digest is unchanged.
