# A global quadratic time bound in the higher-reuse count

Status: independently analytically audited on 2026-10-22 at 20:55 UTC. The computability analysis independently checked the same ledger. The higher-R and coupled-charge refinements below were independently approved at 20:59 UTC. None of these statements proves eventual capture.

## Statement

Consider any finite feasible trajectory prefix with t reads, starting from m black cells. Let q count the read EVENTS that are the third or a later visit to their physical cell, counting visits from the beginning of this prefix. Then

    t <= P(m,q)
       = 132 m^2 + 230 m q + 100 q^2 + 422 m + 370 q + 326.

In particular,

    t <= (12m+10q+20)^2,
    q >= max(0,(sqrt(t)-12m-20)/10).

The weaker estimate t<=326(m+q+1)^2 also follows immediately.

Every intermediate black mass is at most

    6m+5q+8.

The same assertions apply after any time cut, using the finite black mass at that cut and counting subsequent visits anew. No claim of positive asymptotic density is made; the lower bound is of square-root order. Standard highways themselves have many higher-reuse events, so this is not a bound on nonstandard adjacent-K events.

## 1. Exact run restrictions

A run means a maximal constant-letter segment of the finite turn word. Let r_i and l_i count R and L runs of length i. Let n_R=sum_i r_i and n_L=sum_i l_i. Empty words cause no difficulty.

Every run has length at most4. Five identical turns read the first cell again with the same turn, with no intervening visit to it.

Every internal run has length other than3. The words LRRRL and RLLLR make the first and last letters read the same physical cell, again with no intervening visit, so they violate alternation. Thus

    r_3+l_3 <= 2.

### Four-R runs

Except for a run beginning at the first read of the whole word, the fourth read of RRRR is the predecessor of its first read. This is therefore a non-first R read. If it is the second read of that cell, the first was L, so it is an initially black cell. There are at most m such second-R events. Otherwise the fourth read is one of the q higher-reuse events. Distinct four-R runs have distinct charged read events. Consequently

    r_4 <= m+q+1.

### Four-L runs

Consider the first read of an LLLL run. If it is a first visit, its cell is initially black, giving at most m such runs. Otherwise, the next read after all four L turns returns to this cell and is at least its third visit. Charge that event to q. At most one run is exempt because the finite word ends immediately after its fourth L. Therefore

    l_4 <= m+q+1.

### Singleton-L runs

At most m singleton Ls are first visits, and at most q are higher-reuse reads. The remaining singleton L is a second visit to an initially white cell v.

By the fixed sector, the two incoming headings at v are identical or opposite. If identical, the predecessor cell is the same on both visits. Unless v was the initial head cell, the read immediately before this second L is a non-first read of that predecessor. Since the L is a singleton run, that neighboring read is R.

If the headings are opposite, the first R and the second L have the same successor. Unless this L is the final read of the finite prefix, its immediately following read is a non-first read of that successor and is R by singleton status.

A non-first R is either the second read of an initially black cell, at most m events, or a higher-reuse event, at most q. Each such R has at most two adjacent positions that could charge it. There is at most one initial-head second-L exception and one final-read exception. Hence

    l_1 <= m+q+2(m+q)+2 = 3m+3q+2.

This is a counting statement, not a disjoint partition across the separate inequalities: an event may be charged in two different bounds, which is harmless because both contributions are retained in the final coefficients.

## 2. Mass and singleton-R counts

Let c be raw curvature, the number of R letters minus the number of L letters. Black mass changes by c, so c>=-m. The exact run identity is

    c = 2(n_R-n_L) - r_1 + r_3 + 2r_4 + l_1 - l_3 - 2l_4.

Since n_R-n_L<=1, the preceding bounds imply

    c <= 2+2+2(m+q+1)+(3m+3q+2)
      = 5m+5q+8.

Thus the final mass is at most6m+5q+8. Apply the same argument to EVERY initial subprefix. Its higher-reuse count is no larger than q, so the same upper bound M=6m+5q+8 holds throughout the trajectory prefix.

Solving the identity for r_1 and using c>=-m gives

    r_1 <= 6m+5q+8.

## 3. Long stretches of length-two runs

Call a run exceptional when its length is not2. The total number E of exceptional runs satisfies

    E = r_1+l_1+(r_3+l_3)+r_4+l_4
      <= (6m+5q+8)+(3m+3q+2)+2+2(m+q+1)
      = 11m+10q+14.

Between these exceptional runs are at most E+1 stretches consisting entirely of runs of length2. Each stretch starts with RR or LL and is a power of RRLL or LLRR, followed by at most two letters.

A full RRLL period starting at the origin heading north reads

    (0,0) R, (1,0) R, (1,-1) L, (2,-1) L

and translates by(2,0). Its successive periods have completely disjoint read sets. A full LLRR period has the analogous disjoint horizontal strip with displacement(-2,0). These statements remain true after any spatial rotation or translation.

Thus k full periods within such a stretch require2k distinct cells black at the stretch's entry. These cells are not read by any earlier phase of that stretch. Entry mass is at most M, hence2k<=M. The stretch length is therefore at most

    4k+2 <= 2M+2 = 12m+10q+18.

Every exceptional run has length at most4. Consequently

    t <= 4E+(E+1)(12m+10q+18)
      <= 132m^2+230mq+100q^2+422m+370q+326.

For s=m+q+1>=1, E<=14s and M<=8s, so the same expression is at most326s^2. This proves the stated simpler square-root consequence.

## 4. The explicit two-visit corollary

When q=0, the word reads every cell at most twice. The bound becomes

    B2(m) <= 132m^2+422m+326.

Thus a third read must occur within the next P(m,0)+1 reads of any finite board of mass m, irrespective of its geometry. The earlier qualitative proof and König argument remain correct, but are superseded quantitatively by this explicit polynomial bound.

The constants are deliberately conservative. No optimality is claimed. The exact complete small-m controls B2(0..6)=8,16,24,32,42,54,66 are far smaller.

## 5. Higher-R reads suffice, and a coupled charge sharpens the bound

This refinement was independently analytically approved at 20:59 UTC. Let u count only third-or-later reads that turn R. A second R can occur only at an initially black cell, so the number of NON-FIRST R reads is at most m+u.

For any non-first singleton L, compare it with the immediately PREVIOUS visit to its cell, which read R. The same/opposite-heading argument from Section1 still applies. Its chosen adjacent neighbor is non-first, and singleton status forces that neighboring turn to be R. No assumption that the previous R was the first visit is needed. Only the initial-head previous-R-at-time-zero exception and the final-read exception remain. Thus

    l_1 <= m+2(m+u)+2 = 3m+2u+2.

Also r_4<=m+u+1. For L4, the following return to its initial cell necessarily reads R, so the same charge proves l_4<=m+u+1.

A small but exact capacity coupling strengthens the singleton estimate. Every R4 run except a possible initial one is charged to its fourth R, a distinct non-first R event. Such an event has an R immediately on its left. It can therefore receive at most ONE neighboring singleton-L charge, not two. Subtracting this unavailable capacity gives

    l_1 <= 3m+2u-r_4+3.

Combine this with the exact run identity, keeping the negative terms, to obtain

    current_mass + r_1 + 2l_4 <= 5m+3u+8.

This is valid for every prefix. Consequently every intermediate mass is at most M'=5m+3u+8, and r_1 has the same bound.

The exceptional-run count can now be grouped as

    E = r_1 + (l_1+r_4) + (r_3+l_3) + l_4
      <= (5m+3u+8)+(3m+2u+3)+2+(m+u+1)
      = 9m+6u+14.

The same self-avoiding RRLL/LLRR argument bounds each regular stretch by

    2M'+2 = 10m+6u+18.

Therefore the sharpened global estimate is

    t <= 4E+(E+1)(10m+6u+18)
      <= 90m^2+114mu+36u^2+348m+222u+326
      <= (10m+6u+20)^2.

In particular,

    u >= max(0,(sqrt(t)-10m-20)/6).

Thus every finite-seed tail must repeatedly create black at cells that have already been read at least twice. This is stronger than merely requiring infinitely many repeated reads. It still gives no positive density and no bound on nonstandard K renewals.

The q=0 two-visit lifetime bound improves accordingly to

    B2(m) <= 90m^2+348m+326.

The literal checker check_higher_reuse_counts.py verifies the run inequalities, coupled mass inequality, exceptional-run count, and final polynomial on400,000 finite prefixes from40 varied seeds. These are controls only; the proof is the charge argument above.

## 6. Consequence for periodic white-input fronts

Let a nonzero translating-periodic front be realizable from a finite black seed. For each displacement class c, let n_c be the total number of read phases in one full period, ordered by the true first-read chronology. Far enough along that ray, the first read is R and the list alternates. Let

    g = number of classes with odd n_c,
    Q_R = sum_c floor((n_c-1)/2),

so g is the black-mass growth per period and Q_R is the number of higher-R events per period. Let R1 and L4 be the numbers of cyclic maximal runs of lengths1 and4 with the indicated letters in that period. Advancing through sufficiently many periods and dividing the coupled mass inequality by the period count gives

    g + R1 + 2L4 <= 3Q_R.

Endpoint constants and the finite initial seed disappear under this limit. This conclusion concerns finite-seed, white-input fronts, not arbitrary periodic motion on an infinite black background.

If every class has multiplicity at most3, and n1,n3 count the classes of multiplicity1 and3, then g=n1+n3 and Q_R=n3. Hence

    n1 + R1 + 2L4 <= 2n3,

in particular n1<=2n3. This is only a necessary condition, not an exclusion of all multiplicity-three fronts.


## 7. Spatial higher-reuse consequence of the audited midpoint inequality

The independently established midpoint inequality in ../continuation_2026-10-22/ant_continuation2/chronology/axial_separator_proof.md Section4 states

    |B_t symmetric_difference B_0| >= 2 ||p_t-d(h_t)/2-p_0+d(h_0)/2||_infinity.

Together with mass_t<=5m+3u+8 and |B_t symmetric_difference B_0|<=mass_t+m, this gives

    3u >= 2||p_t-p_0||_infinity-6m-10.

This is only an algebraic corollary of two audited bounds. In particular, a trajectory with linear spatial escape has linearly many higher-R read events. No inference to positive K density or failure of standard behavior is valid.
