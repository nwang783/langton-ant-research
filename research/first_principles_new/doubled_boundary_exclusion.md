# Finite square seeds exclude an eventually all-exponent-two boundary ray

Status: independently analytically audited proof. The companion all-exponent-one exclusion is also independently audited. Neither statement is a highway theorem.

## Statement and geometry

For a square ant started with finitely many black cells, the limiting reduced ray cannot have an eventual tail consisting entirely of exponent2 syllables. Thus exponent1 must occur infinitely often.

Discard a finite prefix and rotate so that the putative permanent spine roots and intermediate core reads are

    w_k=(2k,0), R module, heading north;
    u_k=(2k+1,0), the intermediate R core read;
    l_k=(2k+1,-1), L module, heading south;
    v_k=(2k+2,-1), the intermediate L core read;
    w_(k+1)=(2k+2,0).

The board at this cut has finite black support. Every permanent call chooses child2. The general spine grammar permits an optional completed G at child1 and an optional completed B at the next permanent root. Expanding each B into its one or two G fingers gives ONLY the following geometric kinds of non-core reads:

1. North-going G_L fingers in the column pair {2k,2k+1}, starting at u_k=(2k+1,0), heading east. These arise either as the optional child1 G of the R call, or as the mandatory first finger of a B_R at w_k.
2. South-going G_R fingers in the column pair {2k+1,2k+2}, starting at v_k=(2k+2,-1), heading east. These arise either as the optional child1 G of the L call, or as the mandatory first finger of a B_L at l_k.
3. East-going fingers in the two central rows0,-1. A second finger of B_R is G_L starting at l_k, heading south. A second finger of B_L is G_R starting at w_(k+1), heading north.

The parent four-step circuits of B packets themselves read only the central two rows. This classification follows directly from the exact B grammar and the canonical poses above. It does not assume packet depths are bounded.

## 1. Only finitely many north fingers occur at distinct stages

For every north G_L finger at stage k, its first point after the root is

    q_k=(2k+1,1).

That point is read L, for every depth n>=0, by the exact initial G pattern. The north finger must therefore see q_k black before its first read.

No core update, south finger, or east finger reaches row1. North fingers at different indices have disjoint column pairs. Hence before the first north finger at stage k, q_k has never been read in the tail. It must have been black at the initial cut.

There are only finitely many such black points. Thus north fingers occur at only finitely many indices k. Individual calls return finitely and the per-module return ledger bounds their number, so this is also a finite number of north fingers in total. Fix K beyond every stage at which one occurs.

In particular, for j>=K there is no B_R at w_j, since its mandatory first finger would be north-going.

## 2. East far-end changes at odd columns are one-way

Consider the vertical pair at odd column2j+1:

    u_j=(2j+1,0), l_j=(2j+1,-1).

The interior pattern of EVERY east G finger is upper-white/lower-black, and its interior reads restore both colors.

For a G_L east finger starting at column2k+1, its far endpoint has column2k+n+2 and initial common color1 XOR (n mod2). If that column is odd, n is odd and the required common color is0.

For a G_R east finger starting at column2k+2, its far endpoint has column2k+n+3 and initial common color n mod2. If that column is odd, n is even and again the required common color is0.

Therefore EVERY east far-end operation at an odd column is exactly

    (upper,lower) = (0,0) -> (1,1).

No such operation changes11 to00. An east interior cannot repair an upper black bit either: it requires that bit already white and restores it.

## 3. A future odd-column black pair cannot be repaired

Fix j>=K, and consider the time before the permanent R core read at u_j. All earlier spine stages lie strictly to its west.

No north finger at a different stage reaches u_j, because the north column pairs are disjoint. There is no north finger at its own stage j by the choice of K. South fingers remain in rows<=-1 and cannot reach u_j. The core has not previously read u_j.

The only possible remaining changes to u_j before its R read are east-finger changes. It cannot be a near endpoint of an earlier east finger: their near columns are their own stage's current or next core columns. The only same-stage east near endpoint at its odd column would belong to B_R at w_j, and that B_R is excluded by the absence of north fingers. Thus before the required R read, u_j can only be an east interior or far endpoint.

It follows that u_j was white initially and no east far-end flip has occurred at its column: once a far-end flip made it black, none of the permitted earlier events could make it white again.

Now consider l_j before its FIRST read at its own stage, whether that first read starts an optional B_L or the permanent L call. Both require L. Earlier south fingers occupy disjoint column pairs and miss l_j; there is no same-stage south finger before that first root read. There is no same-stage B_R/north operation. East interiors restore l_j, and an east far-end flip at its odd column has just been ruled out by the preceding R-read requirement at u_j.

Hence l_j must already have been black at the initial cut. This holds for every j>=K. The l_j are distinct, contradicting finite initial black support.

## Consequence and limits

Together with `alternating_boundary_exclusion.md`, this proves that both syllable exponents1 and2 occur infinitely often in the limiting ray of every finite-support square ant, with both proofs independently reviewed. It does not bound gap lengths, prove a positive frequency, bound decorations, or imply the standard104 word.
