# Arbitrary finite DCUV factor: boundary extension of the epoch bound

Status: independently SIGNED, 2026-10-23 02:56 UTC. The context-complete recurrent-eight epoch bound and this arbitrary-factor boundary extension are both signed.

Let F(m,u)=20R(t+1)+28t, where B=57+38(m−5)+60u, R=ceil(2B/5), and t=floor((2R+1)^2/3). This is increasing in m>=5 and u>=0.

Claim: a physically feasible finite concatenation of the exact raw macros D10,C15,V18,U28, beginning with m black cells and containing u raw U macros, has at most

203+F(m+21,u)

fine steps. Its future need not remain in the language.

Use the already signed arbitrary D/C/V trimming argument with the following explicit changes. Remove at most four leading C macros, costing60 steps and at most12 additional entry mass. Remove its final maximal packet A C^k, where A is D, V or U and k<=4; this costs at most28+60=88 steps. This packet begins with actual M11, except standalone terminal D, for which the endpoint-forced L supplies its entry M11 exactly as in the signed D/C/V trim.

The terminal DCC·D exception is retained and repaired identically: if the retained last packet is DCC and the removed packet was standalone D, remove its last C as well, exposing a recurrent DC with an actual C-entry M11. The combined suffix cost25 is inside88. Other terminal successors cannot leave this exception: raw DCC·D·C, DCC·V and now DCC·U are each infeasible. The first conflict in DCC·U is at zero-based read52, earlier than the end of U.

Actual right markers exclude C^4, V C^3, and U C^3. The additional U C^3 M11 conflict is at zero-based read81. The independently signed all-ten boundary ledger excludes every internal DCC and every noninitial DCCC. Remove a possible initial DCCC, costing55 steps and mass gain9.

The remaining complete factor therefore uses the eight recurrent packet types, has entry mass at most m+21, and has at most u U macros. Apply the signed epoch-reset bound and monotonicity. The discarded pieces cost at most60+88+55=203. If the factor is too short for disjoint pieces, these separate upper charges remain conservative.

Additional literal controls are stored in dcuv_arbitrary_factor_trim_controls.json. The existing signed DCC·D and DCC·D·L positive controls remain essential; no full future marker is invented at a removed standalone D endpoint.

Independent validation: audits/dcuv_arbitrary_factor_trim_independent.json. No future-language premise or U-count bound is inferred.
