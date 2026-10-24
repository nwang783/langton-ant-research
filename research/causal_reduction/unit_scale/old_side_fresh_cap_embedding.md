# Old-side returns contain arbitrary causally fresh finite caps

23 October 2026, 15:09 UTC. Author semantic construction using the signed exceptional return map and clean-front identity; independent review requested. This is an exact prepared-interface embedding and finite-prefix realization, NOT a capture or noncapture conclusion.

## Canonical data and two distinct ownership restrictions

Use the signed notation from nonlinear_global_budget_2026-10-23/exceptional_arbitrary_base_return_map.md and clean_reverse_interface_identity.md. The incoming13-cell standard state S starts at(-15,10,W), with drift d=(-2,-2). Its exceptional phase72 obstacle has stable depth11 and replay length52262. The complete terminal state R has2216 black cells, head r=(0,-49), heading E, and future standard drift e=-d=(2,2).

Let Q be the complete104 read-slot set at R, and M its odd-read mask. Define the strict-past READ set and causal reverse field

    P_minus = union_(j<0)(Q+j e),
    C_rev   = XOR_(j<0)(M+j e).

Each individual cell has finitely many contributing slots. In particular C_rev is white outside P_minus. Strict-past ownership refers to P_minus, NOT merely the black set C_rev: an initially added black bit at a previously read white cell would still change the earlier trace.

The original incoming complete future READ set is

    P_in = union_(j>=0)(Q_in+j d).

For the canonical standard base, a finite discrepancy D is inert for the entire incoming trace if and only if D is disjoint from P_in. Sufficiency is deterministic induction. Necessity follows at the first visited discrepancy cell, since the same earlier trajectory has made the same flips and cannot cancel an unread discrepancy.

The reverse and incoming normal bands are far apart, but that fact alone does not authorize arbitrary all-plane cap edits at a reverse cut. The separate P_minus condition must still be respected.

## The embedding

Let F be ANY finite set of cells with

    F intersection P_minus = empty.

These are additions-only black caps on cells that are white and genuinely unread in the reverse causal past. F can span any finite transverse range; it need not be confined to the reverse read strip. For an integer T>=1 put F_T=F+T e.

There is a computable T0 such that for every T>=T0:

1. X_T=S union F_T is a finite base already following incoming standard H forever.
2. F_T misses every translated stable-replay read set A+n d for n>=0, the original finite inverse-ten history, and the canonical base itself.
3. Every strict-past reverse period before head r+T e also misses F_T.

For items1 and2, all incoming and stable-replay rays go in direction d, while the finite cap is shifted in the opposite direction e. For example require the minimum x-coordinate of F_T to exceed the maximum x-coordinate of Q_in, A, S and the original inverse-ten set. Every further d translate only decreases x, so this ONE finite bound works for all n. For item3, an intersection of F_T with Q+j e, j<T, would translate to an intersection of F with Q+(j-T)e, contradicting the strict-past hypothesis. This property is not weakened by increasing T.

Thus the original incoming forbidden strip imposes NO additional finite-cap restriction after a sufficiently long reverse-direction translation. The intrinsic reverse strict-past restriction remains exact and cannot be removed by that translation.

## Exact whole infinite interface

The signed arbitrary-base return map is safe here with K=0. Its clean infinite old-side interface at head r is

    C_rev XOR W_[0,infinity) XOR F_T,

where W_[0,infinity) is the COMPLETE original settled incoming halfwake. Its normal band[-28,-18] misses the reverse read band[42,52], so the original wake is unchanged by the clean reverse periods. The preceding ownership facts make the next T reverse periods legal and untouched by F_T.

At head r+T e, translate the ENTIRE field back by T e. The exact resulting state is

    head r, heading E,
    C_rev XOR F XOR shift(-T e,W_[0,infinity)).       (1)

No old wake has been deleted. It recedes longitudinally as T grows. Because its generating mask is finite and its halfline points in direction -e, it misses any prescribed finite neighborhood for sufficiently large T. Hence(1) converges locally to C_rev XOR F.

## Genuine finite initial seeds and arbitrary fixed continuation length

For n>=0 place the exceptional obstacle at its canonical depth11+n. Use the finite initial seed

    S union F_T union {o+(11+n)d},

with the canonical phase72 offset o. Once T is large as above these sets are disjoint, so its initial mass is exactly14+|F|, independent of n and T. If necessary, omit finitely many n to preserve the original inverse-ten history; this changes no limiting claim.

The retained pristine theorem and the untouched-cap argument give a continuous actual trajectory through n incoming periods, the stable replay and n+T reverse periods. Its elapsed time at the normalized cap section is

    52262 + 208n + 104T.

Its COMPLETE field, before translating back, is

    F_T XOR shift(-n e,R.black) XOR W_[0,n)
        XOR XOR_(j=-n)^(T-1)(M+j e).                (2)

This formula keeps all old debris, both archives and the finite remote endcap. For fixed T, letting n grow gives the signed infinite interface. Then increasing T removes the old halfwake only on any chosen bounded observation region, as in(1).

Consequently EVERY specified finite continuation of the ideal state(C_rev XOR F,r,E), including its literal turn word, full visited-cell histories and finite inverse-ten suffix, is realized exactly by some sufficiently large finite seed from(2). The proof is finite propagation after complete-field local agreement. It does not promote local convergence to an all-future capture statement or assert that one fixed seed realizes every continuation length.

## Meaning for the open scattering route

The exceptional return interface does not automatically reduce the complexity of the causally fresh cap class: every finite such cap is present, with constant initial-mass overhead14. The original incoming read restriction can be moved away, while reverse-causal ownership cannot. Arbitrary edits on already read reverse cells, arbitrary whole-plane finite XOR caps at the same prescribed cut, repeated autonomous scattering, and universal capture remain outside this conclusion.
