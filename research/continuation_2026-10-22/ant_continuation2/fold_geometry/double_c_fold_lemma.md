# Three double-C folds are impossible on pure V rails

Date: 22 October 2026. This is an all-parameter physical obstruction for a restricted sublanguage. The mixed U/V version is false, and the full component H remains open.

Use the before-marker C and V words from the first continuation, and put F=CC. Then F has length 30, displacement (-1,1), and final heading south. V has length 18, displacement (1,3), and unchanged heading.

## Theorem

For every pair of integers n,m>=0, the finite word

\[
F V^n F V^m F
\]

is physically infeasible, independently of the initial coloring.

The obstruction is two consecutive visits to one cell requesting the same letter:

| Parameter range | Cell q | Earlier time | Later time | Letter |
|---|---|---:|---:|---|
| n=0 | (2,1) | 7 | 67 | R |
| n>=1, m>=n | (0,-1) | 3 | 36n+55 | L |
| n>=1, m<n, r=n-m | (-r,3-3r) | 18r+23 | 60+18(n+m)+23 | R |

Times are zero-based pre-update indices in the displayed word.

## Exact geometric premises

F has footprint in [-2,2] x [-1,3]. Its only visits to (2,1), (0,-1), and (0,3) are respectively phases 7:R, 3:L, and 23:R. It does not visit (-2,-1).

V has footprint in [-1,2] x [-1,3]. Its only visit to the line y=3x+1 is (0,1), phase 11:R. Its visits to (1,2) are phases 13:L and 17:R. The first twelve letters of F and V are the same marker M.

The five block boundaries have the following poses:

1. Initial F: (0,0), north, time 0.
2. First V run: (-1,1), south, time 30.
3. Second F: (-1-n,1-3n), south, time 30+18n.
4. Second V run: (-n,-3n), north, time 60+18n.
5. Third F: (m-n,3m-3n), north, time 60+18(n+m).

## Consecutiveness proof

If n=0, the reflected second F cannot reach q=(2,1): this would require its local cell (-3,0), outside its footprint. After those two F blocks, the next block is either V or F. Its common marker reads q at phase 7, giving time 67. The first F's phase 7 is the previous read, and both request R.

Suppose n>=1 and m>=n. Let q=(0,-1). A visit by copy k of the first V run would require its local cell (-1-k,2-3k). For k>=1 this is outside V's x range; for k=0 it is (-1,2), which V does not read. A visit by the second F would require (-1-n,2-3n). For n>=2 the x coordinate is outside F; for n=1 it is the absent cell (-2,-1). In the second V run, copy k would need local cell (n-k,3(n-k)-1). Every k<n-1 requires height at least 5 and misses. Copy n-1 reaches (1,2), first at its phase 13, requesting L. Its time is 60+18n+18(n-1)+13=36n+55. The previous read is the initial F's phase 3, also L.

Finally suppose n>=1 and m<n, and put r=n-m>0. Let q=(-r,3-3r). In the first V run, copy k needs local cell (r-k-1,3(r-k-1)+1). The line-intersection premise shows there is exactly one such visit: k=r-1, local phase 11, requesting R. It exists because 1<=r<=n. Its time is 30+18(r-1)+11=18r+23.

The second F would need local cell (-1-m,-2-3m), below its footprint. A second-run V copy k<m would need local cell (m-k,3(m-k)+3), again above its footprint. At the third F the cell is local (0,3), whose first visit is phase 23:R. There are therefore no intervening reads, and the final row of the table follows.

This proves the theorem for all n,m, not only tested values.

## Infinite-class consequence

An infinite physically consistent concatenation of F and V contains at most two F blocks. Otherwise three successive F blocks give the forbidden word above. It is therefore eventually V-periodic. The exact U/V fuel theorem gives two new initially black cells per subsequent V block, so no such infinite stream can start from finite support.

Thus every finite-support trajectory is excluded from having an eventual tail over the two blocks {V,CC}. This is a restricted consequence; it does not exclude tails containing isolated C blocks, Q or B, or arbitrarily mixed U/V rails.

## Exact limitation: mixed U/V rails defeat the lemma

The word

\[
F V^4 U^2 F V^3 F
\]

is physically feasible, and it remains feasible after appending the next full marker M. Hence replacing V^n,V^m by arbitrary U/V words makes the three-fold claim false. The verifier records the complete finite first-L seed and consecutive-read trace certificate for this witness. A proof for H must control these mixed rails, rather than simply applying the pure-V fold formula with total rail length.
