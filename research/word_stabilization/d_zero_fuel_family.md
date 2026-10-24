# A zero-new-fuel diagonal block which can continue

Status: exact finite-ingredient proof, not yet independently audited. This is a negative control, not a counterexample to standard104 capture.

Let D=LLLLRLRRRR and P=U C C V, with the literal U28,C15,V18 words bound in certify_d_zero_fuel_family.py. For every integer n>=1, the word P D^n is physically feasible from a finite initial black set, and its minimal entry mass is n+10. Its length is 76+10n. At the first D block, every local first-L site was already read earlier in P. Nevertheless D can continue with another D; it can also continue with C,V or U in separate finite controls.

## All-parameter argument

Literal P ends at (-2,2,S). D restores its heading and translates by (-1,-1) in this frame. Reconstruct all ten read offsets. Solving equality between offsets in two translated copies shows that different copies can share a cell only at copy separation at most two. Solving equality with the fixed P footprint shows that only copies numbered zero and one can meet P.

The checker verifies D^4 and P D^6 literally. These are a complete finite cover, not an extrapolation in n: any first equal-consecutive-read conflict wholly in the D suffix has both visits in a window of at most three consecutive copies, hence translates to D^4. Any conflict whose earlier visit lies in P has its later visit in copy zero or one, hence occurs in P D^6. Both are absent. Thus all finite powers are feasible.

For first-L freshness, all possible same-copy and earlier-copy predecessors are among the preceding two copies. From copy two onwards, all possible predecessor-copy offsets exist, and none can lie in P. Hence the new first-L phase set is stationary there. The finite cover finds no new first-L in copy zero and exactly phase1 in every copy numbered one or later. P itself needs eleven entry-black cells. Therefore P D^n needs precisely 11+(n-1)=n+10 entry-black cells.

## Shortest explicit witness

The eleven-cell initial black set is

    {(-2,3),(-1,-1),(-1,0),(-1,1),(-1,2),(-1,4),
      (0,-1),(0,0),(0,2),(0,3),(1,0)}.

The initial pose is (0,0,N). The first D begins at time76 and pose(-2,2,S). Its local first-L phases0,1,2,3,5 have earlier last reads at global times72,21,70,75,73, all R. Its old phase1 input is therefore the U phase21 cell, precisely the unbalanced U CC V return obstruction encountered in the earlier C15-only language. Truncating that terminal C to D removes the old continuation barrier.

The seven-word shifted/coalesced quotient admits P D^n paths for arbitrary n; the finite state-set iteration is recorded. This is only a graph-path control and is not an assertion that one finite seed realizes an infinite D tail. Indeed the exact mass n+10 diverges with n. The quotient transformations themselves are exploratory, not dependencies of any signed global theorem.

## Checker and certificate

certify_d_zero_fuel_family.py regenerates literal positions, all overlap equations, the finite-cover feasibility checks, fresh phase sets, the shortest seed replay, and the quotient state-set loop. d_zero_fuel_family_certificate.json records their outputs and the source hash.

## Independent audit

On 2026-10-22 the separate checker ../audits/check_d_zero_fuel_family_independent.py verified the all-parameter overlap proof, stationary fresh-site formula, and the nine-cell DVCCVCDDCD negative control. Its JSON output is alongside the checker. No extrapolation from finite simulations is used in the all-n statement.
