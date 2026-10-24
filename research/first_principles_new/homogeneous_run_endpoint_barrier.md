# The unique external endpoint of a homogeneous two-run

22 October 2026. Independently analytically audited all-parameter chronological lemma. It uses the established exact G/B packet grammar and its two-row geometry. No global attraction claim is made.

## 1. Common horizontal-finger data

Normalize an R-start eastward exponent-two block so that its core is on upper row0 and lower row-1, with R roots (2k,0). Its only eastward completed fingers are:

- G_L based at (2k+1,-1), heading S, as the second finger of B_R;
- G_R based at (2k+2,0), heading N, as the second finger of B_L.

Their starting columns differ, and their depths are arbitrary. Nevertheless EVERY such finger has exactly the same strictly interior two-rail requirement:

    upper bit0, lower bit1.                               (1)

It reads each strict interior bit twice and restores this pattern. At a far endpoint column f, it requires two equal bits c(f), then flips both, where

    c(f)=1 for even f, and c(f)=0 for odd f.               (2)

For G_L of depth n with odd starting column, f has parity n and its far bit is1 XOR n. For G_R of depth n with even starting column, f has parity n+1 and its far bit is n. Both give (2).

All non-east-finger events in the block are core turns, B parent-face turns, and north/south G fingers. Choose X at least the maximum x coordinate touched by ANY of those events and at least every east finger's starting column. Such an X depends only on the finite core's stage range, not on finger lengths: every north/south finger stays in its own stage column pair, and the B parent faces have unit width.

## 2. External endpoint barrier theorem

At most one east G finger in the entire block can have its far column strictly greater than X.

Proof. Suppose the first such finger has far column f>X. Immediately after it finishes, every tail column X<x<f has pattern01, while column f has equal bits1-c(f). No other event except an east finger can touch either rail at x>X.

Consider a later east finger with far endpoint f'>X, choosing the first later one if any. Its starting column is at most X. There are three cases:

- X<f'<f: its endpoint still has pattern01, but it requires equal bits.
- f'=f: its endpoint still has equal bits1-c(f), but it requires c(f).
- f'>f: column f is strictly interior, but still has equal bits rather than01.

Every case is impossible. Events whose far endpoint is at most X never touch the tail and cannot repair these conflicts. This proves the theorem.

Consequently the NET lamp change in the entire forward tail x>X is either empty or exactly one vertical pair of bits on the two central rows. Arbitrarily many tail cells may have been read and restored; no bound on packet depth, duration, or read support is being asserted.

## 3. Direct parallel-run transfer

For a maximal R-start eastward two-block of length2n, its following entry is (2n,0,N). If the intervening exponent-one block has even length2m, m>=1, the next two-block starts at (2n+m,m,N) and travels east. Its first R-stage charge points have x=2n+m+1, and later charges have still greater x. All are beyond the old core/nonhorizontal slab, which ends by x=2n+1. Thus the old two-block can directly create at most two bits on the next block's entire charge set, by Section2. In fact its overlap is even more restricted for m=1, but that sharpening is not needed.

For an odd old two-block of length2n+1, the following entry is (2n+1,-1,S), with next sign L. An even one-block2m gives a subsequent L-start eastward two-block. After omitting its first L stage, the R-stage charge points begin at x=2n+m+3, beyond the old slab's maximum x=2n+2. The same bound of two old-run additions applies to these later charge points. The omitted L stage has its own bounded net corner mask and is not silently absorbed into this assertion.

An odd intervening one-block instead makes the next two-block perpendicular. The independently audited transverse-mask lemma bounds the old block's direct additions on its two charge lines by eight.

These are direct net-toggle bounds for the specified older block only. The intervening one-block and any omitted endpoint stage can add further bits. More importantly, still earlier blocks may have left black fuel in the next charge set. The lemma therefore does not yet produce a global well-founded budget, nor does it rule out longer recycling cycles.
