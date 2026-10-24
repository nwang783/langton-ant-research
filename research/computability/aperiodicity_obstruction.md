# What an undecidability reduction would have to create

Research date: 22 October 2026. Status: analytic metatheorems independently reviewed by the audit analysis. These do not prove undecidability, independence, a counterexample, or the highway conjecture.

## 1. Three disjoint behavior classes

Let H be the finite complete states whose eventual turn stream is the fixed standard104 word, up to cyclic phase. Let P be those whose eventual turn stream is periodic but not standard104. Let A be those whose turn stream is not eventually periodic. Thus E=H union P is the eventually-periodic class, and A is its complement.

A periodic turn word with nonzero net heading rotation yields a bounded geometric path after at most four copies. A heading-restoring zero-drift word also yields a bounded path. Neither can be an actual infinite ant suffix, by finite-domain escape. Hence every actual eventually periodic turn stream has a heading-restoring period with nonzero displacement.

For any supplied HEADING-RESTORING nonzero-drift period word, whether a supplied complete finite state follows that word forever is decidable: partition the finitely many phase positions into translation classes modulo the full drift, or use exact finite-field/self-write parity thresholds. This is the same elementary arithmetic underlying existing highway terminal certificates, but it applies to arbitrary supplied period words.

Consequently H, P and E are all computably enumerable, and H and P are disjoint. To enumerate E, dovetail all start times and finite period words, verify their infinite tails, and output the successful certificate. To decide whether a verified periodic tail is standard104, compare its infinite word against the finitely many phases of W104 over lcm(|v|,104) positions. The comparison is finite and exact. If it is nonstandard, no later shift can become standard: two purely periodic words agreeing on a suffix agree everywhere after the corresponding phase alignment.

No completeness claim is made about these c.e. sets. In particular, H might be the set of every finite input.

## 2. Undecidable H forces genuine nonperiodicity

Theorem 1. If every finite seed is eventually periodic, H is decidable.

Proof. Search for any verified periodic-tail certificate, which terminates under the premise. Classify its period by the finite word comparison above. QED.

Corollary. If H is undecidable, there exists a genuinely non-eventually-periodic finite seed. Nonstandard periodic highways alone cannot account for undecidability of H.

More generally, if A is c.e., H is decidable: dovetail an A recognizer with the E recognizer. The first decides nonperiodicity, while the second returns a period that determines H membership. Thus undecidability of H would prove that A is not recognizable, not merely that H's complement is not recognizable.

## 3. A single exceptional orbit cannot hide undecidability

Let ~ identify complete finite states related by time shift, translation and quarter-turn rotation. This equivalence is decidable by rigid_reachability.md, and eventual periodicity is invariant under ~.

Theorem 2. If A consists of only finitely many ~-classes, H is decidable.

Proof. Let a_1,...,a_k be one finite representative of each such class. A decision program may contain this fixed finite list as constants; the theorem is an existence-of-algorithm implication and does not claim an effective way to discover the list from an unspecified finiteness premise. Test whether X~a_i for some i. If so return  Otherwise X is in E, so search for its periodic-tail certificate and classify it. QED.

Corollary. If H is undecidable, A contains infinitely many inequivalent complete space-time orbits, even after quarter-turn rotation and translation. The same conclusion applies within the range of a computable many-one reduction from an undecidable language to H: finitely many exceptional ~-classes in that range would give a source-language decider by the same procedure.

The decidable equivalence relation is more than this corollary needs. Each individual rigid space-time class is already c.e. by enumerating integer time shifts and rigid motions; a finite union would make A c.e. and Theorem 1 would suffice. The rigid reachability theorem remains independently useful for explicit acceptance-target decisions.

This is stronger than the observation that some noncapturing seed must exist. It is still only a conditional restriction on any possible reduction.

## 4. Correct reduction polarity

Because H is c.e., a computable many-one reduction NONHALT <=_m H is impossible: otherwise NONHALT would be c.e. This is an unconditional obstruction, regardless of whether the highway conjecture is true.

The useful orientation for a counterexample/universality route is

   machine e halts  iff  f(e) is in H,

with f a total computable compiler into COMPLETE FINITE physical black sets. Equivalently, nonhalting maps to noncapture. That orientation is not known to exist. If it did, H would be c.e.-complete and the universal conjecture would be false; Theorems 1 and 2 show that the compiler would also produce infinitely many inequivalent genuinely aperiodic outputs.

A reduction from the plane-tiling existence problem, when phrased as a co-c.e. existence property, likewise cannot map tileability to positive H membership. It would need the complement polarity (non-tilability to capture / tileability to noncapture), or a different target. This states the hierarchy obstruction, not an actual ant tiling simulation.

With an oracle for E one can decide H: ask whether X is eventually periodic; on NO return  and on YES find and classify a periodic certificate. Thus H <=_T E. A halting-complete H would force E to have the complete c.e. Turing degree as well. No reverse reduction or equality H=E follows without an additional periodic-tail classification theorem.

## 5. Formal-system distinction

The universal conjecture has the form forall encoded finite X exists t C(X,t), where C is a computable exact standard-tail verifier. This is a Pi_2 presentation, not a Pi_2-hardness result. A single fixed sentence is not itself a varying-input undecidable decision problem.

Every particular positive instance has a finite simulation and tail certificate, so it has a finite formal proof in an arithmetic theory strong enough to verify those elementary integer calculations. A true universal statement can nevertheless be unprovable in a particular effective theory because the theory cannot prove the unbounded search total. No such independence has been proved for this ant statement, and the formal theory must be named before an independence claim is meaningful.

If the universal conjecture is true, the maximum capture time over all inputs of encoding length at most n is a total computable function: enumerate the finite set of inputs and wait for every exact capture search to terminate. That does not imply a tractable bound or a bound provably total in a chosen weak theory. It does rule out saying the worst-case function is intrinsically noncomputable merely because the transients look complicated.

## 6. Explicit arbitrary-period tail verifier

Let v have length P, restore the supplied heading, and have nonzero drift d. Let q_i be its absolute pre-update phase positions. At time kP+i, the required actual black bit is

   1_B(q_i+k d) XOR #{(j,s): q_j-q_i=s d,
                      s>0 or (s=0 and j<i), s<=k} mod 2.

The self-write part changes only at the finitely many nonnegative thresholds s obtained from phase pairs. The initial-field part is nonzero only at finitely many computable integer ray hits k, because B is finite and d is nonzero. For each phase, test epoch zero, every threshold s, every hit k, and k+1 after each hit. They delimit all constant intervals, including the final infinite interval. Agreement with v_i on those tests proves agreement at every epoch; induction on updates then proves the prescribed infinite trajectory. Taking the earliest mismatching test epoch/phase instead gives the exact first mismatch.

The implementation periodic_tail_checker.py was written independently of existing ant modules. Its controls verify all 104 phases in four rotations, direct early mismatch agreement, and an initial defect at epoch 10^30 without simulating to that time. periodic_tail_controls.json records those finite controls. The all-time proof is the parity formula, not the test count.

## 7. The exact degree of the positive-instance delay envelope

Status: independent analytic review passed on 22 October 2026.

Fix a finite binary encoding of complete finite inputs, and let tau(X) be the LEAST physical time at which an exact standard104 tail certificate passes. This is a partial computable function, defined exactly on H: test times in increasing order and the finite set of standard phases at each time. Define the total finite-valued envelope

    F(n)=max({tau(X): encoding_length(X)<=n and X in H} union {0}).

There are finitely many encoded inputs of length at most n, so F(n) is mathematically defined even if some of those inputs never capture. The function is nondecreasing and lower semicomputable, by enumerating successful capture searches. Its exact Turing degree is the degree of H:

- Given an oracle for H, list the finitely many positive inputs of length at most n, run their searches, and take the maximum. Thus F<=_T H.
- Given F, decide X in H by testing all candidate capture times through F(encoding_length(X)). Thus H<=_T F.

In particular, H is decidable if and only if F is computable. Equivalently, H is decidable if and only if there exists ANY total computable upper bound g(n) on the positive capture times of all inputs of length at most n. The reverse direction only needs bounded finite search through g(n); the forward direction uses F itself.

If H were undecidable, then for every total computable g there would be infinitely many n with F(n)>g(n). Otherwise finitely many exceptions could be absorbed into a fixed finite constant, yielding a computable upper bound and a contradiction. This is an infinitely-often growth statement, not a claim that F eventually dominates every computable function.

If the universal conjecture is true, H is the constant-YES set and F is computable. Enormous observed transients do not contradict this, and they do not prove that F grows like a universal Busy Beaver function. The encoding-length domain is essential: fixing the NUMBER of initial black cells while allowing arbitrarily distant coordinates does not give a finite input set, and the corresponding delay supremum can be infinite.

### 7.1 Fixed one-black mass already has an infinite delay supremum

This is an inherited certified scattering family, not a new simulation theorem. For n>=200, start at (0,0),N with exactly one black cell

    q_n=(-33-2n,-14-2n).

The all-parameter exceptional-rectangle proof, Section2's one-bit prefix, certifies an entire standard NW tail by time 208n+70733. Its first contact with q_n is at t_n=104n+10881; before that contact the orbit equals the blank orbit. At t_n the standard phase72 white read R is changed to L, whereas t_n-104 still has the old R read. Any 104-periodic tail onset T must therefore satisfy T>t_n-104. In particular,

    104n+10778 <= tau({q_n}) <= 208n+70733.

Thus the supremum of actual permanent standard-capture time over seeds of black mass1 is infinite, although every member of this particular family has a certified tail. This says nothing about unbounded defect COUNT at fixed mass.

Authoritative dependencies: continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_proof.md, Sections1-2; exceptional_rectangle_affine_certificate.json; audit.md SectionA and audits/exceptional_rectangle_replay.log. The template JSON itself still carries its original candidate-extraction status; the later exact affine verifier and independent audit, not the two-run extraction, justify the all-n theorem. The phase0 version at 208n+70738 is also used and documented in scattering/retained_frontier/PROOF.md.


## 8. Independence alone would not imply fast-growing transients

A separate logical pitfall is to infer that a universal capture statement, if independent of a theory, must have capture delays beyond that theory's provably total growth rates. That inference is not valid without additional structure.

For an elementary abstract counterexample, suppose U=forall n R(n) is a true but unprovable sentence of a named theory T, with R a computable bounded witness predicate. Define an artificial exact capture test

    C(n,t) iff R(n) and t=1.

Its positive membership problem is decidable by evaluating R. Every positive instance captures at time1, and its positive delay envelope is at most1. Yet forall n exists t C(n,t) is exactly U and remains unprovable in T. This is an abstract logical example, NOT a model of the ant's physical transition rule.

For the ant, no independence result has been established. If HC were true but unprovable in T, the particular exhaustive capture-search program's totality would likewise be unprovable in T, provided T formalizes the elementary equivalence. It would not follow merely from this that the numerical delay function outruns every T-provably total function. The missing proof could instead concern the correctness of a small bound, rather than the size of that bound.
