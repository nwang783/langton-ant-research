# A four-left run needs an initial defect under a three-read cap

22 October 2026. Analytic proof independently reviewed by the proof-certificate auditor on 22 October 2026. The finite initial-head exception is retained explicitly. This is a local obstruction, not a classification of cap-three fronts.

## Proposition

In an ant trace whose physical read multiplicities are at most three, a maximal L4 run with a preceding and following read must have either an initially black cell or the initial head cell among its four unit-face cells.

Consequently any finite-seed translating periodic white-input front with displacement-class multiplicity at most three has no L4 run. More generally, a globally cap-three finite-seed trace has only finitely many L4 runs.

## Proof

Suppose all four face cells are initially white and none is the initial head. Normalize the four L reads, in chronological order, to

    w=(0,0), x=(-1,0), y=(-1,-1), p=(0,-1),

with the ant entering w heading north. The immediately preceding read is R at p, with incoming heading west. The immediately following read is R at w, with incoming heading north. Both are R because a legal constant-letter run has length at most four and this one is maximal.

Every displayed L is the second read of its cell: on an initially white cell, a L can only be the second or fourth read, and the latter violates the cap. Its required first R occurs strictly before the block, because the four block cells are distinct and every block read is L.

The R at p immediately before the block is therefore p's first read. There were no earlier reads of p. Likewise w's displayed L and following R are its second and third reads, so w has one earlier R.

At a fixed physical cell the arrival axis is fixed. The earlier R at w therefore arrived either north or south. It cannot have arrived north from p, because that would require an earlier read of p. No time-zero exception is possible because w is not the initial head. Hence it arrived south and turned right westward into x. This visit to x occurs before x's displayed second-read L, and so it is x's unique first R. That R arrived westward and departed northward.

The earlier R required at y arrived either north or south. If it arrived north, its right turn moved east into p. It cannot be immediately before the displayed first R at p: that read's incoming heading is west, whereas this arrival would be east. Hence it would give an earlier read of p, impossible. More directly, any arrival at p from y has heading east, different from its displayed first read.

Thus y's first R arrived southward from x. Since y is not the initial head, this requires an earlier read of x departing southward. But x has only one read before its displayed L, namely the first R already forced to depart northward. Contradiction.

## Finiteness and periodic consequence

Every such L4 run touches one of the finitely many initially black cells or the initial head cell. Distinct maximal runs have disjoint sets of read times. Each exceptional cell is read at most three times, so the number of such runs is finite (the coarse bound 3(m+1), with possible endpoint adjustments, suffices).

For a cap-three translating periodic tail, cut at an exact periodic boundary. Its future cell read counts are at most three, and the board at that boundary has finite black support. Any recurring L4 run would contradict the preceding finiteness statement. Thus L4=0 in its cyclic period.

## Immediate module consequence

Every completed G ladder G_a(n) contains its unique innermost base block b^4, where b=a for even n and the opposite sign for odd n. After excluding the finite exceptional L4 events, every completed G packet therefore has a R4 base: G_R depths are even and G_L depths are odd. This is a restriction on which depths are possible, not a bound on the depths or the number of G packets.
