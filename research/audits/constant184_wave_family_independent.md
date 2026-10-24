# Independent all-parameter certificate: 184 original black cells and unbounded defect counts

23 October 2026, 16:48 UTC. Exact mathematical/computational PASS.

## Bound supplied object

The supplied affine contract is `causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json`, SHA256 90fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399. The six explicit router words and caps have plan SHA256 e3d6af0700c933ddff96319415e0d59f5b7e0407c883b9f1d990d8d91d87deac. The prose statement `prepared1564_constant_mass_producer.md` has SHA256 c7ed1e209be5b500682cbc641b1681657d9250248aae941fab8879d0faf8de82.

`check_1564_constant_mass_family_independent.py/json` verifies the complete word directly, without importing the author's simulator, support-guard implementation, discovery procedure, local router oracle, or gluing code. It derives all affine starts and repeat counts and compares ALL 184 seed families and ALL 16 word/count/pose/time stages exactly with the frozen manifest.

For every integer N>=1, R=100+28N. Start at (33+14N,70+14N), heading W, with the 184 listed black cells and every other cell white. The entire supplied word is legal. Its N-wave block begins at time 91747+24024N at (-6,-6,NORTH), and ends at time 91747+25588N at (14N-6,14N-6,NORTH), with 10805+2876N current black cells. No edit occurs after time zero.

## Why the finite checker covers every integer parameter

Trace each fixed word once. Each occurrence slot has fixed transverse normal t=x-y, fixed x parity a, and scalar coordinate z=(x-a)/2. The initial pose's coefficient of N is divisible by 14; every router and repeat endpoint preserves that property. Thus every slot has

    z = alpha*N + beta + s*k,

where alpha is divisible by seven, and s is +1 or -1 for a standard H block, +7 for the wave, or zero for one fixed router/launch slot. The repeat index satisfies 0<=k<c*N+d. All repeat counts are positive for every N>=1.

Split z=7w+r, 0<=r<7. Every read slot and every initially black seed family then has an EXACT integer affine eligibility interval

    L(N) <= w <= U(N).

There is no rounding dependence left in N. For standard slots, only the fixed constants require floor/ceiling by seven. Wave and fixed-word slots occupy their exact residue r. Each eligible slot contributes exactly one read of that physical cell.

Chronology is exact. Different blocks retain their supplied order. Inside one repeated block, substitute the unique eligible k into time P*k+i. Terms involving the fixed cell and N cancel when comparing slots, leaving a fixed key i-P*beta/s. The checker uses an equivalent integer key for the wave. Fixed-word slots keep their literal index. Consequently each spatial slab has a finite, completely ordered list of physical reads, not a relaxed incidence inventory.

For each of the 1460 nonempty (t,a,r) classes, collect all affine starts L and successors U+1, including all seed points. Partition N>=1 at the floor of every pairwise boundary-line crossing and its next integer. On every resulting integer interval, the checker explicitly verifies that the order and equality pattern of these affine boundaries is constant, using both finite endpoints or the slope for the unbounded interval. This is an exact one-variable arrangement, not sample extrapolation. The union of all parameter cuts is just {1,2}.

Between every consecutive spatial boundary, the eligible read list and seed membership are fixed. Every consecutive pair of read symbols alternates; the first symbol is L exactly when that cell belongs to the initial seed. No two seed families collide, and every seed cell is actually read. Outside the extreme boundaries there are neither reads nor seed cells. These local conditions are necessary and sufficient for the prescribed complete deterministic turn word on the initially white complement.

The complete checks cover 1508 parameter regions, 4581 spatial slabs, and 17470 chronological read obligations. Their affine first-L cardinalities sum identically to 184, including on every unbounded region. The complete obligation digest is 92ac92738a5f15a4e7d2890d867c8722c6d902c72815fab503843ad2a527438e. Literal whole-board specializations at N=1,2,5 provide separate implementation controls, not the all-N premise.

## Exact true-history defect count

The actual inverse ten-turn history at the initial pose is LRLRRRRLLL for every N>=1. This is independently reconstructed from the canonical 13-cell initial core. Every other affine seed family is checked against every inverse-history read position by exact linear equality, excluding an integer N>=1 collision.

Use the 84 ten-letter factors of the cyclic standard H word. An adjacent defect is a position where both overlapping ten-letter histories are outside this language. Every nonempty H power can be compressed to one H for counting: its last ten letters are unchanged, and extra copies add only standard histories. The routers, 55-letter phase suffix, and 24-letter launch remain fully retained. After one wave period, the last-ten state is the same for all further copies, which each add exactly 614 defects. Exact counting gives

    K(prefix_N) = 614*N + 92.

The finite R100,N3 sample, checked separately on all 96439 reads, gives 1934 defects and matches this seam formula. Its parameter R is deliberately not substituted for the all-N family R=100+28N.

## Consequence and exact limitation

The supremum of total future defects over finite initial seeds of mass 184 is infinite. A translation and proper rotation normalize every member to the same initial origin and heading without changing mass, word or defect count. The initial positions, and hence seed diameter, depend on N. This disproves any upper bound on total defects depending only on the original black-cell count.

It does NOT supply one finite seed with infinitely many defects, an infinite finite-board realization of the 1564 word, or a counterexample to eventual standard104 capture. The exact wave still requires increasing CURRENT black supply. The constructed ordinary flights manufacture that supply before the finite episode; their duration and final current mass grow with N. No subsequent behavior is asserted.

Combining this family with the separately signed at-most-12-addition two-sided completion also gives already bi-standard capturing examples with at most 196 initial black cells and arbitrarily many defects. This is a deduction from the existing completion theorem, not a claim that the unmodified 184-cell seeds themselves have been shown to capture.
