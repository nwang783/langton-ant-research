# Open-chain mass is another unbounded transfer coordinate

24 October 2026. Analytic addendum to d3db81f8, submitted for independent review.

Consider a spatial prefix T<=t of a complete front, with t strictly below its
actual read maximum. No read class is omitted below the genuine read minimum.
Every named cell has its COMPLETE chronological history. In the literal event
successor graph, no closed component is possible: it would already be a proper
closed part of the single actual event orbit, since a read remains above t.
Thus all named events belong to open chains between the crossing ports.

At an even cut use the four physical counts from d3db81f8:
(w,n,s,u), with w+n=s+u. An ant event enters the prefix through a negative-normal
crossing and leaves through a positive-normal crossing. Each open chain has one
of each endpoint. Therefore its number of chains is EXACTLY

C = s+u = w+n.

Let ell_i be the number of named READ EVENTS in chain i, and N_t the accumulated
number of named read events in the prefix. The disjoint chain decomposition gives

sum_i ell_i = N_t.

If instead a chain is encoded by the number of actual steps from its preceding
outside read to its following outside read, that weight is ell_i+1, so the sum
of those weights is N_t+C. This convention distinction matters.

When a new complete cell with n_t reads is added, every old read remains in the
new chains unless a forbidden proper closed component is formed. Hence open-chain
mass increases by exactly n_t. Chains can merge or split as boundary endpoints
are replaced, but cannot erase an old read. In particular, a transfer cycle that
returns to the SAME full chain lengths and port data cannot include any positive
number of new reads. A nontrivial count-level or modulo-four cycle is not a cycle
of the exact weighted interface.

For example, the homogeneous count-level fixed point w=n=s=u=2k with h=l=k
adds two even cells of 4k reads each per two-level step. Its port counts and chain
number C=4k repeat, but the total chain mass increases by 8k. No literal unchanged
whole interface is obtained from that count cycle alone.

This is NOT an exclusion of fronts of arbitrarily large period. At final closure
N equals the full period, and a hypothetical family of wider completed fronts
could have growing N and period. A finite CONTROL graph carrying unbounded length
counters or affine clock weights is still possible in principle. Such a proposed
normalization must prove that it preserves all rank inequalities, physical port
ordinals, full-drift voltage and the final one-cycle/winding condition. The mass
identity does not provide that normalization or rule it out.

This addendum identifies a second unbounded coordinate even if crossing counts
could be bounded: chain lengths. Neither that count bound nor a sufficient
finite weighted quotient is currently proved for the signed middle-short family.
