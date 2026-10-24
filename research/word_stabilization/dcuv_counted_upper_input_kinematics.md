# Counted protected upper-input transfers in recurrent DCUV

Status: independently SIGNED, 2026-10-23 03:19 UTC. No complete transfer is excluded by this low-count result.

The packet IDs in this computation are remapped from the signed recurrent-eight profile:

new0..7 = original [0,1,4,5,6,7,8,9] = D,DC,V,VC,VCC,U,UC,UCC.

Their raw C counts are [0,1,0,1,2,0,1,2]. The protected count is the number of raw C macros from source start through the strict intermediates, excluding the target. Counts0..3 are exact. State4 means at least4 and retains the actual target heading separately.

The full counted least-gap protocol is exactly the signed DCV protocol in dcv_protected_count_kinematics.md, with the signed recurrent-eight literal contexts and complete adjacency list. No DCV-only forbidden relation is imported. The ordinary base is empty on this recurrent-eight restriction; the protected base is the336,516-clause signed HB restriction, freshly replayed in chronology_dcuv/recurrent8_kernels/.

## New short-turn kinematics

At each macro pose use the square center s=p+rot((-1/2,-1/2),h). Literal center increments in incoming heading are D:(1,1), C:(1,1) with a left quarter turn, V:(1,3), and U:(0,4). D,V,U preserve heading.

For a proposed counted pair, subtract the complete source displacement, including its C turns, and rotate the remaining center displacement into the source exit heading. Call the resulting integral vector(x,y), and let r be the exact number of remaining C macros.

If r=0, x=d+v and y=d+3v+4u with d,v,u>=0. In particular x>=0, y>=x, x+y is even, and x=0 forces y divisible4. Only these necessary conditions are used.

If r=1, subtract the C increment(1,1), which is in the source-exit heading. The remaining(X,Y) is a sum of generators(1,1),(1,3),(0,4) before the turn and(-1,1),(-3,1),(-4,0) afterward. Thus Y>=0, X<=Y and X+Y is even. If Y=0, only(-4,0) can occur, so X is divisible4. Zero-length straight runs remain allowed.

For r>=2 and overflow, no additional kinematic exclusion is used. The exact heading relation h+count=0 mod4 and count>=source-C-count are still imposed below overflow.

## Discovery output

Source: dcuv_recurrent8_count_kernel.cpp. The frozen mapped inputs, family queries and closure are under chronology_dcuv/recurrent8_counted/.

The candidate set starts at828,300 counted clauses and stabilizes after15 deletion rounds at422,015 clauses. Every one of the1,188 upper-input producer alignments is forbidden for its unique heading-compatible exact count in0..3, while every overflow query remains admitted. Thus any actual produced identity consumed at one of U's three upper inputs would require at least4 C macros between producer and consumer starts.

For the two stubborn source-D controls, (0,7,2,2,S),q=(2,0) requires at least6 C macros and (0,7,5,0,W),q=(2,0) at least5, by heading congruence. This is not an all-length impossibility theorem and does not prove initial fuel per U.

Independent validation: audits/check_dcuv_counted_protected_independent.cpp, check_dcuv_counted_queries_independent.py and dcuv_counted_replay/{clauses,queries,inputs_manifest}.json. All422,015 clauses,12,023,773 inference options and142 short controls pass. All4,752 exact count0..3 queries exclude; all1,188 overflow queries remain.
