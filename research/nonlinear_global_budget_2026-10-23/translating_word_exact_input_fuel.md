# Exact input-fuel criterion for a translating ant word

## Setup

Fix a finite turn word w of length P, a starting heading, and a starting
position. Suppose replaying its geometric turns restores the heading and
has nonzero displacement f. Ignore colors initially. Record each phase
position q_i, turn w_i, and phase i. Group positions modulo the subgroup
Z f. In each group choose a representative c and write q_i=c+k_i f.
There are only finitely many nonempty groups.

Sort every group's slots by decreasing k_i, then increasing phase i.
Let Delta be the largest max(k_i)-min(k_i) over all groups.

## Geometric feasibility

The infinite turn stream w^infinity is realizable on some binary board
(possibly infinite) IF AND ONLY IF every sorted group list alternates
R,L,R,L,... or L,R,L,R,... .

Indeed a fixed physical cell c+n f is visited by those copies of slots
with k_i<=n. Its visit time is(n-k_i)P+i, giving exactly the stipulated
order on the eligible suffix. If one group contains consecutive equal
symbols, cells far enough ahead see that whole list and demand the same
color twice without an intervening flip. Conversely, set each cell's
initial color to its required first symbol (L means black). Alternation
then guarantees every later turn by induction on absolute time.
Cells never read may have arbitrary colors.

## Exact eventual finite-copy fuel

Assume the alternating-list condition. Let a be the number of complete
group lists whose FIRST symbol is L. For each group define its left fringe
at integers min(k)<=n<max(k): use the first slot among k_i<=n. Let b be
the total number of L first symbols on these finite fringes.

For every N>=max(1,Delta), the exact minimum starting black mass permitting
N copies w^N at this pose is

    F_w(N) = a N + b.

Proof. A slot can occur in the first N copies exactly when
0<=n-k_i<=N-1. In the left fringe n<max(k), the largest eligible k gives
the same first symbol as the infinite list; its required copy number is
at most Delta-1<N. For each group, the N cells
max(k)<=n<=max(k)+N-1 have its complete-list first symbol, since the
largest-k slot is always eligible and earliest. These two parts cover
all cells read in N copies when N>=Delta. The black requirements are
therefore b+aN. They are necessary because every cell's initial color is
forced at its first read, and sufficient by placing black EXACTLY on
those first-L cells. Every eligible finite-copy list is a contiguous
sublist of the full alternating list, hence remains alternating.

For smaller N there is still an exact finite interval-counting formula;
no asymptotic extrapolation is needed.

## Finite infinite-word realizability

Consequently an alternating translating word is realizable forever on
SOME FINITE board IF AND ONLY IF a=0. If a>0 its future requires infinitely
many distinct initially black cells. If a=0, black is needed only at the
b left-fringe cells; that finite board realizes the infinite word exactly.
Its minimum initial mass is b. Extra black outside the complete future
read set is irrelevant.

Thus any genuine nonstandard translating word with a=0 would ALREADY be
a finite-seed nonstandard infinite trajectory. A positive-a prepared
wave is a different phenomenon: it consumes an infinite pre-existing
black supply even when it increases total black count as it goes.

## Net black production is not input renewal

Let a_out count full group lists whose LAST symbol is R. A read list
starts black precisely if its first symbol is L, and finishes black
precisely if its last symbol is R. Since the list alternates, its total
black change is that difference. Summing groups gives the exact identity

    (#R in w)-(#L in w) = a_out-a.

In particular positive net black production does not imply zero input
fuel. It can be larger output density after consuming a positive input
density on different physical cells.

For the signed1564 wave: Delta=1, a=197,b=1,a_out=301, net+104,
and614 adjacent-K per period. For the signed4352 wave: Delta=1,
a=406,b=57,a_out=590, net+184, and1972 adjacent-K per period.
Both are impossible as infinite trajectories on a finite CURRENT board.
Neither gives a bound in ORIGINAL seed mass, since earlier long clean
standard flights can generate arbitrarily large current black supplies.

The statement concerns one fixed translating word. It is not a global
rank for arbitrary ant trajectories, nor a bound on the number or length
of successive different word regimes.
