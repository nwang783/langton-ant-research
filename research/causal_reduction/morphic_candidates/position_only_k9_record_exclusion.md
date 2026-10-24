# Heading-free scale-nine inflation: finite-support exclusion by records

Status: independently audited by the computability analysis, both analytically
and through a separately implemented finite replay. This is a finite-support
theorem, not an any-initial-coloring exclusion.

Independent artifacts: `computability/check_position_k9_record_independent.py`
and its JSON. They regenerate words with copied-state branching, use complex
coordinates, and exhaust refinements by breadth-first copied fields. Every
word, pair, node count, and chronology-conflict count agrees.

## Statement

There is no standard square-ant trajectory on a finite black set satisfying

    p(9n) = 3 p(n)   for every n >= 0,

with p(0)=0. No relation between h(9n) and h(n) is assumed. The initial heading
is arbitrary. Image words may be selected independently at every occurrence.
No finite controller or substitution hypothesis is used.

We use the already established nontrapping theorem: a finite-support ant
trajectory cannot remain in a finite set of physical cells. Thus some directed
coordinate has arbitrarily high records. Rotate that direction to north.
Rotation preserves the displayed real scale-three identity.

Write W[t:t+q] for the q turns read beginning at time t. Put A=RRLRRRRLR.

## Exact finite ingredients

The standalone checker `check_position_k9_records.py` imports no previous
inflation geometry or inventory. It checks all 512 nine-letter words, retaining
262 whose repeated cell reads alternate. For each coarse heading Hc and coarse
turn c, include every fine starting heading Hf of the same parity and every
retained word whose displacement is three times that coarse step. This produces
240 oriented records. Fine/coarse heading parity agrees because 9n and n have
the same parity; heading equality is not assumed.

1. Every such word has maximum read-height at most 4 above its coarse-center
   image. Unless its coarse step is north, its maximum read-height is at most 2.
2. Consider a fine macro starting at (0,-3), heading E or W, ending at (0,0),
   followed by a macro ending at (3,0). Require alternating reads in their
   combined history, and require every first read in y>=0 to be R. Exactly six
   pairs survive. In all six, the second macro starts N and equals A, while
   the first macro makes no read in y>=0. The preceding (heading,word) pairs are:

       E RRRRLLRRL       E RRRLRRLRL       E LLRLLLLRL
       W RLRLLLLRL       W LRRLRRLRL       W LLLLRLRRL

3. No geometric nine-macro refinement of the coarse word A can have first fine
   image A. Both coarse and fine initial headings are N; every other fine
   boundary heading is free. Initial cell colors are completely unrestricted.
   Complete literal DFS has 635 nodes, by depth 1,1,6,18,51,260,298, and reaches
   no seventh macro, hence certainly no complete 81-letter refinement. Every
   branch is rejected only by a repeated cell receiving equal consecutive
   turns. There is no node, time, or depth cap.

All assertions and counts are bound in `position_k9_record_certificate.json`.

## Record lemma

Choose a positive integer Y above every initially black cell's north-coordinate
and above the starting point. Let t=tau(Y) be the first time the trajectory
reaches row Y. Then h(t)=N and W[t]=R, since that whole row was previously unread
and has no initial black cells.

Consider the fine macros indexed by n<t-1. Their coarse centers have height
at most Y-1. A center of height Y-1 cannot take a north step, since that would
reach Y before t. Ingredient 1 therefore bounds their fine read-heights by
3(Y-1)+2 < 3Y. Centers of height at most Y-2 have bound
3(Y-2)+4 < 3Y. Thus no read before time 9(t-1) reaches row 3Y or above.
Those rows also have no initially black cells.

The macro indexed t-1 goes from 3p(t-1) to 3p(t), a north displacement of three.
Its fine entry heading is E or W by parity. The macro indexed t has coarse
turn R from north heading, hence fine displacement east by three. Translate
3p(t) to (0,0) for this finite comparison only. Their actual combined history
meets ingredient 2, because every first read in the upper half-plane is on a
pristine white cell. Consequently:

    tau(3Y) = 9 tau(Y),
    h(9t) = N,
    W[9t:9t+9] = A.

The equality of record times follows because none of the previous macro's
reads reaches the upper half-plane, while its final move arrives at 3p(t).
The finite inventory does not assume the preceding coarse turn is R: its
coarse heading may be W with R or E with L.

## Two successive scales give the contradiction

Apply the record lemma once at Y and again at 3Y. Set s=9t=tau(3Y).
Then both W[s:s+9] and W[9s:9s+9] equal A, and both entry headings are N.
For 0<=j<=9, the original global identity gives

    p(9s+9j)-p(9s) = 3 (p(s+j)-p(s)).

Therefore W[9s:9s+81] is a geometric nine-macro refinement of the coarse
nine-letter word A at time s, with its first fine macro also A. Its actual
read chronology alternates on all repeated cells. Ingredient 3 excludes it.
This contradiction rules out arbitrarily large records in any direction,
contradicting nontrapping.

IMPORTANT: We never claim that a time-shifted whole trajectory obeys the
original self-inflation identity. Only the displayed finite block relation is
used. No black-fuel count, bounded mass, standard-highway classification,
finite-state controller, or eventual factorization is assumed.
