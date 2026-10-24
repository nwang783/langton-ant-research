# Geometric C-age genealogy and a cubic finite-C duration bound

Status: proposed on 2026-10-23 07:48 UTC; independent review pending. This is a necessary C-recurrence theorem for complete recurrent-eight finite factors, not a DCUV exclusion or capture theorem.

Consider a finite context-complete recurrent-eight packet factor, with entry black mass m>=5, the signed disjoint five-cell core, residual entry mass r0=m-5, total C-macro count k and raw duration L. Use the signed current residual-identity ledger, including consumption and fresh reproduction at U's recycled cell. Packet outputs are distinct current physical residual cells.

## A distinguished-input table

For each packet choose the following input in its source coordinates. The age lower bound is JO's source-included, consumer-excluded C age for a produced input. D_infinity is the greatest L-infinity distance from this chosen input to ANY output of the packet.

| Packet | Chosen input | JO minimum age | D_infinity |
|---|---|---:|---:|
| D | (0,1) | 3 | 2 |
| DC | (0,1) | 3 | 3 |
| V | (1,2) | 3 | 2 |
| VC | (1,2) | 3 | 3 |
| VCC | (0,3) | 4 | 3 |
| U | (0,3) | 4 | 3 |
| UC | (0,3) | 4 | 3 |
| UCC | (0,3) | 4 | 4 |

In every row D_infinity is at most the minimum age. Quarter rotations preserve L-infinity distance. These are exact literal-coordinate inequalities, not bounds on a guessed physical genealogy.

## An auxiliary output forest

Write C_before(P) for the number of C macros preceding a packet P inside the factor. Give each identity produced by P birth time C_before(P), and each entry residual identity virtual birth time -4. When P produces an output identity, make the chosen input identity its auxiliary parent. The same parent may have many children. The parent is actually consumed, and a recycled output is a fresh child identity, not the old identity.

If the chosen parent was produced by an earlier packet Q, its pre-consumer age is exactly C_before(P)-C_before(Q). JO therefore says this birth-time difference is at least the row's required age and hence at least the spatial parent-child distance. If the parent is an entry identity, the birth-time difference is C_before(P)+4>=4, again at least the spatial distance. Birth time strictly increases along every edge, so every auxiliary ancestry chain terminates at one of the r0 entry identities.

Telescoping the distances along that chain shows that an output born at C-before time b is within L-infinity distance b+4 of its entry root. At any factor boundary with cumulative C count j, every current produced identity has b<=j, while every surviving entry identity is its own root. Thus

current residual support is contained in the union, over entry residual cells z, of z+[-j-4,j+4]^2.

In particular, because current residual identities occupy distinct integer cells,

r(j) <= r0*(2j+9)^2.

Unread entry debris may lie arbitrarily far away. The union-of-root-boxes estimate uses only its cardinality, not its diameter or proximity to the head. If r0=0 no packet can start, since every recurrent-eight packet has a residual input.

## Duration by C epochs

Use the previously signed zero-C epoch argument: an epoch consists of zero-C packets followed by its next positive-C packet, or a final zero-C suffix. An identity produced inside an epoch has pre-consumer C age0 until its terminal packet and cannot be consumed there, because every produced input has JO age at least2. Every consumed input therefore comes from the epoch-entry residual ledger; distinct input identities cannot be reused. Literal lengths give

epoch duration <= 10*r_entry + 15*c_epoch.

The epoch-entry cumulative C counts form a subset of {0,...,k}. At entry count j the spatial bound gives r_entry<=r0*(2j+9)^2. Summing over the larger full set and using total positive-C count k yields

L <= 10*r0*sum_{j=0}^k (2j+9)^2 + 15*k
  = (10/3)*(m-5)*(k+1)*(4*k^2+56*k+243) + 15*k.

The polynomial is integer-valued at every nonnegative integer k. This improves the signed age-energy exponential-in-k duration bound to O((m+1)*(k+1)^3), by using physical cell capacity in addition to the JO ages. Therefore an infinite finite-support recurrent-eight tail would require at least a cube-root C recurrence rate in its elapsed raw time, with the entry mass fixed. No upper bound on C count, finite tail, U-event fuel bound, arbitrary-factor trimming extension, or global capture conclusion follows.
