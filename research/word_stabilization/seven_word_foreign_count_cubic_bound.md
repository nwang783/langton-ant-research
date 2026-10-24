# Seven-word duration controlled by non-DCV occurrences

Status: independently SIGNED, 2026-10-23 03:03 UTC. This is not a proof of finite U/F/Q/B occurrence or of global highway capture.

Let W be a physically feasible finite concatenation of the exact seven macros D,C,V,U,F,Q,B from shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json. Let m be its entry black mass and k its number of U,F,Q,B macros. Define deliberately conservative constants

G=193(k+1)+74k=193+267k,
B=57+38(m+G)+3G+60k,
R=ceil(2B/5)+G+1,
t=floor((2R+1)^2/2).

Claim: the fine duration of W is at most

G+20R(t+1)+74t.

In particular, for fixed finite m, an infinite seven-word tail would require k(T)=Omega(T^(1/3)). This strengthens finite-occurrence exclusion quantitatively without asserting that any particular non-DCV macro must recur at that rate.

## 1. Retained DCV factors and discarded bridges

Split W at its k foreign U/F/Q/B macros. There are at most k+1 DCV blocks. Apply the independently signed arbitrary-factor DCV trimming lemma to each block. Its retained portion, if nonempty, is a complete recurrent-five packet factor, and at most193 fine steps per block are discarded. Each foreign macro has length at most74. Consequently all discarded prefixes, suffixes and inter-factor bridges have total fine length at most G. If no retained factor remains, W itself has length at most G.

Suppose retained factors remain. Anchor coordinates at the entry of the first. Its black mass m0 is at most m+G, since every discarded fine step can increase mass by at most1. There are at most k bridges between consecutive retained factors. We do not import any DCV transfer clause across such a bridge.

## 2. Typed potentials and a bridge reset

Within each retained factor, use the signed four rotated DCV max potentials: core term 2L(p)+a_h for L(x,y)=x+3y and a=(2,52,54,-8); typed output weights between -60 and60; baseline weight60, dominating every DCV input weight.

Initially track the core only. Initial residual black cells are inactive. In a retained factor, a newly consumed inactive initial identity activates at baseline60 at cost at most76, as in the signed deferred-activation proof. At most m0 initial identities exist. Surviving baseline identities always dominate the required DCV input weight. Typed identities may invoke198 only within their actual retained DCV factor.

At a bridge of fine length g, retire all previous producer types. At its end give baseline60 to every surviving active black residual cell, every old core black cell surviving outside the new core even if the bridge never reads it, and every newly produced or newly encountered black residual cell. Keep the new core separate. Untouched inactive initial black cells outside the new core stay inactive. Cells entering the core are accounted for by the core term; if a subsequent DCV packet emits one as a residual output it receives a fresh typed identity by the exact ledger.

The bridge increases each max potential by at most6g+120:

- An old active residual term rises by at most120 when reset from its old weight, at least-60, to60.
- An old core black cell becoming residual costs at most74 relative to the old core term, from the signed core maximum14 plus baseline60.
- A newly changed or encountered residual cell lies on the bridge's physical read path. Its displacement has l1 norm at most g, so its baseline term is at most6g+68 above the old core, since min a_h=-8.
- The new core term is at most6g+62 above the old core, since max a_h-min a_h=62.

Taking the maximum is bounded by6g+120. This reset has no dependence on the number of active residual cells, and does not assume any residual-token identity persists through a bridge. Inactive initial cells met in a bridge need no additional76 charge. At retained-factor entry, cells known only because they belong to the new core are handled by that core term, not silently assigned an unbounded residual weight.

Thus every retained-boundary rotated max is at most54+76m0+6G+120k. The minimum active weight-60, the signed fine-prefix maximum36 and core maximum14 give the strip bound B above for all retained-factor fine read cells, core cells and produced black cells. The four strips imply a radius-ceil(2B/5) square.

Every bridge and the initial/final discarded pieces lie within G steps of a retained boundary. Adding G+1 to the radius covers every fine read and endpoint of W, including its initial prefix and terminal endpoint. Remote initial black cells outside this square remain unchanged.

## 3. Mass and duration

Exact macro lengths and mass increments (R count minus L count) are

D:(10,0), C:(15,3), V:(18,4), U:(28,4), F:(56,2), Q:(64,6), B:(74,6).

All changed cells lie in the radius-R square, so final mass minus initial mass is at most (2R+1)^2. Every non-D macro adds at least2 black cells, giving at most t non-D macros. Every D run translates by a fixed rotated(1,1), hence contains at most2R macros. There are at most t+1 runs, and each non-D macro has length at most74. This gives20R(t+1)+74t when retained factors exist. The addedG covers the empty-retained case uniformly.

The resulting expression is cubic in m+k, with intentionally loose constants. The only language-specific exclusion used inside a retained factor is the already signed DCV theorem; no foreign-language version of198 is presumed.

## Explicit recurrence-rate form

For integer R, t=2R(R+1). Also R<=3383+16m+4670k and G<=R. Hence the displayed duration is at most400(3383+16m+4670k)^3. At a macro endpoint of fine elapsed time T this implies

k >= ((T/400)^(1/3)-3383-16m)/4670.

A negative right side gives no information. For arbitrary fine times, using the preceding macro endpoint loses at most74 steps and preserves the same asymptotic cube-root statement. These deliberately coarse constants are included only to make the asymptotic implication explicit.

Independent analytic and literal-arithmetic validation: audits/check_seven_word_bridge_constants_independent.py/json, including old-core reset handling and the optional explicit400 constant.
