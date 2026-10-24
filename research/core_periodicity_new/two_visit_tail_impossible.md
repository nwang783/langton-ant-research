# Every infinite finite-seed tail has a triple-read cell

Status: proved, independently analytically reviewed by the proof auditor on 2026-10-22 at 20:47 UTC. The computability analysis proposed the two-visit class and its merge/fork matching; this analysis supplied the closing run and mass argument. The theorem is a chronological restriction, not eventual capture.

## Theorem

For Langton's R-white / L-black / flip-and-move ant on the square lattice, started with finitely many black cells, it is impossible that every physical cell is read at most twice over the entire infinite future.

The board after any finite time is again finite. Consequently, for EVERY time T, there is a cell read at least three times strictly after T. This does not imply infinitely many distinct triple-read cells: a recurrent cell could witness many tails.

## Proof

Suppose, for contradiction, that each cell is read at most twice. Write p_t for the cell read at time t and h_t for its incoming heading. The sector

    (h_t - x_t - y_t) mod 2

is invariant. Thus any two incoming headings at the same cell are identical or opposite.

There are only finitely many visits to initially black cells and to the initial head cell. Choose a cut after all of them, with one extra step of margin. At every subsequent read, R means that the cell is being visited for the FIRST time, and L means that it is being visited for the SECOND time. All such cells were initially white.

### 1. Every late L has an adjacent L

Let a late L at v be its second visit, and let a be its earlier R visit.

If the incoming headings at those visits are identical, their predecessor cell u is identical. The first visit to v was not at time zero, since the initial head cell has been excluded. Therefore u was read immediately before each visit to v. These are u's two visits. Its second read, immediately before the present L, is also L because u is initially white.

If the two incoming headings are opposite, the first R and the second L choose the same outgoing direction. Their successor cell w is therefore identical. It is read immediately after each visit to v. Those are w's two visits, so the read immediately after the present L is L.

The two occurrences of u or w in this argument are at distinct times. Any third occurrence would already violate the hypothesis. The cut ensures that the relevant neighboring reads are not initial-black exceptions.

This is the merge/fork matching in local form: a doubled directed edge joins a twice-read merge cell to a twice-read fork cell. Initially white endpoints are traversed first as RR and later as LL.

### 2. Late runs have a very restricted form

There is no late RRRR. For any four consecutive right turns, the fourth read cell equals the predecessor of the first read cell. It was therefore read four time indices earlier and cannot be a fresh R. We start this assertion at least one step beyond the cut.

There is no late LLLL. Four left turns return to the first read cell of that block. Its L was already its second visit, so the next read would be its third.

A maximal run of exactly three turns is impossible anywhere in an interior feasible word. In LRRRL, the first and last L read the same cell with the same turn; they are consecutive visits to that cell, contradicting alternation. RLLLR has the symmetric conflict. The three intermediate read cells are the other three corners of the relevant unit square, so there is no intervening visit to the conflicted cell.

Thus all sufficiently late R runs have length1 or2. Every sufficiently late L run has length2: length1 is excluded by the preceding adjacency lemma, length3 by the equal-letter conflict, and length at least4 by LLLL. There are infinitely many runs, since an infinite constant-turn tail would contain four equal turns.

After possibly discarding an initial partial run, the tail therefore decomposes as

    R^{a_1} LL R^{a_2} LL R^{a_3} LL ...,
    with every a_i in {1,2}.

### 3. Mass forces an impossible axial tail

Let M be the finite number of black cells at the chosen run boundary. Every R increases black mass by1, and every L decreases it by1. A block R^a LL changes mass by a-2, which is -1 for a=1 and0 for a=2. Since black mass is nonnegative, at most M of these blocks can have a=1.

The trajectory must therefore eventually execute

    (RRLL)^infinity.

Starting at (0,0) heading north, one RRLL period reads

    (0,0) R, (1,0) R, (1,-1) L, (2,-1) L,

and ends at (2,0) with the same heading. Its translates by (2k,0) have disjoint read sites. Hence every sufficiently late L cell in this tail is a new cell not read in its finite preceding history. Such a first L requires an initially black cell. There are infinitely many of them, contradicting finite initial black support.

This proves the theorem. Rotation or translation changes none of the argument.

## A total computable mass-only two-visit lifetime bound

For m>=0, form the tree of finite feasible turn words with at most m distinct first-L cells and with at most two reads at every physical cell. At a first visit one may branch R or L if fuel remains; at a second visit the turn is forced to be opposite; a third visit is disallowed. The tree is finitely branching and effectively generated without a spatial cutoff.

If this tree had an infinite branch, its at most m first-L sites would form a finite initial black set that realizes the entire branch. That would contradict the theorem. By König's lemma the tree is finite. Consequently exhaustive depth-first enumeration terminates for EVERY m and computes its exact maximum word length B2(m).

Thus there is an unconditional total computable bound, depending only on initial black mass and not its spatial placement, on the number of reads that can precede a third read of some cell. No simple closed formula, primitive-recursive complexity bound, or relation to the number of adjacent-K renewals is asserted here.

The computability analysis's complete searches before this proof gave

    m:       0, 1, 2, 3, 4, 5, 6
    B2(m):   8,16,24,32,42,54,66.

Those values are controls, not the proof. The independently owned enumeration is in ../computability/probe_two_visit_fuel.py and its JSON. The proof above explains why analogous exhaustive searches must eventually terminate for every fixed m.

## Scope and next question

This excludes all infinite finite-support trajectories with a globally bounded reuse count of2, including constructions whose geometry has no cell read more than twice. It does not exclude bounded reuse counts of3 or larger, proper escape, or eventual highways. It does not prove infinitely many distinct cells receive three visits, nor any positive density of triple reads.

A possible next structural question is whether the first genuinely renewable same-sector packet necessarily contains three or four visits to a particular physical cell, and whether such higher-multiplicity packets admit a directed finite-fuel ledger. No such ledger is proved here.

## Audited quantitative strengthening

A direct run-count refinement now gives the explicit proposed bound

    B2(m) <= 132m^2+422m+326.

The computability analysis independently checked its exact ledger. The full argument, including a stronger bound for arbitrary prefixes in terms of their third-or-later read count q, is in higher_reuse_count_bound.md. The auditor independently approved the numerical strengthening at 20:55 UTC. The subsequent higher-R refinement improves the zero-reuse bound further to 90m^2+348m+326.
