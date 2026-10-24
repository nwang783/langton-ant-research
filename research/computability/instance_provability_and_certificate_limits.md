# Individual provability and limits of counterexample certificates

Status: exact conditional metatheorems, independently analytically audited on 2026-10-22 at22:34 UTC. No undecidability or independence result for the actual ant is claimed.

## Setup

Let H(X) mean that the finite complete ant state X eventually has a cyclic standard104 turn tail. The exact tail verifier supplies a computable witness predicate V such that

    H(X) iff exists w V(X,w).

One can include the finite accepting computation of V in w, making this an ordinary Sigma1 arithmetic formula with a primitive-recursive finite proof checker. Let P be the c.e. set of states having some translating periodic turn tail that is not standard104. Let A be the remaining aperiodic states. Thus

    not H = P disjoint_union A.

These sets and their exact verifiers are described in `aperiodicity_obstruction.md` and `periodic_tail_checker.py`. A rigid full-orbit class consists of integer-time shifts, translations, and quarter rotations of one finite complete state. Each such class is c.e., and H, P, A are constant on it.

## 1. True positive instances have finite proofs

Fix an ordinary arithmetic base that formalizes the ant rule and proves soundness of the standard and nonstandard periodic-tail verifiers. Every actually capturing finite state X has a finite certificate w. Its finite verification can be checked inside the base, and the proved verifier implication then yields H(X).

Therefore a true capturing instance is not an unprovable positive instance in any theory extending this base. The universal conjecture

    for every finite X, H(X)

could nevertheless be true but unprovable: proving each instance, with no uniform proof of total certificate search, is not a proof of the universal statement. This is the same uniformity distinction as an unproved totality statement for a program that really halts on every input.

This observation does not claim a feasible proof length, an available numerical time bound, or any independence of the actual conjecture. A true NONCAPTURING statement is instead negative/Pi1 and can in principle evade a given proof system.

## 2. Any sound effective negative-certificate scheme

Let N be any c.e. subset of the actual noncapturing states. Think of N as the states for which a fixed sound effective certificate scheme proves noncapture. Suppose H is undecidable.

Then A minus N meets infinitely many rigid full-orbit classes.

Proof. Otherwise choose representatives X_1,...,X_r of the finitely many classes containing all states in A minus N. Every chosen class is wholly aperiodic, so wholly noncapturing. Enumerating N, P, and those finitely many c.e. classes would enumerate all of not H, and nothing else. Since H itself is c.e., this would decide H, a contradiction. The representatives are hardcoded in this existence argument; no effective way to find them is assumed. QED.

Thus actual undecidability would force infinitely many genuinely aperiodic orbit classes beyond EVERY one sound effective negative-certificate scheme. Failure of a particular certificate search is not evidence that such classes exist: the premise H undecidable remains unproved.

## 3. Formal theories

Take N to be the states X for which a fixed recursively axiomatized theory T proves not H(X). If T extends the base from Section1 and is consistent, then N is sound for these negative statements: a false not-H theorem would concern a truly capturing X, whose H theorem already exists in the base, contradicting consistency.

Consequently, IF H is undecidable, infinitely many aperiodic rigid orbit classes contain states whose noncapture T does not prove.

To strengthen this to fully T-independent instances, impose Sigma1-soundness (or soundness for the particular H-instance formulas). A merely consistent extension can falsely prove a Sigma1 capture statement, so consistency alone does not establish independence. Under Sigma1-soundness, every state in A minus N has neither a T-proof of H(X) nor a T-proof of not H(X).

No proof of a concrete independent ant state or of an independent universal conjecture follows from these conditional metatheorems.

## 4. Consequence for synthesis languages

The same argument applies to any effective all-time trajectory certificate language with a decidable verifier and a sound decidable standard-capture query. Examples include the automatic-history and ordered-event certificate frameworks in this directory, within their stated encoding hypotheses.

If every finite input had such a certificate in one fixed effectively enumerable family, one could enumerate certificates matching the supplied input, verify them, and answer the capture query. That would decide H. Thus undecidability of H would force states outside every such complete effective presentation family. With standard and nonstandard periodic certificates included, Section2 strengthens this to infinitely many aperiodic rigid classes lacking a sound negative certificate in the chosen family.

This is a limitation conditional on actual undecidability, not a reason to stop using effective synthesis: a single valid negative certificate would already refute the highway conjecture, and H could be decidable even if the conjecture is false.
