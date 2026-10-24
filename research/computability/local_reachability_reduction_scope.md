# What local-event undecidability would imply for finite seeds

22 October2026. Status: analytic deductions passed independent
review on22 October2026 at21:04 UTC. Dependencies are the audited exact arbitrary-period tail verifier,
constructive Presburger space-time theorem, and complete-orbit rigid-motion
reachability decider. No halting reduction has been constructed.

## 1. Eventual periodicity makes all first-order history queries decidable

Let E be the set of finite complete ant states whose future relative turn
word is eventually periodic, with arbitrary finite period. A valid periodic
tail must restore the heading and have nonzero drift; otherwise its path is
bounded, impossible for a finite seed. The exact phase-ray checker gives a
computable finite certificate for membership in E.

Suppose E contains EVERY finite state. Given an input X, dovetail simulation
and all finite proposed periodic tails until a genuine certificate is found.
The procedure terminates under the stated hypothesis. The constructive
Presburger theorem in presburger_spacetime.md then supplies formulas for

- the ant's position and heading at every nonnegative integer time;
- the complete black-cell relation at every time, including old debris;
- all finite transient states before the periodic tail.

Therefore any supplied FIRST-ORDER query of that full integer space-time
structure is decidable uniformly in X and the query. In particular this
covers reachability of a fixed finite colored pattern at the head, a pose at
a specified absolute cell, or a finite Boolean combination of such tests.
It also covers first-order recurrence statements, not only existential
reachability. This is a conditional algorithm, not proof of its totality
without the E-all hypothesis.

Consequently:

    Undecidability of a first-order local-event problem on FINITE seeds
    would force a genuinely non-eventually-periodic finite-seed orbit.

It would do more than merely exhibit an alternative periodic highway. The
standard104 conjecture implies E-all, so any such undecidability theorem
would in particular REFUTE that conjecture, not simply show it hard to prove.
Infinite periodic-background universality does not meet the finite-seed
hypothesis and supplies no such reduction.

The first-order/tail-decidable restriction matters. An arbitrary computable
predicate of the ENTIRE growing board could itself simulate an encoded
machine for a number of steps derived from the current board. Eventual
periodic geometry does not automatically decide that artificially powerful
predicate's unbounded future occurrence.

## 2. Finitely many exceptional aperiodic orbit classes still do not suffice

Let P be a fixed computable predicate of complete states satisfying:

1. P is invariant under translations and quarter rotations of the complete
   state. A pattern specified relative to the head and incoming heading is
   an example.
2. Given an exact eventual-periodic certificate, the existence of a future
   P event is decidable. First-order local predicates satisfy this condition.

Let L_P(X) mean that P(F^t X) holds for some t>=0. If the genuinely aperiodic
finite states lie in only FINITELY many complete rigid space-time orbit
classes, then L_P is recursive.

Proof. Choose representatives X_1,...,X_d of those exceptional classes.
These are finite hardcoded constants; no effective procedure for finding
them is asserted. Use the independently audited complete-orbit decider in
rigid_reachability.md to test whether X belongs to one of these classes.
If it does not, X is eventually periodic, so the certificate search and
hypothesis2 decide L_P(X).

For a fixed exceptional representative X_i, define its two-sided event set

    S_i={t in Z : P(F^t X_i)}.

If S_i is unbounded above, every time translate has a future P event. If
S_i is empty, none does. Otherwise S_i has a greatest integer s_i, and the
state at time n has a future P event exactly when n<=s_i. Thus the required
information is only one of two constant flags or one hardcoded integer.
The exact orbit decider, followed if necessary by enumeration of rigid
motions and signed times, recovers n from the given X. Rigid invariance of
P eliminates the unknown translation/rotation. This decides L_P on the
exceptional classes as well. QED.

Hence undecidability of such a covariant local event requires INFINITELY MANY
inequivalent genuinely aperiodic complete space-time orbits. The constants
in the finite-exception proof are nonuniform, but that suffices for the
computability implication. It does not give us a current practical decider.

An absolute-location target lacks rigid invariance. Translating an input
changes the target relative to its orbit, and a single complicated orbit
can then encode a nontrivial spatial visitation set. Section1 still applies
to such targets, but the finite-exception strengthening does not follow.

## 3. Compiler consequences independent of eventual periodicity

Even without any periodicity hypothesis, a computable halting reduction
into L_P cannot have all its compiled states in only finitely many rigid
space-time classes: the preceding temporal-threshold argument would decide
the reduction's entire image. Thus a genuine finite-support compiler needs
unboundedly many dynamically inequivalent complete orbits, not merely time
shifts or rigid motions of a fixed finite collection of universal traces.

This is separate from rigid_reachability.md's finite FULL accepting-template
obstruction. That earlier theorem constrains the accepting fields. This one
constrains the family of input ORBITS and allows arbitrary accepting debris,
provided the accepting predicate has the specified covariance.
