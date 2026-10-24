# The interleaving boundary crossing is already present, and side cuts are exact

23 October 2026, 16:36 UTC. Exact clarification from the signed K=1
endpoint maps, not a new interior resource or general exclusion.

## 1. The apparent extra crossing is the selected L1/R2 pair

Let D_i be the actual LEFT excursion from selected R2_i to R0_(i+2).
It contains selected L1_(i+1). The next LEFT excursion D_(i+1) starts
at R2_(i+1). Their boundary endpoint indices interleave:

    i, i+1, i+2, i+3.

It is tempting to infer an additional interior intersection from this.
But the known selected contact v_(i+1) already supplies it.

Normalize that selected contact to the signed N,N,S prefix. The older
excursion uses L1(N)->W. The next excursion enters at R2(S)->W. They
share the outgoing W physical edge, at chronological ordinals 1 and 2.
Their sheet labels are precisely the selected top/middle exchange.
The L1 passage is on LEFT and the R2 passage enters LEFT from RIGHT.

Thus a count of odd intersections for interleaving boundary endpoints
can be satisfied at this boundary contact itself. It does not force an
extra deep L supplier or a second interior exchange. Any argument that
pushes the paths off the boundary must carry the induced endpoint
ordering and this shared-edge crossing through that push explicitly.
The actual L3 near-return control remains retained.

This is a precise obstruction to the naive interleaving count, not a
claim that every possible pair of excursions has no other intersections.

## 2. A different exact permutation cut separates physical side currents

Let sigma be the actual full-P edge-occurrence successor permutation.
At each of the ell selected curve contacts, swap the OUTGOING R0 and
R2 successors, leaving L1 and optional L3 unchanged. The changed pairs
are

    incoming R0(LEFT) -> outgoing R2(LEFT),
    incoming R2(RIGHT) -> outgoing R0(RIGHT).

All other visits stay on their actual side. Consequently the resulting
permutation sigma_side is a cycle decomposition of the disjoint physical
LEFT and RIGHT currents. It is NOT the L1/R2 sheet repair; the two cuts
must not be confused.

The signed K=1 endpoint maps give the entire cycle count exactly:

- RIGHT excursions have E(i)=i-1. Concatenating at the changed contact
  pairs therefore gives ONE RIGHT cycle, winding -1.
- LEFT excursions have G(i)=i+2. Concatenating them gives gcd(ell,2)
  LEFT cycles, each with winding 2/gcd(ell,2).

There are no extra cycles hiding away from the contacts: every actual
edge occurrence on either side lies in one finite excursion, and all
excursions have their contact endpoints in the complete crossing set.

Hence the total number of sigma_side cycles is

    1+gcd(ell,2).

For odd ell, the single LEFT cycle has winding TWO. It is not asserted
embedded or primitive. For even ell, there are two LEFT cycles of
winding one. The RIGHT and LEFT total homologies remain -1 and 2.
These cycles partition the physical edge occurrences and retain all
source L visits and arbitrary side detours.

As a consistency check, ell disjoint transpositions relate sigma_side
to the single P-cycle, so its cycle-count parity is correct:

    (1+gcd(ell,2))-1 congruent ell modulo 2.

No new speed bound or additive extra cycle budget is inferred. The
point is an exact boundary-aware permutation interface for comparison
with the separately signed chronological sheet repair.
