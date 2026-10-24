# No supplied minimal-pose repair at the owned return contact

Scope: the signed unmodified394-cell family N=3M+4, M>=1, at its first old launch-memory contact. Any added initial black cells must be genuinely fresh, meaning disjoint from the complete preceding READ history. No already-owned cell may be altered by intervention.

The contact is q=(14,-7), incoming W. The prescribed15324 word wants R and would reach (14,-6), incoming N, but q is black and forces L. Consider replacing this one intended step by an internally ant-legal turn word of length at most9, with exactly that final position and heading.

Alternating movement axes imply the length is1 modulo4: the number of vertical moves is (n+1)/2 and must be odd to have vertical displacement1. Thus only lengths1,5,9 need consideration. The first turn is necessarily L.

Complete geometry gives zero candidates of length1, two of length5, and18 of length9. Rejecting any word that reads the same cell with equal consecutive turns leaves exactly

- length5: LLLLR;
- length9: LLRRRRLLR, LLLRRRRLR, LLLLRLLLL.

Every remaining word begins LL. Its second read is (14,-8), which is white in every family member. Its exact launch histories are L at5209, R at5213, L at5217, so its last launch read leaves it white. The cell misses the entire future4352 READ set. The source-transition and complete earlier return phases have respective lower u bounds156M+182 and182, whereas this cell has u=6. Finally, the fixed17353-read extra return prefix before q also misses it. It is therefore still an already-owned white cell at the proposed repair.

Consequently all four internally legal candidates fail at their second read. No preloaded fresh additions anywhere can repair this conflict without changing an earlier read. There is no survivor whose endpoint or later future could be mistaken for a physical repair.

This excludes exactly the supplied length<=9 exact-pose replacement. It does not exclude a longer detour, an earlier deviation, a changed launch, or a different outgoing pose. No length escalation is performed.

Artifacts: check4352_minimal_contact_repair.py and prepared4352_minimal_contact_repair.json contain every geometric candidate and its first internal or inherited-color conflict. The initial proof is author-checked, pending independent review.
