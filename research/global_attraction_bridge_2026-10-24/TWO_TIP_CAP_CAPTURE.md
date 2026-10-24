# Three causal two-tip-cap families still cannot turn wake length into outward growth

Status: author checked; frozen for independent audit. This extends the exact one-cap test, not the arbitrary-controller classification.

## Bounded architecture and outcome

Take the same six-cell seed S, head (1,1), S, and a_K=(5+2K,-4-2K), K>=0. Add exactly two initially black cap cells, a_K and a_K+b, for one of the three fixed offsets

    b=(1,0), (0,-1), or (1,1).

Every original board has exactly eight black cells. The first and third variants have the whole half-plane x+y<1 white; the south variant has x+y<0 white. These are actual finite causal launches: the ant writes its own K-period standard wake from the original seed, not from an edited late wake state.

All three families capture for EVERY integer K>=0. For K>=11:

| second offset | actual first read after main cap | fixed certificate delay | endpoint relative to a_K | final drift |
|---|---:|---:|---|---|
| (1,0) | never | 2184 | (6,14), W | (2,2) |
| (0,-1) | 1857 | 2184 | (6,12), W | (2,2) |
| (1,1) | 86 | 2392 | (8,16), W | (2,2) |

The minimum x+y in every such complete orbit is -19. Thus there are 20 strict pristine SW record cuts in the east and northeast variants, and 19 in the south variant. Extra wake length produces no additional outward SW depth. The east cell is inert; the south and northeast cells are genuine subsequently consumed inputs, not irrelevant decorations.

For all parameters including short wakes, there are at most 14088 guard-avoiding genuinely pristine record TIME CUTS among the eight coordinate/diagonal directions. The direction-marked bound is 112704. Both bounds are only for these three specified eight-cell families.

## Why both caps are genuinely initially unread

The signed one-cap launch gives W H^K H[0:45], reaching a_K at T_K=279+104K. Relative to the unperturbed wake, the second cap's first reads have offsets 60,46,75 respectively, all strictly after the main cap's offset45. All intersections with the earlier finite launch have negative wake-ray indices. Hence neither cap is read before T_K for any K>=0. The actual first turn there is L, and each stored post-contact word begins with that actual read.

This checks the initial state and first-contact chronology, not merely a geometric placement near a prepared infinite wake.

## All-parameter full-field transfer

At main contact, normalize a_K to zero. The full board is exactly the one-cap contact field B_K XOR {b}. Therefore the parameter difference between K and11 is still B_K XOR B_11; the fixed additional cap cancels in this comparison.

For EACH of the three actual post-contact continuations, the checker verifies that the same 50 source rays and32 backward wake rays from the one-cap proof miss every finite continuation read and every infinite final-tail phase ray. These are 246 independent complete-ray exclusions. Consequently every parameter-dependent archived cell remains unread throughout the complete future. The K=11 full-field future transfers to every K>=11 by literal read induction, with no discarded output and no inferred repeatable state.

This is stronger than testing a large finite wake or an infinitely supplied rail. It identifies why the arbitrarily long extra wake is never recruited by these three finite tip perturbations.

## Short wakes and budget

The literal certificate retains all complete final boards and full words for K=0,...,11 in each variant: 36 finite controls, including the three anchors. Every final tail passes an exact all-ray parity test. The maximum post-contact sufficient certificate delay is 13104, at K=1 in the south variant. This unusually long isolated transient is not parameter-growing outward behavior. No chosen certificate time is claimed to be the earliest periodic-word onset.

Every full history decomposes as the fixed arbitrary launch W of length234, one finite standard piece H^K H[0:45], an arbitrary post-contact piece of length at most13104, and one infinite standard tail. The signed standard-piece interior lemma therefore gives

    234 + 13104 + 2*375 = 14088

guard-avoiding pristine record time cuts. A current pristine half-plane is required; ordinary head records inside prepared material are not counted by substitution.

For K>=11 the exact path minimum calculation includes W, one tangential H period, the complete post-contact continuation, and one outward-in-the-opposite-direction final period. The last tail has x+y drift+4, so later periods cannot lower the minimum. Every first visit to a level strictly below the initial minimum black level is pristine. Level1 is blocked initially in all variants, and level0 is additionally blocked by the still-unread south cap. This gives the stated20/19 SW records.

## Scope

This is a falsifier test that failed in a provable way: three nearest unread tip perturbations do not make the stored tangential resource yield increasing outward progress. It does not classify all two-cell caps, all bounded tip patterns, or all standard-wake scattering. Nor does it establish a universal mass-only pristine-record budget.

Run `python check_two_tip_cap_capture.py`. The manifest binds the literal certificate, complete checks, and the exact one-cap and standard-piece dependencies.
