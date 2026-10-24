# Exact future pruning: oracle boundary and a total first-three-input interface

24 October 2026. AUTHOR analytic reduction and bounded executable controls; independent audit requested. This is not a claim that finite-seed noncapture is undecidable or unrecognizable.

## 1. What was already proved and is not being claimed anew

The retained computability work already provides an exact arbitrary-period translating-tail verifier and proves that universal finite-seed eventual periodicity would make all first-order space-time queries decidable. See ../computability/local_reachability_reduction_scope.md and its audited dependencies. The exact canonical absorber and full-field periodic ray tests are also retained.

Thus a genuine finite-seed halting-to-local-reachability compiler would refute universal translation; infinite-background universality does not supply one. No such finite compiler or undecidability result is constructed here. In particular, if universal canonical capture is true, noncapture is empty and decidable. It would be incorrect to label noncapture inherently unrecognizable on the basis of universality folklore.

The new point here is the precise computational status of the ENTIRE future-relevant pruning used by the rho criterion, and a restricted total operator made possible by the newly signed at-most-two-black canonical theorem.

## 2. Whole pruning has exactly the finite-cell reachability oracle strength

For a finite complete state X=(B,p,h), let Prune(X)=C*(X), the current BLACK cells whose current identities are eventually consumed. Let Hit(X,q) mean that the head visits the specified physical cell q at some nonnegative future cut.

Given a cell-reachability oracle, Prune(X) is computed by asking Hit(X,q) for each of the finitely many q in B. The first such visit consumes its original BLACK identity.

Conversely, to decide Hit(X,q) with a whole-pruning oracle, form

    X_q=(B union {q},p,h).

The trajectories of X and X_q are identical until the first read of q. Therefore q is visited in one if and only if it is visited in the other, regardless of the different turn at that first read. Since q is initially BLACK in X_q,

    Hit(X,q) iff q belongs to Prune(X_q).

This is a uniform one-query reduction. Hence the total set-valued pruning function and arbitrary finite-cell reachability are Turing-equivalent. This does NOT show either one is noncomputable; their actual decidability remains unproved.

For a supplied state and radius R, rho(X)>R is computably enumerable: simulate until some original BLACK cell outside the head-centered R box is first read. Hence rho(X)<=R is co-c.e. This observation alone does not show the scalar radius function is noncomputable, and no reverse reduction from full pruning to that scalar is asserted.

## 3. A new total restricted operator: exact pruning if at most two, otherwise the first three

The signed all-position at-most-two-black canonical theorem supplies a total certificate search for every finite comparison board of size0,1,2, at any actual pose. It does NOT supply capture of the arbitrary full input below.

Given an arbitrary finite full board B, keep its ORIGINAL current black identities fixed. Start S=empty. Repeat:

1. Compute a certified complete future for the comparison state(S,p,h). It has at most two initial black cells, so the signed theorem guarantees eventual canonical capture. Its finite transient plus exact104 tail is an effective complete description.
2. Find the earliest visit to any cell of B minus S along that entire comparison future. The finite prefix is explicit; the infinite tail is checked by exact arithmetic q=Q_i+k*d, k>=0. There are only finitely many omitted original cells.
3. If there is no omitted-cell visit, return Prune(X)=S, with exact original consumption times and a full-board canonical certificate. Every omitted initial bit remains in the board but is never read.
4. If a visit exists, add that one original cell to S. If this is the third distinct cell, return those first three actual original-cohort contacts and stop. Otherwise repeat from the ORIGINAL comparison cut, not from the hit state.

At most three comparison runs are used. Each run has at most two initial black cells and therefore terminates. The earliest omitted-cell test is finite exact arithmetic. The resulting operator is TOTAL on every finite full input.

## 4. Correctness and the no-reset condition

Inductively, S consists of the first k actual consumed ORIGINAL identities, k<=2. The actual input and its comparison(S,p,h) differ initially only at omitted original cells. Until the first visit to any omitted cell, they therefore have identical reads, toggles, poses and complete generated output. In particular, every required first-read white condition is preserved.

The next omitted-cell visit is consequently the next actual original input consumption. A newly born R lifetime is NOT a member of the fixed original cohort. A later second read of a selected physical cell is not counted again. The comparison always starts at the original cut, so fresh output is never discarded or converted into free restart fuel.

If no omitted input is ever visited, the entire actual future is the comparison future; all other black cells are retained and unread. Since each member of S has a recorded actual first visit, S is exactly the full future-relevant pruning, not merely an upper bound.

If a third original input is found, the operator certifies only that fact. It does NOT classify the rest of Prune(X), decide capture, or certify noncapture. Capturing histories routinely take this branch.

Consequences:

- The predicate |C*(X)|<=2 is decidable on arbitrary finite full boards.
- On its positive branch, exact C*(X), rho(X), original-cohort completion time and a canonical tail certificate are computable.
- On its negative branch, three genuine original input identities and their first consumption times are supplied effectively.
- Every hypothetical noncanonical input must take the three-input branch at every cut, but repeatedly applying the operator does not prove termination, bound the number of renewals, or force compact recurrence.

The qualitative statement that a noncanonical input cannot have at most two future-relevant current cells was already available by deleting never-read bits. The contribution here is the TOTAL constructive first-three-or-exact-pruning interface, using complete certified comparison futures rather than an unbounded wait for the third contact.

## 5. A restricted effective rho test

Let I=B intersect the head-centered radius-R box. If |I|<=2, compute the complete captured future of comparison(I,p,h) and its first hit of B minus I.

- No hit means every outside original bit is forever unread, so rho(X)<=R.
- A hit is an actual first outside original input and proves rho(X)>R.

This is a total exact test on that explicitly sparse-interior class. It does not apply merely because one hopes the future-relevant inside population is small; the supplied premise is the number of CURRENT BLACK cells inside the box.

This operational interface should not be confused with a general algorithm for recognizing compact whole-relevant geometry.

## 6. Retrospective compact recurrence still has finite positive certificates

The independently signed recurrence bridge says that bounded rho at infinitely many cuts is equivalent to an eventual nonzero translating periodic future. Its proof is retrospective: two equal normalized full prunings in one orbit determine the same future, while a translator has bounded normalized pruning.

Because eventual translation has exact finite periodic-tail certificates, compact recurrence is nevertheless computably enumerable as a PROPERTY OF THE WHOLE INPUT, via that equivalent certificate search. This does not make the individual-cut rho test effective, identify the compact cuts during a run, or prove the certificate search always terminates.

The persistent escape alternative rho(t)->infinity is therefore the co-c.e. complement of eventual translation, by that equivalence. Its actual recognizability or decidability is not established. No new universality, undecidability, independence or global attraction conclusion is inferred.

## 7. Executable controls and limits

prune_two_original_inputs.py implements the comparison algorithm and the sparse-interior test. The mathematical version is total by the signed two-black theorem. The execution harness supplies an explicit200000-read comparison budget; budget exhaustion is UNKNOWN, never a negative result. None of the named runs exhausted that budget.

Controls include empty input; a singleton at the head with eight complete retained but never-read remote inputs; two black cells; three black cells; a four-cell G-shaped input with heading N; and the fourteen-cell defect input with heading N. Actual first-contact lists are independently replayed against their FULL original boards. The one-hit-plus-unread control returns exact pruning of size1, while the three/four/fourteen-cell controls return the actual first three identities, not a false noncapture label. Three sparse-radius controls and force-BLACK first-hit equivalence controls include exact all-future no-hit certification.

The comparison terminal certificates are checked against every retained current black cell by exact infinite phase-ray parity. Long sampled repeats are only candidate generators, not acceptance tests. The signed all-position source theorem is the termination premise; the finite control runs are not a replacement proof of that theorem.
