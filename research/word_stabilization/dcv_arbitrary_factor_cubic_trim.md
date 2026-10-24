# Boundary trim for an arbitrary finite D/C/V factor

Status: SIGNED by independent analytic and literal boundary review, 2026-10-23 01:58 UTC. The DCC·D exception was identified and repaired before signoff. No global ant-runtime bound is asserted.

Let f(m)=20R(t+1)+18t, where R=ceil((114+76(m-5))/5), A=(2R+1)^2 and t=floor(A/3), be the signed duration bound for context-complete recurrent packet factors. For m>=5 this function is increasing.

Claim: every physically feasible finite factor which is a concatenation of the exact macros D10,C15,V18 and begins with m black cells has at most

193+f(m+21)

fine steps. The bound is independent of the initial seed diameter.

1. Remove its leading C run. Literal C^5 is infeasible, so at most four C macros are removed, costing at most60 steps and increasing mass by at most12. If nothing remains, the claim already holds.
2. Remove the last entire maximal packet A C^k, A in{D,V}. Even without an M11 after it, C^5 is infeasible, so k<=4. This removes at most18+4*15=78 steps. The removed packet begins with an actual M11: V begins with it; D followed by C has its next L; and a final standalone D is followed by a forced L because its endpoint is its phase6 R-read cell, never reread later inside D. Thus this removed suffix supplies the required actual right marker to the retained prefix.
3. Handle the one terminal boundary exception explicitly. A retained final DCC may precede a removed standalone D: both raw DCC·D and DCC·D·L are feasible. One cannot invent a full M11 after that removed D; the second invented L would cause the first conflict at read51. In precisely this case, also remove the final C of the retained DCC, leaving DC. The removed C begins with an actual M11 and supplies the correct marker for this retained DC. This augmented suffix costs only15+10=25 steps, still within the78-step suffix budget. No other removed terminal packet permits the exception: raw DCC·V and DCC·D·C are infeasible, and these are prefixes of every other possible removed terminal packet after DCC.
4. Every remaining retained packet has a following actual packet or the just-exposed actual C marker. The signed short grammar excludes C^4 M11 and V C^3 M11. An internal DCC has a complete following packet, including its actual endpoint marker, and is excluded by the signed no-successor relation. The only possible terminal DCC has already been shortened in step3. The signed predecessor exclusion likewise leaves DCCC possible only as the first retained packet. Remove that initial DCCC if present, costing55 steps and mass gain9.

The remaining factor consists entirely of recurrent D,DC,V,VC,VCC packets, each with actual M11. Its initial black mass is at mostm+21, because only the leading C run and optional first DCCC were removed before it. The signed bound gives at most f(m+21) steps. The three removed pieces total at most60+78+55=193 steps. If the pieces overlap because the original factor is short, assigning them these separate maxima is conservative.

The endpoint-forced L after a final D is an actual ant consequence, not an artificial choice of a future context. No assumption is made that the ant continues in the D/C/V language after the finite factor. Source dependencies are the signed literal packet-boundary ledger and the separately signed deferred-activation cubic bound.

Literal boundary controls are reproduced by check_dcv_arbitrary_factor_trim_controls.py and stored in dcv_arbitrary_factor_trim_controls.json. In particular, the positive DCC·D·L control prevents silently reintroducing the invalid endpoint-marker inference. The terminal suffix charge is max(78,25)=78, not78+15.

Independent validation: audits/check_dcv_arbitrary_factor_trim_independent.py/json reconstructs the boundary identities and checks all17,938 feasible factors through nine macros, including273 standalone-terminal-D exceptions. These finite controls supplement the all-length boundary proof; they are not its replacement.
