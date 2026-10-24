# Effective mass-only lifetime and the exact remaining seven-word bridge

23 October 2026, 21:00 UTC. Analytic corollaries submitted for independent review.

## 1. Raw-language interface

Use the literal raw alphabet D10, C15, V18, U28. The separate new finite-support complete-eight theorem, together with the already signed actual-marker boundary reduction, excludes an infinite actual raw-word concatenation from finite black support.

This lift does not assume uniqueness of packetization. Fix any supplied infinite raw decomposition. C^5 is raw-infeasible, so after at most four leading C macros there are infinitely many non-C bases. Group each base with its maximal following finite C run. Every non-C base begins the actual M11: V/U already have it as a prefix, while D10 obtains its eleventh L from the next raw macro. Thus every maximal packet has actual following M11. Literal C^4+M11, DC^4+M11 and V/U C^3+M11 bound run lengths. The signed twenty complete-context DCC-successor / DCCC-predecessor exclusions then remove DCC and all but a possible initial DCCC. A restarted infinite suffix would be an actual complete-eight factor on a still finite black board, contradiction.

There is no invented terminal marker: the argument is for an infinite raw decomposition, whose actual next raw macro always supplies the stated context. A separate digest may instead use the already signed finite-factor trimming argument; either route has the same conclusion. The raw-lift digest and complete-eight manifest are the authoritative dependencies, not this paragraph alone.

## 2. A total computable diameter-independent bound

For an integer m>=0, form the rooted four-ary tree T_m of ALL finite raw D/C/V/U concatenations with these properties:

- At each physical cell, its consecutive turns alternate L,R,L,R,... .
- At most m distinct physical cells have FIRST turn L.

Turn words determine the head path exactly, so both tests are decidable by finite literal simulation. The empty word is the root and every prefix in macro units remains in the tree. Do not identify equal local states or discard a coordinate merely because it is far away.

Every actual finite raw concatenation begun on at most m black cells belongs to T_m: a first-L cell was initially black, and different first-L cells are distinct initial cells. Conversely, each finite accepted word is physically realized by putting black precisely at its first-L cells, with all other cells white.

Suppose T_m were infinite. It is finitely branching, so König's lemma gives an infinite branch. Its union turn word has globally at most m first-L cells. Put black at exactly that FINITE union set. Every first-R cell is initially white and every repeat alternates, so the entire branch is one actual ant trajectory from that finite board, with the fixed supplied raw decomposition. This contradicts the raw-language exclusion. Therefore T_m is a finite tree.

Define L(m) as its maximum RAW FINE LENGTH, including zero for the root. Exhaustively traverse the tree, with no node/depth cutoff, and return this maximum. The proved finiteness makes this a TOTAL COMPUTABLE function. It is monotone in m because T_m is nested. Consequently every actual finite D/C/V/U concatenation begun at mass m has length at most L(m), independently of the initial seed diameter.

This is an effective definition with a proof of termination, not an assumed totality claim. No numerical prefix tree was evaluated in this work. The reference function mass_only_lifetime in the accompanying checker is deliberately not called by its fixed literal/graph checks. No practical complexity or small numerical value is asserted.

## 3. Effective control by F/Q/B occurrences

Use the exact seven words D,C,V,U,F,Q,B from the retained coalesced quotient. Let a finite actual concatenation begin at mass m and contain k foreign macros from {F,Q,B}. Define

    a_0=m,
    a_(i+1)=a_i+L(a_i)+6,
    G(m,k)=74k+sum_(i=0)^k L(a_i).

Split at the k foreign macros. Every intervening raw D/C/V/U block, even with no future language premise, is bounded by L at its entry mass. Every fine step changes black mass by at most one, and a foreign macro has net mass increment at most six and raw length at most 74. Induction therefore bounds each successive entry mass by a_i and the total raw duration by G(m,k).

Hence an infinite seven-word tail must have infinitely many F/Q/B occurrences. The bound is computable and diameter-independent but not claimed polynomial or useful numerically. It does not bound k, license importing a DCUV identity across a foreign macro, or prove the seven-word tail impossible.

## 4. Exact graph stopping point and recurrent supports

The fixed existing coalesced quotient has one cyclic strongly connected component with 214 vertices, 993 edges and ALL seven raw labels. Retaining only D/C/V/U-labelled edges leaves one cyclic component of 93 vertices and 417 edges. Retaining only F/Q/B-labelled edges leaves no cycle.

The new physical theorem prevents an actual finite-support path from eventually remaining in the D/C/V/U subalphabet. It does NOT delete its vertices from the full mixed component: the actual path may leave through F/Q/B and return, replenishing support between those visits. Individual sublanguage termination is not a common switching-fuel bound.

Together with the earlier signed no-D, C-free, and D/C/F/Q/B exclusions, any hypothetical infinite seven-word tail must contain infinitely many D, infinitely many C, infinitely many F/Q/B, and infinitely many U or V. Thus its minimal unresolved recurrent supports are exactly of the forms

    D,C,U,T  or  D,C,V,T,  with nonempty T subset of {F,Q,B},

where the minimal sets use one member of T and supersets remain unresolved. This strengthens the older three-group pairwise-disjunction note, but does not supply a new global K-label union.

No eventual restriction of an arbitrary ant to this seven-word graph has been proved here. The signed UNION6 theorem uses a DIFFERENT eight-packet graph with inherited successor constraints; it is not the complete-eight D/DC/V/VC/VCC/U/UC/UCC alphabet. The separate singleton theorems cannot be combined into a larger union merely from the present restricted-language exclusion. A new global K-event bridge and a common mixed-language resource would still be required.

## Fixed controls

check_dcuv_raw_tail_and_graph_bridge.py rederives the raw lengths, ten maximal packet expansions, five long-C conflicts, twenty complete-context boundary conflicts, and the exact three graph decompositions above. It performs no trajectory-prefix enumeration and makes no new global graph-coverage assertion.
