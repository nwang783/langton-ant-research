# Exact far-interface obstruction to direct capped-rail renewal

2026-10-23 06:42 UTC. New narrow consequence of the signed complete JZ tables.
An executed automatic comparison is supplied; independent review is requested.
This is not a ban on new phases, genuine remote preparation, moving controllers
or arbitrary ant behavior following these local excursions.

Let G_r,H_r be the complete prepared transport/growth operators. All have the
same input/output pose(0,0,E). Let I^G_s,I^H_s be their minimum input boards,
and R^G_s,R^H_s their complete read sets. An output can run the next operator
only if it agrees with that operator's input ON ITS READ SET. No equality is
required outside the next read set; old garbage there is explicitly ignored.

## Statement

For every source r>=0 and every target s>=1, each of the four pairs
G_r->G_s, H_r->G_s, G_r->H_s, H_r->H_s has a mismatch at one of

    (2s,0), (2s,1), (2s+1,0),

belonging to the target's read set. In particular, no direct renewal works,
even with an arbitrary parameter update s=f(r). If the target s grows
unbounded, no arbitrary repairs restricted to ONE fixed finite controller
region can hide this interface failure. Finitely many initial exceptions do
not change that conclusion.

## Complete elementary proof

The G_r output has upper black cells only at x=-2,-1, and its positive lower
black rod ends at the ODD coordinate2r-1. The H_r output has the same two
negative upper markers plus the lone positive upper cell x=2r+1, and its
positive lower black rod ends at the ODD coordinate2r+1. Their only extra
negative lower cell is x=-2.

A target G_s requires black at(2s,1). Since2s is positive and EVEN, neither
source has it: G has no positive upper black, and H's positive upper black is
at an odd coordinate. This cell belongs to R^G_s, proving both target-G cases.

A target H_s requires its lower row black through the EVEN coordinate2s, and
requires white at(2s+1,0), which is nevertheless in R^H_s. A source's positive
lower black rod ends at some odd L, possibly L=-1 for G_0. If L<2s, the source
is white at(2s,0), contradicting required black. Otherwise oddness gives
L>=2s+1, so the source is black at(2s+1,0), contradicting required white.
This proves both target-H cases. Every listed mismatch has x>=2s, escaping
any fixed finite region as s grows.

The proof uses complete endpoint boards, not just masses, and makes no
assumption about white-input axial fronts. It does not say a remote repair is
impossible; it says such a repair is genuinely necessary and cannot be replaced
by silently resetting a finite local cap.

## Executed generic comparison

`renewal_interfaces.py` starts from the image-derived macro input/output/read
relations. A generic integer-affine carry pullback permits independent target
depth s, including negative intermediate carries. For each pair it checks that
the relation of a mismatch in the three listed cells projects onto EVERY
(r,s) with s>=1. Exact automaton emptiness proves this for all binary inputs.
The mismatch automata have a finite state count recorded in
`renewal_interfaces.json`.

As an additional reusable interface test, the program separately decides for
all fixed integer offsets c whether the complete spatial union of mismatches
between source r and target r+c is bounded. The automatic first-order bounded-
repair predicate is false for every c in all four pairings. This weaker check
is superseded by the explicit arbitrary-depth lemma, but exercises the generic
bounded-local-repair decision rather than assuming full board equality.

The initial prepared boards here are exact, with no arbitrary infinite ambient
field. Finite extra controller cells are covered by the bounded-repair statement.
Nothing is asserted about a different macro family with additional endpoint
states, a translated/rotated physical port supplied by new work, or a moving
controller. No finite-seed counterexample or global capture proof results.
