# Final adversarial proof audit

Reviewed the three notes in `constructive_alternatives/` and independently fetched the pinned square-clock proof at commit `22e0c9edcc566a4c2f7a9bf92f5cd05c19199617` (file SHA `a31945aed3504dc618f55a01b73c60cf6e68207f`). No new simulations were run.

## Verdict

**All principal mathematical statements are valid, with their stated limited scope.** I found no counterexample or hidden deletion of relevant history. The final marginal-clock-count interpretation benefits from one explicit coordinate clarification below; its displayed identity and nonnegativity claim are correct.

| Statement | Status | Essential qualification |
|---|---|---|
| Exact column invariant and its row rotation | Valid | All eight local branches agree modulo four under the stated white-right convention. |
| Two-endpoint displacement bound | Valid | Counts changed cells in strict intervening columns; it does not count crossings or accumulate a retreat penalty. |
| Distance beyond the initial rectangle | Valid | Bounds current distance, not retreat or support diameter. |
| Uniform mass-ceiling escape time `U(K)=E(K+2)` | Valid | The clock includes the exit update, so there is no missing extra step. |
| Finite-state alternative `V(K)` | Valid | The exterior field is fixed throughout the confined prefix and remains part of the complete state. |
| Four-cell endpoint compatibility with all stated clock centers | Valid as an endpoint construction | No actual transition or infinite orbit is established. |
| Adjacent-endpoint marginal gain identity | Valid | Counts solve separate projected identities; path and color consistency remain open. Clarify the center convention as below. |
| No recurrence of a complete centered finite state | Valid | Uses the two-endpoint bound and positional unboundedness. |
| Uniform low-mass occupation estimate and mean-mass divergence | Valid | Gives vanishing frequency and divergent averages, not pointwise divergence of mass. |
| Two bounded-retreat inequalities imply a translating periodic trace | Valid | Concerns position, heading, and turn trace; it neither proves the hypothesis nor classifies the period as 104. |

## Checks that matter

### Signed cuts and escape time

On strict opposite sides of a column the head potential changes by two modulo four. Each changed cell contributes `+1` or `-1`, and unchanged black cells cancel. Therefore at least two distinct changed cells lie in each of the `|x_t-x_s|-1` intervening columns. This proves the stated symmetric-difference bound and hence the two-endpoint bound. The same argument after rotation gives the row bound. The strict endpoint convention is correct, including displacement zero or one.

If every observed mass is at most `K`, the positions at all times `0,...,U(K)` have coordinate spans at most `K+1`, and hence fit in a square with `K+2` lattice cells per side. Choosing that square retrospectively is legitimate because the escape clock is uniform over placements and exterior colors. The source clock has range at most `R_n` on internal states; `T-1` internal updates precede first exit, giving `T <= R_n+1 = E(n)`. Substitution gives exactly

`U(K) = [39*3^K - 2*K^2 - 12*K - 21]/2`.

I checked the clock's sign cases, integer-valuedness, field-range sum, and head-range bound. They justify the quoted dependency independently of experimental evidence. In the alternative argument, observations `0,...,V(K)` supply `V(K)+1` complete states and therefore the required repetition.

### Occupation bound

A centered-state recurrence with drift `d` gives equal endpoint mass at every repeated period boundary. Applying the cut bound to increasingly distant boundaries forces `d=0`; an exact full-state recurrence then contradicts unboundedness. The invariant `heading - mass (mod 4)` fixes the heading for each mass on one orbit, so the central-state count requires no extra factor four and the zero-mass state occurs at most once.

At a noncentral observation `a`, the removed comparison cell has distance strictly greater than `R`. It cannot be read in the next `R` updates. Thus the comparison is valid throughout the observation block `[a,a+R)`, with masses differing by exactly one. Each comparison trajectory is a legal finite-support trajectory, so the uniform function `A_(K-1)(R)` applies separately to every block. Greedy block starts are at least `R` apart, giving at most `ceil(N/R)` blocks even when the last extends beyond the target interval. No cell is deleted from the trajectory being bounded.

The recurrence, `S_K(R)` estimate, floor/ceiling estimates, induction exponents, and coefficient comparison all check. In particular, `D_K=2K D_(K-1)+1`, the closed form for `D_K`, and `C_K=2(K+1)9^K` are consistent. The mean bound follows directly by counting observations of mass at least `K+1`; its stated threshold is `(2C_K)^(D_K)` and is correct. Quantification is uniform over starting times, support diameters, and initial fields.

### Bounded retreat

Linear independence makes `W` finite, including for irrational coefficients. The retreat assumptions bound both forms below; unboundedness then forces one form to be unbounded above, and bounded retreat upgrades this to convergence to positive infinity. All cells of the finite restarted input eventually lie strictly behind the resulting future lower bound.

For any other black cell, a past visit supplies both upper window inequalities, and a possible future visit would supply both lower inequalities. Every black cell outside the window is therefore actually future-invisible. The first-divergence argument justifies deletion for the entire future, not merely for a finite prefix. Equal reduced masks are complete finite states, so their futures agree by translation covariance; the original trace inherits those equalities. Zero displacement would make the position trace bounded, which is impossible. The pigeonhole period bound `4*2^|W|` has the correct endpoint count.

## Minor coordinate clarification in the endpoint-count section

For a physical diagonal level `ell`, a `+ -> -` epsilon reversal contributes `4g(c-ell)`, whereas a `- -> +` reversal contributes `4g(ell-c)`. Thus the interpretation of `A_d g(z-d)` as `+ -> -` counts is immediate with:

- the `x+y` clock: `z=c-1`, `d=ell-1`;
- the rotated `x-y` clock: `z=c`, `d=ell`.

Earlier in the note `z` was `1-c` or `-c`. Since the endpoint difference `D(z)` is even, replacing those by the conventions above leaves every identity unchanged. State that replacement explicitly before assigning the epsilon labels. Otherwise the earlier convention reverses which coefficient represents which epsilon transition. This is a labeling clarification, not a failure of the nonnegative marginal solution.

The three formulas for `V(z)` are correct, including both shared boundaries. The residual identity in `a <= z <= b` uses the three integer points `a,a+1,a+2`, as stated. The minimum of the all-center clock difference is exactly `2*(3^b-3^a)`, attained at center parameter zero. These facts establish endpoint compatibility only; they supply no missing chronology.

## Material limitations

The notes do not prove pointwise mass divergence, bounded retreat for arbitrary finite inputs, eventual periodicity without that hypothesis, period-104 classification, or the full Langton-ant highway conjecture. Complete finite configurations are not claimed to translate periodically in the bounded-retreat theorem; unread black wake can continue to accumulate. No novelty or priority conclusion follows from this audit.
