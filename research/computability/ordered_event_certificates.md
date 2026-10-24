# Automatic ordered-event certificates, without an automatic physical clock

22 October 2026. Status: analytic certificate extension independently audited. No accepted nonstandard finite-seed ant model is known.

## Motivation

An expanding circuit can have affine side geometry in its lap number but quadratic elapsed physical time. Requiring a Presburger graph in ordinary physical time would exclude it before checking the ant rule. That restriction is unnecessary: the complete inverse check only needs the order of read events, immediate succession, and physical cell equality.

## 1. An exactly checkable clock domain of order type omega

Supply automatic (or Presburger) descriptions of a domain D subset N^d and a strict relation <_D. Require:

1. D is nonempty, and <_D is a strict linear order on D.
2. Every event has a larger event.
3. Every event has only finitely many predecessors.

The third condition is first-order expressible in the ambient numerical structure:

    for every e in D, there exists M, such that every f in D with f<_D e
    has every numerical coordinate at most M.

A subset of N^d is finite exactly when it is bounded in this sense. Thus all three requirements are decidable by automatic first-order closure. They imply that (D,<_D) has order type omega. Indeed the finite predecessor set of any element has a least element, giving the global minimum; every nonempty upper segment has a least element by taking any one of its elements and looking below it; and finite initial segments preclude an infinite block before any event.

Immediate succession is first-order definable by the absence of an intermediate event. Consequently every read event has one successor and, except at the minimum, one predecessor. The order is effectively enumerable by successive searches. This construction supplies a checked discrete physical-event clock without requiring an automatic numerical rank function e->t.

## 2. Inverse ant validation in this domain

Supply automatic or Presburger relations describing a unique physical position and heading at each e in D, using a certified automatic presentation of Z^2. Check:

- Unique total pose at every event.
- Consecutive events have one quarter-turn and its corresponding unit move.
- Consecutive visits in <_D to the same physical cell prescribe opposite R/L turns.
- The set of FIRST-L EVENTS is finite.

All conditions are first-order in the supplied automatic structure. Finiteness of the event set uses a numerical bound on its index coordinates, not a bound on physical time or on geometric distance. If the conditions hold, recover the finitely many first-L positions. These are the finite minimal initial black seed. Induction along the checked omega order proves that the specified complete path is its actual ant trajectory.

As in the automatic visit-equivalence extension, a certified cell-equality relation can replace the full position graph if the geometry and equality are established separately.

## 3. Standard104 capture remains decidable

Although ordinary clock addition need not be automatic in the event domain, fixed successor distances are first-order definable. Let S^104(e,f) denote exactly104 successor applications, a fixed finite FO formula.

Eventual standard104 is equivalent to the existence of an event e0 such that:

1. Its next104 prescribed turns equal a chosen cyclic phase of W104.
2. For all e>=e0 and f with S^104(e,f), the turns at e and f agree.

The finitely many phases can be disjoined. This is a first-order query, so standard capture and its negation are exactly decidable on every validated ordered-event certificate. No variable physical-time modulus or rank arithmetic is needed.

General eventual periodicity with an UNKNOWN period is not automatically a single FO query in this weaker clock presentation. We do not import the ordinary-time arbitrary-period decidability claim without an additional rank/addition structure.

For membership of a GIVEN finite state X, additionally bind the minimum event pose to X and require every visited cell's first-turn bit to equal its membership bit in the supplied B_X. Do not require B_X to equal the extracted minimal seed: extra initial black cells which are never visited are harmless. With an automatic position relation these initial-field compatibility conditions are first-order and decidable.

Enumerating these seed-bound finite certificates gives a c.e. class EventAuto containing all eventually periodic inputs (use the ordinary-time Presburger models). Standard capture is decidable on the promise EventAuto. Thus an undecidability proof for capture would also force histories outside this broader certificate class. A verified negative model would instead be an explicit finite-seed counterexample. Neither has been obtained.

## 4. Concrete affine expanding-loop schemas

A typical domain is

    e=(n,b,j,r),
    n>=0, b in a fixed finite block set,
    0<=j<a_b n+c_b,
    r in the finite phase set of block b,

ordered lexicographically. All fibers of a fixed n are finite and at least one block is nonempty infinitely often. Domains can be adjusted to include fixed finite corner words and finite-state phase changes n mod q. Domain validity and order type can be checked as above.

If each repeated block has restored heading, fixed displacement, and affine repeat count, each within-lap pose is affine in n,j after finitely many phase splits. If the NET LAP DISPLACEMENT is constant, the start pose of lap n is affine in n as well. Such a complete geometry has a Presburger event-indexed pose relation even though its physical duration per lap is affine and its elapsed physical time is quadratic.

This includes the natural geometry of linearly expanding rectangular circuits with constant seam displacement, once exact corner words are supplied. It does not assert that their alternating reads or finite initial black demand pass. A lap displacement that itself grows with n generally creates quadratic starting coordinates and is not covered by this affine special case without an additional representation.

There is no conflict with the theorem that ordinary-time Presburger ant space-time is equivalent to eventual periodicity. Here the event-to-physical-time rank can be nonlinear and non-Presburger. The distinction is precisely what makes this certificate language potentially useful for nonperiodic constructions.
