# Why the current computability structure alone cannot settle capture

22 October 2026. Status: elementary model-separation construction independently
audited, including negative clocks and true-history event boundaries. This is NOT a model of Langton's ant and
NOT an undecidability reduction to the ant.

## 1. A reversible toy system

Let B(e,n) be the primitive-recursive predicate saying that program e has
halted within n computation steps, with B(e,n)=false for n<0. A state is

    X=(e,c,t),

where e is a program code, t is an integer clock, and c is either a nonnegative
integer cutoff or infinity. Its update is simply

    F(e,c,t)=(e,c,t+1).

It is computably reversible and has the strict integer clock Theta(X)=t.
Complete signed orbit equivalence is decidable: the e,c coordinates must agree,
and then the unique signed time offset is the difference of clocks.

Give a state the binary observable

    a(e,c,t)=1 iff t is a positive power of2,
                    B(e,t) is false,
                    and (c=infinity or t<c).

Otherwise its observable is0. Thus an uncapped nonhalting program emits1 at
powers of2, while every capped or halting program eventually emits only0.
The update, observable and their bounded iterates are elementary computable
in explicit binary encodings; bounded universal simulation is sufficient.

Define H_toy to mean eventual0. Then

    H_toy(e,c,t) iff c is finite or program e halts.

For c=infinity and a nonhalting e, the infinitely many1s have unbounded gaps,
so the observable is not eventually periodic with ANY period. Hence H_toy is
c.e.-complete and its noncapture set is co-c.e.-complete; no nonstandard
periodic inputs exist.

## 2. Exact arbitrary-period tail certificates are decidable

Given a nonempty proposed periodic binary word w, any w containing1 is
impossible: every actual periodic tail in this system is all0, by the previous
paragraph. For w consisting only of0, let p be the least positive power of2
with p>=max(t,1). There are no possible1s between clock t and p. The whole
future is all0 exactly when the marker at p is suppressed, namely

    B(e,p) or (c finite and c<=p).

If it is not suppressed, its literal1 is an immediate counterexample to the
all0 tail. If it is suppressed, the suppression persists forever. This gives
an elementary exact verifier for every proposed periodic tail, despite
undecidable EVENTUAL capture.

## 3. The next adjacent defect is an elementary total operation

Take the target standard word to be0^104. A bad-ten event J(u) means the ten
observables ending at integer clock u are not all0. Define K(u)=J(u-1)J(u),
using the unique true two-sided history. An isolated marker1 at p gives
adjacent events at p+1 through p+9. Early neighboring markers can merge such
intervals, but do not invalidate this implication.

Using the same next-marker p, inspect all events from t through p+10. If the
marker at p is active, a K occurs by p+1. If it is suppressed, there are no
future1s from p onward, and any remaining boundary K ends before p+10.
Consequently this finite inspection finds the first future K or proves none
exists. It is elementary and total. Returning the state just after that K
is the exact renewal map; its iteration terminates iff H_toy.

Thus this system simultaneously has:

- an invertible computable update and a strict computable integer clock;
- decidable complete-state orbit equivalence;
- exact decidable certificates for any proposed periodic tail;
- an elementary total next-adjacent-defect map;
- capture exactly when only finitely many adjacent defects occur;
- c.e.-complete eventual capture and unrecognizable aperiodic noncapture.

The actual ant's corresponding structural results therefore cannot, BY
THEMSELVES, prove universal capture or rule out c.e.-complete capture.
Additional ant geometry, color chronology or conserved charges must enter.

## 4. Capturing finite-prefix completions do not repair this gap

For any observed finite future prefix of (e,infinity,t), choose a finite cutoff
c larger than every clock in that prefix. The state(e,c,t) has the identical
prefix and eventually emits only0. The same is trivially true if the original
state was already capped. Hence every finite observable prefix has a capturing
completion, while capture remains undecidable over the full input family.

This parallels the logical density consequence of the ant's four-cell port,
not its detailed geometry or exact four-black-cell bound. The new cutoff is
an unbounded integer parameter. No statement about actual ant seeds follows.

The example also illustrates the event-count compiler obstruction: a late
halting program emits only logarithmically many marker groups in its running
time, but no computable function of its code can bound those finite counts
on all halting programs. Such a bound would decide halting by the exact
finite-count query. Sparse defects can still carry uncomputable complexity;
a computably bounded defect budget cannot.

## 5. Universal capture can be unprovable without undecidable membership

There is a second useful variation. Fix an effectively axiomatized arithmetic
theory T with a primitive-recursive proof predicate, strong enough for the
usual second incompleteness theorem. Replace unrestricted program e by the
program M_n which checks whether any integer at most n codes a T-proof of
contradiction. If none does, M_n halts after this finite check; if one does,
it loops forever. Index states by n rather than arbitrary e.

For uncapped states of this restricted system,

    H_n iff no T-proof of contradiction has code<=n.

This membership predicate is decidable by a finite proof check. Capturing
inputs also have a computable running-time and event-count majorant: every
halting M_n stops after that same finite bounded proof check. Nevertheless,

    every state captures iff Con(T).

The equivalence is formalizable in an ordinary weak arithmetic base. If T
is consistent and meets the second incompleteness hypotheses, T cannot prove
universal capture for this toy system. If T is additionally sound, its negation
cannot be proved either. Consistency alone is not being substituted for the
soundness needed for that latter assertion.

This is a concrete separation of three notions: undecidable membership,
unprovable universal termination, and false universal termination. In the
restricted model membership is decidable and the universal statement is true
under consistency, yet it is unprovable in T. In the unrestricted model
membership is c.e.-complete and the universal statement is false. Neither
construction is claimed to be physically implemented by Langton's ant.

Background theorem attribution: Kurt Gödel, *Über formal unentscheidbare Sätze
der Principia Mathematica und verwandter Systeme I*, Monatshefte38 (1931),
173–198, [publisher record](https://doi.org/10.1007/BF01700692). The publisher
record and bibliographic data were checked; its complete paywalled text was
not retrieved here. Section5 invokes the standard second-incompleteness
hypotheses explicitly, rather than claiming every conceivable proof predicate
or weak theory satisfies them.

Finite implementation controls in `check_clocked_model_controls.py/json`
pass29,478 first-event cases,29,478 exact-zero-tail cases, and3,490 overlapping
renewals. Known halting times are used only for these boundary controls; the
universal-machine separation is the analytic argument, not an experiment.
