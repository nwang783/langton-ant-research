# Reduced signed-curvature budget: candidate, not theorem

Status at 2026-10-22 18:15 UTC: unproved. This does not prove eventual periodicity, and no counterexample to eventual periodicity has been found.

## Exact combinatorial formulation

For a feasible finite turn word w, start at (0,0,N), and define m(w) as the number of distinct physical cells whose first read in w is L. Feasibility means that the turns on successive reads of each cell alternate. The minimal realizing initial black set is precisely the set of first-L cells, so m(w) is not a spatial-box surrogate.

Reduce w in C4*C4, deleting maximal fourth powers of either generator online. For the resulting positive normal form r, put c(r)=number of R letters minus number of L letters, including syllable multiplicities. The current candidate is

    c(r) <= 2 m(w) + 3.                              (C)

This concerns temporary finite reduced prefixes; these may contain exponent-3 syllables. It is not being silently restricted to the eventual exponent-1/2 boundary core.

The stronger coefficient-one claim is FALSE. The feasible seven-step word RRRLRRR, with initial black set {(0,-1)}, is already reduced, and has c=5, m=1. Thus c-m=4. This is a counterexample only to the auxiliary inequality, not to the highway conjecture.

## Finite controls

The independently written inverse-feasible-word DFS in search_curvature_two_mass.cpp explores both possibilities only at the first read of an unassigned cell, and thereafter enforces alternation. It maintains the exact free-product stack. With depth 500 and m<=3, it completed 68,992,899 prefixes, with max(c-2m)=3 and no violation. See curvature_two_mass500.log. This is a finite control, not a proof or evidence of a uniform time bound.

The auditor independently completed all feasible prefixes through length 256 with m<=3, 8,021,476 prefixes, again with maximum 3; through length32 with m<=5, 135,988 prefixes; a depth80,m<=8 search was capped after 10,000,013 prefixes and is not exhaustive. Their files are in ../audits/search_reduced_curvature.py and its JSON/log outputs.

## Rotation/quasimorphism interpretation

For r=a_1^{e_1}...a_k^{e_k}, let sign(R)=+1 and sign(L)=-1, and define

    f(r) = sum_i sign(a_i)(e_i-2).

Alternating syllables give |f(r)-c(r)|<=2. Also f(r^-1)=-f(r), since inversion replaces e by 4-e and reverses syllable order. On the eventual 1/2 core, f is (#L exponent1)-(#R exponent1).

The centers of successive R/L square faces form a nearest-neighbor dual-lattice path. At an interior syllable, exponent2 is straight, R exponent1 turns left, and L exponent1 turns right. Thus f is the clockwise quarter-turn sum of this path, apart from endpoint conventions. The raw c and this f must not be confused with the physical ant's accumulated un-reduced heading rotation.

## Exact online deficit dynamics

Let q=2m+3-c(r). Starting from q=3, the update is:

* append R without cancellation: q decreases by 1;
* append the fourth R and cancel R^4: q increases by 3;
* append an already-seen-cell L without cancellation: q increases by 1;
* first-read L without cancellation: q increases by 3;
* append the fourth already-seen-cell L and cancel L^4: q decreases by 3.

(The first-read-L cancellation case gains 2 additional units.) A proof must therefore constrain the R-extension and L^4-erasure cases using physical revisit consistency. Autonomous coset legality alone is insufficient.

## Failed local shortcut

It is false that every clockwise simple dual-core loop must enclose or encounter an initial black cell. On the blank run reduced after 30,000 steps, stages85 through93 describe the dual square

 (1.5,.5),(1.5,1.5),(2.5,1.5),(3.5,1.5),
 (3.5,.5),(3.5,-.5),(2.5,-.5),(1.5,-.5),(1.5,.5).

The associated syllables are R,L,R^2,L,R^2,L,R^2,L,R. This is a clockwise area-4 loop. The internal quarter-turn sum is3, with the omitted closing corner accounting for the fourth turn. The trace is only a finite diagnostic unless separately justified as permanent, but it already defeats the analogous claim for all reduced prefixes. See inspect_core_loops.py and core_loop_controls.json. Any proof of (C) needs credit accumulated before such a loop, rather than a fresh-seed charge for every individual clockwise loop.

## Why a causal-forest proof is not yet available

Each consumed black token is paired to its most recent R producer, or to an initial-black root. The resulting cursor ancestry is an exact forest with at most m+1 roots. But root count does not bound descendants, and restoration of a cell's color does not restore its token ancestry. In particular, G_R(1)=RRLLLLRR replaces an interior black token by an entry-descendant token even though its final color is restored. Repeated physical copies of a vertex must not be assumed to admit a planar history embedding. A ribbon-surface/Euler-characteristic route remains a possibility, not a proved reduction.

## Scope if proved

(C) would provide a genuine seed-dependent one-sided bound on reduced signed curvature. It would rule out indefinitely accumulating positive dual-core winding without matching negative excursions. It would NOT rule out aperiodic zero-average paths, negative-winding spirals, or locally compensating positive/negative loops. A further dynamical mechanism would still be required for core periodicity.

## Checkpoint and deliberate pivot, 19:27 UTC

This approach reached a proof plateau. The unresolved implication is precisely that repeated L reads carry enough ordered, chronological negative-curvature credit to offset their possible new R-run allowances. The trivial reduced-word inequality c<=2*(number of L letters)+3 explains the coefficient two, but replacing all L letters by first-L cells remains unproved. No unsupported global curvature claim will be used downstream. The analysis has pivoted to the exact adjacent-bad-pair renewal map and directed supply/rank constraints.

Further negative controls: the stronger proposed inequality c+2||position||_infinity<=2m+7 is FALSE, with an exact m=3,length200 witness in curvature_radius_control.log. Frozen active-loop continuations do not preserve the blank maximum3: their maximum reduced curvature reaches6 by t=13. These diagnostics defeat the corresponding simple potential candidates and are not statements about the ant's actual future.
