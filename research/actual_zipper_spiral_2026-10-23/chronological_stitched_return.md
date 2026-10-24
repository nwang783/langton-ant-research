# Charged chronological positive-positive reuse of the complete first R output

Frozen 2026-10-24. Exact finite full-board controls, not a claim of an all-parameter theorem or recurring growth. This supersedes the exploratory `charged_left_return_probe` snapshots as the authoritative finite statement. All constants below describe q=3,5,7,9,15 exact controls unless explicitly called a conjectured all-q extension.

## What is proved by literal replay

A complete finite initial board is supplied before the first update. No cells are added between phases. The ant executes:

1. A maximal ordinary w epoch of positive gain q-2, consuming only the prescribed old staircase spiral input.
2. A charged chronological old return guide, ending at the FAVORABLE INNER endpoint of the complete first-R output. Every first-R lifetime survives unchanged through this transport.
3. A second maximal ordinary w epoch of positive gain q-2. It consumes EVERY first-R lifetime, ALL old corner stitches, and exactly two transport-born lifetimes. It consumes no lifetime born in the second epoch.

The transport has exactly two w-exceptional blocks: an old cycle R L at its beginning and RRRRL at its end. The first and second ordinary epochs have no w exceptions. However the second epoch contains many z-cycle births/erasures. These are fully counted, not erased from the board or treated as free.

This is actual chronological recycling of ALL gain-bearing output, not an alternative-entry teleport, an independent pre-funded second spiral, or just mass-neutral rod carry. The return GUIDE is nevertheless pre-funded, of quadratic size, and mostly destroyed. No whole-state recurrence follows.

For q=5: entry mass430 =217 input +4 stitches +209 guide cells. The first ordinary epoch has 220 R lifetimes and gain+3. Return transport418 updates preserves all220. The second maximal ordinary epoch has 226 L,229 R, gain+3; its L ownership is220 first-R,4 old stitches,2 transport-R. Total w exceptional count is2; complete second-epoch z counts are115 births and116 erasures.

## Deterministic geometry

`return_guide_geometry.py` supplies the exact seed. Start (1,1), E. Use a spacing-12 q-run CCW coarse spiral with odd q>=3. Map (a,b) to fine w (a-b,a+b), replacing a coarse step by horizontal then vertical unit steps. Seed the q-1 corner stitches joining the external tips of each consecutive positive-turn pair. Append one clockwise unit hook to the fine spiral input.

The guide lies at coarse LEFT offset d=2 from the input, hence away from its first-R output on the right. Its exact outer patch includes a unit old w cycle attached to the terminal input vertex U and a long path from its adjacent vertex to the reverse left-offset spiral. Its inner patch winds around the initial input endpoint and terminates at fine w (0,-1). Every three-edge unit-U in the guide is replaced by its direct one-edge chord BEFORE seeding. This smoothing is essential: the rejected unsmoothed guide created its own forward-chord obstruction. The old outer cycle supplies the initial renewal; the final RRRRL connects to the preserved first-R inner endpoint (1,-1). At that moment the actual physical pose is (0,3), N.

The entire literal seed, all three words, final black board and final birth-origin labels are in `chronological_stitched_return_witness_q3.json` and `_q5.json`. No simulator teleport or conditional board completion is used.

## Exact formulas, checked instances

Let n=12((q+1)/2)^2 for odd q. The explicit deterministic construction and the following formulas are verified for q=3,5,7,9,15. An analytic all-q routing proof is still pending independent review; a finite list alone does not disprove any asymptotic lower bound.

Initial input=2n+1, stitches=q-1, guide=2n-10q+43, complete M=4n-9q+43. Initial cycle ranks (w,z)=(1,0).

- First epoch: L=2n+1, R=2n+q-1, G=q-2, T=4n+q. No births or erasures in either graph. Ranks remain(1,0).
- Transport: L=2n-10q+41, R=2n-11q+50, G=9-q, T=4n-21q+91. Births(w,z)=(0,2), erasures=(1,1). Exactly2 w-exceptional blocks, first r1/old-cycle L and last r4/new-bridge L. Ranks afterward(0,1).
- Second maximal epoch: L=2n+2q, R=2n+3q-2, G=q-2, T=4n+5q-2. Births(w,z)=(0,n+(3q-1)/2), erasures=(0,n+(3q+1)/2). It is w-ordinary throughout, but NOT paired-forest throughout. Ranks afterward(0,0), and the current w vertex is isolated.

Total T=12n-15q+89, final mass M+q+5. Total w births0/erasures1 and w-exceptional blocks2. Total z births and erasures both n+(3q+3)/2. Thus a cost that counts BOTH graph erasures is large even though w exceptional count is small in these controls.

The first epoch has no same-epoch L on an R birth. All2n+q-1 first-R lifetimes survive the complete transport, then are consumed in the second epoch. All q-1 stitches are also consumed there. The second epoch ends with an additional R L L tail, consuming two transport-R lifetimes, so its maximal gain is q-2, not the q-1 gain of the shorter first-R-exhaustion checkpoint.

An optional actual predecessor is obtained by adding black cell(0,1) and starting there,S. Its L leads to the displayed entry. That predecessor is a w-cycle erasure, not a bridge. Counting it adds one constant w exception and one cell; do not label it a paired-bridge predecessor.

## Exact final-state obstruction to iteration

The guide is NOT regenerated. All but THREE original guide lifetimes are consumed by transport; no original input or stitch lifetime survives. Final origin counts are:

-3 original guide lifetimes;
-2n-11q+47 transport-R lifetimes;
-2n+3q-2 second-epoch R lifetimes.

Spatially, in each checked instance NO original input or stitch cell is black at the final cut; only FOUR original guide cell positions are black (three surviving original lifetimes and one recolored position). The complete final graph is a forest, split into many components, with current w vertex isolated. The largest w component in each checked instance has only12(q+1)+5 edges, compared with entry M=Theta(q^2). This is a measured exact property of the supplied controls, not yet an all-q fragmentation theorem.

In particular the old stitches that made the first output one path are gone, and no black cell is left at their positions. The final field is not another seed of the same form, not a translated initial state, and not a verified parameter-shifted family member. A possible later reassembly would require a separate exact construction.

## Implications and limits

The controls establish two genuinely positive ordinary epochs with complete chronological first-R reuse. They show why favorable port access and the opposite graph cannot be omitted from a resource argument. They do NOT establish unbounded gain with bounded w exceptions without an all-q proof, do NOT show sharpness of the cubic global bound, and do NOT produce infinite behavior. The transport contribution9-q is negative for large q, and its quadratic old fuel is fully charged. The family is a targeted boundary test, not a generic scan.
