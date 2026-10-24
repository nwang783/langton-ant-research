# The standard highway has two straight causal spines

## Statement

 The motion restores its heading with displacement d=(-2,2). This is a rotation of the source's usual southwest orientation.

On every actual orbit whose turn stream eventually equals this standard word, the edge-token forest, after deleting a finite initial part, has exactly two infinite forward spines. They are parallel straight Tait-lattice rays, on x+y=1 and x+y=-3 in the normalized word frame. Every spine step is (-1,1). Translation/rotation and phase changes preserve the assertion.

Every spine producer has r=4 (degree zero at arrival); the next spine node is the child of its SECOND inserted edge, consumed forward. The four spine-node phases and parent data are:

- phase 13: parent phase 27, parent delay 90, black lifetime age 88;
- phase 27: parent phase 13, parent delay 14, black lifetime age 12;
- phase 45: parent phase 55, parent delay 94, black lifetime age 92;
- phase 55: parent phase 45, parent delay 10, black lifetime age 8.

The phase cycles {13,27} and {45,55} each wind once through a physical period. There are 46 cursor-node phases per period. Every other cursor node is in a finite bush attached to a spine. Maximum cursor-node bush depth is six ancestry edges (seven when terminal buds are counted as leaves), and maximum delay from its spine ancestor is 253 physical updates. Twelve terminal permanent-black buds are emitted per period.

Including the root spine node, the four repeating bush modules have node counts:

- phase 13 module: 3 nodes, 2 permanent buds;
- phase 27 module: 14 nodes, 4 permanent buds;
- phase 45 module: 9 nodes, 0 permanent buds;
- phase 55 module: 20 nodes, 6 permanent buds.

Every black lifetime consumed in the stable highway has age at most 116; parent-node delay is at most 117. These are attributes of the standard highway, not general ant bounds.

## Complete finite coverage

`certify_standard_forest.py` imports only the literal 104-letter word, not a simulator or previous certificate. It first computes phase positions q_i and headings. Every read of the same physical cell as phase i is exactly a pair (j,k) satisfying

`q_j + k*d = q_i`, with 0<=j<104 and integer k.

Because d is nonzero, each j has at most one such integer k. Checking all 104 j therefore exhausts ALL past and future reads of that cell in the bi-infinite periodic geometric motion. There is no epoch cutoff. Their exact chronological times are j+104k.

For every translation class, these finitely many ordered turns start with R and alternate. Every L consequently has a unique preceding R, and every R either has a unique next L or is never consumed. These are the token lifetime edges. For the R at time b, its owner node starts just after the most recent temporal L before b; at most four R's can intervene. This determines the parent of the node immediately after the consuming L. All lifetime ages, parent delays, insertion slots and spatial displacements follow from exact integer comparisons.

The resulting parent-phase map on 46 phases has exactly two directed cycles, each containing two phases. The sum of temporal parent delays on each cycle is exactly 104. All other phases enter one of these cycles, with at most six parent steps and at most 253 elapsed updates.

To see why this proves exactly two spines rather than merely two quotient cycles, lift a cycle back to integer epochs. A cycle with total delay 104w produces exactly w forward infinite chains, indexed by epoch modulo w. Here w=1 for each of the two cycles. Every non-cycle phase has a finite parent path into a cycle and cannot be part of an additional infinite forward chain: in a finite functional graph, a forward infinite child chain can visit off-cycle phases only finitely often before it would force an additional cycle. The explicit depth bound strengthens this observation. A finite preperiod can merge the two tails under one earlier ancestor but cannot create an additional infinite end.

The cursor positions at phases 13,27,45,55 are respectively (-1,2), (-2,3), (-5,2), (-6,3). The checked cycle edges have displacement d/2=(-1,1), establishing the straight parallel geometry. The slot and r checks establish the degree-zero second-child characterization.

For each R with no later read in its translation class, its token is permanent. There are exactly twelve such phases. Assigning every node and bud to its first spine ancestor gives the module counts above. This also independently explains the standard mass growth 12.

## Passage from a periodic tail to an actual finite-seed orbit

An actual standard tail may initially consume cells written before its entry time. The all-period translation-class calculations bound the span between any two reads of one cell by a finite constant (the checker retains the exact data). After sufficiently many periods, every consumed token's producer and parent node lie inside the periodic tail. Those late parent relations therefore equal the certified phase map exactly, independently of untouched external debris. A finite initial forest cannot add an infinite spine unless it has descendants in this tail; these are already accounted for by the two lifted cycles.

This argument does not assume whole-board translation symmetry. Permanent debris remains present and is explicitly represented by buds or earlier unused roots.

## Trust boundary and the unsolved global problem

The theorem is an exact finite arithmetic deduction about the given standard word. It is not a proof-assistant formalization or external review. The file `blank_ancestry.json` is only a discovery replay; the all-epoch proof is the finite translation-class argument above.

Nothing here proves that arbitrary finite seeds acquire these two spines. In particular, a proof excluding all infinite renewal would be false: these two simple renewable dependency cycles are necessary even in the desired solution. A prospective global argument must distinguish them from productive nonstandard renewal while retaining finite but possibly arbitrarily large side bushes.

## Independent audit correction

The independent audit accepted the core forest and cycle-lifting argument but caught an important leaf-count convention: cursor nodes have bush depth at most six; the permanent buds at phases 100 and 103 have depth seven. The certificate now reports both quantities. No claim about general seed stabilization was audited as proved.
