# What the signed D/C/V theorem implies for the larger seven-word language

The literal alphabet is D,C,V,U,F,Q,B, with words in `shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json`. No eventual restriction of an arbitrary finite-seed ant to this alphabet is assumed here.

The signed no-D six-word theorem excludes an infinite tail with only C,V,U,F,Q,B. The signed C-free theorem excludes an infinite tail with only D,V,U,F,Q,B. Therefore every hypothetical infinite finite-support seven-word tail has infinitely many D and infinitely many C macros.

Let T denote the group {F,Q,B}. The three signed restricted-language exclusions imply:

- D/C/F/Q/B exclusion: infinitely many U or infinitely many V;
- D/C/U exclusion: infinitely many V or infinitely many T;
- new D/C/V exclusion: infinitely many U or infinitely many T.

A finite alphabet cannot hide infinitely many group events among only finitely many of each member. These three pairwise disjunctions say exactly that at least two of the three groups {U},{V},T occur infinitely often. Thus the minimal unresolved recurrent support patterns contain D,C together with one of

- U and V;
- U and at least one of F,Q,B;
- V and at least one of F,Q,B.

Larger patterns, including all three groups, remain possible within this necessary condition. The statement does not imply eventual entry into one smaller alphabet and does not bound the number of switches. Concatenating individually finite-fuel regimes does not give a common global fuel bound because one regime may replenish resources used by another.

As a direct graph check, the existing actual coalesced seven-word quotient has one strongly connected component of214 vertices and993 edges, containing all seven labels. Therefore the new sublanguage theorem does not by itself collapse that graph to a finite transient part. This graph fact is a small exact check of the frozen artifact, not a new coverage claim for the global K graph.

Dependencies: `no_d_packet_fuel_theorem.md` (audit EK), `d_cfree_fuel_theorem.md` (audit DX), `d_turn_sublanguages.md` (audit EP), and `dcv_finite_tail_theorem.md` with its independent complete-family and potential audits. Global arbitrary mixed-K finiteness and the universal highway conjecture remain open.
