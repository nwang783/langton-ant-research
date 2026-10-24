# Protected-token counts and global short-turn kinematics

Status: the analytic protocol and frozen count closure below are submitted for independent audit. They do not exclude the >=4-C case of any of the original 69 potential-violating transfers.

## 1. Counted protected premise

Use the seven literal maximal-C packets D,DC,DCC,DCCC,V,VC,VCC and their actual M11 right contexts. Let c(A) be 0,1,2,3,0,1,2 respectively. A counted protected pair consists of packets A,B, their relative pose (p,h), a physical q, and k=min(4,N), where N counts raw C macros from the beginning of A up to but excluding the beginning of B. In addition to this count, q is black immediately after RAW A and every strict intermediate packet's complete RAW+M11 context avoids q.

For k<4, the endpoint heading requires h+k=0 mod4 and k>=c(A). A count4 state means >=4, not exactly four. It retains the actual relative heading separately. A finite stored universe is used only for candidate forbidden clauses. Missing types are possible unless the already signed ordinary/protected relation, the exact heading/count condition, or the global kinematic condition excludes them.

## 2. Global kinematic necessary conditions

At a marked pose (p,h), place the black-square center at s=p+rot((-1/2,-1/2),h). Literal geometry gives the following center increments in the old heading frame:

- D: (1,1), with no heading change.
- C: (1,1), with one left quarter turn.
- V: (1,3), with no heading change.

For a proposed pair with k<4, subtract the COMPLETE source packet's known displacement and rotate into its exit heading. Call the remaining center displacement (x,y), and put r=k-c(A). These are integer coordinates; a nonintegral result is impossible.

If r=0, only D and V can occur between the source endpoint and target start. Therefore x=d+v and y=d+3v for d,v>=0, implying x>=0, x<=y<=3x and x+y even. The test permits d=v=0, so adjacency is not accidentally excluded.

If r=1, first subtract the unique C center increment (1,1), which occurs in the source exit heading. Before that C, D and V contribute (1,1) and (1,3); afterward they contribute (-1,1) and (-3,1). For the remaining sum (X,Y), every generator has positive Y and satisfies -3Y<=X<=Y. Thus Y>=0, -3Y<=X<=Y, and X+Y is even. Again zero straight runs are allowed. Only necessity is used.

For r>=2, the implementation makes no additional kinematic exclusion. For overflow k=4, it likewise makes none. These necessary conditions are valid at arbitrary separation, so they remain available when a pose or q falls outside the finite candidate universe.

## 3. Counted induction rules

The proof parameter remains the actual number of packet indices between A and B, not the C count. Thus same-count dependencies may be used only on strict proper subpairs.

The adjacent and gap-two bases are removed from the candidate set whenever literal physical controls realize the protected premise. Direct black contradictions and already signed ordinary/protected clauses remain available.

For a gap of at least three, let C be the successor of A and D the predecessor of B. Both avoid q in complete context. If r is the capped C count from the beginning of C to the beginning of D, the outer count is cap(c(A)+r+c(D)). The three proper pairs A→D, C→B, C→D have capped counts cap(c(A)+r), cap(r+c(D)), and r. The neighbor rule checks all count choices and all literal successor/predecessor types; at least one proper pair must already be forbidden for every possibility.

For the first odd intervening reader R of an equal-letter source/target cell, the counts u on A→R and v on R→B satisfy cap(u+v)=k. Its full context avoids q. A reader may be omitted only if one proper counted pair is forbidden, or an older ordinary/protected clause excludes it. This is the original first-odd-reader argument with an additional count partition.

The two-cell rule uses states (u,color), with u in {0,1,2,3,4} and color in four bit states. It starts after A at u=c(A), and ends just before B at u=k. Free increment edges u→u+1 overapproximate any number of untracked intervening C turns. A tracked reader R at count u contributes the literal two-cell partial-color transition and goes to cap(u+c(R)). It is retained whenever some v with cap(u+v)=k has both proper counted pairs still possible. Every actual intervening history maps to such a path, so failure of reachability proves the outer clause. No untracked count increment is required after state4 because that state already represents all larger values.

## 4. Frozen computation

`generic_protected_kinematic_count_kernel.cpp` includes the exact two-cell/protected geometry from `generic_protected_patch2_kernel.cpp` and implements the counted relation. The signed-base invocation is:

/tmp/dcv_kinematic_count seven_sub_dcv_kernel.input seven_sub_dcv_star4_kernel.tsv dcv_protected_patch2_kernel.tsv dcv_protected_kinematic_count_signedbase dcv_bad_transfers_rows.txt

The original signed protected base has102,122 clauses. The new candidate set starts at215,183 counted states after short controls, and stabilizes at113,750 clauses after16 deletion rounds. The file `dcv_protected_kinematic_count_signedbase.tsv` records each final clause and its inference kind/witness cells. Each of the69 exact low-count target queries is forbidden; every overflow query remains possible in this abstraction. If independently replayed, the conclusion is that every remaining potential-violating transfer must contain at least four C macros between source start and target start. It is not a global bound on C turns, a freshness theorem, or an exclusion of full D/C/V tails.

## Independent signoff, 2026-10-23 00:20 UTC

Audit FX independently checked all 113,750 clauses and all 276 finite-count target queries, using only the original signed ordinary/protected bases. Files: `../audits/check_counted_protected_clauses_independent.cpp/json` and `../audits/check_counted_target_queries_independent.py`, `../audits/counted_target_queries_independent.json`. Every overflow query remains. This replaces pending-audit qualifications above, not the explicit scope limitations.
